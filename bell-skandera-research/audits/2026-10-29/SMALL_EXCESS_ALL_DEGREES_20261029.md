# All-degree small-excess reduction (29 October 2026)

**UNREVIEWED RESEARCH NOTE.** Not a proof of unrestricted Bell–Skandera; no claim of novelty or external endorsement.

For an integer real-negative-rooted polynomial F(t)=1+a1*t+...+ad*t^d, put s=a1-d>=0. Factor F into irreducible integer constant-one factors. For each irreducible Q, Smyth's 1984 theorem gives [t]Q > (17719/10000) deg(Q) unless Q belongs to five explicit exceptional polynomials (1+t, 1+3t+t^2, 1+6t+5t^2+t^3, 1+7t+13t^2+7t^3+t^4, 1+8t+14t^2+7t^3+t^4). All five satisfy Kruskal–Katona (KK), and simplicial joins multiply f-polynomials.

Every non-(1+t) factor has excess at least half its degree, therefore (1+t)^max(0,d-2s) divides F. After removing *all* Smyth exceptional factors, remaining G has degree g < 10000*s/7719 (unless G=1). Excess is additive and nonnegative on all factors.

**Analytic all-degree restricted theorem:** For s<=3, g<=3. Every degree<=3 real-negative-rooted polynomial with positive integer coefficients satisfies KK. At d=3, write m=a2>=3. Maclaurin gives a3<=(m/3)^(3/2). Write C(r,2)<=m<C(r+1,2). KK2(m)=C(r,3)+C(m-C(r,2),2). For r=3,4,5 check m=3..14. For r>=6, C(r,3)>=(C(r+1,2)/3)^(3/2), because 6(r-1)^2(r-2)^2-r(r+1)^3 at r=x+6 is 5x^4+81x^3+453x^2+935x+342>0. KK1 follows from Newton and a1>=d. Thus all degrees with s<=3 satisfy Bell–Skandera, conditional only on Smyth's published theorem.

**Exact-arithmetic candidate through s<=6:** The same reduction gives g<=7. For g=4..7 the nonexceptional trace n must satisfy floor(17719g/10000)+1<=n<=g+6. Enumerate all integer coefficient prefixes with Maclaurin bounds C(g,k)<=a_k<=floor(C(g,k)(n/g)^k) and Newton bounds a_k<=floor(a_(k-1)^2*C(g,k-2)*C(g,k)/(a_(k-2)*C(g,k-1)^2)). For g=4,5, all admissible vectors satisfy KK directly. For g=6,7 enumerate a2,a3,a4, reject negative H3 (3x3 reciprocal-root power-sum Hankel determinant), then check KK2,KK3, and all possible a5,a6 KK violations using exact Newton bounds; the terminal inequality follows from global Maclaurin. All cases passed in a separate standard-library checker; no previous d<=17 witnesses were used. For g=4 allowed n=8,9,10; g=5 n=9,10,11; g=6 n=11,12; g=7 n=13. No complete or unrestricted theorem is asserted without review.

Smyth's **original 1984 primary source itself enumerates all irreducible totally positive algebraic integers with excess <=6** (see its appendix), offering an independent route to audit this corollary: https://www.numdam.org/article/AIF_1984__34_3_1_0.pdf . Bell–Skandera paper's statement of the five-exception theorem: https://www.lehigh.edu/~mas906/papers/logc.pdf .

Earlier conversational slip corrected: product(lambda_i)>=1 does NOT imply sum(1/lambda_i)>=d. This false inference is not used.

Next task: independent proof audit of all cases and find a structural reduction valid for arbitrarily large s. No degree-18 brute-force expansion.