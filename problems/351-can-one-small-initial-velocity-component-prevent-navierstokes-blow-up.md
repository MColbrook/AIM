# 351. Can one small initial velocity component prevent Navier–Stokes blow-up?

**Area:** Fluid mechanics and nonlinear partial differential equations
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Consider the unforced incompressible Navier–Stokes equations on $`\mathbb R^3`$, with viscosity one:

```math
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad u(0)=u_0.
```


Use the initial-data class of Chemin–Zhang–Zhang's Theorem 1.3: $`u_0\in\dot H^{1/2}(\mathbb R^3)^3`$ is divergence-free and $`\nabla\times u_0\in L^{3/2}(\mathbb R^3)\cap L^2(\mathbb R^3)`$. Let $`T_*`$ be the maximal lifespan of its Fujita–Kato solution in

```math
C([0,T_*);\dot H^{1/2})\cap L^2_{\mathrm{loc}}([0,T_*);\dot H^{3/2}).
```


**Is there a universal $`\varepsilon>0`$ such that $`T_*=\infty`$ whenever some fixed unit vector $`e\in\mathbb R^3`$ satisfies $`\|u_0\cdot e\|_{H^{1/2}(\mathbb R^3)}<\varepsilon`$?** There is no smallness assumption on the other components.

Here $`H^{1/2}`$ is the inhomogeneous Sobolev space. This retains the norm printed in the source's final introduction paragraph; the adjacent solution spaces are homogeneous and carry dots. The condition concerns the initial velocity, with no later-time smallness assumed.

This entry records the question in the source's $`\mathcal V^2`$ working class. The question's paragraph does not separately repeat that restriction.

## Application

The question tests whether one initially weak velocity direction can prevent singularity formation in a fully three-dimensional viscous flow, even when the other velocity components are large.

## Known results and scope

The source proves criteria using one component throughout a time interval. Barker, Prange and Tan show that a component initially equal to zero can grow substantially; their discussion explicitly distinguishes this norm inflation from a blow-up counterexample to the question.

A 2026 preprint by Yu studies conditional local regularity from a small space-time component quantity and additional structural hypotheses. It does not announce this unconditional initial-data result.

## References

1. J.-Y. Chemin, P. Zhang and Z. Zhang, [*On the critical one component regularity for 3-D Navier–Stokes system: general case*](https://arxiv.org/abs/1509.01952v1), *Archive for Rational Mechanics and Analysis* **224** (2017), 871–905, [DOI:10.1007/s00205-017-1089-0](https://doi.org/10.1007/s00205-017-1089-0). Theorems 1.1 and 1.3, and final introduction paragraph on native arXiv p. 2; the later paper cites published p. 873.
2. T. Barker, C. Prange and J. Tan, [*On Symmetry Breaking for the Navier–Stokes Equations*](https://doi.org/10.1007/s00220-023-04897-1), *Communications in Mathematical Physics* **405** (2024), article 25. Question (Q), Theorems A/A′ and ensuing discussion in the [arXiv body](https://arxiv.org/html/2302.02836v3).
3. R. Yu, [*Strict 2.5D Shadows for One-Component Navier–Stokes Regularity*](https://arxiv.org/abs/2606.11720), preprint (2026), §1 and Theorem F.2.

## Status review

The source's native formula, working class, latest arXiv versions and later-result scopes were checked. Bounded theorem, counterexample and announcement searches found no resolution of this initial-data question; AIM and admitted FURTHER semantic searches found no matching entry. The [audit](../FURTHER_problems/_tracking/ns-small-initial-component-review-2026-10-23.json) records the published-text access limits and exact source-page evidence. No complete-paper or independent later-proof certification is claimed.


### Online recheck, 2026-10-30

One-component space-time criteria and symmetry-breaking/norm inflation do not answer the unconditional initial-component question. General blowup announcements do not assert arbitrarily small critical H1/2 size of one initial component in this working class; modified, forced or anisotropically dissipative equations have different hypotheses.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1509.01952); [status source 2](https://doi.org/10.1007/s00220-023-04897-1); [status source 3](https://arxiv.org/abs/2606.11720). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-0799eb2a69ecf3fa** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
