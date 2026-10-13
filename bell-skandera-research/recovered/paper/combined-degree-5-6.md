# Finite exact certificates for the degree-five and degree-six cases of the Bell–Skandera question

**Research draft — 10 October 2026 — unreviewed, AI-generated; novelty unconfirmed.**

## Abstract

We present candidate proofs that a polynomial with constant coefficient 1, positive integral coefficients and only real zeros is the face polynomial of a simplicial complex when its degree is five or six. The proof method combines classical Maclaurin inequalities for elementary symmetric functions, a monotone binomial-ratio comparison to Kruskal–Katona upper shadows, exact enumeration under Newton's inequalities, and negative Hermite moment-matrix determinants for every enumerated candidate obstruction. The finite portions are independently reproduced by two programs employing distinct combinatorial and algebraic implementations. These arguments have not received external expert review.

## 1. Definitions and statement

Let

$$F(t)=\sum_{k=0}^n u_k t^k,\quad u_0=1,\quad u_k\in\mathbb{Z}_{>0}\ (1\le k\le n),\quad n\in\{5,6\}.$$

A *face polynomial* of a simplicial complex records the numbers of faces by cardinality, including the empty face. Define the Kruskal–Katona upper-shadow function $K_k(m)$ as follows: express $m=\binom{r_k}{k}+\binom{r_{k-1}}{k-1}+\cdots$ in its canonical $k$-binomial representation with decreasing upper indices and put $K_k(m)=\binom{r_k}{k+1}+\binom{r_{k-1}}{k}+\cdots$. The required and sufficient inequalities are $u_{k+1}\le K_k(u_k)$ for $k=1,\ldots,n-1$.

**Candidate theorem.** For $n=5$ and for $n=6$, every such $F$ with all roots real satisfies the Kruskal–Katona inequalities and hence is a simplicial-complex face polynomial.

## 2. Reduction from a continuous inequality to finite exceptions

All zeros of $F$ must be negative. Write $F(t)=\prod_{j=1}^n(1+\lambda_jt)$ with $\lambda_j>0$. Let $C_k=\binom nk$. Maclaurin's inequalities for the elementary symmetric functions $u_k$ yield

$$u_{k+1}^{k}C_k^{k+1}\le C_{k+1}^{k}u_k^{k+1}.\tag{1}$$

Since $u_n=\prod_j\lambda_j\ge1$, they also give $u_k\ge C_k$ for every $k$. A violation of Kruskal–Katona at index $k$ necessarily has, by coefficient integrality,

$$C_{k+1}^{k}m^{k+1}\ge (K_k(m)+1)^k C_k^{k+1},\quad m=u_k.\tag{2}$$

For $x>k$, set

$$R_k(x)=\frac{\binom{x}{k+1}^{k}}{\binom{x+1}{k}^{k+1}}.$$

This is strictly increasing: its logarithmic derivative, divided by $k(k+1)$, equals

$$\frac1{k+1}\sum_{j=0}^{k}\frac1{x-j}-\frac1k\sum_{j=-1}^{k-2}\frac1{x-j}>0,$$

since the first uniform index distribution stochastically dominates the second, and $j\mapsto1/(x-j)$ increases. If at some integer $r_0$ we have

$$\binom{r_0}{k+1}^{k}C_k^{k+1}>C_{k+1}^{k}\binom{r_0+1}{k}^{k+1},\tag{3}$$

then every $m\ge\binom{r_0}k$ satisfies $u_{k+1}<K_k(m)$ by choosing $r\ge r_0$ with $\binom rk\le m<\binom{r+1}k$ and noting $K_k(m)\ge\binom r{k+1}$. Hence only the finite ranges $C_k\le m<\binom{r_0}k$ need checking against (2). All computations use exact integer arithmetic.

### Degree five

Take $r_0=14$ for $k=1,2,3,4$; the comparison at $r_0$ is valid for each $k$ (strictly). The exceptional coefficient sets $E_k=\{m : (2)\text{ holds}\}$, where a KK violation is not excluded by Maclaurin alone, are

| $k$ | Exceptional $u_k$ values |
|---:|---|
| 1 | none |
| 2 | 11, 12, 13, 17, 18 |
| 3 | 12, 13, 14, 15, 17 |
| 4 | none |

Newton's inequalities are

$$2a^2\ge5b,\quad b^2\ge2ac,\quad c^2\ge2bd,\quad2d^2\ge5ce$$

for $F=1+at+bt^2+ct^3+dt^4+et^5$. Any possible KK violation has $b$ in $E_2$ or $c$ in $E_3$. Together with the lower bounds $a,d\ge5$, these inequalities imply the overinclusive finite ranges $10\le b\le28$ and $10\le c\le32$, with $b\in E_2$ or $c\in E_3$, and

$$5\le a\le\lfloor b^2/(2c)\rfloor,\quad 5\le d\le\lfloor c^2/(2b)\rfloor,\quad 1\le e\le\lfloor 2d^2/(5c)\rfloor,$$

also imposing $2a^2\ge5b$. Exhaustive exact enumeration produces 125 vectors, of which precisely six violate Kruskal–Katona.

