# 104. Does an indicator Gabor basis force tiling and spectrality?

**Area:** Spectral theory and mathematical physics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\geq1`$ and let $`K\subset\mathbb R^d`$ be Lebesgue measurable, with $`0<|K|<\infty`$. Suppose some countable $`\Lambda\subset\mathbb R^{2d}`$ makes
```math
\left\{|K|^{-1/2}e^{2\pi i b\cdot x}\mathbf1_K(x-a):(a,b)\in\Lambda\right\}
```

an orthonormal basis of complex $`L^2(\mathbb R^d)`$.

Must $`K`$ have **both** of the following properties?

1. There exists a countable $`T\subset\mathbb R^d`$ such that
   $`\sum_{t\in T}\mathbf1_K(x-t)=1`$ for almost every $`x\in\mathbb R^d`$.
2. There exists a countable $`\Gamma\subset\mathbb R^d`$ such that
   $`\{|K|^{-1/2}e^{2\pi i\gamma\cdot x}:\gamma\in\Gamma\}`$
   is an orthonormal basis of $`L^2(K)`$.

The set $`K`$ need not be bounded, and $`\Lambda`$ need not be a lattice or a Cartesian product. The conclusion requires existence of $`T`$ and $`\Gamma`$, without prescribing them as projections of $`\Lambda`$.

## Application

Gabor bases describe exact orthogonal time and frequency expansions. This implication would connect the support geometry of indicator pulses to translation tilings and Fourier bases.

## References

- R. J. Chung and C.-K. Lai, *Non-symmetric convex polytopes and Gabor orthonormal bases*, Proc. Amer. Math. Soc. **146** (2018), 5147–5155, [DOI](https://doi.org/10.1090/proc/14183), **Problem 1.2**. [Primary v5](https://arxiv.org/html/1711.10569v5).
- C.-K. Lai and A. Mayeli, *Non-separable lattices, Gabor orthonormal bases and tilings*, J. Fourier Anal. Appl. **25** (2019), 3075–3103, [DOI](https://doi.org/10.1007/s00041-019-09692-y), **Problem 1.2**. [Primary v2](https://arxiv.org/html/1711.10560v2).
- L. Liehr, *Compactly Supported Gabor Orthonormal Bases*, [arXiv:2605.29984v1](https://arxiv.org/html/2605.29984v1), 28 May 2026, Theorems 1.1–1.3 and 4.4.

## Status review


**Known cases:** Liehr's 2026 compact-support classification assumes a one-dimensional lattice; product/separable results are also restricted. The nonproduct-window counterexample is not an indicator window. No theorem for arbitrary finite-measure sets and arbitrary countable time-frequency sets found.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Partial progress; general implication open in the searches checked 28 October 2026.** The source records an affirmative answer for separable countable time-frequency sets. Liehr’s 2026 classification settles bounded supports in dimension one when the time-frequency set is a lattice. These hypotheses leave the general question above unresolved.

Liehr’s counterexample to product realization uses a fractional Fourier window, not an indicator of a finite-measure set: its defining integral is a nonzero entire function times a nonvanishing chirp and dilation, so the window is nonzero almost everywhere on the real line. Unbounded support alone would not establish this distinction.

This question does not assert the classical spectral-set/translation-tile equivalence. Current-resolution, announcement and semantic duplicate searches found no complete matching result or existing AIM/private entry. AIM 449 concerns Gaussian frame optimization.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-general-indicator-Fuglede-Gabor-C212-C-20261028/OWNER-EXACT-INDICATOR-ONB-IMPLIES-TILING-AND-SPECTRALITY-PRIMARY-LATEST2026-PARTIAL-CURRENT-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-general-indicator-Fuglede-Gabor-C212-C-20261028/A-INDEPENDENT-INDICATOR-GABOR-NORMALIZATION-NONLATTICE-QUANTIFIERS-AND-2026-WINDOW-SCOPE-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-general-indicator-Fuglede-Gabor-C212-C-20261028/ROOT-EXACT-INDICATOR-GABOR-PRIMARY-CURRENT2026-AND-SEMANTIC-FINAL-REVIEW.json).


### Online recheck, 2026-10-30

Liehr's 2026 compact-support classification assumes a one-dimensional lattice; product/separable results are also restricted. The nonproduct-window counterexample is not an indicator window. No theorem for arbitrary finite-measure sets and arbitrary countable time-frequency sets found.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2605.29984); [status source 2](https://arxiv.org/abs/1711.10569); [status source 3](https://arxiv.org/abs/1711.10560). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-b4b5bc2210561991** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
