# 883. Bartnik's cosmological splitting conjecture

**Area:** Mathematical relativity and Lorentzian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq2`$ and let $`(M^{n+1},g)`$ be a connected, smooth, time-oriented Lorentzian manifold without boundary, with metric signature $`(-,+,\ldots,+)`$. Assume that:

- $`M`$ is globally hyperbolic and has a compact smooth spacelike Cauchy hypersurface. A Cauchy hypersurface meets every inextendible causal curve exactly once.
- The timelike convergence condition holds: $`\mathrm{Ric}_g(X,X)\geq0`$ for every timelike tangent vector $`X`$.
- Every maximal timelike geodesic is complete in both time directions: its proper-time parameter ranges over $`\mathbb R`$.

Must there be a compact Riemannian manifold $`(S^n,h)`$ and an isometry

```math
(M,g)\cong(\mathbb R\times S,-dt^2+h)?
```

This is Conjecture 1.2 of [2], restricted to spatial dimensions at least two. The conclusion is a global metric product. No timelike line, constant-mean-curvature slice, curvature bound on individual timelike planes, or symmetry is assumed.

## Application

The physically relevant case has $`n=3`$. The question concerns spatially closed cosmological models: under the stated focusing condition, could a spacetime remain timelike complete in both directions without being a static product? It asks for rigidity in the cosmological singularity theorems; see [1, 2].

## References

1. R. Bartnik, [*Remarks on cosmological spacetimes and constant mean curvature surfaces*](https://doi.org/10.1007/BF01218388), *Communications in Mathematical Physics* **117** (1988), 615–624. Original attribution; bibliographic details verified against the publisher. The formulation used here was read in [2].
2. G. J. Galloway and C. Vega, [*Rigidity in vacuum under conformal symmetry*](https://arxiv.org/abs/1712.00785v1), arXiv:1712.00785v1 (2017); *Letters in Mathematical Physics* **108** (2018), 2285–2292, [DOI](https://doi.org/10.1007/s11005-018-1079-7). Conjecture 1.2, Theorems 1.1 and 1.3.
3. G. J. Galloway, R. J. McCann and A. Ohanyan, [*Failure of local equi-Lipschitzness for families of Lorentz distances to Cauchy surface foliations*](https://arxiv.org/abs/2606.21997v2), *General Relativity and Gravitation* **58** (2026), 105, [DOI](https://doi.org/10.1007/s10714-026-03609-z). Sections 3–4, especially Corollary 3.5 and Conjectures 4.1–4.2.
4. R. J. McCann and A. Ohanyan, [*Positive resolution of Bartnik's cosmological splitting conjecture*](https://arxiv.org/abs/2606.03873v3), arXiv:2606.03873v3, **withdrawn 22 June 2026**. Retained here to explain a misleading solution-search hit.
5. J. L. Flores, J. Herrera and D. A. Solis, [*Low regularity approach to Bartnik's conjecture*](https://arxiv.org/abs/2412.08967v1), arXiv:2412.08967v1 (2024), Introduction and Theorem 1.1. Its synthetic curvature hypothesis is stronger than the smooth timelike Ricci condition above.
6. N. Gigli, M. Graf, R. J. McCann, A. Ohanyan, E. Woolgar and M. Zanardini, [*Almost-splitting of spacetimes under timelike sectional curvature bounds*](https://arxiv.org/abs/2610.10051), preprint (7 October 2026). This concerns almost-splitting with sectional-curvature and long-segment assumptions.

## Status review


### Online recheck, 2026-10-30

The June McCann-Ohanyan announcement remains explicitly withdrawn in the current primary record because its starting proposition is false. The follow-up paper formulates equivalent open assertions. Conditional line, symmetry, Busemann and sectional-curvature splitting results do not establish the three assumptions alone.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2606.03873). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known cases:** A complete maximizing timelike line gives the classical splitting theorem [2, Theorem 1.1]. In the vacuum case, a timelike conformal Killing field suffices [2, Theorem 1.3]. These are additional hypotheses.

**Recent claim checked:** The authors explicitly withdrew [4] because its starting proposition is false. Their subsequent paper [3] formulates equivalent conjectures and identifies the failed regularity argument. The examples there do not disprove Bartnik's conjecture: they drop compactness or the strong energy condition.

**Remaining target:** Obtain the product conclusion from the three assumptions above alone, or construct a counterexample satisfying all three. The stronger-hypothesis results [5, 6] do not settle it.

**Duplicate and resolution audit:** See the dated [review receipt](../FURTHER_problems/_tracking/bartnik-status-review.json). The review compares the complete AIM catalogue, retained entries, pending and excluded FURTHER findings, current announcement metadata and later literature. No matching active resolution was found. This is a dated literature-status assessment, not a guarantee against an unindexed announcement or a proof audit of every cited result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e9e0cd710d4ce8b2**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
