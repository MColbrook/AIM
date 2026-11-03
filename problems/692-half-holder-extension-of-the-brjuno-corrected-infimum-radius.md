# 692. Half-Hölder extension of the Brjuno-corrected infimum radius

**Area:** Holomorphic dynamics and small divisors
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D=\{z\in\mathbb C:|z|<1\}`$. For irrational $`\theta\in(0,1)`$, let $`S_\theta`$ consist of all injective holomorphic maps $`f:D\to\mathbb C`$ with $`f(0)=0`$ and $`f'(0)=\lambda_\theta=e^{2\pi i\theta}`$. Let $`h_f(z)=z+O(z^2)`$ be the unique formal series satisfying

```math
f\circ h_f=h_f\circ(\lambda_\theta z).
```

Write $`R(f)`$ for the power-series radius of convergence of $`h_f`$ and define

```math
r_{\inf}(\theta)=\inf_{f\in S_\theta}R(f).
```

Define the ordinary continued-fraction quantities

```math
\alpha_0=\theta,\qquad
\alpha_{j+1}=\frac1{\alpha_j}-\left\lfloor\frac1{\alpha_j}\right\rfloor,
\qquad \beta_{-1}=1,\quad\beta_j=\prod_{k=0}^j\alpha_k,
```

and $`B(\theta)=\sum_{j\ge0}\beta_{j-1}\log(1/\alpha_j)`$. Let $`\mathcal B`$ be the irrational angles in $`(0,1)`$ with $`B(\theta)<\infty`$.

Does there exist a function $`U:[0,1)\to\mathbb R`$ and a finite constant $`C`$ such that

```math
U(\theta)=\log r_{\inf}(\theta)+B(\theta)\quad(\theta\in\mathcal B),
\qquad
|U(x)-U(y)|\le C|x-y|^{1/2}\quad(x,y\in[0,1))?
```

The radius is for the normalized series $`h_f`$, not its inverse. No requirement that the whole convergence disk map into $`D`$ is added. Rational and non-Brjuno angles enter through the requested extension. The infimum is over all $`S_\theta`$, rather than a fixed polynomial family.

## Application

Small divisors make the size of a linearizable neighborhood depend irregularly on the multiplier. The correction by the Brjuno function asks whether that dependence has a uniform square-root modulus after its main arithmetic singularity is removed.

## References

1. Marco Abate, [*Open problems in local discrete holomorphic dynamics*](https://doi.org/10.1007/s13324-011-0017-y), *Analysis and Mathematical Physics* **1** (2011), 261–287. Definition of $`r`$ on p. 266; Definition 7, Theorem 3 and OP2 on p. 267. [Preprint](https://arxiv.org/abs/1107.4876v1); the published e-offprint was read separately.
2. Stefano Marmi, [*An introduction to small divisors problems*](https://homepage.sns.it/marmi/papers/introduction_small_divisors.pdf), arXiv:math/0009232v1 (2000). Definition 1.5 and Section 5.1 identify the normalization and infimum; Question 5.17 separately asks about attainment by a quadratic polynomial.
3. Xavier Buff and Arnaud Chéritat, [*A new proof of a conjecture of Yoccoz*](https://www.math.univ-toulouse.fr/~buff/Preprints/NewYoccoz/NewYoccoz.pdf), inspected author version, Definitions 1–4 and Theorem 1. It compares general univalent-germ radii with a quadratic radius.
4. Davoud Cheraghi and Arnaud Chéritat, [*A proof of the Marmi–Moussa–Yoccoz conjecture for high types*](https://www.ma.imperial.ac.uk/~dcheragh/Research/2015-1.pdf), inspected 2015 author version, Theorem 1 and Section 5.1, Theorem 5.1. Its quadratic and Inou–Shishikura class estimates impose high-type restrictions.
5. Nataliya Goncharuk, [*Complexified Marmi–Moussa–Yoccoz conjecture for high type*](https://www.math.stonybrook.edu/cal/posters/6794.pdf), authored seminar abstract, 27 February 2026. The stated scope is quadratic maps and high-type angles.

## Status review


**Known cases:** The target concerns the infimum over all injective germs. High-type quadratic Siegel-radius results and bounded comparison with that radius do not imply the required uniform half-Holder extension for the infimum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target concerns the infimum over all injective germs. High-type quadratic Siegel-radius results and bounded comparison with that radius do not imply the required uniform half-Holder extension for the infimum.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Yoccoz's bound in [1] gives $`|\log r_{\inf}+B|\le C_0`$ on $`\mathcal B`$, ensuring finite initial values. Boundedness alone gives no modulus of continuity.

The more familiar quadratic conjecture uses the conformal radius of the Siegel disk of $`P_\theta(z)=e^{2\pi i\theta}z+z^2`$. This is a different definition. The selected estimates in [3], together with the injective scaled quadratic $`e^{2\pi i\theta}z+z^2/2`$, give only

```math
\frac1{10}R(P_\theta)\le r_{\inf}(\theta)\le2R(P_\theta).
```

A bounded difference of logarithms does not transfer Hölder regularity. The results in [4] and the 2026 abstract [5] likewise do not identify the infimum over all univalent germs with a uniformly controlled quadratic or renormalization family. The exact infimum formulation of [1] is retained here.

No matching complete solution or announcement was located in the recorded bounded checks. The original 1997 paper and several full follow-up bodies remain unreviewed; the exact eligible 2011 primary statement was read. These checks do not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/abate-infimum-radius-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-abate-infimum-radius-review.json), [current comparisons](../FURTHER_problems/_tracking/abate-infimum-radius-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/abate-infimum-radius-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/abate-infimum-radius-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/abate-infimum-radius-coordinator-review-2026-10-19.json) record the checked scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6a8bc625e7cc1b4f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
