# 045. Is there a uniform polynomial bound for three commuting contractions?

**Area:** Operator theory and multivariable functional calculus
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`H`$ be any complex Hilbert space, and let $`T_1,T_2,T_3\in B(H)`$ be pairwise commuting contractions. For a scalar polynomial $`p\in\mathbb C[z_1,z_2,z_3]`$, put

```math
\|p\|_{\infty,\mathbb D^3}=\sup_{|z_1|,|z_2|,|z_3|\leq 1}|p(z_1,z_2,z_3)|.
```


**Question (Paulsen, Chapter 5).** Is there a finite constant $`K_3`$, independent of $`H`$, the commuting triple and $`p`$, such that

```math
\|p(T_1,T_2,T_3)\|\leq K_3\,\|p\|_{\infty,\mathbb D^3}
```


for **every** scalar polynomial $`p`$? Paulsen asks the analogous question for each fixed number $`n`$ of commuting contractions. This entry isolates $`n=3`$, the first unresolved case. The bound with $`K_3=1`$ is already false; the question allows an unspecified finite constant.

## Application

A positive answer would give a bounded polynomial functional calculus, uniformly over all commuting contraction triples, in terms of the supremum norm on the tridisc. Equivalently, it would make the scalar Schur–Agler and supremum norms comparable in three variables. A negative answer would exhibit scalar polynomials and contraction triples with arbitrarily large norm ratios.

## References

1. V. Paulsen, [*Completely Bounded Maps and Operator Algebras*](https://www.cambridge.org/core/books/completely-bounded-maps-and-operator-algebras/47AF05B5F924ADE4FA30770B10050B76/listing), Cambridge Studies in Advanced Mathematics 78, Cambridge University Press, first printed 2003, Chapter 5, printed p. 64. [Read-copy source](https://ndl.ethernet.edu.et/bitstream/123456789/77329/1/55.pdf).
2. M. Hartz, [*On von Neumann's inequality on the polydisc*](https://doi.org/10.1007/s00208-024-03040-2), *Mathematische Annalen* **391** (2025), 5235–5264, Theorem 1.1 and its following paragraph.
3. M. Hartz and Y. Wang, [*On the Schur–Agler Norm*](https://arxiv.org/pdf/2602.14047v1), arXiv:2602.14047v1 (17 February 2026), introduction, pp. 1–2.

## Status review

Hartz proves a degree-independent bound for **homogeneous** polynomials in three variables and explicitly says this does not settle the bound for arbitrary polynomials. Hartz and Wang still describe finiteness of the general three-variable constant as unknown in February 2026. A [2026 matrix-tuple result](https://arxiv.org/abs/2610.20355) has a constant depending on matrix size, so it does not provide Paulsen's dimension-independent bound. Paulsen's following matrix-polynomial question concerns a stronger norm and is kept separate here. Focused searches for a later complete proof, counterexample or announced resolution through 2026-10-22 found none; the search is bounded. No equivalent target was found in local AIM problems or admitted FURTHER entries. The [original-body receipt](../FURTHER_problems/_tracking/paulsen-polydisc-constant-original-2026-10-22.json) and [status audit](../FURTHER_problems/_tracking/paulsen-polydisc-constant-status-2026-10-22.json) record the source version and scope checks.


### Online recheck, 2026-10-30

The uniform constant for arbitrary scalar polynomials and arbitrary Hilbert-space dimension is still distinguished from Hartz's homogeneous-polynomial theorem. The July 2026 Szász paper also says norm equivalence is unknown; no later complete result found.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/s00208-024-03040-2); [status source 2](https://arxiv.org/abs/2602.14047); [status source 3](https://link.springer.com/article/10.1007/s00020-026-02847-9). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-d349125a92ada493** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
