# 1 November 2026 — exact all-degree nonunit trace-boundary rigidity

**UNREVIEWED mathematical deduction.** Not an unrestricted Bell–Skandera proof, novelty claim, external specialist review or formal verification. Independent of the d<=17 computational search. A more detailed self-contained PROOF.md and standard-library checker are packaged in Bell_Skandera_2026-11-01_nonunit_trace_boundary_audit.zip.

## The scaled reciprocal integer polynomial

Let F(t)=prod_(i=1)^d (1+lambda_i*t) in Z[t], with lambda_i>0, F(0)=1, N=prod lambda_i=a_d>=1. Define
B_N(x)=prod (x-N/lambda_i)=x^d-a_(d-1)x^(d-1)+N*a_(d-2)x^(d-2)-...+(-1)^d N^(d-1).
This is MONIC INTEGER because its j-th elementary symmetric coefficient is N^(j-1)a_(d-j). Its roots beta_i=N/lambda_i are positive algebraic integers with sum a_(d-1), product N^(d-1). Integrality of the whole F is essential to the evaluation B_N(1) below.

## Theorem 1: sharp universal nonunit barrier

For d>=2, N>=2 implies a_(d-1)>=2d-1. AM-GM gives a_(d-1)>=d*N^((d-1)/d)>=d*2^((d-1)/d)>2d-2, using exp(-log(2)/d)>1-1/d. The coefficient is an integer. Equality is attained by (1+t)^(d-1)(1+2t). Thus a_(d-1)-d<d-1 forces N=1 in ANY degree.

## Theorem 2: exact classification at the boundary, for EVERY degree

If d>=2, N>=2, and a_(d-1)=2d-1, then necessarily

    N=2 and F(t)=(1+t)^(d-1)(1+2t).

Proof: N>=3 is impossible by AM-GM: for d>=3, a_(d-1)>=d*3^((d-1)/d)>=d*3^(2/3)>2d; for d=2, 2sqrt(3)>3. Put beta_i=2/lambda_i. They are roots of monic B_2 in Z[x], with sum 2d-1 and product 2^(d-1).

First every beta_i>=1. Otherwise for b=beta_j in (0,1), AM-GM on the remaining d-1 roots gives
  1 <= b*(1+(1-b)/(2(d-1)))^(d-1)
    <= b*exp((1-b)/2) < 1,
where log b <= b-1 proves the last strict inequality. Contradiction.

If every beta_i>1, then prod(beta_i-1)=(-1)^d B_2(1) is a **positive integer**, hence >=1. AM-GM on beta_i-1 gives sum(beta_i-1)>=d, but this sum is d-1. Contradiction. Therefore some beta_j=1. The others then have sum 2(d-1) and product 2^(d-1); equality in AM-GM forces all others to equal 2. Thus B_2=(x-1)(x-2)^(d-1), and F=(1+2t)(1+t)^(d-1). QED.

This uses GLOBAL integer-polynomial structure: the crucial statement B_2(1) is an integer cannot be deduced from integrality of only the top few coefficients.

## Interior-index consequence

The boundary forces a_(d-2)=(d-1)^2. This is precisely the DOWNWARD Kruskal–Katona bound D_(d-1)(2d-1)=(d-1)^2, by the two-term binomial expansion 2d-1=C(d,d-1)+C(d-1,d-2). Newton's inequality ALONE gives the opposite ceiling
a_(d-2) <= floor((2d-1)^2(d-1)/(4d))=(d-1)^2.
Therefore the global integer resultant closes an otherwise unresolved exact integer gap at the penultimate interior index, for all d.

## Theorem 3: all-degree low REVERSE excess (conditional on Smyth 1984)

If a_(d-1)-d<=3 (and F has all negative real roots, positive integer coefficients, F(0)=1), then F is a simplicial-complex face polynomial, regardless of degree and leading norm.

If N=1, reverse F; its forward excess is <=3. Remove the five correctly oriented Smyth exceptions. The nonexceptional core has degree g<30000/7719<4. Each exceptional factor and its reverse is an f-polynomial (exact KK verification), and every degree<=3 negative-real-rooted integer polynomial is an f-polynomial (29 Oct analytic lemma). Reverse back and join.

If N>=2, Theorem 1 implies d<=4. d<=2 is automatic. At d=3, a2<=6, and Maclaurin a2^3>=27N^2 forces N=2 and a2>=5; downward D_3(2)=5<=a2, while the first KK condition always follows from Newton. At d=4, a3<=7 and Maclaurin a3^4>=4^4*N^3 force N=2,a3=7. Maclaurin and Newton then force a2=9,a1=5, so F=(1+t)^3(1+2t). QED.

Smyth exceptions in F-orientation: (1,1), (1,3,1), (1,5,6,1), (1,7,13,7,1), (1,7,14,8,1). Source: https://www.numdam.org/article/AIF_1984__34_3_1_0.pdf ; corrected factor audit: audits/2026-10-29/independent_followup/AUDIT.md.

## Limits

This is an exact all-DEGREE boundary classification, NOT an unrestricted proof of the penultimate KK inequality or Bell–Skandera. The root barrier beta>=1 and integer-resultant argument fail immediately when a_(d-1)>2d-1; extending them is the new research target. A standalone dated ZIP holds the detailed proof, exact rational and integer tests through d=250, and SHA256 manifest. No degree-18 expansion.