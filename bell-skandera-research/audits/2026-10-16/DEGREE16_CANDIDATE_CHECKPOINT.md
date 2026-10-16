# Bell–Skandera: degree-16 research checkpoint — 2026-10-16

**UNREVIEWED candidate computer-assisted result through degree 16. NOT an established proof, published theorem, novelty determination or an all-degree resolution.** Preserve earlier checkpoints and full 15 October candidate proof.

## New exact Hankel interval lemma

For fixed coefficients q1,...,q4 of a monic reciprocal polynomial with positive roots, Newton's power sums and the Hankel moment determinants satisfy

- derivative H4 with respect to q6 is -6 H3;
- second derivative H4 with respect to q5 is -50 H2;
- third derivative H4 with respect to q5 is zero.

Here Hr is the determinant of the r-by-r moment matrix. Real positive roots require H2 and H3 nonnegative. Consequently H4 is nonincreasing in q6 and a concave quadratic in q5. If the exact integer coefficient constraints require L5 <= q5 <= U5 and q6 >= L6(q5), where L6 is nondecreasing, then
H4(q5,q6) <= H4(q5,L6(L5)).
Compute the maximum of the right-hand quadratic exactly using its endpoints and the two integers nearest its vertex. A strictly negative maximum excludes the *entire interval* of q5 values without testing each integer.

SymPy established the exact derivative identities. A fresh Python verifier independently reconstructed all coefficient prefixes and evaluated the 4-by-4 determinant using its direct permutation expansion, rather than the C++ Schur formula. **It still consumes the same C++-generated list of residual cases**, so the classification is NOT independently certified by this test.

## Results

| Degree | Initial KK-violating pairs | Norm-one residual cases | Special cases | Negative interval blocks | q5 integer values ruled out | Survivors |
|---|---:|---:|---:|---:|---:|---:|
| 14 | 1,466,064 | 306 | 4 | 37,520 | 4,370,337 | 0 |
| 15 | 5,171,064 | 580 | 11 | 104,612 | 17,462,898 | 0 |
| 16 | 18,426,173 | 1,016 | 22 | 256,006 | 61,662,703 | 0 |

For degree 16, the frontier was produced by **five disjoint runs covering every k=1,...,15** (k1–5, k6–8, k9–10, k11, k12–15), then recombined and verified. Complete category partition: original Smyth factor reduction 18,375,775; final-coefficient impossibility 1,026; reversed Smyth factor reduction for norm one 48,334; norm-one residual 1,016; special norm-three-capable pairs 22. The totals sum to 18,426,173.

Residual indices: k12 (3), k13 (896), k14 (117); all 22 specials k14. The generalized verifier includes an additional k=d-4 case and enumerates both initial reversed coefficients. The C++ execution examined 1,038 residual-plus-special pairs, 7,314 admissible prefixes, 17,945 q3 nodes and 257,017 q4 nodes. Exactly 256,006 permitted q5 intervals were excluded, containing 61,662,703 integers; zero survivors. The Python permutation-determinant verifier independently obtained exactly the same excluded interval and integer totals, with zero uncleared intervals (it counts 256,337 q4 prefixes with nonnegative H3 rather than the C++ total including failed H3 checks).

All 22 special norm-two cases fail the necessary exact Hankel H3 check (largest computed maxima range from −465,675,264 to −1,010,181,528). Norm three is eliminated conditionally on the inverse-trace lemma because u_(d-1) <=53 implies u_(d-1)/3 + 1.5 log(3) < 53/3+3 < 29*16/20, forcing the reducible factor (1+t). Earlier norm-two cases satisfy the inverse-trace sufficient integer condition.

## Status and reproduction

Generated package: `Bell_Skandera_2026-10-16_degree16_candidate_and_interval_certificate.zip` (full executed C++17 and Python source, segmented degree-16 list and combined JSON, and logs). **This package is not necessarily on GitHub; confirm any upload.** The older original degree-14 ZIP is present in the repository. The complete proof candidate still depends on Smyth 1984 hypotheses, exceptional polynomial factor/reciprocal induction, KK finite cutoff and rounding, PSD necessity, inverse-trace lemma and complete case classification.

C++ frontier uses 128-bit root-power arithmetic for k<=12; the maximum computed bit length at d16 is 122, and k>=13 and decision comparisons use Boost arbitrary-precision arithmetic. Do not extend beyond degree 16 without rechecking overflow bounds.

The recent literature (Bell–Skandera 2007; Mu–Welker 2026; Liu–Wang–Zhang 2026) leaves the general conjecture open, but a brief search does **not** establish novelty of our candidate finite-degree result.

**Next priority: independently reconstruct the complete d16 finite frontier in another implementation / machine-checkable certificate and audit every mathematical reduction before advancing further.**