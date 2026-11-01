# 1 November 2026 — all-degree adjacent-integer trace/norm rigidity

**Unreviewed elementary deduction, no novelty claim.** Generalizes the integer-resultant step of NONUNIT_TRACE_BOUNDARY_2026_11_01.md but does NOT establish unrestricted Bell–Skandera.

**Lemma (every d>=2 and integer c>=1).** Let B(x) be monic in Z[x] with d strictly positive real roots beta_i. If

    sum_i beta_i = (c+1)*d-1,
    product_i beta_i = c*(c+1)^(d-1),

then necessarily

    B(x)=(x-c)*(x-(c+1))^(d-1).

**Proof.** Suppose one root b<c. AM–GM on the other d-1 roots gives
c*(c+1)^(d-1) <= b*((c+1)+(c-b)/(d-1))^(d-1).
The right / left ratio is at most (b/c)*exp((c-b)/(c+1))<1, since log(b/c)<=b/c-1=-(c-b)/c. Contradiction, hence beta_i>=c for all i.

If none equals c, prod(beta_i-c)=(-1)^d B(c) is a **positive integer** >=1. AM–GM then implies sum(beta_i-c)>=d, whereas the given trace gives sum(beta_i-c)=d-1. Therefore at least one beta_i=c. For the remaining d-1 positive roots, arithmetic and geometric means both equal c+1; AM–GM equality forces every remaining root to equal c+1. QED.

The c=1 case precisely supplies the all-degree rigidity used to classify the Bell–Skandera norm-two boundary a_d=2, a_(d-1)=2d-1. The case-specific trace/norm condition is essential. At the next trace a_(d-1)=2d, the family (1+t)^(d-2)*(1+4t+2t^2) already shows beta_min<1 and B_2(1)=+/-1.

The full mathematical note plus 4,000 exact parameter-degree and 36,000 rational root-barrier controls are in Bell_Skandera_2026-11-01_nonunit_trace_boundary_audit.zip. These checks supplement, not replace, the symbolic proof. No claim of originality, a complete conjecture proof, peer review or proof-assistant verification.
