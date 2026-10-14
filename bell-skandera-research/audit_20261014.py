"""2026-10-14 independent exact arithmetic audit for degree-12 k=5.
Run from bell-skandera-research with: python audit_20261014.py
Checks necessary-condition arithmetic, not exhaustive-search completeness.
"""
from math import comb
from fractions import Fraction
from random import Random
import json
from explore import kk, moments
from degree12_search import affine_bound, N, C

def down(m, k):
    total = 0
    upper = m + k
    for j in range(k, 0, -1):
        lo, hi = j - 1, upper
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if comb(mid, j) <= m:
                lo = mid
            else:
                hi = mid - 1
        if lo >= j:
            total += comb(lo, j-1)
        m -= comb(lo, j)
        upper = lo - 1
    assert m == 0
    return total

def det_independent(A):
    A = [[Fraction(x) for x in row] for row in A]
    result = Fraction(1)
    for j in range(len(A)):
        pivot = next((i for i in range(j, len(A)) if A[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            result = -result
        x = A[j][j]
        result *= x
        for i in range(j+1, len(A)):
            factor = A[i][j] / x
            for k in range(j+1, len(A)):
                A[i][k] -= factor * A[j][k]
    return result

def run():
    rng = Random(20261014)
    pairs = json.load(open('degree12_frontier.json'))['indices']['5']['pairs']
    assert len(pairs) == 30203
    exceptions = sorted(set(m for m, v in pairs))
    assert len(exceptions) == 809
    for m in exceptions:
        q = kk(m, 5)
        assert down(q, 6) <= m < down(q+1, 6), (m, q)
    print('PASS', len(exceptions), 'inverse-shadow checks')
    for m, v in pairs:
        assert v > kk(m, 5)
        assert v**5*C[5]**6 <= C[6]**5*m**6
    print('PASS', len(pairs), 'finite-frontier pair constraints')
    checks = 0
    for _ in range(20):
        u = [1] + [rng.randrange(1, 10000) for _ in range(N)]
        for j in range(1, N+1):
            b, a = affine_bound(u, j)
            shift = j % 2
            q = (j-shift)//2 + 1
            for x in (0, 1, 7, u[j]):
                v = u[:]
                v[j] = x
                p = moments(v, j)
                value = det_independent([[p[i+h+shift] for h in range(q)] for i in range(q)])
                assert value == b+a*x
                checks += 1
    print('PASS', checks, 'independent rational determinant comparisons')
    positive_checks = 0
    for _ in range(30):
        roots = [rng.randrange(1, 5) for _ in range(N)]
        u = [1] + [0]*N
        for root in roots:
            for j in range(N, 0, -1):
                u[j] += root*u[j-1]
        for j in range(1, N+1):
            b, a = affine_bound(u, j)
            assert b+a*u[j] >= 0
            positive_checks += 1
    print('PASS', positive_checks, 'positive-root determinant checks')

if __name__ == '__main__':
    run()
