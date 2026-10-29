> **29 October follow-up correction:** Two Smyth exceptions were reversed in the earlier small-excess note. The corrected all-degree s<=3 proof and independently reproduced s<=6 certificate, with precise scope and an all-order Hankel identity, are in the [adversarial follow-up audit](audits/2026-10-29/independent_followup/AUDIT.md). The unrestricted conjecture remains unproved. Earlier trace-factor reductions require the corrected exception orientation; no new finite-degree extension is claimed.

> **CURRENT CHECKPOINT — 29 OCTOBER 2026:** The candidate finite-degree Bell–Skandera result remains **UNREVIEWED through d=17**. A new [29 October independent norm-one H4 monotone-corner audit](audits/2026-10-29/AUDIT_2026-10-29.md) proves an exact polynomial identity showing that if the 4×4 Hankel determinant and its q5 slope are both negative at the lower Newton-chord corner, H4 stays negative for **every** larger admissible q5 and q6. A new exact adjugate/cofactor [checker](audits/2026-10-29/h4_monotone_corner_certificate_20261029.py) verified **all 979,103 H3-nonnegative q4 prefixes across d9–17**, including 1,073 previously skipped empty-q5 prefixes, and found **strictly negative corner determinants and slopes throughout**. It independently checked 1,500 direct 4×4 Leibniz identities/derivatives, fixed input-list SHA256 digests and five deliberate tamper cases. This removes the q5 upper-bound, quadratic vertex and q5-interval maximization steps from the **norm-one branch**, conditional on the already audited frontier and q1..q4 prefix coverage. [Reproduction instructions](audits/2026-10-29/REPRODUCE_FROM_GITHUB_2026-10-29.md). No established theorem, novelty, unrestricted proof, external specialist or Lean/Coq verification is claimed. No degree-18 extension; prioritize independent scrutiny.
---

> **CURRENT CHECKPOINT — 28 OCTOBER 2026:** The candidate finite-degree Bell–Skandera result remains **UNREVIEWED through d=17**. A new [28 October exact norm-two corner audit](audits/2026-10-28/AUDIT_2026-10-28.md) proves that for all 74 exceptional norm-two rows d14–17, the 3x3 Hankel determinant is strictly decreasing in both free coefficient variables throughout their admissible ranges. Therefore **one exact determinant evaluation at the lower corner per row** excludes all 74; the earlier quadratic-vertex maximization and 815,161-point grid are unnecessary for this branch. A standalone standard-library [checker](audits/2026-10-28/norm2_corner_certificate_20261028.py), [tamper tests](audits/2026-10-28/test_norm2_corner_tampering_20261028.py), and [reproduction instructions](audits/2026-10-28/REPRODUCE_FROM_GITHUB.md) are committed. All 16 frontier certificates d2–17 and all d9–17 Bareiss checks were rerun; the final d17 rerun completed with zero survivors, matching the 26 Oct result. No external specialist or Lean/Coq review has occurred. **No established theorem, novelty or unrestricted proof is claimed.** Do not extend d18 before independent scrutiny.
---

> **CURRENT CHECKPOINT — 27 OCTOBER 2026:** The finite-degree Bell–Skandera candidate remains **UNREVIEWED through d=17**. The [27 October exact norm-three audit](audits/2026-10-27/AUDIT_2026-10-27.md) independently proves the inverse-trace pointwise bound with exact rational enclosures and proves log(3)<11/10 by a fifth-order exponential Taylor bound. The resulting strict integer obstruction 20u_(d−1)+99>87d excludes **all 74 norm-three special rows** in degrees 14–17 (conditional on removing any x−1 factor by induction). Five deliberately corrupted case lists were rejected. A [specialist review brief](audits/2026-10-27/SPECIALIST_REVIEW_BRIEF_2026-10-27.md) lists proof dependencies and highlights a separate disproved Mu–Welker auxiliary conjecture that must not be confused with Bell–Skandera. [Reproduction instructions](audits/2026-10-27/REPRODUCE_FROM_GITHUB.md) and exact Python source are committed and readback-verified. The 26 October structural-pruning proof audit and complete degree-17 Bareiss rerun remain authoritative for the other branches. **No peer-reviewed theorem, novelty claim, or unrestricted proof is established.** Independent specialist/formal review remains the priority; do not extend d18 yet.
---

