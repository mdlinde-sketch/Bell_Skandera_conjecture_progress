# Bell–Skandera: independent research audit, 16 October 2026

**Status: UNREVIEWED candidate computer-assisted theorem through degree 14. Not an all-degree proof.** This supplements, without replacing, the 15 October degree-12/13 candidate notes and the older unfinished degree-12 brute-force checkpoints.

## What was actually executed

A newly written standalone C++17/Boost generator, `independent_frontier_20261016.cpp`, independently reconstructs the exact Kruskal–Katona/Maclaurin adjacent-pair frontier and trace/factor classification; it does **not** read the primary Python verifier's case list. Its scaled 256th-root upper bound is a rigorous integer-only bound, followed by exact Boost-integer comparisons. An independently written Python generator matched the **complete** degree-12 residual list and category counts, not merely the total.

| Degree | Initial pairs | Residual norm-one cases | Extra special cases |
|---:|---:|---:|---:|
| 9 | 2,940 | 2 | 0 |
| 10 | 10,226 | 6 | 0 |
| 11 | 34,948 | 13 | 0 |
| 12 | 120,676 | 29 | 0 |
| 13 | 418,796 | 81 | 0 |
| 14 | **1,466,064** | **306** | **4** |

The degree-14 category partition is: 1,458,754 original-Smyth-reduced, 260 impossible by the final-coefficient upper bound, 6,740 reversed-Smyth-reduced for norm one, 306 residual norm-one pairs, and 4 special pairs permitting final coefficient 3. The 306 norm-one residual cases contain 301 possible norm-two branches, all reduced by the inverse-trace lemma, and 5 cases allowing only norm one. The four special pairs are `(k,m,n)=(12,268,43),(12,273,44),(12,274,44),(12,279,45)`.

The independent degree-14 unit-norm verifier, `independent_unitnorm_d14_20261016.cpp`, consumes **this newly generated case list**, enumerates exact Newton-tangent/local/chord coefficient intervals, and tests the necessary unshifted Hankel determinants H3 and H4 using arbitrary-precision permutation determinants. It examined all **310** norm-one residual/special cases: 1,614 admissible starting q1 prefixes; 5,255 depth-3 nodes; 37,779 depth-4 nodes; 4,370,337 depth-5 nodes; **zero admissible depth-6 nodes; zero survivors**. It uses only the proven nonpositive affine slopes in q4/q6 for interval pruning. Six constructed positive-rooted degree-14 controls from products of Smyth exception factors passed H3/H4 tests.

The four special **norm-two** branches were independently checked by `audit_norm2_degree14_20261016.py`. On reversing the polynomial and scaling the reciprocal roots by 2, the first elementary symmetric functions are integral. For every allowed q3 the exact H3 determinant is already negative at the smallest allowable q4, and decreases with q4. Maximum H3 determinants for the four pairs, respectively: `-203612864`, `-251319136`, `-241075200`, `-294303096`. The **norm-three** branch is forced to have F(-1)=0 by the inverse-trace inequality: u_(d-1)<=45, so u_(d-1)/3 + 1.5 log 3 < 15+3 < 29*14/20 (using log 3<2).

## New short exact proof of the inverse-trace bound

Define h(x)=x-(3/4)log(x|x-1|), x>0, x !=1. On each of (0,1) and (1,infinity), h''(x)=(3/4)(1/x^2+1/(x-1)^2)>0.

**0<x<1:** At x0=7/20, h'(x0)=1/91, so convexity yields h(x)>=h(7/20)-7/1820. Put z=309/491. The positive-term atanh expansion yields

    log(400/91) > 2(z+z^3/3+z^5/5+z^7/7) > 59/40.

The last inequality is exact rational arithmetic. Consequently

    h(x)>7/20+(3/4)(59/40)-7/1820 = 3021/2080 > 29/20.

**1<x<3:** At x0=43/20, h'(x0)=-1/989, so h(x)>=h(43/20)-17/19780. By the positive exponential series,

    exp(23/25)>1+23/25+(23/25)^2/2+(23/25)^3/6
              =115921/46875 > 989/400.

Therefore log(989/400)<23/25 and

    h(x)>43/20-(3/4)(23/25)-17/19780
        =144309/98900 > 29/20.

**x>=3:** h'(3)=3/8>0 and h''>0. Also exp(2)>1+2+2+8/6>6, so log 6<2. Thus h(x)>=h(3)>3/2>29/20.

This replaces the numerical stationary-point bounds in the original inverse-trace lemma with a short, entirely rational certificate. Summing h(1/lambda_i) gives the lemma from the 15 October candidate note.

## Reproduction

Run in this directory (Boost headers required):

```sh
g++ -O3 -std=c++17 independent_frontier_20261016.cpp -o independent_frontier
./independent_frontier 12
./independent_frontier 13
./independent_frontier 14
g++ -O3 -std=c++17 independent_unitnorm_d14_20261016.cpp -o independent_unitnorm_d14
./independent_unitnorm_d14
python3 audit_norm2_degree14_20261016.py
g++ -O3 -std=c++17 test_hankel_controls_20261016.cpp -o test_hankel_controls
./test_hankel_controls
```

**Scope of exactness:** The 256th-root accelerator uses unsigned 128-bit integers. It was designed and tested only through degree 14; do not reuse at larger degrees without a new overflow proof. The low-degree classification also uses 64-bit binomial tables, sufficient in the tested range. The finite-frontier reduction and moment-PSD necessity remain mathematical dependencies that require external specialist review.

## Literature and outstanding issues

Sources reviewed: Smyth (1984), *Totally positive algebraic integers of small trace*, DOI 10.5802/aif.975; Mu–Welker (2025/2026), arXiv:2503.24076; Liu–Wang–Zhang (September 2026), arXiv:2609.23694. The last paper disproves a **different** recursive-decomposition conjecture. No matching published degree-14 theorem was identified in this limited search, which does not establish novelty.

**Remaining risks:** independent mathematical review of Smyth applicability/exceptions, factor and reciprocal induction, KK cutoff monotonicity, exact integer interval coverage and affine Hankel pruning; independent degree-14 full-frontier reproduction in another implementation; and a machine-checkable proof/certificate. No all-degree proof is claimed.

**Repository write status at time of original audit:** GitHub connector create-file attempts on 16 October were blocked by a safety check. The repository was subsequently renamed and writes became possible. Original ZIP remains archived verbatim at repository root.
