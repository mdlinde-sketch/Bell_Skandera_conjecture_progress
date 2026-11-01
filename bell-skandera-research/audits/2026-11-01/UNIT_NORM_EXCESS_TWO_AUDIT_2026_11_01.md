# 1 November 2026 — sharp all-degree unit-norm trace-two classification

**UNREVIEWED research deduction, conditional on Smyth (1984).** Not an unrestricted Bell–Skandera proof; novelty, specialist review and formal verification are not claimed. No d18 extension.

## Theorem

If R(t) in Z[t] is monic with constant coefficient 1, all roots negative real, degree d, and [t]R=d+2, then R is **exactly one** of:

(A) (1+t)^(d-2) (1+4t+t²), d>=2;
(B) (1+t)^(d-3) (1+5t+6t²+t³), d>=3;
(C) (1+t)^(d-4) (1+3t+t²)², d>=4.

All three exist and have [t²]R equal to C(d,2)+2d-4 for (A) or C(d,2)+2d-3 for (B),(C). In particular

    [t²]R >= C(d,2)+2d-4.

For d>=3, D_(d-1)(d+2)=C(d,2)+2d-5, so the sharp lower bound exceeds the penultimate KK shadow by **one integer**. Reversing coefficients: for every monic constant-one F in Z[t] with all roots negative and a_(d-1)=d+2,

    a_(d-2) >= C(d,2)+2d-4 = D_(d-1)(d+2)+1.

This resolves the exact degree-28 partial-integrality obstruction of 31 October: a27=30 implies a26 must be **430 or 431** in any genuine integer polynomial, not 428. Its KK threshold is 429.

## Proof (factorwise Smyth, corrected exception orientation)

Factor R into monic irreducibles over Z. All factors have constant coefficient 1 (positive roots in the transformed variable), and leading coefficient 1. For each factor Q, the excess e=[t]Q-deg Q is a nonnegative integer by AM–GM and its unit norm. Excesses add to 2. An e=0 irreducible must be 1+t.

For a nonexceptional irreducible of degree r, Smyth's strict trace theorem gives 7719*r<10000*e. For e=1 this forces r=1; monic constant-one degree-one Q=1+t has e=0, so no nonexceptional e=1 factor exists. The only exceptional e=1 factor is 1+3t+t².

For e=2, the strict bound gives r<=2. Degree one again is impossible. The unique monic constant-one quadratic of trace 4 is 1+4t+t². The only exceptional e=2 factor is 1+5t+6t²+t³. The remaining Smyth quartic exceptions have e=3. Thus the partition of total excess 2 is either one e=2 factor or two e=1 factors, plus arbitrary 1+t factors. This yields precisely (A),(B),(C). All are negative-real-rooted; the cubic's reciprocal positive-root polynomial x³-5x²+6x-1 has discriminant 49 and no negative roots. Expand coefficients to finish.

**Correct Smyth exceptions** in F-orientation:
(1,1), (1,3,1), (1,5,6,1), (1,7,13,7,1), (1,7,14,8,1).

Smyth primary source: https://www.numdam.org/article/AIF_1984__34_3_1_0.pdf (1984). His paper already classified trace-minus-degree <=6; this specialized corollary is not claimed novel.

## Exact controls and scope

A standalone Python standard-library checker (same audit directory) verifies the three families for d=4..250, 741 exact cases, plus the d28 KK gap. These controls are supplementary, not a substitute for the Smyth factor theorem. An expanded proof, SHA256 manifest, source and JSON log are in the dated reproducible ZIP Bell_Skandera_2026-11-01_unit_norm_excess_two_audit.zip.

The unbounded-excess interior-index problem remains open. Do not claim unrestricted Bell–Skandera.
