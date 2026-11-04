# 569. Does discontinuous information help randomized approximation?

**Area:** Information-based complexity and randomized numerical recovery
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`F,G`$ be real normed spaces and $`S:F\to G`$ continuous, possibly nonlinear. Put $`B=\{f:\|f\|_F<1\}`$. Compare the information classes $`\Lambda_c=F'`$ and $`\Lambda_a`$, the algebraic dual of $`F`$.

An algorithm may use a random seed, choose its successive linear measurements from the chosen class adaptively, stop after a finite number $`N(f,\omega)`$ of queries, and return $`A_\omega(f)\in G`$. Require the cardinality and output maps to be jointly measurable for the norm Borel structures, and require $`\sup_{f\in B}\mathbb E N(f,\omega)\le n`$. Define
```math
e_n^{\rm ran}(S,\Lambda)=\inf_A\sup_{f\in B}\bigl(\mathbb E\|S(f)-A_\omega(f)\|_G^2\bigr)^{1/2}.
```

Must
```math
e_n^{\rm ran}(S,\Lambda_c)=e_n^{\rm ran}(S,\Lambda_a)
```

hold for every $`F,G,S`$ and $`n\ge1`$? The errors may be infinite. Completeness of the normed spaces and linearity of $`S`$ are not assumed.

## Application

This tests whether idealized discontinuous observations change what randomized numerical recovery can achieve. The deterministic worst-case counterpart is proved in the source for every continuous $`S`$. The paper also gives comparison bounds for compact linear operators between Hilbert spaces. The randomized general question is explicitly retained in Remark 8; the 2026 Acta survey again refers to the continuity assumption as conjecturally unnecessary. Those partial results do not by themselves give the displayed equality in its full model.

## Status review

Bounded searches through 18 October 2026 found no complete matching claim. The final 2013 publication body has not been compared with the fully read 2011 primary manuscripts. The later author manuscript retains this question; its added-in-proof notice resolves separate worst-case locality. The 2026 survey uses a different error, budget and measurability model and is cited as current context. No separate measurability of raw probes is imposed here. These distinctions prevent an automatic-continuity argument from silently narrowing the question.



### Online recheck, 2026-10-30

The original randomized continuous-versus-algebraic-linear information question remains distinct from its solved worst-case counterparts. The 2026 survey uses different budget/error/measurability conventions; no exact-model resolution found.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1106.2945); [status source 2](https://arxiv.org/abs/2602.02066). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References

1. A. Hinrichs, E. Novak and H. Woźniakowski, *Discontinuous information in the worst case and randomized settings*, [arXiv:1106.2945v1](https://arxiv.org/abs/1106.2945v1), abstract, §3 and Remark 8, pp. 16–17; *Mathematische Nachrichten* **286** (2013), 679–690, [DOI](https://doi.org/10.1002/mana.201100128). The [16 September 2011 author version](https://users.fmi.uni-jena.de/~novak/triebel_arxive.pdf) retains this question.
2. D. Krieg and M. Ullrich, *Approximation of functions: Optimal sampling and complexity*, [arXiv:2602.02066v2](https://arxiv.org/abs/2602.02066v2), Remark 9.6, p. 145; *Acta Numerica* **35** (2026), 273–457, [DOI](https://doi.org/10.1017/S0962492925100287).

The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-randomized-discontinuous-information-review.json), [semantic comparison](../FURTHER_problems/_tracking/discontinuous-information-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/discontinuous-information-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/discontinuous-information-coordinator-review-2026-10-18.json) record the exact extents and limitations. These are AI literature and formulation checks, not human peer review or certification of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-8b825ff887eb95a8** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
