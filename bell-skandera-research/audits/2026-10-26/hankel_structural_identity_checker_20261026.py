"""Exact independent algebraic controls for Hankel interval pruning.

Standard library only. This does NOT prove certificate completeness, Smyth's
theorem, or Bell–Skandera. No imports from earlier determinant verifiers.
"""
from itertools import permutations
from random import Random

R = Random(20261026)

def det(M):
    n = len(M)
    total = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        term = 1
        for i in range(n):
            term *= M[i][p[i]]
        total += (-1 if inv%2 else 1)*term
    return total

def moments(d,q):
    p = [d]
    for j in range(1,7):
        p.append(sum((-1)**(i-1)*q[i]*p[j-i] for i in range(1,j))
                 + (-1)**(j-1)*j*q[j])
    return p

def hankel(p,n):
    return det([[p[i+j] for j in range(n)] for i in range(n)])

def audit():
    # Arbitrary integer coefficients, not just favorable positive-root cases.
    for _ in range(3000):
        d = R.randint(7,30)
        q = [1]+[R.randint(1,150) for _ in range(6)]
        p = moments(d,q)
        h2,h3,h4 = (hankel(p,n) for n in (2,3,4))
        q6 = q.copy(); q6[6] += 1
        assert hankel(moments(d,q6),4)-h4 == -6*h3
        q5 = q.copy(); q5[5] += 1
        q52 = q.copy(); q52[5] += 2
        assert (hankel(moments(d,q52),4)
                -2*hankel(moments(d,q5),4)+h4) == -50*h2
        q4 = q.copy(); q4[4] += 1
        assert hankel(moments(d,q4),3)-h3 == -4*h2

    # Norm-two scaled reciprocal coefficients: q3=4*a3, q4=8*a4.
    for _ in range(2000):
        d = R.randint(7,30)
        n,m,a,b = (R.randint(1,150) for _ in range(4))
        def h3_norm2(a,b):
            return hankel(moments(d,[1,n,2*m,4*a,8*b,0,0]),3)
        h2 = d*(n*n-4*m)-n*n
        assert h3_norm2(a,b+1)-h3_norm2(a,b) == -32*h2
        assert (h3_norm2(a+2,b)-2*h3_norm2(a+1,b)
                +h3_norm2(a,b)) == -288*d
    print("PASS: 3,000 H4 derivative/concavity and 2,000 norm-two H3 exact identities")

if __name__=="__main__":
    audit()
