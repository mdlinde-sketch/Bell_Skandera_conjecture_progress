# Reproduce the 23 October 2026 checkpoint from committed GitHub source

**Requires Python 3.10+ standard library.** Run from the repository's `bell-skandera-research/audits/2026-10-21/` directory after checking out main.

```bash
python emit_frontier_certificate.py
python check_frontier_certificate.py frontier_cover_d17.jsonl.gz
python check_hankel_bareiss.py frontier_checked_d17.json
python ../2026-10-20/norm2_full_grid_20261020.py frontier_checked_d17.json

python ../2026-10-22/smyth_sturm_certificate_20261022.py
python ../2026-10-22/exception_join_certificate.py
python ../2026-10-23/reciprocal_norm_factor_audit.py
python ../2026-10-23/clone_complex_audit.py
```

The untrusted witness generator imports exact integer frontier routines from the committed 18 October `independent_python_frontier_degree17.py` and writes the compressed witness locally. The independent frontier checker does **not** import those routines; it validates disjoint interval coverage and all classification inequalities afresh.

Expected d17 frontier: 7,596 disjoint leaves, 969,827 explicit adjacent pairs, 2,142 residual, 37 specials, with SHA256 hashes `f2763600f7244981a711a4d581b078afa3cc285b9d847300b112995eb7b121e0` and `48f93be87cc5fc15fc6ba20d104630633a35466d114462459be6cee5754763b7`. Expected Bareiss: 6,573,665 q4 checks, 578,295 negative H4 intervals, 193,610,278 excluded q5 integers, zero survivors. Expected norm-two: 37 specials, 539,000 exact H3 grid checks, all negative.

Expected 22–23 October structural tests: 5 positive-root Sturm counts; 10 exceptional/reverse f-polynomial witnesses and 100 joins; 49,200 arbitrary-norm divisibility checks, 15 direct unit-norm exceptional controls; 40 constructive vertex-cloning checks.

**Caveats:** The generated certificate and checkers are finite, exact-arithmetic and independently implemented in parts, but the underlying mathematical reductions and Smyth theorem application are not formally verified by a proof assistant or peer reviewed. The Bell–Skandera conjecture remains unresolved in general. This GitHub source can regenerate the degree-17 certificate without the dated ZIP archives, but those archives also contain logs and additional controls.
