# A proposed exact proof of the degree-five Bell–Skandera assertion

**Status:** Self-contained argument with finite exact-arithmetic certificate, independently cross-checked by symbolic real-root counts. **Not peer-reviewed; novelty not established.** 8 October 2026.

## Theorem (proposed)

Every polynomial
\[
F(t)=1+at+bt^2+ct^3+dt^4+et^5\in\mathbb Z[t]
\]
with positive coefficients and only real zeros is the \(f\)-polynomial of a simplicial complex.

## 1. Continuous bounds and discrete shadows

Put \(u_0=1,u_1=a,u_2=b,u_3=c,u_4=d,u_5=e\), and \(C_k=\binom5k\). Since the zeros are real and the coefficients positive, \(F(t)=\prod_{j=1}^5(1+\lambda_j t)\) with \(\lambda_j>0\). The \(u_k\) are elementary symmetric functions of the \(\lambda_j\). Maclaurin's inequalities imply
\[
u_{k+1}^k C_k^{k+1}\le C_{k+1}^k u_k^{k+1}\quad(1\le k\le4),
\]
and, since \(e\ge1\), also \(u_k\ge C_k\) for \(1\le k\le5\).

Let \(K_k(m)\) denote the Kruskal–Katona maximum for \((k+1)\)-faces from \(m\) \(k\)-faces: if \(m=\sum_j\binom{r_j}{j}\) is the \(k\)-binomial expansion, then \(K_k(m)=\sum_j\binom{r_j}{j+1}\). The Kruskal–Katona theorem says that \(F\) is an \(f\)-polynomial exactly when \(u_{k+1}\le K_k(u_k)\) for \(k=1,2,3,4\).

If the inequality at index \(k\) fails, integrality gives \(u_{k+1}\ge K_k(u_k)+1\). Hence, with \(m=u_k\), necessarily
\[
C_{k+1}^k m^{k+1}\ge (K_k(m)+1)^k C_k^{k+1}.\tag{1}
\]

## 2. Uniform finite bound for all four indices

For real \(x>k\) put
\[
R_k(x)=\frac{\binom{x}{k+1}^{k}}{\binom{x+1}{k}^{k+1}}.
\]
Its logarithmic derivative divided by \(k(k+1)\) is
\[
\frac1{k+1}\sum_{j=0}^k\frac1{x-j}-\frac1k\sum_{j=-1}^{k-2}\frac1{x-j}>0.
\]
The inequality holds because \(j\mapsto1/(x-j)\) is increasing and the uniform distribution on \(\{0,\ldots,k\}\) stochastically dominates the uniform distribution on \(\{-1,\ldots,k-2\}\). Thus \(R_k\) increases.

Direct integer arithmetic verifies, for each \(k=1,2,3,4\),
\[
\binom{14}{k+1}^{k} C_k^{k+1}\ge C_{k+1}^{k}\binom{15}{k}^{k+1}.
\]
For any \(m\ge\binom{14}{k}\), choose \(r\ge14\) such that \(\binom r k\le m<\binom{r+1}k\). Then \(K_k(m)\ge\binom r{k+1}\), and the increasing-ratio bound gives
\[
C_{k+1}(m/C_k)^{(k+1)/k}<\binom r{k+1}\le K_k(m).
\]
Consequently, (1) is impossible for \(m\ge\binom{14}k\).

For the remaining finite ranges \(C_k\le m<\binom{14}k\), evaluating (1) exactly gives:

| Index \(k\) | Only values of \(u_k\) where a KK failure is not ruled out |
|---|---|
| 1 | none |
| 2 | \(11,12,13,17,18\) |
| 3 | \(12,13,14,15,17\) |
| 4 | none |

The attached Python verifier checks these finite statements using integers only.

## 3. Exhaustive reduction to six integer vectors

Let \(B=\{11,12,13,17,18\}\) and \(C=\{12,13,14,15,17\}\). Any KK failure must have \(b\in B\) or \(c\in C\). Newton's inequalities for degree five imply
\[
2a^2\ge5b,\quad b^2\ge2ac,\quad c^2\ge2bd,\quad 2d^2\ge5ce.
\]
Since \(a\ge5\) and \(d\ge5\), an exceptional \(b\) implies \(c\le\lfloor b^2/10\rfloor\le32\); an exceptional \(c\) implies \(b\le\lfloor c^2/10\rfloor\le28\). Thus every potential counterexample occurs in the **finite**, overinclusive set
\[
10\le b\le28,\quad10\le c\le32,\quad (b\in B\lor c\in C),
\]
\[
5\le a\le\lfloor b^2/(2c)\rfloor,\quad
5\le d\le\lfloor c^2/(2b)\rfloor,\quad
1\le e\le\lfloor2d^2/(5c)\rfloor,\quad
2a^2\ge5b.
\]
An exhaustive enumeration with exact integer arithmetic finds **125** vectors in this set. Exactly **six** violate at least one Kruskal–Katona inequality:

| \((a,b,c,d,e)\) | \(\det H_3\) | \(\det H_4\) |
|---|---:|---:|
| (6,12,12,6,1) | -144 | -600 |
| (6,13,14,6,1) | 36 | -2846 |
| (6,13,14,7,1) | -20 | -710 |
| (6,14,14,7,1) | -196 | 348 |
| (7,14,14,7,1) | -784 | -8064 |
| (6,14,15,8,1) | -53 | -362 |

## 4. Exact rejection by moment-matrix positivity

For a hypothetical real-rooted candidate, set
\[
Q(x)=x^5-a x^4+b x^3-c x^2+d x-e=\prod_{j=1}^5(x-\lambda_j).
\]
Let \(p_s=\sum_j\lambda_j^s\), with \(p_0=5\), computed from the coefficients by Newton identities. For \(q=3,4\), define the Hankel/Hermite moment matrix \(H_q=(p_{i+j})_{0\le i,j<q}\). Since
\[
H_q=\sum_{j=1}^5 (1,\lambda_j,\ldots,\lambda_j^{q-1})^T
(1,\lambda_j,\ldots,\lambda_j^{q-1}),
\]
its determinant must be nonnegative for real \(\lambda_j\). The table gives an explicitly negative determinant for every one of the six remaining vectors. None is real-rooted. Therefore every degree-five real-rooted positive integer polynomial satisfies all four Kruskal–Katona inequalities. \(\square\)

## Reproducibility and limits

The companion `bell_skandera_degree5_verification.py` checks all finite inequalities, enumerates all 125 candidates, calculates the six exact Hermite determinants and asserts the theorem's finite certificate. A separate SymPy root-isolation calculation independently found only 1 or 3 distinct real roots in each of the six cases, never 5.

**Literature:** Bell–Skandera, *Multicomplexes and Polynomials with Real Zeros* (2007), especially Theorem 4.8; Mu–Welker, *On a question about real rooted polynomials and f-polynomials of simplicial complexes* (2026); Liu–Wang–Zhang, *Counterexamples to the Mu–Welker recursive decomposition in every degree* (September 2026). The current proof adapts classical Maclaurin/Kruskal–Katona machinery with exact finite certification and moment positivity. An external mathematician should verify both the proof and its originality before any public theorem claim.
