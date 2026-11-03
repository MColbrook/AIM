# 561. Linear-size equal-weight discretization of the L1 norm

**Area:** Approximation theory and numerical analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^d`$ be compact, let $`\mu`$ be a Borel probability measure on $`\Omega`$, and let $`X_N\subset C(\Omega;\mathbb R)`$ be an $`N`$-dimensional real linear space, $`N\ge2`$. Write $`\|f\|_p=(\int_\Omega |f|^p\,d\mu)^{1/p}`$ and $`\|f\|_\infty=\max_\Omega|f|`$.

Assume that, for some $`K\ge1`$, the space satisfies the Nikol’skii inequality
```math
\|f\|_\infty\le\sqrt{KN}\,\|f\|_2\qquad(f\in X_N).
```

**Does an absolute constant $`C>0`$ exist such that every such space admits points $`\xi^1,\ldots,\xi^m\in\Omega`$ with $`m\le CKN`$ and**
```math
\frac12\|f\|_1\le\frac1m\sum_{j=1}^m|f(\xi^j)|\le\frac32\|f\|_1
\qquad(f\in X_N)?
```

The same points must work for the whole space. They may depend on $`X_N,\mu`$ and $`K`$; repetitions are allowed. All weights are exactly $`1/m`$. The constant $`C`$ must be independent of $`N,K,d,\Omega,\mu`$ and $`X_N`$. No algorithm for finding the points and no probability of success are required.

A bound $`m\le CKN\log(KN)`$ is known. The question asks whether the logarithmic overhead can be removed at the fixed distortion above. Linear-size discretization of the L2 norm is known under the same assumption. It does not directly control integrals of $`|f|`$ for all $`f`$ in the space.

## Application

Equal-weight evaluations provide a simple quadrature rule for estimating integral norms of functions in a trial space. Such norm estimates enter stable approximation, validation of discretizations and recovery from function values. The assumption limits how sharply a normalized function in the space can concentrate; the question asks whether this control permits sampling with a number of points proportional to the dimension.

## References

1. B. Kashin, E. Kosov, I. Limonova and V. Temlyakov, [Sampling discretization and related problems](https://arxiv.org/abs/2109.07567), arXiv:2109.07567v2,10 February 2022; first submitted 15 September 2021. Definitions (2.1)–(2.2), Condition E/(2.9), D.15–D.16 and §2.7 Open Problem 3. Related publication: [Journal of Complexity 71 (2022), 101653](https://doi.org/10.1016/j.jco.2022.101653).
2. F. Dai, E. Kosov and V. Temlyakov, [Some improved bounds in sampling discretization of integral norms](https://arxiv.org/abs/2208.09762), arXiv:2208.09762v2,11 April 2023, Theorem 1.1. Published in [Journal of Functional Analysis 285 (2023), 109951](https://doi.org/10.1016/j.jfa.2023.109951). This gives simultaneous L1 and L2 discretization with a logarithmic factor; simultaneous L2 control is not required in the question above.
3. F. Dai, E. D. Kosov and V. N. Temlyakov, [A survey of sampling discretization of integral and uniform norms](https://surveys-in-approximation-theory.com/papers/20/20.pdf), *Surveys in Approximation Theory* **10** (2026), 1–42, published 22 October 2026. Section 6, p. 29, explicitly retains logarithm removal for $`1\le p<2`$ as open, including the L1 question above. The earlier [arXiv version](https://arxiv.org/html/2603.02459v1) has a sole-v1 record dated 2 March 2026 and a served HTML date of 24 August 2026; no historical-version parity is asserted.

## Status review

Reviewed 18 October 2026. This is the L1, equal-weight, Nikol’skii-controlled instance of the older survey’s discretization programme, with the linear dependence on $`KN`$ asked explicitly in the current survey. The cited 2023 result retains a logarithmic factor. Current Orlicz-norm results inspected here retain logarithmic overhead or give one-sided inequalities; neither establishes this two-sided L1 assertion. Arbitrary-weight rules, arbitrary linear embeddings and the L2 theorem do not meet its requirements.

The older survey’s unrestricted supremum over all measures and spaces has a rare-atom obstruction. That construction has an unbounded concentration constant and does not settle the displayed question with its stated dependence on $`K`$. The final 2026 survey’s problem statement was checked on 27 October 2026; this is a reference update, without a full comparison of its 42 pages. The final 2022 and 2023 journal editions have not been fully compared with the selected preprints. The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-nikolskii-l1-linear-discretization-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/nikolskii-l1-prove2-0174-review.json) and [coordinator review](../FURTHER_problems/_tracking/nikolskii-l1-coordinator-review-2026-10-18.json) passed at their recorded extents. The checks preserve the stated model and version limits; they do not certify every referenced proof.


### Online recheck, 2026-10-30

The October 2026 survey retains removal of the logarithmic overhead for p<2. Uniform-norm hyperbolic-cross discretization, weighted rules and L2 sparsification are not the two-sided equal-weight L1 statement under the stated Nikolskii bound.

Comparators and current-status sources: [status source 1](https://surveys-in-approximation-theory.com/papers/20/20.pdf); [status source 2](https://arxiv.org/abs/2603.02459); [status source 3](https://arxiv.org/abs/2208.09762). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c1934f05b9ec012f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
