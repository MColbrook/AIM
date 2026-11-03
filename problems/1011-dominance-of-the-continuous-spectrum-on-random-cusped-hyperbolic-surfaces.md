# 1011. Dominance of the continuous spectrum on random cusped hyperbolic surfaces

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`k(g)\ge1`$ be integers with $`k(g)=o(\sqrt g)`$. Sample a complete oriented finite-area hyperbolic surface $`X`$ of genus $`g`$ with $`k(g)`$ cusps from normalized Weil–Petersson volume $`\mathbb P_{g,k(g)}`$ on its moduli space. Fix $`I=[a,b]`$ with $`1/4<a<b<\infty`$.

Let $`N(X,I)`$ count the discrete eigenvalues of the nonnegative scalar Laplacian in $`I`$, with multiplicity. Write $`\Phi_X(s)`$ for the cusp scattering matrix in the usual period-one cusp normalization and $`\varphi_X(s)=\det\Phi_X(s)`$. Thus its coefficients occur in the constant terms $`\delta_{bc}y^s+\Phi_{bc}(s)y^{1-s}`$ of the Eisenstein series. Put

```math
\tau(r)=\frac14+r^2,\qquad
M(X,I)=\frac1{4\pi}\int_{\tau^{-1}(I)}
-\frac{\varphi_X'(1/2+ir)}{\varphi_X(1/2+ir)}\,dr.
```


The inverse image uses real $`r`$ of both signs; the prime differentiates in $`s`$. Does every $`\varepsilon>0`$ satisfy

```math
\mathbb P_{g,k(g)}\!\left(M(X,I)\ne0\ \text{and}\ 
\left|\frac{N(X,I)}{M(X,I)}\right|<\varepsilon\right)\longrightarrow1
\quad(g\to\infty)?
```


This makes the high-probability ratio language of [1, Conjecture 1.10] precise by requiring the ratio to be defined on that event. The source does not specify a value at $`M=0`$; none is assigned here. No positivity of this signed scattering integral is assumed.

## Application

The question separates the contribution of square-integrable eigenmodes from scattering states in the quantum spectrum of a negatively curved surface of large genus.

## References

1. E. Le Masson and T. Sahlsten, [*Quantum ergodicity for Eisenstein series on hyperbolic surfaces of large genus*](https://doi.org/10.1007/s00208-023-02671-1), *Mathematische Annalen* **389** (2024), 845–898. Definitions p. 846, Weil–Petersson model §1.3, Conjecture 1.10 p. 853. [Accepted arXiv v3](https://arxiv.org/abs/2006.14935v3), revised 27 June 2023.

## Status review


**Known cases:** The target counts discrete spectrum against a signed scattering integral on a fixed interval above one quarter. Quantum ergodicity and lower spectral gaps do not establish high-probability dominance of the continuous spectrum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target counts discrete spectrum against a signed scattering integral on a fixed interval above one quarter. Quantum ergodicity and lower spectral gaps do not establish high-probability dominance of the continuous spectrum.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. No matching complete proof or announced solution was found in bounded current searches. Recent spectral-gap results below $`1/4`$ do not control this count on a fixed interval above $`1/4`$.

The page uses the latest and published conjecture, including its corrected sign, integration variable and cusp-growth hypothesis. Its explicit nonzero-denominator convention is an interpretation of the source's ratio statement. A proposed reformulation using area-normalized counts remains held: the source's introductory and detailed density theorems state different cusp-growth ranges. No equivalence relying on that discrepancy is asserted here.

The [coordinator review](../FURTHER_problems/_tracking/random-surface-ratio-coordinator-review-2026-10-23.json), [independent review](../FURTHER_problems/_tracking/journal1118-random-surface-ratio-independent-audit.json), [owner review](../FURTHER_problems/_tracking/arxiv2585-random-hyperbolic-surface-ratio-candidate-audit-2026-10-23.json) and [duplicate audit](../FURTHER_problems/_tracking/random-surface-ratio-all-status-duplicates-2026-10-23.json) record the exact scope, current comparisons and bounded search limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-110964b90e663db3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
