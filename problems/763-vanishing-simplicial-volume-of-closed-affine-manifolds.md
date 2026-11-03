# 763. Vanishing simplicial volume of closed affine manifolds

**Area:** Affine differential geometry; topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq1`$ and let $`M`$ be a smooth closed, connected, oriented $`n`$-manifold. Here closed means compact without boundary. Suppose $`M`$ admits a flat affine structure: there is a smooth coordinate atlas whose transition maps are restrictions of affine transformations of $`\mathbb R^n`$. Equivalently, its tangent bundle has a smooth connection with zero curvature and zero torsion.

The **real simplicial volume** is

```math
\|M\|=\inf\left\{\sum_{j=1}^{k}|a_j|:\ \sum_{j=1}^{k}a_j\sigma_j
\text{ is a real singular cycle representing }[M]_{\mathbb R}\right\}.
```

Must $`\|M\|=0`$?

No completeness, asphericity, parallel volume form, injectivity of holonomy or pure translation in holonomy is assumed. The oriented formulation covers the nonorientable case by passing to the orientation double cover. The invariant uses real coefficients; integral and stable integral simplicial volume are different questions.

## Application

This asks for a topological obstruction to the existence of a flat affine geometry. A positive answer would imply the vanishing of Euler characteristic for every closed affine manifold, because its tangent Euler class has a bounded representative. It relates local affine coordinates to the global cost of representing the fundamental class by real cycles. It is stronger than the Euler-characteristic conclusion alone.

## References

1. M. Bucher, C. Connell and J.-F. Lafont, *Vanishing simplicial volume for certain affine manifolds*, Proceedings of the American Mathematical Society **146** (2018), 1287–1294, conjecture on p.1288 and definitions on pp.1287–1288. [Published article](https://people.math.osu.edu/lafont.1/Bucher-Connell-Lafont-PAMS.pdf), [DOI](https://doi.org/10.1090/proc/13799), [eligible preprint](https://arxiv.org/abs/1610.00832).
2. A. Casali and M. Moraschini, *Topological volumes of certain complete affine manifolds*, [arXiv:2502.06303v1](https://arxiv.org/abs/2502.06303v1), Conjecture1.2 and Corollary1.4. This later preprint is used for current status.

## Status review


**Known cases:** The complete affine result assumes an infinite amenable normal subgroup, while the original special case also assumes holonomy conditions. Euler-characteristic vanishing does not imply real simplicial-volume vanishing, and an affine flat connection need not be a Riemannian flat metric.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The complete affine result assumes an infinite amenable normal subgroup, while the original special case also assumes holonomy conditions. Euler-characteristic vanishing does not imply real simplicial-volume vanishing, and an affine flat connection need not be a Riemannian flat metric.

Additional comparison sources: [comparison source 1](https://people.math.osu.edu/lafont.1/Bucher-Connell-Lafont-PAMS.pdf); [comparison source 2](https://doi.org/10.1090/proc/13799); [comparison source 3](https://arxiv.org/abs/1610.00832); [comparison source 4](https://arxiv.org/abs/2502.06303v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The complete published source was read, including its diagrams. The original theorem assumes an aspherical affine manifold, injective holonomy and a nontrivial pure translation. The later result in [2] assumes completeness and an infinite amenable normal subgroup of the fundamental group. Its Conjecture1.2 retains the general question.

The current Cocos manuscript claiming vanishing Euler characteristic does not claim this stronger simplicial-volume conclusion; no converse to the Euler-characteristic inequality is used. The OpenAI integral scalar-curvature theorem concerns Riemannian metrics. Flatness of a general affine connection does not supply a compatible Riemannian metric of nonnegative scalar curvature.

The AIM motion-planning question 524 starts with positive simplicial volume and asks about topological complexity, without an affine structure. It has a different target. Bounded current searches found no matching complete resolution; they are not proof that none exists. The exact five-alias scan of 186 cached all-status catalogue pages returned no matching listing descriptions. A separate reviewer checked the selected primary statements and current comparison scopes; no independent certification of the cited proofs is claimed.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/affine-simplicial-volume-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-affine-simplicial-volume-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/affine-simplicial-volume-duplicate-snapshot.json) and [coordinator review](../FURTHER_problems/_tracking/affine-simplicial-volume-coordinator-review-2026-10-17.json) preserve the exact hypotheses and catalogue/version limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-043673bdf48ecf83**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
