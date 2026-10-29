# Bell–Skandera: corrected small-excess proof and all-order structural audit

29 October 2026, Brisbane. Base repository commit: `f5733cd0451381ac00de1300e17c414688070444`.

## Status

**A concrete error was found and repaired. The unrestricted conjecture is not proved.**
The five-exception list in the latest small-excess note has two polynomials reversed.
With the correct list, the all-degree excess-at-most-three result has an analytic
proof, and the excess-at-most-six result has a fully specified finite arithmetic
proof certificate reproduced independently here. These are research proofs subject
to independent mathematical review, not externally refereed or formally verified results.
No degree-by-degree extension was performed. The existing daily task was not modified.

The other results below are an all-order determinant identity with a conditional
exclusion criterion, and a proof that exception stripping leaves genuinely
unbounded irreducible cores. Neither is an unrestricted Bell–Skandera theorem.

## 1. The exception error and two exact counterexamples to the old reduction

For `F(t)=sum a_j t^j`, the polynomial relevant to trace is

    P(x)=x^d F(-1/x)=x^d-a_1 x^(d-1)+...+(-1)^d a_d.

Smyth's original theorem, printed page 2, lists the monic exceptions

    x-1; x^2-3x+1; x^3-5x^2+6x-1;
    x^4-7x^3+13x^2-7x+1; x^4-7x^3+14x^2-8x+1.

Thus the constant-one exceptions are

    1+t; 1+3t+t^2; 1+5t+6t^2+t^3;
    1+7t+13t^2+7t^3+t^4; 1+7t+14t^2+8t^3+t^4.

