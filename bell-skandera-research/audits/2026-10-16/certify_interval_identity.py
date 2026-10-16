"""Exact SymPy verification of the degree-16 Hankel interval lemma."""
import sympy as s
D,u1,u2,u3,u4,u5,u6=s.symbols("d u1 u2 u3 u4 u5 u6",integer=True)
q=[None,u1,u2,u3,u4,u5,u6]
p=[D,u1]
for k in range(2,7):
    p.append(s.expand(sum((-1)**(i-1)*q[i]*p[k-i] for i in range(1,k))
                      +(-1)**(k-1)*k*q[k]))
H2=s.Matrix([[p[i+j] for j in range(2)] for i in range(2)]).det(method="domain-ge")
H3=s.Matrix([[p[i+j] for j in range(3)] for i in range(3)]).det(method="domain-ge")
H4=s.Matrix([[p[i+j] for j in range(4)] for i in range(4)]).det(method="domain-ge")
checks={
    "dH3/du4=-4H2": s.simplify(s.diff(H3,u4)+4*H2)==0,
    "dH4/du6=-6H3": s.simplify(s.diff(H4,u6)+6*H3)==0,
    "d2H4/du5²=-50H2": s.simplify(s.diff(H4,u5,2)+50*H2)==0,
    "d3H4/du5³=0": s.simplify(s.diff(H4,u5,3))==0,
}
assert all(checks.values()),checks
print(checks)
