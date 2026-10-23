"""Exact arithmetic regression for the arbitrary-norm reciprocal Smyth-factor lemma.
No external packages. This is a test, not a proof of Smyth's theorem.
"""
from fractions import Fraction
from itertools import product

EXCEPTIONS={
    "x-1":[1,1],
    "x2-3x+1":[1,3,1],
    "x3-5x2+6x-1":[1,5,6,1],
    "x4-7x3+13x2-7x+1":[1,7,13,7,1],
    "x4-7x3+14x2-8x+1":[1,7,14,8,1],
}

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def monic_division(a,b):
    assert b[-1]==1
    rem=list(a)
    quotient=[0]*max(0,len(a)-len(b)+1)
    while len(rem)>=len(b):
        c=rem[-1];k=len(rem)-len(b);quotient[k]=c
        for j,v in enumerate(b):rem[j+k]-=c*v
        while rem and rem[-1]==0:rem.pop()
    return quotient,rem

def reciprocal_polynomial(f):
    d=len(f)-1;N=f[-1]
    out=[0]*(d+1);out[-1]=1
    for j in range(1,d+1):out[d-j]=(-1)**j*N**(j-1)*f[d-j]
    return out

def exceptional_polynomial(f):
    d=len(f)-1
    return [(-1)**(d-i)*f[d-i] for i in range(d+1)]

def audit():
    E={name:exceptional_polynomial(f) for name,f in EXCEPTIONS.items()}
    checks=hits=nonunit=0
    for d in range(1,9):
        for roots in product((1,2,3),repeat=d):
            f=[1]
            for root in roots:f=mul(f,[1,root])
            N=f[-1];b=reciprocal_polynomial(f)
            direct=[Fraction(1)]
            for root in roots:direct=mul(direct,[-Fraction(N,root),Fraction(1)])
            assert b==direct
            for name,e in E.items():
                checks+=1
                _,remainder=monic_division(b,e)
                if not remainder:
                    hits+=1
                    if N>1:
                        nonunit+=1
                        assert name=="x-1"
                        assert sum(c*(-1)**j*N**(d-j) for j,c in enumerate(f))==0
    # Exercise all five exceptional factors explicitly in norm-one examples.
    for name,vec in EXCEPTIONS.items():
        for r in range(3):
            f=list(reversed(vec))
            for _ in range(r):f=mul(f,[1,1])
            assert f[-1]==1
            _,remainder=monic_division(reciprocal_polynomial(f),E[name])
            assert not remainder,(name,r)
    assert (checks,hits,nonunit)==(49200,80,72)
    print("PASS",checks,"factor checks;",nonunit,"nonunit hits all x-1;",
          "15 unit-norm exceptional-factor controls")

if __name__=="__main__":audit()
