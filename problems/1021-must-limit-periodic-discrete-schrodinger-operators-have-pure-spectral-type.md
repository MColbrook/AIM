# 1021. Must limit-periodic discrete Schrödinger operators have pure spectral type?

**Area:** Spectral theory and aperiodic media
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Let $`V:\mathbb Z\to\mathbb R`$ be a bounded uniform limit of periodic sequences, and define the bounded self-adjoint operator on $`\ell^2(\mathbb Z)`$ by
```math
(H_Vu)(n)=u(n-1)+u(n+1)+V(n)u(n).
```

Must its spectral type be pure? Precisely, in the canonical decomposition
```math
\ell^2(\mathbb Z)=\mathcal H_{\mathrm{pp}}(H_V)\oplus
\mathcal H_{\mathrm{ac}}(H_V)\oplus\mathcal H_{\mathrm{sc}}(H_V),
```

must at most one summand be nonzero?

This is Damanik–Fillman, Question 10.1, in the discrete Schrödinger setting specified in their introduction. The summands denote pure-point, absolutely continuous and singular continuous spectral subspaces. Pure-point spectrum means a complete eigenvector system; compact resolvent is not required.

## Application

These operators model waves or particles in media approximated uniformly by periodic structures. The question asks whether distinct spectral mechanisms can coexist in one such operator.

## References

1. D. Damanik and J. Fillman, [*Spectral Properties of Limit-Periodic Operators*](https://arxiv.org/pdf/1802.05794), v1 (2018), Introduction and Question 10.1, p.36; Chapter 15 in *Analysis and Geometry on Graphs and Manifolds*, LMS Lecture Note Series **461** (2020), 382–444. [DOI](https://doi.org/10.1017/9781108615259.016).
2. M. Gomez Solis, [*A note on the absolutely continuous spectrum of limit-periodic Jacobi matrices*](https://arxiv.org/html/2610.19416), v1, 14 October 2026, Definitions 1.1–1.3 and Theorem 1.2.

3. M. J. Colbrook, [*A limit-periodic Schrödinger operator with mixed absolutely continuous and singular continuous spectrum*](../research/solutions/1021-limit-periodic-mixed-spectrum/limit_periodic_mixed_spectrum.pdf), 3 November 2026. [TeX source](../research/solutions/1021-limit-periodic-mixed-spectrum/limit_periodic_mixed_spectrum.tex), [solution package](../research/solutions/1021-limit-periodic-mixed-spectrum/README.md), and [independent AI mathematical review](../research/solution_reviews/2026-11-03-aim1021/1021-review.md).

## Status review

**Outcome:** Counterexample.

**Resolution, 2026-11-03:** Colbrook constructs a bounded real limit-periodic potential for which the stated discrete Schrödinger operator has nonzero absolutely continuous and singular continuous spectral subspaces and no eigenvalues. Both continuous types occur in the spectral measure of the same vector. Thus the answer to the purity question is negative.

The construction starts from the period-three potential $`(100,0,0)`$ and uses nested periodic approximants. Slow cellwise modulations preserve a positive density on a fixed positive-measure compact set, while long forbidden plateaus make a separate isolated spectral cluster narrow enough to have zero measure in the limit. Exact local three-block repetitions exclude eigenvalues, so that nonempty singular cluster is singular continuous.

The [independent AI review](../research/solution_reviews/2026-11-03-aim1021/1021-review.md) checked the complete proof against the current target, including the Floquet density, adiabatic estimate and margin, barrier estimate, inductive parameter order, spectral-measure limit, persistence of the singular cluster, and exact Gordon repetitions. All four references were checked in primary texts; 35 exact supporting identities and inequalities passed in normal and optimized Python. The review was performed by Codex (AI); no human peer review or Lean verification is asserted. The distinct hull-element and coupling questions are not claimed to be resolved.

### Earlier status checks, through 2026-10-30

Every uniform limit of periodic discrete potentials is allowed. Dense examples of each pure class and the October pure-absolute-continuity theorem under an exponential approximation condition do not exclude mixed spectra generally.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

All three pure spectral types occur in the source, even densely among limit-periodic potentials. That does not settle whether mixed types occur.

The October 2026 result proves pure absolute continuity under a particular exponential approximation-rate condition. It does not cover arbitrary uniform limits. Random Anderson-model and quasiperiodic results also have different hypotheses.

The [coordinating review](../FURTHER_problems/_tracking/focused-limit-periodic-spectral-purity-D030-C179-Root-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, current-announcement and semantic duplicate checks, with an independent formulation review. These bounded checks do not prove continued openness. Questions about varying the hull element or coupling constant are separate source questions.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8b7a9f3341559561**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
