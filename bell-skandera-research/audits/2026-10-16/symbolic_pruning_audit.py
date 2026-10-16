"""2026-10-16 exact SymPy audit of determinant pruning identities.
No input from the C++ residual case generator.
"""
import sympy as sp
p = sp.symbols('p0:7')
H2 = sp.det(sp.Matrix([[p[0], p[1]], [p[1], p[2]]]))
H3 = sp.det(sp.Matrix([[p[i+j] for j in range(3)] for i in range(3)]))
H4 = sp.det(sp.Matrix([[p[i+j] for j in range(4)] for i in range(4)]))
S2 = sp.det(sp.Matrix([[p[i+j+1] for j in range(2)] for i in range(2)]))
S3 = sp.det(sp.Matrix([[p[i+j+1] for j in range(3)] for i in range(3)]))
checks = {
    "dH3_dp4_eq_H2": sp.simplify(sp.diff(H3,p[4])-H2)==0,
    "dH4_dp6_eq_H3": sp.simplify(sp.diff(H4,p[6])-H3)==0,
    "dS3_dp5_eq_S2": sp.simplify(sp.diff(S3,p[5])-S2)==0,
    "H3_affine_p4": sp.simplify(sp.diff(H3,p[4],2))==0,
    "H4_affine_p6": sp.simplify(sp.diff(H4,p[6],2))==0,
    "S3_affine_p5": sp.simplify(sp.diff(S3,p[5],2))==0,
}
assert all(checks.values()), checks
for name, value in checks.items():
    print(name, value)
print("With Newton identities, slopes in q4/q6/q5 are -4H2/-6H3/+5S2.")
