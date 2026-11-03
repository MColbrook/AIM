# 786. Can a finite cover lower the fundamental-group rank of a hyperbolic 3-manifold by more than one?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a finitely generated group $`G`$, let $`\mathrm{rk}(G)`$ be the minimum number of generators of $`G`$. Let $`M`$ be a compact, orientable hyperbolic $`3`$-manifold and let $`\widetilde M\to M`$ be any finite-sheeted covering. Must
```math
\mathrm{rk}\pi_1(\widetilde M)\geq \mathrm{rk}\pi_1(M)-1?
```

Equivalently, can a finite-index subgroup of a hyperbolic $`3`$-manifold group ever need at least two fewer generators than the ambient group? The compact and orientable hypotheses follow Shalen's original Conjecture 4.2.

## Application

The conjecture would constrain how the algebraic complexity of a hyperbolic $`3`$-manifold changes under finite covering. A one-generator drop can occur, so the proposed bound is sharp. An analogous one-step lower bound for mod-$`p`$ first-homology rank is known, but does not settle the rank of the fundamental group.

## References

1. P. B. Shalen, [*Hyperbolic volume, Heegaard genus and ranks of groups*](https://msp.org/gtm/2007/12/gtm-2007-12-014p.pdf), *Geometry & Topology Monographs* **12** (2007), 335–349, Conjecture 4.2, p. 339. Original precise conjecture and discussion of the known cyclic-cover and homology cases.
2. M. Aschenbrenner, S. Friedl and H. Wilton, [*3-Manifold Groups*](https://www.maths.gla.ac.uk/~mpowell/Aschenbrenner-Friedl-Wilton-3-manifold-groups-final-version-031115.pdf), author-final manuscript (2015), §7.5.2, Conjecture 7.5.4, printed p. 125; [EMS published book](https://ems.press/books/elm/217/contents), DOI [10.4171/154](https://doi.org/10.4171/154). The checked manuscript and published edition have different pagination.
3. I. Biringer, [*Subgroups of bounded rank in hyperbolic 3-manifold groups*](https://arxiv.org/abs/2401.01328), *Bulletin of the London Mathematical Society* **56** (2024), 3829–3837, DOI [10.1112/blms.13170](https://doi.org/10.1112/blms.13170). Proves a related bounded-rank tower theorem, not the proposed bound for every individual cover.

## Status review


**Known cases:** The target is generator rank under every finite cover, with a drop at most one. Homology-rank transfer, cofinal towers, two-generator restrictions and bounds involving manifold volume do not establish the general inequality.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is generator rank under every finite cover, with a drop at most one. Homology-rank transfer, cofinal towers, two-generator restrictions and bounds involving manifold volume do not establish the general inequality.

Additional comparison sources: [comparison source 1](https://msp.org/gtm/2007/12/gtm-2007-12-014p.pdf); [comparison source 2](https://www.maths.gla.ac.uk/~mpowell/Aschenbrenner-Friedl-Wilton-3-manifold-groups-final-version-031115.pdf); [comparison source 3](https://ems.press/books/elm/217/contents); [comparison source 4](https://doi.org/10.4171/154); [comparison source 5](https://arxiv.org/abs/2401.01328); [comparison source 6](https://doi.org/10.1112/blms.13170). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2015 book manuscript identifies this as open. Bounded primary-source and announcement searches through 22 October 2026 found no matching proof or counterexample; Biringer's later tower result has a different conclusion. Local AIM and FURTHER problem-text searches found no duplicate. This is a dated literature check, not a proof of openness; the [audit](../FURTHER_problems/_tracking/d054-shalen-finite-cover-rank-status-2026-10-22.json) records its scope.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4a6bb637d84f35ef**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
