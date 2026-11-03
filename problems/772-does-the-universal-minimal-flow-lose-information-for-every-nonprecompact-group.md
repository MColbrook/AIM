# 772. Does the universal minimal flow lose information for every nonprecompact group?

**Area:** Topological dynamics of continuous symmetry groups
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`G`$ be a Hausdorff topological group. It is *precompact* if, for every identity neighbourhood $`U`$, some finite $`F\subset G`$ satisfies $`G=FU`$.

Use continuous right actions of $`G`$ on nonempty compact Hausdorff spaces. An *ambit* is such a space with a distinguished point having dense orbit. Let $`(S(G),e)`$ be the greatest ambit: it admits a continuous pointed $`G`$-map onto every ambit. Let $`M(G)`$ be the universal minimal flow; every orbit is dense, and it maps equivariantly onto every minimal compact $`G`$-flow.

For $`g\in G`$, put $`R_g(x)=xg`$ on $`M(G)`$, and define
```math
E(M(G))=\overline{\{R_g:g\in G\}}\ \subset M(G)^{M(G)},
```

where the closure uses pointwise convergence. Give this space the right action $`(p\cdot g)(x)=p(x)g`$ and distinguished point $`\mathrm{id}`$. There is a canonical continuous surjection
```math
\Phi:(S(G),e)\longrightarrow(E(M(G)),\mathrm{id}).
```

If $`G`$ is not precompact, must $`\Phi`$ fail to be injective? This is Pestov's conjecture [1, Conjecture1.1]. It concerns the canonical pointed map, rather than an arbitrary homeomorphism of the underlying spaces. No discreteness, local compactness, separability, or metrizability assumption is imposed.

## Application

The conjecture asks whether minimal compact dynamics necessarily loses some of the information contained in a group's greatest compact ambit, except when the group is already precompact. It compares universal constructions used to study continuous group actions.

## References

1. Dana Bartošová and Andy Zucker, [*Fraïssé structures and a conjecture of Furstenberg*](https://emis.de/ft/33933), *Commentationes Mathematicae Universitatis Carolinae* **60** (2019), 1–24, definitions on printed pp.1–3 and Conjecture1.1. [DOI](https://doi.org/10.14712/1213-7243.2015.276); [arXiv metadata](https://arxiv.org/abs/1802.02513).
2. Eli Glasner, Todor Tsankov, Benjamin Weiss and Andy Zucker, [*Bernoulli disjointness*, author text](https://math.univ-lyon1.fr/~tsankov/papers/BDJ.pdf), Introduction and Corollary1.4. *Duke Mathematical Journal* **170** (2021), 615–651, [DOI](https://doi.org/10.1215/00127094-2020-0093); [latest listed arXiv version](https://arxiv.org/abs/1901.03406v2).

## Status review


**Known cases:** The canonical pointed greatest-ambit map is required for every nonprecompact Hausdorff group. Infinite discrete-group cases, metrizable-flow descriptions and particular transformation semigroups do not settle arbitrary topological groups.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The canonical pointed greatest-ambit map is required for every nonprecompact Hausdorff group. Infinite discrete-group cases, metrizable-flow descriptions and particular transformation semigroups do not settle arbitrary topological groups.

Additional comparison sources: [comparison source 1](https://emis.de/ft/33933); [comparison source 2](https://doi.org/10.14712/1213-7243.2015.276); [comparison source 3](https://arxiv.org/abs/1802.02513); [comparison source 4](https://math.univ-lyon1.fr/~tsankov/papers/BDJ.pdf); [comparison source 5](https://doi.org/10.1215/00127094-2020-0093); [comparison source 6](https://arxiv.org/abs/1901.03406v2). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

For precompact groups the canonical map is an isomorphism. The conjectured failure of injectivity is known for every infinite discrete group by [2], and [1] treats additional automorphism-group cases. Those results leave the unrestricted topological-group question distinct from its discrete special case.

The discovery passage was Conjecture1.10 in arXiv:1808.08771v1. Its latest version is withdrawn because it was superseded by the joint work [2]; it is not used here as current authority. The full general conjecture is explicitly stated in the published source [1].

Bounded searches through 30 October 2026 found no matching complete solution or announcement. Recent work on proper Ellis semigroup compactifications of particular transformation groups was not identified with this canonical map for arbitrary $`G`$. No equivalent AIM, OpenAI-announcement or existing FURTHER target was located; the existing question about amenability of smooth mapping groups asks a different property. These are bounded literature checks, not a proof that no resolution exists.

The [primary, current and semantic review](../FURTHER_problems/_tracking/ROOT-C317-Pestov-canonical-map-primary-current-and-semantic-review-20261030.json), [independent formulation review](../FURTHER_problems/_tracking/C-C317-Pestov-right-ambit-canonical-map-independent-model-peer-20261030.json) and [final review](../FURTHER_problems/_tracking/ROOT-FINAL-Pestov-canonical-map-admission-review-20261030.json) record the inspected extents and conventions.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-1ef2d32d41e2dd3d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
