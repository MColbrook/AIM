# 1020. Can coupling change the spectral type of a limit-periodic Schrödinger operator?

**Area:** Spectral theory and aperiodic media
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a bounded real sequence $`V`$ that is a uniform limit of periodic sequences. On $`\ell^2(\mathbb Z)`$ set
```math
(H_\lambda u)(n)=u(n-1)+u(n+1)+\lambda V(n)u(n).
```

Let $`T_V(\lambda)\subset\{\mathrm{pp},\mathrm{ac},\mathrm{sc}\}`$ record which pure-point, absolutely continuous and singular continuous spectral subspaces of $`H_\lambda`$ are nonzero.

Can there exist such a **fixed** $`V`$ and $`0<\lambda_1<\lambda_2`$ with $`T_V(\lambda_1)\ne T_V(\lambda_2)`$?

This specifies Damanik–Fillman Question 10.3. Zero coupling is excluded. Positive couplings suffice: the unitary map $`(Su)(n)=(-1)^nu(n)`$ gives $`SH_\lambda S=-H_{-\lambda}`$, and spectral reflection preserves these three types.

## Application

The question tests whether changing the strength of one aperiodic medium can change its spectral mechanism, without changing its spatial pattern.

## References

1. D. Damanik and J. Fillman, [*Spectral Properties of Limit-Periodic Operators*](https://arxiv.org/pdf/1802.05794), v1 (2018), Introduction and Question 10.3, p.36; Chapter 15 in *Analysis and Geometry on Graphs and Manifolds*, LMS Lecture Note Series **461** (2020), 382–444. [DOI](https://doi.org/10.1017/9781108615259.016).
2. M. Gomez Solis, [*A note on the absolutely continuous spectrum of limit-periodic Jacobi matrices*](https://arxiv.org/html/2610.19416v1), 14 October 2026, Definition 1.3 and Theorem 1.2.

## Status review


**Known cases:** A single fixed limit-periodic potential must change basic spectral class at two positive couplings. Quasiperiodic block-product models, spectral-support changes and restricted fast approximation theorems do not give this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A single fixed limit-periodic potential must change basic spectral class at two positive couplings. Quasiperiodic block-product models, spectral-support changes and restricted fast approximation theorems do not give this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The October 2026 theorem assumes a particular exponential approximation rate; it does not settle this unrestricted coupling question. Moving eigenvalues or spectral supports also does not establish a change in $`T_V`$.

[Single-operator purity](1021-must-limit-periodic-discrete-schrodinger-operators-have-pure-spectral-type.md) and [classification across the hull](1018-can-spectral-type-vary-within-a-limit-periodic-schrodinger-hull.md) are separate questions. The [coordinating review](../FURTHER_problems/_tracking/focused-limit-periodic-coupling-type-D030-C179-Root-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary-source, latest-version, current-resolution/announcement and semantic duplicate checks, including an independent formulation review. These bounded checks do not prove continued openness. The precise formulation uses the archived preprint; full parity with the published chapter is not asserted.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8786a09fd67a0031**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
