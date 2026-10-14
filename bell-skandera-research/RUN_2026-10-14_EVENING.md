# Bell–Skandera degree-12 research — 14 October 2026 evening (Brisbane)

## Scheduling check
The ChatGPT scheduled task was enabled at 19:00 Brisbane on 14 Oct. Its automation record shows last_run_time 2026-10-14T09:07:19Z (=19:07:19 AEST). Notifications and email were disabled, explaining why no notification was seen. This manual research continuation is separate from that scheduled run. Turning a user's PC off does not stop server-side scheduled runs.

## Authoritative starting checkpoints (read from GitHub)
- k=5: 6,733 / 30,203, no survivors, 9,632,007 nodes.
- k=6: 1,504 / 34,464, no survivors, 6,861,404 nodes.
- k=2,3,4 previously marked complete; not independently rerun in this session.
- Previous reported degree-11 results and degree-12 finite reduction remain unreviewed claims.

## Newly computed in this manual session
- Reconstructed entire degree-12 frontier using exact `degree12_frontier.py` and `explore.py` logic: all 11 per-index pair counts reproduce, total 120,676. Pair at zero-based index 6733 of k=5 is (941,1119); at zero-based index 1504 of k=6 it is (994,826). This corroborates the search ordering.
- k=5: extended 6,733 -> **8,541** completed pairs, 1,808 newly completed, zero survivors. Cumulative nodes **15,693,981**, increment 6,061,974. Next pair (zero-based index 8541): **(966,1151)**.
- k=6: extended 1,504 -> **1,788** completed pairs, 284 newly completed, zero survivors. Cumulative nodes **10,996,275**, increment 4,134,871. Next pair (zero-based index 1788): **(1001,840)**.
- Runtime was two bounded passes for k5 (26+25 seconds) and one for k6 (30 seconds). The code only counts completely exhausted pairs; a timed-out pair is retried.
- Exactly duplicated published search logic inside an isolated Python runtime because direct raw.githubusercontent.com download was blocked by DNS; updated checkpoints were committed using the connected GitHub write tool.

## Independent arithmetic audit
`audit_evening_20261014.py` ran with Python standard library and passed these independently checkable tests:
- 120,676 finite-pair constraints checked against exact Newton/Maclaurin inequality and strict KK violation requirement.
- 4,397 distinct exceptional m values checked with independently inverted lower shadow (including boundary test).
- 1,920 exact rational-Gaussian determinant comparisons against affine moment determinant values at 0, 1, 2, 17, u_j.
- 5,460 positive-integer-root determinant controls, including repeated roots and singular Hankel matrices.
- 5,005 necessary Newton log-concavity controls for those root-generated coefficient vectors.
- 108 coefficient cap checks for k=5/6 when the sampled root-generated vector lies in the capped domain.

## Adversarial assessment and limitations
All checks above validate necessary arithmetic and consistency with positive-root families, **not completeness** of the degree-12 reduction or exhaustive search. Source script is AI-generated and its pruning soundness and search-loop coverage remain subject to independent formal review. The new portions report no survivors under these necessary conditions, but cannot be called a proof of degree 12. We did not independently replay earlier 6,733 k5 pairs, 1,504 k6 pairs, or degree-11 certificates.

Relevant current literature checked: Lili Mu and Volkmar Welker, Advances in Applied Mathematics 175 (2026), 103041, https://doi.org/10.1016/j.aam.2026.103041 ; Feihu Liu, Ying Wang and Zihao Zhang, arXiv:2609.23694 (Sept 2026), counterexamples to a recursive-decomposition conjecture, **not** counterexamples to Bell–Skandera.

## Next exact state
Read latest k5 and k6 checkpoint JSON from GitHub before any subsequent run; do not use older prompt numbers. Next pairs k5=(966,1151), k6=(1001,840). Other incomplete branches include k7 and k8; k8 older state is not recoverable. Priority next: independent search-enumeration coverage audit, improved pruning/structural inequalities, and verified new progress at k5/k6.
