"""Independent arithmetic spot-audit for Bell–Skandera degree-12 search.
Recreated and executed in the 2026-10-13 live test. Standard library only.
This tests necessary-condition arithmetic, NOT exhaustive-search completeness.
"""
from fractions import Fraction
from random import Random
from math import comb
from explore import moments, kk
from degree12_search import affine_bound, N

def independent_det(a):
    a = [[Fraction(z) for z in row] for row in a]
    sign = 1
    product = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign = -sign
        p = a[j][j]
        product *= p
        for i in range(j + 1, len(a)):
            t = a[i][j] / p
            for h in range(j + 1, len(a)):
                a[i][h] -= t * a[j][h]
    return sign * product

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
        total += comb(lo, j - 1) if lo >= j else 0
        m -= comb(lo, j)
        upper = lo - 1
    assert m == 0
    return total

def main():
    r = Random(20261013)
    checks = 0
    for rep in range(24):
        u = [1] + [r.randrange(1, 1200) for _ in range(N)]
        for j in range(1, N + 1):
            b, a = affine_bound(u, j)
            shift = j % 2
            q = (j - shift) // 2 + 1
            for value in (0, 1, 2, 17, u[j]):
                v = u[:]
                v[j] = value
                p = moments(v, j)
                d = independent_det([[p[x+y+shift] for y in range(q)] for x in range(q)])
                assert d == b + a * value, (rep, j, value)
                checks += 1
    root_checks = 0
    for rep in range(24):
        roots = [r.randrange(1, 9) for _ in range(N)]
        u = [1] + [0] * N
        for rt in roots:
            for j in range(N, 0, -1):
                u[j] += rt * u[j-1]
        for j in range(1, N + 1):
            b, a = affine_bound(u, j)
            assert b + a*u[j] >= 0
            root_checks += 1
    for rep in range(30):
        k = r.randrange(2, 11)
        m = r.randrange(comb(12, k), comb(30, k))
        shadow = kk(m, k)
        assert down(shadow, k+1) <= m
        assert down(shadow+1, k+1) > m
    print('PASS independent rational determinant identities:', checks)
    print('PASS positive-root determinant controls:', root_checks)
    print('PASS inverse KK shadow spot tests:', 30)

if __name__ == '__main__':
    main()
