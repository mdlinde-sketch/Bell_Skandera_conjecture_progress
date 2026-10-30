# 30 October 2026 — all-degree terminal Kruskal–Katona lemma

**UNREVIEWED independent research argument.** Not the unrestricted Bell–Skandera theorem, no originality or external/formal verification claimed. The full dated ZIP contains the extended proof, source, exact controls, and hashes. No degree-18 work.

## Theorem

For every integer k>=2,m>=1, let D_k(m) be the downward Kruskal–Katona shadow of m k-sets (colex minimum). Then

    (D_k(m)-1)^k < k^k * m^(k-1),

equivalently D_k(m)<=ceil(k*m^((k-1)/k)).

Consequently, if F(t)=1+a1*t+...+ad*t^d has positive integer coefficients and all negative real roots, then **the terminal KK inequality holds in every degree**:

    D_d(a_d) <= a_(d-1).

Indeed Maclaurin gives a_(d-1)>=d*a_d^((d-1)/d), and the coefficient is an integer.

## Complete mathematical proof of the scalar bound

The colex recursion for m=C(r,k)+q, r>=k, 0<=q<C(r,k-1), is D_k(m)=C(r,k-1)+D_(k-1)(q), D_j(0)=0. Put A=C(r,k), B=C(r,k-1), h=r-k+1, a=(k-1)/k, b=(k-2)/(k-1).

**k=2:** D_2(C(r,2)+q)=r if q=0 and r+1 otherwise. The strict inequality follows respectively from (r-1)^2<4C(r,2) and r^2<4(C(r,2)+q) for r>=2, q>=1.

**r=k, k>=3:** 1<=m<=k and the first m k-facets of the (k+1)-vertex simplex have D_k(m)=km-C(m,2). For every positive integer m, (m-1)/2+1/m>log m (check m=1,2,3; for m>=4, log m<(m-1)/2 by differentiation). Hence (D_k(m)-1)/(km)=1-((m-1)/2+1/m)/k < 1-log(m)/k <= exp(-log(m)/k)=m^(-1/k).

**Induction, k>=4,r>=k+1:** For q=0, B=kA/h<=kA^a because A<=h^k. For q>=1, induction yields D_k(A+q)-1 < B+(k-1)q^b. We claim B<=(k-1)A^a: A/h^k=prod_(j=1)^k[(h+j-1)/(jh)] decreases in h>=2 and at h=2 equals (k+1)/2^k. For k>=4, (3/2)^k>=k+1, so A^(1/k)/h<=3/4. Hence B/A^a=kA^(1/k)/h<=3k/4<=k-1. Since q>=1, q^b<=q^a. Jensen's inequality gives A^a+q^a<=2^(1/k)(A+q)^a, while (k-1)2^(1/k)<=k by Bernoulli's inequality. Thus B+(k-1)q^b <=(k-1)(A^a+q^a)<=k(A+q)^a. The induction is strict.

**k=3:** The r=3 base is covered above. For r>=7, B<=2A^(2/3), because A^(1/3)/h decreases in h and at r=7, B^3=21^3=9261<8*35^2=9800. Apply the same Jensen induction using k=2. For r=4,5,6 and 1<=q<B, D_2(q)<=q+1 (q edges sharing a vertex), so D_3(A+q)-1<=B+q. The ratio R(q)=(A+q)^2/(B+q)^3 increases then decreases because R'/R=(2B-3A-q)/((A+q)(B+q)). Its minimum on [1,B-1] is at an endpoint. The exact positive margins 27(A+q)^2-(B+q)^3 at q=1 and B-1 are: r4 (332,856), r5 (1936,2888), r6 (7811,6823). For q=0 use B-1<3A^(2/3). QED.

## Scope, adversarial controls, and next target

This is a universal **endpoint** lemma valid for unbounded degree and unbounded excess s=a1-d, independent of Smyth and the unreviewed d<=17 certificates. It does not imply any interior KK inequality, so it does **not** prove Bell–Skandera. The stronger no-ceiling inequality D_k(m)<=k*m^((k-1)/k) is false at (k,m)=(10,2) and (10,3). A standard-library exact verifier checked 198,000 (k,m) grid pairs, 6,225 random large pairs, 2,033 ratio controls, 28 small k=3 cases and 480 positive-integer-root polynomials. The symbolic argument, not these samples, establishes the lemma.

Original KK/Maclaurin definitions: Bell–Skandera, https://www.lehigh.edu/~mas906/papers/logc.pdf (Theorem 2.2, Observation 3.4). Novelty has not been checked exhaustively. Seek independent review and an analogous **interior-index** theorem; do not extend degree 18.