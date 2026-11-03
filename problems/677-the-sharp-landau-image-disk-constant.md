# 677. The sharp Landau image-disk constant

**Area:** Complex analysis and conformal geometry
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb D=\{z\in\mathbb C:|z|<1\}`$. For each holomorphic function $`f:\mathbb D\to\mathbb C`$ with $`|f'(0)|=1`$, define

```math
\rho(f)=\sup\{r>0:\text{ there is }a\in\mathbb C\text{ with }D(a,r)\subset f(\mathbb D)\},
\qquad
L=\inf_f\rho(f).
```

Is

```math
L=\frac{\Gamma(1/3)\Gamma(5/6)}{\Gamma(1/6)}\approx0.5432589653?
```

The image disk can have any center. No injectivity or inverse branch is required, and no boundary regularity is assumed. The supremum need not be attained. The upper bound is known; the question is the matching bound for every normalized holomorphic function.

## Application

This asks for the sharp quantitative form of the open mapping theorem: how much geometric coverage follows from fixing the infinitesimal scale at one point? Extremal covering maps connect the question with hyperbolic uniformization and planar lattices.

## References

1. L. Bétermin, M. Faulhuber and S. Steinerberger, [*A variational principle for Gaussian lattice sums*](https://arxiv.org/abs/2110.06008), v2 (2026), Appendix A.5, pp. 48–49. First submitted in 2021.
2. H. Rademacher, [*On the Bloch-Landau Constant*](https://doi.org/10.2307/2371963), American Journal of Mathematics **65** (1943), 387–390, upper-bound construction.
3. M. Faulhuber, A. Gumber and I. Shafkulovska, [*The AGM of Gauss, Ramanujan’s corresponding theory, and spectral bounds of self-adjoint operators*](https://doi.org/10.1007/s00605-024-02051-0), Monatshefte für Mathematik **206** (2025), 551–582, §4.7.

## Status review


### Online recheck, 2026-10-30

Recent October univalent Bloch-Landau improvements, including the current arXiv and Zenodo certificates, impose injectivity and do not give the sharp image-disk constant for every holomorphic function. Bounded/harmonic Landau-radius and prescribed-center problems are different. No exact lower bound matching the Rademacher upper candidate was found.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2610.34580); [comparison source 2](https://zenodo.org/records/23650159); [comparison source 3](https://arxiv.org/abs/2110.06008); [comparison source 4](https://www.math.purdue.edu/~eremenko/landau.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check:** No matching complete resolution located in the reviewed primary sources and searches through 18 October 2026. Selected independent, catalogue and coordinator reviews found no matching complete resolution or announcement.

The 2025 AGM identity evaluates the known upper candidate and leaves its sharpness conjectural. Recent prescribed-pole meromorphic results concern a different function class. The Bloch constant additionally requires a disk admitting a univalent inverse patch; it is a separate extremal problem. Gaussian lattice polarization does not itself establish the universal bound over all holomorphic maps.

The [primary packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/landau-image-disk-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-landau-image-disk-review.json), [semantic comparison](../FURTHER_problems/_tracking/landau-image-disk-duplicates-review-2026-10-18.json), [catalogue review](../FURTHER_problems/_tracking/landau-image-disk-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/landau-image-disk-coordinator-review-2026-10-18.json) record the evidence and its limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-15aa23e22c144438**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
