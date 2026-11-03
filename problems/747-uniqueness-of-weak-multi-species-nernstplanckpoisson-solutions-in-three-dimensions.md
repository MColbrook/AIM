# 747. Uniqueness of weak multi-species Nernst–Planck–Poisson solutions in three dimensions

**Area:** Electrochemistry and energy storage
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected open set with $`C^2`$ boundary, and let $`P\ge1`$ and $`z_1,\ldots,z_P\in\mathbb Z`$. For each finite $`T>0`$, let the measurable scalar diffusivities satisfy

```math
0<d_*(T)\le d_i(t,x)\le d^*(T)<\infty
\quad\text{a.e. on }Q_T=(0,T)\times\Omega.
```

They may differ between species and depend on space and time. Let $`f_i(t,x,y)`$ be continuous on $`[0,\infty)\times\overline\Omega\times[0,\infty)^P`$, continuously differentiable in $`y`$ with continuous derivatives on that set, uniformly bounded, and quasi-positive: $`f_i(t,x,y)\ge0`$ whenever $`y_i=0`$. Fix nonnegative $`\tau\in L^\infty(\partial\Omega)`$ with $`\int_{\partial\Omega}\tau\,dS>0`$, time-independent $`\xi\in L^q(\partial\Omega)`$ for some $`q>2`$, and nonnegative $`c_i^0\in L^p(\Omega)`$ for some finite $`p\ge2`$.

Consider the system, with physical constants scaled to one,

```math
\partial_t c_i-\nabla\cdot\bigl(d_i(\nabla c_i+z_i c_i\nabla\Phi)\bigr)=f_i(t,x,c),
\qquad -\Delta\Phi=\sum_{i=1}^Pz_i c_i,
```

with no-flux boundary conditions for each concentration and $`\partial_\nu\Phi+\tau\Phi=\xi`$ for the potential.

Here a weak solution means $`c_i\ge0`$ and, for every finite $`T>0`$,

```math
c_i\in C([0,T];L^1(\Omega))\cap L^1(0,T;W^{1,3/2}(\Omega)),\qquad c_i(0)=c_i^0,
```

```math
\Phi\in L^\infty(0,T;H^1(\Omega))\cap L^2(0,T;H^2_{\rm loc}(\Omega))
\cap C([0,T];L^r(\Omega))\quad\text{for every }1\le r<6,
```

and $`F_i=d_i(\nabla c_i+z_i c_i\nabla\Phi)\in L^1(Q_T;\mathbb R^3)`$. The equations and boundary conditions mean

```math
\int_{Q_T}\bigl(-c_i\partial_t\psi+F_i\cdot\nabla\psi\bigr)
=\int_\Omega c_i^0\psi(0)+\int_{Q_T}f_i(t,x,c)\psi
```

for every smooth $`\psi`$ on $`[0,T]\times\overline\Omega`$ with $`\psi(T)=0`$, and

```math
\int_\Omega\nabla\Phi(t)\cdot\nabla\varphi
+\int_{\partial\Omega}(\tau\Phi(t)-\xi)\varphi
=\int_\Omega\left(\sum_{i=1}^Pz_i c_i(t)\right)\varphi
```

for every smooth $`\varphi`$ on $`\overline\Omega`$, for almost every $`t`$. Smooth tests may equivalently be restrictions of ambient smooth functions.

**For every such set of data, is there at most one weak solution in this class?** Equality of potentials is literal: the nonzero nonnegative Robin coefficient fixes the additive constant. No equality of diffusivities, restriction to two species, smallness, or additional boundedness of the concentrations is assumed.

## Application

These equations describe diffusion and electric migration of several ionic species in a dilute electrolyte with a charged boundary. Uniqueness at the regularity supplied by global existence would make the resulting weak evolution determined by the initial concentrations and boundary data.

## References

