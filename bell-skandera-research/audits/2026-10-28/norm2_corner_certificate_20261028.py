"""28 Oct 2026: independent 74-corner norm-two Hankel certificate.

Mathematical input: For each (d,k,m,n) with k=d-2 and norm N=2,
write a_j=u_(d-j), so a1=n, a2=m. Newton/Maclaurin bounds give
  a3 >= L3(m), a4 >= L4(a3) >= L4(L3(m)).
The scaled reciprocal Hankel determinant H3(d,n,m,a3,a4) satisfies
  dH3/da4 = -32 H2, H2=d*(n*n-4*m)-n*n,
  dH3/da3 = -8*S(a3),
  S(a3)=36*d*a3 -10*d*m*n + d*n**3 +12*m*n - n**3.
For the 74 input rows H2>0 and S(L3)>0. As S increases with a3,
H3 strictly decreases in BOTH variables on the entire admissible region.
Thus H3 <= H3(L3,L4(L3)) <0, contradicting PSD.

Independent direct 3x3 Leibniz determinant; no prior H3 envelope imports,
no quadratic maximization and no floating-point arithmetic. The rows are
UNTRUSTED inputs checked against fixed hashes and algebraic constraints.
This is a finite branch certificate, NOT an all-degree theorem.
"""
from __future__ import annotations
import hashlib
import json
from itertools import permutations
from math import comb
from pathlib import Path
import random
import sys

EXPECTED = {
  14: ('85f4374cc8bbebb5b73b6691a77b0927dab91817ba098f22d7f27801f022f5eb',4),
  15: ('9aef47ba87c1c4e5ca5c736dba236869656abcd63e1849f78c28b4552f69b055',11),
  16: ('bcd58517824add03c7cf448b0c101066989227471f781b872c4bb444627628ab',22),
  17: ('48f93be87cc5fc15fc6ba20d104630633a35466d114462459be6cee5754763b7',37),
}


def ceil_integer_root_ratio(num: int, den: int, power: int) -> int:
    assert num>=0 and den>0 and power>=1
    lo,hi=0,1
    while den*hi**power<num:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if den*mid**power>=num:hi=mid
        else:lo=mid
    return hi


def chord(d: int,j: int,prev: int) -> int:
    r=d-j+1
    return ceil_integer_root_ratio(prev**(r-1)*comb(d,j)**r,
                                   comb(d,j-1)**(r-1),r)


def upper_local(d: int,j: int,prev: int,prevprev: int) -> int:
    return comb(d,j)*comb(d,j-2)*prev**2//(comb(d,j-1)**2*prevprev)


def det_leibniz(mat):
    size=len(mat)
    total=0
    for p in permutations(range(size)):
        inversions=sum(p[i]>p[j] for i in range(size) for j in range(i+1,size))
        term=1
        for i in range(size):term*=mat[i][p[i]]
        total+=(-1 if inversions%2 else 1)*term
    return total


def moments(d,n,m,a,b):
    # e1=n, e2=2m, e3=4a, e4=8b for beta_i=2/lambda_i.
    e=[1,n,2*m,4*a,8*b]
    p=[d]
    for j in range(1,5):
        p.append(sum((-1)**(i-1)*e[i]*p[j-i] for i in range(1,j))
                 +(-1)**(j-1)*j*e[j])
    return p


def H3(d,n,m,a,b):
    p=moments(d,n,m,a,b)
    return det_leibniz([[p[i+j] for j in range(3)] for i in range(3)])


def H2(d,n,m):
    return d*(n*n-4*m)-n*n


def S(d,n,m,a):
    return 36*d*a-10*d*m*n+d*n**3+12*m*n-n**3


def norm_cap(d,k,m,n):
    # Exact upper bound on u_d from the normalized Newton slope.
    j=d
    return comb(d,j)*n**(j-k)*comb(d,k)**(j-k-1)//(comb(d,k+1)**(j-k)*m**(j-k-1))


def check_file(path: Path):
    data=json.loads(path.read_text())
    d=data['degree'];rows=data['suspect']
    assert d in EXPECTED and len(rows)==EXPECTED[d][1]
    digest=hashlib.sha256(json.dumps(sorted(rows),separators=(',',':')).encode()).hexdigest()
    assert digest==EXPECTED[d][0],(d,'case-list hash mismatch')
    minimum_H2=None;minimum_S=None;largest_corner_H3=None
    for k,m,n,cap,inv in rows:
        assert k==d-2 and cap==3 and inv==n
        assert norm_cap(d,k,m,n)==3
        lo=chord(d,3,m)
        hi=upper_local(d,3,m,n)
        assert lo<=hi,(d,k,m,n,'invalid a3 interval')
        b=chord(d,4,lo)
        h2=H2(d,n,m)
        s=S(d,n,m,lo)
        h3=H3(d,n,m,lo,b)
        assert h2>0 and s>0 and h3<0,(d,k,m,n,h2,s,h3)
        minimum_H2=h2 if minimum_H2 is None else min(minimum_H2,h2)
        minimum_S=s if minimum_S is None else min(minimum_S,s)
        largest_corner_H3=h3 if largest_corner_H3 is None else max(largest_corner_H3,h3)
    return {'degree':d,'rows':len(rows),'minimum_H2':minimum_H2,
            'minimum_S':minimum_S,'largest_corner_H3':largest_corner_H3,
            'input_sha256':digest}


def independent_identity_controls(count=2000):
    rng=random.Random(20261028)
    for _ in range(count):
        d=rng.randint(5,25)
        n,m,a,b=[rng.randint(1,100) for _ in range(4)]
        h=H3(d,n,m,a,b)
        assert H3(d,n,m,a,b+1)-h==-32*H2(d,n,m)
        # Since H3 is quadratic in a with second derivative -288d,
        # H3(a+1)-H3(a)= H3'(a)-144d.
        assert H3(d,n,m,a+1,b)-h==-8*S(d,n,m,a)-144*d
        assert H3(d,n,m,a+2,b)-2*H3(d,n,m,a+1,b)+h==-288*d
    return count


def main(paths):
    assert len(paths)==4
    controls=independent_identity_controls()
    results=[check_file(Path(path)) for path in paths]
    assert [r['degree'] for r in results]==[14,15,16,17]
    assert sum(r['rows'] for r in results)==74
    print('PASS 28 Oct exact corner certificate; independent identities',controls)
    for r in results:print(json.dumps(r,sort_keys=True))
    print('PASS all 74 N=2 special rows: strictly negative H3 at the unique lower corner')
    return results


if __name__=='__main__':
    main(sys.argv[1:])
