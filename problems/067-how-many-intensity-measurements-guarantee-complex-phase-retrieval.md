# 067. How many intensity measurements guarantee complex phase retrieval?

**Area:** Inverse problems; phase retrieval and quantum tomography
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`M\geq2`$, let $`N_*(M)`$ be the smallest $`N`$ for which there exist measurement vectors $`\phi_1,\ldots,\phi_N\in\mathbb C^M`$ such that

```math
\bigl(|\langle x,\phi_j\rangle|^2\bigr)_{j=1}^N
=\bigl(|\langle y,\phi_j\rangle|^2\bigr)_{j=1}^N
\quad\Longrightarrow\quad y=e^{i\theta}x
```


for **every** $`x,y\in\mathbb C^M`$ and some real $`\theta`$. Determine $`N_*(M)`$ for every dimension $`M`$. The vectors may be chosen arbitrarily; the question is about the existence of a globally injective measurement family, rather than injectivity of a random family or recovery of almost every signal.

## Application

Intensity detectors in coherent imaging and pure-state quantum tomography discard phase. The function $`N_*(M)`$ is the exact minimum measurement budget that still distinguishes all complex signals up to the unavoidable global phase. Knowing the sharp budget would clarify how much of the measurement overhead in constructive and generic schemes is necessary.

## References

1. D. G. Mixon, [*Phase Transitions in Phase Retrieval*](https://arxiv.org/pdf/1403.1458), arXiv:1403.1458v2 (2014), Problem 1 on printed page 11 and the surrounding discussion of complex injectivity.
2. A. Conca, D. Edidin, M. Hering and C. Vinzant, [*An algebraic characterization of injectivity in phase retrieval*](https://arxiv.org/abs/1312.0158), *Applied and Computational Harmonic Analysis* **38** (2015), 346–356, [doi:10.1016/j.acha.2014.06.005](https://doi.org/10.1016/j.acha.2014.06.005). Generic sufficiency of $`4M-4`$ measurements.
3. C. Vinzant, [*A small frame and a certificate of its injectivity*](https://arxiv.org/abs/1502.04656), arXiv:1502.04656 (2015). An injective eleven-vector frame in $`\mathbb C^4`$.
4. M. Huang and J. Kim, [*Phase Retrieval in $`\mathbb C^4`$ Requires Exactly Eleven Measurements*](https://arxiv.org/abs/2607.27719), arXiv:2607.27719v3 (2026). The matching lower bound $`N_*(4)\geq11`$.
5. Z. Xu, [*The Minimum Number of Measurements for Almost-Everywhere Complex Phase Retrieval*](https://arxiv.org/abs/2608.15003), arXiv:2608.15003v3 (2026). A different, almost-everywhere threshold.
6. Z. Li, [*On Injectivity of Phase Retrieval*](https://arxiv.org/abs/2606.17922), arXiv:2606.17922v1 (2026). Positive probability of noninjectivity for Gaussian frames with $`4M-5`$ measurements, a different probabilistic statement.

## Status review


**Known cases:** The July 2026 announcement settles only M=4 (eleven measurements). Generic sufficiency, almost-everywhere recovery and Gaussian-frame assertions do not determine the global existence minimum for all dimensions.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The once-proposed necessity of $`4M-4`$ measurements is false: Vinzant's eleven-vector example lies below that count when $`M=4`$. Huang and Kim subsequently showed that ten cannot suffice in that dimension, giving the exact special value $`N_*(4)=11`$. The $`4M-4`$ generic-sufficiency theorem supplies an upper bound for every $`M`$, but no formula for the exact existence minimum in all dimensions. Xu's almost-everywhere theorem and Li's Gaussian noninjectivity result have different quantifiers and do not answer Mixon's Problem 1. A bounded search through 2026-10-21 found no exact all-dimensional proof or announcement. The [source-bound original review](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0185-review.json), [status audit](../FURTHER_problems/_tracking/complex-phase-retrieval-minimum-status-2026-10-21.json), and [semantic duplicate snapshot](../FURTHER_problems/_tracking/complex-phase-retrieval-minimum-duplicates-2026-10-21.json) record the evidence and limits.


### Online recheck, 2026-10-30

The July 2026 announcement settles only M=4 (eleven measurements). Generic sufficiency, almost-everywhere recovery and Gaussian-frame assertions do not determine the global existence minimum for all dimensions.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2607.27719); [status source 2](https://arxiv.org/abs/1312.0158); [status source 3](https://arxiv.org/abs/2608.15003). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-171c662c4b5e87bb** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
