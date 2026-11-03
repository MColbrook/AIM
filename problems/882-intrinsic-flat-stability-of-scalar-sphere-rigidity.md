# 882. Intrinsic-flat stability of scalar sphere rigidity

**Area:** Scalar geometry and mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix constants $`D,V>0`$. Let $`g_j`$, $`j=1,2,\ldots`$, be any sequence of smooth Riemannian metrics on the standard smooth three-sphere $`\mathbb S^3`$. Assume
```math
\mathrm{Scal}_{g_j}\ge 6-\frac1j,\qquad
\mathrm{MinA}(\mathbb S^3,g_j)\ge4\pi-\frac1j,\qquad
\mathrm{diam}_{g_j}(\mathbb S^3)\le D,\qquad
\mathrm{Vol}_{g_j}(\mathbb S^3)\le V.
```
Here
```math
\mathrm{MinA}(\mathbb S^3,g)=\inf\{\mathrm{Area}_g(\Sigma):\Sigma\subset\mathbb S^3\text{ is a nonempty smooth closed embedded minimal surface}\}.
```
Minimal means that the mean curvature vanishes. Both stable and unstable surfaces are included, with no genus restriction. The sphere has no boundary.

Give each sphere its intrinsic Riemannian distance $`d_j`$ and its integration current $`T_j`$ for the standard orientation. Must the whole sequence converge to the unit round sphere in the volume-preserving intrinsic-flat sense? Explicitly, writing $`d_{\mathrm{rd}}`$ and $`T_{\mathrm{rd}}`$ for the round distance and integration current, is it true that
```math
d_{\mathcal F}\bigl((\mathbb S^3,d_j,T_j),(\mathbb S^3,d_{\mathrm{rd}},T_{\mathrm{rd}})\bigr)\longrightarrow0,
\qquad
\mathrm{Vol}_{g_j}(\mathbb S^3)\longrightarrow2\pi^2?
```
The distance $`d_{\mathcal F}`$ is the Sormani–Wenger intrinsic flat distance: the infimum of flat distances of the currents after distance-preserving embeddings into a common complete metric space. No identification of points between the spheres is prescribed in the conclusion.

## Application

Scalar curvature is a central geometric quantity in general relativity. This conjecture asks whether almost attaining a sharp scalar-curvature and minimal-surface bound forces a closed three-dimensional space to be close to the round model in a weak geometric sense. The specified convergence permits thin wells while tracking total volume.

## References

1. Christina Sormani and participants at the IAS workshop, [*Conjectures on Convergence and Scalar Curvature*](https://arxiv.org/abs/2103.10093v1), Conjecture 9.1, equations (124)–(125), and Remark 9.3, pp. 41–42 (2021). Attribution: Fernando C. Marques and André Neves.
2. Hunter Stufflebeam and Paul Sweeney Jr, [*Width Stability of Rotationally Symmetric Metrics*](https://doi.org/10.1007/s12220-025-02020-5), Journal of Geometric Analysis **35** (2025), 238, Conjecture 1.1 and Theorem A; [open published text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12187838/).
3. Paul Sweeney Jr, [*Examples for scalar sphere stability*](https://doi.org/10.1007/s00526-025-03036-z), Calculus of Variations and Partial Differential Equations **64** (2025), 188; [preprint](https://arxiv.org/abs/2301.01292v2), Conjecture 1.3 and Theorems A-prime and B-prime.
4. Sven Hirsch and Yiyue Zhang, [*Stability of Llarull's theorem in all dimensions*](https://doi.org/10.1016/j.aim.2024.109980), Advances in Mathematics **458** (2024), 109980; [preprint](https://arxiv.org/abs/2310.14412v3), Theorems 1.1 and 1.6.

## Status review


**Known cases:** Rotationally symmetric width stability is established. Width-only counterexamples have minimum minimal-surface area tending to zero; Llarull stability imposes a degree/map comparison assumption. Neither class settles the stated unrestricted three-sphere minimum-area conjecture.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Rotationally symmetric width stability is established. Width-only counterexamples have minimum minimal-surface area tending to zero; Llarull stability imposes a degree/map comparison assumption. Neither class settles the stated unrestricted three-sphere minimum-area conjecture.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The general conjecture remains open in the cited sources. Stufflebeam–Sweeney prove the rotationally symmetric case, in all dimensions at least three, and retain the general three-dimensional conjecture. Their Theorem A also gives volume convergence in that symmetric setting.

Sweeney's counterexamples to a width-only assertion have minimum minimal-surface area tending to zero, so they do not satisfy the displayed minimum-area bound. Other examples fail Gromov–Hausdorff convergence while still converging to the round sphere in the requested volume-preserving intrinsic-flat sense.

The Llarull stability results require an area-nonincreasing map of nonzero degree to the round sphere, or stronger metric-comparison and Sobolev assumptions. Those hypotheses are not part of this conjecture. Wenger compactness alone gives a subsequence with some intrinsic-flat limit; identifying that limit as round and preserving its total mass remain additional conclusions.

The volume question in Remark 9.3 is included in this entry, rather than made a separate problem. No matching complete general resolution was located in the recorded bounded searches. The [source and current review](../FURTHER_problems/_tracking/parallel/continuum/scalar-sphere-stability-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-scalar-sphere-stability-review.json), [semantic comparison](../FURTHER_problems/_tracking/scalar-sphere-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/scalar-sphere-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/scalar-sphere-coordinator-review-2026-10-19.json) record the checks and their limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c980a03a2a342504**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
