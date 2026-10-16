# Reproducing the degree-16 candidate (16 October 2026)

**Not a verified or peer-reviewed theorem.** All routines use exact integer arithmetic for decisions. Requires C++17 compiler with Boost, Python 3, and SymPy for the separate symbolic identities.

Start from the `audits/2026-10-16` directory. Compile `frontier_segment.cpp`, then run it as `./frontierseg 16 1 6`, `./frontierseg 16 6 9`, `./frontierseg 16 9 11`, `./frontierseg 16 11 12`, `./frontierseg 16 12 16`. The last invocation creates `independent_cpp_degree16_k12-15_20261016.json`; the other invocations create the other named partitions. Run `python combine_degree16.py` to check coverage and generate `independent_cpp_degree16_FULL_20261016.json`.

Compile `unitnorm_extended.cpp` as `unitext`, run `./unitext 16 independent_cpp_degree16_FULL_20261016.json`. Then run `python third_interval_verifier.py independent_cpp_degree16_FULL_20261016.json` and `python certify_interval_identity.py`. Expected: 1,038 residual/special cases, 256,006 negative q5 interval blocks, 61,662,703 q5 integers excluded, zero survivors. These are checks of *necessary* positivity conditions only; their value depends on the completeness of the independent coefficient classification.

Norm-two special H3 exclusions use `audit_norm2_degree14_20261016.py` (set d=16 and iterate 22 special cases), originally preserved inside the first 16 October degree-14 ZIP. Norm-three special cases require the inverse-trace lemma. See `DEGREE16_CANDIDATE_CHECKPOINT.md` for the mathematical argument and warnings.

The complete executed 16 October degree-16 source + JSON + logs is separately packaged in `Bell_Skandera_2026-10-16_degree16_candidate_and_interval_certificate.zip`. This README does not assert that binary archive itself is uploaded to GitHub.