| $(a,b,c,d,e)$ | Negative exact Hermite certificate |
|---|---|
| (6,12,12,6,1) | $\det H_3=-144$ |
| (6,13,14,6,1) | $\det H_4=-2846$ |
| (6,13,14,7,1) | $\det H_3=-20$ |
| (6,14,14,7,1) | $\det H_3=-196$ |
| (7,14,14,7,1) | $\det H_3=-784$ |
| (6,14,15,8,1) | $\det H_3=-53$ |

### Degree six

For $n=6$, the thresholds satisfying (3) are

| $k$ | $r_0$ | $\binom{r_0}k$ | Exact positive margin in (3) |
|---:|---:|---:|---:|
| 1 | 17 | 17 | 36 |
| 2 | 15 | 105 | 7,509,375 |
| 3 | 14 | 364 | 15,830,171,800,625 |
| 4 | 12 | 495 | 56,605,491,731,250,000 |
| 5 | 10 | 252 | 9,330,627,060,167,616 |

The finite exceptional values from (2) are

| $k$ | Exceptional $u_k$ values |
|---:|---|
| 1 | none |
| 2 | 16–19, 23–25 |
| 3 | 21–29, 31–33, 42–43 |
| 4 | 17–24, 27–30 |
| 5 | none |

With $F=1+at+bt^2+ct^3+dt^4+et^5+ft^6$, the degree-six Newton inequalities are

$$12b\le5a^2,\quad15ac\le8b^2,\quad16bd\le9c^2,\quad15ce\le8d^2,\quad12df\le5e^2.\tag{4}$$

If $b$ is exceptional then $b\le25$, yielding $c\le55$ and $d\le113$. If $c$ is exceptional then $c\le43$, yielding $b,d\le69$. If $d$ is exceptional then $d\le30$, yielding $c\le80$ and $b\le240$. Thus any possible counterexample lies within the **derived**, not arbitrary, integer box

$$15\le b\le240,\quad 20\le c\le80,\quad15\le d\le113,$$

with $b$, $c$ or $d$ exceptional, satisfying $16bd\le9c^2$, and

$$\max(6,\lceil\sqrt{12b/5}\rceil)\le a\le\lfloor8b^2/(15c)\rfloor,$$

$$6\le e\le\lfloor8d^2/(15c)\rfloor,\qquad1\le f\le\lfloor5e^2/(12d)\rfloor.$$

Exactly 4,445 vectors survive. Exactly 22 violate Kruskal–Katona; the full list and the exact negative Hermite determinant for each appear in [the degree-six supplemental note](../supplement/degree6-original-note.md) and in both verification scripts. These are not sampled cases; the bounding argument covers every candidate vector.

## 3. Moment-matrix obstruction

Define the polynomial in the reciprocal-root variables

$$Q(x)=x^n-u_1x^{n-1}+u_2x^{n-2}-\cdots+(-1)^nu_n=\prod_{j=1}^n(x-\lambda_j).$$

Let $p_s=\sum_{j=1}^n\lambda_j^s$ be its power sums ($p_0=n$), computed exactly from the coefficients by Newton identities. For $q=3,4$, define $H_q=(p_{i+j})_{0\le i,j<q}$. When all $\lambda_j$ are real,

$$H_q=\sum_{j=1}^n v_q(\lambda_j)v_q(\lambda_j)^\mathsf T,\quad v_q(x)=(1,x,\ldots,x^{q-1})^\mathsf T,$$

which is positive semidefinite. Hence $\det H_q\ge0$. Every one of the six (degree five) and 22 (degree six) remaining KK violations has an *explicitly negative* $H_3$ or $H_4$ determinant. Consequently none is real-rooted. Combined with the analytic bound and complete finite enumeration, this proves the candidate theorem **conditional only on correctness of the presented argument and computation**, which remain open to external audit.

## 4. Reproducibility, limitations, and attribution

- Standard-library certificates: [`verification/degree5_certificate.py`](../verification/degree5_certificate.py) and [`verification/degree6_certificate.py`](../verification/degree6_certificate.py).
- Independent checks: [`verification/degree5_independent.py`](../verification/degree5_independent.py) and [`verification/degree6_independent.py`](../verification/degree6_independent.py); these use explicit colex faces and companion-matrix traces, followed by SymPy exact real-root isolation.
- Four scripts were rerun on 10 October 2026, matching the reported counts and determinant witnesses.
- No external peer review has been performed. The fixed-degree cases may overlap earlier results not found during preliminary searches.
- **Disclosure:** The derivations, programs, and writing were AI-generated by OpenAI GPT-6 in an interaction guided by Michael Linde, who selected and steered the research problem. They should not be represented as independently human-proved results.

## References

1. J. Bell and M. Skandera, “Multicomplexes and polynomials with real zeros”, *Discrete Mathematics* 307 (2007), 668–682. https://www.lehigh.edu/~mas906/papers/logc.pdf
2. L. Mu and V. Welker, “On a question about real rooted polynomials and f-polynomials of simplicial complexes”, *Advances in Applied Mathematics* 175 (2026), 103041. https://arxiv.org/abs/2503.24076
3. F. Liu, Y. Wang and Z. Zhang, “Counterexamples to the Mu–Welker recursive decomposition in every degree”, arXiv:2609.23694. https://arxiv.org/abs/2609.23694
