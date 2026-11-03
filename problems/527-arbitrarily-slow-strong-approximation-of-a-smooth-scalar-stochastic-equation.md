# 527. Arbitrarily slow strong approximation of a smooth scalar stochastic equation

**Area:** Numerical analysis of stochastic differential equations
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`(\varepsilon_n)_{n\geq1}`$ be any sequence of positive numbers tending to zero. Do there exist globally bounded functions $`a,b\in C^\infty(\mathbb R)`$, with $`b`$ globally Lipschitz, such that the scalar autonomous Itô equation

```math
dX_t=a(X_t)\,dt+b(X_t)\,dW_t,\qquad 0\leq t\leq1,\qquad X_0=0,
```

has the following property for every $`n\geq1`$?

```math
\inf_{t_1,\ldots,t_n\in[0,1]}
\inf_{u:\mathbb R^n\to\mathbb R\ \mathrm{Borel\ measurable}}
\mathbb E\bigl|X_1-u(W_{t_1},\ldots,W_{t_n})\bigr|
\geq\varepsilon_n.
```

Here $`W`$ is a standard real Brownian motion. The sampling times are deterministic and may be placed arbitrarily. The coefficients may depend on the entire prescribed sequence, but one pair of coefficients must satisfy every displayed lower bound. Their bounds and the Lipschitz constant of $`b`$ need not be uniform over sequences.

Smoothness and boundedness ensure a unique nonexplosive strong solution. No bound on the derivatives of $`a`$, uniform ellipticity, or nonvanishing condition on $`b`$ is imposed. The question concerns the best possible method using the indicated Brownian samples, rather than the performance of a particular discretization.

The corresponding construction is known in state dimension two [2]. The scalar case is explicitly asked in [1, Remark 4(ii)]. When both coefficients are globally Lipschitz, standard polynomial convergence results apply; those hypotheses are stronger than smoothness and boundedness of the drift. Slow polynomial examples with square-root diffusion, and scalar equations with merely measurable time dependence, have different coefficient assumptions.

## Application

This asks whether smooth bounded scalar stochastic dynamics can be intrinsically arbitrarily difficult to simulate strongly from finitely many observations of their driving Brownian path. It would clarify how state dimension and degeneracy of the diffusion affect the limits of numerical simulation.

## References

1. T. Müller-Gronbach and L. Yaroslavtseva, *On the complexity of strong approximation of stochastic differential equations with a non-Lipschitz drift coefficient*, Journal of Complexity **85** (2024), 101870. [DOI](https://doi.org/10.1016/j.jco.2024.101870), [public preprint](https://arxiv.org/pdf/2403.00637v1), Theorem 8 and Remark 4(ii), p. 7; information model, pp. 1–3.
2. M. Gerencsér, A. Jentzen and D. Salimova, *On stochastic differential equations with arbitrarily slow convergence rates for strong approximation in two space dimensions*, Proceedings of the Royal Society A **473** (2017), 20170104. [DOI](https://doi.org/10.1098/rspa.2017.0104), [latest preprint](https://arxiv.org/pdf/1702.03229v2), Theorem 1.2, pp. 1–2; coefficient construction and Lemma 2.1, pp. 3–4.

## Status review

**Checked:** 18 October 2026. The complete public survey and the selected model and dimensional comparison in the latest version of [2] were read. Current searches found no matching scalar autonomous resolution or complete announcement in the sources checked. AIM 639 concerns a prescribed fractional-noise scheme and a fixed rate; it is a different target.

The final journal body of [1] was inaccessible, so its parity with the public preprint has not been certified. The independent selected-primary, bounded current-results and announcement, semantic and all-status catalogue checks passed at their recorded extents. The current Wong–Zakai rate theorem assumes bounded derivatives through order three, which is stronger than the displayed drift hypothesis.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/scalar-sde-arbitrary-slow-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-scalar-sde-arbitrary-slow-review.json), [semantic comparison](../FURTHER_problems/_tracking/scalar-sde-slow-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/scalar-sde-slow-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/scalar-sde-slow-coordinator-review-2026-10-18.json) record exact scopes and limits. These AI literature and formulation checks are not human peer review or certification of every cited proof.


### Online recheck, 2026-10-30

Arbitrarily slow approximation is known in dimension two and above. The recent scalar survey explicitly asks the autonomous one-dimensional smooth bounded case; results with Lipschitz drift, time-irregular coefficients or a particular scheme do not settle it.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2403.00637); [status source 2](https://arxiv.org/abs/1702.03229). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-46b826d1084f3de2** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