> **CURRENT CHECKPOINT — 26 OCTOBER 2026:** The Bell–Skandera finite-degree candidate remains **UNREVIEWED through d=17**. A new [26 October structural proof audit](audits/2026-10-26/STRUCTURAL_PRUNING_PROOF_NOTE.md) derives exact KK/Newton rectangle-pruning monotonicity and the rank-independent bordered-determinant identities underpinning the H4 concave interval exclusion and norm-two H3 envelope. A new [independent exact identity checker](audits/2026-10-26/hankel_structural_identity_checker_20261026.py) passed 3,000 H4 and 2,000 norm-two controls. The full dated archive also checks 2,176 cutoff instances, 3,400 rectangle comparisons, 2,012 trace comparisons, all 7,596 d17 witness leaves and 4,000 positive-root coefficient controls. The 25 October timed-out d17 Bareiss rerun was **completed successfully on 26 October**: 2,179 rows, 6,573,665 q4 checks, 578,295 strictly negative H4 intervals excluding 193,610,278 q5 integers, zero survivors, matching the 24 October result. [Reproduce the 26 October checks](audits/2026-10-26/REPRODUCE_FROM_GITHUB.md). The [25 October lower-degree audit](audits/2026-10-25/AUDIT_2026-10-25.md) remains authoritative for d2–16. **No peer-reviewed theorem, novelty claim or unrestricted proof is established.** Seek formal/external mathematical review before d18. Historical degree-12 work below is superseded.
---




# Bell–Skandera: degree-12 research checkpoint

Last updated: **14 October 2026, evening (Brisbane)**.

**Resume at degree 12, not the older degree-7 package.** Candidate certificates through degree 11 were reported in an earlier shared research log, but the original degree-11 verifier/certificates have not yet been independently recovered or reviewed. Nothing here constitutes a proof of Bell–Skandera.

Original shared research checkpoint: https://chatgpt.com/share/6accb4a5-2d88-83ec-bf9d-05544e8303f2

## Current exact degree-12 computational frontier

The finite reduction yields **120,676** putative violating adjacent coefficient pairs. Regenerated from integer arithmetic on 14 Oct; analytic finite cutoff and coefficient bounds are proved (conditional on standard Newton/Maclaurin and KK results) in `FINITE_REDUCTION_PROOF_AUDIT_2026-10-14.md`. Full search completeness and moment-pruning soundness still require independent review.

| Index k | Total frontier pairs | Current saved progress | Status |
| ---: | ---: | ---: | --- |
| 1 | 0 | n/a | Excluded by finite reduction |
| 2 | 393 | 393 | Locally exhausted; zero survivors reported |
| 3 | 3,364 | 3,364 | Locally exhausted; zero survivors reported |
| 4 | 13,291 | 13,291 | Locally exhausted; zero survivors reported |
| 5 | 30,203 | **8,541** | Partial; zero survivors reported |
| 6 | 34,464 | **1,788** | Partial; zero survivors reported |
| 7 | 25,171 | 0 | Unsearched locally |
| 8 | 11,045 | 0 recoverable | Older work reported >7,900 tested; no resumable state |
| 9 | 2,504 | 0 recoverable | Older log reports complete; certificate not recovered |
| 10 | 241 | 0 recoverable | Older log reports complete; certificate not recovered |
| 11 | 0 | n/a | Excluded by finite reduction |

**Current authoritative machine state is always the latest `degree12_k*_checkpoint.json`**, not this summary or scheduled-task prompt. Currently k5 next pair is (966,1151), k6 next pair is (1001,840). Do not reset or double-count completed pairs.

## Method and validation

- Read `DEGREE12_METHOD.md` for finite frontier and exact shifted/unshifted moment pruning.
- Read `FINITE_REDUCTION_PROOF_AUDIT_2026-10-14.md` for the formal analytic reduction and coefficient caps.
- Read `LIVE_TEST_2026-10-13.md` and `RUN_2026-10-14_EVENING.md` for provenance and known limitations.
- Run `python audit_evening_20261014.py` for an independent arithmetic consistency audit (not exhaustive coverage).
- Resume one branch at a time using `python degree12_search.py 5 60` or `python degree12_search.py 6 60`; file writes are checkpointed after complete pairs. Direct external network/GitHub cloning may be unavailable inside the execution sandbox; use the connected GitHub service and verify commits.
- Before claiming a degree-12 proof, independently audit both recursion completeness and all moment-based pruning, and exhaust every remaining branch.

### Known limits

The positive-root matrix arguments yield necessary conditions. Zero survivors in *partially* completed searches is evidence only for those specific checked ranges. Random/arithmetic audits do not prove search completeness. The broader Bell–Skandera conjecture remains unresolved in this research.
