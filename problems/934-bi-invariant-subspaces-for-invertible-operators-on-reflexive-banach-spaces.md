# 934. Bi-invariant subspaces for invertible operators on reflexive Banach spaces

**Area:** Operator theory and Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be any infinite-dimensional complex reflexive Banach space and let $`A:X\to X`$ be a bounded invertible complex-linear operator. Must there be a norm-closed linear subspace $`M`$ such that
```math
\{0\}\subsetneq M\subsetneq X,
 \qquad A(M)=M?
```

The equality means that the **same** nontrivial subspace is invariant under both $`A`$ and $`A^{-1}`$. Equivalently, must every bounded-operator representation of the discrete group $`\mathbb Z`$ on such an $`X`$ be reducible? This is Atzmon's question for $`\mathbb Z`$ [1, Introduction and Section 4].

## Application

A common invariant subspace gives a proper closed component preserved by every forward and backward iterate of a reversible linear evolution. The question tests how much reflexivity alone constrains such decompositions, beyond special spectral, symmetry or growth hypotheses.

## Known results and scope

Atzmon proves a sufficient criterion [1, Theorem 6] when an additional conjugate-linear involution intertwines $`A`$ with $`A^{-1}`$ and suitable matrix coefficients are positive definite. Weighted translation examples satisfying further symmetry are covered by that criterion. These assumptions are absent from the universal question. A subspace with only $`A(M)\subseteq M`$ does not suffice. Results for nonreflexive spaces do not decide this reflexive-space formulation.

## References

1. A. Atzmon, [*Reducible representations of abelian groups*](https://www.numdam.org/item/10.5802/aif.1859.pdf), *Annales de l'Institut Fourier* **51** (2001), no. 5, 1407–1418, [doi:10.5802/aif.1859](https://doi.org/10.5802/aif.1859). The introduction, printed p. 1407, and Section 4, printed p. 1415, state the universal reflexive bi-invariance question; Theorem 6 gives an additional-hypothesis result.
2. C. Cheng, X. Fang and J. Jiang, [*On the third problem of Halmos on Banach spaces*](https://arxiv.org/abs/2203.14670), arXiv:2203.14670. This treats related but distinct inverse-intransitivity questions and conditional operator classes.

## Status review


**Known cases:** The target is a common nontrivial closed subspace invariant under both an invertible operator and its inverse on every reflexive complex space. One-sided invariant-subspace announcements, nonreflexive examples and conditional Atzmon results do not settle it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is a common nontrivial closed subspace invariant under both an invertible operator and its inverse on every reflexive complex space. One-sided invariant-subspace announcements, nonreflexive examples and conditional Atzmon results do not settle it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

No matching complete proof, counterexample or announced resolution of the exact universal statement was located in bounded searches through 21 October 2026. Enflo's [2023 announced Hilbert-space result](https://arxiv.org/abs/2305.15442) concerns ordinary one-sided invariant subspaces, so it does not resolve the common-subspace question for all reflexive Banach spaces. The related Halmos results in [2] have different hypotheses. Searches of AIM and admitted FURTHER pages found no duplicate. These checks do not certify exhaustive absence of a solution.

The [primary-source audit](../FURTHER_problems/_tracking/atzmon-reflexive-biinvariant-primary-2026-10-21.json), [current-status audit](../FURTHER_problems/_tracking/atzmon-reflexive-biinvariant-status-2026-10-21.json), and [duplicate/scope audit](../FURTHER_problems/_tracking/atzmon-reflexive-biinvariant-duplicates-2026-10-21.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f83ff8d1cebc0b80**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
