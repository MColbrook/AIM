# 453. Bourgain–Spencer accuracy for random elliptic media at finite contrast

**Area:** Stochastic homogenization; diffusion in heterogeneous media

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Let $`d\ge2`$. Let $`G=C_0*\xi`$, where $`\xi`$ is vector-valued spatial Gaussian white noise and $`C_0`$ is a smooth compactly supported matrix-valued kernel. Let $`a(x)=a_0(G(x))`$, with $`a_0\in C_b^1`$ taking symmetric matrix values satisfying $`\lambda I\le a_0\le I`$ for some $`\lambda>0`$. For deterministic $`f\in C_c^\infty(\mathbb R^d;\mathbb R^d)`$, let $`\nabla u_\varepsilon\in L^2`$ be the unique gradient solving

```math
-\nabla\cdot a(x/\varepsilon)\nabla u_\varepsilon=\nabla\cdot f.
```

Do there exist constant tensors $`A^1,\ldots,A^{2d}`$, depending only on the law of $`a`$, with $`A^1`$ positive definite, for which the following approximation holds? Define deterministic gradients recursively by

```math
-\nabla\cdot A^1\nabla v_1=\nabla\cdot f,
```



```math
-\nabla\cdot A^1\nabla v_n=\nabla\cdot\sum_{k=2}^n A^k_{j_1\cdots j_{k-1}}\partial_{j_1}\cdots\partial_{j_{k-1}}\nabla v_{n+1-k},\quad 2\le n\le2d,
```

where $`A^k_{j_1\cdots j_{k-1}}`$ is a $`d\times d`$ matrix and repeated indices are summed. With $`U_\varepsilon=\sum_{n=1}^{2d}\varepsilon^{n-1}v_n`$, is

```math
\|\mathbb E\nabla u_\varepsilon-\nabla U_\varepsilon\|_{L^2(\mathbb R^d)}\le C_{f,\eta}\varepsilon^{2d-\eta}\qquad(0<\varepsilon\le1)
```

valid for every $`f`$ and $`0<\eta<1`$? There is no small-contrast assumption on $`a`$. Constants may depend on its law and ellipticity.

## Application

A high-order deterministic equation for ensemble averages would improve predictions of effective transport beyond the accuracy available for individual random samples.

## References

1. M. Duerinckx, *Non-perturbative approach to the Bourgain–Spencer conjecture in stochastic homogenization*, J. Math. Pures Appl. **176** (2023), 183–225, Conjecture 1 and Definition 3.3. [Article](https://doi.org/10.1016/j.matpur.2023.06.005); [author manuscript](https://arxiv.org/abs/2102.06319).
2. M. Duerinckx, M. Lemm and F. Pagano, *On Bourgain's approach to stochastic homogenization*, Arch. Ration. Mech. Anal. **249**, 81 (2025), §2.3 and Remark 2.3. [Author manuscript](https://arxiv.org/abs/2406.09909).

## Status review

**Proposed resolution (2026-11-27, UTC):** Kaiwen Jin's [analytic manuscript](../research/solutions/453-bourgain-spencer-nonperturbative-homogenization/paper.pdf) claims the full estimate at every fixed ellipticity contrast, with a single family of tensors for all permitted data and losses. The [target comparison and review scope](../research/solutions/453-bourgain-spencer-nonperturbative-homogenization/target-comparison.md) map the proof to the original recursion and state the scope of the AI checks. The claim awaits independent mathematical review.

**Earlier literature check (2026-09-22):** Open in the literature checked at that date.

The statement specializes Conjecture 1 to smooth finite-range Gaussian-generated coefficients and spells out its higher-order proxy, avoiding an ill-posed truncated high-order PDE. The 2025 paper still requires small contrast and explicitly leaves the non-perturbative improvement open. Searches on 2026-09-22 for Bourgain–Spencer, non-perturbative ensemble averages, proofs and counterexamples, including the authors' publication lists, found no full finite-contrast resolution. The $`d-\eta`$ non-perturbative accuracy and contrast-dependent $`2d-\delta K-\eta`$ results do not give the assertion above.
