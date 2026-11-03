# 758. Arbitrary-friction incremental contact in three-dimensional isotropic elasticity

**Area:** Contact mechanics and variational inequalities
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected $`C^{1,1}`$ domain. Partition its boundary into disjoint relatively open parts $`\Gamma_U,\Gamma_T,\Gamma_C`$ whose closures cover $`\partial\Omega`$. Assume $`\Gamma_U`$ and $`\Gamma_C`$ have positive surface measure, $`\Gamma_C`$ has Lipschitz boundary as a boundary patch, and $`\mathrm{dist}(\Gamma_U,\Gamma_C)>0`$.

Write $`n`$ for the outward normal and $`v_n=v\cdot n`$, $`v_t=v-v_n n`$ for boundary traces. Put

```math
V=\{v\in H^1(\Omega;\mathbb R^3):\mathrm{Tr}v=0\text{ on }\Gamma_U\},
\qquad \varepsilon(v)=\tfrac12(\nabla v+\nabla v^T).
```

Let $`G,\lambda\in W^{1,\infty}(\Omega)`$ be real isotropic elastic moduli satisfying $`G\ge c>0`$ and $`3\lambda+2G\ge c>0`$. Define

```math
a(u,v)=\int_\Omega\left(2G\varepsilon(u):\varepsilon(v)
                    +\lambda\mathrm{div}u\mathrm{div}v\right)\,dx.
```

Prescribe $`F\in L^2(\Omega;\mathbb R^3)`$, $`T\in L^2(\Gamma_T;\mathbb R^3)`$, a gap $`g\in H^{1/2}(\Gamma_C)`$, a tangential previous-step displacement $`w_t\in H^{1/2}(\Gamma_C;\mathbb R^3)`$ with $`w_t\cdot n=0`$, and a friction coefficient $`f\in W^{1,\infty}(\Gamma_C)`$ with $`f\ge0`$. Set

```math
\ell(v)=\int_\Omega F\cdot v\,dx+\int_{\Gamma_T}T\cdot\mathrm{Tr}v\,dS,
\qquad
K=\{t\in H^{-1/2}(\Gamma_C):t\le0\}.
```

Here $`H^{-1/2}(\Gamma_C)`$ is the dual of $`H^{1/2}(\Gamma_C)`$, and $`t\le0`$ means nonpositive as a distribution. Such a $`t`$ is the unknown normal reaction. For each $`t\in K`$, let $`u_t\in V`$ be the unique minimizer of

```math
E_t(v)=\tfrac12 a(v,v)-\ell(v)-\langle t,v_n\rangle
                   +\langle-ft,|v_t-w_t|\rangle.
```

The brackets are duality pairings on $`\Gamma_C`$. Positivity of $`-ft`$, Korn's inequality and strict convexity make this frozen-reaction problem well defined. The subscript on $`u_t`$ indexes the reaction; $`(u_t)_n`$ below denotes its normal boundary trace.

Does there always exist $`t\in K`$ such that

```math
\left\langle (u_t)_n-g,\widehat t-t\right\rangle\ge0
\qquad\text{for every }\widehat t\in K,
```

with no smallness condition on $`f`$?

This is the unregularized incremental Signorini–Coulomb problem against a rigid obstacle. The same normal reaction determines both nonpenetration and the friction threshold. The question includes homogeneous isotropic elasticity. It asks for existence; a negative answer must provide admissible fixed data with no solution.

## Application

A time discretization of slowly loaded elastic contact produces this problem at each step. An existence result for unrestricted friction would clarify which three-dimensional continuum contact models remain mathematically meaningful when frictional feedback is strong.

## References

1. P. Ballard and F. Iurlano, *Existence results for the time-incremental elastic contact problem with Coulomb friction in 2D*, Mathematical Models and Methods in Applied Sciences **34** (2024), 2217–2263. [DOI](https://doi.org/10.1142/S0218202524500477). Precise formulation and source of the higher-dimensional direction: [revised author preprint, arXiv:2303.16298v2](https://arxiv.org/abs/2303.16298v2), 28 January 2026, §§1.1–1.3, Definition 2.3, Theorem 2.13 and Remark 2.19. The displayed question is the three-dimensional isotropic version of that formulation.
2. J. Jarušek, *Contact problems with bounded friction. Coercive case*, Czechoslovak Mathematical Journal **33** (1983), 237–261. [DOI](https://doi.org/10.21136/CMJ.1983.101875). Earlier small-friction theory; the historical comparison is also given in reference 1, §1.2.

## Status review


**Known cases:** The current Evidence Press v2.1.0-candidate explicitly restricts to matched two-body elastic interfaces with compact cross compliance and says it does not settle general three-dimensional contact. That does not cover this arbitrary-friction rigid-obstacle model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current Evidence Press v2.1.0-candidate explicitly restricts to matched two-body elastic interfaces with compact cross compliance and says it does not settle general three-dimensional contact. That does not cover this arbitrary-friction rigid-obstacle model.

Additional comparison sources: [comparison source 1](https://doi.org/10.1142/S0218202524500477); [comparison source 2](https://arxiv.org/abs/2303.16298v2); [comparison source 3](https://doi.org/10.21136/CMJ.1983.101875); [comparison source 4](https://doi.org/10.5281/zenodo.23171696). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves existence without a friction smallness condition in two dimensions. Its proof uses a special boundary weak-product property whose extension to three dimensions is explicitly left for further investigation. Proving the unrestricted three-dimensional analogue of that property is not the proposed problem: concentrating dominated boundary tractions can violate it without giving a contact nonexistence example.

An [October 2026 unrefereed announcement](https://doi.org/10.5281/zenodo.23171696) proposes arbitrary-friction existence for a particular class of two elastic bodies with a smooth closed matched interface. Its compact cross-compliance assumption does not cover the general rigid-obstacle model above. Its statement and scope were read; its full proof was not certified.

The later two-dimensional quasistatic evolution programme, finite-dimensional contact models, prescribed-pressure friction, normal-compliance regularizations and inverse recovery of elastic coefficients have different targets. Current bounded searches found no full resolution of this three-dimensional isotropic question. The final journal body of reference 1 has not been compared with its revised author preprint. [Detailed review](../FURTHER_problems/_tracking/parallel/continuum/incremental-3d-coulomb-review.json).

The independent selected-primary audit confirmed the formulation and the scope of the current announcement. The all-status AIM/OpenAI and FURTHER comparisons found no equivalent target at the recorded extents. All186 cached catalogue-description pages were scanned under six contact aliases; all15 returned windows were read, including unrelated aliases from the combined scan. The closest abstract quasi-hemivariational listing applies normal-compliance/slip-dependent conditions; no implication for this unregularized contact operator was identified. Complete mission proofs were not audited.

[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-incremental-3d-coulomb-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/incremental-3d-coulomb-prove2me0115-review.json) and [coordinator review](../FURTHER_problems/_tracking/coulomb-coordinator-review-2026-10-17.json) preserve exact hypotheses, publication/version limits and bounded search evidence.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-cafb218500248da0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
