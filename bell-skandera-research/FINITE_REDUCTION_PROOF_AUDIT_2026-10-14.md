# Degree-12 Bell–Skandera: independent analytic audit of finite cutoff and coefficient caps
14 October 2026 (evening), Brisbane. This note proves two necessary reductions used by the search, *conditional on* the stated positive-real-rooted hypothesis. It does not certify degree 12, exhaustive code correctness, or mathematical novelty.

## Definitions
Let \(F(t)=\prod_{i=1}^d(1+\lambda_i t)=\sum_{j=0}^d u_jt^j\), with \(\lambda_i>0\), \(u_j\) positive integers and \(u_0=1\). Set \(C_j=\binom{d}{j}\). Newton/Maclaurin imply that \(v_j=u_j/C_j\) is log-concave:
\[
v_j^2\ge v_{j-1}v_{j+1},\qquad v_0=1,\quad v_d=u_d\ge1.
\]
Let \(K_k(m)\) be the Kruskal–Katona *maximum possible next face count* for \(m\) k-faces. A violation at adjacent indices \(k,k+1\) requires \(u_{k+1}\ge K_k(u_k)+1\).

## Lemma 1: rigorous finite cutoff
Fix \(1\le k<d\). Define
\[
R_k(x)=\frac{\binom{x}{k+1}^{k}}{\binom{x+1}{k}^{k+1}},\qquad x>k.
\]
Then \(R_k\) is strictly increasing. Indeed,
\[
\frac{d}{dx}\log R_k(x)
 = k\sum_{j=0}^{k}\frac1{x-j}
 -(k+1)\sum_{j=-1}^{k-2}\frac1{x-j}.
\]
The first sum has \(k+1\) terms and the second has \(k\). If \(U\) is uniform on \([0,1)\), couple the uniform indices as \(J=\lfloor(k+1)U\rfloor\) and \(L=\lfloor kU\rfloor-1\). Then \(J>L\) pointwise, and \(1/(x-j)\) strictly increases with \(j\), giving a strictly positive derivative.

Suppose an integer threshold \(r>k\) satisfies
\[
\binom{r}{k+1}^k C_k^{k+1}
> C_{k+1}^k\binom{r+1}{k}^{k+1}.
\]
Monotonicity gives the same inequality at every integer \(a\ge r\). For any \(m=u_k\ge\binom{r}{k}\), choose the unique integer \(a\ge r\) with
\[
\binom{a}{k}\le m<\binom{a+1}{k}.
\]
Monotonicity of \(K_k\) and its exact value on binomial numbers show \(K_k(m)\ge K_k(\binom{a}{k})=\binom{a}{k+1}\).
Maclaurin gives
\[
u_{k+1}^{k}C_k^{k+1}\le C_{k+1}^{k}m^{k+1}
< C_{k+1}^{k}\binom{a+1}{k}^{k+1}
< C_k^{k+1}\binom{a}{k+1}^{k}.
\]
Hence \(u_{k+1}<\binom{a}{k+1}\le K_k(m)\). No Kruskal–Katona violation is possible for such \(m\).

As \(R_k(x)\) tends to \((k!)^{k+1}/((k+1)!)^k\), existence of a threshold for each relevant \(d,k\) is confirmed by the exact integer inequalities used in the generator, not by floating-point asymptotics. Consequently any violation has \(C_k\le u_k<\binom{r}{k}\), and the finite adjacent-pair frontier can be enumerated using exact integers.

## Lemma 2: exact finite coefficient caps
Let \(f_j=\log v_j\). Discrete log-concavity implies concavity of the piecewise-linear interpolation through \((j,f_j)\). Since \(f_0=0\) and \(f_d\ge0\), we first obtain \(f_j\ge0\), i.e. \(u_j\ge C_j\).

Fix any \(k<d\) with \(u_k\le M\) and \(M\ge C_k\). For \(j<k\), concavity at the intermediate point \(k\in[j,d]\) gives
\[
f_k\ge\frac{d-k}{d-j}f_j+\frac{k-j}{d-j}f_d
\ge\frac{d-k}{d-j}f_j,
\]
hence \(u_j\le C_j(M/C_k)^{(d-j)/(d-k)}\). For \(j\ge k\), concavity at \(k\in[0,j]\) gives \(f_k\ge (k/j)f_j\), hence \(u_j\le C_j(M/C_k)^{j/k}\).

The implementation takes the exact floor of these expressions using integer powers and integer roots. No arbitrary coefficient cutoff is needed.

## What this proves and what it does not
The analytic finite cutoff and caps are justified by Newton/Maclaurin and Kruskal–Katona, so **every hypothetical positive-real-rooted counterexample must be among the generated finite adjacent coefficient pairs and within these coefficient caps**, provided the recorded \(r_k\) inequalities and code arithmetic are independently verified. This says **nothing** about whether the subsequent recursive search completely and correctly enumerates all coefficient vectors inside the caps. All PSD moment pruning must also be independently audited.

The 14 October evening search recorded zero new survivors at k5 and k6 but is **not** a finished degree-12 proof. The reduction is elementary enough that no priority/novelty claim is made; Mu–Welker (Advances in Applied Mathematics 175, 2026, 103041) gives the contemporary background.
