# 15 October 2026: candidate computer-assisted proof through degree 12 — UNREVIEWED

**STATUS: Candidate finite-degree result; NOT a published/independently refereed proof and NOT a solution in all degrees.**

Research continued from the degree-12 checkpoint without overwriting the earlier incomplete k=5/k=6 brute-force results. A new structural induction using Smyth's 1984 trace theorem (doi:10.5802/aif.975), reciprocal polynomials, an elementary inverse-trace inequality, and exact moment-based exclusion reduces the computation substantially.

The main certificate and a separate independently implemented exact-integer determinant audit were run successfully on 15 October 2026 for every degree 2 through 12. Reconstructed finite-frontier sizes:
d=4 2; d=5 11; d=6 56; d=7 222; d=8 835; d=9 2940; d=10 10226; d=11 34948; d=12 120676. d=2,3 have zero candidate pairs.

After inductive factor reductions, candidate cases needing finite norm-one enumeration were d9:2, d10:6, d11:13, d12:29; both independent verifiers found 0 surviving vectors with identical DFS node counts 31, 127, 368, and 27706 respectively. Extra adversarial tests passed 10000 rational-rounding checks and 1018 constructed positive-rooted integer polynomials.

**Logical status:** These computational outputs plus the written lemmas form a candidate *computer-assisted proof* for all degrees ≤12, contingent on independent specialist scrutiny of trace theorem applicability, KK finite cutoff, integer bound directions, PSD determinant necessity and recursive coverage. This does not settle Bell–Skandera for arbitrary degrees and does not establish novelty.

The complete self-contained research bundle was exported in the ChatGPT conversation on 15 October as `Bell_Skandera_2026-10-15_candidate_proof_to_degree12.zip`, containing `PROOF_CANDIDATE_2026-10-15.md`, `verify_through_12.py`, `independent_residual_audit.py`, `adversarial_tests.py` and machine-readable results. This note does **not** assert that those archive contents have been published to GitHub; upload the ZIP/extract files to this repository for durable reproducibility.

**Next priority:** independent adversarial mathematical review of the written certificate and a third verifier in a different language (or Lean/Isabelle), along with a literature search for prior degree-12 results. Do not revert to the 120676-pair brute-force search unless this structural proof fails.
