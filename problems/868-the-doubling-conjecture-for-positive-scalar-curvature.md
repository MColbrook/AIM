# 868. The doubling conjecture for positive scalar curvature

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a compact smooth manifold with nonempty boundary, and let
```math
DX=X\cup_{\partial X}X
```

be its smooth double. Suppose $`DX`$ admits a Riemannian metric with strictly positive scalar curvature.

Must $`X`$ admit a Riemannian metric $`g`$ such that
```math
\mathrm{Scal}_g>0\quad\text{on }X,
\qquad H_g>0\quad\text{on }\partial X?
```


Here positive mean curvature uses the source's outward-normal convention: parallel hypersurfaces just inside the boundary have smaller volume, and volume increases when moving outward. Thus the boundary is strictly mean convex. The metric on $`X`$ need not be the restriction of the initially given metric on $`DX`$, and no product structure near the boundary is required.

## Application

Doubling turns a boundary-value existence question for positive scalar curvature into a closed-manifold existence question. The forward implication is known; the conjecture asks whether it captures all topological obstructions to finding such a boundary metric.

## Known progress

The statement holds in dimensions at most three. The latest source revision, v2 (25 May 2022), retains Conjecture 7.1, as does the published article.

Frenck's April 2026 preprint proves broad higher-dimensional cases, with a split-injection condition on the image of the fundamental group of each boundary component. Its Theorems A and B impose further dimension, spin or cohomological hypotheses; its Theorem C treats selected four-dimensional cases. These results leave the unrestricted conjecture open. In particular, connected boundary makes one auxiliary condition vacuous but does not remove the fundamental-group splitting requirement. The preprint also rules out a proposed example from the source as a counterexample.

## Status review


**Known cases:** Frenck April 2026 Theorems A-C assume conditions on boundary fundamental-group images, dimension, spin or cohomology, or treat selected four-manifolds. They do not establish the arbitrary-manifold doubling implication. The source retains Conjecture 7.1.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Frenck April 2026 Theorems A-C assume conditions on boundary fundamental-group images, dimension, spin or cohomology, or treat selected four-manifolds. They do not establish the arbitrary-manifold doubling implication. The source retains Conjecture 7.1.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Selected original, latest and published statement windows and the actual main theorems of the 2026 preprint were read. Searches for the named conjecture, counterexamples, later proofs and announcements, including Prove2Me, found no matching unrestricted resolution on the review date. All-status AIM/OpenAI and FURTHER comparisons distinguish this existence question from integral scalar-curvature inequalities, rational inessentiality, and minimal-graph boundary-limit questions. This is a bounded current-status review, not a certification of every cited proof.

## References

1. J. Rosenberg and S. Weinberger, [Positive scalar curvature on manifolds with boundary and their doubles](https://arxiv.org/abs/2201.01263), Conjecture 7.1 and Remark 1.4. [Published article](https://doi.org/10.4310/PAMQ.2023.v19.n6.a12); [public primary PDF](https://par.nsf.gov/servlets/purl/10505138).
2. G. Frenck, [The doubling conjecture for positive scalar curvature](https://arxiv.org/abs/2604.12901), v1 (14 April 2026), Theorems A–C and Remark 1.1.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f9fd3f5adab5bf24**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
