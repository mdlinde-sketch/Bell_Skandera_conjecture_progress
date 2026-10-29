#!/usr/bin/env python3
"""Finite controls for structural arguments; not an unrestricted proof."""
import json
from math import comb
from audit_exact import shadow, sturm_positive

def path(n):
    a,b=[1],[1]
    for _ in range(2,n+1):
        c=b+[0]
        for j,v in enumerate(a):c[j+1]+=v
        while c[-1]==0:c.pop()
        a,b=b,c
    return b

rows=[]
for p in [5,7,11,13,17,19,23,29,31]:
    d=(p-1)//2
    a=[comb(2*d-j,j) for j in range(d+1)]
    assert a==path(2*d)
    P=[(-1)**(d-j)*a[d-j] for j in range(d+1)]
    assert sturm_positive(P)==d
    assert a[1]==2*d-1 and a[-1]==1
    assert all(shadow(j,a[j])<=a[j-1] for j in range(2,d+1))
    rows.append({'p':p,'degree':d,'excess':d-1,'norm':1,'positive_roots':d})
tests=0
for d in range(2,81):
    for m in range(1,501):
        assert (shadow(d,m)-1)**d<d**d*m**(d-1),(d,m)
        tests+=1
print(json.dumps({'prime_family_controls':rows,'terminal_scalar_candidate':{
    'tests':tests,'degree_range':[2,80],'m_range':[1,500],
    'status':'NO FAILURE IN FINITE RANGE; UNIVERSAL STATEMENT UNPROVED'},
    'status':'PASS'},indent=2))
