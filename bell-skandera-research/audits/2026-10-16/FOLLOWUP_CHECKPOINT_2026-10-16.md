# Bell–Skandera research: independent follow-up, 16 October 2026

**Status: UNREVIEWED candidate result through degree 14; no established proof or novelty claim.** Incremental audit of `Bell_Skandera_2026-10-16_independent_degree14_audit (8).zip`, not a replacement for its primary research note.

## Checks reported from 16 October session

1. Inspected Smyth's 1984 *Totally positive algebraic integers of small trace*, printed page 2: trace > 1.7719d apart from five listed exceptional minimal polynomials (x-1; x²−3x+1; x³−5x²+6x−1; x⁴−7x³+13x²−7x+1; x⁴−7x³+14x²−8x+1). Primary PDF https://www.numdam.org/item/10.5802/aif.975.pdf . Application to reducible polynomials still needs review.
2. Recompiled archival independent C++ frontier for d14: raw 1,466,064; Smyth original reduced 1,458,754; coefficient cap impossible 260; reversed Smyth reduced 6,740; norm-one residual 306; inverse-lemma norm-two eliminated 301; four special cases. JSON matched archived result.
3. Compiled shifted-augmented C++ DFS using additional shifted S2/S3 necessary tests: 310 residual and special cases; 1,614 initial accepted prefixes; depth3 5,255; depth4 37,779; depth5 4,370,337; depth6 zero; zero survivors. Shifted tests pruned zero *additional* cases. This shares the original DFS structure and is NOT an independent third verifier. A prior standalone C++ rerun timed out and must not be counted as success.
4. Executed archived norm-two H3 special test: all four fail, maximum H3 negative. Executed six exceptional-factor controls, all H3/H4 nonnegative.
5. Symbolic SymPy determinant audit proved dH3/dp4=H2; dH4/dp6=H3; dS3/dp5=S2 and affine dependence. With Newton identities the coefficient slopes are -4H2, -6H3, +5S2. Interval-pruning direction verified conditional on preceding PSD minors.
6. Independent canonical-binomial KK upper-shadow checks on Smyth exception polynomials and reciprocals passed.
7. Five hundred seeded degree-14 positive-root polynomials verified Newton identities and PSD H3/H4/S3 using exact arithmetic.
8. Independent full Python d14 frontier reconstruction exceeded the execution limit; its full-list equality against C++ remains UNVERIFIED.

## Outstanding risks

- Full recursive DFS coverage, integer bound direction/rounding, Smyth applications and exceptional reductions, KK cutoff monotonicity, reciprocal factor induction and inverse trace lemma require independent mathematical scrutiny.
- Need independent third verifier or small machine-checkable proof certificate. Symbolic checks alone do not establish completeness.
- Literature novelty and priority not established; avoid claiming theorem.
- This checkpoint preserves *reported* 16 October test outcomes. The source scripts are committed beside it for reproducibility. Read all numerical claims as candidate evidence pending third-party replication.
