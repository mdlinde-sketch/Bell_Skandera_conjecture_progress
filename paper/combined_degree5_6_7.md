# Bell–Skandera conjecture: computational candidate proofs in degrees 5, 6 and 7

**Status (11 October 2026): Unreviewed, AI-generated research manuscript. These are *candidate proofs*, not established mathematical results.** The three degree-specific arguments and their verification code are provided for public inspection. Computational checks do not replace critical review of the infinite-to-finite reduction, exhaustiveness, or validity of the mathematical steps.

**Research provenance:** The human project lead proposed the cross-domain discovery process, selected the Bell–Skandera conjecture, and directed the work. GPT-6 generated the mathematical arguments, calculations, and verification programs. No independent mathematician has certified these claims.

This document collates the original proof notes; it is not evidence of additional verification. See the `verification/` directory for runnable programs and `reviews/` for a preliminary adversarial review of degree 5. Please open a GitHub issue with a minimal counterexample, a failing calculation, or a literature reference if an error or prior result is found.

---

# Part 1 — Degree 5

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

---

# Part 2 — Degree 6

# An exact finite certificate for the degree-six Bell–Skandera assertion

**Research note, 9 October 2026. Status: candidate proof, not peer-reviewed.**

## Statement

**Proposed theorem.** If
\[
F(t)=1+a t+b t^2+c t^3+d t^4+e t^5+f t^6\in\mathbb Z[t]
\]
has positive coefficients and only real zeros, then its coefficient vector is the face vector of a simplicial complex.

This is a degree-six case of the Bell–Skandera question, not a proof of the general conjecture.

## 1. Continuous-to-discrete reduction

Write \(u=(1,a,b,c,d,e,f)\), \(C_k=\binom6k\), and
\(F(t)=\prod_{i=1}^{6}(1+\lambda_i t)\) with \(\lambda_i>0\).
Maclaurin's inequalities imply
\[
 u_{k+1}^{k} C_k^{k+1}\le C_{k+1}^{k}u_k^{k+1}
 \quad (1\le k\le5).
\tag{1}
\]
Since \(u_6=f=\prod\lambda_i\ge1\), they also imply \(u_k\ge C_k\) for every \(k\).

Let \(K_k(m)\) be the largest possible number of \((k+1)\)-element faces with exactly \(m\) \(k\)-element faces, given by the canonical \(k\)-binomial (colex) expansion. Kruskal–Katona says that \(u\) is an \(f\)-vector precisely when \(u_{k+1}\le K_k(u_k)\) for all \(k=1,\ldots,5\).

If the inequality at \(k\) fails and \(m=u_k\), integrality and (1) require
\[
 (K_k(m)+1)^k C_k^{k+1}\le C_{k+1}^k m^{k+1}.
 \tag{2}
\]

For \(x>k\), the ratio
\[
 R_k(x)=\frac{\binom{x}{k+1}^{k}}{\binom{x+1}{k}^{k+1}}
\]
is strictly increasing. Indeed, its logarithmic derivative divided by \(k(k+1)\) equals
\[
 \frac1{k+1}\sum_{j=0}^k\frac1{x-j}
 -\frac1k\sum_{j=-1}^{k-2}\frac1{x-j}>0,
\]
since the first uniform index distribution stochastically dominates the second and \(j\mapsto1/(x-j)\) is increasing.

For each \(k\), the following exact positive integer margins certify that
\(\binom r{k+1}^k C_k^{k+1}>C_{k+1}^k\binom{r+1}k^{k+1}\) at \(r=r_k\):

| \(k\) | \(r_k\) | \(\binom{r_k}k\) | Left minus right |
|---:|---:|---:|---:|
| 1 | 17 | 17 | 36 |
| 2 | 15 | 105 | 7,509,375 |
| 3 | 14 | 364 | 15,830,171,800,625 |
| 4 | 12 | 495 | 56,605,491,731,250,000 |
| 5 | 10 | 252 | 9,330,627,060,167,616 |

