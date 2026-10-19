# Reproduce the 18 October 2026 degree-17 candidate audit

Requires Python 3.10+, g++ with Boost multiprecision headers, and (only for the inverse-trace certificate) standard-library Python. All classifications and determinant comparisons use exact integers, not floating-point arithmetic.

Run from this archive's extracted folder:

```
python independent_python_frontier_degree17.py 17
python adversarial_math_audit_20261018.py
python certified_inverse_trace.py
python independent_special_norm2.py python_independent_frontier_degree17.json
python third_interval_verifier.py python_independent_frontier_degree17.json

g++ -O3 -std=c++17 independent_cpp_interval_frontier17.cpp -o cpp_interval17
for d in $(seq 2 17); do ./cpp_interval17 "$d"; done
python compare_all_degree_frontiers.py

g++ -O3 -std=c++17 frontier_segment.cpp -o frontier_segment
./frontier_segment 17 13 17
python compare_degree17_lists.py

g++ -O3 -std=c++17 unitnorm_extended.cpp -o unitnorm_extended
./unitnorm_extended 17 python_independent_frontier_degree17.json
```

Expected: 2,142 residual cases, 37 specials, 578,295 negative q5 interval blocks, 193,610,278 candidate q5 values excluded, no survivors. The original C++ brute-frontier command checks k=13..16; the NEW C++ interval-frontier command independently checks all k for all degrees 2..17. Both implementations share the mathematical interval argument but use separately implemented integer arithmetic. The Python interval verifier takes roughly 1–2 minutes on a contemporary CPU; C++ is faster.

The prior day 17 October audit through degree 16 is in the separately archived file `Bell_Skandera_2026-10-17_independent_audit.zip`; the mathematical hypotheses and caveats carry over. Read `DEGREE17_CANDIDATE_CHECKPOINT_2026-10-18.md` before treating any result as a theorem.
