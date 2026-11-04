# AIM 905: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/905-does-lipschitz-affine-approximation-determine-the-exact-martingale-cotype.md) · [PDF manuscript](../../solutions/905-lipschitz-approximation-martingale-cotype/aim905.pdf) · [source and reproduction](../../solutions/905-lipschitz-approximation-martingale-cotype/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## Independent review: AIM 905

Reviewed 2026-11-03 at base commit 5d7e26e8444eb98de91988454564e45e011107c4.

**Verdict: PASS — full affirmative resolution at the original exponent q, including arbitrary probability spaces.** No substantive gap was found. The argument does not replace the hypothesis by a Sobolev bound, constrain the affine approximants, assume complemented target subspaces, or pass to $`q+\varepsilon`$.

Source: [905.tex](../../solutions/905-lipschitz-approximation-martingale-cotype/SOURCE_RECEIPT.json). Canonical statement: [problem 905](../../../problems/905-does-lipschitz-affine-approximation-determine-the-exact-martingale-cotype.md). Hashes appear in verification/verification_results.json.

### Hypothesis match and reduction to curves

The source's $`\mathcal D_X`$ is exactly the canonical integral: average qth power of error to arbitrary Y-valued affine maps, integrated with $`dt/t^{q+1}`$. Scaling maps legitimately gives $`\mathcal D_X(f)\leq CL^q|\mathop{\mathrm{supp}}f|`$ for Lipschitz constant at most L.

In the reduction lemma (lines 41–84), support volume is at most $`(4R)^{n-1}`$, and the telescoping product gives
```math
\mathop{\mathrm{Lip}}_X(f_R)\leq\|\ell_1\|+R^{-1}\sum_{j>1}\|\ell_j\|\leq L.
```
For the chosen transverse centers and $`t\leq1`$, $`R\geq2B`$ makes the cutoff identically one on the whole intrinsic ball. Restricting to the inner cube costs exactly $`\kappa=(2b)^n/|B_X|`$. Averaging every affine map over the transverse cube gives an affine function of the first coordinate, and Jensen proves the lower bound for all such maps, including those outside the curve's span. The substitution $`u=bt`$ gives the factor $`b^q`$. The asserted K follows. Empty products correctly handle $`n=1`$.

### Separated-scale martingale encoding (lines 86–183)

1. Conditional Jensen puts all values of the martingale in $`B_Y`$ when its terminal supremum norm is at most one. There are finitely many values of every $`a_k`$. Thus every positive $`\delta_k`$ exists, and the next dyadic scale can be chosen small enough. The gaps may depend on the martingale without affecting the final constant, since the curve hypothesis is uniform over all curves.

2. The selected binary digits are independent fair signs. The functions $`g_k`$ have norm at most one and mean zero. Their primitives, extended by zero, are continuous, globally 1-Lipschitz, and supported in $`[0,1]`$. This finite-valued construction needs no differentiability or Radon–Nikodym property of Y.

3. On cells of length $`2h_{k+1}`$, earlier selected digits are fixed and integration of later digits gives $`M_k`$. Hence the integral of $`g_N-g_k`$ over each complete cell is zero. Its norm is at most two, so the primitive on the remaining partial cell is bounded by $`4h_{k+1}`$. There is no additional factor from the number of later differences.

4. On a full period of $`r_{m_k}`$, earlier digits are constant because the dyadic grids are nested. $`F_k`$ is affine plus the displayed tent. The sign function $`\psi`$ has zero zeroth and first moments, and its average against the tent is $`h_ka_k(I)/4`$. Applying the norm after the Bochner integral and then Hölder bounds the error of every Y-valued affine map. Tail subtraction and $`4h_{k+1}\leq h_k\delta_k/8`$ give the claimed lower bound $`h_k\|a_k(I)\|/8`$. Zero differences and the terminal scale cause no exception.

5. The specified center/scale rectangles contain I and have local interval length at most $`3h_k`$. They are disjoint at each scale in the center variable and across scales in the scale variable. Recomputing the contribution gives
   ```math
\frac{h_k\|a_k(I)\|^q}{18\cdot12^q}.
```
   Earlier digits have the uniform joint distribution over full periods. Thus $`\sum_I2h_k\|a_k(I)\|^q=E\|M_k-M_{k-1}\|^q`$, yielding exactly the valid bound $`A=36\cdot12^qK`$.

The scale weight compensates for the tent amplitude, independent of the frequency gaps. This justifies the exact exponent rather than only a qualitative or q-plus-epsilon consequence.

### Bellman renorming (lines 185–258)

Subtracting a deterministic starting x and dividing by two bounds every ball-valued Walsh–Paley martingale's energy by $`2^qA`$. The supremum defining $`\Phi`$ is finite and even. Joining near-optimal finite martingales after a fair split from $`(x+y)/2`$, with horizons equalized by constant steps, proves exactly
```math
\Phi((x+y)/2)\geq(\Phi(x)+\Phi(y))/2+2^{-q}\|x-y\|^q.
```
No optimal martingale must attain the supremum. Taking $`y=-x`$ gives $`u=\Phi(0)-\Phi\geq0`$ and $`u(x)\geq\|x\|^q`$.

