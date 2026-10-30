#!/usr/bin/env python3
"""2026-10-30 exact independent regression for ALL-ORDER terminal KK theorem.
The mathematical proof is in TERMINAL_KK_PROOF_2026-10-30.md.
No unrestricted Bell-Skandera proof, novelty, or formal verification claimed.
"""
from functools import lru_cache
from math import comb
from random import Random
import json

@lru_cache(None)
def shadow(k,m):
    if m==0:return 0
    if k==1:return 1
    lo,hi=k,k+1
    while comb(hi,k)<=m:hi*=2
    while lo+1<hi:
        t=(lo+hi)//2
        if comb(t,k)<=m:lo=t
        else:hi=t
    return comb(lo,k-1)+shadow(k-1,m-comb(lo,k))

def ok(k,m):
    return (shadow(k,m)-1)**k < k**k*m**(k-1)

def run():
    small=[]
    for r in (4,5,6):
        A,B=comb(r,3),comb(r,2)
        margins=[(27*(A+q)**2-(B+shadow(2,q)-1)**3,q) for q in range(1,B)]
        assert min(margins)[0]>0
        small.append((r,len(margins),min(x for x,q in margins)))
    ratio=0
    for k in range(4,101):
        for r in range(k+1,k+21):
            A,B=comb(r,k),comb(r,k-1)
            assert B**k<=(k-1)**k*A**(k-1)
            ratio+=1
    for r in range(7,100):
        assert comb(r,2)**3<=8*comb(r,3)**2
        ratio+=1
    n=0
    for k in range(2,101):
        for m in range(1,2001):
            assert ok(k,m),(k,m)
            n+=1
    rng=Random(20261030)
    nr=0
    for k in range(2,251):
        for z in range(25):
            m=rng.randrange(1,10**rng.randint(2,24))
            assert ok(k,m),(k,m)
            nr+=1
    assert shadow(10,2)**10>10**10*2**9
    assert shadow(10,3)**10>10**10*3**9
    roots_tests=0
    for d in range(2,26):
        for z in range(20):
            a=[1]
            for root in (rng.randrange(1,5) for _ in range(d)):
                b=[0]*(len(a)+1)
                for i,v in enumerate(a):
                    b[i]+=v;b[i+1]+=root*v
                a=b
            assert a[-2]>=shadow(d,a[-1])
            roots_tests+=1
    print(json.dumps(dict(status='PASS',k3_base=small,ratio_controls=ratio,
       scalar_exact_grid=n,scalar_exact_random=nr,positive_integer_root_polynomials=roots_tests,
       false_no_ceiling_examples=[(10,2),(10,3)]),indent=2))

if __name__=='__main__':run()