For \(m\ge\binom{r_k}k\), choose \(r\ge r_k\) with \(\binom rk\le m<\binom{r+1}k\). Then \(K_k(m)\ge\binom r{k+1}\), while (1) and the increasing ratio give
\[
 u_{k+1}\le C_{k+1}(m/C_k)^{(k+1)/k}
 < C_{k+1}(\binom{r+1}k/C_k)^{(k+1)/k}
 <\binom r{k+1}\le K_k(m).
\]
Hence only \(C_k\le m<\binom{r_k}k\) can violate KK. Checking (2) with exact integers over those finite intervals leaves:

| Index \(k\) | Values of \(u_k\) not ruled out |
|---:|---|
| 1 | none |
| 2 | \(B=\{16,17,18,19,23,24,25\}\) |
| 3 | \(C=\{21,22,23,24,25,26,27,28,29,31,32,33,42,43\}\) |
| 4 | \(D=\{17,18,19,20,21,22,23,24,27,28,29,30\}\) |
| 5 | none |

## 2. Rigorous finite coefficient bounds

The degree-six Newton inequalities are
\[
12b\le5a^2,\quad15ac\le8b^2,\quad16bd\le9c^2,
\quad15ce\le8d^2,\quad12df\le5e^2.\tag{3}
\]
Any possible counterexample has \(b\in B\), \(c\in C\), or \(d\in D\). The coefficient lower bounds are \(a\ge6,b\ge15,c\ge20,d\ge15,e\ge6,f\ge1\).

* If \(b\in B\), then \(b\le25\), \(c\le\lfloor8\cdot25^2/(15\cdot6)\rfloor=55\), and \(d\le\lfloor9\cdot55^2/(16\cdot15)\rfloor=113\).
* If \(c\in C\), then \(c\le43\), \(b,d\le\lfloor9\cdot43^2/(16\cdot15)\rfloor=69\).
* If \(d\in D\), then \(d\le30\), \(c\le\lfloor8\cdot30^2/(15\cdot6)\rfloor=80\), and \(b\le\lfloor9\cdot80^2/(16\cdot15)\rfloor=240\).

Thus **every** counterexample is in the overinclusive integer box
\[
 15\le b\le240,\quad20\le c\le80,\quad15\le d\le113,
\]
with \(b\in B\lor c\in C\lor d\in D\), subject to \(16bd\le9c^2\) and
\[
 \max(6,\lceil\sqrt{12b/5}\rceil)\le a\le\left\lfloor\frac{8b^2}{15c}\right\rfloor,
\quad6\le e\le\left\lfloor\frac{8d^2}{15c}\right\rfloor,
\quad1\le f\le\left\lfloor\frac{5e^2}{12d}\right\rfloor.
\tag{4}
\]
There is **no arbitrary search cutoff**: (4) follows from necessary inequalities.

## 3. Exact exhaustive certificate

Enumerating (4) with integer arithmetic produces exactly **4,445** vectors. Evaluating all five Kruskal–Katona inequalities leaves exactly **22** violators. Each is rejected by a negative leading Hermite moment determinant of size 3 or 4.

For a candidate \(u\), form
\[
Q(x)=x^6-ax^5+bx^4-cx^3+dx^2-ex+f,
\quad p_s=\sum_{j=1}^6\lambda_j^s,
\quad H_q=(p_{i+j})_{0\le i,j<q}.
\]
The \(p_s\) are integer polynomials in the coefficients, computable by Newton's identities. If all \(\lambda_j\) are real, \(H_q=\sum_j v_q(\lambda_j)v_q(\lambda_j)^T\) is positive semidefinite, so \(\det H_q\ge0\).

The exact witnesses follow. The \(u\) column includes the constant coefficient 1. A negative determinant is a conclusive real-rootedness obstruction.

