# Proof skeleton and review obligations for the degree-17 candidate

**This is a structured proof candidate, NOT a verified theorem.** It is intended to make every reduction and possible hidden assumption explicit for an adversarial mathematical reviewer.

## Candidate finite-degree statement

For every integer 1 <= d <= 17, suppose F(t)=1+u_1 t+...+u_d t^d has strictly positive integer coefficients and all roots real. Then its coefficient sequence is the f-vector of some finite simplicial complex, equivalently u_(k+1) <= K_k(u_k) for all 1 <= k < d, where K_k is the canonical Kruskal–Katona shadow function. The assertion for d=1 is immediate.

## Proof strategy: strong induction on degree

1. All roots of F are strictly negative (positive coefficients and real-rootedness), so F(t)=prod_(i=1)^d (1+lambda_i t) with lambda_i>0. The monic integer polynomial P(x)=prod(x-lambda_i) has trace u_1 and norm N=u_d>=1.

2. Smyth's trace theorem (check exact primary-source hypotheses!) gives u_1 > (17719/10000)d unless P has an irreducible factor among x-1, x²-3x+1, x³-5x²+6x-1, x⁴-7x³+13x²-7x+1, x⁴-7x³+14x²-8x+1. Each corresponding factor of F has an f-polynomial coefficient vector [1,1], [1,3,1], [1,5,6,1], [1,7,13,7,1], [1,7,14,8,1], verified by KK. Gauss's lemma and constant term F(0)=1 give a factorization F=E G over integer-coefficient polynomials with constant 1, positive coefficients and strictly negative roots. If E is exceptional, by the induction hypothesis G is an f-polynomial, and F is the f-polynomial of the join of the complexes for E and G. Thus the no-exception case may assume u_1>(17719/10000)d.

3. If N=1, the reciprocal polynomial of P is again monic integer with strictly positive roots. The same Smyth theorem gives u_(d-1)>(17719/10000)d unless it contains an exceptional factor. In that case F has the reversed exceptional f-polynomial as a factor, and induction again applies. If N>=2, use the independently certified pointwise inequality 1/x+(3/2)log x-(3/4)log|x-1|>29/20 for x>0, x!=1. Summing over lambda_i and using |P(1)|>=1 yields u_(d-1)/N+(3/2)log N>(29/20)d unless P(1)=0, in which case F has factor (1+t). The exact sufficient integer inequalities for forcing P(1)=0 are 10 u_(d-1)+30<29d when N=2, and 20 u_(d-1)+180<87d when N=3. These follow from log2<1 and log3<2 respectively.

4. Suppose F has a KK violation at some k: write m=u_k, n=u_(k+1) >= K_k(m)+1. Newton–Maclaurin normalized log-concavity implies n^k C_k^(k+1)<=C_(k+1)^k m^(k+1) and u_j >= C_j=binom(d,j). The exact finite cutoff r(d,k), with strict inequality C(r,k+1)^k C_k^(k+1)>C_(k+1)^k C(r+1,k)^(k+1), proves that every violating m satisfies C_k<=m<C(r,k). For fixed m,n, the exact log-concavity caps for any j are

   - j<k: u_j <= floor(C_j m^(k+1-j) C_(k+1)^(k-j) / [C_k^(k+1-j) n^(k-j)]),
   - j>k+1: u_j <= floor(C_j n^(j-k) C_k^(j-k-1) / [C_(k+1)^(j-k) m^(j-k-1)]).

   These are necessary inequalities. No floating-point rounding is used.

5. The independently implemented Python and C++ interval-frontier classifiers partition every m in this finite range. Each interval [a,b] is either impossible because K_k(a)+1>nmax(b), reducible by original Smyth trace because upper_u1(b,K_k(a)+1)<=17719d/10000, or bisected down to singleton m and every admissible n enumerated. The monotonicity arguments rely only on K_k and nmax being nondecreasing, and upper_u1 increasing in m and decreasing in n. Both classifiers independently produce identical residual/special lists for every d<=17, including d17's 2,142 residual and 37 special pairs.

6. For N=1, if u_(d-1) upper cap is below Smyth's threshold, reverse-exception factor induction applies. Otherwise only the residual/special pairs remain. The finite classification for d17 shows all such pairs occur at k in {d-4,d-3,d-2}; consequently q1..q4 of the monic reciprocal polynomial Q(t)=t^d F(1/t) are bounded by exact integer Maclaurin chord/local/tangent inequalities, with the fixed adjacent coefficients inserted. For each admissible q1..q4 prefix, the positive-root Hankel determinants H2,H3,H4 must be nonnegative. Where H3>=0, H4 is nonincreasing in q6, and where H2>=0 it is a concave quadratic in q5. The exact lower chord q6>=L6(q5)>=L6(L5) gives an explicit concave-quadratic upper bound over each entire q5 interval. Both independently written determinant verifiers certify all 578,295 d17 interval maxima are strictly negative. Hence no norm-one violating F survives.

7. For N=2, the remaining special pairs all have k=d-2. The scaled reciprocal roots 2/lambda_i have integer elementary symmetric functions e_j=2^(j-1)u_(d-j). Their 3×3 moment Hankel determinant must be nonnegative. Exact Maclaurin chord/local/tangent bounds cover every possible original u_(d-3),u_(d-4); the independent 3×3 determinant audit certifies H3<0 for every allowed prefix in all 37 d17 special pairs. All other N=2 cases are eliminated by the sufficient inverse-trace factor condition. For N=3, all 37 special pairs have upper_u_(d-1)<=57, giving 20*57+180<87*17; the inverse-trace factor condition applies. The d17 frontier bounds N<=3. Thus every putative KK violation is either impossible or reducible to a lower-degree f-polynomial, contradicting minimality.

8. Repeat the same certificate for all lower degrees 2..16 (archived 17 October), completing the proposed induction through d=17.

## What could still be wrong?

- The exact Smyth theorem may have subtle restrictions (irreducibility, algebraic integer conventions, exception list, strictness). Check the original 1984 paper, not only a secondary summary.
- The machine certificate is exact arithmetic but not a formalized proof assistant derivation; its code and all interval completeness conditions require independent review.
- The Python/C++ classifiers use separate implementations but share the same mathematical interval-cover lemma. Exact agreement is a strong test of implementation bugs, not proof that the lemma is valid.
- A reader must verify the scaled reciprocal N=2 coefficient bounds, the Hankel PSD requirements including repeated roots, and the correctness of the H4 concavity bound.
- The exceptional-factor induction requires careful application of Gauss's lemma and proof that each factor has positive coefficients after normalization; the join construction must be stated explicitly.
- This proof is finite-degree only. The current certificate has not established a general-degree result or originality.

**Conclusion:** The d<=17 computation is now independently reproduced across two languages, with direct determinant cross-checks. The correct next step is formal mathematical review of this skeleton and the executable certificate, not a public proof claim.
