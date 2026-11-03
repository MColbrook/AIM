# 522. Sharp uniform approximation of Lipschitz functions by shallow ReLU networks

**Area:** Approximation theory / numerical analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge2`$ and let $`\Omega=[0,1]^d`$. Define

```math
\mathrm{Lip}(f)=\sup_{x\ne y\in\Omega}\frac{|f(x)-f(y)|}{\|x-y\|_2},\qquad
K_d=\{f\in C(\Omega;\mathbb R):\|f\|_\infty+\mathrm{Lip}(f)\le1\}.
```

Let $`\Sigma_n`$ consist of the functions

```math
S(x)=b_0+\sum_{j=1}^n a_j\max\{w_j\cdot x+b_j,0\},\qquad
a_j,b_j,b_0\in\mathbb R,\quad w_j\in\mathbb R^d.
```

All parameters are unrestricted. Is there a constant $`c_d>0`$ such that, for every integer $`n\ge1`$,

```math
\sup_{f\in K_d}\inf_{S\in\Sigma_n}\|f-S\|_\infty\ge c_d n^{-1/d}?
```

The known upper bound has order $`n^{-1/d}`$. The available general lower bound has order $`(n\log(2+n))^{-1/d}`$, leaving a logarithmic gap. The question concerns best approximation with one hidden layer; no regularity of the parameter selection or bounds on the weights are imposed.

## Application

This determines the worst-case expressive power of shallow ReLU networks for multivariate Lipschitz response surfaces. It separates what the architecture can represent from questions about training or statistical estimation.

## References

1. R. DeVore, B. Hanin and G. Petrova, *Neural Network Approximation*, Acta Numerica **30** (2021), 327–444, [DOI](https://doi.org/10.1017/S0962492921000052). [Eligible preprint](https://arxiv.org/pdf/2012.14501v1), §7, equation (7.1), Problem 3 and §7.2.2, pp. 69–75: the original Lipschitz logarithmic-gap question.
2. Y. Yang and D.-X. Zhou, *Optimal Rates of Approximation by Shallow ReLU Powers Neural Networks and Applications to Nonparametric Regression*, Constructive Approximation **62** (2025), 329–360, [published article](https://doi.org/10.1007/s00365-024-09679-z), Corollary 2.4(3) and the following lower-bound discussion: the upper bound and the distinction between unrestricted and continuous parameter selection.
3. T. Mao, J. W. Siegel and J. Xu, *Approximation Rates for Shallow ReLU Powers Neural Networks on Sobolev Spaces via the Radon Transform*, [arXiv:2408.10996v3](https://arxiv.org/html/2408.10996v3), Introduction, equations (1.12)–(1.13) and Table 1: explicitly retains the remaining logarithmic gap. Published in SIAM Journal on Mathematical Analysis **58**(2) (2026), 1171–1186, [DOI](https://doi.org/10.1137/24M1686693).

## Status review

Checked on **18 October 2026**. The current cited primary version retains this gap. Sharp results for fixed coefficient budgets and critical Besov balls do not establish the displayed lower bound for unrestricted shallow networks and the whole Lipschitz ball. The one-dimensional case follows from free-knot spline theory and is excluded here.

The exact unit-ball normalization is a formulation choice equivalent up to constants to the cited Lipschitz and first-order Sobolev norms. Unit-ball and cube domains transfer by fixed rescaling and Lipschitz extension. The source preprint and selected current primary passages were read; final Acta and SIAM PDF parity was not certified. The independent selected-primary, semantic, current-results and catalogue gates passed at their recorded extents. The served current arXiv HTML carries an internal August 2026 date despite its October 2025 version record; it is used as the body retrieved in October 2026, without certifying historical content parity. The Chen–Wang full-body access gap is retained; its inspected abstract does not announce the displayed lower bound.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/shallow-relu-lipschitz-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-shallow-relu-lipschitz-review.json), [semantic comparison](../FURTHER_problems/_tracking/shallow-relu-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/shallow-relu-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/shallow-relu-coordinator-review-2026-10-18.json) record the exact extents. These are AI formulation and literature checks, not human peer review or certification of all cited proofs.


### Online recheck, 2026-10-30

The 2026 SIAM paper still has logarithmic losses. The September critical-Besov theorem imposes a bounded outer coefficient budget and different norms/classes; it does not establish the unrestricted Lipschitz-ball uniform lower bound.

Comparators and current-status sources: [status source 1](https://doi.org/10.1137/24M1686693); [status source 2](https://arxiv.org/abs/2609.06418); [status source 3](https://arxiv.org/abs/2605.18468). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-466ae24e446bfce1** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
