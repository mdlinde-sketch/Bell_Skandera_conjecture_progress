# Reproduce the 25 October lower-degree audit

Python 3.10+ standard library only. In a temporary working directory, place these repository files together:

- `audits/2026-10-18/independent_python_frontier_degree17.py` (untrusted candidate generator).
- `audits/2026-10-21/emit_frontier_certificate.py` (untrusted witness generator).
- `audits/2026-10-25/frontier_checker_all_degrees_20261025.py` (independent frontier verifier).
- `audits/2026-10-25/lower_degree_hankel_audit_20261025.py` (exact Bareiss verifier).
- `audits/2026-10-25/test_lower_degree_witness_tampering_20261025.py` (negative controls).

Then run the following Python in that directory:

```python
from independent_python_frontier_degree17 import independent
from emit_frontier_certificate import emit
import json,subprocess,sys
for d in range(2,17):
    obj=independent(d,verbose=False)
    with open(f'regenerated_frontier_d{d}_20261025.json','w') as f:
        json.dump({'degree':d,'residual':obj['residual'],'suspect':obj['suspect']},f)
    emit(d,f'frontier_cover_d{d}_20261025.jsonl.gz')
    subprocess.run([sys.executable,'frontier_checker_all_degrees_20261025.py',
                    f'frontier_cover_d{d}_20261025.jsonl.gz',str(d)],check=True)
    if d>=9:
        subprocess.run([sys.executable,'lower_degree_hankel_audit_20261025.py',
                        f'frontier_checked_d{d}_20261025.json'],check=True)
```

Run `python test_lower_degree_witness_tampering_20261025.py`. Then rerun `audits/2026-10-24/norm2_quadratic_envelope_20261024.py` with the degree-14,15,16 input JSONs from that directory, and the earlier exact-rational inverse-trace certificate.

**Note:** the GitHub 21 October `emit_frontier_certificate.py` imports the 18 October generator via a sibling-path fallback; when both files are in the same directory, Python's current-directory import also works. The generated gzip witnesses, case-list JSONs and full logs are in the dated ZIP, not committed. Mathematical assumptions remain subject to external review.
