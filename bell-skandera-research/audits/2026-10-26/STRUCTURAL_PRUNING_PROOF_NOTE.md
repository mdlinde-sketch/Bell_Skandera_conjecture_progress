# 26 October 2026 — adversarial mathematical-reduction audit

**UNREVIEWED candidate finite-degree result through d=17. No all-degree proof, external verification, or novelty claim.**

## Complete interval-rectangle pruning: mathematical justification

Write F(t)=sum(u_j t^j)=prod(1+lambda_i t), with lambda_i>0, and C_j=binom(d,j). A KK violation at k means m=u_k and n=u_(k+1)>=K_k(m)+1. Newton log-concavity gives n^k C_k^(k+1)<=C_(k+1)^k m^(k+1). Let Nmax(m) be the floor of the corresponding upper bound for n. Both K_k and Nmax are nondecreasing.

For every m in an interval [a,b], any violating n satisfies K_k(a)+1<=n<=Nmax(b). Therefore K_k(a)+1>Nmax(b) rigorously excludes the entire interval. Otherwise the exact Newton upper bound on the trace u1 for k>1 is floor[d*m^k*C_(k+1)^(k-1)/(C_k^k*n^(k-1))]. It is nondecreasing in m and nonincreasing in n, so the single endpoint (b,K_k(a)+1) upper-bounds every trace in the rectangle. For k=1, u1=m<=b. If that cap is at most 17719*d/10000, Smyth's trace theorem plus the exceptional-factor induction eliminates the rectangle. The previously established strictly increasing T_k(r)=C(r,k+1)^k/C(r+1,k)^(k+1) provides a persistent finite cutoff.

## Hankel H4 interval dominance: symbolic, rank-independent proof

For q_j the elementary symmetric coefficients of positive reciprocal roots and p_j their Newton power sums, define H2=det(p_(i+j)) for i,j=0,1 and H3 for i,j=0,1,2. The 4x4 Hankel determinant is H4. Write M for its leading 3x3 block and v=(p3,p4,p5). The polynomial identity H4=p6 det(M)-v^T adj(M) v holds even if M is singular. Newton identities imply dp6/dq6=-6, dp5/dq5=5, dp6/dq5=6q1. Consequently dH4/dq6=-6H3 and the q5^2 coefficient in H4 is -25H2. Positive-root moment matrices are positive semidefinite, so H2,H3>=0.

For any admissible integer q5 in [L5,U5], the Newton lower chord forces q6>=L6(q5)>=L6(L5). Thus H4(q5,q6)<=H4(q5,L6(L5)). This last expression is a concave quadratic in q5, whose maximum on the integer interval occurs at an endpoint or one of the two integers adjacent to the vertex. A strictly negative upper maximum excludes the entire q5 interval. This proves the soundness of the *mathematical* H4 pruning rule conditional on valid coefficient bounds and exhaustive q1..q4 enumeration.

For the norm-two H3 envelope, q3=4a3 and q4=8a4 imply dH3/da4=-32H2 and coefficient(a3^2)=-144d, explaining the earlier 74-case quadratic certificate.

## Exact independent checks and rerun

A new standalone Python standard-library audit, with direct Leibniz determinants and no imports from prior Bareiss/Schur code, passed: 2,176 cutoff crossing/persistence checks, 3,400 rectangle monotonic comparisons, 2,012 trace-cap comparisons, all 7,596 archived d17 frontier leaves, 3,000 H4 derivative/concavity identities, 2,000 norm-two H3 identities, and 4,000 genuine positive-integer-root coefficient-bound controls.

The generalized Bareiss d17 verification was rerun **to completion on 26 October**, correcting the incomplete 25 October attempt: 2,179 cases; 6,573,665 q4 checks; 578,295 strictly negative H4 intervals; 193,610,278 q5 integer possibilities excluded; zero survivors; largest H4 upper bound -328,673,910,854. This reproduces the earlier complete 24 October run and does not constitute a new algorithm.

## Unresolved obligations

No flaw was found by these checks. The full argument still depends on the exact factorwise Smyth theorem, exceptional/reciprocal induction, KK shadow theorem, Newton coefficient bounds, inverse-trace lemma, certificate completeness, and correct implementation. The two structural identities above are not Lean/Coq formalizations or independent specialist review. Do not extend to degree 18 before a mathematical review of these links.
