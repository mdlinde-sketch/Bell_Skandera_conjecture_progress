#!/usr/bin/env python3
"""Independent exact coefficient and KK checks for 2026-11-01 unit-norm theorem.
The mathematical classification relies on Smyth 1984, not on these controls.
"""
from math import comb
from functools import lru_cache
import json

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power(a,n):
    b=[1]
    for _ in range(n):b=mul(b,a)
    return b

@lru_cache(None)
def D(k,m):
    if m==0:return 0
    if k==1:return 1
    r=k
    while comb(r+1,k)<=m:r+=1
    return comb(r,k-1)+D(k-1,m-comb(r,k))

def main():
    families={"A":[1,4,1],"B":[1,5,6,1],"C":[1,6,11,6,1]}
    checked=0
    for d in range(4,251):
        for name,g in families.items():
            a=mul(power([1,1],d-(len(g)-1)),g)
            assert len(a)==d+1 and a[0]==a[-1]==1
            assert a[1]==d+2
            assert a[2]==comb(d,2)+2*d-(4 if name=='A' else 3)
            assert (a[-2]==d+2 if name!='B' else a[-2]==d+3)
            assert D(d-1,a[-2])<=a[-3]
            checked+=1
    d=28
    assert D(27,30)==429
    assert comb(d,2)+2*d-4==430
    assert {comb(d,2)+2*d-4,comb(d,2)+2*d-3}=={430,431}
    print(json.dumps({"date":"2026-11-01","status":"PASS","families":3,
      "degrees":"4..250","exact_family_controls":checked,
      "d28_a26_allowed":[430,431],"d28_a26_partial_example":428,
      "d28_KK_shadow":429,"conditional_input":"Smyth 1984 strict trace theorem"},indent=2))
if __name__=='__main__':main()
