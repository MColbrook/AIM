# 666. Injectivity radius of the canonical Stiefel manifold

**Area:** Riemannian geometry / manifold optimization and data analysis

**Status:** 🔵 OPEN

**Last checked:** 2026-10-21

## Problem statement

For integers $`n\geq 4`$ and $`2\leq p\leq n-2`$, consider the real Stiefel manifold

```math
\mathrm{St}(n,p)=\{U\in\mathbb{R}^{n\times p}:U^\top U=I_p\}
```

with the canonical Riemannian metric

```math
g^{\mathrm{can}}_U(\xi,\zeta)
=\mathop{\mathrm{tr}}\!\left(\xi^\top\left(I_n-\frac12 UU^\top\right)\zeta\right),
\qquad \xi,\zeta\in T_U\mathrm{St}(n,p).
```

Determine its global injectivity radius. Specifically, prove or disprove the conjecture

```math
\mathop{\mathrm{inj}}(\mathrm{St}(n,p),g^{\mathrm{can}})=\sqrt{2}\,\tau
\qquad\text{for every }2\leq p\leq n-2,
```

where $`\tau`$ is the smallest positive root of $`\sin(t)/t+\cos(t)=0`$; equivalently, $`\tau\in(\pi/2,\pi)`$ solves $`\tan\tau=-\tau`$. The proposed radius is approximately $`0.9132618916\pi`$.

Here the injectivity radius at $`U`$ is the supremum of the radii of open tangent balls on which the Riemannian exponential at $`U`$ is a diffeomorphism onto its image; the global radius is the infimum over $`U`$. Homogeneity makes this independent of the base point. Geodesics shorter than this radius are uniquely minimizing.

## Application

The Stiefel manifold represents orthonormal frames used in manifold optimization, statistics and data fitting. A sharp injectivity radius gives a uniform length threshold guaranteeing that a computed canonical-metric geodesic realizes the Riemannian distance, and identifies the domain on which normal coordinates and the Riemannian logarithm are unambiguous. These uses concern geometric computations with constrained data; they are discussed in [1, Introduction] and [3, Section 1].

## References

1. P.-A. Absil and S. Mataigne, [The Ultimate Upper Bound on the Injectivity Radius of the Stiefel Manifold](https://doi.org/10.1137/24M1644808), *SIAM Journal on Matrix Analysis and Applications* 46(2), 1145–1167 (2025), Sections 5–8; [accepted preprint, arXiv:2403.02079v3](https://arxiv.org/abs/2403.02079v3).
2. R. Zimmermann and J. Stoye, [High Curvature Means Low Rank: On the Sectional Curvature of Grassmann and Stiefel Manifolds and the Underlying Matrix Trace Inequalities](https://doi.org/10.1137/24M1655755), *SIAM Journal on Matrix Analysis and Applications* 46(1), 748–779 (2025); [preprint, arXiv:2403.01879v3](https://arxiv.org/abs/2403.01879v3), Theorem 8 and Section 3.4.
3. J. Stoye, S. Mataigne, P.-A. Absil and R. Zimmermann, [Shortest geodesic loops, sectional curvature, and injectivity radius of the Stiefel manifold](https://doi.org/10.1007/s10543-026-01141-9), *BIT Numerical Mathematics* 66, article 42 (22 June 2026), Theorems 3.4 and 7.3, Section 7.2 and Appendix C; [arXiv:2511.01563v2](https://arxiv.org/abs/2511.01563v2).
4. R. Zimmermann and J. Stoye, [The Injectivity Radius of the Compact Stiefel Manifold under the Euclidean Metric](https://doi.org/10.1137/24M1663818), *SIAM Journal on Matrix Analysis and Applications* 46(1), 298–309 (2025); [arXiv:2405.02268](https://arxiv.org/abs/2405.02268).

## Status review

**Literature check, 2026-10-21:** The published June 2026 paper [3, Section 7.2] explicitly retains the canonical-metric case as a conjecture. Searches for subsequent proofs or counterexamples, including the relevant arXiv records and later work on canonical Stiefel injectivity and conjugate radii, found no matching resolution.

**Known bounds:** The sharp sectional-curvature upper bound $`5/4`$ in [2], the shortest nontrivial geodesic-loop length $`2\pi`$ in [1, 3], and the explicit conjugate points in [1] give

```math
\sqrt{\frac45}\,\pi
\leq \mathop{\mathrm{inj}}(\mathrm{St}(n,p),g^{\mathrm{can}})
\leq \sqrt{2}\,\tau <\pi.
```

Klingenberg's formula expresses the radius as the minimum of the conjugate radius and half the shortest loop length. Since the displayed upper bound is below $`\pi`$, the remaining question is whether any geodesic has a conjugate point before $`\sqrt{2}\tau`$.

Appendix C of [3] identifies the first conjugate point along one specified geodesic in $`\mathrm{St}(4,2)`$; this does not determine the minimum over all initial directions. The exact Euclidean-metric radius $`\pi`$ in [4] uses a different metric. The excluded cases $`p=1`$, $`p=n-1`$ and $`p=n`$ have canonical-metric radius $`\pi`$ in the relevant positive-dimensional cases [3, Section 7.1]. The task here is the stated dimension range and canonical normalization.


Admission from [PR 173](https://github.com/MColbrook/AIM/pull/173) is documented in the [dated source and scope review](../research/solution_reviews/2026-10-21-active-prs/173-new-problem-review.md).
