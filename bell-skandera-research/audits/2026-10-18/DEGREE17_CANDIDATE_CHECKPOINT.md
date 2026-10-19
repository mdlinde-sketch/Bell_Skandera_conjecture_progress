# Bell–Skandera degree-17 independent audit — 18 October 2026

**UNREVIEWED candidate computer-assisted finite-degree result through d=17. NOT a peer-reviewed proof, all-degree solution, or verified novelty claim.** This extends the d16 checkpoint without altering historical work.

## Frontier classification (exact integer arithmetic)
A pure-Python frontier generator classified every k=1,...,16 for d17 via 15,176 m-intervals and 969,827 explicitly evaluated (m,n) pairs. Remaining: **2,142 norm-one residual pairs** (k13: 483, k14: 1,508, k15: 151) and **37 special pairs** (all k15). Each special allows final coefficient at most three.

An independently implemented C++17/Boost interval-frontier generator reproduced **the exact Python case lists and interval/check counts for every d=2,...,17**, covering all k. The original C++ brute frontier also independently reproduced d17 k13–16 lists.

SHA256 canonical sorted Python residual list: `f2763600f7244981a711a4d581b078afa3cc285b9d847300b112995eb7b121e0`.
SHA256 canonical sorted Python special list: `48f93be87cc5fc15fc6ba20d104630633a35466d114462459be6cee5754763b7`.

## Exact determinant exclusions
Independent Python Leibniz 4×4 and C++17/Boost Schur-complement Hankel verifiers both handled 2,179 cases and 113,409 q1/q2 prefixes, 69,201 q3 nodes and **578,295 strictly-negative quadratic q5 intervals**, ruling out **193,610,278** q5 integer possibilities; **zero survivors**. These programs independently evaluate determinants but use the generated candidate list. All 37 norm-two special cases fail exact H3 (largest maximum -722,782,224). Norm-three exclusion is conditional on the 17 October inverse-trace lemma: u_(d-1) <=57 and 20*57+180<87*17 imply a (1+t) factor.

The exact interval step assumes H2,H3>=0 and uses dH4/dq6=-6 H3 and d²H4/dq5²=-50 H2. Monotone exact lower chord q6>=L6(q5)>=L6(L5) reduces each q5 interval to maximum of an explicit concave quadratic.

## Falsification controls
18 Oct controls passed: 623 explicit colex-vs-KK examples; 1,880 exact cutoff boundary tests; 4,080 coefficient tests on genuine positive-root polynomials; 12 norm-two reversed chord/tangent checks; 360 real-rooted interval controls. They do not substitute for a formal completeness argument.

## Critical limits
The executable research archive generated 18 October is `Bell_Skandera_2026-10-18_degree17_candidate_audit.zip`. This checkpoint **does not claim the ZIP is already in GitHub**. See the same-date reproduction note and scripts if committed. Outstanding: prove KK cutoff and coefficient enumeration cover all cases, inspect Smyth (1984) hypotheses and exceptions, validate factor/reciprocal join induction, formalize inverse-trace and PSD arguments, review overflow and all DFS paths, and obtain independent specialist/formal review. No degree-18 or all-degree claim.

Related bibliography: Smyth, *Totally positive algebraic integers of small trace* (1984), DOI 10.5802/aif.975; Bell–Skandera (2007); Mu–Welker (2026); Liu–Wang–Zhang (2026). Novelty has not been established.
