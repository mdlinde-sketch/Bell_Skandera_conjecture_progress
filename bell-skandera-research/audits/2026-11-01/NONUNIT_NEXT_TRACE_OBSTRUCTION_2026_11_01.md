# 1 November 2026 — exact obstruction ONE integer above the nonunit boundary

**Not a counterexample to Bell–Skandera.** This is a counterexample only to extending the previous all-degree integer-resultant proof unchanged.

For every d>=2 let F_d(t)=(1+t)^(d-2)(1+4t+2t²). Its quadratic factor has two strictly negative real roots (discriminant 8>0) and is itself an f-polynomial on four vertices with two edges. The entire family is integer, strictly negative-rooted and simplicial, with

    a_d=2;  a_(d-1)=4+2(d-2)=2d.

The norm-scaled reciprocal polynomial for N=2 has roots beta_i=2+sqrt(2),2-sqrt(2), and d-2 copies of 2, hence

    B_2(x)=(x²-4x+2)(x-2)^(d-2);
    B_2(1)=(-1)^(d-1), a NONZERO integer.

In particular beta_min=2-sqrt(2)<1. The two critical steps of the sharp trace (2d-1) rigidity proof — beta>=1 and forced B_2(1)=0 — fail immediately at trace 2d, even for genuinely integral negative-real-rooted polynomials.

For every d>=3 a_(d-2)=d²-d-1, while the downward Kruskal–Katona shadow is D_(d-1)(2d)=d²-d-2. This family satisfies penultimate KK with exact slack 1. Thus the obstruction is against the **naive proof extension**, NOT the conjecture.

Next mathematical target: find inequalities involving nonzero integer B_N(1), possibly additional integer evaluations B_N(m), which enforce interior KK beyond the sharp norm-two boundary. Avoid blind degree extension. Independently tested via exact integer witness d=2..250; see dated ZIP Bell_Skandera_2026-11-01_nonunit_trace_boundary_audit.zip.
