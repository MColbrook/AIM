# AIM 935: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/935-the-numerical-index-of-real-lebesgue-spaces.md) · [PDF manuscript](../../solutions/935-real-lebesgue-numerical-index/aim935.pdf) · [source and reproduction](../../solutions/935-real-lebesgue-numerical-index/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## Independent review: AIM 935

Reviewed 2026-11-03 at base commit 5d7e26e8444eb98de91988454564e45e011107c4.

**Verdict: PASS — full negative resolution for every $`1<p<\infty,\ p\ne2`$.** No substantive gap was found in the general perturbation argument, either p=4 proof, or the interval corollary. The result disproves the proposed formula; it does not compute the numerical index itself.

Sources: [935.tex](../../solutions/935-real-lebesgue-numerical-index/SOURCE_RECEIPT.json), [935_general.tex](../../solutions/935-real-lebesgue-numerical-index/SOURCE_RECEIPT.json), [935_clean.tex](../../solutions/935-real-lebesgue-numerical-index/SOURCE_RECEIPT.json), [935_robustness.tex](../../solutions/935-real-lebesgue-numerical-index/SOURCE_RECEIPT.json). Canonical statement: [problem 935](../../../problems/935-the-numerical-index-of-real-lebesgue-spaces.md). Hashes and verifier results appear in verification/verification_results.json.

### Exact scope

The canonical object is the ordinary numerical radius of all bounded real-linear operators on scalar real $`L_p([0,1])`$. The submission builds real three-dimensional matrices and then proves equality of norm and numerical radius under pointwise amplification and an explicit surjective isometry to the scalar space. It addresses that exact object, not rank-one, absolute, complex, or two-dimensional numerical indices. The general theorem is for every fixed p; it does not require perturbation constants uniform as $`p\to2`$.

### General-p analytic argument

1. **Scalar maximum and nondegeneracy (general source lines 24–56).** The substitution $`t=e^{-x}`$ gives $`f_p(e^{-x})=\sinh((p-2)x/2)/\cosh(px/2)`$. Its logarithmic derivative is strictly decreasing from $`+\infty`$ to $`-1`$. Thus there is exactly one zero, and the positive function has strictly negative second derivative there. The change of variables preserves nondegeneracy at the interior maximum. Oddness and reciprocal symmetry give exactly the stated extrema of $`h_p`$.

2. **Unperturbed operator (lines 59–102).** With $`c=2^{-1/p}`$, $`u=(c,c)`$, $`\|u\|_p=\|j_p(u)\|_q=1`$. Hölder gives $`\|T_0\|\leq1`$, with equality at a pure y vector. The numerical form is exactly $`F_0=g_p(x,cy)+g_p(z,cy)`$. The scalar inequality for each pair sums to $`|F_0|\leq M_p(|x|^p+|z|^p+|y|^p)`$, using $`2c^p=1`$. Both pairs can attain the same signed scalar extremum, so $`v_p(T_0)=M_p`$.

3. **All maximizing vectors are covered (lines 104–135).** At a maximizer $`y\ne0`$, since otherwise $`F_0=0<M_p\|v\|_p^p`$. Common real rescaling to $`cy=1`$ is valid: both numerical form and norm power scale by $`|\lambda|^p`$. In that chart the normalized form is a positive weighted average of $`h_p(x),h_p(z)`$. Equality forces both scalar entries to be the same signed extremum. The maximizing set on the unit sphere is therefore finite, and all its coordinates are nonzero.

4. **Nondegenerate local deficits.** At a maximizing pair the scalar deficits and their first derivatives vanish. Their second derivatives are strictly positive after the proper sign choice. Therefore the weighted deficit has a diagonal positive definite Hessian: derivatives of its weights and denominator create no additional surviving second-order terms. This verifies the quadratic local deficit needed for the globally optimized radius.

5. **Perturbation vanishes at every extremum (lines 137–167).** For $`0<t<1,\ p>2`$, the denominator $`t^2-t^{2p-2}`$ is positive. Direct algebra gives
   ```math
\kappa-1=\frac{(1-t^2)(1+t^{2p-2})}{t^2-t^{2p-2}}>0.
```
   Every extremizing leaf ratio is $`1,-t^2`$, or $`-t^{-2}`$. The displayed substitution gives $`G(-t^2,1)=0`$, and antisymmetry under swapping leaves plus degree-p homogeneity cover the remaining cases and signs. The numerical form
   $`G=|x|^p-|z|^p+\kappa(j_p(x)z-j_p(z)x)`$
   has the correct signs for the proposed matrix R.

6. **The radius upper bound is global (lines 169–191).** Near all the maximizing vectors, every coordinate stays nonzero; nonintegral p therefore causes no smoothness issue in those charts. The normalized perturbation vanishes at the center and is bounded by a constant times chart distance. Completing the square against the quadratic deficit gives $`M_p+C\varepsilon^2`$. On the complement of finitely many neighborhoods, continuity and compactness supply a fixed positive gap, and the normalized perturbation is bounded. Small enough $`|\varepsilon|`$ handles that entire complement. This is a uniform bound over all unit vectors for each fixed p, not merely an evaluation at original extrema.

7. **The norm gains an earlier-order term (lines 193–220).** With $`w=(c,-c)`$, $`\|w\|_p=1`$, $`Rw=(1-\kappa)u`$, and $`\langle j_p(u),w\rangle=0`$. On the isometric input subspace $`(sw,y)`$, the output is $`((y-(\kappa-1)\varepsilon s)u,0)`$. Its scalar functional norm is
   ```math
(1+(\kappa-1)^q|\varepsilon|^q)^{1/q},\qquad q=p/(p-1)\in(1,2).
```
   Thus the ratio upper bound is
   ```math
M_p-\frac{M_p}{q}(\kappa-1)^q|\varepsilon|^q+o(|\varepsilon|^q)<M_p
```
   for every sufficiently small nonzero epsilon. The coefficient is positive, and $`q<2`$ ensures the quadratic radius loss is smaller. This proves every $`p>2`$, without extrapolating from p=4.

