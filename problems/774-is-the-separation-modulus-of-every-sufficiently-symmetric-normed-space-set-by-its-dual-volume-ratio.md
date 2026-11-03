# 774. Is the separation modulus of every sufficiently symmetric normed space set by its dual volume ratio?

**Area:** Metric geometry and Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a metric space $`X`$, let $`\mathrm{SEP}(X)`$ be the least $`\sigma`$ such that, at every scale $`\Delta>0`$, a random partition of $`X`$ into sets of diameter at most $`\Delta`$ can be chosen with

```math
\Pr[x\text{ and }y\text{ lie in different cells}]\leq \sigma\,\frac{d_X(x,y)}{\Delta}\qquad(x,y\in X).
```


Let $`X`$ be a finite-dimensional real normed space with **enough symmetries**: every linear operator commuting with every surjective linear isometry of $`X`$ is a scalar multiple of the identity. Write $`n=\dim X`$, and let $`\mathrm{vr}(X^*)`$ be the volume ratio of the unit ball of its dual: the $`n`$th root of its volume divided by that of a maximum-volume ellipsoid inside it.

**Naor's Conjecture 6:** Are there universal positive constants $`c,C`$ such that every such $`X`$ satisfies

```math
c\,\mathrm{vr}(X^*)\sqrt n\leq\mathrm{SEP}(X)\leq C\,\mathrm{vr}(X^*)\sqrt n?
```


The constants must be independent of the space and its dimension. The memoir states a relation up to lower-order dimension factors and gives a constant-factor argument for spaces with a coordinate $`1`$-symmetric basis. The universal constant-factor assertion above is the remaining target.

## Application

Random partitions control how a metric space can be clustered at all scales. The proposed estimate would turn the dual ball's volume ratio into a sharp general bound for this clustering invariant, with consequences for Lipschitz extension bounds.

## References

1. A. Naor, [*Extension, Separation and Isomorphic Reverse Isoperimetry*](https://ems.press/content/book-files/47359), *Memoirs of the European Mathematical Society* **11** (2024), DOI 10.4171/MEMS/11, Introduction p.6, Conjecture 6 and equation (1.8); Section 1.6.2, Remark 41. The source gives the definitions, partial results and exact conjecture.
2. M. A. Gunes and A. Naor, [*The separation modulus of unitarily invariant matrix norms*](https://arxiv.org/html/2508.03853), arXiv:2508.03853 (2025), Introduction. A later constant-factor result for a particular family of spaces.

## Status review


**Known cases:** The target is a constant-factor relation for every finite-dimensional normed space whose isometry commutant is scalar. Coordinate-symmetric, matrix-norm and restricted polytope results do not cover that full symmetry class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is a constant-factor relation for every finite-dimensional normed space whose isometry commutant is scalar. Coordinate-symmetric, matrix-norm and restricted polytope results do not cover that full symmetry class.

Additional comparison sources: [comparison source 1](https://ems.press/content/book-files/47359); [comparison source 2](https://arxiv.org/html/2508.03853); [comparison source 3](https://doi.org/10.1112/mtk.70070). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The later matrix-norm result and [restricted 2026 convex-polytope result](https://doi.org/10.1112/mtk.70070) do not cover every normed space with enough symmetries. This is distinct from the [Euclidean Lipschitz-extension modulus question](764-growth-of-the-euclidean-lipschitz-extension-modulus.md) already listed here. The [bounded status, announcement and duplicate review](../FURTHER_problems/_tracking/naor-separation-modulus-symmetry-status-2026-10-21.json) found no matching complete result; it cannot rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-24a48a1ec991ddab**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
