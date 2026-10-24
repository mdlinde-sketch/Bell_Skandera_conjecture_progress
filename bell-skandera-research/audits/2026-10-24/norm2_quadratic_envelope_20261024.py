"""Exact two-variable norm-two Hankel envelope certificate for degrees 14--17.

For each norm-two special case with adjacent reversed coefficients
  a1 = n = u_(d-1), a2 = m = u_(d-2),
all possible a3 and a4 obey a3 in [L3(m), U3(m,n)] and
  a4 >= L4(a3) >= L4(L3(m)).
The Hankel determinant H3 of the scaled reciprocal roots beta=2/lambda
has slope -32 H2 with respect to a4 and quadratic coefficient -144*d
with respect to a3, so a single exact concave quadratic dominates every
possible integer pair (a3,a4).  No grid enumeration or floats are used.

This is a finite certificate conditional on standard Maclaurin/Newton
coefficient bounds and positive-root Hankel PSD necessity.
"""
import json,sys
from math import comb

def ceil_root_ratio(num,den,k):
    lo,hi=0,1
    while den*hi**k<num:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if den*mid**k>=num:hi=mid
        else:lo=mid
    return hi

def lower_chord(d,j,prev):
    r=d-j+1
    return ceil_root_ratio(prev**(r-1)*comb(d,j)**r,comb(d,j-1)**(r-1),r)

def local_upper(d,j,prev,prevprev):
    return comb(d,j)*comb(d,j-2)*prev*prev//(comb(d,j-1)**2*prevprev)

def det3(d,n,m,a3,a4):
    # Coefficients of scaled reciprocal B_2: e1=n,e2=2m,e3=4a3,e4=8a4
    p0=d;p1=n;p2=n*n-4*m
    p3=n*p2-2*m*n+12*a3
    p4=n*p3-2*m*p2+4*a3*n-32*a4
    return p0*(p2*p4-p3*p3)-p1*(p1*p4-p2*p3)+p2*(p1*p3-p2*p2)

def maximum_quadratic_integer(f0,f1,f2,width):
    diff=f2-2*f1+f0
    assert diff%2==0
    A=diff//2;B=f1-f0-A
    assert A<0
    def value(t):return f0+B*t+A*t*t
    positions={0,width}
    vertex=B//(-2*A)
    for t in (vertex,vertex+1):
        if 0<=t<=width:positions.add(t)
    return max(value(t) for t in positions),A

def check(path):
    obj=json.load(open(path));d=obj['degree'];rows=obj['suspect']
    worst=None;details=[]
    for k,m,n,ud,um in rows:
        assert k==d-2 and ud==3,(d,k,m,n,ud)
        H2=d*(n*n-4*m)-n*n
        assert H2>0,(d,k,m,n,H2)
        lo=lower_chord(d,3,m)
        hi=local_upper(d,3,m,n)
        assert lo<=hi
        amin=lower_chord(d,4,lo)
        f0=det3(d,n,m,lo,amin)
        f1=det3(d,n,m,lo+1,amin)
        f2=det3(d,n,m,lo+2,amin)
        bound,A=maximum_quadratic_integer(f0,f1,f2,hi-lo)
        assert A==-144*d,(d,k,m,n,A)
        assert bound<0,(d,k,m,n,bound)
        worst=bound if worst is None else max(worst,bound)
        details.append({'k':k,'m':m,'n':n,'a3_min':lo,'a3_max':hi,
                        'a4_floor':amin,'H2':H2,'H3_upper':bound})
    print('PASS d=',d,'cases=',len(rows),'max H3 upper=',worst,'min H2=',min(x['H2'] for x in details))
    return {'degree':d,'cases':len(rows),'max_H3_upper':worst,'certificates':details}

if __name__=='__main__':
    result=[]
    for path in sys.argv[1:]:result.append(check(path))
    with open('norm2_quadratic_envelope_results_20261024.json','w') as f:
        json.dump(result,f,indent=2)
