# 589. Does cyclic monotonicity imply optimality for finite Borel multi-marginal costs?

**Area:** Optimal transport and convex analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge3`$, let $`X_1,\ldots,X_N`$ be Polish spaces with Borel probability measures $`\mu_1,\ldots,\mu_N`$, and let $`\Pi(\mu_1,\ldots,\mu_N)`$ denote their couplings. Suppose $`c:\prod_{j=1}^N X_j\to[0,\infty)`$ is **finite-valued and Borel measurable**, and for some $`f_j\in L^1(\mu_j)`$,

```math
c(x_1,\ldots,x_N)\le\sum_{j=1}^N f_j(x_j)\quad\text{for every }(x_1,\ldots,x_N).
```


A set $`\Gamma\subseteq\prod_jX_j`$ is $`c`$-*cyclically monotone* if, for every finite family $`x^{(1)},\ldots,x^{(m)}\in\Gamma`$ and every choice of permutations $`\sigma_2,\ldots,\sigma_N`$ of $`\{1,\ldots,m\}`$,

```math
\sum_{k=1}^m c(x_1^{(k)},\ldots,x_N^{(k)})
\le \sum_{k=1}^m c(x_1^{(k)},x_2^{(\sigma_2(k))},\ldots,x_N^{(\sigma_N(k))}).
```


**Question.** If $`\gamma\in\Pi(\mu_1,\ldots,\mu_N)`$ has $`c`$-cyclically monotone **topological support**, must it minimize $`\int c\,d\gamma`$ over all couplings? The upper bound makes every such integral finite. This is the nonnegative version of the survey's broader real-valued Borel-cost question, obtained by removing only continuity from Griessler's theorem.

## Application

Cyclic monotonicity checks every finite rearrangement of points in a plan's support. A positive answer would show when those finite tests certify global optimality even for a discontinuous measurable cost in multi-marginal transport.

## References

1. L. De Pascale, A. Kausamo and K. Wyczesany, [*60 Years of Cyclic Monotonicity: a Survey*](https://journalofconvexanalysis.com/articles/jca32020/), *Journal of Convex Analysis* **32** (2025), no. 2, 399–430, Theorem 4.1 and following open question, printed pp. 416–418; [author preprint v2](https://arxiv.org/pdf/2308.07682v2), physical pp. 17–18.
2. C. Griessler, [*$`c`$-cyclical monotonicity as a sufficient criterion for optimality in the multi-marginal Monge–Kantorovich problem*](https://arxiv.org/pdf/1601.05608), Theorem 1.2, physical p. 2. The established theorem assumes a continuous nonnegative cost with the same integrable upper bound.
3. L. De Pascale and A. Kausamo, [*Sufficiency of $`c`$-cyclical monotonicity in a class of multi-marginal optimal transport problems*](https://doi.org/10.1017/S0956792524000202), *European Journal of Applied Mathematics* **36** (2025), 68–81, Theorem 1.4. Its later general result still assumes continuity.
4. M. Petrache, [*Cyclically monotone non-optimal $`N`$-marginal transport plans and Smirnov-type decompositions for $`N`$-flows*](https://doi.org/10.1051/cocv/2020050), *ESAIM: Control, Optimisation and Calculus of Variations* **26** (2020), article 120, §2.2. Its counterexample uses an infinite-valued cost, and it leaves the finite-valued case open.

## Status review

The 2025 survey explicitly asks whether continuity can be removed. Griessler's theorem and the later De Pascale–Kausamo theorem still require it. Petrache's counterexample uses $`+\infty`$ and so does not decide the finite-valued question. A 2026 multi-marginal duality preprint located in the current-status search still assumes bounded **continuous** cost and an additional splitting condition. Focused proof, counterexample and announcement searches through 2026-10-22 found no result settling this exact nonnegative Borel case; the search is bounded. No equivalent target was found in the local AIM or admitted FURTHER problems. The [source review](../FURTHER_problems/_tracking/multimarginal-borel-cyclic-original-2026-10-22.json) and [status audit](../FURTHER_problems/_tracking/multimarginal-borel-cyclic-status-2026-10-22.json) record the exact assumptions and limits.


### Online recheck, 2026-10-30

The 2025 multi-marginal optimality theorem still assumes continuous cost. Borel two-marginal results and infinite-valued multi-marginal counterexamples do not decide the finite nonnegative Borel case with an integrable marginal-sum bound.

Comparators and current-status sources: [status source 1](https://doi.org/10.1017/S0956792524000202); [status source 2](https://arxiv.org/abs/2308.07682); [status source 3](https://arxiv.org/abs/1601.05608). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-bf78dc1e6ac7095f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
