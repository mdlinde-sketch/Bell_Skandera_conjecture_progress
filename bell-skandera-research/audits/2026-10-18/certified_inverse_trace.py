"""Exact-rational proof of an inverse-trace inequality for totally positive
integer polynomials without the factor (x-1).

For every x>0, x !=1:
  1/x + (3/2)*log(x) - (3/4)*log(|x-1|) > 29/20.
Then if P(x) is monic in Z[x] with d positive real roots lambda_i,
P(0) != 0, P(1) != 0, and N=|P(0)|:
  sum_i 1/lambda_i + (3/2)*log(N) > 29*d/20.
Proof by summing and |P(1)|>=1.
"""
from fractions import Fraction as Q


def log_bounds(y: Q, n=12):
    """Exact rational lower and upper bounds for log(y), y>0."""
    assert y > 0
    t = (y - 1) / (y + 1)
    partial = 2 * sum((t ** (2 * j + 1)) / (2 * j + 1) for j in range(n))
    tail = 2 * abs(t) ** (2 * n + 1) / ((2 * n + 1) * (1 - t * t))
    return partial - tail, partial + tail


def critical_minimum_lower(xlo, xhi):
    """Lower bound on g(x) for any x in (xlo,xhi) entirely on one side of 1."""
    assert 0 < xlo < xhi and not (xlo <= 1 <= xhi)
    low_log_x = log_bounds(xlo)[0]
    high_log_distance = log_bounds((1 - xlo) if xhi < 1 else (xhi - 1))[1]
    return 1 / xhi + Q(3,2) * low_log_x - Q(3,4) * high_log_distance


def proof():
    root_lo, root_hi = Q(3605551,10**6), Q(3605552,10**6)
    assert root_lo**2 < 13 < root_hi**2
    # Derivative of g is (3x^2-10x+4)/(4x^2(x-1)).
    # g tends to +infinity at x=0,1-,1+,infinity.
    # Thus its two global local minima occur at x=(5 +/- sqrt(13))/3.
    small_lo, small_hi = (5-root_hi)/3, (5-root_lo)/3
    large_lo, large_hi = (5+root_lo)/3, (5+root_hi)/3
    a = critical_minimum_lower(small_lo, small_hi)
    b = critical_minimum_lower(large_lo, large_hi)
    target = Q(29,20)
    assert a > target and b > target
    print('CERTIFIED: g(x)>29/20 for all positive x!=1')
    print('small-root minimum rational lower bound:',a,'=',float(a))
    print('large-root minimum rational lower bound:',b,'=',float(b))
    print('lower margins:',float(a-target),float(b-target))
    return a,b

if __name__ == '__main__': proof()