Source: [Smyth, 1984, printed p. 2](https://www.numdam.org/article/AIF_1984__34_3_1_0.pdf).
The displayed Theorem 4.10 in the [Bell–Skandera manuscript](https://www.lehigh.edu/~mas906/papers/logc.pdf)
instead reverses the cubic and last quartic. The research note inherited that
orientation. This is a mathematical discrepancy, not just an OCR concern:

* `F=1+5t+6t^2+t^3` has d=3, s=2, but `5 < 1.7719*3`.
* `F=1+7t+14t^2+8t^3+t^4` has d=4, s=3, but `7 < 1.7719*4`.

Both are irreducible, real-negative-rooted integer polynomials, and neither is in
the old exception list. Their corresponding positive-root polynomials reduce
modulo 2 to `x^3+x^2+1` and `x^4+x^3+1`. The cubic has no root in F_2; the quartic
has no root and is not divisible by the sole monic irreducible quadratic
`x^2+x+1`. Hence both are irreducible over Q. Exact rational Sturm chains in
`audit_exact.py` verify respectively three and four positive roots of P.

Removing the old listed exceptions leaves these polynomials untouched. The claimed
bound `g < 10000*s/7719` would give respectively `g<2.5911` and `g<3.8866`, which
is false. This refutes the reduction **as written**, not its repaired conclusion
and not Bell–Skandera. Downward KK checks verify both corrected exceptions.

The reversed versions are themselves valid face polynomials, so checking their
KK inequalities did not detect the missing cases. This explains why the old
arithmetic script passes despite the theorem-input error.

## 2. Repaired infinite-to-finite reduction

Assume F has constant 1, integer nonnegative coefficients, degree d and only real
zeros. Its zeros are strictly negative. Write `F=prod(1+lambda_i t)`, lambda_i>0.
The norm `prod lambda_i=a_d` is a positive integer. Maclaurin therefore gives
`a_k >= C(d,k)` and `a_1>=d`.

Factor the monic P into monic irreducibles in Z[x]. Each factor has positive
roots. Transforming each back gives integer constant-one factors Q of F, with
positive coefficients. Each factor has nonnegative integer excess
`s(Q)=[t]Q-deg Q`, by AM–GM and its positive integer norm. Degrees and excesses
add. Products of simplicial face polynomials are realized by joins on disjoint
vertex sets.

Extract all factors in the **corrected** exception list, with multiplicity.
Their KK inequalities are checked exactly. Every remaining irreducible factor
has trace greater than `17719/10000` times its degree by Smyth's theorem.
Summing this strict inequality, if the remaining G is nonconstant, gives

    7719 deg G < 10000 s(G) <= 10000 s(F).

No irreducibility assumption on G is needed. If s=0, G=1. The old multiplicity
bound also survives: every irreducible factor other than 1+t has excess at least
half its degree, so `(1+t)^max(0,d-2s)` divides F. Equality in the latter degree
bound for the non-(1+t) part forces that part to be a power of `1+3t+t^2`.

This is a reduction for every finite s, but its bound grows with s. Quantifying
over all finite s does not turn any one finite run into a proof for unbounded s.

## 3. Analytic proof for s <= 3

The repaired bound gives `deg G<=3`. Here is a complete low-degree argument.
For every d, n=a_1>=d and Newton gives

    a_2 <= (d-1)n^2/(2d) <= n(n-1)/2.

This proves the first KK inequality and settles degrees at most two. In degree
three put m=a_2>=3. Maclaurin gives `27 a_3^2<=m^3`.
Write `C(r,2)<=m<C(r+1,2)`. Upward KK is

    K_2(m)=C(r,3)+C(m-C(r,2),2).

For m=3,...,14 the respective integer upper bounds for a_3 are
`1,1,2,2,3,4,5,6,7,8,9,10`; direct downward shadows in the saved results verify
each. For r>=6,

    C(r,3) >= (C(r+1,2)/3)^(3/2),

since after squaring and cancelling positive factors this is
`6(r-1)^2(r-2)^2-r(r+1)^3>=0`. Setting r=x+6 gives
`5x^4+81x^3+453x^2+935x+342>0` for x>=0. Thus a_3<=K_2(m).
All extracted factors and G are face polynomials, so their join realizes F.

**Conclusion:** subject to the cited trace theorem and standard KK/Newton results,
the analytic s<=3 theorem survives the exception correction.

## 4. Independent exact certificate for s <= 6

Now deg G<=7. Degrees at most three are handled above. If g>=4 and n=[t]G, then

    floor(17719g/10000)+1 <= n <= g+6.

The nine (g,n) pairs are (4,8),(4,9),(4,10),(5,9),(5,10),(5,11),
(6,11),(6,12),(7,13). No preceding degree-17 certificates are needed.

For each prefix, all actual coefficients are included by the lower bounds C(g,k)
and the upper bound

    U_k=min(floor(C(g,k)n^k/g^k),
            floor(a_(k-1)^2 (k-1)(g-k+1)/(a_(k-2) k(g-k+2)))).

All divisions here have positive denominators. No floating point is used.
Enumerate a_2,a_3,a_4 under these bounds. Newton sums p_0=g,p_1,...,p_4 determine
the 3 by 3 matrix `(p_(i+j))`. For actual positive roots it is a Gram matrix:
`sum_i (1,lambda_i,lambda_i^2)^T(1,lambda_i,lambda_i^2)`. Thus a negative
determinant rejects a prefix soundly. A nonnegative determinant is not treated
as sufficient for real-rootedness; all such prefixes are retained.

The independent checker uses the **downward** operator D_k(m), formed by replacing
each C(r,j) in the k-binomial expansion by C(r,j-1). KK requires
`D_k(a_k)<=a_(k-1)`. This implementation is independently checked against actual
colex-set shadows for 246 examples.

On every retained prefix it checks D_3(a_3)<=a_2 and D_4(a_4)<=a_3.
For g>=5 it checks D_5(U_5)<=a_4 whenever the a_5 range is nonempty; monotonicity
of D_5 covers the whole range. For g=7 it checks **every** possible a_5 and
D_6(U_6)<=a_5 whenever the a_6 range is nonempty. This is broader than the old
checker's Maclaurin-prefiltered list of a_5 suspects.

The terminal pair is independently handled for each integer
`1<=m=a_g<=floor(n^g/g^g)`. Maclaurin implies
`a_(g-1)>=g*m^((g-1)/g)`. The exact test

    (D_g(m)-1)^g < g^g m^(g-1)

ensures that every integer a_(g-1) allowed by this lower bound is at least D_g(m).
This check handles the terminal pairs, including g=6 and g=7, without
enumerating completions. It is checked only in the stated finite ranges, not
assumed universally.

| g | n | a_2,a_3,a_4 prefixes | retained after H3 | all a_5 checks |
|---:|---:|---:|---:|---:|
|4|8|684|284|0|
|4|9|1,835|851|0|
|4|10|4,756|2,254|0|
|5|9|3,763|1,715|0|
|5|10|11,922|5,106|0|
|5|11|28,256|13,159|0|
|6|11|39,421|18,102|0|
|6|12|101,295|44,154|0|
|7|13|254,745|116,823|5,336,636|

All checks pass. The original standalone checker was also run unchanged and
passed all nine rows. Its arithmetic was sound on those rows; its exception
input was incomplete. The new script imports no old verification code.

**Conclusion:** the corrected reduction plus the analytic lemma and finite
certificate establish the s<=6 result at the level of a reproducible computational
research proof. External review of the argument and implementation remains outstanding.

## 5. All-order Hankel corner identity (proved algebraically)

Fix r>=2. For formal elementary coefficients q_0=1,q_1,...,q_(2r), let p_j be
their Newton sums, p_0=d. Write

    H_j=det((p_(a+b))_(0<=a,b<j)),
    M=(p_(a+b))_(0<=a,b<r), v=(p_r,...,p_(2r-1))^T.

Fix q_1,...,q_(2r-2), and let q_(2r-1)=z+t, q_(2r)=w+u. A subscript 0 means
evaluation at (z,w). Then, with no invertibility assumption,

    H_(r+1)(z+t,w+u)
      = H_(r+1)(z,w) + A t -(2r-1)^2 H_(r-1)t^2 -2r H_r u,

    A=2r q_1 H_r-2(2r-1) e_last^T adj(M) v_0.

Proof: the bordered determinant identity is
`H_(r+1)=p_(2r)det M-v^T adj(M)v`, a polynomial identity even when M is singular.
Newton's identities show that p_(2r-1) changes by (2r-1)t and p_(2r) changes by
2r q_1 t-2r u; all entries of M stay fixed. Finally
`adj(M)_(last,last)=H_(r-1)`. Expanding proves the formula.

For positive roots, H_(r-1),H_r>=0. Therefore a negative corner and A<=0 exclude
the **entire** quadrant t,u>=0. More generally, if an independently justified
affine lower bound gives u>=c t, c>=0, substitute u=c t+v with v>=0: the same
criterion holds with slope A-2r c H_r. This is a conditional exclusion theorem
at every order, for arbitrary degree and excess. It does not prove that the
required signs hold on every hypothetical KK-violating prefix.

The old H4 formula is precisely r=3. Exact controls in `hankel_all_orders.py`
cover 378 cases at orders r=2,...,7, including singular positive-root blocks.
The proof is the symbolic derivation, not the finite control set.

## 6. Why a fixed exception list cannot bound the remaining core

For every odd prime p=2d+1 define

    F_p(t)=sum_(j=0)^d C(2d-j,j)t^j.

These are the matching-generating polynomials of the path on 2d vertices:
choosing j nonadjacent edges gives C(2d-j,j) matchings. Hence each is already
the face polynomial of a matching complex. This construction is not a
counterexample to Bell–Skandera.

The recurrence for path matchings is `R_N=R_(N-1)+t R_(N-2)`, R_0=R_1=1.
Equivalently, `x^N R_N(-1/x^2)` is the characteristic polynomial of the path
adjacency matrix. Its roots are `2 cos(k*pi/(N+1))`, as follows by substituting
the sine eigenvectors into the three-term recurrence. Pairing opposite roots
when N=2d gives

    F_p(t)=prod_(k=1)^d (1+4 cos^2(k*pi/p)t).

All reciprocal-root parameters are positive, and are the conjugates of
`2+zeta_p+zeta_p^(-1)`. This number generates the real cyclotomic subfield:
subtracting 2 gives zeta_p+zeta_p^(-1), and zeta_p satisfies a quadratic over
that real field. Since zeta_p is nonreal, the extension has degree exactly 2;
the real degree is (p-1)/2=d. Thus P=x^d F_p(-1/x), and hence F_p, is irreducible.

The coefficient formula gives a_d=1, a_1=2d-1, and **s=d-1**, which is unbounded
as p ranges over primes. For p>=11 these polynomials lie outside all five
Smyth exceptions. After removing any fixed finite collection of irreducible
factors, infinitely many of these cores remain intact. Consequently no
degree bound independent of s can follow from such exception stripping alone.

This does not preclude a different unrestricted proof. It identifies the
missing step: control of irreducibles of unbounded degree/excess using global
integrality and KK information, rather than another finite exception audit.

## 7. Scope of unbounded-excess consequences and unresolved candidates

The corrected s<=6 theorem immediately extends to any product of factors each
having excess at most six, without a bound on the number of factors. Vertex
cloning also realizes Q(mt) for any positive integer m whenever Q is a face
polynomial: replace every vertex by m alternatives, using at most one clone
of each original vertex per face. Joins of these cloned factors therefore
allow unbounded degree and total excess. These are restricted sufficient
conditions, not the unrestricted theorem requested; no novelty is asserted.

One scalar candidate examined during this session is
`(D_d(m)-1)^d < d^d m^(d-1)` for all d>=2,m>=1. It would settle every terminal
KK inequality by AM–GM. Exact tests for 2<=d<=80 and 1<=m<=500 found no failure.
**No proof is supplied**, and this candidate is not used outside the finite
ranges certified in Section 4. This was a test of a uniform scalar inequality,
not an expansion of finite-degree Bell–Skandera claims.

The current [Mu–Welker manuscript](https://arxiv.org/html/2503.24076v2) supplies
a sufficient rounded binomial-index criterion; it does not assert the full
conjecture. The [Liu–Wang–Zhang preprint](https://arxiv.org/html/2609.23694v1)
refutes a proposed recursive real-rootedness mechanism, using polynomials which
are themselves face polynomials. It is not a counterexample to Bell–Skandera.
Neither result fills the unbounded irreducible-core gap here.

The older d<=17 computations were not fully rerun in this session. The exception
orientation must be audited wherever trace induction is used. An earlier
exception-and-reversal join audit can supply witnesses for both orientations,
but that alone does not prove every trace-reduction branch used the right list.
The 29 October H4 identity itself is unaffected.

## Reproduction

Python 3 standard library, no network, no external packages, no old certificates:

```text
python audit_exact.py > audit_results.json
python hankel_all_orders.py > hankel_results.json
python structural_controls.py > structural_results.json
```

Saved outputs record exact counts. `structural_controls.py` records finite
controls for the prime family and the explicitly unproved scalar candidate.
The scripts use assertions: run normally, without Python's -O option.
Proof obligations are separated above from implementation checks and exploratory
evidence. No claim of unrestricted correctness, novelty, or peer review is made.
