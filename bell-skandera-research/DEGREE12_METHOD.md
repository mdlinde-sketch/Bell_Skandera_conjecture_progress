# Degree-12 continuation: exact shifted-moment pruning

12 October 2026. AI-generated, unreviewed research. This is not a proof of degree 12 and makes no novelty claim.

## Correct starting point

The shared research log at https://chatgpt.com/share/6accb4a5-2d88-83ec-bf9d-05544e8303f2 reports complete candidate searches through degree 11, and partial degree-12 searches. Its degree-11 package link was visible but did not open or expose downloadable content in the shared page. Those earlier programs and their saved state were not recovered. Earlier reported results must not be confused with newly reproduced computations.

The newly reconstructed finite-bound generator reproduces the reported degree-11 total of 34,948 violating adjacent pairs exactly. For degree 12 it produces 120,676 pairs, with 11,045 at index 8 and 2,504 at index 9, matching the detailed log. No earlier-degree exhaustive search was needed for this reconstruction.

## Finite domain

Write F(t)=sum(u_j t^j)=product(1+lambda_i t), with u_0=1, positive integer coefficients, and twelve positive lambda_i. Put C_j=binom(12,j). Maclaurin gives u_j>=C_j and

    u_(k+1)^k C_k^(k+1) <= C_(k+1)^k u_k^(k+1).

Let K_k(m) be the Kruskal–Katona maximum, computed from the canonical k-binomial expansion. A violation at k requires n>=K_k(m)+1 and the displayed inequality for m=u_k, n=u_(k+1).

As in the earlier manuscript, R_k(x)=binom(x,k+1)^k/binom(x+1,k)^(k+1) is strictly increasing for x>k. A direct way to justify the average comparison in its logarithmic derivative is to couple the two uniform index distributions with t in [0,1): floor((k+1)t) is strictly greater than floor(kt)-1. Since 1/(x-j) is strictly increasing in j, the derivative is positive.

The exact thresholds r_k in the table below satisfy

    binom(r_k,k+1)^k C_k^(k+1) > C_(k+1)^k binom(r_k+1,k)^(k+1).

For m>=binom(r_k,k), monotonicity, the leading binomial term of K_k(m), and Maclaurin rule out any violation. All smaller m are tested using integers.

The normalized sequence v_j=u_j/C_j is log-concave, with v_0=1 and v_12>=1. Fixing an exceptional index k with maximum M bounds every coefficient:

    u_j <= C_j (M/C_k)^((12-j)/(12-k))  for j<k;
    u_j <= C_j (M/C_k)^(j/k)            for j>=k.

The code computes these caps by exact integer roots, then uses the adjacent Newton inequalities to restrict enumeration further. Bounds are derived, not arbitrary numeric cutoffs.

| k | r_k | Exceptional values | Violating pairs |
|---:|---:|---:|---:|
| 1 | 35 | 0 | 0 |
| 2 | 33 | 48 | 393 |
| 3 | 32 | 186 | 3,364 |
| 4 | 30 | 436 | 13,291 |
| 5 | 29 | 809 | 30,203 |
| 6 | 27 | 1,023 | 34,464 |
| 7 | 25 | 773 | 25,171 |
| 8 | 23 | 642 | 11,045 |
| 9 | 21 | 359 | 2,504 |
| 10 | 19 | 121 | 241 |
| 11 | 17 | 0 | 0 |

## Additional necessary moment constraints

Let p_s=sum(lambda_i^s), so p_0=12. In addition to the ordinary moment matrix H_q=(p_(a+b)), the shifted matrix S_q=(p_(a+b+1)) is positive semidefinite: for any real vector z,

    z^T S_q z = sum_i lambda_i (sum_a z_a lambda_i^a)^2 >= 0.

Consequently every leading determinant of either matrix is nonnegative. This uses positivity of the roots lambda_i, not merely their reality.

Suppose u_1,...,u_(j-1) are fixed. For even j use H_(j/2+1); for odd j use S_((j+1)/2). The highest moment p_j occurs only in the bottom-right matrix entry. Newton's identities make it affine in u_j, while all earlier moments are independent of u_j. Thus the selected determinant is exactly B+A*u_j, including singular cases.

The implementation obtains B and A by evaluating the determinant at u_j=0 and 1. This is coefficient interpolation of an affine identity; those artificial values need not themselves describe real-rooted polynomials. Nonnegativity implies an integer lower bound ceil(-B/A) when A>0, an upper bound floor(B/(-A)) when A<0, rejection when A=0 and B<0, and no added restriction otherwise. The implementation uses exact signed integer division and never divides by a presumed nonzero principal minor.

Only necessary conditions are used for rejection. Nonnegative leading determinants alone are not asserted to establish real-rootedness or positive semidefiniteness in singular cases. A surviving vector would require further investigation. Zero survivors after complete exhaustive enumeration is the relevant exclusion result.

## Validation and limits

`check_affine_bounds.py` performs 7,200 exact comparisons using a separate rational Gaussian determinant implementation, arbitrary coefficient inputs, signed rounding checks, and positive integer root controls with repeated roots allowed. These checks validate arithmetic identities and controls, not the completeness of the full search. The infinite reduction and exhaustive enumeration remain subject to independent review.

The newly written program has completely exhausted indices 2, 3 and 4 with zero survivors. It is distinct from the unavailable earlier compiled program and does not import that program's completion claims. Degree 12 is still incomplete.

## Reproduction and resumption

Use Python 3, standard library only, from this directory:

    python degree12_frontier.py
    python check_affine_bounds.py
    python degree12_search.py 5 60
    python degree12_search.py 6 60

The last argument is a run-time allowance in seconds. The search saves completed adjacent pairs after each pair. If interrupted within a pair, that pair is retried rather than marked complete. Checkpoint files are local to this new implementation and its pair ordering. Do not import the reported 7,900-pair progress from the older run without recovering and comparing its actual saved pair list. Avoid concurrently running two searches for the same index.

`degree12_frontier.json` contains every pair and exact cap. `degree12_k*_checkpoint.json` records locally completed work. Keep these files with the scripts. The older `explore.py` and degree-8 files are retained for provenance but are not the frontier to resume.
