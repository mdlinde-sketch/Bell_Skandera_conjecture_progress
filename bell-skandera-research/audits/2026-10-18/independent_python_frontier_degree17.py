"""Independent pure-Python degree-16 frontier coverage certificate.

Instead of iterating all 18.4m candidate adjacent pairs or importing the C++
residual list, partition *all m* into intervals and certify entire rectangles
using monotonic bounds. Exact integer Maclaurin root, canonical KK shadow and
log-concavity inequalities; no floats or external case lists.

It verifies completeness of the *survivor case list*, not the raw-pair count.
"""
from bisect import bisect_right
from collections import Counter
from math import comb
import json,sys,time

D=17
CH=[[comb(a,i) if a>=i else 0 for a in range(65)] for i in range(18)]

def kth_root_floor(n,k):
    if n==0:return 0
    lo,hi=0,1<<((n.bit_length()+k-1)//k)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return lo

def max_n(d,k,m):
    numerator=comb(d,k+1)**k*m**(k+1)
    denominator=comb(d,k)**(k+1)
    return kth_root_floor(numerator//denominator,k)

def kk_next(k,m):
    total=0
    cap=65
    for i in range(k,0,-1):
        a=bisect_right(CH[i],m,i,cap)-1
        if a>=i:
            m-=CH[i][a]
            total+=CH[i+1][a]
        cap=a
    assert m==0
    return total

def max_coeff(d,k,m,n,j):
    if j==k:return m
    if j==k+1:return n
    if j<k:
        a=k+1-j
        b=k-j
        return comb(d,j)*m**a*comb(d,k+1)**b//(comb(d,k)**a*n**b)
    a=j-k
    b=j-k-1
    return comb(d,j)*n**a*comb(d,k)**b//(comb(d,k+1)**a*m**b)

def cutoff(d,k):
    r=d
    while comb(r,k+1)**k*comb(d,k)**(k+1) <= comb(d,k+1)**k*comb(r+1,k)**(k+1):r+=1
    return r

def independent(d=16,verbose=True):
    assert 2 <= d <= 17, "This audited binomial table covers degrees 2 through 17 only"
    start=time.time()
    stats=Counter()
    by_k={}
    residual=[];special=[]
    for k in range(1,d):
        L,H=comb(d,k),comb(cutoff(d,k),k)-1
        stack=[(L,H)]
        local=Counter()
        while stack:
            a,b=stack.pop()
            local['blocks']+=1
            nlo=kk_next(k,a)+1
            nhi=max_n(d,k,b)
            if nlo>nhi:
                local['no_pair_blocks']+=1
                continue
            if 10000*max_coeff(d,k,b,nlo,1)<=17719*d:
                local['trace_certified_blocks']+=1
                continue
            if a<b:
                mid=(a+b)//2
                stack.append((mid+1,b));stack.append((a,mid))
                continue
            local['m_explicit']+=1
            for n in range(nlo,nhi+1):
                local['n_explicit']+=1
                if 10000*max_coeff(d,k,a,n,1)<=17719*d:
                    local['trace_individual']+=1
                    continue
                ud=max_coeff(d,k,a,n,d)
                if ud<1:
                    local['no_norm']+=1
                    continue
                um=max_coeff(d,k,a,n,d-1)
                if ud>=3:
                    special.append([k,a,n,ud,um]);local['special_norm3']+=1
                    continue
                if 10000*um>17719*d:
                    residual.append([k,a,n,ud,um]);local['residual_norm1']+=1
                else:local['trace_reverse']+=1
                if ud>=2 and 10*um+30>=29*d:
                    special.append([k,a,n,ud,um]);local['special_norm2']+=1
        by_k[k]=dict(local)
        stats.update(local)
        if verbose:print('k=',k,dict(local),'elapsed',round(time.time()-start,2),flush=True)
    return {'degree':d,'counts':dict(stats),'by_k':by_k,'residual':residual,'suspect':special}

if __name__=='__main__':
    d=int(sys.argv[1]) if len(sys.argv)>1 else 16
    output=independent(d)
    path=f'python_independent_frontier_degree{d}.json'
    with open(path,'w') as f:json.dump(output,f,indent=2)
    print('RESULT',len(output['residual']),len(output['suspect']),output['counts'])
