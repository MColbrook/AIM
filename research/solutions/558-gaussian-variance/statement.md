# 558. Variance ordering for Gaussian alpha-divergence approximations

**Area:** Bayesian uncertainty quantification and variational inference

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`d\ge2`$, let $`\mu\in\mathbb R^d`$, and let $`\Sigma`$ be a real symmetric positive-definite, non-diagonal $`d\times d`$ matrix. Write $`p`$ for the density of $`N(\mu,\Sigma)`$ and let $`\mathcal Q`$ be the family of all Gaussian densities $`N(\nu,\Psi)`$ with $`\nu\in\mathbb R^d`$ and positive diagonal covariance $`\Psi`$.

For $`\alpha>1`$, define

```math
D_\alpha(p\Vert q)=\frac{1}{\alpha(\alpha-1)}\left(\int_{\mathbb R^d}p(x)^\alpha q(x)^{1-\alpha}\,dx-1\right),
```

with value $`+\infty`$ when the integral diverges. Let $`q_\alpha=N(\mu,\Psi(\alpha))`$ minimize this divergence over $`\mathcal Q`$. The finite-divergence domain is

```math
\alpha\Sigma^{-1}+(1-\alpha)\Psi^{-1}\succ0.
```

The minimizing mean equals $`\mu`$. The covariance is well-defined and unique: in diagonal precision coordinates $`T=\Psi^{-1}`$, its optimization is equivalent to minimizing

```math
-\log\det\bigl(\alpha\Sigma^{-1}-(\alpha-1)T\bigr)-(\alpha-1)\log\det T
```

on the convex domain $`T\succ0`$, $`\alpha\Sigma^{-1}-(\alpha-1)T\succ0`$; this objective is strictly convex and diverges at the boundary.

Prove or disprove that, for every such target and every $`1<\alpha_1<\alpha_2`$,

```math
\Psi_{ii}(\alpha_1)\le\Psi_{ii}(\alpha_2)\qquad(i=1,\ldots,d),
```

with strict inequality for at least one coordinate. This is the conjecture in Remark 12 of [1], with the ordering convention of Definition 2. It compares marginal variances of separately optimized approximations, rather than divergence values at a fixed pair of distributions.

## Application

Factorized Gaussian variational inference is used to approximate Bayesian posteriors efficiently. Its reported marginal variances depend on the divergence being minimized. The conjecture would establish whether increasing $`\alpha`$ above one always increases those variances for Gaussian targets, giving a precise interpretation of this tuning parameter in uncertainty quantification. It does not assert posterior calibration or extend the ordering to arbitrary non-Gaussian targets.

## References

1. C. C. Margossian, L. Pillaud-Vivien and L. K. Saul, [Variational Inference for Uncertainty Quantification: an Analysis of Trade-offs](https://www.jmlr.org/papers/v26/24-0878.html), *Journal of Machine Learning Research* **26**(202) (2025), 1–41. Definition 2 and Theorem 3, pp.5–6; §4.2, pp.13–16; §5.2–5.3, especially Remark 12, p.26. [Published PDF](https://www.jmlr.org/papers/volume26/24-0878/24-0878.pdf).
2. The same authors, [latest manuscript located, arXiv:2403.13748v5](https://arxiv.org/html/2403.13748v5), 19 October 2025, Remark 12. This is another version of [1], not independent confirmation.

## Status review

Reference [1] proves the analogous ordering for $`0<\alpha_1<\alpha_2<1`$. For $`\alpha>1`$, it proves that every optimized variance is at least the corresponding target variance, with some strict inequality, and that the optimized variances are finite and positive. Those facts do not compare two parameters above one. Its non-ordering example involving a score-based divergence (§5.5) concerns a different comparison.

Remark 12 remains in the latest manuscript located. Searches through 24 September 2026 found no matching proof, counterexample or solution announcement. Later symmetry-based guarantees concern recovery of means and correlations in different variational families, and do not establish this coordinatewise ordering. The entry is distinct from the repository's existing inference, sampling and entropy targets.
