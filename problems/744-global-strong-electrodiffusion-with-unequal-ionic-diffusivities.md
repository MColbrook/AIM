# 744. Global strong electrodiffusion with unequal ionic diffusivities

**Area:** Electrochemistry and fluid transport
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be any bounded connected domain with smooth boundary. Fix an integer $`m\ge3`$, charges $`z_i\in\{-1,1\}`$ with both signs present, and arbitrary positive constants $`D_i,\epsilon,\nu,K`$. The diffusivities $`D_i`$ need not be equal.

Prescribe smooth time independent boundary concentrations $`\gamma_i>0`$ and voltage $`W`$. For smooth strictly positive initial concentrations $`c_{i,0}`$ with $`c_{i,0}|_{\partial\Omega}=\gamma_i`$, and a smooth divergence free initial velocity $`u_0`$ vanishing on the boundary, consider

```math
\begin{aligned}
\partial_t c_i+u\cdot\nabla c_i
 &=D_i\nabla\cdot(\nabla c_i+z_ic_i\nabla\Phi),\qquad i=1,\ldots,m,\\
-\epsilon\Delta\Phi&=\rho:=\sum_{i=1}^m z_i c_i,\\
\partial_tu-\nu\Delta u+\nabla p&=-K\rho\nabla\Phi,\qquad \nabla\cdot u=0,
\end{aligned}
```

with $`c_i=\gamma_i`$, $`\Phi=W`$ and $`u=0`$ on $`\partial\Omega`$.

Does the unique local strong solution extend to every finite time? Here, writing

```math
V=\{v\in H^1_0(\Omega;\mathbb R^3):\nabla\cdot v=0\},
```

require, for every $`T<\infty`$,

```math
\begin{aligned}
c_i&\ge0,\qquad
c_i\in L^\infty(0,T;H^1(\Omega))\cap L^2(0,T;H^2(\Omega)),\\
u&\in L^\infty(0,T;V)\cap L^2(0,T;H^2(\Omega;\mathbb R^3)\cap V).
\end{aligned}
```

The equations hold in distributions, boundary conditions in the trace sense, and initial data as time traces. At each time the displayed Dirichlet Poisson problem determines $`\Phi`$; pressure is defined up to a function of time. No bound uniform as $`T\to\infty`$ or $`\epsilon\to0`$ is requested.

The source explicitly raises global smoothness for the general three dimensional Stokes coupling. Its Theorem 2 gives the continuation criterion $`\int_0^T\|\rho(t)\|_{L^2}^4\,dt<\infty`$. Theorems 3 and 4 establish global existence for two oppositely charged species with arbitrary diffusivities, and for arbitrarily many unit charge species with a common diffusivity. The question above retains unit charges and asks to remove the common diffusivity restriction for mixtures.

## Application

Different ions diffuse at different rates. Concentration reservoirs and applied boundary voltages can drive electrochemical transport far from equilibrium, including electroconvective instability. The question asks whether this standard low Reynolds number model continues to determine a regular evolution for arbitrarily large smooth data.

## References

1. P. Constantin, M. Ignatova and F.-N. Lee, *Nernst–Planck–Navier–Stokes Systems far from Equilibrium*, Archive for Rational Mechanics and Analysis **240** (2021), 1147–1168. [DOI](https://doi.org/10.1007/s00205-021-01630-x), [pinned preprint](https://arxiv.org/abs/2008.10462v1), [final author manuscript](https://web.math.princeton.edu/~const/cilfin.pdf). Introduction, second page; Definition 1 and Theorems 1–4. Both complete author versions were read; subscription publisher body parity was not established.
2. E. Abdo and M. Ignatova, *Long time dynamics of Nernst–Planck–Navier–Stokes systems*, Journal of Differential Equations **379** (2024), 794–828. [DOI](https://doi.org/10.1016/j.jde.2023.10.040). The periodic setting treats small data in arbitrary dimension and large data in dimension two; this does not cover the displayed three dimensional reservoir problem.

## Status review


**Known cases:** The inspected Constantin-Ignatova-Lee reservoir theorem treats two oppositely charged species; its displayed estimates use c1 and c2. Equal-diffusivity mixtures and two-dimensional Couette stability do not settle three-dimensional mixtures with at least three species and arbitrary diffusivities.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The inspected Constantin-Ignatova-Lee reservoir theorem treats two oppositely charged species; its displayed estimates use c1 and c2. Equal-diffusivity mixtures and two-dimensional Couette stability do not settle three-dimensional mixtures with at least three species and arbitrary diffusivities.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00205-021-01630-x); [comparison source 2](https://arxiv.org/abs/2008.10462v1); [comparison source 3](https://web.math.princeton.edu/~const/cilfin.pdf); [comparison source 4](https://doi.org/10.1016/j.jde.2023.10.040); [comparison source 5](https://arxiv.org/abs/2404.16433v5). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 16 October 2026. No matching complete proof, counterexample or announced full resolution was located. The complete Prove2Me listing comparison found no target aliases. All statuses of AIM, the OpenAI announcement index and the current FURTHER list were also compared.

X. Xu's [January 2026 preprint revision](https://arxiv.org/abs/2404.16433v5), *Global existence of a strong solution to the initial value problem for the Nernst–Planck–Navier–Stokes system in high space dimensions*, announces a whole-space result with every ionic diffusivity equal to one. It does not treat the displayed unequal-diffusivity reservoir problem. Two-dimensional, one-dimensional, small-data and global weak-solution results likewise have different scope.

The [review packet](../FURTHER_problems/_tracking/parallel/continuum/multi-ion-stokes-global-review.json) records exact primary-source extents, current announcement comparisons, nearest duplicate targets and publisher-version access limits. This is a dated literature check, not a guarantee that no proof exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-00526cc3d22a73c4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
