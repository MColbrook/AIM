# 537. Does zero simplicial volume force zero Euler characteristic?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq1`$ and let $`M`$ be a connected, oriented, closed topological $`n`$-manifold. Here closed means compact without boundary. Assume $`M`$ is **aspherical**: its universal covering space is contractible.

Define its real simplicial volume by

```math
\|M\|=\inf\left\{\sum_{j=1}^{k}|a_j|:\ \sum_{j=1}^{k}a_j\sigma_j
\text{ is a real singular cycle representing }[M]_{\mathbb R}\right\}.
```

Does

```math
\|M\|=0\quad\Longrightarrow\quad
\chi(M)=\sum_{i=0}^{n}(-1)^i\dim_{\mathbb Q}H_i(M;\mathbb Q)=0
```

hold for every such $`M`$?

No curvature, residual finiteness, affine structure, smoothability or Euclidean universal-cover assumption is imposed. The reverse implication is not claimed: closed hyperbolic three-manifolds have zero Euler characteristic and positive simplicial volume.

## Application

This connects two basic measures of the topology of an aspherical manifold. An affirmative answer would turn nonzero Euler characteristic into an obstruction to arbitrarily small real fundamental cycles. In the smooth case, the source shows that it is equivalent to bounded representability of the tangent Euler class.

## References

1. C. Löh, M. Moraschini and G. Raptis, *On the simplicial volume and the Euler characteristic of (aspherical) manifolds*, Research in the Mathematical Sciences **9** (2022), article44, Question1.1, definitions2.1–2.2 and Proposition2.22. [Published article](https://doi.org/10.1007/s40687-022-00341-3), [eligible preprint](https://arxiv.org/abs/2109.08115).
2. I. Kim and X. Wan, *Positivity of simplicial volume for closed nonpositively curved four-manifolds with nonzero Euler characteristic*, [arXiv:2506.09524v4](https://arxiv.org/abs/2506.09524v4), Conjecture1.2 and Theorem1.4.
3. P. Capovilla, *Aspherical4-manifolds with positive Euler characteristic and their geography*, [arXiv:2511.15577v1](https://arxiv.org/abs/2511.15577v1), introduction and Remark4.2.

4. OpenAI, *The Singer conjecture in dimension four* (2026), Theorem1.1 and Corollary1.2. [Manuscript](https://github.com/openai/math/blob/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf).
5. OpenAI, *An integral scalar curvature bound for real simplicial volume* (2026), Theorem1.1. [Manuscript](https://github.com/openai/math/blob/main/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf).

## Status review


**Known cases:** New 23 October 2026 angle-cocycle paper proves the implication under immersed straightening, including convex-projective manifolds. It does not prove every aspherical topological manifold admits such a structure. Nonpositively curved four-dimensional and scalar-curvature comparisons are likewise restricted.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 17 October 2026. The complete final36-page source[1] was read, including its diagrams. The current theorem[2] proves the implication for closed nonpositively curved four-manifolds. That geometric hypothesis is additional. The construction[3] of Euler-characteristic-one aspherical four-manifolds has positive simplicial volume and hence gives no counterexample.

The OpenAI four-dimensional Singer manuscript concentrates the $`L^2`$-Betti numbers in degree two; it does not assert that the remaining number vanishes whenever real simplicial volume vanishes. The separate scalar-curvature inequality does not settle this target in the absence of an appropriate Riemannian metric.

The source's relative-boundary and bounded-Euler-class formulations are retained with this question, rather than counted as separate entries. Its counterexamples obtained by replacing a manifold with a more general aspherical space do not satisfy the stated manifold hypothesis. The independent selected-primary audit and the scoped catalogue comparison passed.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/gromov-zero-volume-euler-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-gromov-zero-volume-euler-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/lmr-all-target-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/gromov-lueck-prove2-0147-review.json) and [coordinator review](../FURTHER_problems/_tracking/gromov-zero-volume-euler-coordinator-review-2026-10-17.json) record exact hypotheses and reading limits.


### Online recheck, 2026-10-30

New 23 October 2026 angle-cocycle paper proves the implication under immersed straightening, including convex-projective manifolds. It does not prove every aspherical topological manifold admits such a structure. Nonpositively curved four-dimensional and scalar-curvature comparisons are likewise restricted.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.32342); [status source 2](https://arxiv.org/abs/2506.09524); [status source 3](https://doi.org/10.1007/s40687-022-00341-3). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ebc6155a43d61e57** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
