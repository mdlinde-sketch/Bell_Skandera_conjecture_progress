# Independent adversarial audit: degree-5 Bell–Skandera candidate proof

**Audit date:** 9 October 2026. **Status:** independent computational validation passes; mathematical reduction rechecked; no earlier degree-5 theorem found in targeted literature review. Not peer-reviewed and not a guarantee of originality.

## 1. Mathematical statement and infinite reduction

Let \(F(t)=1+at+bt^2+ct^3+dt^4+et^5\), with positive integer coefficients and five real zeros. All zeros are negative and \(F(t)=\prod_{i=1}^5(1+\lambda_i t)\) with \(\lambda_i>0\). Put \(u=(1,a,b,c,d,e)\), \(C_k=\binom5k\). Maclaurin yields

\[u_{k+1}^{k} C_k^{k+1}\le C_{k+1}^{k}u_k^{k+1}.\]

Since \(e=\prod_i\lambda_i\ge1\), also \(u_k\ge C_k\). Write \(K_k(m)\) for the Kruskal–Katona largest possible count of \((k+1)\)-faces when there are \(m\) \(k\)-faces. If \(u_{k+1}>K_k(u_k)\), integrality implies the **necessary inequality**

\[(K_k(m)+1)^k C_k^{k+1}\le C_{k+1}^k m^{k+1},\qquad m=u_k. \tag{A}\]

For \(r\ge14\) such that \(\binom r k\le m<\binom{r+1}k\), colex compression gives \(K_k(m)\ge\binom r{k+1}\). Define

\[R_k(x)=\frac{\binom{x}{k+1}^{k}}{\binom{x+1}k^{k+1}},\qquad x>k.\]

The normalized logarithmic derivative equals

\[\frac{1}{k+1}\sum_{j=0}^k\frac1{x-j}-\frac1k\sum_{j=-1}^{k-2}\frac1{x-j}>0,\]

because a uniform index on \(\{0,\ldots,k\}\) strictly first-order stochastically dominates a uniform index on \(\{-1,\ldots,k-2\}\), and \(j\mapsto1/(x-j)\) is strictly increasing. Thus \(R_k\) is increasing. The exact inequalities

\[\binom{14}{k+1}^{k}\binom5k^{k+1}>\binom5{k+1}^{k}\binom{15}k^{k+1}\quad (k=1,2,3,4)\]

have positive left-minus-right margins respectively **25**, **16,733,500**, **4,672,611,811,875**, and **45,461,556,098,196,875**. Hence Maclaurin is strictly too strong to permit any KK violation whenever \(m\ge\binom{14}k\).

The independent colex construction checks all smaller \(m\), finding precisely

| k | Small \(m\) for which (A) permits a violation |
|---|---|
|1|none|
|2|11, 12, 13, 17, 18|
|3|12, 13, 14, 15, 17|
|4|none|

## 2. Independent finite enumeration

The new `bell_skandera_degree5_independent.py` constructs all \(k\)-faces in colex order on 15 vertices, computes the number of \((k+1)\)-faces for which all \(k\)-faces are present, and thereby obtains \(K_k(m)\) **without** implementing the original binomial-expansion \(K_k\) routine. For \(m<\binom{14}k\) the universe is more than large enough. The Kruskal–Katona extremal theorem guarantees colex attains the maximum.

To cover all possible real-rooted KK failures, Newton's necessary inequalities restrict to

\[b\in[10,28],\qquad c\in[10,32],\qquad b\in B\ \text{or}\ c\in C,\]
\[5\le a\le\left\lfloor b^2/(2c)\right\rfloor,\qquad 2a^2\ge5b,\]
\[5\le d\le\left\lfloor c^2/(2b)\right\rfloor,\qquad1\le e\le\left\lfloor2d^2/(5c)\right\rfloor,\]

where \(B=\{11,12,13,17,18\}\) and \(C=\{12,13,14,15,17\}\). The bounds on \(b,c\) follow from \(a,d\ge5\), so no unbounded cases are omitted. There are **125** integer vectors satisfying these conditions. For a hand-checkable count, define

