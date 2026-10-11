#!/usr/bin/env python3
"""Independent degree-six audit. Requires SymPy.
Uses literal colex simplicial complexes for Kruskal--Katona and companion
matrix traces for Hermite determinants (rather than Macaulay expansions or
Newton power-sum identities). Checks every candidate in the finite box.
"""
from itertools import combinations
from math import comb, isqrt
from collections import Counter
from sympy import Matrix, symbols, Poly, oo

LIMITS={1:30,2:240,3:364,4:495,5:252}

def colex_capacity(k,mmax):
    n=k+1
    while comb(n,k)<mmax:n+=1
    faces=sorted(combinations(range(n),k),key=lambda s:s[::-1])
    index={face:j for j,face in enumerate(faces)}
    added=[0]*(len(faces)+1)
    for high in combinations(range(n),k+1):
        last=max(index[face] for face in combinations(high,k))
        added[last+1]+=1
    out=[];total=0
    for value in added:
        total+=value;out.append(total)
    return out

K={k:colex_capacity(k,lim) for k,lim in LIMITS.items()}
C=[comb(6,k) for k in range(7)]
exc={}
for k in range(1,6):
    r=6
    while comb(r,k+1)**k*C[k]**(k+1)<=C[k+1]**k*comb(r+1,k)**(k+1):r+=1
    exc[k]=set(m for m in range(C[k],comb(r,k))
       if (K[k][m]+1)**k*C[k]**(k+1)<=C[k+1]**k*m**(k+1))
assert [len(exc[k]) for k in range(1,6)]==[0,7,14,12,0]

rows=[];total=0
for c in range(20,81):
    for d in range(15,114):
        for b in range(15,241):
            if not any((b in exc[2],c in exc[3],d in exc[4])):continue
            if 16*b*d>9*c*c:continue
            alow=max(6,isqrt((12*b+4)//5))
            while 5*alow*alow<12*b:alow+=1
            ahigh=8*b*b//(15*c)
            ehigh=8*d*d//(15*c)
            for e in range(6,ehigh+1):
                fhigh=5*e*e//(12*d)
                for f in range(1,fhigh+1):
                    for a in range(alow,ahigh+1):
                        u=(1,a,b,c,d,e,f)
                        total+=1
                        bad=[k for k in range(1,6) if u[k+1]>K[k][u[k]]]
                        if bad:rows.append((u,bad))
assert total==4445,total
assert len(rows)==22,len(rows)

# Compute root power sums by traces of the multiplication-by-x matrix in Q[x]/(Q).
for u,bad in sorted(rows):
    _,a,b,c,d,e,f=u
    companion=Matrix([[0,0,0,0,0,-f],
                      [1,0,0,0,0,e],
                      [0,1,0,0,0,-d],
                      [0,0,1,0,0,c],
                      [0,0,0,1,0,-b],
                      [0,0,0,0,1,a]])
    ps=[int((companion**j).trace()) for j in range(7)]
    h3=Matrix(3,3,lambda i,j:ps[i+j]).det(method='domain-ge')
    h4=Matrix(4,4,lambda i,j:ps[i+j]).det(method='domain-ge')
    assert h3<0 or h4<0,(u,h3,h4)
    x=symbols('x')
    Q=Poly(x**6-a*x**5+b*x**4-c*x**3+d*x**2-e*x+f,x)
    # Exact real-root isolation; sum multiplicities, not merely distinct roots.
    real_multiplicity=sum(multiplicity for interval,multiplicity in Q.intervals())
    assert real_multiplicity<6,(u,real_multiplicity)
    print(u,'KK',bad,'H3',h3,'H4',h4,'real roots counted with multiplicity',real_multiplicity)
print('PASS: independently checked 4445 candidates, 22 violations, all excluded by exact Hermite minors and real-root isolation.')