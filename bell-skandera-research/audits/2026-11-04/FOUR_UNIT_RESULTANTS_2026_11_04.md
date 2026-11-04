# 4 November 2026 — four consecutive unit resultants in unbounded irreducible cores

**Exact obstruction to a proof strategy, NOT a Bell–Skandera counterexample or unrestricted proof. Novelty and external/formal verification not claimed.**

For every prime p>=5 let d=(p-1)/2, F_p(t)=sum_(j=0)^d C(2d-j,j)t^j and P_p(x)=x^d F_p(-1/x). The 29 October independent audit proves P_p irreducible, positive-rooted, and F_p is a matching-complex f-polynomial, with unbounded d and excess d-1.

**Theorem (all such primes):** |P_p(0)|=|P_p(1)|=|P_p(2)|=|P_p(3)|=1, and P_p(4)=p.

**Proof:** Put z=zeta_p, alpha=2+z+z^-1. Then P_p(x)=Norm_(Q(z+z^-1)/Q)(x-alpha), so P_p(x)^2=Norm_(Q(z)/Q)(x-alpha). The exact identities are

    1-alpha = -z^-1 (1-z^3)/(1-z)
    2-alpha = -z^-1 (1-z^4)/(1-z^2)
    3-alpha = -z^-1 (1+z^3)/(1+z).

For j=1,2,3,4, Norm(1-z^j)=Phi_p(1)=p, and Norm(1+z^j)=Phi_p(-1)=1, since p>=5 is prime. Norm(-z^-1)=1. Thus P_p(j)^2=1 for j=1,2,3. Since F_p is monic, P_p(0)=(-1)^d. Finally 4-alpha=(1-z)(1-z^-1) has norm p^2, so P_p(4)=p (positive since all alpha<4). QED.

This strictly strengthens the 3 November single-unit-resultant obstruction: even simultaneous nonzero integer evaluations at FOUR consecutive integers cannot alone bound irreducible core degree. It does not rule out higher-coefficient constraints, and does not challenge the 2 November inverse-trace theorem. A standard-library independent exact checker verifies all 166 primes 5<=p<1000, max degree 498. Full dated archive: Bell_Skandera_2026-11-04_four_unit_resultants_audit.zip, with expanded proof, checker, JSON and hashes. No d18 expansion.