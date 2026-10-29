#!/usr/bin/env python3
"""Independent exact audit; Python 3 standard library only, no repository imports.
Run: python audit_exact.py > audit_results.json
Proof scope and derivations are in AUDIT.md. No unrestricted conjecture claim.
"""
from math import comb
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache
import json

def trim(p):
    while p and p[-1] == 0: p.pop()
    return p

def remainder(a,b):
    a=list(map(Q,a)); b=list(map(Q,b))
    while a and len(a)>=len(b):
        z=a[-1]/b[-1]; j=len(a)-len(b)
        for i,v in enumerate(b): a[i+j]-=z*v
        trim(a)
    return a

def sturm_positive(p):
    seq=[list(map(Q,p)), [Q(i)*p[i] for i in range(1,len(p))]]
    while seq[-1]:
        r=remainder(seq[-2],seq[-1])
        if not r: break
        seq.append([-x for x in r])
    def variations(v):
        v=[1 if x>0 else -1 for x in v if x]
        return sum(a!=b for a,b in zip(v,v[1:]))
    return variations([p[0] for p in seq])-variations([p[-1] for p in seq])

@lru_cache(None)
def shadow(k,m):
    """Minimum (k-1)-faces forced by m k-faces: downward KK operator."""
    ans=0; cap=m+k
    for j in range(k,0,-1):
        if not m: break
        lo=j-1; hi=cap
        while lo+1<hi:
            mid=(lo+hi)//2
            if comb(mid,j)<=m: lo=mid
            else: hi=mid
        ans+=comb(lo,j-1); m-=comb(lo,j); cap=lo
    assert m==0
    return ans

def det(a):
    n=len(a); total=0
    for p in permutations(range(n)):
        z=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n): z*=a[i][p[i]]
        total+=z
    return total

def moments(a,d):
    p=[d]
    for k in range(1,len(a)):
        p.append(sum((-1)**(j-1)*a[j]*p[k-j] for j in range(1,k))
                 +(-1)**(k-1)*k*a[k])
    return p

def cap(d,n,k): return comb(d,k)*n**k//d**k

def next_cap(d,n,a):
    k=len(a)
    # Simplified Newton ratio, derived independently of binomial products.
    return min(cap(d,n,k), a[-1]**2*(k-1)*(d-k+1)//(a[-2]*k*(d-k+2)))

def small_cases():
    out=[]
    for d in range(4,8):
        for n in range(17719*d//10000+1,d+7):
            counts={'prefixes':0,'H3_negative':0,'H3_nonnegative':0,'a5_tests':0}
            # All terminal pairs certified by Maclaurin and downward KK.
            for m in range(1,cap(d,n,d)+1):
                required=shadow(d,m)
                assert (required-1)**d < comb(d,d-1)**d*m**(d-1)
            for b in range(comb(d,2),next_cap(d,n,[1,n])+1):
                assert shadow(2,b)<=n
                for c in range(comb(d,3),next_cap(d,n,[1,n,b])+1):
                    for e in range(comb(d,4),next_cap(d,n,[1,n,b,c])+1):
                        counts['prefixes']+=1
                        a=[1,n,b,c,e]; p=moments(a,d)
                        h=det([[p[i+j] for j in range(3)] for i in range(3)])
                        if h<0:
                            counts['H3_negative']+=1; continue
                        counts['H3_nonnegative']+=1
                        assert shadow(3,c)<=b and shadow(4,e)<=c,(d,n,a)
                        if d==4: continue
                        hi=next_cap(d,n,a)
                        if hi<comb(d,5): continue
                        assert shadow(5,hi)<=e,(d,n,a,hi)
                        if d<=6: continue # terminal pair already certified
                        for f in range(comb(d,5),hi+1):
                            counts['a5_tests']+=1
                            hi6=next_cap(d,n,a+[f])
                            if hi6>=comb(d,6):
                                assert shadow(6,hi6)<=f,(d,n,a,f,hi6)
            out.append(dict(d=d,n=n,**counts))
    return out

def controls():
    # Downward operator tested independently against actual colex shadows.
    from itertools import combinations
    tests=0
    for k in range(2,5):
        faces=sorted(combinations(range(9),k),key=lambda x:tuple(reversed(x)))
        lower=set()
        for m,f in enumerate(faces,1):
            lower.update(combinations(f,k-1))
            assert shadow(k,m)==len(lower)
            tests+=1
    # Exact finite part of the analytic cubic lemma, with integer rounding.
    cubic=[]
    for m in range(3,15):
        h=0
        while 27*(h+1)**2<=m**3: h+=1
        assert shadow(3,h)<=m
        cubic.append([m,h,shadow(3,h)])
    corrected=[(1,1),(1,3,1),(1,5,6,1),(1,7,13,7,1),(1,7,14,8,1)]
    exceptions=[]
    for a in corrected:
        d=len(a)-1
        # x^d F(-1/x), ascending coefficients
        p=[(-1)**(d-j)*a[d-j] for j in range(d+1)]
        assert sturm_positive(p)==d
        assert all(shadow(k,a[k])<=a[k-1] for k in range(2,d+1))
        exceptions.append({'coefficients':a,'positive_roots':d,'excess':a[1]-d})
    # The two missing exceptions refute the old residual-degree bound.
    for a in [corrected[2],corrected[4]]:
        d=len(a)-1; s=a[1]-d
        assert 10000*a[1]<17719*d and 7719*d>=10000*s
        # Irreducibility mod 2: divide by all possible monic factors up to d/2.
        poly=sum((a[j]%2)<<j for j in range(d+1))
        for k in range(1,d//2+1):
            for divisor in range(1<<k,1<<(k+1)):
                r=poly
                while r.bit_length()>=divisor.bit_length():
                    r ^= divisor << (r.bit_length()-divisor.bit_length())
                assert r!=0
    return {'colex_controls':tests,'cubic_rounding_table':cubic,'corrected_exceptions':exceptions}

if __name__=='__main__':
    print(json.dumps({'controls':controls(),'small_excess':small_cases(),'status':'PASS'},indent=2))
