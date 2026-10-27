# Reproduce the 27 October exact norm-three audit

Use Python 3.10+ (standard library only). The checker expects the independently generated `frontier_checked_d14_20261025.json` through `frontier_checked_d17_20261025.json` in the current working directory. These case lists are included in the dated full ZIP; regenerate them from the 25 October GitHub frontier source and witnesses if using GitHub only.

```bash
python norm3_rational_obstruction_20261027.py
```

Expected result: all 74 norm-three special rows excluded, with minimum strict integer margins 219, 226, 233 and 240 for d14–17. The program proves `log(3)<11/10` by a fifth-order exponential Taylor lower bound and proves the pointwise inverse-trace inequality with exact rational enclosures; no floating-point computations or external packages.

This is a single proof-obligation audit. It does not prove the complete Bell–Skandera finite-degree candidate or the unrestricted conjecture. For the full frontier/Hankel certificate use the 25–26 October reproduction instructions.
