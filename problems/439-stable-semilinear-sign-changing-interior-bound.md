# 439. Interior bounds for stable elliptic states with sign-changing reaction laws

**Area:** Semilinear elliptic PDEs and reaction equilibria

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03
## Problem statement

For each $`d\in\{6,7,8,9\}`$, does there exist $`C_d<\infty`$ such that, for every $`f\in C^1(\mathbb R)`$ and every $`u\in C^2(B_1)`$ satisfying

```math
-\Delta u=f(u),\qquad \int_{B_1} f'(u)\varphi^2\le\int_{B_1}|\nabla\varphi|^2\quad(\varphi\in C_c^\infty(B_1)),
```

one has

```math
\|u\|_{L^\infty(B_{1/2})}\le C_d\|u\|_{W^{1,2}(B_1)}?
```

Here $`B_r\subset\mathbb R^d`$ is a centered ball, stability means the displayed nonnegative second-variation inequality, and no sign assumption is imposed on $`f`$ or $`u`$. The constant must be independent of the reaction law.

## Application

Stable stationary reaction-diffusion patterns can have both production and depletion regimes. A uniform estimate would rule out concentration in dimensions below ten without requiring the reaction to have one sign.

## References

1. X. Cabré, [Stable solutions to reaction-diffusion elliptic problems](https://arxiv.org/abs/2603.03161), lecture survey (2026), §3.5.4.
2. F. Peng, Y. R.-Y. Zhang and Y. Zhou, [Interior Hölder regularity for stable solutions to semilinear elliptic equations up to dimension 5](https://arxiv.org/abs/2204.06345), preprint (2022), main interior estimate and discussion of dimensions 6–9.

3. L.-H. Huang, Y. Zhou and W. Zou, [*Interior Regularity for Stable Solutions of Semilinear Elliptic Equations with Sign-Changing Nonlinearities*](https://arxiv.org/abs/2610.21641), arXiv:2610.21641v1 (15 October 2026), Theorem 1.2, equation (1.18). [Primary manuscript](https://arxiv.org/pdf/2610.21641v1).

## Status review

**Resolution update (3 November 2026):** Affirmative proof. Huang–Zhou–Zou’s Theorem 1.2, equation (1.18), asserts a Hölder seminorm bound depending only on dimension and the L² norm of the gradient, for stable classical solutions with arbitrary locally Lipschitz sign-changing reaction laws in every dimension from two through nine. Averaging the Hölder difference estimate over a second point in the half-ball and applying Cauchy–Schwarz bounds the supremum by the L² norm of the function plus that gradient norm. This gives exactly the displayed W¹,² bound in dimensions 6–9, with a constant independent of the reaction law. The proof uses the seminorm estimate (1.18); the different full Hölder norm estimate (1.19), whose right side contains the negative part of the reaction, is not needed.

[Proof](https://arxiv.org/pdf/2610.21641v1) · [Dated statement comparison and elementary mean argument](../research/solution-status-audit-2026-11-03/lane-b/439.json). The theorem hypotheses and current announcement were checked.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

The survey identifies the missing interior boundedness estimate in dimensions 6–9 when f may change sign. The Peng–Zhang–Zhou theorem handles dimensions at most five with a W1,2 norm. Review-date searches for sign-changing stable solutions and later higher-dimensional interior estimates found no proof of the displayed universal bound. Entire-space Liouville theorems under special assumptions on the zeros of f have different hypotheses.
