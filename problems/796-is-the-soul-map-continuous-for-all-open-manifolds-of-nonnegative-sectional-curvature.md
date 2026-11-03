# 796. Is the soul map continuous for all open manifolds of nonnegative sectional curvature?

**Area:** Riemannian geometry and spaces of metrics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`V`$ be a connected open smooth manifold admitting a complete Riemannian metric of nonnegative sectional curvature. Let $`\mathcal M_{\sec\geq0}(V)`$ be the moduli space of such metrics modulo diffeomorphisms, with the quotient of smooth convergence uniformly on compact subsets of $`V`$. Each metric has a compact, totally convex soul $`S\subset V`$; although its construction uses a basepoint, its isometry class is independent of that choice.

Let $`\mathscr V`$ contain one representative of each diffeomorphism type that occurs as a soul of such a metric on $`V`$. Give $`\coprod_{S\in\mathscr V}\mathcal M_{\sec\geq0}(S)`$ the disjoint-union topology. Is the map
```math
\mathrm{soul}:\mathcal M_{\sec\geq0}(V)
\longrightarrow\coprod_{S\in\mathscr V}\mathcal M_{\sec\geq0}(S),
\qquad [g]\longmapsto[g|_{S_g}],
```

continuous for every such $`V`$? A counterexample would also settle the question. The curvature assumption is sectional $`\sec\geq0`$, including zero curvature.

## Application

The soul links the geometry of a noncompact manifold to a compact one. Continuity would let nearby complete metrics be compared through their compact souls, despite the soul being selected using geometry at infinity that the compact-open metric topology does not directly observe.

## Known cases

The cited paper proves continuity when $`V`$ is *indecomposable*: it admits a complete nonnegatively curved metric whose soul normal sphere bundle has no section. It also cites the codimension-one case, where the soul map is a homeomorphism. These cases do not cover every open $`V`$.

## References

1. I. Belegradek and D. González-Álvaro, [*Diffeomorphic souls and disconnected moduli spaces of nonnegatively curved metrics*](https://aif.centre-mersenne.org/item/10.5802/aif.3471.pdf), *Annales de l’Institut Fourier* **72** (2022), no. 1, 109–122, §1, printed pp. 109–110 and Theorem 1.1. [DOI](https://doi.org/10.5802/aif.3471); [arXiv record](https://arxiv.org/abs/2005.05755).

## Status review


**Known cases:** The soul map uses the compact-open smooth metric topology and a disjoint union of compact soul moduli. Known results for diffeomorphic or indecomposable souls do not imply continuity for every open nonnegatively curved manifold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The soul map uses the compact-open smooth metric topology and a disjoint union of compact soul moduli. Known results for diffeomorphic or indecomposable souls do not imply continuity for every open nonnegatively curved manifold.

Additional comparison sources: [comparison source 1](https://aif.centre-mersenne.org/item/10.5802/aif.3471.pdf); [comparison source 2](https://doi.org/10.5802/aif.3471); [comparison source 3](https://arxiv.org/abs/2005.05755). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source-body, native-symbol, status and duplicate review](../FURTHER_problems/_tracking/soul-map-continuity-status-2026-10-21.json) verified the nonnegative curvature symbol against the published page image and searched for later full results or announcements through 21 October 2026. No matching complete solution was located. The search is bounded.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6f08a515d3548c59**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
