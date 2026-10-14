"""Evening 14 October 2026 exact-arithmetic audit of degree-12 frontier.
Checks necessary conditions, independent rational determinants, positive root controls.
A passing result is NOT an exhaustive proof of Bell–Skandera.
Run: python audit_evening_20261014.py
"""
from math import comb
from fractions import Fraction
from random import Random
from itertools import combinations_with_replacement
import json
from pathlib import Path
from explore import kk, moments
from degree12_search import affine_bound, N, C

def rational_det(mat):
    a = [[Fraction(z) for z in row] for row in mat]
    out = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out *= value
        for i in range(j+1, len(a)):
            q = a[i][j] / value
            for h in range(j+1, len(a)):
                a[i][h] -= q * a[j][h]
    return out

def inverse_down(v, k):
    result = 0
    cap = v+k
    for q in range(k, 0, -1):
        lo, hi = q-1, cap
        while lo < hi:
            mid = (lo+hi+1)//2
            if comb(mid,q) <= v: lo=mid
            else: hi=mid-1
        if lo >= q: result += comb(lo,q-1)
        v -= comb(lo,q)
        cap = lo-1
    assert v == 0
    return result

def main():
    data = json.loads((Path(__file__).parent/'degree12_frontier.json').read_text())
    assert data['pair_total'] == 120676
    stats = dict(finite_pair_constraints=0,inverse_KK=0,affine_exact=0,
                 positive_roots=0,cap_soundness=0,newton_soundness=0)
    for k in range(1,N):
        entry = data['indices'][str(k)]
        pairs = entry['pairs']
        assert len(pairs) == entry['pair_count']
        for index,(m,v) in enumerate(pairs):
            if index: assert (m,v) > tuple(pairs[index-1])
            shadow=kk(m,k)
            assert v > shadow
            assert v**k*C[k]**(k+1) <= C[k+1]**k*m**(k+1)
            stats['finite_pair_constraints'] += 1
        for m in sorted(set(m for m,v in pairs)):
            s = kk(m,k)
            assert inverse_down(s,k+1) <= m < inverse_down(s+1,k+1)
            stats['inverse_KK'] += 1
    rng = Random(61220261014)
    for _ in range(32):
        u=[1]+[rng.randrange(1,1500) for _ in range(N)]
        for j in range(1,N+1):
            b,a=affine_bound(u,j)
            shift=j%2
            q=(j-shift)//2+1
            for x in (0,1,2,17,u[j]):
                v=u[:];v[j]=x;p=moments(v,j)
                determinant=rational_det([[p[r+c+shift] for c in range(q)]
                                          for r in range(q)])
                assert determinant == b+a*x
                stats['affine_exact'] += 1
    for roots in combinations_with_replacement(range(1,5),N):
        u=[1]+[0]*N
        for root in roots:
            for j in range(N,0,-1): u[j]+=root*u[j-1]
        for j in range(1,N+1):
            b,a=affine_bound(u,j)
            assert b+a*u[j]>=0
            stats['positive_roots']+=1
            if j<N:
                assert C[j-1]*C[j+1]*u[j]**2 >= C[j]**2*u[j-1]*u[j+1]
                stats['newton_soundness']+=1
        for k in (5,6):
            entry=data['indices'][str(k)]
            if u[k] > max(m for m,v in entry['pairs']): continue
            for j in range(1,N+1):
                assert u[j] <= entry['coefficient_caps'][j-1]
                stats['cap_soundness']+=1
    print('PASS',json.dumps(stats,sort_keys=True))
if __name__ == '__main__':
    main()
