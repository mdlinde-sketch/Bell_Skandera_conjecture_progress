"""Independent adversarial checks of the d<=17 finite reduction, 2026-10-18.

All arithmetic exact. Tests necessary-condition bounds on genuine integer-rooted
polynomials, independently checks KK on small colex complexes, and checks
finite-cutoff inequalities at sampled binomial-boundary points. This does NOT
prove the full finite case enumeration or the trace theorem.
"""
from math import comb
from itertools import combinations
from random import Random
from independent_python_frontier_degree17 import kk_next, max_n, max_coeff, cutoff
from third_interval_verifier import lower,local,tan,h3,h4,max_quadratic

rng=Random(20261018)
stats={}

def colex_key(s):return tuple(reversed(s))
# Compare independent combinatorial shadow counting with the binomial algorithm.
colex_tests=0
for vertices in range(2,10):
 for k in range(1,min(4,vertices-1)+1):
  small=sorted(combinations(range(vertices),k),key=colex_key)
  higher=list(combinations(range(vertices),k+1))
  for m in range(1,len(small)+1):
   included=set(small[:m])
   face_count=sum(all(tuple(t) in included for t in combinations(h,k)) for h in higher)
   assert kk_next(k,m)==face_count,(vertices,k,m,face_count,kk_next(k,m))
   colex_tests+=1
stats['colex_kk_tests']=colex_tests

cutoff_tests=0
for d in range(2,18):
 for k in range(1,d):
  r=cutoff(d,k)
  assert comb(r,k+1)**k*comb(d,k)**(k+1) > comb(d,k+1)**k*comb(r+1,k)**(k+1)
  if r>d:
   assert comb(r-1,k+1)**k*comb(d,k)**(k+1) <= comb(d,k+1)**k*comb(r,k)**(k+1)
  for a in range(r,min(r+5,62)):
   left,right=comb(a,k),comb(a+1,k)-1
   for m in {left,right,(left+right)//2}:
    assert kk_next(k,m)>=max_n(d,k,m),(d,k,a,m,kk_next(k,m),max_n(d,k,m))
    cutoff_tests+=1
stats['cutoff_boundary_tests']=cutoff_tests

# True-root controls: multiply factors (1+wt), w=1,2,3. Coefficients are exact.
root_controls=0
for d in range(2,18):
 for trial in range(30):
  roots=[rng.choice([1,2,3]) for _ in range(d)]
  u=[1]
  for w in roots:
   v=[0]*(len(u)+1)
   for i,c in enumerate(u):v[i]+=c;v[i+1]+=w*c
   u=v
  for k in range(1,d):
   m,n=u[k:k+2]
   assert n<=max_n(d,k,m)
   for j in range(1,d+1):
    assert u[j]<=max_coeff(d,k,m,n,j),(d,k,j,roots,u)
   root_controls+=1
stats['positive_root_adjacent_controls']=root_controls

# Test norm-two reversed-coefficient chord/tangent bounds against true roots.
norm2_controls=0
for d in range(6,18):
 u=[comb(d-1,j)+(2*comb(d-1,j-1) if j else 0) for j in range(d+1)]
 assert u[-1]==2
 n,m=u[d-1],u[d-2]
 a3,a4=u[d-3],u[d-4]
 assert lower(d,3,m)<=a3<=local(d,3,m,n)
 assert lower(d,4,a3)<=a4<=min(local(d,4,a3,m),comb(d,4)*m**3*d**2//(comb(d,2)**3*n**2))
 norm2_controls+=1
stats['norm2_chord_controls']=norm2_controls

# Independent check of H4 interval upper bound for actual norm-one integer-rooted polynomials.
# Products of factors (1+t), (1+3t+t^2), (1+5t+6t^2+t^3) all have positive roots and norm one.
FACTORS=[[1,1],[1,3,1],[1,5,6,1],[1,7,13,7,1],[1,7,14,8,1]]
interval_controls=0
for d in range(6,18):
 for trial in range(30):
  q=[1]
  while len(q)-1<d:
   choices=[f for f in FACTORS if len(f)-1<=d-(len(q)-1)]
   f=rng.choice(choices)
   v=[0]*(len(q)+len(f)-1)
   for i,a in enumerate(q):
    for j,b in enumerate(f):v[i+j]+=a*b
   q=v
  assert q[-1]==1
  r=list(reversed(q))
  q1,q2,q3,q4,q5,q6=r[1:7]
  assert lower(d,5,q4)<=q5<=min(tan(d,5,q1,q2),local(d,5,q4,q3))
  lo5=lower(d,5,q4);hi5=min(tan(d,5,q1,q2),local(d,5,q4,q3))
  lo6=lower(d,6,lo5)
  f0,f1,f2=(h4(d,q1,q2,q3,q4,lo5+i,lo6) for i in range(3))
  upper,A=max_quadratic(f0,f1,f2,hi5-lo5)
  assert h3(d,q1,q2,q3,q4)>=0
  assert h4(d,q1,q2,q3,q4,q5,q6)>=0
  assert upper>=h4(d,q1,q2,q3,q4,q5,q6)
  interval_controls+=1
stats['true_norm1_interval_controls']=interval_controls
print('PASS adversarial exact math controls:',stats)
