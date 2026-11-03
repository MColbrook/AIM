# 1052. Global bounded evolution for the local kinetic Vicsek equation

**Area:** Kinetic equations and collective motion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Write $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$, and use the probability measure $`dm(\theta)=d\theta/(2\pi)`$ on the orientation circle. For $`x\in\mathbb R^2`$, set

```math
e(\theta)=(\cos\theta,\sin\theta),\qquad e^\perp(\theta)=(-\sin\theta,\cos\theta),\qquad
J_f(t,x)=\int_{\mathbb T}e(\eta)f(t,x,\eta)\,dm(\eta).
```

Fix transport speed, angular diffusion and alignment strength equal to one. Consider the local, unnormalized dipolar alignment equation

```math
\partial_t f+e(\theta)\cdot\nabla_x f+
\partial_\theta\big[(J_f\cdot e^\perp(\theta))f\big]
=\partial_\theta^2f.
```

For every nonnegative $`f_0\in C_c^\infty(\mathbb R^2\times\mathbb T)`$, does there exist a single solution on $`[0,\infty)`$ which, for every finite $`T>0`$, satisfies

```math
f\ge0,\qquad
f\in C([0,T];L^1\cap L^2)\cap L^\infty((0,T)\times\mathbb R^2\times\mathbb T),
\qquad \partial_\theta f\in L^2((0,T)\times\mathbb R^2\times\mathbb T),
```

has $`f(0)=f_0`$ in $`L^1\cap L^2`$, and preserves $`\int f\,dx\,dm=\int f_0\,dx\,dm`$? The spaces in the display use $`dx\,dm`$. Require the distributional identity

```math
\int_0^T\!\int f\left[\partial_t\varphi+e\cdot\nabla_x\varphi+
(J_f\cdot e^\perp)\partial_\theta\varphi\right]\,dx\,dm\,dt
+\int f_0\varphi(0)\,dx\,dm
=\int_0^T\!\int \partial_\theta f\,\partial_\theta\varphi\,dx\,dm\,dt
```

for all smooth test functions compactly supported in $`[0,T)\times\mathbb R^2`$ and periodic in $`\theta`$.

The bound may depend on $`T`$ and $`f_0`$. There is no smallness condition on the datum, its mass or its spatial density. The alignment uses $`J_f(t,x)`$ at the same spatial point, without a spatial convolution or division by $`|J_f|`$.

Local bounded existence and uniqueness are available. Thus the question asks whether the bounded evolution can always be continued through every finite time. A counterexample with a finite maximal bounded-existence time would also resolve it.

## Application

The equation models agents moving at fixed speed while their directions diffuse and turn toward the local mean direction. Global bounded evolution would justify this local alignment description for arbitrarily concentrated smooth populations, beyond the small perturbations for which stability theory is available.

## References

1. Marc Briant and Nicolas Meunier, *Well-posedness for systems of self-propelled particles*, Kinetic and Related Models **17** (2024), 659–673. [Publisher](https://www.aimsciences.org/article/doi/10.3934/krm.2023036); [author manuscript](https://arxiv.org/abs/2305.05336v1), equations(1.5)–(1.6), Theorem1.1 and the discussion following Proposition1.2, physical pages2–4. Their general local kernel class includes the displayed dipolar alignment instance; their sign convention puts the interaction divergence on the right, so this instance uses $`k(\omega,\omega_*)=-\omega_*/(2\pi)`$ with their unnormalized circle area measure.
2. Émeric Bouin and Amic Frouvelle, *Quantitative stability of constant equilibria in a non-linear alignment model of self-propelled particles* (2026). [Primary text](https://arxiv.org/html/2604.05927v1), equation(1.1), the normalized sphere measure after(1.2), Theorems1.1–1.3 and introductory discussion. This fixes the physical alignment sign and proves global evolution near subcritical isotropic equilibria, while retaining unrestricted finite-time breakdown as a possibility.
3. Marc Briant, Antoine Diez and Sara Merino-Aceituno, *Cauchy theory for general kinetic Vicsek models in collective dynamics and mean-field limit approximations*, SIAM Journal on Mathematical Analysis **54** (2022), 1131–1168. [DOI](https://doi.org/10.1137/21M1405885); [author text](https://arxiv.org/abs/2004.00883), hypothesis(H1), Theorem2.4 and Remark2.5. Their global nonnormalized-kernel result assumes a bounded regular spatial kernel, which excludes the local Dirac kernel here.

## Status review


**Known cases:** The local unnormalized alignment is spatially pointwise and initial data are unrestricted in size. Near-equilibrium, nonlocal-kernel and normalized-moment theorems do not give global bounded evolution for this model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The local unnormalized alignment is spatially pointwise and initial data are unrestricted in size. Near-equilibrium, nonlocal-kernel and normalized-moment theorems do not give global bounded evolution for this model.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 primary source explicitly retains the unrestricted global question. Searches through 17 October 2026 found no theorem or announced finite-time counterexample for this exact local, angularly diffusive, unnormalized model and arbitrary smooth compact data. The statement is a precise two-dimensional instance of that question.

Global results for spatially homogeneous dynamics, normalized orientation $`J/|J|`$, bounded spatial observation kernels, or Vicsek–BGK relaxation use different equations. The 2025 Gu–He mixing results assume a smooth spatial influence function and parameter restrictions. The 2026 Bouin–Frouvelle theorem requires smallness around a subcritical constant equilibrium.

AIM074 concerns hard-sphere Boltzmann collisions and Euclidean velocities; AIM219 concerns axisymmetry of stationary Onsager minimizers; AIM377 concerns a unit-director fluid system. None is this local kinetic alignment problem. An independent selected-primary audit checked the alignment sign, probability measure, angular reduction, initial trace, weak identity and bounded continuation class. It also checked that finite-mass compact data do not automatically satisfy the newer small-perturbation theorem. The fresh 186-page catalogue scan returned no contexts for the six specified target aliases; this bounded comparison does not certify every mission proof.

The [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-vicsek-review.json), [fresh catalogue receipt](../FURTHER_problems/_tracking/parallel/continuum/vicsek-prove2me0095-comparison.json) and [coordinator status check](../FURTHER_problems/_tracking/coordinator-selected-status-2026-10-17.json) record the passages and dated searches. The original 18-page author text was read in full; the final 15-page 2024 publication remains a version-parity gap. The 2026 primary source provides the current explicit global-existence question, with selected rather than full-paper reading recorded. This later preprint supplies status information; discovery eligibility is through registered journal J158, independently of the arXiv cutoff. No matching complete resolution or announced counterexample was found in these checks.

[Detailed review packet](../FURTHER_problems/_tracking/parallel/continuum/vicsek-global-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9913d6e7ebf1497d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