Local boundedness gives continuity and convexity of u on the open ball. The radial estimate $`u(x)\leq H\|x\|`$ follows using interior radial endpoints tending to the unit boundary; continuity at that boundary is unnecessary. The level set K satisfies
```math
aB_Y\subseteq K\subseteq rB_Y,\qquad a=(2H)^{-1},\quad r=2^{-1/q}<1.
```
Every relevant level-set point is within the continuity region. Hence K is a closed symmetric convex absorbing body, and its gauge p is an equivalent norm with $`ap\leq\|\cdot\|\leq rp`$.

The secant-slope argument gives the valid bound $`L=2H/(1-r)`$ for u on $`r'B_Y`$. The strong midpoint deficit is $`\Delta=(\|x-y\|/2)^q\leq1/2`$. The proposed dilation with $`\eta=\Delta/(4L)`$ remains inside $`r'B_Y`$, since $`r+2\eta\leq r+1/(4L)<r'`$ for $`H\geq1`$. Its u-value remains at most $`1/2`$. Consequently
```math
\delta_p(\varepsilon)\geq a^q\varepsilon^q/(2^{q+2}L).
```
All constants are positive and finite, and q has not changed.

### Arbitrary probability spaces (lines 260–367)

The final implication is actually proved in the source, so the review does not depend on an unchecked citation:

- The scalar Clarkson bound is valid for every real $`q\geq2`$. In the case $`A-B\geq d/2`$, it gives the $`4^{-q}d^q`$ deficit.
- Otherwise $`d\leq A+B=2t`$ implies $`B>t/2`$ and $`A<3t/2`$. The normalized-vector separation is at least $`d/(3t)`$. The modulus bound and the displayed decomposition of $`(x+y)/2`$ give the second deficit $`cd^q/(2\cdot3^q)`$.
- Therefore $`F=p^q`$ has the stated homogeneous midpoint convexity with $`\kappa=\min\{4^{-q},c/(2\cdot3^q)\}`$. Combining with a supporting functional at x gives the tangent inequality with coefficient $`2\kappa`$.
- For a finite-valued martingale, subgradients are chosen separately at finitely many values. Their conditional pairings with differences have mean zero. Telescoping gives the claimed terminal Lq bound.
- On an arbitrary probability space, finite-valued approximants $`s_k`$ generate nested finite sigma algebras $`\mathcal A_k\subseteq\mathcal F_k`$. The finite averages $`N_k=E[M_N\mid\mathcal A_k]`$ exist without any additional property of Y. Tower and contraction give $`\|N_k-M_k\|_{L^q(p)}\leq2\epsilon`$. Since the horizon is finite, passing to the limit in every term is valid.

The final norm comparison is correct:
```math
\left(\sum_kE\|M_{k+1}-M_k\|^q\right)^{1/q}
\leq(r/a)(2\kappa)^{-1/q}(E\|M_N\|^q)^{1/q}.
```
This implies the exact canonical maximum-over-times inequality.

### Primary references and later work

- [Hytönen–Naor, arXiv:1608.01915v1](https://arxiv.org/pdf/1608.01915v1): Theorem 9, (13), and Question 10, printed p. 10, match the hypothesis and target. Proposition 33, pp. 30–32, concerns the earlier weaker scope. The [current author PDF](https://web.math.princeton.edu/~naor/homepage%20files/UAAP-heat-flow.pdf) retains the question.
- [Hytönen–Merikoski, arXiv:1612.09502v3](https://arxiv.org/pdf/1612.09502v3): Theorem 1, p. 3, recalls exact-q renorming. Theorem 4 and Remark 3, p. 5, distinguish the stronger Sobolev estimate. The current record lists v3 of 14 December 2017; journal metadata matches the bibliography.
- [Pisier, publisher record](https://link.springer.com/article/10.1007/BF02760337): author, title, volume 20 (1975), pp. 326–350, and DOI match. Full original theorem pages were inaccessible, so no unverified theorem number is assigned. The submitted direct proof removes a dependence on those inaccessible pages.
- [Ryoo, arXiv:2207.11305v2](https://arxiv.org/pdf/2207.11305v2): Theorem 34, p. 22, is scalar Carnot-group approximation; Theorems 55–57, p. 38, assume q-uniform convexity.
- [Current primary OpenAI catalogue](https://raw.githubusercontent.com/openai/math/main/overview.tex), entry 327, claims qualitative superreflexivity from nontrivial Markov type. The linked PDF could not be fetched because of octet-stream handling. Only that primary catalogue claim was checked, not its full proof or page-1 theorem. It does not supply an exact-q conclusion for this hypothesis.

Targeted current searches did not locate a matching earlier exact-q resolution. This is bounded literature checking, not an exhaustive novelty guarantee.

### Findings and limits

No required correction or restricted-only fallback was identified. The proof explicitly handles unrestricted affine approximants, martingale-dependent gaps, exact exponent, and arbitrary probability spaces. No numerical experiment was needed. This is independent mathematical review, not a proof-kernel certificate.
