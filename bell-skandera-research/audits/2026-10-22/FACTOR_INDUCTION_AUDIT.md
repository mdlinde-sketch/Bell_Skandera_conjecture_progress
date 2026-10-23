# 22 October 2026 — Smyth exceptional-factor induction audit

**UNREVIEWED finite-degree candidate through d=17, not a refereed theorem or unrestricted solution.**

For F(t)=∏(1+λ_i t)∈Z[t] with λ_i>0 and F(0)=1, define P(x)=x^dF(−1/x), a monic integer polynomial with positive roots. If a Smyth exceptional monic E divides P in Q[x], then P=ER with R monic integer by Gauss's lemma. Writing F_E(t)=(−t)^e E(−1/t), F_R(t)=(−t)^(d−e)R(−1/t), one has F=F_E F_R; both factors have integer coefficients, constant 1, and strictly negative roots. Since F_E is a valid simplicial f-polynomial and deg(F_R)<d, induction plus simplicial join handles F.

For norm u_d=1, the monic reciprocal Q(x)=(−1)^d x^dP(1/x) has positive roots. An exceptional factor E|Q gives its reciprocal E*(x)=(−1)^e x^e E(1/x) dividing P. Its F_E* is the coefficient reversal of F_E, also an f-polynomial. The same join induction applies. Repeated factors may be extracted one by one.

Exact standard-library Python programs committed here independently construct colex-initial simplicial complexes for all five exceptional f-polynomials and five coefficient reversals; check face closure, facets and f-vectors; explicitly verify all 100 pairwise joins; and count all positive roots of the five original exceptional polynomials using rational Sturm chains. All tests passed. These checks establish constructive witnesses and test the algebraic step; they do not prove Smyth's trace bound.

The 21 Oct frontier certificate was rerun on 22 Oct: 7,596 disjoint leaves, 969,827 explicit adjacent pairs, 2,142 residual, 37 specials, exact hash matches. Independent Bareiss Hankel verification completed in 34.74 sec: 6,573,665 q4 checks, 578,295 negative H4 intervals, 193,610,278 excluded q5 integers, zero survivors; largest H4 upper bound −328,673,910,854. Norm-two full grid: 539,000 exact H3 checks, all negative, largest H3 −722,782,224. These are reproductions, not a degree extension.

The complete self-contained archive is `Bell_Skandera_2026-10-22_factor_induction_audit.zip`; its compressed witness and generated JSON data are **not** represented by this short GitHub note. Refer to the archive for full independent execution evidence. Next: scrutinize Smyth theorem hypotheses, cutoff, coefficient rectangles, and Hankel PSD interval coverage; pursue independent expert/formal verification before degree 18.
