#!/usr/bin/env python3
"""Independent exact checks; proof in NONUNIT_TRACE_BOUNDARY_2026_11_01.md.
No finite computation proves an all-degree assertion. Standard library only."""
from math import comb
from fractions import Fraction
import json

def C(n,k): return comb(n,k) if 0 <= k <= n else 0

def shadow(k,m):
    if m == 0: return 0
    if k == 1: return 1
    r = k
    while C(r+1,k) <= m: r += 1
    return C(r,k-1) + shadow(k-1,m-C(r,k))

def multiply(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return c

def family(d):
    f = [1]
    for _ in range(d-1): f=multiply(f,[1,1])
    return multiply(f,[1,2])

def kk(f):
    return all(shadow(k,f[k]) <= f[k-1] for k in range(1,len(f)))

def main():
    exceptions=((1,1),(1,3,1),(1,5,6,1),(1,7,13,7,1),(1,7,14,8,1))
    assert all(kk(e) and kk(e[::-1]) for e in exceptions)
    n = 0
    samples=0
    for d in range(2,251):
        assert d**d*2**(d-1)>(2*d-2)**d  # norm>=2 barrier
        assert d**d*3**(d-1)>(2*d-1)**d  # equality excludes norm>=3
        f=family(d)
        assert f[-1]==2 and f[-2]==2*d-1 and f[-3]==(d-1)**2
        assert shadow(d-1,2*d-1)==(d-1)**2 and kk(f)
        # Newton upper bound for the penultimate coefficient.
        assert (2*d-1)**2*(d-1)<4*d*((d-1)**2+1)
        # B_N(x)=(x-1)(x-2)^(d-1), compare all coefficients exactly.
        b=[0]*(d+1)
        for j in range(d):
            v=C(d-1,j)*(-2)**j
            b[j]+=v
            b[j+1]-=v
        for j in range(d+1):
            assert b[j] == (1 if j==0 else (-1)**j*2**(j-1)*f[d-j])
        for p in range(1,20):
            x=Fraction(p,20)
            ratio=x*((Fraction(2*d-1)-x)/Fraction(2*(d-1)))**(d-1)
            assert ratio<1
            samples+=1
        n+=1
    # Exact low-reverse-excess norm>1 calculations at d=4.
    assert 7**4 >= 4**4*2**3 and 7**4 < 4**4*3**3
    assert 8**4 < 6**4*2**2 <= 9**4
    assert 6*49 >= 16*9*2 and 6*49 < 16*10*2
    assert 4**4 < 4**4*2 <= 5**4
    assert 16*81 >= 36*5*7 and 16*81 < 36*6*7
    assert family(4)==[1,5,9,7,2]
    assert shadow(3,2)==5 and shadow(2,5)==4
    print(json.dumps(dict(status="PASS",tested_degrees=n,
                          tested_rational_root_boundaries=samples,
                          corrected_exception_orientations=len(exceptions),
                          formal_proof="see referenced mathematical audit"),indent=2))
if __name__=="__main__":main()
