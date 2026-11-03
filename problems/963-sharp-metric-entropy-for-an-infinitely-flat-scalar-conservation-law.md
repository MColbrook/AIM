# 963. Sharp metric entropy for an infinitely flat scalar conservation law

**Area:** Nonlinear conservation laws and quantitative compactness
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Define

```math
a(0)=0,\qquad a(s)=e^{-1/s^2}\ (s\ne0),\qquad f(u)=\int_0^u a(s)\,ds.
```

Let $`S_t`$ be the Kružkov entropy-solution semigroup for

```math
\partial_tu+\partial_x f(u)=0\qquad\text{on }(0,\infty)\times\mathbb R.
```

Thus the bounded distributional solutions satisfy, for every $`k\in\mathbb R`$,

```math
\partial_t|u-k|+\partial_x\big[\mathrm{sgn}(u-k)(f(u)-f(k))\big]\le0,
```

and attain the initial datum in $`L^1(\mathbb R)`$. Set

```math
\mathcal C=\{u_0\in L^\infty(\mathbb R):\mathrm{ess\,supp}u_0\subset[-1,1],\ \|u_0\|_\infty\le1\},
\qquad K=S_1(\mathcal C).
```

For $`\varepsilon>0`$, let $`N_\varepsilon(K)`$ be the minimum number of subsets of $`L^1(\mathbb R)`$, each of diameter at most $`2\varepsilon`$, needed to cover $`K`$, and put $`H_\varepsilon(K)=\log_2N_\varepsilon(K)`$.

**Determine the asymptotic order of $`H_\varepsilon(K)`$ as $`\varepsilon\downarrow0`$:** obtain upper and lower estimates with the same dependence on $`\varepsilon`$, up to positive multiplicative constants independent of $`\varepsilon`$. No particular rate is conjectured here.

This is a restricted prototype of the sharpness question in [1], with the flux, amplitude, support and observation time fixed. Signed initial data are allowed, with no initial bounded-variation assumption. The covering convention above is part of the question; changes in the argument of a rapidly growing rate cannot silently be absorbed into multiplicative constants.

## Application

Covering entropy measures the number of bits needed to represent an entire solution family at a given accuracy. Sharp estimates help identify how much information a numerical method must retain when the flux is extremely weakly nonlinear near an inflection point.

## References

1. Fabio Ancona, Olivier Glass and Khai T. Nguyen, *Quantitative compactness estimate for scalar conservation laws with nonconvex fluxes*, in [*Hyperbolic Problems: Theory, Numerics, Applications (HYP2018)*](https://www.aimsciences.org/book/AM/volume/26), edited by A. Bressan, M. Lewicka, D. Wang and Y. Zheng, AIMS Series on Applied Mathematics **10** (2020), 248–255. Definition 1.1 and data class (3), p. 249; Theorem 3.1, p. 253; Remark 1, p. 254.
2. Rossana Capuani, Prerona Dutta and Khai T. Nguyen, [*Metric entropy for functions of bounded total generalized variation*](https://arxiv.org/abs/1912.00219v3), latest inspected preprint v3, 18 November 2020. Section 3.2, Theorem 3.7, Remark 3.8, Proposition 3.2 and Remark 3.9. Published in *SIAM Journal on Mathematical Analysis* **53** (2021), 1168–1190; final-body parity remains unreviewed.
3. Fabio Ancona, Olivier Glass and Khai T. Nguyen, [*On Kolmogorov entropy compactness estimates for scalar conservation laws without uniform convexity*](https://arxiv.org/abs/1806.07758), eligible 2018 preprint. The inspected author-version assumptions and Theorems 1.2 and 1.5 concern convex fluxes or a single inflection with finite polynomial degeneracy.
4. Fabio Ancona, Alessio Basti and Fabio Camilli, [*Kolmogorov epsilon-entropy of numerical solutions for scalar conservation laws with convex flux*](https://arxiv.org/abs/2605.07427v1), 8 May 2026, model assumption (2.2) and Theorem 2.1.

## Status review


**Known cases:** The fixed infinitely flat nonconvex flux and exact epsilon-order are essential. Polynomial-degeneracy and convex numerical-scheme entropy bounds do not furnish matching rates for this class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fixed infinitely flat nonconvex flux and exact epsilon-order are essential. Polynomial-degeneracy and convex numerical-scheme entropy bounds do not furnish matching rates for this class.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Here $`f''(u)=2u^{-3}e^{-1/u^2}`$ for $`u\ne0`$, so $`f`$ is concave to the left of zero and convex to its right. Every derivative at zero vanishes. It has no affine interval and satisfies the weak genuine nonlinearity condition used for compactness in [1]. Bounded characteristic speed, the maximum principle and that compactness result give finite covering numbers for $`K`$.

The finite-polynomial sharp estimates in [1] and [3] do not include this flux. The general PDE application in [2] supplies an upper bound, and its Remark 3.8 states that this bound is generally not optimal. Sharp lower estimates for a larger generalized-variation class do not automatically give lower estimates for its smaller PDE-image subset. Splitting positive and negative states also does not decouple entropy solutions across sign-changing shocks. The numerical results in [4] assume a uniformly strictly convex flux.

No matching complete rate or announcement for this precise prototype was located in the recorded bounded checks. Several final-body and cited-proof checks remain pending; these reviews do not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/flat-inflection-entropy-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-flat-inflection-entropy-review.json), [current comparisons](../FURTHER_problems/_tracking/flat-inflection-entropy-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/flat-inflection-entropy-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/flat-inflection-entropy-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/flat-inflection-entropy-coordinator-review-2026-10-19.json) record scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fcf1f790b571c652**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
