# Reproduce 26 October 2026 mathematical-reduction audit

**UNREVIEWED finite-degree candidate through degree 17; not a verified theorem.**

Python 3.10+ standard library only. The newly committed standalone checker requires no generated case lists:

```bash
python hankel_structural_identity_checker_20261026.py
```

It independently checks 3,000 exact 4x4 Hankel derivative/concavity identities and 2,000 exact norm-two 3x3 identities, using direct Leibniz determinants rather than the archived Bareiss or Schur implementations. The mathematical derivations are in STRUCTURAL_PRUNING_PROOF_NOTE.md.

For the complete rectangle/KK/Newton and genuine positive-root stress tests, download the dated 26 October research ZIP, extract it, and run:

```bash
python structural_pruning_audit_20261026.py
python lower_degree_hankel_audit_20261025.py frontier_checked_d17_20261025.json
```

The first script checks 2,176 cutoff instances, 3,400 rectangle comparisons, 2,012 trace-cap comparisons, all 7,596 d17 frontier witness leaves, 3,000 H4 identities, 2,000 norm-two identities and 4,000 positive-root coefficient-bound controls. The second command reruns the exact degree-17 Bareiss certificate; on 26 October it completed with 2,179 cases, 578,295 negative intervals, 193,610,278 excluded q5 integers and zero survivors. Expected logs are included in the ZIP.

The full ZIP also includes the 25 October lower-degree certificates, generated witnesses, all prior source files and detailed audit. These tests corroborate, but cannot replace, independent mathematical review of Smyth's theorem, factor induction, KK completeness, coefficient bounds and Hankel PSD necessity.
