# 386. Is geometric visibility enough for conditional wave continuation from boundary Cauchy data?

**Area:** Inverse problems and hyperbolic PDE
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^n`$ be a bounded smooth domain with a smooth Riemannian metric $`g`$, let $`\Gamma`$ be an open portion of $`\partial\Omega`$, and let $`S`$ be the corresponding observed part of the lateral space-time boundary. Consider the wave operator from Stefanov's Section 3,

```math
P=\partial_t^2-\bigl(\Delta_g+a^j(x)\partial_{x_j}+q(x)\bigr),
```

with smooth lower-order coefficients. The Cauchy data on $`S`$ comprise $`u|_S`$ and the normal derivative $`\partial_\nu u|_S`$. An a priori bound on $`u`$ permits a *conditional* Hölder estimate on certain interior space-time regions $`Q_\varepsilon`$: roughly, the norm there is bounded by a positive power of the forcing and observation-data norm, together with the a priori norm.

**Question.** Is the largest region on which such a conditional Hölder estimate holds characterized by geometric visibility: every projected zero bicharacteristic through the region meets the observed boundary set $`S`$? Equivalently, is this necessary ray condition sufficient to extend the source's estimate beyond the pseudoconvexity-constructed $`Q_\varepsilon`$ to the optimal visible region, under the same lateral Cauchy-data setup?

The source proves visibility is necessary for its stability estimate. It proves a sharp region for a Euclidean ball/annulus example, while asking whether the ray criterion determines the optimal region in general. Unique continuation or recovery of singularities alone would not answer the conditional Hölder question.

## Application

The issue governs how far partial boundary measurements can stably recover a wave field. It matters for the source's partial-data thermoacoustic tomography setting, where a uniqueness region may be larger than the region controlled by a useful Hölder estimate.

## References

- P. Stefanov, [*Conditionally stable unique continuation and applications to thermoacoustic tomography*](https://doi.org/10.3934/mine.2019.4.789), *Mathematics in Engineering* **1** (2019), 789–799. [Author PDF](https://www.math.purdue.edu/~stefanop/publications/Unique_Continuation.pdf), introduction and Section 3, especially equations (4)–(9), Theorem 3.1 and Section 3.3.
- E. Burman, L. Oksanen, J. Preuss and Z. Zhao, [*Unique continuation for the wave equation: the stability landscape*](https://arxiv.org/abs/2510.20359), arXiv:2510.20359 (2025). Its observations are volumetric interior data, so it treats a different setup.

## Status review


**Known cases:** The source gives conditional boundary-Cauchy estimates under pseudoconvexity/foliation hypotheses and special-case sharpness. Interior volumetric observations and qualitative unique continuation do not identify the optimal boundary-observed conditional-Holder region solely from visibility.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The publisher's scientific HTML question passage was independently rechecked against retained VT_ampere source bytes. The author's full PDF supplies the model, estimate and special-case sharpness missing from that short passage. Bounded searches of later primary research, including the author's [current publication list](https://www.math.purdue.edu/~stefanop/pubs.html), found no theorem or announced resolution for the exact lateral-boundary Cauchy-data characterization. The 2025 stability-landscape paper uses interior volumetric observations and does not by itself settle this question. This review does not certify every later paper. The [source receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0669-J310-remote-html-body-review.json), [independent model comparison](../FURTHER_problems/_tracking/stefanov-wave-visible-region-primary-comparison-2026-10-22.json), [status audit](../FURTHER_problems/_tracking/stefanov-wave-visible-region-status-2026-10-22.json) and [duplicate check](../FURTHER_problems/_tracking/stefanov-wave-visible-region-duplicates-2026-10-22.json) record the limits.


### Online recheck, 2026-10-30

The source gives conditional boundary-Cauchy estimates under pseudoconvexity/foliation hypotheses and special-case sharpness. Interior volumetric observations and qualitative unique continuation do not identify the optimal boundary-observed conditional-Holder region solely from visibility.

Comparators and current-status sources: [status source 1](https://www.math.purdue.edu/~stefanop/publications/Unique_Continuation.pdf); [status source 2](https://arxiv.org/abs/2510.20359). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-421dc569288d76f9** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
