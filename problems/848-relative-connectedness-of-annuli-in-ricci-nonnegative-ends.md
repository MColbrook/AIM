# 848. Relative connectedness of annuli in Ricci-nonnegative ends

**Area:** Geometric analysis and heat kernels on manifolds
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a complete, noncompact Riemannian manifold without boundary whose Ricci curvature is nonnegative outside a compact set. It has finitely many ends [1, Proposition 7.10]. Represent an individual end by a complete manifold $`M_i`$ that agrees outside a compact region with the corresponding unbounded component of $`M\setminus K`$, as in [1, Definition 7.7].

Must **every** $`M_i`$ have *relatively connected annuli* (RCA)? In the notation of [1, Definition 5.1], this asks whether there are a basepoint $`o_i`$ and a constant $`C_A>1`$ such that, for every $`r\geq C_A^2`$ and any $`x,y\in M_i`$ at distance $`r`$ from $`o_i`$, a continuous path from $`x`$ to $`y`$ stays in
```math
B_{M_i}(o_i,C_A r)\setminus B_{M_i}(o_i,r/C_A).
```

This is the endwise question of [1, Remark 7.11]; it does not require a manifold with several ends to satisfy RCA as a whole.

## Application

RCA permits comparison of geometry and analysis around large annuli. Combined with curvature assumptions, it leads to volume comparison, doubling, Poincaré inequalities and Harnack estimates on ends [1, Proposition 7.10 and Corollary 7.13]. An affirmative answer would remove a separate geometric hypothesis from such estimates for this Ricci-curvature class.

## Known results and scope

The source proves RCA for ends under asymptotically nonnegative **sectional** curvature, and under nonnegative Ricci curvature outside a compact set **together with finite first Betti number** [1, Proposition 7.8]. Its more general Proposition 7.10 gives volume comparison *if* an end has RCA. Neither implication answers Remark 7.11 without those extra assumptions. Multi-ended connected sums illustrate why RCA of the whole manifold is a different demand.

## References

1. A. Grigor'yan and L. Saloff-Coste, [*Stability results for Harnack inequalities*](https://www.numdam.org/item/10.5802/aif.2116.pdf), *Annales de l'Institut Fourier* **55** (2005), no. 3, 825–890, [doi:10.5802/aif.2116](https://doi.org/10.5802/aif.2116). Definitions 5.1 and 7.7, Propositions 7.8 and 7.10, Remark 7.11, and Corollary 7.13.
2. A. Grigor'yan and L. Saloff-Coste, [*Heat kernel on manifolds with ends*](https://www.numdam.org/item/10.5802/aif.2480.pdf), *Annales de l'Institut Fourier* **59** (2009), no. 5, 1917–1997. Its Ricci-outside-compact example continues to assume RCA on each end.

## Status review


**Known cases:** The source proves endwise relatively connected annuli with finite first Betti number or stronger asymptotically nonnegative sectional curvature. Later heat-kernel and Riesz-transform applications retain RCA as an extra premise; these are not proofs of the unrestricted Ricci-outside-compact implication.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source proves endwise relatively connected annuli with finite first Betti number or stronger asymptotically nonnegative sectional curvature. Later heat-kernel and Riesz-transform applications retain RCA as an extra premise; these are not proofs of the unrestricted Ricci-outside-compact implication.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded searches through 21 October 2026 found no complete resolution or matching announcement of the exact endwise assertion. In the 2009 continuation [2], RCA remains an explicit additional hypothesis for the Ricci-outside-compact example. A [September 2026 Riesz-transform paper](https://arxiv.org/abs/2609.23398) likewise assumes RCA on its components, but that separate setting does not prove the question open. AIM and admitted FURTHER pages contained no equivalent target. These checks cannot rule out unindexed work.

The [primary-source audit](../FURTHER_problems/_tracking/ricci-end-annuli-primary-2026-10-21.json), [current-status audit](../FURTHER_problems/_tracking/ricci-end-annuli-status-2026-10-21.json), and [duplicate/scope audit](../FURTHER_problems/_tracking/ricci-end-annuli-duplicates-2026-10-21.json) record the selected evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d42e81c2afb0b2b0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
