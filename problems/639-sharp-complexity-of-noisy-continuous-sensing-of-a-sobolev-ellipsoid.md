# 639. Sharp complexity of noisy continuous sensing of a Sobolev ellipsoid

**Area:** Numerical analysis / information-based complexity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-04

## Problem statement

Let $`B=\{x\in\ell_2(\mathbb N;\mathbb R):\|x\|_2\le1\}`$, with its norm topology, and define the compact operator

```math
D:B\longrightarrow\ell_2,\qquad (Dx)_j=\frac{x_j}{j}.
```

An algorithm makes at most $`n`$ deterministic scalar measurements. For every fixed previous answer vector $`h\in\mathbb R^{i-1}`$, its next query $`\lambda_i(\cdot;h):B\to[-1,1]`$ must be continuous. It receives answers satisfying

```math
|y_i-\lambda_i(x;y_1,\ldots,y_{i-1})|\le\delta,
\qquad i=1,\ldots,n.
```

The errors are adversarial: every answer vector satisfying these inequalities is allowed. The reconstruction $`\phi:\mathbb R^n\to\ell_2`$ is arbitrary. No continuity in the previous answers, common Lipschitz bound, randomness, or computational cost restriction is imposed.

Define

```math
e_n(\delta)=\inf_{\lambda_1,\ldots,\lambda_n,\phi}
\sup_{\substack{x\in B,\ y\in\mathbb R^n\\
|y_i-\lambda_i(x;y_1,\ldots,y_{i-1})|\le\delta\ (1\le i\le n)}}
\|Dx-\phi(y)\|_2.
```

Determine the joint order of $`e_n(\delta)`$ for $`n\ge1`$ and $`0<\delta\le1/2`$, up to positive multiplicative constants independent of **both** $`n`$ and $`\delta`$. In other words, find an explicit comparison function $`F(n,\delta)`$ and absolute constants $`0<c\le C<\infty`$ such that $`cF(n,\delta)\le e_n(\delta)\le CF(n,\delta)`$ throughout that range. No particular formula for $`F`$ is conjectured here.

The bounds currently available from [1] are

```math
\frac{c}{n\log_2(1/\delta)}\le e_n(\delta)\le\frac{C}{n}.
```

Thus the order in $`n`$ is known for each fixed positive noise level. The constants in that comparison do not settle the joint limit as the noise decreases.

There is also the lower bound $`e_n(\delta)\ge2^{-n}`$. Indeed, the adversarial transcript argument in the solution of AIM 553, restricted to the unit sphere in the first $`2^n`$ coordinates, gives an antipodal pair with identical exact answers. On that sphere $`\|Dx\|_2\ge2^{-n}`$. The same pair is admissible with zero measurement error in the noisy model. Together with [1, §5.1], this already gives $`e_n(0)\asymp2^{-n}`$; the noise-free order is not a new problem in this entry.

## Application

This is a compact function approximation problem. In the normalized sine basis on $`(0,\pi)`$, the functions in the unit derivative ball of $`H^1_0(0,\pi)`$ have coefficients $`x_j/j`$ with $`\|x\|_2\le1`$. The question therefore measures the intrinsic accuracy of sequential continuous sensing of such functions when each measurement has bounded error. Queries are continuous in the Sobolev input norm; they are not restricted to linear functionals or point values.

## References

1. D. Krieg, E. Novak, L. Plaskota and M. Ullrich, [*Noisy Nonlinear Information and Entropy Numbers*](https://doi.org/10.1007/s00041-026-10249-z), Journal of Fourier Analysis and Applications **32** (2026), article 36. The model is in §1; the joint noisy diagonal-operator question is in §5.2, especially (9) and the final paragraph on pages 13–14.
2. D. Krieg, E. Novak and M. Ullrich, [*How many continuous measurements are needed to learn a vector?*](https://arxiv.org/abs/2412.06468v2), version 2, 22 September 2026. Theorem 1 and §4 give exact-measurement approximation results, without the joint positive-noise characterization required here.
3. [AIM 553: Continuous adaptive measurements](https://github.com/MColbrook/AIM/blob/main/research/solutions/siavash-sadeghi-553/aim553_report.tex), §1.3, adversarial transcript proof. Its fixed-radius argument gives the additional exponential lower bound above.

## Status review

**Known cases:** The new [manuscript](../research/solutions/639-noisy-continuous-sensing-partial/main.pdf) proves

```math
e_n(\delta)\le\frac{256}{L\log_2(1+2^n/L)},\qquad L=\log_2(1/\delta).
```

Together with the existing lower bounds this gives the sharp orders $`(nL)^{-1}`$ for $`L\le2^{n/2}`$ and $`2^{-n}`$ for $`L\ge2^n`$. Queries are continuous into $`[-1,1]`$ and tolerate the stated adversarial errors.

**Remaining target:** Determine the uniform joint order in the intermediate transition, including $`L`$ of order $`2^n/n`$, where the remaining ratio can grow like $`n/\log n`$.

**Audit, 4 November 2026:** The solutions were found by AI and are written up by Matthew J. Colbrook. A [fresh independent AI audit](../research/solution_reviews/2026-11-04-numerical-analysis/639-review.md) checked the submitted argument, target match and dependencies. No independent human review or formal verification is claimed.

### Earlier status history

Checked on **18 October 2026**. The published source explicitly leaves the behavior for infinite-dimensional diagonal operators unresolved. This formulation fixes $`p=2`$ and $`\sigma_j=1/j`$ and asks for constants uniform in the noise level. The source's finite-rank noise-correction construction, the known noise-free exponential order, and the entropy bounds for arbitrary discontinuous queries do not supply that characterization. No matching later complete result or announcement was located in the documented searches.

This concerns deterministic adaptive continuous measurements of an infinite-dimensional compact embedding. The solved finite-dimensional exact-measurement problem AIM 553 and the nonadaptive continuous-reconstruction problem AIM 570 impose different models. The independent selected-primary, bounded current-results and announcement, semantic and all-status catalogue checks passed at their recorded extents. The final published version is the discovery source; no historical parity with the older arXiv body is assumed.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/noisy-continuous-diagonal-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-noisy-continuous-diagonal-review.json), [semantic comparison](../FURTHER_problems/_tracking/noisy-diagonal-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/noisy-diagonal-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/noisy-diagonal-coordinator-review-2026-10-18.json) record exact scopes and limits. These AI formulation and literature checks are not human peer review or certification of every cited proof.


### Online recheck, 2026-10-30

The published noisy-information paper leaves the infinite-dimensional diagonal example open. Noise-free exponential accuracy and fixed-noise polynomial order do not give the joint n,delta asymptotic with uniform constants.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/s00041-026-10249-z); [status source 2](https://arxiv.org/abs/2510.23213); [status source 3](https://arxiv.org/abs/2412.06468). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-451423a47a56d254** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
