# 162. Does fixed noise select a unique inviscid fluid law?

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`H`$ be the mean-zero real divergence-free subspace of $`L^2(\mathbb T^2;\mathbb R^2)`$, where $`\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2`$. Use the real sine/cosine orthonormal basis $`e_j`$ of source Eq.(1.3), indexed by $`j\in\mathbb Z^2\setminus\{0\}`$. Fix real coefficients $`b_j\ne0`$ with $`\sum_j|j|^2b_j^2<\infty`$, and independent standard Brownian motions $`\beta_j`$. For each $`\nu>0`$, let $`\mu_\nu`$ be the unique stationary velocity law of
```math
du+[(u\cdot\nabla)u-\nu\Delta u+\nabla p]dt
 =\sqrt\nu\sum_j b_j e_j\,d\beta_j,
\qquad\nabla\cdot u=0.
```

Must $`\mu_\nu`$ converge weakly in $`\mathcal P(H)`$ as $`\nu\downarrow0`$ for every such fixed noise? Alternatively, construct one fixed coefficient family and two viscosity sequences with different limit laws. The covariance remains fixed; no deterministic force or damping is added.

## Application

This asks whether a fixed small-forcing protocol selects reproducible inviscid fluid statistics.

## References

1. S. Kuksin and A. Shirikyan, [*Rigorous results in space-periodic two-dimensional turbulence*](https://arxiv.org/html/1712.09830), *Physics of Fluids* **29** (2017), 125106. [DOI](https://doi.org/10.1063/1.4996545). Equations (1.3)–(1.5), (5.1), (5.6), Theorem 5.1 and Open Problem 4(a).
2. B. Ferrario, [*On 2D Eulerian limits à la Kuksin*](https://doi.org/10.1016/j.jde.2022.09.034), *Journal of Differential Equations* **342** (2023), 1–20, Section 5 and Theorem 5.1.
3. A.-S. Sznitman and K. Widmayer, [*An inviscid limit to an effective energy-enstrophy diffusion process*](https://arxiv.org/abs/2602.15805), v2 (2026), Introduction and Section 5.

## Status review


**Known cases:** Subsequential Euler-invariant limits are known. Dependence on a changed viscosity exponent and effective finite-dimensional observable dynamics do not settle sequence independence of the full velocity law with one fixed noise covariance and the fixed Laplacian.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Subsequential compactness and nontrivial Euler-invariant limits are known. The source asks about sequence dependence and expects it can occur. Ferrario proves dependence on the viscosity exponent, which leaves the fixed-operator question. The 2026 finite-dimensional stirred model controls energy/enstrophy observables rather than this full velocity law.

The [coordinating review](../FURTHER_problems/_tracking/focused-Kuksin-inviscid-stationary-limit-J154-C188-C-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, current-resolution, announcement and semantic duplicate checks, with independent model review. The archived formulation is used without asserting full published-body parity. Bounded checks do not prove continued openness.


### Online recheck, 2026-10-30

Subsequential Euler-invariant limits are known. Dependence on a changed viscosity exponent and effective finite-dimensional observable dynamics do not settle sequence independence of the full velocity law with one fixed noise covariance and the fixed Laplacian.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1712.09830); [status source 2](https://doi.org/10.1016/j.jde.2022.09.034); [status source 3](https://arxiv.org/abs/2602.15805). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-0614d0fd64c7bb4a** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
