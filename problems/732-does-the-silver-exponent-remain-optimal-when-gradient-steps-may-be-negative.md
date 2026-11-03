# 732. Does the silver exponent remain optimal when gradient steps may be negative?

**Area:** Continuous optimization; complexity of first-order methods
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`n\ge1`$ and a real stepsize schedule $`h=(h_1,\ldots,h_n)\in\mathbb R^n`$. The schedule is chosen before the objective is queried; it may depend on the horizon $`n`$. For any dimension $`d\ge1`$, differentiable convex $`f:\mathbb R^d\to\mathbb R`$ with $`1`$-Lipschitz gradient and a nonempty minimizer set, run plain gradient descent

```math
x_k=x_{k-1}-h_k\nabla f(x_{k-1}),\qquad k=1,\ldots,n.
```

Negative and zero steps are allowed. Define the normalized worst-case error

```math
R_n(h)=\sup_{d\ge1}\ \sup_f\ \sup_{x_\star\in\mathrm{argmin}f}\
\sup_{x_0\ne x_\star}
\frac{f(x_n)-f(x_\star)}{\tfrac12\|x_0-x_\star\|^2}.
```

Put $`p_{\rm sil}=\log_2(1+\sqrt2)`$. **Is it true that for every $`\delta>0`$ there are constants $`c_\delta>0`$ and $`n_\delta\ge1`$ such that**

```math
R_n(h)\ge c_\delta n^{-p_{\rm sil}-\delta}
\quad\text{for every }n\ge n_\delta\text{ and every }h\in\mathbb R^n?
```

The constants are independent of the dimension, objective and schedule. The output is the last iterate. Schedules chosen from observed gradients, momentum, auxiliary iterates and selection of the best earlier iterate are outside this question.

## Application

The question asks whether occasional steps against the gradient can improve the best polynomial worst-case convergence exponent of a particularly simple optimization method. It separates the power of a fixed scalar schedule from the power of algorithms that store additional iterates or adapt to the objective.

## References

1. Yuhan Ye and Kaizhao Liu, [*Silver Rate Is (Almost) Optimal for Gradient Descent*](https://arxiv.org/abs/2609.09152v2), September 2026, equation (1), Theorem 1.1 and §5, first remaining question. The displayed formulation asks for the polynomial exponent, allowing an arbitrary fixed loss $`\delta>0`$.
2. Jason M. Altschuler and Pablo A. Parrilo, *Acceleration by stepsize hedging: Silver Stepsize Schedule for smooth convex optimization*, Mathematical Programming **213** (2025), 1105–1118, [DOI](https://doi.org/10.1007/s10107-024-02164-2). The nonnegative silver schedule attains the exponent $`p_{\rm sil}`$.
3. Guy Kornowski and Ohad Shamir, [*Open Problem: Anytime Convergence Rate of Gradient Descent*](https://proceedings.mlr.press/v247/kornowski24a.html), COLT 2024, PMLR **247**, 5335–5339. This earlier existence question has a later affirmative answer and is not being reopened here.

## Status review


**Known cases:** The fresh silver-rate theorem covers predetermined nonnegative schedules only. Signed lower bounds with a larger exponent, fixed finite horizons and one-dimensional equality do not give the silver exponent for arbitrary signed schedules in every dimension.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fresh silver-rate theorem covers predetermined nonnegative schedules only. Signed lower bounds with a larger exponent, fixed finite horizons and one-dimensional equality do not give the silver exponent for arbitrary signed schedules in every dimension.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2609.09152v2); [comparison source 2](https://doi.org/10.1007/s10107-024-02164-2); [comparison source 3](https://proceedings.mlr.press/v247/kornowski24a.html); [comparison source 4](https://arxiv.org/abs/2609.02855v2); [comparison source 5](https://www.primalspace.me/papers/gradient-descent-dimension-gaps/horizon-dimension-bounds.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The September 2026 primary proves a lower bound with exponent $`p_{\rm sil}+o(1)`$ for **nonnegative** predetermined schedules. Its conclusion explicitly leaves the extension to schedules with negative steps open. The formulation above retains only the optimal-polynomial-exponent part; it does not additionally demand removal of the subpolynomial loss in that theorem.

The known upper bound uses nonnegative steps and is therefore also available within the larger signed class. An earlier [signed-schedule lower bound](https://arxiv.org/abs/2609.02855v2) has exponent approximately $`1.6342`$. A September 2026 [author working paper](https://www.primalspace.me/papers/gradient-descent-dimension-gaps/horizon-dimension-bounds.pdf) announces an improvement to $`1.5570595`$; its inspected statement still does not give the desired exponent approximately $`1.2716`$. Its equality of signed and nonnegative minimax values concerns dimension one at every horizon, or every dimension through five steps. Those restrictions do not settle the present unbounded-horizon, all-dimension question. Ordinary first-order oracle lower bounds and results for quadratic objectives do not automatically close this gap for all smooth convex objectives.

Selected independent, current-status, semantic and catalogue checks through 18 October 2026 found no matching complete resolution or announcement. The September 2026 strongly convex follow-up also explicitly retains the extension to negative steps in the smooth convex setting. Search absence is not proof of openness.

The [primary review](../FURTHER_problems/_tracking/coordinator-pmlr/signed-gradient-silver-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-signed-gradient-silver-review.json), [semantic comparison](../FURTHER_problems/_tracking/coordinator-pmlr/signed-gradient-duplicates-review.json), [catalogue review](../FURTHER_problems/_tracking/coordinator-pmlr/signed-gradient-catalogue-review.json) and [coordinator review](../FURTHER_problems/_tracking/coordinator-pmlr/signed-gradient-coordinator-review.json) preserve the evidence and its limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ba8ecac366a14c8c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