| \(u=(1,a,b,c,d,e,f)\) | Failed KK indices | Negative Hermite witness |
|---|---|---|
| `(1, 7, 18, 24, 18, 7, 1)` | 2, 3, 4 | det H3 = **-168** |
| `(1, 7, 19, 26, 20, 7, 1)` | 3 | det H3 = **-48** |
| `(1, 7, 19, 26, 20, 8, 1)` | 3, 4 | det H3 = **-48** |
| `(1, 7, 19, 27, 19, 7, 1)` | 2 | det H4 = **-8784** |
| `(1, 7, 19, 27, 20, 7, 1)` | 2, 3 | det H4 = **-3465** |
| `(1, 7, 19, 27, 21, 8, 1)` | 2, 3, 4 | det H3 = **-24** |
| `(1, 7, 20, 27, 20, 7, 1)` | 3 | det H3 = **-536** |
| `(1, 7, 20, 28, 21, 8, 1)` | 3, 4 | det H3 = **-236** |
| `(1, 7, 20, 28, 22, 8, 1)` | 3 | det H3 = **-256** |
| `(1, 7, 20, 28, 22, 9, 1)` | 3, 4 | det H3 = **-256** |
| `(1, 7, 20, 29, 21, 8, 1)` | 4 | det H3 = **-24** |
| `(1, 7, 20, 29, 23, 8, 1)` | 3 | det H3 = **-64** |
| `(1, 7, 20, 29, 23, 9, 1)` | 3, 4 | det H3 = **-64** |
| `(1, 7, 20, 30, 23, 9, 1)` | 4 | det H4 = **-3232** |
| `(1, 7, 20, 30, 24, 10, 1)` | 4 | det H4 = **-364** |
| `(1, 8, 21, 28, 21, 8, 1)` | 3, 4 | det H3 = **-896** |
| `(1, 8, 21, 29, 21, 8, 1)` | 4 | det H3 = **-1030** |
| `(1, 8, 22, 29, 21, 8, 1)` | 4 | det H3 = **-70** |
| `(1, 8, 22, 30, 23, 9, 1)` | 4 | det H3 = **-376** |
| `(1, 8, 22, 31, 23, 9, 1)` | 4 | det H3 = **-342** |
| `(1, 8, 23, 31, 23, 9, 1)` | 4 | det H3 = **-118** |
| `(1, 9, 23, 31, 23, 9, 1)` | 4 | det H3 = **-5012** |

