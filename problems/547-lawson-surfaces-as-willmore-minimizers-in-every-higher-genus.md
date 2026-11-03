# 547. Lawson surfaces as Willmore minimizers in every higher genus

**Area:** Geometric analysis and bending-energy minimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

For each integer $`g\ge2`$, let $`\xi_{g,1}\subset S^3`$ be Lawson's embedded minimal surface of genus $`g`$, in the unit round three-sphere. Is every smooth closed connected orientable embedded surface $`M\subset S^3`$ of genus $`g`$ subject to
```math
W(M):=\int_M(1+H^2)\,dA\ \ge\ \mathrm{area}(\xi_{g,1}),
```

with equality if and only if $`M`$ is an ambient Möbius image of $`\xi_{g,1}`$? Here $`H=(k_1+k_2)/2`$ is the scalar mean curvature. There is no symmetry or conformal-class restriction on $`M`$.

This is the higher-genus conjecture stated in Kusner–Lü–Wang's Introduction, physical pp.1–2 of the pinned author version. The equality clause is part of the question.

## Application

The question asks which shape minimizes a curvature-based bending energy when topology is fixed. It provides a sharp benchmark for geometric variational methods and numerical surface optimization.

## References

1. Rob Kusner, Ying Lü and Peng Wang, *The Willmore Problem for Surfaces with Symmetry*, Journal of Geometric Analysis **36** (2026), article305. [Published article](https://doi.org/10.1007/s12220-026-02501-1); [author version2410.12582v2](https://arxiv.org/abs/2410.12582v2), Introduction and Theorem1.1, physical pp.1–3.
2. Jacob Bernstein and Daniel Ketover, *On the Willmore energy of Möbius bands*, [arXiv:2609.26745](https://arxiv.org/abs/2609.26745) (2026), abstract. This concerns a different topology and boundary condition.

## Status review

The July2026 published abstract explicitly retains the unrestricted higher-genus conjecture. Theorem1.1 in the inspected author version assumes a specified symmetry group. Fixed-conformal-class minimization and local stability also leave the displayed unrestricted comparison open. The genus-one Willmore theorem does not settle this question.

Current searches located no matching complete solution or announcement. A similarly titled2024 author upload about Willmore action was checked in selected sections; it does not announce the required global theorem. No equivalent AIM, OpenAI-result or existing FURTHER target was identified in the recorded comparisons and cached catalogue-description checks.

The [coordinator review](../FURTHER_problems/_tracking/lawson-willmore-coordinator-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/lawson-willmore-current-review-2026-10-19.json), [duplicate comparison](../FURTHER_problems/_tracking/lawson-willmore-duplicates-review-2026-10-19.json) and [independent scope audit](../FURTHER_problems/_tracking/parallel/continuum/cross-lawson-kusner-genus-willmore-review.json) record the bounded evidence. Only the author PDF's first three physical pages and the published abstract were read for the main source; the final published body was not inspected. These checks do not certify absence of every possible resolution.


### Online recheck, 2026-10-30

The 2026 surfaces-with-symmetry result retains group symmetry. Fixed-conformal-class, higher-codimension and other-topology statements do not prove the unrestricted genus-g Lawson lower bound with its equality classification.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2410.12582); [status source 2](https://doi.org/10.1007/s12220-026-02501-1). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ef7b1502c4175743** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
