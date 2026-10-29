> **29 October follow-up correction:** Two Smyth exceptions were reversed in the earlier small-excess note. The corrected all-degree s<=3 proof and independently reproduced s<=6 certificate, with precise scope and an all-order Hankel identity, are in the [adversarial follow-up audit](bell-skandera-research/audits/2026-10-29/independent_followup/AUDIT.md). The unrestricted conjecture remains unproved. Earlier trace-factor reductions require the corrected exception orientation; no new finite-degree extension is claimed.

# Bell–Skandera conjecture: candidate proofs for degrees 5–7

**Research status:** AI-generated, **unreviewed candidate proofs**, not established theorems. Mathematical arguments and finite computational certificates are provided for independent verification. Neither a successful script run nor agreement between different programs verifies the completeness of the underlying analytic reduction.

The Bell–Skandera conjecture asks whether every real-rooted polynomial with constant coefficient 1 and nonnegative integer coefficients has a coefficient sequence that is the face vector of a simplicial complex.

## Read the work

- **[Combined degree-5, degree-6 and degree-7 manuscript](paper/combined_degree5_6_7.md)**
- [Degree-5 proof note](research/degree5_proof_note.md)
- [Degree-6 proof note](research/degree6_proof_note.md)
- [Degree-7 proof note](research/degree7_proof_note.md)
- [Preliminary degree-5 adversarial report](reviews/degree5_adversarial_report.md)

## Reproduce the calculations

| Degree | Standard-library exact checker | Independent SymPy checker |
| --- | --- | --- |
| 5 | [degree5_certificate.py](verification/degree5_certificate.py) | [degree5_independent.py](verification/degree5_independent.py) |
| 6 | [degree6_certificate.py](verification/degree6_certificate.py) | [degree6_independent.py](verification/degree6_independent.py) |
| 7 | [degree7_certificate.py](verification/degree7_certificate.py) | [degree7_independent.py](verification/degree7_independent.py) |

Run from the repository root:

```sh
python verification/degree5_certificate.py
python verification/degree6_certificate.py
python verification/degree7_certificate.py
python -m pip install sympy
python verification/degree5_independent.py
python verification/degree6_independent.py
python verification/degree7_independent.py
```

Some scripts can be computationally intensive. See each script's docstring for its requirements and implementation.

## Limitations and requests for review

The core claim in each draft depends on a mathematically complete *infinite-to-finite reduction*, after which finitely many integer vectors are checked. Reviewers should first audit the inequality directions, exceptional-value cutoffs, exhaustiveness of the candidate search, and the Hermite-positivity obstruction. The scripts are evidence for the stated computations, not a substitute for proving those reductions correct.

**Authorship/provenance:** The human project lead chose the problem and research direction and initiated publication. GPT-6 generated the mathematical ideas, proposed proofs, and checking code. These outputs have not undergone independent academic peer review. Please open an issue with any concrete error, missing case, counterexample or relevant prior publication.

**No priority or correctness claim:** These documents are shared as working research for public scrutiny; novelty and mathematical correctness remain to be determined.
