# 531. Uniqueness of the positive Einstein metric on the four-sphere

**Area:** Differential geometry / mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb S^4`$ have its standard smooth structure, and let $`g`$ be any smooth Riemannian metric on it satisfying

```math
\mathrm{Ric}_g=3g.
```

Must $`(\mathbb S^4,g)`$ be isometric to the unit round four-sphere? Equivalently, is every positive Einstein metric on the standard smooth four-sphere round up to scaling and isometry?

No sectional-curvature sign, symmetry, volume, Yamabe-constant or closeness-to-round assumption is imposed. The question concerns the standard smooth sphere, without an assertion about exotic smooth homotopy spheres.

## Application

Positive Einstein metrics are compact Riemannian solutions of the vacuum Einstein equation with positive cosmological constant. This classification question also appears in the study of compact Euclidean gravitational geometries. Boucher and Gibbons explicitly pose it as a stronger geometric question than uniqueness of a static de Sitter region.

The round metric is locally rigid, but local rigidity does not rule out other components of the solution space. Akutagawa–Endo–Seshadri prove a uniform gap theorem: a positive Einstein metric is round if its conformal Yamabe constant lies above a specified threshold slightly below $`Y(\mathbb S^4,[g_{\mathrm{round}}])/\sqrt3`$. This retains an extra hypothesis.

Recent classification claims assuming nonnegative or positive sectional curvature do not cover arbitrary metrics in the question. Neither the known squashed-sphere deformation calculations nor results requiring an isometric torus action supply an unrestricted classification.

## References

1. W. Boucher and G. W. Gibbons, *Cosmic baldness*, in *The Very Early Universe* (Cambridge, 1982), Cambridge University Press, 1983, pp. 273–278. [Eligible author reprint](https://arxiv.org/abs/1109.3535v1), exact conjecture in “Generalized Israel’s theorem”, PDF p. 4.
2. K. Akutagawa, H. Endo and H. Seshadri, *A gap theorem for positive Einstein metrics on the four-sphere*, Mathematische Annalen **373** (2019), 1329–1339. [DOI](https://doi.org/10.1007/s00208-018-1749-x), [latest eligible preprint](https://arxiv.org/abs/1801.10305v2), introduction and Theorem 1.2.

## Status review


**Known cases:** Positive-sectional-curvature classifications and torus-symmetric or twistor-curvature theorems do not classify arbitrary positive Einstein metrics on standard S4. No active unrestricted resolution located; the torus-symmetry preprint's withdrawal is retained.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Status checked: 17 October 2026.** Current primary statements and announced results were compared with the unrestricted question. The October 2026 Chen–Dong torus-symmetry preprint was withdrawn; its earlier statement is not treated as an active theorem. The detailed review records the narrower hypotheses of current claims, the gaps in access to final published bodies, and the scoped catalogue comparison. An independent selected-primary audit has passed. The precise formulation, independent audit and scoped catalogue comparison passed coordinator review.

Dameno’s 2026 twistor-space classification assumes an additional curvature condition on the associated twistor metric; that condition does not follow just from the base metric being Einstein. [Published theorem](https://doi.org/10.1007/s00209-026-04100-w), Theorem 1.1 and Corollary 1.2.

[Source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/positive-einstein-s4-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-positive-einstein-s4-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/positive-einstein-s4-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/positive-einstein-s4-prove2-0156-review.json) and [coordinator review](../FURTHER_problems/_tracking/positive-einstein-s4-coordinator-review-2026-10-17.json) record the checked scope and remaining access/version gaps. These are dated literature checks, not a guarantee that no solution exists.


### Online recheck, 2026-10-30

Positive-sectional-curvature classifications and torus-symmetric or twistor-curvature theorems do not classify arbitrary positive Einstein metrics on standard S4. No active unrestricted resolution located; the torus-symmetry preprint's withdrawal is retained.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.12210); [status source 2](https://doi.org/10.1007/s00209-026-04100-w); [status source 3](https://github.com/openai/math/blob/main/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-f9303a5f48457b24** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
