# 861. Bounded additive graph approximation of Euclidean three-space

**Area:** Metric geometry; approximation of continuous distances
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a connected undirected graph $`G=(\mathbb Z^3,E)`$, constants $`M\in\mathbb N`$ and $`0<\delta\le D<\infty`$, and an assignment of real lengths $`\ell:E\to[\delta,D]`$, such that every vertex has degree at most $`M`$ and its shortest-path distance satisfies

```math
\bigl|d_G(p,q)-\|p-q\|_2\bigr|\le C
\qquad(p,q\in\mathbb Z^3)
```

for one finite constant $`C`$?

Here $`d_G(p,q)`$ is the infimum of the sums of edge lengths along finite paths from $`p`$ to $`q`$. The constants are independent of the endpoints and their separation. The graph need not be periodic, planar or a nearest-neighbour lattice graph. Edge lengths need not be integers or equal the Euclidean distances between their endpoints.

Burago and Ivanov ask this particular three-dimensional case in the introduction of [1]. They also explain why the lattice formulation captures approximation of the whole Euclidean space by a graph with uniformly bounded degree and edge lengths.

## Application

The question concerns representing distances in an unbounded continuous space by a network of uniformly limited local complexity. A bounded additive error remains bounded as the represented region grows. In contrast, a fixed relative error permits the absolute distance error to grow without limit. The question asks for existence of such a representation; it does not require an efficient construction or an algorithm for finding shortest paths.

## References

1. D. Burago and S. Ivanov, *Uniform approximation of metrics by graphs*, [arXiv:1210.2435v2](https://arxiv.org/pdf/1210.2435v2), §§1–2, especially pp.1–3. Published in *Proceedings of the American Mathematical Society* **143** (2015), 1241–1256, [DOI](https://doi.org/10.1090/S0002-9939-2014-12299-4). The complete pinned 15-page preprint was read; the final 16-page journal version has an access gap.
2. Z. Cai, K. Chen, S. Du, A. Filtser, S. Pettie and D. Skora, *The Squishy Grid Problem*, SoCG 2026, LIPIcs **367**, 27:1–27:16, [published article](https://doi.org/10.4230/LIPIcs.SoCG.2026.27), §1.1; [latest preprint](https://arxiv.org/abs/2507.23105). The selected introduction distinguishes its planar-grid problem from [1].

## Status review


**Known cases:** The two-dimensional graph approximation and the Gromov-hyperbolic theorem do not cover Euclidean three-space. Periodic-graph obstructions do not exclude arbitrary nonperiodic graphs; the Squishy Grid theorem uses a planar nearest-neighbor graph and distance-dependent error.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The two-dimensional graph approximation and the Gromov-hyperbolic theorem do not cover Euclidean three-space. Periodic-graph obstructions do not exclude arbitrary nonperiodic graphs; the Squishy Grid theorem uses a planar nearest-neighbor graph and distance-dependent error.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reference [1] proves the corresponding existence statement in two-dimensional Euclidean space and for Gromov hyperbolic geodesic spaces with bounded coarse geometry. Its obstruction to periodic approximations does not cover arbitrary nonperiodic graphs.

Reference [2] studies the fixed nearest-neighbour graph in the plane and obtains a distance-dependent error bound. That result does not supply the constant-error three-dimensional representation requested here.

Bounded searches through 17 October 2026 located no matching proof, counterexample or complete announcement. The review packet records the exact version, hypotheses, current comparisons and duplicate checks. Independent selected-primary review passed. All186cached catalogue pages were compared using six target aliases; the four returned contexts concern different questions. Complete final-journal parity remains unverified, so the question locator is attributed to the pinned preprint.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/uniform-metric-r3-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-uniform-metric-r3-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/uniform-metric-r3-prove2-0129-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/uniform-metric-r3-coordinator-review-2026-10-17.json) give exact source coverage and search limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ef24fec894f4a8b1**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
