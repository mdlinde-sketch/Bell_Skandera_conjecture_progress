"""27 October 2026: independent exact norm-three obstruction for Bell–Skandera.

This is a necessary-condition certificate, conditional on the elementary
calculus lemma and on removing any (x-1) factor by degree induction.
It does NOT establish Bell–Skandera or verify the full finite frontier.
Only Python standard library exact rational/integer arithmetic.
"""
import json
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path


def log_interval(y, terms=14):
    """Provable rational enclosure for log(y), y>0, via artanh."""
    assert y > 0
    t = (y-1)/(y+1)
    partial = 2*sum((t**(2*j+1))/(2*j+1) for j in range(terms))
    err = 2*abs(t)**(2*terms+1)/((2*terms+1)*(1-t*t))
    return partial-err, partial+err


def critical_min_lower(xlo,xhi):
    assert Q(0)<xlo<xhi and (xhi<1 or xlo>1)
    # g(x)=1/x+3/2 log x -3/4 log|x-1|.
    low_x = log_interval(xlo)[0]
    high_dist = log_interval(1-xlo if xhi<1 else xhi-1)[1]
    return 1/xhi + Q(3,2)*low_x - Q(3,4)*high_dist


def prove_inverse_trace_pointwise():
    # g'(x)=(3x^2-10x+4)/(4x^2(x-1)); minima at (5 +/- sqrt(13))/3.
    lo,hi=Q(3605551,10**6),Q(3605552,10**6)
    assert lo*lo<13<hi*hi
    minima=[((5-hi)/3,(5-lo)/3),((5+lo)/3,(5+hi)/3)]
    bounds=[critical_min_lower(a,b) for a,b in minima]
    assert min(bounds)>Q(29,20)
    return bounds


def prove_log3_upper():
    # e^(11/10) > its fifth-order Taylor polynomial > 3, hence log(3)<11/10.
    x=Q(11,10)
    partial=sum(x**j/factorial(j) for j in range(6))
    assert partial>3
    return partial


def coeff_cap(d,k,m,n,j):
    if j==k: return m
    if j==k+1: return n
    if j<k:
        return comb(d,j)*m**(k+1-j)*comb(d,k+1)**(k-j)//(comb(d,k)**(k+1-j)*n**(k-j))
    return comb(d,j)*n**(j-k)*comb(d,k)**(j-k-1)//(comb(d,k+1)**(j-k)*m**(j-k-1))


def check(root=Path('.')):
    inverse_min=prove_inverse_trace_pointwise()
    exp_partial=prove_log3_upper()
    all_rows=[]
    per_degree={}
    for d in range(14,18):
        rows=json.loads((root/f'frontier_checked_d{d}_20261025.json').read_text())['suspect']
        margins=[]
        for k,m,n,ud,um in rows:
            assert k==d-2
            assert coeff_cap(d,k,m,n,d)==ud==3
            assert coeff_cap(d,k,m,n,d-1)==um==n
            # If P(1) != 0, the exact inverse-trace lemma gives
            #   n/3 + 3/2 log(3) > 29d/20.
            # Since log(3)<11/10, it NECESSARILY follows that
            #   20*n + 99 > 87*d.
            # All rows violate that necessary strict inequality.
            margin=87*d-(20*um+99)
            assert margin>=0,(d,k,m,n,margin)
            margins.append(margin)
            all_rows.append([d,k,m,n,ud,um,margin])
        per_degree[d]={'rows':len(rows),'minimum_integer_margin':min(margins),
                       'maximum_trace_cap':max(x[4] for x in rows)}
    assert len(all_rows)==74
    print('PASS exact inverse-trace pointwise minima >29/20:',[str(x) for x in inverse_min])
    print('PASS exact exp(11/10) Taylor lower >3:',str(exp_partial))
    print('PASS norm-three excluded for all 74 specials, conditional on P(1)!=0:')
    print(json.dumps(per_degree,sort_keys=True))
    return per_degree


if __name__=='__main__': check()