8. **Dual exponents and scalar Lp (lines 223–239).** Finite-dimensional reflexivity makes the T/adjoint norming-pair correspondence exhaustive, preserving numerical radius; operator norms are also equal. The substitution $`s=t^{p-1}`$ gives $`M_q=M_p`$, so every $`1<p<2`$ follows. For pointwise amplification, integrate the homogeneous degree-p inequality against $`j_p(f)`$. Constant vector-valued functions give the reverse bounds, so both norm and numerical radius are exactly preserved. The three-interval map scaled by $`3^{1/p}`$ is a surjective isometry to scalar real $`L_p([0,1])`$. This proves the claimed inequality for the exact canonical space.

### Independent short p=4 proof

Both polynomial identities (935.C2)–(935.C3) check by expansion. In the deficit identity the $`x^2b^2`$ terms cancel; in the G identity all b-dependent terms cancel. The coefficient-vector estimate uses a leaf coefficient matrix of Euclidean operator norm four and then Hölder with exponent $`4/3`$, giving $`20^{3/4}`$.

Completing the square gives exactly $`v_4(T)\leq M_4+20\sqrt{10}\varepsilon^2`$. Replacing b and epsilon by their negatives bounds the negative numerical form too. On the indicated subspace the scalar functional is $`y-3\varepsilon s`$, of norm $`(1+3^{4/3}|\varepsilon|^{4/3})^{3/4}`$. At $`\varepsilon=2^{-12}`$, the strict comparison reduces correctly to $`80\sqrt5<96\,3^{4/3}`$. This supplies another valid p=4 proof independently of the general argument's compactness step and of the rational Gram matrices.

### Exact rational certificate and execution safety

I read all three verifier scripts before executing them. They use only Python's standard library, perform small fixed computations, and contain no network call, subprocess, installation, plotting, or deletion. The exact and independent scripts write JSON beside their own copies. The interval script only prints results.

The scripts were copied into this review's verification directory and run with the specified Python executable and -B. No submitted file was executed in place or rewritten. All three passed.

- Plus leading minors: 10102, 61375400, 976429002, 6319567977, 39156751988, 156153016840.
- Minus leading minors: 9902, 57656315, 466262882, 4413501692, 8528707160, 32937577888.
- Both quartic identities passed. The separate verifier reconstructed all fifteen coefficients and checked rational LDLT factorization with positive pivots.
- $`Aw=(2260310,76761,2485216)`$.
- The norm-witness integer margin is 916493558274854032306529, strictly positive.
- $`4716^2-8\cdot1667^2=9544>0`$.
- Hence $`v(T)/\|T\|<1667/4716<1/(2\sqrt2)=M_4`$.

The generated and submitted JSON objects are equal. Newline-normalized texts are identical. The only byte difference is LF in the originals versus Windows CRLF in regenerated files. All copied scripts are byte-identical to the originals. Hashes and comparisons are recorded in verification/verification_results.json.

The scripts verify the rational p=4 certificate and interval arithmetic. They are not premises of the general-p analytic argument.

### Interval corollary

The analytic inequalities in 935_robustness.tex also check. For $`\max|x_i|=1`$, one coordinate has zero p-variation, so only two summands contribute to each derivative bound. The maximum absolute row sum is $`3351/1000`$. Three-dimensional norm comparison incurs one factor $`3^{|1/p-1/4|}`$, not its square. The convexity chord bound $`3^d\leq1+2d`$ on $`[0,1]`$ has the correct direction.

The derivative of $`f_p(t)`$ and its bound $`15/58`$ are correct. Exact arithmetic confirmed
```math
\text{ratio upper}=\frac{87994832581079}{248910480000000},
\qquad \text{$`M_p`$ lower}=\frac{51261}{145000},
```
with positive difference $`1030282921/248910480000000`$. The conjugate-exponent interval endpoints are also correct. This valid interval result is weaker than the all-p theorem.

### Primary references and later work

- [Martín–Merí–Popov, arXiv:1011.4785](https://arxiv.org/pdf/1011.4785): definitions are on p. 1; Section 5, Problem 5.1, p. 13, states the real-case $`M_p`$ conjecture. The [current arXiv record](https://arxiv.org/abs/1011.4785) lists the original v1.
- [Chiclana, arXiv:2606.01675v1](https://arxiv.org/pdf/2606.01675v1): Theorem 1.1, p. 1, is specifically real dimension two. Its introduction, pp. 1–2, distinguishes the general Lp problem. The [current arXiv record](https://arxiv.org/abs/2606.01675) lists v1 of 1 June 2026. A three-dimensional counterexample does not contradict it.

Targeted current searches for real Lebesgue numerical index, three-dimensional counterexamples, and 2026 developments did not locate a matching earlier all-p counterexample. The current primary OpenAI research catalogue had no matching numerical-index entry. These are bounded checks, not an exhaustive novelty guarantee.

### Findings and limits

No required correction or restricted-only fallback was identified. The exact value of the numerical index is undetermined by this submission, but the stated identity question is fully answered negatively, indeed at every permitted exponent. No plotting or installation was run. This is independent mathematical review with exact arithmetic replay for the finite rational certificate, not a proof-kernel certificate for the analytic theorem.
