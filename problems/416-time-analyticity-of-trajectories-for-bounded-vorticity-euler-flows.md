# 416. Time analyticity of trajectories for bounded-vorticity Euler flows

**Area:** Ideal fluids and Lagrangian regularity
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^2=\mathbb R^2/\mathbb Z^2`$. For any real $`\omega_0\in L^\infty(\mathbb T^2)`$ with $`\int_{\mathbb T^2}\omega_0=0`$, let $`\omega,u`$ be the unique global Yudovich solution of

```math
\partial_t\omega+u\cdot\nabla\omega=0,\qquad
\Delta\psi=\omega,\qquad \int_{\mathbb T^2}\psi=0,\qquad
u=\nabla^\perp\psi,\qquad \nabla^\perp=(-\partial_2,\partial_1),
```

with $`\omega(0)=\omega_0`$. This is the mean-zero incompressible Euler flow, with $`\omega\in L^\infty(\mathbb R\times\mathbb T^2)`$ and $`u\in C(\mathbb R;L^2)`$; vorticity has its usual strong $`L^p`$ initial trace for every finite $`p`$.

The continuous, spatially log-Lipschitz representative of $`u`$ defines the unique flow

```math
\frac{d}{dt}\Phi_t(x)=u(t,\Phi_t(x)),\qquad \Phi_0(x)=x.
```

For every such datum and every $`x\in\mathbb T^2`$, is $`t\mapsto\Phi_t(x)`$ real analytic at every $`t_0\in\mathbb R`$? Precisely, a local lift of this torus-valued path to $`\mathbb R^2`$ should equal a convergent real power series near $`t_0`$. Its radius may depend on the datum, particle and time. A counterexample in this class also resolves the question.

## Application

This asks whether trajectories of individual fluid tracers have convergent time Taylor expansions even when the vorticity is merely bounded. It does not require spatial analyticity of the flow.

## References

- B. Khesin, G. Misiołek and A. Shnirelman, *Geometric Hydrodynamics in Open Problems*, ARMA **247** (2023), article15, Remark6.2, p15: [published author-hosted copy](https://www.math.utoronto.ca/khesin/papers/Problems_in_GHD_ARMA.pdf), [DOI](https://doi.org/10.1007/s00205-023-01848-x). The bounded-vorticity question is stated explicitly; the formulation above specializes it to the flat torus.
- P. Gamblin, *Système d’Euler incompressible et régularité microlocale analytique*, AIF **44** (1994), 1449–1475, TheoremsA–B: [official PDF](https://aif.centre-mersenne.org/item/10.5802/aif.1441.pdf).
- F. Sueur, *Smoothness of the trajectories of ideal fluid particles with Yudovich vorticities in a planar bounded domain*, JDE **251** (2011), 3421–3449, Theorem1: [author version](https://arxiv.org/abs/1004.1718).
- T. D. Drivas and T. M. Elgindi, *Singularity formation in the incompressible Euler equation in finite and infinite time*, EMS Surveys **10** (2023), 1–100, Remark2.7, p9: [published PDF](https://ems.press/content/serial-article-files/37045).

- M. Hernandez, *Mechanisms of Lagrangian analyticity in fluids*, ARMA **233** (2019), 513–598, Corollary 3.9 and Section 3.3: [author version](https://arxiv.org/abs/1705.06238). The inspected torus theorem requires Hölder vorticity.

## Status review

The published 2023 sources explicitly retain the question. Known bounded-vorticity results give Gevrey regularity, which does not imply analyticity. Analyticity theorems for Hölder vorticity or regular vortex patches impose extra hypotheses. Bounded searches on 19October2026 located no matching resolution; an independent selected review and the all-status catalogue description check passed. The coordinator’s final comparison is pending.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/yudovich-trajectories-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-yudovich-trajectories-review.json), [semantic comparison](../FURTHER_problems/_tracking/yudovich-trajectories-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/yudovich-trajectories-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/yudovich-trajectories-coordinator-review-2026-10-19.json) record evidence and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

Yudovich existence and smooth/Gevrey trajectories are known, but not their real analyticity for every bounded vorticity. Holder-vorticity, regular-vortex-patch and different phase-space analyticity theorems add hypotheses.

Comparators and current-status sources: [status source 1](https://www.math.utoronto.ca/khesin/papers/Problems_in_GHD_ARMA.pdf); [status source 2](https://arxiv.org/abs/1004.1718); [status source 3](https://arxiv.org/abs/2509.21121). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-03efb3c13aa58a87** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
