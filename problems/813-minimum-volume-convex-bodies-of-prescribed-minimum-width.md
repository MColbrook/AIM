# 813. Minimum-volume convex bodies of prescribed minimum width

**Area:** Convex geometry and shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each integer $`n\ge3`$, let $`K\subset\mathbb R^n`$ range over compact convex sets with nonempty interior. Define
```math
h_K(u)=\max_{x\in K}x\cdot u,\qquad
w(K)=\min_{u\in S^{n-1}}\bigl(h_K(u)+h_K(-u)\bigr).
```

Determine the exact value
```math
c_n=\inf\{\mathrm{Vol}_n(K):w(K)=1\}
```

and characterize every attaining body up to Euclidean isometry.

This is the higher-dimensional Euclidean Pál isominwidth problem. The constraint prescribes the *minimum* directional thickness; it does not require constant width in every direction. No symmetry is imposed, and no particular minimizing shape is asserted. Equivalently, determine the sharp constant and equality cases in $`\mathrm{Vol}_n(K)\ge c_n w(K)^n`$.

## Application

The problem asks for the least volume of material in a convex solid that has a specified minimum thickness in every direction. It is a sharp benchmark for convex shape optimization.

## References

1. Károly J. Böröczky, Ansgar Freyer and Ádám Sagmeister, *Pál's Isominwidth Problem in the Hyperbolic Space*, Journal of Geometric Analysis **36** (2026),76, [published article](https://doi.org/10.1007/s12220-025-02258-z), abstract and Introduction, physical pp.1–2; [author version2502.04427v2](https://arxiv.org/abs/2502.04427v2).
2. Ádám Sagmeister, *On the perimeter, diameter and circumradius of ordinary hyperbolic reduced polygons*, Canadian Mathematical Bulletin **68**(3) (2025),950–965, [published article](https://doi.org/10.4153/S0008439525000189), Introduction, p.950.
3. Ferenc Fodor and Ádám Sagmeister, *Optimal stability of Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, [arXiv:2606.02882v2](https://arxiv.org/abs/2606.02882v2), revised6October2026, abstract.

## Status review


**Known cases:** The high-dimensional minimum-volume problem is for minimum width, not constant width. Recent hyperbolic or ball-convex results do not determine the Euclidean sharp constant and all equality cases in every dimension at least three.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The high-dimensional minimum-volume problem is for minimum width, not constant width. Recent hyperbolic or ball-convex results do not determine the Euclidean sharp constant and all equality cases in every dimension at least three.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 source explicitly retains the Euclidean problem for $`n\ge3`$. Planar results, spherical inequalities and hyperbolic variants have different dimensions or admissible classes. The October2026 stability preprint concerns ball-convex bodies in planes. None supplies the required higher-dimensional sharp volume comparison. The regular simplex should not be assumed optimal: in dimensions at least three, simplices are not reduced.

Current searches found no matching complete solution or announcement. AIM242 concerns constant-width bodies, while AIM246 minimizes curve length. No equivalent target was identified among the inspected AIM/OpenAI entries, pending findings, existing FURTHER pages and cached website comparisons.

The [coordinator review](../FURTHER_problems/_tracking/pal-isominwidth-coordinator-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/pal-isominwidth-current-review-2026-10-19.json), [duplicate comparisons](../FURTHER_problems/_tracking/pal-isominwidth-duplicates-review-2026-10-19.json) and [independent scope audit](../FURTHER_problems/_tracking/parallel/continuum/cross-pal-euclidean-isominwidth-selected-review-2026-10-19.json) record the bounded evidence and limitations. Only selected primary passages were read; these checks do not certify that every possible resolution has been excluded.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8b7c1b3365314dd0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
