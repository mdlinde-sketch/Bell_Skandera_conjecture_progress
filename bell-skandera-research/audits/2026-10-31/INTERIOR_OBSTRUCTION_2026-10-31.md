# 31 October 2026 — exact obstruction to extending the terminal KK lemma

**UNREVIEWED research. NOT a counterexample to Bell–Skandera.** No unrestricted theorem, novelty, external specialist or formal proof is claimed. A full self-contained dated ZIP and exact Python checker are also saved in the research workspace.

## Independent review of 30 October terminal proof

The scalar estimate `(D_k(m)-1)^k < k^k*m^(k-1)` survived adversarial review of the r=k facet base, k>=4 induction (`B <= (k-1)*A^((k-1)/k)`, q=0 handled separately), k=3 exceptional endpoint margins, and integer rounding. New independent exact checks: 20,097 facet-base cases and 3,332 colex binomial-boundary cases, all passed. **No defect found in these steps; this is not a formal or complete independent proof.**

## Universal scalar gap at the penultimate index

For any k>=3 let d=k+1 and m=k+2=C(d,k)+1. The downward shadow is
`D_k(m)=C(k+1,2)+(k-1)`.
Maclaurin alone gives
`a_(k-1)>=C(k+1,2)*((k+2)/(k+1))^((k-1)/k)`,
whose right side is strictly less than `C(k+1,2)+(k-1)/2` by concavity. The integer choice `a_(k-1)=C(k+1,2)+ceil((k-1)/2)` therefore satisfies this scalar lower bound but violates KK. Hence the terminal argument cannot simply be copied to interior indices.

The true integer real-negative-rooted family
`E_k(t)=(1+t)^(k-1)*(1+3t+t^2)`
has `a_k=k+2` and `a_(k-1)=C(k+1,2)+(k-1)=D_k(a_k)`, attaining equality in the penultimate KK condition for every k>=2.

## Exact degree-28 partial-integrality counterexample

Let y be a zero of `H(y)=y^26*(428-780y+351y^2)-1` in `(189/200,473/500)`. Rational arithmetic gives `H(189/200)<0<H(473/500)`. Set `T=30-26y`, `P=y^(-26)`; the discriminant `T^2-4P` is positive on this interval, as it exceeds `(30-26*(473/500))^2-4*(200/189)^26>0`. Let x,z>0 satisfy x+z=T, xz=P.

Then `F(t)=(t+x)(t+z)(t+y)^26` is monic, has constant coefficient 1 and only negative real roots. Its coefficients satisfy
`a_28=1, a_27=30, a_26=428` exactly, but
`D_27(30)=C(28,26)+D_26(2)=378+51=429>428`.
The terminal KK condition still holds: `D_28(1)=28<=30`.

**Crucially F is NOT in Z[t].** Its coefficient `a_1=26/y+(30-26y)*y^26` lies strictly between 28 and 29, verified by exact rational endpoint bounds. Therefore this example refutes ONLY the attempted inference from root positivity plus integrality of the top three coefficients, **not** Bell–Skandera. Any valid interior-index argument must use more global coefficient integrality or other information.

## Reproduction and next task

The standard-library checker `interior_obstruction_certificate_20261031.py` verifies the IVT signs, positive discriminant, a1 nonintegrality, colex shadows, 20,097 base cases and 3,332 boundary cases with exact fractions/integers. It does not use the degree-17 certificates. The complete dated ZIP is `Bell_Skandera_2026-10-31_interior_obstruction_audit.zip`. Review all global-integrality constraints, factorwise Smyth with corrected exceptions, and higher Hankel PSD; do not extend d18 or blindly increment excess.

Previous work: [terminal lemma](../2026-10-30/TERMINAL_KK_PROOF_2026-10-30.md); [corrected Smyth exceptions](../2026-10-29/independent_followup/AUDIT.md).
