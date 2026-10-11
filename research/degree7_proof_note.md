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