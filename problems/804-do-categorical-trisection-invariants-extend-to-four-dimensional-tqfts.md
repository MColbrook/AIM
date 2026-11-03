# 804. Do categorical trisection invariants extend to four-dimensional TQFTs?

**Area:** Geometric topology; mathematical quantum field theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Meusburger, Mulevicius and Torzewska associate a number $`Z_{\mathcal D}(X)`$ to each closed oriented smooth four-manifold $`X`$ from categorical data $`\mathcal D`$: three spherical fusion categories, an indecomposable finite semisimple bimodule category over two of them with a bimodule trace, and a pivotal functor from the third into its spherical category of bimodule endofunctors. A labelled trisection diagram computes the invariant; the authors prove it is unchanged by the relevant diagram moves.

For **general admissible data** $`\mathcal D`$, can $`Z_{\mathcal D}`$ be extended to a four-dimensional topological quantum field theory? Concretely, can one assign compatible state spaces to closed oriented three-manifolds and maps to four-dimensional cobordisms, satisfying the gluing and monoidal axioms, with the assigned scalar on every closed $`X`$ equal to $`Z_{\mathcal D}(X)`$? If not for all inputs, identify precisely which categorical data admit such an extension or an obstruction. The known Crane–Yetter realizations for particular data do not answer the general-input question.

## Application

A TQFT extension would make the closed-manifold number compatible with cutting and gluing four-manifolds along three-dimensional boundaries. It could connect trisection diagram calculations to state spaces and cobordism maps used in quantum topology. The question does not require a fully extended theory assigning data to points.

## References

1. C. Meusburger, V. Mulevicius and F. Torzewska, [*Categorical 4-manifold invariants from trisection diagrams*](https://arxiv.org/abs/2511.19384), arXiv:2511.19384v1 (2025), introduction, “Open questions,” and Theorem 4.28. Gives the general closed-manifold construction and notes that its four-dimensional TQFT origin remains unknown, even for the Bärenz–Barrett special case.
2. C. Meusburger, “Trisection invariants of four-manifolds,” in D. Reutter, S. Schafer-Nameki and C. Schweigert (eds.), [*Higher Structures from Symmetries in Quantum Field Theory*](https://doi.org/10.4171/OWR/2026/12), *Oberwolfach Reports* **23** (2026), no. 1, 737–794, contribution printed pp. 767–768, especially “Open Questions” on p. 768. Explicitly raises the TQFT extension and the boundary-gluing issue.

## Status review


**Known cases:** Categorical trisection closed-four-manifold scalars and special Crane-Yetter identifications do not construct compatible boundary state spaces and gluing for all the admissible categorical data. The general TQFT extension remains unmatched.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Categorical trisection closed-four-manifold scalars and special Crane-Yetter identifications do not construct compatible boundary state spaces and gluing for all the admissible categorical data. The general TQFT extension remains unmatched.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2025 primary paper realizes particular data through Crane–Yetter-type invariants, yet asks whether its general construction arises from a four-dimensional TQFT. The authors repeated the question in the July 2026 workshop report. Other four-dimensional TQFT constructions do not, by themselves, give boundary states and gluing maps for this entire family. A bounded search through 2026-10-22 located no general proof, counterexample or matching announcement. The [read journal passage](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0645-J050-J279-cached-backfill-body-review.json), [current-status audit](../FURTHER_problems/_tracking/trisection-invariant-tqft-status-2026-10-22.json) and [duplicate audit](../FURTHER_problems/_tracking/trisection-invariant-tqft-duplicates-2026-10-22.json) give the precise scope and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-791b40a8a029edcb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