All 22 determinants are independently reproduced by a separate implementation using **literal colex face sets** (rather than the Macaulay expansion) and **traces of companion-matrix powers** (rather than Newton's power-sum identities). A third exact check, symbolic real-root isolation with multiplicities, independently confirms that none of the 22 polynomials has six real roots. No candidate survives.

Therefore all degree-six real-rooted polynomials with positive integer coefficients and constant term 1 satisfy Kruskal–Katona, subject to independent review of the finite certificate. \(\square\)

## Reproducibility and limitations

* `bell_skandera_degree6_certificate.py`: self-contained Python 3 standard-library certificate, including exact monotonicity thresholds, exception sets, exhaustive enumeration, and Bareiss Hermite determinants.
* `bell_skandera_degree6_independent.py`: independently written checker, requiring SymPy, using literal colex complexes, companion matrices, and symbolic real-root isolation. Both report 4,445 candidates, 22 KK violators, and 22 negative Hermite witnesses.
* The derivation relies only on classical Maclaurin/Newton inequalities, Kruskal–Katona, and moment-matrix positivity. The computational novelty is the complete degree-six finite elimination, **not** any of these classical ingredients.
* Targeted searches of the Bell–Skandera (2007), Mu–Welker (2026), and Liu–Wang–Zhang (September 2026) literature found no earlier degree-six proof. This is not a guarantee of novelty. This note is not peer-reviewed and should be checked by a specialist before any submission.

### Literature

1. J. Bell and M. Skandera, *Multicomplexes and polynomials with real zeros*, Discrete Mathematics 307 (2007), 668–682. https://www.lehigh.edu/~mas906/papers/logc.pdf
2. L. Mu and V. Welker, *On a question about real rooted polynomials and f-polynomials of simplicial complexes*, Advances in Applied Mathematics 175 (2026), 103041. https://arxiv.org/abs/2503.24076
3. F. Liu, Y. Wang and Z. Zhang, *Counterexamples to the Mu–Welker recursive decomposition in every degree*, arXiv:2609.23694 (September 2026). https://arxiv.org/abs/2609.23694

---

# Part 3 — Degree 7

# A finite exact certificate for the degree-seven Bell–Skandera assertion

**Research note — 11 October 2026. Status: AI-generated candidate proof; not peer-reviewed or independently checked by a mathematician.**

## Proposed theorem

If

\[
F(t)=1+u_1t+u_2t^2+\cdots+u_7t^7\in\mathbb Z[t]
\]

has strictly positive coefficients and only real zeros, then its coefficient sequence is the face vector of a simplicial complex. This establishes the degree-seven case of the Bell–Skandera conjecture **provided the mathematical reduction and accompanying exact certificates withstand independent specialist review**. It does not establish the conjecture in general.

The proof strategy transfers a condition from the **truncated moment problem** (positive semidefinite Hankel/Hermite matrices) to a **discrete extremal combinatorics** constraint (Kruskal–Katona), with the infinite-to-finite step supplied by **ultra-log-concavity** and coefficient integrality.

## 1. Real-rootedness constraints

All zeros of \(F\) are negative because its coefficients are positive. Thus

\[
F(t)=\prod_{i=1}^7(1+\lambda_i t),\qquad \lambda_i>0.
\]

Put \(C_j=\binom7j\), \(v_j=u_j/C_j\), and \(v_0=1\). Newton's inequalities make \((v_j)_{j=0}^7\) log-concave:

\[
v_j^2\ge v_{j-1}v_{j+1}\quad(1\le j\le6).
\tag{1}
\]

Because \(u_7=\prod_i\lambda_i\) is a positive integer, \(v_7=u_7\ge1\). The Maclaurin inequalities give \(v_j\ge v_7^{j/7}\ge1\), hence

\[
u_j\ge C_j\quad(0\le j\le7).\tag{2}
\]

Log-concavity between \(v_0=1\), \(v_k\), and \(v_7\ge1\) yields the following two-sided coefficient bounds for any fixed \(1\le k\le6\):

\[
\boxed{\begin{aligned}
 v_j&\le v_k^{(7-j)/(7-k)} && (1\le j<k),\\
 v_j&\le v_k^{j/k} && (k<j\le7).
\end{aligned}}\tag{3}
\]

The first inequality is obtained by interpolating the concave sequence \(\log v_i\) between \(j\) and \(7\); the second interpolates between \(0\) and \(j\). These are exact, not numerical, bounds.

## 2. Reduction to 93 exceptional coefficient values

Let \(K_k(m)\) be the Kruskal–Katona upper-shadow function, calculated by the canonical \(k\)-binomial expansion of \(m\). The coefficient sequence is a simplicial-complex face vector if and only if

\[
u_{k+1}\le K_k(u_k)\quad(1\le k\le6).\tag{4}
\]

Maclaurin's inequality implies

\[
u_{k+1}^k C_k^{k+1}\le C_{k+1}^k u_k^{k+1}.\tag{5}
\]

If (4) fails at \(k\), integrality requires

\[
(K_k(m)+1)^k C_k^{k+1}\le C_{k+1}^k m^{k+1},\qquad m=u_k.\tag{6}
\]

For \(x>k\), define

\[
R_k(x)=\frac{\binom{x}{k+1}^k}{\binom{x+1}{k}^{k+1}}.
\]

It is strictly increasing: the logarithmic derivative divided by \(k(k+1)\) is

\[
\frac1{k+1}\sum_{j=0}^k\frac1{x-j}
-\frac1k\sum_{j=-1}^{k-2}\frac1{x-j}>0.
\]

The first average dominates the second because \(j\mapsto1/(x-j)\) is increasing and the first uniform index distribution stochastically dominates the second.

Choose \(r_k\) so that

\[
\binom{r_k}{k+1}^k C_k^{k+1}
>C_{k+1}^k\binom{r_k+1}{k}^{k+1}.\tag{7}
\]

For \(m\ge\binom{r_k}{k}\), choose \(r\ge r_k\) with \(\binom r k\le m<\binom{r+1}k\). The monotonicity above, (5), and \(K_k(m)\ge\binom r{k+1}\) imply \(u_{k+1}<K_k(m)\). Therefore a violation can only occur below \(\binom{r_k}k\). Exact integer evaluations of (6) in those finite ranges yield:

| \(k\) | \(r_k\) | Number of exceptional \(m=u_k\) | Exceptional values |
|---:|---:|---:|---|
| 1 | 20 | 0 | none |
| 2 | 18 | 14 | 22–27, 30–34, 39–41 |
| 3 | 17 | 32 | 36–54, 61–70, 72–74 |
| 4 | 15 | 27 | 37–54, 56–64 |
| 5 | 13 | 20 | 24–35, 38–45 |
| 6 | 11 | 0 | none |

Each threshold (7) is checked with a **strict positive integer margin** in the standard-library certificate. All 3,841 coefficient values in the finite ranges are independently checked against literal colex face sets (including the 93 exceptional values).

## 3. No arbitrary search cutoffs

If (4) fails at \(k\), its coefficient \(u_k\) belongs to the exceptional set \(E_k\). Put \(M_k=\max E_k\). From (3), for every \(j\),

\[
u_j\le C_j\left(\frac{M_k}{C_k}\right)^{p/q},
\qquad
(p,q)=\begin{cases}
(7-j,7-k)&j<k,\\
(j,k)&j\ge k.
\end{cases}
\tag{8}
\]

The exact integer cap is the largest \(U_j\) satisfying

\[
U_j^q C_k^p\le C_j^q M_k^p.\tag{9}
\]

The caps for \((u_1,\ldots,u_7)\) are:

| Failed KK index | Exact coefficient caps |
|---:|---|
| 2 | (15, 41, 95, 133, 111, 52, 10) |
| 3 | (21, 53, 74, 94, 73, 31, 5) |
| 4 | (23, 57, 78, 64, 44, 17, 2) |
| 5 | (68, 141, 160, 109, 45, 17, 2) |

For each \(m\in E_k\), all possible integer values \(n=u_{k+1}\) with \(n>K_k(m)\) and \(n^kC_k^{k+1}\le C_{k+1}^km^{k+1}\) are generated exactly. There are respectively **33, 89, 73, and 27** possible adjacent violating pairs for \(k=2,3,4,5\).

The six Newton inequalities are, in integers,

\[
\begin{gathered}
3u_1^2\ge7u_2,\qquad 5u_2^2\ge9u_1u_3,\\
3u_3^2\ge5u_2u_4,\qquad3u_4^2\ge5u_3u_5,\\
5u_5^2\ge9u_4u_6,\qquad3u_6^2\ge7u_5u_7.
\end{gathered}\tag{10}
\]

For every violating pair, a depth-first search fills all remaining coefficients within the exact caps (9) and the lower bounds (2), pruning via (10) and checking all six inequalities at completion. The search uses **only integer arithmetic**.

## 4. Moment-matrix falsification of every remaining candidate

Let

\[
Q(x)=x^7-u_1x^6+u_2x^5-u_3x^4+u_4x^3-u_5x^2+u_6x-u_7
\]

have roots \(\lambda_1,\ldots,\lambda_7\). Write \(p_s=\sum_i\lambda_i^s\) and

\[
H_q=(p_{i+j})_{0\le i,j<q}.
\]

If all roots are real, \(H_q=\sum_i(1,\lambda_i,\ldots,\lambda_i^{q-1})(1,\lambda_i,\ldots,\lambda_i^{q-1})^T\) is positive semidefinite, so **every** \(\det H_q\ge0\). The integer power sums are computed by Newton identities. A negative determinant is a conclusive obstruction to real-rootedness.

| Failed KK index \(k\) | Newton-admissible vectors | \(\det H_3\ge0\) | Of those, \(\det H_4<0\) |
|---:|---:|---:|---:|
| 2 | 1,660 | 848 | 848 |
| 3 | 455 | 4 | 4 |
| 4 | 146 | 24 | 24 |
| 5 | 263 | 44 | 44 |
| **Total** | **2,524** | **920** | **920** |

The totals count a polynomial more than once if it violates more than one KK inequality. The 920 \(H_3\)-nonnegative occurrences correspond to **902 distinct coefficient vectors**. Each is excluded by a negative fourth-order Hermite determinant. For instance,

\[
(u_0,\ldots,u_7)=(1,8,26,46,47,27,8,1)
\]

violates KK, satisfies all six Newton inequalities, and has

\[
\boxed{\det H_3=52,\qquad\det H_4=-4084.}
\]

The exact enumeration leaves **zero possible real-rooted KK violators**. Together with the analytic reductions, this supplies the proposed degree-seven proof. \(\square\)

## 5. Independent adversarial checks

- `bell_skandera_degree7_certificate.py` is a Python 3 standard-library certificate using a generic constraint-satisfaction recursion, exact binomial expansions, Newton's identities, and fraction-free Bareiss determinants. It independently constructs every search bound and checks all candidate counts.
- `bell_skandera_degree7_independent.py` is a separate implementation requiring SymPy. It uses four distinct explicit nested-loop enumeration schemes, computes KK bounds independently and checks **all 3,841 finite-range KK shadow values** against literal colex simplicial complexes, then computes all 902 negative \(H_4\) determinants from **traces of a 7×7 companion matrix** rather than Newton's identities.
- Both programs reproduce exactly 2,524 Newton-admissible candidate occurrences, 920 occurrences with nonnegative \(H_3\), and no candidate with nonnegative \(H_4\).
- As a cross-check against prior work, all 902 distinct \(H_3\)-nonnegative vectors have \(u_1\in\{8,9\}\). Bell and Skandera (2007) reported the containment of real-rooted f-polynomials in simplicial f-polynomials for fixed first coefficient \(u_1\le10\), although that reported finite check is not a substitute for independently auditing the new certificate.

## 6. Novelty and limitations

Bell and Skandera (2007) already established that each fixed degree has at most finitely many counterexamples; the **finiteness mechanism is not new**. Mu and Welker (2026) established further sufficient criteria. Liu, Wang, and Zhang (September 2026) disproved a separate recursive-decomposition conjecture, not the Bell–Skandera question. Targeted searches did not find a prior degree-seven proof, but absence from search results is **not evidence of priority**.

The potential new contribution is the **explicit complete degree-seven finite elimination** with two exact, reproducible computational certificates. The argument remains **unreviewed AI-generated research**. An independent mathematician should scrutinise especially the monotone cutoff, the two-sided log-concavity bounds, the completeness of the coefficient enumeration, and the relationship between moment-matrix positivity and real-rootedness before the result is described as an established theorem.

### Sources

1. J. Bell and M. Skandera, *Multicomplexes and polynomials with real zeros*, Discrete Mathematics 307 (2007), 668–682. https://www.lehigh.edu/~mas906/papers/logc.pdf
2. L. Mu and V. Welker, *On a question about real rooted polynomials and f-polynomials of simplicial complexes*, Advances in Applied Mathematics 175 (2026), 103041. https://arxiv.org/abs/2503.24076
3. F. Liu, Y. Wang and Z. Zhang, *Counterexamples to the Mu–Welker recursive decomposition in every degree*, arXiv:2609.23694 (September 2026). https://arxiv.org/abs/2609.23694