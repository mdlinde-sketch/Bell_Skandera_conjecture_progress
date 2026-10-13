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
