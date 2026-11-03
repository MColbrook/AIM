# 1036. Does absolute PPT imply absolute separability?

**Area:** Quantum information and matrix analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`m,n\geq3`$ and let $`\rho\in M_m(\mathbb C)\otimes M_n(\mathbb C)`$ be a bipartite density matrix: $`\rho\geq0`$ and $`\mathrm{Tr}\rho=1`$. Say that $`\rho`$ is **absolutely PPT** if, for every global unitary $`U\in U(mn)`$,

```math
(\mathrm{id}_m\otimes\mathrm{transpose})(U\rho U^*)\geq0.
```


Say that $`\rho`$ is **absolutely separable** if $`U\rho U^*`$ is separable for every such $`U`$: it can be expressed as a convex combination of positive product states on $`\mathbb C^m\otimes\mathbb C^n`$.

**Question.** Must every absolutely PPT state be absolutely separable? Equivalently, do the two spectral sets coincide for every pair of local dimensions? A counterexample may be sought in any $`m,n\geq3`$. The converse implication is automatic because separable states have positive partial transpose. The $`2\otimes n`$ case is already known, which is why the stated question starts at three on each side.

## Application

Absolute separability asks whether a bipartite state's eigenvalues alone guarantee that no global unitary can create entanglement. Absolute PPT has a finite semidefinite characterization in terms of those eigenvalues. If the classes coincide, that characterization would decide this robust separability property; a counterexample would show its exact limitation.

## References

1. S. Arunachalam, N. Johnston and V. Russo, *Is absolute separability determined by the partial transpose?*, **Quantum Information & Computation** 15(7–8) (2015), 694–720. [Published PDF](https://www.rintonpress.com/xxqic15/qic-15-78/0694-0720.pdf), §4, Question 1 on printed p. 699; [author page](https://njohnston.ca/publications/is-absolute-separability-determined-by-the-partial-transpose/). The paper proves selected special cases and necessary conditions.
2. A. Patra and B. C. Hiesmayr, [*On the separability of Bell-diagonal states with absolutely positive partial transposition*](https://arxiv.org/abs/2610.12000), arXiv:2610.12000v1 (8 October 2026). The abstract explicitly retains the general question and proves basis-specific Bell-diagonal results.
3. J. Louvet, E. Serrano-Ensástiga, T. Bastin and J. Martin, *Nonequivalence between absolute separability and positive partial transposition in the symmetric subspace*, **Physical Review A** 111 (2025), 042418. [DOI](https://doi.org/10.1103/PhysRevA.111.042418), [author version](https://arxiv.org/abs/2411.16461v2). The counterexamples use a different symmetric-state setting and do not answer the ordinary bipartite question.

## Status review


**Known cases:** The full ordinary bipartite APPT class in dimensions at least three is required. The October Bell-diagonal theorem is basis-specific, and symmetric-subspace nonequivalence is a different definition.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The full ordinary bipartite APPT class in dimensions at least three is required. The October Bell-diagonal theorem is basis-specific, and symmetric-subspace nonequivalence is a different definition.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2015 paper asks the equivalence for all bipartite dimensions and notes that it holds when one local dimension is two. Later results settle some structured state families, but the 8 October 2026 Patra–Hiesmayr abstract still describes the unrestricted question as unresolved. The symmetric-subspace counterexamples in [3] do not transfer to global unitaries on the full bipartite matrix algebra. Bounded searches through 20 October 2026 found no matching complete proof, counterexample or announcement; they cannot certify exhaustive absence. AIM032 and AIM206 concern different PPT/entanglement questions, and no matching FURTHER entry was found.

The [source review](../FURTHER_problems/_tracking/absolute-ppt-primary-review-2026-10-20.json), [current-status check](../FURTHER_problems/_tracking/absolute-ppt-current-review-2026-10-20.json), [semantic comparison](../FURTHER_problems/_tracking/absolute-ppt-duplicates-review-2026-10-20.json) and [coordinator decision](../FURTHER_problems/_tracking/absolute-ppt-coordinator-review-2026-10-20.json) give the selected evidence and limits. They do not verify every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-46a04b9f961f5a43**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
