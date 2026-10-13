"""Exact fixed-degree Bell--Skandera exploration. AI-generated, unreviewed.
Usage: python explore.py DEGREE
No floating point or arbitrary coefficient cutoffs.
"""
from math import comb
from itertools import count
from collections import Counter
import json, sys, time
from pathlib import Path

def kk(m,k):
    result=0
    for j in range(k,0,-1):
        lo,hi=j-1,m+j
        while lo<hi:
            mid=(lo+hi+1)//2
            if comb(mid,j)<=m: lo=mid
            else: hi=mid-1
        result+=comb(lo,j+1)
        m-=comb(lo,j)
    assert m==0
    return result

def rootfloor(a,q):
    lo,hi=0,1
    while hi**q<=a: hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**q<=a: lo=mid
        else: hi=mid
    return lo

def det(A):
    A=[r[:] for r in A]; prev=1; sign=1
    for k in range(len(A)-1):
        if not A[k][k]:
            pivot=next((i for i in range(k+1,len(A)) if A[i][k]),None)
            if pivot is None:return 0
            A[k],A[pivot]=A[pivot],A[k];sign=-sign
        v=A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                x=A[i][j]*v-A[i][k]*A[k][j]
                A[i][j],r=divmod(x,prev)
                assert r==0
            A[i][k]=0
        prev=v
    return sign*A[-1][-1]

def moments(u,maxpower):
    n=len(u)-1;c=[(-1)**j*x for j,x in enumerate(u)];p=[n]
    for s in range(1,maxpower+1):
        p.append(-sum(c[j]*p[s-j] for j in range(1,min(s,n+1)))
                 -(s*c[s] if s<=n else 0))
    return p

def run(n):
    C=[comb(n,j) for j in range(n+1)]
    report={'degree':n,'status':'exploration, unreviewed','indices':{}}
    survivors=set(); witnesses={}; started=time.time()
    for k in range(1,n):
        r=next(r for r in count(n) if comb(r,k+1)**k*C[k]**(k+1)>C[k+1]**k*comb(r+1,k)**(k+1))
        E=[m for m in range(C[k],comb(r,k)) if (kk(m,k)+1)**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1)]
        info={'threshold':r,'exceptions':E};report['indices'][k]=info
        if not E:continue
        caps=[1]+[rootfloor(C[j]**q*max(E)**p//C[k]**p,q) for j in range(1,n+1) for p,q in [( (n-j,n-k) if j<k else (j,k))]]
        info['caps']=caps
        pairs=[(m,v) for m in E for v in range(kk(m,k)+1,rootfloor(C[k+1]**k*m**(k+1)//C[k]**(k+1),k)+1)]
        info['pairs']=len(pairs);counts=Counter();order=list(range(k-1,0,-1))+list(range(k+2,n+1))
        def visit(u,pos):
            if pos==len(order):
                if any(C[j-1]*C[j+1]*u[j]**2<C[j]**2*u[j-1]*u[j+1] for j in range(1,n)):return
                counts['candidates']+=1
                key=tuple(u)
                if key not in witnesses:
                    p=moments(u,2*n-2)
                    for size in range(3,n+1):
                        value=det([[p[i+j] for j in range(size)] for i in range(size)])
                        if value<0:
                            witnesses[key]=(size,value);break
                    else:witnesses[key]=(0,0);survivors.add(key)
                counts['rejected_H'+str(witnesses[key][0])]+=1
                return
            j=order[pos]
            if j<k: upper=min(caps[j],C[j]*C[j+2]*u[j+1]**2//(C[j+1]**2*u[j+2]))
            else: upper=min(caps[j],C[j-2]*C[j]*u[j-1]**2//(C[j-1]**2*u[j-2]))
            for value in range(C[j],upper+1):
                u[j]=value;visit(u,pos+1)
        for m,v in pairs:
            u=[0]*(n+1);u[0]=1;u[k]=m;u[k+1]=v;visit(u,0)
        info['counts']=dict(counts)
        print(k,info,flush=True)
    report['distinct_candidates']=len(witnesses)
    report['survivors']=sorted(survivors)
    report['elapsed_seconds']=time.time()-started
    out=Path(__file__).parent
    (out/f'degree{n}_results.json').write_text(json.dumps(report,indent=2))
    (out/f'degree{n}_witnesses.json').write_text(json.dumps([[list(u),q,v] for u,(q,v) in sorted(witnesses.items())]))
    print('DONE',n,'distinct',len(witnesses),'survivors',len(survivors),'seconds',report['elapsed_seconds'],flush=True)
    return report

if __name__=='__main__':run(int(sys.argv[1]))
