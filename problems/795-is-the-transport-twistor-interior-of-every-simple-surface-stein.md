# 795. Is the transport twistor interior of every simple surface Stein?

**Area:** Complex geometry; inverse problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\overline{\mathbb D}=\{z\in\mathbb C:|z|\le1\}`$ and let $`\sigma\in C^\infty(\overline{\mathbb D};\mathbb R)`$. Assume the Riemannian surface $`(\overline{\mathbb D},g)`$, with $`g=e^{2\sigma}|dz|^2`$, is **simple**: its boundary is strictly convex, all maximal unit-speed geodesics exit in finite forward and backward time, and there are no conjugate points. There is no curvature-sign or smallness assumption.

On $`Z^\circ=\mathbb D_z\times\mathbb D_\mu`$, give the open bidisk the integrable complex structure $`J_\sigma`$ specified by

```math
T^{0,1}_{J_\sigma}Z^\circ
=\mathrm{span}_{\mathbb C}\{\partial_{\bar\mu},\Xi_\sigma\},
```

where Wirtinger derivatives act in the displayed coordinates and

```math
\Xi_\sigma=e^{-\sigma}\left[
\mu^2\partial_z+\partial_{\bar z}
+(\mu^2\partial_z\sigma-\partial_{\bar z}\sigma)
(\bar\mu\partial_{\bar\mu}-\mu\partial_\mu)
\right].
```

This is the interior of the transport twistor space of $`g`$; its complex structure is part of the question, rather than the usual product complex structure of the bidisk.

**Must $`(Z^\circ,J_\sigma)`$ be a Stein surface for every such $`\sigma`$?** One equivalent formulation asks for a smooth, bounded-below exhaustion $`\psi:Z^\circ\to\mathbb R`$ whose sublevel sets are relatively compact and whose Levi form $`i\partial_{J_\sigma}\bar\partial_{J_\sigma}\psi`$ is positive definite everywhere. No extension of $`\psi`$ across the degenerate boundary $`|\mu|=1`$ is required.

The disk formulation covers arbitrary smooth compact oriented simple surfaces by global isothermal coordinates.

## Application

The complex structure packages geodesic transport and fibrewise holomorphic functions used in two-dimensional tomography. Establishing the Stein property would make global complex-analytic tools available for these transport spaces and clarify the geometry underlying non-Abelian X-ray range descriptions.

## References

1. J. Bohr and G. P. Paternain, *The Transport Oka-Grauert principle for simple surfaces*, Journal de l’École polytechnique — Mathématiques **10** (2023),727–769, §1.2 p.731 and Lemma4.10 p.750. [Final published PDF](https://www.numdam.org/item/10.5802/jep.231.pdf), [DOI](https://doi.org/10.5802/jep.231), [eligible preprint](https://arxiv.org/abs/2108.05125).
2. J. Bohr, F. Monard and G. P. Paternain, *Local and Global Blow Downs of Transport Twistor Space*, SIGMA **22** (2026),045,45pp., §2.5 equation(2.7), Theorems1.2–1.4 and Question3.7. [Published PDF](https://sigma-journal.com/2026/045/sigma26-045.pdf), [DOI](https://doi.org/10.3842/SIGMA.2026.045).
3. F. Monard and Z. Qi, *A family of non-simple surfaces whose transport twistor spaces admit global blow-down maps*, [arXiv:2510.09518v1](https://arxiv.org/abs/2510.09518v1), introduction and Theorem1.

## Status review


**Known cases:** The final SIGMA blow-down paper leaves general simple-surface global structure open and covers constant curvature or small perturbations. An arbitrary domain in C2 and holomorphic bundle triviality do not themselves establish Steinness of the transport-twistor interior.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The final SIGMA blow-down paper leaves general simple-surface global structure open and covers constant curvature or small perturbations. An arbitrary domain in C2 and holomorphic bundle triviality do not themselves establish Steinness of the transport-twistor interior.

Additional comparison sources: [comparison source 1](https://www.numdam.org/item/10.5802/jep.231.pdf); [comparison source 2](https://doi.org/10.5802/jep.231); [comparison source 3](https://arxiv.org/abs/2108.05125); [comparison source 4](https://sigma-journal.com/2026/045/sigma26-045.pdf); [comparison source 5](https://doi.org/10.3842/SIGMA.2026.045); [comparison source 6](https://arxiv.org/abs/2510.09518v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The original source explicitly raises the Stein question and proves it for Euclidean domains. The final2026 paper supplies local blow-down maps and global maps for constant-curvature metrics and their small perturbations; Question3.7 still asks for general simple-surface global maps. The Monard–Qi theorem treats an explicit rotationally symmetric family, including some non-simple surfaces.

These are distinct assertions: a biholomorphism onto an arbitrary open subset of $`\mathbb C^2`$ alone does not establish the Stein property. Holomorphic triviality of the bundles in the transport Oka–Grauert theorem also does not, by itself, establish Steinness of this open interior.

The OpenAI Shafarevich counterexamples concern universal covers of projective varieties. Their actual stated constructions do not assert a transport-twistor structure of a simple Riemannian disk, so they do not supply a counterexample in the specified class.

No matching resolution was found in the bounded current-status searches. Exact source extents, semantic comparisons and passed independent/catalogue gates are recorded in the review packet; no exhaustive absence proof is asserted.

[Owner review](../FURTHER_problems/_tracking/parallel/rough-filtering/twistor-stein-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-twistor-stein-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/twistor-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/batch-0150-deployment-validation.json), [selected announcement passages](../FURTHER_problems/_tracking/parallel/rough-filtering/openai046-selected-pages.json) and [coordinator review](../FURTHER_problems/_tracking/twistor-stein-coordinator-review-2026-10-17.json) record exact versions and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6c1184a53267571c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
