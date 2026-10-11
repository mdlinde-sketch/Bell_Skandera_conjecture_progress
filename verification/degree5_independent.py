"""Independent certificate: explicit colex simplicial complexes and companion-matrix traces.
Not derived from the original binomial-expansion KK routine or determinant code.
"""
from itertools import combinations
from math import comb
from sympy import symbols, Poly, Matrix, oo

# Independently calculate maximum shadows by constructing actual colex complexes.
def face_capacity(k):
    faces = sorted(combinations(range(15), k), key=lambda s: s[::-1])
    rank = {s: i for i, s in enumerate(faces)}
    threshold_counts = [0] * (len(faces) + 1)
    for high_face in combinations(range(15), k+1):
        last_needed = max(rank[part] for part in combinations(high_face,k))
        threshold_counts[last_needed + 1] += 1
    running = 0
    for i in range(len(threshold_counts)):
        running += threshold_counts[i]
        threshold_counts[i] = running
    return threshold_counts

capacities = {k:face_capacity(k) for k in range(1,5)}
exceptions = {}
for k in range(1,5):
    exceptions[k]=[]
    for m in range(comb(5,k),comb(14,k)):
        kk=capacities[k][m]
        # Necessary condition for coefficient >= kk+1 consistent with Maclaurin:
        if (kk+1)**k * comb(5,k)**(k+1) <= comb(5,k+1)**k * m**(k+1):
            exceptions[k].append(m)
assert exceptions == {1:[],2:[11,12,13,17,18],3:[12,13,14,15,17],4:[]}
print('EXCEPTIONS',exceptions)

# Exhaust full independently derived Newton integer intervals, no arbitrary caps.
violations=[]
checked=0
for b in range(10,29):
  for c in range(10,33):
    for a in range(5, b*b//(2*c)+1):
      if 2*a*a < 5*b: continue
      for d in range(5, c*c//(2*b)+1):
        for e in range(1, 2*d*d//(5*c)+1):
          if b not in exceptions[2] and c not in exceptions[3]:
              continue
          checked+=1
          coeff=[1,a,b,c,d,e]
          bad=[(k,coeff[k+1],capacities[k][coeff[k]]) for k in range(1,5) if coeff[k+1]>capacities[k][coeff[k]]]
          if bad: violations.append(((a,b,c,d,e),bad))
print('CANDIDATES',checked)
print('VIOLATORS',len(violations))
assert checked == 125
expected_rows = {(6,12,12,6,1),(6,13,14,6,1),(6,13,14,7,1),
                 (6,14,14,7,1),(7,14,14,7,1),(6,14,15,8,1)}
assert {row for row,bad in violations} == expected_rows

x=symbols('x')
for (a,b,c,d,e),bad in violations:
    poly=Poly(x**5-a*x**4+b*x**3-c*x**2+d*x-e,x)
    C=Matrix([[0,0,0,0,e],[1,0,0,0,-d],[0,1,0,0,c],[0,0,1,0,-b],[0,0,0,1,a]])
    p=[int((C**j).trace()) for j in range(7)]
    h3=Matrix(3,3,lambda i,j:p[i+j])
    h4=Matrix(4,4,lambda i,j:p[i+j])
    real_count=poly.count_roots(-oo,oo)
    D3=int(h3.det(method='domain-ge')); D4=int(h4.det(method='domain-ge'))
    assert D3 < 0 or D4 < 0
    assert real_count < 5
    print('ROW',(a,b,c,d,e),'BAD',bad,'H3',D3,'H4',D4,'REAL_DISTINCT',real_count)
print('PASS: independently verified all six candidates fail real-rootedness.')