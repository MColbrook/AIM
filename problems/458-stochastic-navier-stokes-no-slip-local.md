# 458. Local no-slip Navier–Stokes theory under non-small transport noise

**Area:** Stochastic fluid PDEs; solid boundaries

**Status:** ✅ SOLVED

**Last checked:** 2026-10-21

## Problem statement

Let $`D\subset\mathbb R^3`$ be bounded with smooth boundary, $`\nu>0`$, and $`b_1,\ldots,b_K\in C^\infty(\overline D;\mathbb R^3)`$ be divergence-free, tangent to $`\partial D`$, and satisfy

```math
\nu I-\tfrac12\sum_kb_k\otimes b_k\ge\delta I\quad(\delta>0).
```

For every smooth divergence-free $`u_0`$ vanishing on $`\partial D`$, does

```math
du=[\nu\mathbb P_D\Delta u-\mathbb P_D\nabla\cdot(u\otimes u)]dt+\sum_k\mathbb P_D[(b_k\cdot\nabla)u]dW^k_t,\qquad u|_{\partial D}=0,
```

have a pathwise unique local adapted solution in

```math
C([0,\tau];B^{1/2}_{4,4}(D;\mathbb R^3))\cap L^4(0,\tau;W^{1,4}_0(D;\mathbb R^3))
```

for an almost surely positive stopping time $`\tau`$, with continuous dependence in probability after common stopping? Here $`\mathbb P_D`$ is the Helmholtz projection and the equation is understood in the weak solenoidal $`W^{-1,4}`$ space, or equivalently by the extrapolated Dirichlet Stokes semigroup. Require only the displayed stochastic parabolicity condition on noise amplitude, rather than a perturbatively small norm of $`b`$.

## Application

Solid walls impose a physically important constraint on turbulent transport models; a local theory is needed before questions of long-time behavior can be posed in this setting.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 9. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. D. Goodair, *Navier-Stokes Equations with Navier Boundary Conditions and Stochastic Lie Transport: Well-Posedness and Inviscid Limit*, discussion of the no-slip obstruction. [Author manuscript](https://arxiv.org/abs/2308.04290).
3. D. Goodair, *Anisotropic Inviscid Limit for the Navier-Stokes Equations with Transport Noise Between Two Plates* (2026 preprint). [Preprint](https://arxiv.org/abs/2603.13199).

## Status review

**Resolution reviewed 2026-10-21:** Kaiwen Jin's revised [manuscript](../research/458/paper/paper.pdf), [PR 175](https://github.com/MColbrook/AIM/pull/175) at `a9e2073c1da1a576c699b0a71661068013c43ab7`, establishes local adapted existence, pathwise uniqueness in the displayed class, and continuous dependence after common stopping for the full finite smooth-noise target under the stated stochastic parabolicity condition.

The [complete independent AI review](../research/solution_reviews/2026-10-21-active-prs/175-review.md) reconstructs the full argument and checks its primary-source interfaces. A [second independent review](../research/solution_reviews/2026-10-21-active-prs/175-second-review.md) verifies the repaired channel-calculus step: Lemmas 3.1–3.2 supply the compatible positive and negative fractional right inverses required by the Kunstmann–Weis 2013 erratum, as well as the projection-image conditions. This closes the blocker in the [15 October review](../research/solution_reviews/2026-10-15-active-prs/458-review.md).

**Literature check:** No earlier complete solution of this exact target was found on 21 October 2026. Goodair's no-slip weak martingale and two-dimensional results have different solution and dimension quantifiers; the torus theory does not establish the stated arbitrary smooth-domain no-slip theorem. The review records the primary-source comparisons and search limits.

The accepted conclusion concerns the precise finite smooth-coefficient formulation above. It does not assert global three-dimensional regularity, a theorem for arbitrary rough or infinite-dimensional noise, human peer review or Lean verification.
