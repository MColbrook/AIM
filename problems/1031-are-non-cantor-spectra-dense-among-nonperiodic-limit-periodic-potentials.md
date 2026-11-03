# 1031. Are non-Cantor spectra dense among nonperiodic limit-periodic potentials?

**Area:** Spectral theory and aperiodic media
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Let $`\mathrm{LP}_{\mathrm{np}}`$ be the bounded real sequences on $`\mathbb Z`$ that are uniform limits of periodic sequences and are themselves nonperiodic. Set
```math
(H_Vu)(n)=u(n-1)+u(n+1)+V(n)u(n)
\quad\text{on }\ell^2(\mathbb Z).
```

For every $`V\in\mathrm{LP}_{\mathrm{np}}`$ and $`\varepsilon>0`$, does there exist $`W\in\mathrm{LP}_{\mathrm{np}}`$ such that
```math
\|W-V\|_\infty<\varepsilon,
\qquad \mathrm{int}\sigma(H_W)\ne\varnothing?
```

This is Damanik–Fillman Question 10.4. These spectra are compact and perfect, so having nonempty interior is equivalent here to failing to be a Cantor set. The approximating potential $`W`$ must remain nonperiodic; its entire spectrum need not be a single interval.

## Application

The problem tests whether spectral bands can persist under arbitrarily small changes of a uniformly aperiodic medium, alongside the known abundance of Cantor spectra.

## References

1. D. Damanik and J. Fillman, [*Spectral Properties of Limit-Periodic Operators*](https://arxiv.org/html/1802.05794v1), Section 4 and Question 10.4, p.36; Chapter 15 in *Analysis and Geometry on Graphs and Manifolds*, LMS Lecture Note Series **461** (2020), 382–444. [DOI](https://doi.org/10.1017/9781108615259.016).
2. D. Damanik, Z. Gan and H. Krüger, [*Limit-periodic Schrödinger operators with a discontinuous Lyapunov exponent*](https://doi.org/10.1016/j.jfa.2020.108565), *Journal of Functional Analysis* **279** (2020), 108565, Theorem 1.3.
3. M. J. Colbrook, [*Dense nonperiodic limit-periodic potentials with finite interval spectra*](../research/solutions/1031-limit-periodic-finite-interval-spectra/aim1031.pdf), 3 November 2026. [TeX source](../research/solutions/1031-limit-periodic-finite-interval-spectra/aim1031.tex), [package and reproduction](../research/solutions/1031-limit-periodic-finite-interval-spectra/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-spectral-batch/1031-review.md).

## Status review

**Outcome:** Affirmative proof.

**Reviewed result, 2026-11-03:** Nonperiodic limit-periodic potentials with finite unions of nondegenerate spectral intervals are dense among all limit-periodic potentials. The [manuscript](../research/solutions/1031-limit-periodic-finite-interval-spectra/aim1031.pdf) and [individual audit](../research/solution_reviews/2026-11-03-spectral-batch/1031-review.md) record the proof, checked references and exact target comparison. Review was performed by Codex (AI).

### Earlier status check, 2026-10-30

The nearby potential must stay nonperiodic and have spectral interior. Dense periodic spectra, positive-measure Cantor spectra and particular non-Cantor examples do not imply density in this class.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Specific nonperiodic examples with non-Cantor spectra are known. Dense periodic potentials do not answer this question. Neither do dense potentials with discontinuous Lyapunov exponents, positive-measure spectra or purely absolutely continuous spectral type.

The [coordinating review](../FURTHER_problems/_tracking/focused-nonCantor-LP-density-D030-C179-Root-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary-source, latest-version, current-resolution/announcement and semantic duplicate checks, including an independent formulation review. The formulation uses the archived chapter; full published-body parity is not asserted. These bounded checks do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f21752e16a430439**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
