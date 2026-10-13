"""Exact arithmetic verification for a proposed degree-5 Bell--Skandera proof.

This checks the finite computations. The accompanying argument must also prove
that Maclaurin's inequality and a monotone binomial-ratio bound reduce all
Kruskal--Katona failures to the finite exceptional sets checked here.

Run: python bell_skandera_degree5_verification.py
Requires Python 3.9+ standard library only.
"""
from math import comb
from itertools import permutations


def kk_upper(m, k):
    """Maximum number of (k+1)-faces allowed by m k-faces."""
    rem, bound, ans = m, m + k, 0
    for j in range(k, 0, -1):
        lo, hi = j, bound - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if comb(mid, j) <= rem:
                lo = mid
            else:
                hi = mid - 1
        n = lo
        if comb(n, j) <= rem:
            rem -= comb(n, j)
            ans += comb(n, j + 1)
            bound = n
            if rem == 0:
                break
    return ans


def det(mat):
    n = len(mat)
    ans = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = 1
        for i in range(n):
            term *= mat[i][perm[i]]
        ans += (-1 if inversions % 2 else 1) * term
    return ans


def hermite_minors(a, b, c, d, e):
    # Q(x) = x^5 - ax^4 + bx^3 - cx^2 + dx - e;
    # power sums of its five roots, computed using Newton identities.
    coeff = [1, -a, b, -c, d, -e]
    p = [5]
    for n in range(1, 7):
        if n <= 5:
            val = -sum(coeff[j] * p[n-j] for j in range(1, n)) - n * coeff[n]
        else:
            val = -sum(coeff[j] * p[n-j] for j in range(1, 6))
        p.append(val)
    h3 = [[p[i+j] for j in range(3)] for i in range(3)]
    h4 = [[p[i+j] for j in range(4)] for i in range(4)]
    return det(h3), det(h4)


# For m >= C(14,k), let C(r,k) <= m < C(r+1,k).
# kappa_k(m) >= C(r,k+1), and
# C(r,k+1)^k / C(r+1,k)^(k+1) increases for r >= 14.
# The four following inequalities certify the infinite tails.
for k in range(1, 5):
    assert comb(14, k+1)**k * comb(5, k)**(k+1) >= (
        comb(5, k+1)**k * comb(15, k)**(k+1)
    )

# The exact Maclaurin inequality is
# c_{k+1}^k * C(5,k)^(k+1) <= C(5,k+1)^k * c_k^(k+1).
# Thus it automatically implies KK except at these m.
expected = {1: set(), 2: {11, 12, 13, 17, 18},
            3: {12, 13, 14, 15, 17}, 4: set()}
for k in range(1, 5):
    exceptions = {
        m for m in range(comb(5, k), comb(14, k))
        if comb(5, k+1)**k * m**(k+1) >=
           (kk_upper(m, k)+1)**k * comb(5, k)**(k+1)
    }
    assert exceptions == expected[k], (k, exceptions)

# Any real-rooted candidate has a>=5, b>=10, c>=10, d>=5, e>=1.
# A KK violation requires b in expected[2] or c in expected[3].
# Newton gives b<=28 if c is exceptional, and c<=32 if b is exceptional.
# Its remaining inequalities provide exact finite bounds for a,d,e.
violators = []
newton_candidates = 0
for b in range(10, 29):
    for c in range(10, 33):
        if b not in expected[2] and c not in expected[3]:
            continue
        for a in range(5, b*b//(2*c)+1):
            if 2*a*a < 5*b:
                continue
            for d in range(5, c*c//(2*b)+1):
                for e in range(1, (2*d*d)//(5*c)+1):
                    newton_candidates += 1
                    if (b > comb(a, 2) or c > kk_upper(b, 2) or
                        d > kk_upper(c, 3) or e > kk_upper(d, 4)):
                        violators.append((a, b, c, d, e))

expected_violators = [
    (6, 12, 12, 6, 1), (6, 13, 14, 6, 1),
    (6, 13, 14, 7, 1), (6, 14, 14, 7, 1),
    (7, 14, 14, 7, 1), (6, 14, 15, 8, 1),
]
assert newton_candidates == 125, newton_candidates
assert sorted(violators) == sorted(expected_violators), violators

print('Maclaurin exceptional coefficients:', expected)
print('Newton-admissible finite candidates:', newton_candidates)
print('Kruskal--Katona violators and exact Hermite principal minors:')
for row in violators:
    h3, h4 = hermite_minors(*row)
    assert h3 < 0 or h4 < 0, (row, h3, h4)
    print(row, 'H3 =', h3, 'H4 =', h4)
print('PASS: Every possible degree-5 KK violator fails a necessary real-rootedness test.')
