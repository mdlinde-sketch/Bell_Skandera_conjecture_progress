# Reproduce the 28 October norm-two monotonic-corner certificate

**Unreviewed finite-degree candidate through d17 only.** Requires Python 3.10+ and the standard library.

In one directory, place `norm2_corner_certificate_20261028.py`, `test_norm2_corner_tampering_20261028.py`, and the four input files `norm2_special_cases_degree14_20261024.json` through `norm2_special_cases_degree17_20261024.json` (already committed under `audits/2026-10-24/`). Then run:

```bash
python norm2_corner_certificate_20261028.py norm2_special_cases_degree14_20261024.json norm2_special_cases_degree15_20261024.json norm2_special_cases_degree16_20261024.json norm2_special_cases_degree17_20261024.json
python test_norm2_corner_tampering_20261028.py
```

The checker verifies all four SHA256 case-list digests, computes H2, S(L3) and H3 at the lower corner using exact integers and a separate Leibniz determinant, tests 2,000 exact derivative identities, and rejects all 74 norm-two cases. The tampering test rejects five modified inputs. It **does not** verify the full frontier, norm-one Bareiss, norm-three, Smyth, or induction. For those use the 25–27 October source and full dated archive.
