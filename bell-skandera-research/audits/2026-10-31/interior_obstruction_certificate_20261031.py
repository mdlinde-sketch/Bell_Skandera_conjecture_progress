#!/usr/bin/env python3
"""Exact rational proof controls, 31 October 2026. Not Bell-Skandera counterexample."""
from fractions import Fraction as Q
from math import comb
from functools import lru_cache
import json

@lru_cache(None)
def shadow(k,m):
    if m==0:return 0
    if k==1:return 1
    r=k
    while comb(r+1,k)<=m:r+=1
    return comb(r,k-1)+shadow(k-1,m-comb(r,k))

def main():
    lo,hi=Q(189,200),Q(473,500)
    H=lambda y:y**26*(428-780*y+351*y*y)-1
    assert H(lo)<0<H(hi)
    # x+z=30-26*y; x*z=y**(-26). Discriminant positive.
    assert (30-26*hi)**2-4/lo**26>0
    assert 30-26*hi>0
    # F(t)=(t+x)(t+z)(t+y)^26: a0=1, a28=1,
    # a27=30, a26=428, but a1 is provably noninteger.
    low=26/hi+(30-26*hi)*lo**26
    high=26/lo+(30-26*lo)*hi**26
    assert Q(28)<low<high<Q(29)
    assert shadow(27,30)==429 and shadow(28,1)==28
    base=0
    for k in range(3,201):
        for m in range(1,k+1):
            assert shadow(k,m)==k*m-comb(m,2)
            assert (shadow(k,m)-1)**k<k**k*m**(k-1)
            base+=1
    margins=[]
    for r in (4,5,6):
        A,B=comb(r,3),comb(r,2)
        for q in (1,B-1):
            margin=27*(A+q)**2-(B+q)**3
            assert margin>0
            margins.append((r,q,margin))
    boundaries=0
    for k in range(2,121):
        for r in (k,k+1,k+2,k+3,k+8,k+21,k+55):
            A=comb(r,k)
            for m in (max(1,A-1),A,A+1,A+comb(r,k-1)-1):
                assert (shadow(k,m)-1)**k<k**k*m**(k-1)
                boundaries+=1
    print(json.dumps(dict(status="PASS",date="2026-10-31",
        y_bracket=[str(lo),str(hi)],H_signs=["negative","positive"],
        a0=1,a28=1,a27=30,a26=428,D27_30=429,D28_1=28,
        a1_noninteger=True,base_controls=base,boundary_controls=boundaries,
        k3_margins=margins,
        warning="NOT a Bell-Skandera counterexample; other coefficients nonintegral"),indent=2))
if __name__=="__main__":main()