\[A(b,c)=\#\{a\in\mathbb Z: a\ge5,\ 2a^2\ge5b,\ 2ac\le b^2\},\]
\[E(b,c)=\sum_{d=5}^{\lfloor c^2/(2b)\rfloor}\left\lfloor\frac{2d^2}{5c}\right\rfloor.\]

Then the number of candidate vectors at \((b,c)\) is \(A(b,c)E(b,c)\). All nonzero entries are given below; every other pair in the stated rectangle contributes zero.

| (b,c) | Count | (b,c) | Count |
|---|---:|---|---:|
| (12,12) | 1 | (13,13) | 1 |
| (13,14) | 2 | (14,13) | 2 |
| (14,14) | 4 | (14,15) | 2 |
| (15,14) | 2 | (15,15) | 1 |
| (16,14) | 3 | (16,15) | 2 |
| (16,17) | 3 | (17,16) | 3 |
| (17,17) | 4 | (17,18) | 6 |
| (17,19) | 5 | (17,20) | 6 |
| (18,16) | 4 | (18,17) | 6 |
| (18,18) | 9 | (18,19) | 10 |
| (18,20) | 12 | (18,21) | 7 |
| (18,22) | 10 | (18,23) | 12 |
| (19,17) | 4 | (20,17) | 4 |

**Total: 125.** Only six violate any Kruskal–Katona inequality.

## 3. Exact, machine-independent Hermite witnesses

For every candidate, form \(Q(x)=x^5-ax^4+bx^3-cx^2+dx-e\). Define \(p_j=\sum_i\lambda_i^j\) (\(p_0=5\)), and \(H_q=(p_{i+j})_{i,j=0}^{q-1}\). For real roots, each \(H_q\) is a sum of five rank-one positive semidefinite matrices and \(\det H_q\ge0\).

The following table contains enough integer power sums to independently reconstruct each needed determinant, using just a 3×3 determinant except for row 2, which uses a 4×4 determinant. It also records the exact KK failure.

| (a,b,c,d,e) | KK failure | (p0,p1,p2,p3,p4,p5,p6) | Negative witness |
|---|---|---|---|
| (6,12,12,6,1) | c=12 > K2(12)=11; d=6 > K3(12)=5 | (5,6,12,36,120,401,1332) | det H3 = **-144** |
| (6,13,14,6,1) | c=14 > K2(13)=13 | (5,6,10,24,74,241,766) | det H4 = **-2846** |
| (6,13,14,7,1) | c=14 > K2(13)=13; d=7 > K3(14)=6 | (5,6,10,24,70,211,628) | det H3 = **-20** |
| (6,14,14,7,1) | d=7 > K3(14)=6 | (5,6,8,6,-20,-129,-460) | det H3 = **-196** |
| (7,14,14,7,1) | d=7 > K3(14)=6 | (5,7,21,91,413,1867,8421) | det H3 = **-784** |
| (6,14,15,8,1) | d=8 > K3(15)=7 | (5,6,8,9,0,-49,-217) | det H3 = **-53** |

For the only row where \(H_3\) is not negative, its full witness is

\[H_4=\begin{pmatrix}5&6&10&24\\6&10&24&74\\10&24&74&241\\24&74&241&766\end{pmatrix},\qquad\det H_4=-2846.\]

Every entry can also be checked without computer software from Newton's identities applied to \(Q\). The new verifier **independently** obtains the same power sums as traces of integer powers of the companion matrix \(C\), with characteristic polynomial \(Q\), and calculates determinants through SymPy (not the original code's permutation expansion). Independent exact real-root counting returns fewer than five distinct real roots for every candidate.

## 4. Novelty review (targeted, not a proof of originality)

* Jason Bell and Mark Skandera, *Multicomplexes and polynomials with real zeros*, Discrete Mathematics 307 (2007), 668–682, DOI 10.1016/j.disc.2006.07.020, https://www.lehigh.edu/~mas906/papers/logc.pdf. Establishes multicomplex realisation and a **fixed-degree finiteness** theorem, but not this degree-five elimination.
* Lili Mu and Volkmar Welker, *On a question about real-rooted polynomials and f-polynomials of simplicial complexes*, Advances in Applied Mathematics 175 (2026), 103041, DOI 10.1016/j.aam.2026.103041, https://arxiv.org/abs/2503.24076. Establishes sufficient criteria and investigates recursive methods, but does not claim a degree-five theorem.
* Feihu Liu, Ying Wang, Zihao Zhang, *Counterexamples to the Mu–Welker recursive decomposition in every degree*, arXiv:2609.23694v2 (23 September 2026), https://arxiv.org/html/2609.23694v2. Describes the general Bell–Skandera question as open; resolves only a proposed decomposition-related conjecture in the negative.
* Additional keyword searches tried: “Bell–Skandera degree 5”, “Bell Skandera quintic”, “real-rooted Kruskal–Katona degree five”, “real-rooted f-vector low degrees”, and name/title variants. No prior **degree-five proof** surfaced as of this audit.

**Limitations:** Negative search results cannot rule out an unindexed, differently phrased, unpublished or very recent proof. This novelty review is not an expert priority determination. External subject-matter review remains advisable prior to submission.

## 5. Overall assessment

No discrepancy was found in the reduction, finite enumeration, Hermite witnesses or independent symbolic real-root count. This is a **credible candidate proof of the degree-five Bell–Skandera assertion**, with independent reproducible exact-arithmetic checks. It is not yet peer-reviewed, and the originality question remains provisional.

To rerun the independent certificate: `python bell_skandera_degree5_independent.py` (Python 3.9+ with SymPy). The original standard-library-only verifier is `bell_skandera_degree5_verification.py`.