1. D. Bothe, A. Fischer, M. Pierre and G. Rolland, *Global existence for diffusion–electromigration systems in space dimension three and higher*, Nonlinear Analysis **99** (2014), 152–166. [DOI](https://doi.org/10.1016/j.na.2013.12.015), [primary arXiv v1](https://arxiv.org/abs/1311.1652v1). The explicit uniqueness question is on PDF p. 2; assumptions (5)–(7), Theorems 1–2 and weak identities (8)–(9) specify the class used above.
2. D. Hömberg, R. Lasarzik and L. Plato, *Existence of suitable weak solutions to an anisotropic electrokinetic flow model*, Journal of Differential Equations **428** (2025), 511–584. [DOI](https://doi.org/10.1016/j.jde.2025.02.018), [July 2024 revised primary preprint](https://www.wias-berlin.de/preprint/3104/wias_preprints_3104_20240726.pdf). The published introduction explicitly retains uniqueness for the multi-species, variable-diffusivity, bounded-reaction weak NPP setting as open. Its own anisotropic fluid-coupled model and weak–strong uniqueness discussion do not establish uniqueness in the class above.

3. R. Hu, Q. Lin and Q. Peng, *Onsager-Type Energy Equality and Prodi–Serrin Uniqueness for Electrodiffusion Systems*, [arXiv:2607.00225v1](https://arxiv.org/html/2607.00225v1), §4, Definition4.1 and Theorem4.3. The abstract metadata uses the title ending *Nernst–Planck Fluid Systems*; the shared arXiv identifier fixes the source.

## Status review


**Known cases:** The target allows arbitrarily many species, time-space measurable diffusivities, Robin potential data and the broad original weak class in dimension three. The current suitable-weak-solution paper explicitly retains this uniqueness gap; weak-strong and smoother-coefficient two-species results do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target allows arbitrarily many species, time-space measurable diffusivities, Robin potential data and the broad original weak class in dimension three. The current suitable-weak-solution paper explicitly retains this uniqueness gap; weak-strong and smoother-coefficient two-species results do not cover it.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.na.2013.12.015); [comparison source 2](https://arxiv.org/abs/1311.1652v1); [comparison source 3](https://doi.org/10.1016/j.jde.2025.02.018); [comparison source 4](https://www.wias-berlin.de/preprint/3104/wias_preprints_3104_20240726.pdf); [comparison source 5](https://arxiv.org/html/2607.00225v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Global existence in the displayed class is Theorem 2 of the first reference, combined with Theorem 1. The question concerns uniqueness among arbitrary solutions in that stated weak class, rather than uniqueness for a prescribed electric field or for the regularized problem. The first reference proves the latter auxiliary statements; they do not settle the coupled weak system. Later strong-solution results under equal diffusivities, restricted species, smoother coefficients, stronger data or different boundary conditions do not give this assertion automatically.

Current searches on 17 October 2026 have not located a matching proof or counterexample announcement. Independent selected-primary review passed, and the recorded catalogue comparison found no equivalent question at its stated extent.

The complete2014published body has not been compared with the pinned20page preprint. Nearby uniqueness theorems use narrower dimensions, coefficients, boundary conditions or solution classes, as detailed in the review packet.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/npp-weak-uniqueness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-npp-weak-uniqueness-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/npp-prove2me0129-review.json) and [coordinator review](../FURTHER_problems/_tracking/npp-coordinator-review-2026-10-17.json) give exact source coverage and search limitations.

The 2026 result in reference3 treats periodic two-species, equal-constant-diffusion equations without reactions, in a Leray–Hopf energy class with an additional velocity criterion. It does not establish arbitrary-species Robin weak uniqueness above. Its fluid momentum equation also prevents embedding every pure NPP evolution by simply setting the velocity to zero. The [additional scope check](../FURTHER_problems/_tracking/parallel/continuum/npp-hu-lin-peng2026-scope-review.json) records the selected primary statements read.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a52878be70077b5a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
