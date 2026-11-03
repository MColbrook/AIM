# 743. Uniqueness of crowded active-particle diffusion from degenerate initial data

**Area:** Degenerate diffusion; active matter
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$ and $`\xi=(x,\theta)\in\mathbb T^2\times\mathbb T`$. Put $`e(\theta)=(\cos\theta,\sin\theta)`$. Fix the spatial and angular diffusion coefficients and the Péclet number to one. For a nonnegative density $`f`$, write

```math
\rho(t,x)=\int_{\mathbb T} f(t,x,\theta)\,d\theta.
```

Consider the periodic initial-value problem

```math
\partial_t f+\nabla_x\cdot[(1-\rho)f e(\theta)]
 =\nabla_x\cdot[(1-\rho)\nabla_x f+f\nabla_x\rho]+\partial_\theta^2 f,
 \qquad f(0)=f_0.
```

For every nonnegative $`f_0\in L^q(\mathbb T^3)`$, for some $`q>1`$, suppose

```math
0\leq\rho_0:=\int_{\mathbb T}f_0\,d\theta\leq1\quad\hbox{a.e.},
\qquad 0<\int_{\mathbb T^2}\rho_0\,dx<|\mathbb T^2|.
```

Must any two weak solutions with this datum be equal almost everywhere? No positive uniform lower bound on $`1-\rho_0`$ is imposed; $`\rho_0=1`$ on a proper set of positive measure is allowed.

Here the weak class is fixed as follows. On every finite interval $`(0,T)`$, require

```math
\begin{gathered}
f\geq0,\quad f\in L^3((0,T)\times\mathbb T^3),\quad
\partial_\theta\sqrt f\in L^2((0,T)\times\mathbb T^3),\\
\partial_t f\in L^{6/5}(0,T;W^{-1,6/5}(\mathbb T^3)),\quad
0\leq\rho\leq1,\quad
\partial_t\rho\in L^2(0,T;H^{-1}(\mathbb T^2)),\\
\nabla_x\sqrt{1-\rho}\in L^2((0,T)\times\mathbb T^2),\quad
\sqrt{1-\rho}\nabla_x\sqrt f\in L^2((0,T)\times\mathbb T^3).
\end{gathered}
```

The final weighted derivative can be defined without assuming an unweighted spatial derivative of $`\sqrt f`$: set $`a=\sqrt{1-\rho}`$, $`g=\sqrt f`$, require $`w=ag\in L^2(0,T;H^1(\mathbb T^3))`$, and interpret $`a\nabla_xg=\nabla_xw-g\nabla_xa`$. The product $`g\nabla_xa`$ lies in $`L^2`$, because $`\int g^2\,d\theta=\rho\leq1`$. Accordingly the spatial flux is interpreted as

```math
F=2w\nabla_xw+2f\nabla_x\rho
  =(1-\rho)\nabla_x f+f\nabla_x\rho,
\qquad \partial_\theta f=2\sqrt f\,\partial_\theta\sqrt f.
```

Require the initial trace $`f(t)\to f_0`$ in $`W^{-1,6/5}(\mathbb T^3)`$ and the identity, for every smooth periodic $`\varphi`$ with compact support in $`[0,T)`$,

```math
\int_0^T\!\int f\,\partial_t\varphi+\int f_0\varphi(0)
 +\int_0^T\!\int(1-\rho)f e(\theta)\cdot\nabla_x\varphi
 =\int_0^T\!\int F\cdot\nabla_x\varphi
  +\int_0^T\!\int\partial_\theta f\,\partial_\theta\varphi.
```

All space-angle integrals here are over $`\mathbb T^3`$. This is the finite-interval weighted Sobolev class of the original existence theory and the corrected 2025 paper. The 2026 regularization theorem uses a local-in-time notation for some derivatives; the question here retains the stated full $`(0,T)`$ bounds.

## Application

The equation describes self-propelled particles whose motion slows in crowded regions. Uniqueness would ensure that a given initial distribution determines one continuum evolution, including configurations initially at maximal local occupancy.

## References

