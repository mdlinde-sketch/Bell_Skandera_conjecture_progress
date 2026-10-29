#!/usr/bin/env python3
"""Exact controls for the all-order identity in AUDIT.md; standard library."""
import json, random
from audit_exact import moments, det

def bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a)
    if n==0:return 1
    sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def hankel(p,r):return [[p[i+j] for j in range(r)] for i in range(r)]

def check(d,a,r,t,s):
    p=moments(a,d); matrix=hankel(p,r)
    hr=bareiss(matrix); hm=bareiss(hankel(p,r-1))
    v=p[r:2*r]
    adjlast=[]
    for j in range(r):
        minor=[[matrix[i][k] for k in range(r-1)] for i in range(r) if i!=j]
        adjlast.append((-1)**(j+r-1)*bareiss(minor))
    slope=2*r*a[1]*hr-2*(2*r-1)*sum(x*y for x,y in zip(adjlast,v))
    base=bareiss(hankel(p,r+1))
    b=a[:];b[2*r-1]+=t;b[2*r]+=s
    direct=bareiss(hankel(moments(b,d),r+1))
    assert direct==base+slope*t-(2*r-1)**2*hm*t*t-2*r*hr*s
    if r<=4: assert base==det(hankel(p,r+1))
    return hr==0

def main():
    rng=random.Random(20261029); cases=0; singular=0
    for r in range(2,8):
        for _ in range(60):
            a=[1]+[rng.randint(-12,20) for _ in range(2*r)]
            singular+=check(rng.randint(1,30),a,r,rng.randint(-7,9),rng.randint(-7,9));cases+=1
        # Genuine positive roots with repeated roots make singular Hankel blocks.
        for d in range(2*r,2*r+3):
            from math import comb
            a=[comb(d,j)*2**j for j in range(2*r+1)]
            singular+=check(d,a,r,3,5);cases+=1
    print(json.dumps({'identity_controls':cases,'singular_blocks':singular,'status':'PASS'},indent=2))
if __name__=='__main__':main()
