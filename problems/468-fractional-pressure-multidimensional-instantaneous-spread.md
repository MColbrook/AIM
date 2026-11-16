# 468. Instantaneous spreading for fractional-pressure flow in several dimensions

**Area:** Nonlocal PDEs; propagation of a diffusing front

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-17

## Problem statement

Fix $`N\ge2`$, $`1<m<2`$ and $`0<s<1`$.

On $`\mathbb R^N`$ use the model

```math
u_t=\nabla\cdot(u^{m-1}\nabla p),\qquad p=(-\Delta)^{-s}u,
```

where the inverse fractional Laplacian has Fourier multiplier $`|\xi|^{-2s}`$. Take nonzero, nonnegative $`u_0\in L^1\cap L^\infty`$ with compact support. By a bounded energy weak solution mean a nonnegative distributional solution with the initial trace $`u_0`$, continuous into $`L^1`$ with its weak topology, conserving $`\int u_0`$, and satisfying $`\|u(t)\|_\infty\le\|u_0\|_\infty`$, locally integrable flux, and

```math
\frac12\|(-\Delta)^{-s/2}u(t)\|_2^2+
\int_0^t\!\int u^{m-1}|\nabla(-\Delta)^{-s}u|^2
\le\frac12\|(-\Delta)^{-s/2}u_0\|_2^2.
```

Use also the dissipative $`L^q`$ inequalities, for every $`q>1`$,

```math
\|u(t)\|_q^q+\frac{4q(q-1)}{(m+q-1)^2}\int_0^t\|(-\Delta)^{(1-s)/2}u^{(m+q-1)/2}\|_2^2\,dr\le\|u_0\|_q^q.
```

Does every bounded energy weak solution satisfy

```math
\int_{\{|x|>R\}}u(t,x)\,dx>0\qquad\text{for every }R>0\text{ and }t>0?
```

This asks for unbounded essential support immediately after time zero. It does not require pointwise positivity everywhere or assume radial symmetry.

## Application

The assertion would locate the transition between a moving compact front and immediate long-range spreading in nonlocal porous-medium transport.

## References

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

## Status review

**Resolution claim (2026-11-17):** Kaiwen Jin's [proposed analytic counterexample](../research/solutions/468-fractional-pressure-weak-counterexample/paper.pdf) gives one $`N=3`$, $`m=3/2`$ and $`s\in(7/8,1)`$ for which a global solution in the stated energy class retains compact support for a positive initial interval. Such a solution would negate the universal assertion. The status is **Solution claimed**, with independent review outstanding.

The package includes [editable source](../research/solutions/468-fractional-pressure-weak-counterexample/source/main.tex), a [clause-by-clause target comparison](../research/solutions/468-fractional-pressure-weak-counterexample/TARGET_COMPARISON.md), and an [AI-use and review-scope disclosure](../research/solutions/468-fractional-pressure-weak-counterexample/REVIEW_SCOPE.md). One reader and one specialist AI context examined the complete draft; one revision and final artifact checks followed. No independent human acceptance is claimed.

**Historical literature check (2026-09-22):** Open in cited literature; no later resolution located.

Remark 7 of the survey explicitly leaves the multidimensional extension of infinite propagation open. The 2026 PDE review still states the infinite-propagation result only for dimension one. Searches on 2026-09-22 checked higher-dimensional spreading and later pressure-model papers; no whole-space result for the stated class was located. Infinite spreading of self-similar profiles, results on a torus, and finite propagation for $`m\ge2`$ do not answer this question. The weak formulation uses positive exterior mass because continuity is not being assumed.