1. M. Burger and S. M. Schulz, *Well-posedness and stationary states for a crowded active Brownian system with size-exclusion*, Discrete and Continuous Dynamical Systems **45**(8) (2025), 2882–2915. [Article](https://doi.org/10.3934/dcds.2025006); [author version](https://arxiv.org/abs/2309.17326). Definition 1.1, Theorems 1–2 and §5 fix the weak class and the zero-Péclet special case.
2. L. C. B. Alasio and S. M. Schulz, *Regularity and uniqueness for a model of active particles with angle-averaged diffusions*, NoDEA **32**, 70 (2025), [article](https://doi.org/10.1007/s00030-025-01077-z), with [correction](https://doi.org/10.1007/s00030-025-01139-2). Use the [corrected author version 2501.11488v3](https://arxiv.org/abs/2501.11488v3), Definition 3.1 and Theorem 2 and the paragraph immediately following it.
3. S. M. Schulz, *Instantaneous regularisation via Harnack-type methods for a degenerate non-local equation* (6 October 2026 preprint), [2610.08434v1](https://arxiv.org/abs/2610.08434v1). Introduction, Definitions 2.1–2.2, Theorem 1 and Remark 3.1.

## Status review


**Known cases:** The corrected regularity-and-uniqueness paper still uses nondegenerate regular initial data. Positive-time smoothness in the later rough-data announcement has a lower-parabolicity bound degenerating at zero and does not establish uniqueness from the prescribed degenerate initial trace.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The corrected regularity-and-uniqueness paper still uses nondegenerate regular initial data. Positive-time smoothness in the later rough-data announcement has a lower-parabolicity bound degenerating at zero and does not establish uniqueness from the prescribed degenerate initial trace.

Additional comparison sources: [comparison source 1](https://doi.org/10.3934/dcds.2025006); [comparison source 2](https://arxiv.org/abs/2309.17326); [comparison source 3](https://doi.org/10.1007/s00030-025-01077-z); [comparison source 4](https://doi.org/10.1007/s00030-025-01139-2); [comparison source 5](https://arxiv.org/abs/2501.11488v3); [comparison source 6](https://arxiv.org/abs/2610.08434v1); [comparison source 7](https://arxiv.org/abs/2512.17649v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Checked 17 October 2026.** Global weak existence is known. The corrected 2025 uniqueness theorem assumes $`f_0\in L^2`$, $`\rho_0\in H^1`$ and $`\mathrm*{ess\,sup}\rho_0<1`$, in addition to its regular-data conditions. It explicitly leaves less restrictive initial-data uniqueness under investigation. The 6 October 2026 announcement proves that every solution in the stated class with nonsaturated total mass is smooth for positive times, but explicitly retains general uniqueness/nonuniqueness as open. Its lower parabolicity bound degenerates as $`t\downarrow0`$, so positive-time smoothness alone does not identify two evolutions with the same rough initial trace.

The simpler semilinear model with full spatial Laplacian, and results for zero activity or near-constant strong solutions, do not settle this target. The independent selected-primary audit checked the weighted flux, initial trace, existence class and the scope of the corrected and newer theorems. The 2025 stability preprint [arXiv:2512.17649v1](https://arxiv.org/abs/2512.17649v1) treats linearized or modified models and does not prove this nonlinear initial-trace uniqueness.

All-status AIM/OpenAI and FURTHER comparisons found no equivalent problem. The closest AIM entries concern finite-species cross-diffusion, first-order entropy solutions, linear control or kinetic collision equations, with different equations and solution classes. The fresh 186-page Prove2Me description scan returned no context matching the six target-specific aliases; generic mission proof bodies have not been exhaustively compared.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/active-brownian-weak-uniqueness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-active-brownian-weak-uniqueness-review.json), [fresh catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/active-brownian-prove2me0093-comparison.json) and [stability-paper check](../FURTHER_problems/_tracking/parallel/continuum/active-brownian-stability2512-status-comparison.json) record the exact passages and dated searches. These checks found no matching full result or announcement. The published 2025 DCDS body remains a parity gap; the original author version was read in full and the corrected NoDEA and 2026 passages were checked as recorded. The newer preprints were used for current status, not as discoveries within the January 2022 arXiv cutoff. No independent certification of every cited proof is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f69d19c688548b6b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
