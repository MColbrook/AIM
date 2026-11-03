# 790. Regular cylindrical decompositions in fixed coordinates

**Area:** Real algebraic geometry and computational topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each $`n\geq1`$ and each closed bounded semialgebraic set $`S\subset\mathbb R^n`$, fix an ordering of the coordinate axes. Must there be a finite cylindrical algebraic decomposition $`\mathcal P`$ of $`\mathbb R^n`$, in that order, such that $`S`$ is a union of its cells and every cell $`C\subset S`$ is topologically regular?

A cylindrical decomposition is built inductively from points and open intervals, then graphs of finitely many ordered continuous semialgebraic functions over each lower-dimensional cell and the intervening open bands, including outer bands. For $`d=\dim C`$, regularity means

```math
(\overline C,C)\cong(\overline B^{d},B^{d}),
```

where $`B^d`$ is the open unit ball. The homeomorphism is topological. The order stays fixed throughout. No frontier condition or algorithmic complexity bound is added.

## Application

Semialgebraic sets encode continuous polynomial constraints. Controlled cell topology would improve their geometric descriptions, including configuration spaces used in motion planning [1].

## References

1. J. H. Davenport, A. F. Locatelli and G. K. Sankaran, *Regular cylindrical algebraic decomposition*, [arXiv:1803.04029v1](https://arxiv.org/html/1803.04029v1), Question 1.1(i), Definitions 2.4, 3.1 and 3.4. Published in *Journal of the London Mathematical Society* 101 (2020), 43–59, [DOI](https://doi.org/10.1112/jlms.12257); online 2019. The eligible statement used here is the exact 2018 preprint.
2. S. Basu, A. Gabrielov and N. Vorobjov, *Triangulations of monotone families I: Two-dimensional families*, [arXiv:1402.0460v2](https://arxiv.org/html/1402.0460v2), introduction and Theorem 3.20.
3. H. Baker, *Cylindrical Algebraic Decompositions With Monotone Cells*, University of Bath PhD thesis, award 2025; title page dated August 2024. [Repository PDF](https://purehost.bath.ac.uk/ws/portalfiles/portal/360721124/submit-final.pdf), printed pp.196–197.
4. L. Michel, *On some Exotic Cylindrical Algebraic Decompositions and Cells*, [arXiv:2601.09795v1](https://arxiv.org/html/2601.09795v1), Theorem 2.2 and Propositions 3.7, 3.10 and 3.12.

## Status review


**Known cases:** The target is existence of a regular CAD in one fixed coordinate order. Strong well-based conditional theorems, generic coordinate changes, frontier conditions and nonregular supplied decompositions do not establish or refute that existence statement.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is existence of a regular CAD in one fixed coordinate order. Strong well-based conditional theorems, generic coordinate changes, frontier conditions and nonregular supplied decompositions do not establish or refute that existence statement.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/1803.04029v1); [comparison source 2](https://doi.org/10.1112/jlms.12257); [comparison source 3](https://arxiv.org/html/1402.0460v2); [comparison source 4](https://purehost.bath.ac.uk/ws/portalfiles/portal/360721124/submit-final.pdf); [comparison source 5](https://arxiv.org/html/2601.09795v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The dimension-at-most-two case is covered by [2]. A sufficient criterion in [1, Theorem 3.11] assumes reduced, well-based and strong hypotheses; it does not give existence for every input.

Baker [3] constructs the frontier condition in arbitrary dimension and discusses extending the fixed-order regular construction. Frontier incidence and ball-shaped closures are different requirements. Discussions of three-dimensional constructions require care about using one coordinate order throughout; no broader low-dimensional theorem is asserted here.

Michel [4] disproves several nearby implications about a supplied decomposition or cell. A nonregular example does not show that every decomposition of the same set must fail. Those results do not settle the existential question above.

Bounded primary-source and announcement searches through 25 October 2026 found no matching general resolution. This is a dated literature assessment, not exhaustive absence or proof certification. Selected definitions and theorem statements were read; whole articles and thesis were not reviewed.

Semantic comparisons used the 1,702-row all-status AIM/OpenAI index and current 887 findings. Nearby triangulation, persistence, universal-cover and derived-category questions have different targets. Fresh AIM-head/OpenAI-CONTENTS metadata agrees with the retained snapshot. A live Prove2Me search located no matching target, but full mission-catalogue clearance remains unverified.

**Admission review:** 25 October 2026. The recorded primary-statement, current-status and semantic duplicate checks were completed before admission. Public AIM-head and complete OpenAI-CONTENTS comparisons were refreshed without a change. The dated, bounded search and access limits above remain part of this assessment.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-52169073ac293a11**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
