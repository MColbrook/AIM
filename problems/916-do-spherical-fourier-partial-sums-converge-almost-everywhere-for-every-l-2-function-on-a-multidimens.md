# 916. Do spherical Fourier partial sums converge almost everywhere for every $`L^2`$ function on a multidimensional torus?

**Area:** Harmonic analysis and Fourier series
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`d\ge2`$ and $`f\in L^2(\mathbb T^d)`$, define its circular (spherical when $`d>2`$) partial Fourier sums by

```math
S_R f(x)=\sum_{k\in\mathbb Z^d:\,\lVert k\rVert_2\le R}\widehat f(k)e^{ik\cdot x}.
```


Must $`S_Rf(x)\to f(x)`$ as $`R\to\infty`$ for almost every $`x\in\mathbb T^d`$? Weisz asks whether the maximal inequality and almost-everywhere convergence of his Theorem 4.4 extend to $`p=2`$ with circular partial sums. The displayed convergence question is the central unresolved part; an $`L^2`$ bound for the corresponding maximal operator would be a stronger route to it.

## Application

A positive answer would extend the almost-everywhere Fourier convergence theorem from one dimension and from polygonal summation regions to Euclidean balls in frequency space.

## References

- F. Weisz, [*Summability of Multi-Dimensional Trigonometric Fourier Series*](https://surveys-in-approximation-theory.com/papers/17/17.pdf), *Surveys in Approximation Theory* **7** (2012), 1–179. See printed pp. 17 and 20, Theorems 4.4 and 4.6 and the subsequent question; [publisher record](https://surveys-in-approximation-theory.com/papers/17/index.html).
- K.-M. Perfekt, [*Rectangular Summation of Multiple Fourier Series and Multi-parametric Capacity*](https://link.springer.com/article/10.1007/s11118-020-09861-5), *Potential Analysis* **55** (2021), 389–402. Its introduction explicitly distinguishes the open spherical $`L^2`$ question from its rectangular-sum results.

## Status review


**Known cases:** Triangular, cubic or rectangular partial sums and generalized localization are not spherical almost-everywhere convergence for every L2 function. Restriction and local-smoothing advances do not by themselves establish this zero-regularity endpoint for all multidimensional tori.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Triangular, cubic or rectangular partial sums and generalized localization are not spherical almost-everywhere convergence for every L2 function. Restriction and local-smoothing advances do not by themselves establish this zero-regularity endpoint for all multidimensional tori.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original survey separates known triangular/cubic almost-everywhere convergence from the circular $`L^2`$ case. Perfekt's later paper still states the latter as open. The [2019 generalized-localization result](https://journals.eco-vector.com/0869-5652/article/view/17855/en_US) handles a restricted vanishing-on-an-open-set conclusion, not global convergence. Bounded searches through 22 October 2026 found no matching complete proof, counterexample or announcement; this negative result is not exhaustive. The [publisher-PDF body receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0679-J321-remote-pdf-body-review.json), [scope/status audit](../FURTHER_problems/_tracking/spherical-l2-fourier-2026-10-22-status.json) and [duplicate audit](../FURTHER_problems/_tracking/spherical-l2-fourier-2026-10-22-duplicates.json) record the checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9d08bf8f2e78505f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
