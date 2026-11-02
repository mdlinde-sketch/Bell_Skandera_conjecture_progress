# 2 November 2026 — inverse-trace core rigidity and two exact norm-two classifications

**UNREVIEWED research corollary.** Not an unrestricted Bell–Skandera proof, novelty, specialist endorsement or Lean/Coq verification. No degree-18 extension. Full expanded mathematical proof, independent exact checker, JSON log and SHA256 manifest: `Bell_Skandera_2026-11-02_inverse_trace_core_rigidity_audit.zip`.

## Adversarial check of the 1 November boundary proof

The previous `B_N(x)=prod(x-N/lambda_i)` really is monic integral: coefficient of `x^(d-j)` is `(-1)^j*N^(j-1)*a_(d-j)`. At `N=2, a_(d-1)=2d-1`, fixing any `beta<1` and applying AM–GM gives `1<=beta*(1+(1-beta)/(2(d-1)))^(d-1)<1`. If all beta>1, integer `abs(B_2(1))=prod(beta-1)>=1` contradicts `sum(beta-1)=d-1`. No unjustified step was identified in these implications; this is not external/formal review. The 1 November archive's hashes and three independent exact programs were rerun and passed. At the start of this run the GitHub HEAD was the 1 November verified commit `74a2d4237bdaf60ada65f9c623ddf8ccf741aefc` with no later commits.

## All-degree integer-resultant factor-stripping theorem

Let `F(t)=1+a1*t+...+ad*t^d in Z[t]` have exclusively negative real roots, degree d>=1 and norm `N=ad>=1`. Write `F=(1+t)^r*H`, where `H(-1)!=0` and `h=deg H=d-r`. Define

`Delta(F)=a_(d-1)/N - d + (3/2)*log N`.

Then if h>=1,

`(9/20)*h < Delta(F)`, equivalently `h<(20/9)*Delta(F)`.

**Proof.** Write `H=prod(1+lambda_i*t)`, lambda_i>0, and `P(x)=x^h H(-1/x)=prod(x-lambda_i)`, a monic integer polynomial. Because `P(1)=H(-1)` is a nonzero integer, `abs(P(1))>=1`. The pointwise inequality from the 27 October inverse-trace audit is

`g(x)=1/x+(3/2)log x-(3/4)log|x-1| > 29/20` for x>0,x!=1.

Its derivative is `(3x^2-10x+4)/(4x^2(x-1))`; its only stationary points are `(5+-sqrt(13))/3`. The accompanying **independent exact-rational** checker encloses sqrt(13), evaluates rigorous artanh-series log bounds at both minima and proves strict positive margins, with no floating point. Sum over the h roots:

`(29/20)h < sum g(lambda_i) = a_(h-1)(H)/N +(3/2)log N -(3/4)log|P(1)| <= a_(d-1)/N-r +(3/2)log N`.

Substitute d=h+r and rearrange to obtain the theorem. For h=0, F is a power of 1+t.

**All-degree sufficient condition for every KK index:** If `Delta(F)<=9/5`, then h<4 and hence h<=3. The analytic degree<=3 KK theorem from the corrected 29 October audit makes H a face polynomial; multiplication by (1+t)^r is simplicial join. Thus F satisfies **ALL** Kruskal–Katona inequalities, in any degree and at any forward excess, whenever this explicit coefficient condition holds. It is not a necessary condition, and Delta can grow without bound; therefore the unrestricted conjecture is NOT proved.

## Exact norm-two trace classifications

Using the exact inequality `log 2<7/10`, the general bound gives:

**(A) Every d>=2, N=2 and a_(d-1)=2d:**
`F=(1+t)^(d-2)*(1+4t+2t^2)` **uniquely**. Indeed Delta<21/20, so h<7/3, hence h<=2. h=1 would give trace 2d-1, and h=2 forces H=1+4t+2t² (discriminant 8). This proves the 1 November example is the only genuine integer negative-real-rooted polynomial on that trace boundary. Its `a_(d-2)=d²-d-1` and, for d>=3, `D_(d-1)(2d)=d²-d-2`: exact KK slack 1.

**(B) Every d>=2, N=2 and a_(d-1)=2d+1:** exactly
`(1+t)^(d-2)*(1+5t+2t²)` (d>=2), or
`(1+t)^(d-3)*(1+2t)*(1+3t+t²)` (d>=3).

Indeed Delta<31/20 gives h<31/9<4. h=1 impossible; h=2 forces 1+5t+2t² (discriminant 17). h=3 forces H=1+a*t+7t²+2t³. Newton gives 5<=a<=8; its discriminant is `-8a³+49a²+252a-1480`, equal to 5,68,-59,-424 at a=5,6,7,8. Only a=5,6 are real-rooted; a=6 has an (1+t) factor and is excluded from H; a=5 gives the second displayed family. Both families satisfy KK by explicit simplicial joins. Their a_(d-2) are d²-3 and d²-4 respectively.

## Limits and reproduction

The auxiliary g-inequality was already used on 27 October for a norm-three finite branch; this application and its factor-stripping corollary are not claimed novel. The factor bound is conditional on Delta, and no uniform bound for arbitrary unbounded excess or unrestricted interior KK theorem is obtained. The 31 October partial-integrality example remains NOT a counterexample to Bell–Skandera.

Run `python inverse_trace_root_forcing_certificate_20261102.py` with Python 3 standard library. The exact checker validates the two stationary minima, log2 bound, cubic discriminants, all family coefficients through d=250, and full KK controls through d=80. Full expanded proof and SHA256 hashes are in the dated ZIP. The next research target is an integer-resultant/auxiliary-function constraint involving intermediate symmetric coefficients when Delta is large, with adversarial counterexample searches before any claim.
