#!/usr/bin/env python3
"""Degree-7 Bell--Skandera exact finite certificate (Python 3, stdlib only).

A self-contained, reproducible *candidate proof*, pending external review.
All comparisons, coefficient bounds, and determinants use integer arithmetic.
Run: python bell_skandera_degree7_certificate.py
"""
from math import comb

D = 7
C = [comb(D, j) for j in range(D + 1)]


def kk(m, k):
    """Kruskal--Katona upper shadow by canonical k-binomial expansion."""
    remainder, ceiling, shadow = m, m + k + 2, 0
    for j in range(k, 0, -1):
        lo, hi = j - 1, ceiling - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if comb(mid, j) <= remainder:
                lo = mid
            else:
                hi = mid - 1
        r = lo
        if r >= j:
            remainder -= comb(r, j)
            shadow += comb(r, j + 1)
            ceiling = r
    assert remainder == 0
    return shadow


def bareiss_det(matrix):
    """Exact fraction-free integer determinant."""
    A = [list(row) for row in matrix]
    size, sign, previous = len(A), 1, 1
    for k in range(size - 1):
        if A[k][k] == 0:
            swap = next((j for j in range(k + 1, size) if A[j][k]), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                A[i][j] = quotient
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]


def moments_to_six(u):
    """Traces of roots of x^7-u1*x^6+u2*x^5-...-u7."""
    q = [1] + [(-1) ** j * u[j] for j in range(1, 8)]
    p = [7]
    for s in range(1, 7):
        p.append(-sum(q[j] * p[s - j] for j in range(1, s)) - s * q[s])
    return p


def h3(u):
    a, b, c, d = u[1:5]
    p2 = a*a - 2*b
    p3 = a*a*a - 3*a*b + 3*c
    p4 = a**4 - 4*a*a*b + 2*b*b + 4*a*c - 4*d
    return 7*p2*p4 - 7*p3*p3 - a*a*p4 + 2*a*p2*p3 - p2**3


def h4(u):
    p = moments_to_six(u)
    return bareiss_det([[p[i+j] for j in range(4)] for i in range(4)])



# Positive and negative controls for the exact moment-matrix machinery.
unit_roots = [comb(7,j) for j in range(8)]  # (1+t)^7
assert h3(unit_roots) == 0 and h4(unit_roots) == 0
varied_roots = [1] + [0]*7  # product_{r=1}^7 (1+r*t)
for root in range(1,8):
    for j in range(7,0,-1):
        varied_roots[j] += root * varied_roots[j-1]
assert h3(varied_roots) > 0 and h4(varied_roots) > 0
known_obstruction = [1,8,26,46,47,27,8,1]
assert h3(known_obstruction) == 52 and h4(known_obstruction) == -4084

# Analytic high-range KK cutoff.  The strict binomial ratio used here is
# monotone increasing in r>k (see accompanying proof note).
thresholds, exceptional, caps, pairs = {}, {}, {}, {}
for k in range(1, 7):
    r = next(r for r in range(7, 100)
             if comb(r, k+1)**k * C[k]**(k+1)
             > C[k+1]**k * comb(r+1, k)**(k+1))
    thresholds[k] = r
    exceptional[k] = tuple(m for m in range(C[k], comb(r, k))
        if (kk(m, k)+1)**k * C[k]**(k+1)
        <= C[k+1]**k * m**(k+1))
    if k not in (2, 3, 4, 5):
        continue
    max_m = max(exceptional[k])
    bounds = [1]
    for j in range(1, 8):
        p, q = (7-j, 7-k) if j < k else (j, k)
        maximum = 0
        while (maximum+1)**q * C[k]**p <= C[j]**q * max_m**p:
            maximum += 1
        bounds.append(maximum)
    caps[k] = bounds
    candidates = []
    for m in exceptional[k]:
        nxt = kk(m, k) + 1
        while nxt**k * C[k]**(k+1) <= C[k+1]**k * m**(k+1):
            candidates.append((m, nxt))
            nxt += 1
    pairs[k] = candidates

assert thresholds == {1:20, 2:18, 3:17, 4:15, 5:13, 6:11}
assert {k:len(v) for k,v in exceptional.items()} == {1:0,2:14,3:32,4:27,5:20,6:0}
assert caps == {
    2: [1,15,41,95,133,111,52,10],
    3: [1,21,53,74,94,73,31,5],
    4: [1,23,57,78,64,44,17,2],
    5: [1,68,141,160,109,45,17,2],
}
assert {k:len(v) for k,v in pairs.items()} == {2:33,3:89,4:73,5:27}

stats = {}
for k in (2, 3, 4, 5):
    cap = caps[k]
    order = list(range(k-1, 0, -1)) + list(range(k+2, 8))

    def enumerate_remaining(u, index):
        # Mutable counters live in the dictionary to keep recursion explicit.
        if index == len(order):
            if any(C[j-1]*C[j+1]*u[j]**2 < C[j]**2*u[j-1]*u[j+1]
                   for j in range(1, 7)):
                return
            counts['total'] += 1
            if h3(u) < 0:
                return
            counts['h3_nonnegative'] += 1
            determinant = h4(u)
            if determinant < 0:
                counts['h4_negative'] += 1
                if counts['sample'] is None:
                    counts['sample'] = (tuple(u), h3(u), determinant)
            else:
                raise AssertionError(('POTENTIAL COUNTEREXAMPLE: review!', tuple(u),
                                      h3(u), determinant))
            return
        j = order[index]
        if j < k:
            # Newton at j+1: C[j+1]^2*u[j]*u[j+2]
            #                  <= C[j]*C[j+2]*u[j+1]^2
            maximum = min(cap[j],
                C[j]*C[j+2]*u[j+1]**2 // (C[j+1]**2*u[j+2]))
        else:
            # Newton at j-1, with known u[j-2],u[j-1].
            maximum = min(cap[j],
                C[j-2]*C[j]*u[j-1]**2 // (C[j-1]**2*u[j-2]))
        for value in range(C[j], maximum + 1):
            u[j] = value
            enumerate_remaining(u, index + 1)
        u[j] = None

    counts = {'total':0,'h3_nonnegative':0,'h4_negative':0,'sample':None}
    for m, nxt in pairs[k]:
        u = [None] * 8
        u[0], u[k], u[k+1] = 1, m, nxt
        enumerate_remaining(u, 0)
    stats[k] = counts

assert {k:(v['total'],v['h3_nonnegative'],v['h4_negative']) for k,v in stats.items()} == {
    2:(1660,848,848), 3:(455,4,4), 4:(146,24,24), 5:(263,44,44)
}
print('Degree-7 exact certificate: PASS')
print('High-range thresholds:', thresholds)
print('Exceptional coefficient counts:', {k:len(v) for k,v in exceptional.items()})
print('Possible violating adjacent pairs:', {k:len(v) for k,v in pairs.items()})
for k, v in stats.items():
    print(f'KK failure at k={k}: {v["total"]} Newton-admissible vectors; '
          f'{v["h3_nonnegative"]} pass H3; all have H4<0')
print('Total candidates:', sum(v['total'] for v in stats.values()))
print('Total H3 nonnegative:', sum(v['h3_nonnegative'] for v in stats.values()))
print('PASS: no real-rooted degree-7 polynomial can violate Kruskal--Katona, '
      'subject to independent review of the analytic reduction and certificate.')
