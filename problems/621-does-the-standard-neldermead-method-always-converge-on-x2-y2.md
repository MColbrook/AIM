# 621. Does the standard Nelder–Mead method always converge on x²+y²?

**Area:** Continuous optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Apply the standard two-dimensional Nelder–Mead simplex algorithm with its reflection, **expansion**, contraction and shrink steps, as specified by Lagarias, Poonen and Wright [1, §2], to

```math
f(x,y)=x^2+y^2.
```


Starting from any nondegenerate triangle and using exact arithmetic, must all three successive vertices converge to the unique minimizer $`(0,0)`$?

The expansion step is the distinction: [1] proves convergence to the minimizer for its **restricted** algorithm, which omits expansion, on a much larger class of smooth strictly convex objectives. Its concluding remarks explicitly leave the original expansion-including question open even for this quadratic. Known counterexamples for other convex functions do not refute this special case.

## Application

An answer would establish a rigorous global behavior test for a widely used derivative-free optimization method on the simplest strictly convex quadratic objective. A counterexample would identify a failure of the unmodified method even on this benchmark.

## References

1. J. C. Lagarias, B. Poonen and M. H. Wright, [*Convergence of the restricted Nelder–Mead algorithm in two dimensions*](https://arxiv.org/pdf/1104.0350v1), *SIAM Journal on Optimization* **22** (2012), 501–532, [DOI 10.1137/110830150](https://doi.org/10.1137/110830150). See §2 for the algorithms, Theorem 3.17 for the restricted result and §4, physical preprint p. 23, for the explicit open question.
2. A. Galántai, [*Convergence of the Nelder–Mead method*](https://doi.org/10.1007/s11075-021-01221-7), *Numerical Algorithms* **90** (2022), 1043–1072. Its simplex-convergence theorem has a quantitative step-frequency assumption and does not establish unconditional minimizer convergence here.
3. A. Galántai, [*The Nelder–Mead Simplex Algorithm Is Sixty Years Old: New Convergence Results and Open Questions*](https://doi.org/10.3390/a17110523), *Algorithms* **17** (2024), 523, on value and simplex-convergence results and their limits.

## Status review

The later general convergence theorems checked do not resolve this all-starting-triangle minimizer question; they have extra step conditions or weaker conclusions. Bounded searches through 22 October 2026 found no exact proof, counterexample, or announcement. The [audit](../FURTHER_problems/_tracking/w001-nelder-mead-quadratic-global-convergence-status-2026-10-22.json) records these limits and the duplicate check.


### Online recheck, 2026-10-30

The original expansion-including algorithm and every nondegenerate starting triangle are required. Restricted Nelder–Mead, quantitative step-frequency conditions, common-value convergence and 2026 statistical parameter heuristics do not prove convergence to the quadratic minimizer.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1104.0350); [status source 2](https://doi.org/10.1007/s11075-021-01221-7); [status source 3](https://doi.org/10.1016/j.cam.2026.117521). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-8b243d08720213e1** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
