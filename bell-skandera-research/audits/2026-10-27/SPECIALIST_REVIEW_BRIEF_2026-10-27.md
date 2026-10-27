# Bell–Skandera: independent mathematical review brief (27 October 2026)

**Status: UNREVIEWED candidate computer-assisted finite-degree result for 2 ≤ d ≤ 17.** The unrestricted conjecture is not claimed, nor is novelty or external validation. This is a request for *adversarial* review, not endorsement.

## Precise finite-degree claim under examination

Let F(t)=1+u_1t+...+u_dt^d∈Z[t] have degree d≤17 and all roots strictly negative and real. Does there necessarily exist a finite abstract simplicial complex with f-polynomial F(t)? By Kruskal–Katona (KK), it suffices to prove every adjacent inequality u_(k+1)≤KK_k(u_k). The proposed argument assumes a violating pair and excludes all possible cases via Smyth's trace bound, Newton inequalities, coefficient bounds, exact Hankel moment minors, and factor/join induction.

## Proof-dependency map to attack

1. **Smyth factorwise theorem:** For each irreducible factor of the totally positive monic integer polynomial P(x)=x^d F(-1/x), Smyth (1984) yields trace >1.7719×degree unless the factor is one of five explicit exceptional polynomials. Verify strictness, exact hypotheses and reducible/repeated-factor use. Primary source: https://www.numdam.org/article/AIF_1984__34_3_1_0.pdf (Theorem, p.2).
2. **Exceptional-factor induction:** Each exceptional factor E yields an integer f-polynomial F_E(t); the quotient is integer, constant-one, positive-rooted and lower-degree, so the simplicial join completes induction. For norm-one reciprocal factors, the reversed exceptions must also be f-polynomials. The 22 Oct constructive witnesses cover all ten polynomials. Check monic division and no circular reliance on the desired theorem.
3. **KK/Newton finite reduction:** The strict persistent cutoff is derived from monotonicity of T_k(r)=binom(r,k+1)^k/binom(r+1,k)^(k+1). The untrusted interval witness must cover every integer m from binom(d,k) to the cutoff, without gaps. Rectangle exclusions use KK monotonicity and an exact Newton upper bound. Check endpoint direction, equality, and k=1 separately.
4. **Norm and trace branches:** For N=u_d=1, the reciprocal polynomial has integer coefficients and trace u_(d−1); the remaining cases are handled by exact 3×3/4×4 Hankel determinants. For N=2, the 24 Oct quadratic H3 envelope excludes all 74 special rows. For N=3, the 27 Oct rational inverse-trace certificate excludes all 74 special rows when P(1)≠0; if P(1)=0, factor x−1 and invoke induction. Verify that no norm N≥4 remains after the Newton norm cap.
5. **Hankel necessary conditions:** Positive reciprocal roots imply PSD of moment Hankel matrices. The bordered determinant identity gives dH4/dq6=−6H3 and coefficient(q5²)=−25H2; the q6 lower chord produces a concave quadratic upper envelope. Verify that every admissible q1,...,q6 is included, especially equality boundaries and norm-one vs norm-two scaling.
6. **Arithmetic integrity:** Independent Python frontier and Bareiss checkers use arbitrary-precision integers; prior C++ had a fixed-width narrowing defect and must not be used in its obsolete version. Confirm all untrusted witness hashes, case-list coverage, and exact quadratic integer maxima. Treat generated witnesses as untrusted inputs, not as proof by themselves.

## Related literature warning (not a counterexample to Bell–Skandera)

Liu, Wang and Zhang, *Counterexamples to the Mu--Welker recursive decomposition in every degree* (arXiv:2609.23694, September 2026), report counterexamples to a **separate** conjecture that a Mu–Welker recursive decomposition preserves real-rootedness. Their examples are themselves f-polynomials, so this is **not** a counterexample to the Bell–Skandera conjecture. A reviewer should ensure the present proof does not accidentally depend on that disproved auxiliary assertion. Our claimed finite reduction uses KK, Newton, Smyth, and moment PSD instead.

## Minimal reproduction path

Start at the repository's current README and audits/2026-10-26. The complete 26 Oct ZIP contains all lower-degree witnesses and exact verifiers. The 27 Oct ZIP adds a new independent N=3 obstruction checker and five tamper tests. Run the exact frontier verifier for each d=2,...,17, then the generalized Bareiss checker for d=9,...,17, and the norm-two and norm-three special certificates. The dated ZIP contains source, witness lists and expected logs; the GitHub repository contains code and instructions, with larger generated lists reproducible from source.

## What a reviewer should report

Please identify the **first logically unjustified implication**, if any; distinguish a mathematical gap from a code bug; supply a concrete counterexample or a minimal failing input if possible. A useful review would either reject the candidate with a precise defect or validate the mathematical reduction independently before checking computational certificates. Numerical agreement among implementations is not a substitute for this review.
