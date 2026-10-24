# Reproduce the 24 October quadratic-envelope audit

**Python 3.10+ standard library only.** All 74 norm-two special input rows for d14–17 are committed in this directory; they can be checked without the ZIP archive.

From `bell-skandera-research/audits/2026-10-24/` run:

```bash
python norm2_quadratic_envelope_20261024.py norm2_special_cases_degree14_20261024.json norm2_special_cases_degree15_20261024.json norm2_special_cases_degree16_20261024.json norm2_special_cases_degree17_20261024.json
python test_norm2_envelope_20261024.py
```

Expected: 4, 11, 22, 37 cases respectively; maximum H3 upper bounds -203612864, -292671612, -465675264, -720889920. All are strictly negative. The script writes `norm2_quadratic_envelope_results_20261024.json`.

To independently regenerate the degree-17 frontier and the larger 4×4 Hankel certificate, follow [23 October reproduction instructions](../2026-10-23/REPRODUCE_FROM_GITHUB.md). The full 24 October dated archive also includes the untrusted frontier witness, all older checkers, the complete 815,161-case full-grid control (d14–17), and five bounded-chunk rerun logs of the unchanged 21 October Bareiss verifier. Aggregate results match the previous complete run exactly: 578295 negative H4 intervals, 193610278 q5 integers excluded, zero survivors.

**Caveat:** This is an exact conditional finite certificate, not a formally verified or peer-reviewed proof of Bell–Skandera.
