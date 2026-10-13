"""Separate stdlib degree-8 check: reverse enumeration, down-shadows,
companion-matrix traces and permutation determinants. AI-generated/unreviewed.
Does not import the exploration implementation.
"""
from math import comb
from itertools import permutations
from collections import Counter
from pathlib import Path
import json,time

BASE=Path(__file__).parent
N=8;C=[comb(N,j) for j in range(N+1)]
def down(m,k):
    total=0;upper=m+k
    for j in range(k,0,-1):
        r=j-1
        while r+1<upper and comb(r+1,j)<=m:r+=1
        total+=comb(r,j-1) if r>=j else 0
        m-=comb(r,j);upper=r
    assert m==0
    return total

def companion_traces(u,maxpower):
    # Multiply each column by the companion matrix, using its sparse form.
    last=[-(-1)**(N-i)*u[N-i] for i in range(N)]
    A=[[int(i==j) for j in range(N)] for i in range(N)]
    traces=[N]
    for power in range(maxpower):
        A=[[last[i]*A[N-1][j]+(A[i-1][j] if i else 0) for j in range(N)] for i in range(N)]
        traces.append(sum(A[i][i] for i in range(N)))
    return traces

PERMS={q:[(p,(-1)**sum(p[i]>p[j] for i in range(q) for j in range(i+1,q))) for p in permutations(range(q))] for q in (3,4,5)}
def determinant(p,q):
    result=0
    for perm,sign in PERMS[q]:
        value=sign
        for i,j in enumerate(perm):value*=p[i+j]
        result+=value
    return result

def main():
    started=time.time()
    primary=json.loads((BASE/'degree8_results.json').read_text())
    saved={tuple(u):(q,v) for u,q,v in json.loads((BASE/'degree8_witnesses.json').read_text())}
    seen=set();counts=Counter();hists={};intervals=0
    for k in range(1,N):
        r=N
        while comb(r,k+1)**k*C[k]**(k+1)<=C[k+1]**k*comb(r+1,k)**(k+1):r+=1
        pairs=[];E=[]
        # Invert the lower shadow, independently of the upper-shadow formula.
        v=0
        for m in range(C[k],comb(r,k)):
            while down(v+1,k+1)<=m:v+=1
            intervals+=1
            nxt=v+1
            if nxt**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1):E.append(m)
            while nxt**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1):pairs.append((m,nxt));nxt+=1
        expected=primary['indices'][str(k)]
        assert r==expected['threshold'] and E==expected['exceptions']
        if not E:continue
        caps=[1]
        for j in range(1,N+1):
            p,q=(N-j,N-k) if j<k else (j,k)
            cap=C[j]
            while (cap+1)**q*C[k]**p<=C[j]**q*max(E)**p:cap+=1
            caps.append(cap)
        assert caps==expected['caps'] and len(pairs)==expected['pairs']
        # Extend right first, then left, unlike the primary program.
        order=list(range(k+2,N+1))+list(range(k-1,0,-1))
        hist=Counter()
        def visit(u,pos):
            if pos==len(order):
                key=tuple(u);counts[k]+=1;seen.add(key)
                assert key in saved
                hist[saved[key][0]]+=1
                return
            j=order[pos]
            maximum=caps[j]
            if j>k:maximum=min(maximum,C[j-2]*C[j]*u[j-1]**2//(C[j-1]**2*u[j-2]))
            else:maximum=min(maximum,C[j]*C[j+2]*u[j+1]**2//(C[j+1]**2*u[j+2]))
            for value in range(C[j],maximum+1):
                u[j]=value
                if all(u[s-1] is None or u[s] is None or u[s+1] is None or u[s]**2*C[s-1]*C[s+1]>=u[s-1]*u[s+1]*C[s]**2 for s in range(1,N)):
                    visit(u,pos+1)
            u[j]=None
        for m,v in pairs:
            u=[None]*(N+1);u[0]=1;u[k]=m;u[k+1]=v;visit(u,0)
        assert counts[k]==expected['counts']['candidates']
        hists[k]=dict(hist)
        print('Enumeration verified',k,counts[k],flush=True)
    assert seen==set(saved)
    # Exact witness audit with an unrelated determinant algorithm and trace construction.
    for index,(u,(q,value)) in enumerate(saved.items(),1):
        p=companion_traces(u,2*q-2)
        assert determinant(p,q)==value<0,(u,q,value)
        if q==5:assert determinant(p,3)>=0 and determinant(p,4)>=0
        if index%20000==0:print('Witnesses verified',index,flush=True)
    result={'degree':N,'distinct_vectors_verified':len(seen),'counts':dict(counts),'witness_sizes_by_index':hists,'finite_shadow_values_checked':intervals,'all_exact_witnesses_match':True,'elapsed_seconds':time.time()-started}
    (BASE/'degree8_crosscheck.json').write_text(json.dumps(result,indent=2))
    print('PASS',result,flush=True)

if __name__=='__main__':main()
