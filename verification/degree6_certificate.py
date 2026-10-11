#!/usr/bin/env python3
"""Exact degree-six Bell--Skandera candidate certificate (stdlib only).
Enumerates ALL Newton-admissible integer vectors capable of violating
Kruskal--Katona after the analytic Maclaurin reduction.
"""
from math import comb
from collections import Counter
from itertools import permutations

N=6
C=[comb(N,k) for k in range(N+1)]

def kk(m,k):
    """Kruskal--Katona upper shadow, using the canonical k-binomial expansion."""
    rem, upper, ans = m, m+k+2, 0
    for j in range(k,0,-1):
        lo,hi=j-1,upper-1
        while lo<hi:
            mid=(lo+hi+1)//2
            if comb(mid,j)<=rem:lo=mid
            else:hi=mid-1
        r=lo
        if r>=j:
            rem-=comb(r,j)
            ans+=comb(r,j+1)
            upper=r
    assert rem==0,(m,k,rem)
    return ans

def det(M):
    """Bareiss exact determinant, avoiding external algebra packages."""
    n=len(M)
    A=[row[:] for row in M]
    sign=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    return sign*A[n-1][n-1]

def moments(u,n=6):
    """Power sums of the six positive-root candidates via Newton identities."""
    # Q(x)=x^6-u1*x^5+u2*x^4-...+u6
    q=[1]+[(-1)**j*u[j] for j in range(1,7)]
    p=[6]
    for s in range(1,2*n-1):
        if s<=6:
            v=-sum(q[j]*p[s-j] for j in range(1,s)) - s*q[s]
        else:
            v=-sum(q[j]*p[s-j] for j in range(1,7))
        p.append(v)
    return p

def hermite_det(u,size):
    p=moments(u)
    return det([[p[i+j] for j in range(size)] for i in range(size)])

# For each k, prove the high-range comparison at an integer r by a positive margin.
thresholds={}
exceptions={}
for k in range(1,6):
    for r in range(6,50):
        margin=comb(r,k+1)**k*C[k]**(k+1)-C[k+1]**k*comb(r+1,k)**(k+1)
        if margin>0:
            thresholds[k]=r
            break
    assert k in thresholds
    exceptions[k]=tuple(m for m in range(C[k],comb(thresholds[k],k))
      if (kk(m,k)+1)**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1))
assert thresholds=={1:17,2:15,3:14,4:12,5:10}
assert exceptions=={
  1:(),2:(16,17,18,19,23,24,25),
  3:(21,22,23,24,25,26,27,28,29,31,32,33,42,43),
  4:(17,18,19,20,21,22,23,24,27,28,29,30),5:()}

B,D,E=(set(exceptions[k]) for k in (2,3,4))
checked=0;viol=[]
for b in range(15,241):
    for c in range(20,81):
        for d in range(15,114):
            if not (b in B or c in D or d in E):continue
            if 16*b*d>9*c*c:continue
            amin=6
            while 5*amin*amin<12*b:amin+=1
            for a in range(amin,8*b*b//(15*c)+1):
                for e in range(6,8*d*d//(15*c)+1):
                    for f in range(1,5*e*e//(12*d)+1):
                        u=(1,a,b,c,d,e,f)
                        checked+=1
                        bad=tuple(k for k in range(1,6) if u[k+1]>kk(u[k],k))
                        if bad:viol.append((u,bad))
assert checked==4445,checked
assert len(viol)==22,len(viol)
for u,bad in viol:
    d3,d4=hermite_det(u,3),hermite_det(u,4)
    assert d3<0 or d4<0,(u,d3,d4)
print('Degree 6: analytic exceptional sets',exceptions)
print('Newton-admissible candidates:',checked,'KK violations:',len(viol))
for u,bad in viol:
    d3,d4=hermite_det(u,3),hermite_det(u,4)
    q,w=(3,d3) if d3<0 else (4,d4)
    print('u=',u,'KK bad k=',bad,'negative Hermite minor:',q,w)
print('PASS: Every possible degree-6 KK violation fails a necessary real-rootedness test.')