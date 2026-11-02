#!/usr/bin/env python3
"""Independent exact rational controls; symbolic proof in 2 Nov audit."""
from fractions import Fraction as Q
from math import comb
import json

def log_bounds(x, terms=30):
    assert x > 0
    z=(x-1)/(x+1)
    s=Q(0)
    for j in range(terms):
        s+=2*z**(2*j+1)/Q(2*j+1)
    rem=2*abs(z)**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return s-rem,s+rem

def root_bounds():
    lo=Q(3605,1000); hi=Q(3606,1000)
    assert lo*lo<13<hi*hi
    return ((5-hi)/3,(5-lo)/3),((5+lo)/3,(5+hi)/3)

def min_g_lower(lo,hi):
    assert 0<lo<hi and not(lo<=1<=hi)
    dist_hi = (1-lo) if hi<1 else (hi-1)
    return 1/hi+Q(3,2)*log_bounds(lo)[0]-Q(3,4)*log_bounds(dist_hi)[1]

def poly_mult(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def shadow(k,m):
    if m==0:return 0
    if k==1:return 1
    r=k
    while comb(r+1,k)<=m:r+=1
    return comb(r,k-1)+shadow(k-1,m-comb(r,k))

def kk(f):
    return all(shadow(k,f[k])<=f[k-1] for k in range(1,len(f)))

def norm_two_families(d):
    assert d>=2
    f=[1]
    for _ in range(d-2):f=poly_mult(f,[1,1])
    return poly_mult(f,[1,4,2]),poly_mult(f,[1,5,2])

def main():
    intervals=root_bounds()
    g_lowers=[min_g_lower(*interval) for interval in intervals]
    assert all(x>Q(29,20) for x in g_lowers)
    log2_low,log2_hi=log_bounds(Q(2))
    assert log2_hi<Q(7,10)
    assert Q(3,2)*log2_hi<Q(21,20)
    assert Q(20,9)*(Q(-1,2)+Q(21,20))<2
    assert Q(20,9)*Q(21,20)<3
    assert Q(20,9)*(Q(1,2)+Q(21,20))<4
    discs={a:-8*a**3+49*a*a+252*a-1480 for a in range(5,9)}
    assert discs=={5:5,6:68,7:-59,8:-424}
    a5=[1,5,7,2]
    a6=[1,6,7,2]
    assert a5==poly_mult([1,2],[1,3,1])
    assert a6==poly_mult([1,1],[1,5,2])
    assert kk(a5) and kk(a6)
    count=0
    for d in range(2,251):
        f0,f1=norm_two_families(d)
        assert f0[-1]==2 and f0[-2]==2*d and f0[-3]==d*d-d-1
        assert f1[-1]==2 and f1[-2]==2*d+1 and f1[-3]==d*d-3
        if d<=80: assert kk(f0) and kk(f1)
        if d>=3:
            f2=[1]
            for _ in range(d-3):f2=poly_mult(f2,[1,1])
            f2=poly_mult(f2,[1,5,7,2])
            assert f2[-1]==2 and f2[-2]==2*d+1 and f2[-3]==d*d-4
            if d<=80: assert kk(f2)
        count+=1
    print(json.dumps({"status":"PASS","pointwise_stationary_intervals":2,
      "pointwise_margin_lower_units_1e_5":[int(100000*(x-Q(29,20))) for x in g_lowers],
      "log2_upper_below_7_10":True,"degree3_discriminants":discs,
      "norm2_degree_controls":count,"arithmetic":"exact rational and integer"},indent=2))
if __name__=='__main__':main()
