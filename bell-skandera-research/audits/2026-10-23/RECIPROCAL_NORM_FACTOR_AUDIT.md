# 23 October 2026 — arbitrary-norm reciprocal trace/factor audit

**UNREVIEWED finite-degree Bell–Skandera candidate through d=17. This note is a conditional structural lemma, NOT an all-degree proof or established novelty.**

Let F(t)=∏(1+λ_i t)=Σ u_j t^j∈Z[t], with λ_i>0, u_0=1, N=u_d=∏λ_i≥1. Define B_N(x)=∏(x−N/λ_i). For 1≤j≤d its elementary symmetric coefficients are e_j(N/λ)=N^{j−1}u_{d−j}. Thus B_N is a monic integer polynomial with all roots strictly positive, and trace u_{d−1} **for every integer N**, not only N=1.

Apply Smyth's 1984 totally-positive trace theorem: either u_{d−1}>1.7719d or B_N has an irreducible factor E among the five explicit exceptional unit-norm polynomials. Suppose E has degree e and roots β_i. Since ∏β_i=1, the corresponding λ_i=N/β_i have product N^e. The polynomial G_E(t)=∏(1+(N/β_i)t) belongs to Z[t], has constant 1 and leading coefficient N^e, and divides F in Q[t]. Its quotient H=F/G_E lies in Z[t] by Gauss's lemma (or recursive division using constant 1), with positive integer leading coefficient N/N^e=N^{1−e}. If N>1 this forces e=1. The only degree-one Smyth exception is x−1, hence λ=N and **(1+Nt) divides F**. Its factor 1+Nt is the f-polynomial of N isolated vertices, so the usual join induction applies.

**Conditional all-degree corollary:** If N>1, then either u_{d−1}>1.7719d or (1+Nt)|F. For N=1, the earlier reciprocal-exception factor induction remains valid. This strengthens a structural reduction but does not remove d17's norm-two special cases (u_{d−1} upper caps 51–57, while 1.7719·17≈30.12).

Exact independent tests: 49,200 divisibility comparisons on integer-root products through degree 8, including 72/72 nonunit exception hits exclusively x−1; 15 additional direct unit-norm exception-factor controls; 40 constructive vertex-cloning f-polynomial tests (10 exception/reverse witnesses × N=1,2,3,4). Cloning every vertex into N choices yields f_{Δ[N]}(t)=f_Δ(Nt).

23 October repeated frontier checker: 7,596 disjoint leaves, 969,827 (m,n) pairs, 2,142 residual and 37 special cases; hashes match the 18–22 October records. A separate Bareiss rerun completed: 6,573,665 q4 values, 578,295 strictly-negative H4 intervals excluding 193,610,278 q5 values; zero survivors; largest H4 upper bound −328,673,910,854. The full local archive contains exact programs and execution logs.

**Remaining:** independently scrutinize Smyth's hypotheses and reducible-factor application, norm and integrality argument, exact frontier/Hankel coverage and all-degree originality. No degree-18 claim. Full reproducible archive: Bell_Skandera_2026-10-23_reciprocal_norm_factor_audit.zip (not necessarily present in GitHub).

Primary reference: C. J. Smyth, *Totally positive algebraic integers of small trace*, Ann. Inst. Fourier 34 (1984), 1–28, DOI 10.5802/aif.975.
