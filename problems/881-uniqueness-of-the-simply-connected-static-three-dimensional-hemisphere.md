# 881. Uniqueness of the simply connected static three-dimensional hemisphere

**Area:** Mathematical relativity / geometric analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a compact, connected, simply connected smooth three-manifold with nonempty connected boundary. Suppose $`g`$ is a smooth Riemannian metric and $`f\in C^\infty(M)`$ satisfies

```math
R_g=6,\qquad
\nabla_g^2f=f(\mathrm{Ric}_g-3g),\qquad
f>0\text{ in }\mathrm{int}M,\qquad
f^{-1}(0)=\partial M,\qquad \max_M f=1.
```

Must there be an isometry $`F:(M,g)\to(\mathbb S^3_+,g_{\mathrm{round}})`$ with $`f=x_4\circ F`$, where $`\mathbb S^3_+=\{x\in\mathbb S^3:x_4\ge0\}`$ has unit sectional curvature?

No Ricci-curvature, boundary-area, surface-gravity or local-conformal-flatness assumption is imposed. The dimension, simple connectedness and connected boundary are essential parts of the question.

## Application

The interior metric $`-f^2dt^2+g`$ is a static vacuum spacetime with positive cosmological constant. This asks whether a smooth simply connected three-dimensional static region with a single horizon must have the de Sitter geometry.

## References

1. L. Ambrozio, *On static three-manifolds with positive scalar curvature*, Journal of Differential Geometry **107** (2017),1–45. The eligible manuscript explicitly asks the question on p.3 following Remark3; p.2 defines static triples. [DOI](https://doi.org/10.4310/jdg/1505268028), [eligible manuscript](https://arxiv.org/abs/1503.03803v1), [institutional accepted copy](https://wrap.warwick.ac.uk/128729/7/WRAP-on-static-three-manifolds-positive-scalar-curvature-Ambrozio-2015.pdf).
2. A. Carlotto, *The general relativistic constraint equations*, Living Reviews in Relativity **24** (2021),article2, AppendixD. [Survey](https://doi.org/10.1007/s41114-020-00030-z).
3. L. Branca, P. Mastrolia and M. Rigoli, *Some geometric properties of generalized $`\varphi`$-vacuum static spaces*, Calculus of Variations and Partial Differential Equations **65** (2026),163. Theorem1.4 and its following specialization retain an additional boundary-gradient constraint. [Published article](https://doi.org/10.1007/s00526-026-03337-x).

## Status review


**Known cases:** The known hemisphere results require a curvature, surface-gravity or boundary-gradient bound. Recent boundary-static Robin or quasi-Einstein results change the equation or exclude the static parameter. Nariai quotients fail simple connectedness; higher-dimensional counterexamples do not address dimension three.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known hemisphere results require a curvature, surface-gravity or boundary-gradient bound. Recent boundary-static Robin or quasi-Einstein results change the equation or exclude the static parameter. Nariai quotients fail simple connectedness; higher-dimensional counterexamples do not address dimension three.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check: 17 October2026.** The exact simply connected three-dimensional question is explicit in Ambrozio's manuscript. Known results impose further geometric conditions. Current generalized-static results retain an additional boundary-gradient upper bound. The June2026 Part I theorem and the served August2026 monograph specialize it to $`|\nabla f|^2\le1`$ in this normalization. The 2026 quasi-Einstein hemisphere classification assumes a parameter strictly greater than one; the static case is the excluded value one.

Without simple connectedness, a quotient of the Nariai cylinder supplies a connected-boundary example different from the hemisphere. Higher-dimensional simply connected counterexamples do not settle the three-dimensional question. Recent results on static potentials with Robin boundary conditions study a different boundary system.

The 2017 final published body has not been accessed; the available institutional accepted manuscript and latest eligible preprint were compared with current primary statements. An independent selected-primary audit has passed. The all-status catalogue comparison found no matching alias among its186cachedlistingpages; its scope is recorded in the review packet. The 2026 Calculus of Variations article has a factor discrepancy between its literal boundary display and following specialization; the review packet preserves it. The precise formulation and current theorem comparisons passed review.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/static-hemisphere-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-static-hemisphere-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/static-hemisphere-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/static-hemisphere-prove2-0155-review.json) and [coordinator review](../FURTHER_problems/_tracking/static-hemisphere-coordinator-review-2026-10-17.json) preserve version, access and formula caveats.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b748cc5fb227462e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
