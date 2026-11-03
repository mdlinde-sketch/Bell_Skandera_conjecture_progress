# 3 November 2026 — unit-resultant obstruction in unbounded irreducible cores

**Exact adversarial result about a proof strategy; NOT a Bell–Skandera counterexample, unrestricted proof, novelty claim or external review.**

## Theorem

For every prime p>=5, let d=(p-1)/2 and

    F_p(t)=sum_(j=0)^d binom(2d-j,j)*t^j.

Then F_p is monic, constant-one, irreducible over Z, exclusively negative-real-rooted, and is a simplicial face polynomial (matching complex of the path on 2d vertices). Moreover

    F_p(-1)=+1 for p=1 (mod 6), and -1 for p=5 (mod 6).

Thus the monic totally-positive reciprocal P_p(x)=x^d F_p(-1/x) has

    |P_p(1)|=1

despite having arbitrarily large degree d, no root at x=1, and unbounded coefficient excess s=a_1-d=d-1. **The basic integer-resultant inequality |P(1)|>=1 is exactly saturated by an infinite family of irreducible high-degree cores.** It cannot by itself bound their degrees.

## Proof

The j-th coefficient counts j-matchings in a path on 2d vertices. The path-matching polynomial has exclusively negative real roots; its positive reciprocal-root parameters are 4cos²(k*pi/p), k=1,...,d. For prime p these are conjugates of 2+zeta_p+zeta_p^(-1), a generator of the real cyclotomic subfield of degree d, proving irreducibility. The construction and irreducibility are also proved in audits/2026-10-29/independent_followup/AUDIT.md.

For the path on n vertices, the matching polynomial R_n satisfies R_n=R_(n-1)+t*R_(n-2), with R_0=R_1=1. Evaluating at t=-1 gives the repeating six-term sequence 1,1,0,-1,-1,0. Every prime p>=5 is 1 or 5 modulo 6, so n=p-1 is 0 or 4 modulo 6. Therefore F_p(-1)=R_(p-1)(-1)=+1 or -1 respectively, and P_p(1)=F_p(-1). QED.

## Checks and limitations

The 2 November ZIP's SHA256 hashes and exact-rational certificate were independently rerun and passed. Its g derivative, stationary points, summation and P(1) integrality argument were checked without finding a defect. GitHub HEAD before this audit was 8c55feb8379a61041530f933462c8f7ba55a9a60, with no later commits.

A standalone standard-library exact checker verifies coefficients, the six-period recurrence, and |F_p(-1)|=1 for all 166 primes 5<=p<1000 (largest 997). A reproducible ZIP containing this note, checker, JSON results and SHA256 manifest is saved as Bell_Skandera_2026-11-03_unit_resultant_obstruction_audit.zip.

This does NOT refute using multiple integer evaluations P(j) or coefficient-sensitive resultants; it refutes only a proposed degree bound from the single evaluation |P(1)|>=1. The path family itself satisfies all KK inequalities. Future approaches must use richer global arithmetic and intermediate-coefficient information. No degree-18 expansion or blind excess increment was performed.
