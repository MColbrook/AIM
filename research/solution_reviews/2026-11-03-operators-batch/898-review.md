# AIM 898: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/898-a-universal-lipschitz-bound-for-the-canonical-affine-projection.md) · [PDF manuscript](../../solutions/898-affine-lipschitz-projection/aim898.pdf) · [source and reproduction](../../solutions/898-affine-lipschitz-projection/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## Independent review: AIM 898

Reviewed 2026-11-03 at base commit 5d7e26e8444eb98de91988454564e45e011107c4.

**Verdict: PASS — full negative resolution of the canonical question.** No substantive gap was found in the main theorem, fixed-distortion corollary, or distortion-tending-to-one remark. This follows from checking the proof, not the submission's own review claims.

Source: [898.tex](../../solutions/898-affine-lipschitz-projection/SOURCE_RECEIPT.json). Canonical statement: [problem 898](../../../problems/898-a-universal-lipschitz-bound-for-the-canonical-affine-projection.md). SHA-256 hashes appear in verification/verification_results.json.

### Scope and normalization

The canonical problem specifies the scalar L2 orthogonal projection onto affine functions, on symmetric volume-one isotropic convex bodies, measured with the intrinsic norm. The submission produces intrinsically 1-Lipschitz functions with projected Lipschitz constant at least $`a_n`$, where $`a_n/\sqrt n\to c_*>0`$, in dimension $`n+1`$. Linear normalization preserves that exact projection and both Lipschitz constants. Thus it answers the specified question, including all normalizations.

### Main proof audit

1. **Convexity (source lines 32–65).** The Hessians of $`h+c`$ and $`h-c`$ are diagonal with entries $`-2+2y_i`$ and $`-2-2y_i`$. They are negative semidefinite on the open ball; continuity extends concavity to its closure. Therefore the upper fiber boundary is concave and the lower boundary convex. Compactness, interior, and central symmetry hold. At $`y=0`$ the fiber is exactly $`[-1,1]`$, so $`\|e_0\|_K=1`$.

2. **Lipschitz constant.** Projection of the body onto y is exactly $`B_2^n`$, giving $`\|y\|_2\leq\|(x,y)\|_K`$ by homogeneity. The partial derivative bounds give $`\|\nabla f_n\|_2\leq1`$. Thus $`g_n(x,y)=f_n(y)`$ is intrinsically 1-Lipschitz with no dimensional loss.

3. **Marginal and moments (lines 67–111).** Fiber length is $`2h(y)`$. With $`N=n+4`$, the marginal has the law of the first n coordinates of a uniform point on $`S^{N-1}`$, since its density exponent is $`(N-n-2)/2=1`$. The spherical moment formula is correct. In particular,
   ```math
E Y_i^2=N^{-1},\quad E Y_i^4=\frac3{N(N+2)},\quad
   E Y_i^6=\frac{15}{N(N+2)(N+4)}.
```
   Conditional mean and variance of the vertical coordinate are $`c(Y)`$ and $`h(Y)^2/3`$. Consequently $`E[XY_i]=1/[N(N+2)]`$, and $`W=X-(N+2)^{-1}\sum_iY_i`$ is orthogonal to every $`Y_i`$.

4. **Residual covariance.** Cross-coordinate terms in $`E r(Y)^2`$ vanish by the marginal's coordinate sign symmetries. Combining diagonal terms gives
   ```math
V_n=\frac{2n(N-1)}{3N(N+2)^2(N+4)}.
```
   The radial squared norm has beta parameters $`n/2,2`$; hence $`E h(Y)^2=24/[N(N+2)]`$. Therefore
   ```math
D_n=E W^2=V_n+\frac8{N(N+2)},\qquad n^2D_n\to26/3.
```
   There is no omitted covariance contribution: the conditionally centered vertical noise is orthogonal to every function of Y.

5. **Regression and numerator (lines 113–149).** In coordinates $`(W,Y)`$, the coefficient of W, and thus of the original x, is $`E[r(Y)f_n(Y)]/D_n`$. The affine constant vanishes by oddness. Off-diagonal numerator terms vanish under a single-coordinate sign change. The n diagonal contributions cancel the factor $`1/n`$ in $`f_n`$, leaving exactly
   ```math
n^{3/2}E[r(Y)f_n(Y)]
   =E[(Z_n^3/3-nZ_n/(n+6))\varphi(Z_n)].
```
   The scaling is correct. The Gaussian coupling proves convergence, and the uniform eighth-moment bound plus $`|\varphi(t)|\leq|t|`$ supplies uniform integrability for these expressions of growth at most four.

