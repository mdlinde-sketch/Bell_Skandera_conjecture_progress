#!/usr/bin/env python3
"""Independent degree-7 checker: explicit nested loops, literal colex faces,
SymPy companion-matrix traces and symbolic 4x4 determinants.
Requires: pip install sympy
Run: python bell_skandera_degree7_independent.py
"""
from collections import Counter
from itertools import combinations
from math import comb, isqrt
from sympy import Matrix

C = [comb(7, j) for j in range(8)]


def shadow(m, k):
    # Independent implementation of the canonical binomial expansion.
    remaining, limit, result = m, 1000, 0
    for j in range(k, 0, -1):
        r = j - 1
        while r + 1 < limit and comb(r+1, j) <= remaining:
            r += 1
        remaining -= comb(r, j)
        result += comb(r, j+1)
        limit = r
    assert remaining == 0
    return result


def colex_shadow_table(k, max_m, universe_size):
    """Literal colex upper shadows for *every* m<=max_m.

    A k-set T={t1<...<tk} has zero-based colex rank
    sum_i binom(t_i,i).  A (k+1)-set enters the upper shadow
    exactly when all its k-subsets have appeared.
    """
    enters = [0] * (max_m + 1)
    for S in combinations(range(universe_size), k + 1):
        latest = max(sum(comb(t, i) for i,t in enumerate(T, 1))
                     for T in combinations(S, k)) + 1
        if latest <= max_m:
            enters[latest] += 1
    shadow = [0] * (max_m + 1)
    for m in range(1, max_m + 1):
        shadow[m] = shadow[m-1] + enters[m]
    return shadow


def h3(a,b,c,d):
    p2 = a*a-2*b
    p3 = a*a*a-3*a*b+3*c
    p4 = a**4-4*a*a*b+2*b*b+4*a*c-4*d
    return 7*p2*p4-7*p3*p3-a*a*p4+2*a*p2*p3-p2**3


def companion_h4(u):
    # Completely different construction from the primary certificate:
    # power sums are traces of a 7x7 companion matrix.
    coefficients = [1] + [(-1)**j*u[j] for j in range(1,8)]
    M = Matrix.zeros(7)
    for i in range(6):
        M[i+1,i] = 1
    for i in range(7):
        M[i,6] = -coefficients[7-i]
    traces = [7] + [int((M**j).trace()) for j in range(1,7)]
    H = Matrix(4,4,lambda i,j:traces[i+j])
    return int(H.det(method='domain-ge'))


exceptions = {}
pairs = {}
caps = {}
for k in range(1,7):
    cutoff = next(r for r in range(7,40)
        if comb(r,k+1)**k*C[k]**(k+1) > C[k+1]**k*comb(r+1,k)**(k+1))
    exceptions[k] = [m for m in range(C[k],comb(cutoff,k))
        if (shadow(m,k)+1)**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1)]
    # Exhaustively compare ALL m in the finite range with literal colex faces.
    table = colex_shadow_table(k, comb(cutoff,k)-1, cutoff+1)
    for m in range(C[k], comb(cutoff,k)):
        assert shadow(m,k) == table[m], (k,m,shadow(m,k),table[m])
    if k not in (2,3,4,5):
        continue
    caps[k] = []
    for j in range(1,8):
        p,q = (7-j,7-k) if j<k else (j,k)
        maximum = 0
        while (maximum+1)**q*C[k]**p<=C[j]**q*max(exceptions[k])**p:
            maximum += 1
        caps[k].append(maximum)
    pairs[k] = []
    for m in exceptions[k]:
        x = shadow(m,k)+1
        while x**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1):
            pairs[k].append((m,x))
            x += 1

counts = Counter()
h3_counts = Counter()
all_h3_survivors = set()


def evaluate(k,a,b,c,d,e,f,g):
    u=(1,a,b,c,d,e,f,g)
    counts[k]+=1
    if h3(a,b,c,d)>=0:
        h3_counts[k]+=1
        all_h3_survivors.add(u)


for k in (2,3,4,5):
    cap = caps[k]
    for m,n in pairs[k]:
        if k==2:
            b,c=m,n
            for d in range(35,min(cap[3],3*c*c//(5*b))+1):
                for a in range(7,min(cap[0],5*b*b//(9*c))+1):
                    if 3*a*a<7*b:continue
                    for e in range(21,min(cap[4],3*d*d//(5*c))+1):
                        for f in range(7,min(cap[5],5*e*e//(9*d))+1):
                            for g in range(1,min(cap[6],3*f*f//(7*e))+1):
                                evaluate(k,a,b,c,d,e,f,g)
        elif k==3:
            c,d=m,n
            for b in range(21,min(cap[1],3*c*c//(5*d))+1):
                for a in range(7,min(cap[0],5*b*b//(9*c))+1):
                    if 3*a*a<7*b:continue
                    for e in range(21,min(cap[4],3*d*d//(5*c))+1):
                        for f in range(7,min(cap[5],5*e*e//(9*d))+1):
                            for g in range(1,min(cap[6],3*f*f//(7*e))+1):
                                evaluate(k,a,b,c,d,e,f,g)
        elif k==4:
            d,e=m,n
            for c in range(35,min(cap[2],3*d*d//(5*e))+1):
                for b in range(21,min(cap[1],3*c*c//(5*d))+1):
                    for a in range(7,min(cap[0],5*b*b//(9*c))+1):
                        if 3*a*a<7*b:continue
                        for f in range(7,min(cap[5],5*e*e//(9*d))+1):
                            for g in range(1,min(cap[6],3*f*f//(7*e))+1):
                                evaluate(k,a,b,c,d,e,f,g)
        else:
            e,f=m,n
            for d in range(35,min(cap[3],5*e*e//(9*f))+1):
                for c in range(35,min(cap[2],3*d*d//(5*e))+1):
                    for b in range(21,min(cap[1],3*c*c//(5*d))+1):
                        for a in range(7,min(cap[0],5*b*b//(9*c))+1):
                            if 3*a*a<7*b:continue
                            for g in range(1,min(cap[6],3*f*f//(7*e))+1):
                                evaluate(k,a,b,c,d,e,f,g)

assert [counts[k] for k in (2,3,4,5)] == [1660,455,146,263]
assert [h3_counts[k] for k in (2,3,4,5)] == [848,4,24,44]
assert len(all_h3_survivors) == 902

for u in all_h3_survivors:
    assert companion_h4(u)<0,('UNREJECTED',u)
print('Independent degree-7 verification: PASS')
print('Literal colex checks for every m below cutoff:',sum(comb(r,k)-C[k] for k,r in ((1,20),(2,18),(3,17),(4,15),(5,13),(6,11))))
print('Newton-admissible candidates by failed KK index:',dict(counts))
print('H3-nonnegative candidates by failed KK index:',dict(h3_counts))
print('Distinct H3-nonnegative candidates:',len(all_h3_survivors))
print('All 902 have negative H4 by SymPy companion-matrix traces.')