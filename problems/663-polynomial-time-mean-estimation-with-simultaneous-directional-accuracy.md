# 663. Polynomial-time mean estimation with simultaneous directional accuracy

**Area:** Robust statistics and high-dimensional probability
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix known constants $`q>2`$ and $`\kappa\ge1`$. Does there exist a randomized algorithm, with running time polynomial in $`N,d,\log(1/\delta)`$ for fixed $`q,\kappa`$, and constants $`c_0,c,C>0`$ depending only on $`q,\kappa`$, with the following property?

Let $`X_1,\ldots,X_N`$ be independent copies of an unknown random vector $`X\in\mathbb R^d`$ whose law is absolutely continuous with respect to $`d`$-dimensional Lebesgue measure, with mean $`\mu`$, covariance $`\Sigma`$, and ordered eigenvalues $`\lambda_1\ge\cdots\ge\lambda_d\ge0`$. Assume, for every unit vector $`u`$,
```math
\bigl(\mathbb E|\langle X-\mu,u\rangle|^q\bigr)^{1/q}
 \le \kappa\bigl(\mathbb E|\langle X-\mu,u\rangle|^2\bigr)^{1/2}.
```

Given only the samples, $`q,\kappa`$ and a confidence parameter
$`e^{-c_0N}\le\delta\le1/2`$, the algorithm must return $`\widehat\mu`$ such that, with probability at least $`1-\delta`$ over the observations and its internal randomness, simultaneously for every unit $`u`$,
```math
|\langle\widehat\mu-\mu,u\rangle|
 \le C\left[
 \sqrt{\frac{u^\top\Sigma u\,\log(1/\delta)}{N}}
 +\sqrt{\frac{\sum_{i=k}^d\lambda_i}{N}}\right],
 \qquad
 k=\max\{1,\lceil c\log(1/\delta)\rceil\}.
```

An empty sum is zero. The algorithm receives neither $`\mu`$ nor $`\Sigma`$.

Here polynomial running time counts real arithmetic operations and comparisons, with random bits permitted. This explicitly specifies a computational interpretation of the source's question; it asserts no equivalence with a finite-bit formulation. The integer rounding is explicit, and the constants may change. The density assumption is retained from the source; no algorithmic reduction from singular laws is asserted.

## Application

A statistically valid estimator with this directional accuracy is known. Computing one efficiently would provide uncertainty control that adapts to each direction, including directions with substantially smaller variance. Efficient estimators with a Euclidean sub-Gaussian error bound do not automatically give this stronger simultaneous guarantee.

## Status review

The source's computation remark asks for efficiently computable performance of this type. Later affine-equivariant, private, covariance-estimation and one-dimensional results checked in the accompanying audit have different guarantees or assumptions. No matching announced solution was located in the bounded current searches of 23 October 2026. Independent source, current-status and all-status semantic duplicate checks passed for this precise density-assumed formulation. The source proves statistical existence; the problem asks for an efficient algorithm.



### Online recheck, 2026-10-30

The statistical existence theorem is not a polynomial-time algorithm. Direction-adaptive simultaneous accuracy with the spectral tail term is stronger than a Euclidean sub-Gaussian or a different Mahalanobis guarantee; no matching efficient construction located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2010.11921); [status source 2](https://doi.org/10.4171/JEMS/1321); [status source 3](https://arxiv.org/abs/2310.10758). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References

1. G. Lugosi and S. Mendelson, *Multivariate mean estimation with direction-dependent accuracy*, J. Eur. Math. Soc. 26 (2024), 2211–2247. [DOI](https://doi.org/10.4171/JEMS/1321), [paper](https://ems.press/content/serial-article-files/47642), [2020 preprint](https://arxiv.org/abs/2010.11921). Theorem 1, printed p.2213; Remark (Computation), p.2218.
2. G. Lugosi, *Mean estimation in high dimension*, Proc. ICM 2022, Vol.7, 5500–5514. [DOI](https://doi.org/10.4171/ICM2022/75), [chapter](https://ems.press/content/book-chapter-files/33347), especially p.5509.

3. Z. Chen and Y. Cherapanamjeri, *Statistical Barriers to Affine-equivariant Estimation*, [arXiv:2310.10758v1](https://arxiv.org/abs/2310.10758v1), Theorem 1.1 and Algorithm 2. This gives a different Mahalanobis guarantee.
4. J. Duchi, S. Haque and R. Kuditipudi, *A Pretty Fast Algorithm for Adaptive Private Mean Estimation*, PMLR **195** (2023), 2511–2551, [paper](https://proceedings.mlr.press/v195/kuditipudi23a/kuditipudi23a.pdf), Assumption A1, Theorems 7–8 and Appendix F.2. The comparison with the empirical mean and covariance-concentration assumptions are material.

The [independent scope review](../FURTHER_problems/_tracking/direction-dependent-efficient-mean-independent-peer-2026-10-23.json) and [duplicate review](../FURTHER_problems/_tracking/direction-dependent-efficient-mean-duplicate-review-2026-10-23.json) record the source assumptions, later-theorem comparisons and limits. Bounded checks do not establish exhaustive absence of a solution or certify every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-3e76d5fdd9724f49** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