6. **Positive limit and growth (lines 150–176).** Integration by parts is valid for this C1 function of linear growth with bounded derivative. It yields
   ```math
\gamma=\tfrac13E[(Z^2-1)\min(Z^2,1)]
          =\tfrac13E[(1-Z^2)^2\,1_{\{|Z|\leq1\}}]>0.
```
   Thus $`a_n/\sqrt n\to3\gamma/26=c_*`$, with exactly the stated constant. Evaluation at $`0,e_0`$ gives the projected Lipschitz lower bound $`|a_n|`$.

7. **Isotropic normalization (lines 178–191).** Covariance is positive definite because the body has interior. Its inverse square root, followed by a scalar dilation, gives volume one and scalar covariance. Normalized uniform measure pushes forward; the pullback preserves the affine subspace and its L2 minimizer. This proves the projection conjugacy. It is also an isometry between the two Minkowski norms. The final projection is precisely the formula in the canonical statement.

### Banach–Mazur extensions

The corollary beginning at line 205 checks as well.

- Both branches of $`h_M\pm c_\alpha`$ are concave for $`M\geq1`$, $`2\alpha\leq1`$. The minimum of concave functions is concave, as seen from intersecting their convex hypographs.
- The outer inclusion follows from vertical displacement at most $`\alpha/3\leq\delta`$ from the unit Euclidean ball. For the inner inclusion, $`r\leq1-\delta`$ implies $`M\sqrt{1-r^2}\geq1`$, so the square-root branch is active. The displayed fiber gap is at least $`\delta`$.
- The removed reference mass is at most $`(n/2+1)(1-M^{-2})^{n/2}`$. Actual uniform measure is reference measure conditioned on the actual body. Bounded moments therefore change exponentially little.
- Radiality and permutation symmetry justify the scalar regression formula $`(A-nvt/u)/(B-nv^2/u)`$. All scalar moments are bounded for fixed parameters and $`u^{-1}=O(n)`$, so $`O(n^3p_n)`$ is a valid conservative bound on numerator and denominator errors. Inversion adds only polynomial losses because the reference denominator has a positive $`n^{-2}`$ asymptote.
- The limit is $`\alpha\gamma/(2\alpha^2/3+8M^2)>0`$. Since $`e_0`$ still has norm one, the projected norms diverge. The inclusions give Banach–Mazur distance at most $`(1+\delta)/(1-\delta)`$, preserved by normalization.

For the final remark, the concavity conditions hold eventually for the varying parameters. All parameter-dependent moment and inverse-covariance bounds remain polynomial, whereas the exceptional mass is bounded by a polynomial times $`\exp(-n\delta_n/2)`$. The reference numerator is $`3\gamma n^{-13/8}(1+o(1))`$ and denominator $`4n^{-15/8}(1+o(1))`$, giving $`a_n\sim(3\gamma/4)n^{1/4}`$. The claimed simultaneous divergence and distance tending to one are justified.

### Primary sources and later work

- [Hytönen–Naor, arXiv:1608.01915v1](https://arxiv.org/pdf/1608.01915v1): Question 19 and equations (27)–(28), printed p. 15, match the operator question. Section 5.A, pp. 28–29, gives its transport interpretation. The [current author PDF](https://web.math.princeton.edu/~naor/homepage%20files/UAAP-heat-flow.pdf) retains this formulation.
- [Hytönen–Li–Naor, author version](https://web.math.princeton.edu/~naor/homepage%20files/Quant-UAAP-UMD.pdf): Lemma 10, p. 6 of the 37-page PDF, gives the Euclidean-ball contraction.
- [Bizeul–Klartag, arXiv:2509.10355v1](https://arxiv.org/pdf/2509.10355v1): Theorems 1.2 and 1.4, pp. 4–5, concern statistical L2 risk of polynomial estimators, not the intrinsic Lipschitz operator norm.
- [Jung–Petitjean–Prochazka–Quilis, arXiv:2606.11723v1](https://arxiv.org/html/2606.11723v1): Theorem A chooses an atlas and has a Nagata-dimension-dependent Lipschitz bound, so its approximants differ from this projection.

Targeted current searches did not locate a prior matching resolution. This was bounded literature checking, not an exhaustive novelty guarantee. No substantive external theorem is needed by the submitted proof beyond standard integration and probability.

### Findings and limits

No required correction or restricted-only fallback was identified. Plots were not run or used as proof evidence. The decimal value of the limiting constant is unnecessary. This is independent mathematical review, not a proof-kernel certificate.
