# 284. Optimal final-iterate rate for one-dimensional SGD with bounded unbiased gradients

**Area:** Continuous optimization and stochastic approximation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`F:\mathbb R\to\mathbb R`$ be convex and $`1`$-Lipschitz. Choose a deterministic $`x_1\in[0,1]`$ and integer horizon $`T\ge1`$, and set $`\eta=T^{-1/2}`$. On any filtered probability space $`(\Omega,\mathcal F,(\mathcal F_t),\mathbb P)`$, let $`x_t`$ be $`\mathcal F_t`$-measurable and $`g_t`$ be $`\mathcal F_{t+1}`$-measurable, with

```math
|g_t|\le1\quad\text{almost surely},\qquad
\mathbb E[g_t\mid\mathcal F_t]\in\partial F(x_t).
```

Here $`\partial F`$ is the ambient convex subdifferential on $`\mathbb R`$. Perform exactly $`T`$ updates,

```math
x_{t+1}=\Pi_{[0,1]}(x_t-\eta g_t),\qquad t=1,\ldots,T.
```

Does a universal finite constant $`C`$ exist such that, for every such function, initialization, horizon and oracle process,

```math
\mathbb E\!\left[F(x_{T+1})-\min_{x\in[0,1]}F(x)\right]
\le \frac{C}{\sqrt T}\,?
```

The oracle may depend on the entire past and the queried point. The step is constant throughout the run, with multiplier one. The output is the unchanged final point.

## Application

SGD often returns its final parameter value in learning and stochastic optimization. This asks whether a logarithmic loss is necessary even for one scalar parameter when unbiased gradient estimates are uniformly bounded but may depend on previous observations.

## References

1. Tomer Koren and Shahar Segal, [*Open Problem: Tight Convergence of SGD in Constant Dimension*](https://proceedings.mlr.press/v125/koren20a/koren20a.pdf), PMLR125 (2020),3847–3851, OpenProblem1.
2. Daogao Liu and Zhou Lu, [*The Convergence Rate of SGD's Final Iterate: Analysis on Dimension Dependence*](https://arxiv.org/html/2106.14588v1), Section4.1,Definition4.2 and Section4.3. The bounded stochastic-output model is explicit here.
3. Guglielmo Beretta, Tommaso Cesari, Roberto Colomboni and Andrea Paudice, [arXiv:2606.24879v1](https://arxiv.org/abs/2606.24879v1), Theorems2–3 and Section7, distinguishes iid additive noise, bounded conditional variance and the remaining bounded-gradient case.
4. The same authors, [*Sharp Dimension Dependence for the Last Iterate of the SubGradient Method*](https://arxiv.org/abs/2607.15980v2), latest version21July2026, deterministic fixed-dimensional result.
5. Zijian Liu and Zhengyuan Zhou, [*Revisiting the Last-Iterate Convergence of Stochastic Gradient Methods*](https://arxiv.org/html/2312.08531v4), latest version19March2026, Section3.1.

## Status review


**Known cases:** The latest 2026 one-dimensional SGD paper explicitly says its logarithmic counterexamples use gradients of size sqrt(T) and do not settle uniformly almost-surely bounded gradients. Its iid additive-noise positive theorem, deterministic results, smooth interpolation and different schedules do not cover arbitrary adapted bounded oracles with the specified constant step.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

This is a source-inspired normalized bounded-oracle residual of [1], fixing diameter, oracle bound and step multiplier to one. Its formal setup does not explicitly impose a uniform noise bound; the displayed bounded-output model is grounded directly in [2]. The unqualified original problem is not being presented as wholly unresolved.

The optimal rate is known for deterministic fixed-dimensional subgradients [4], and for state-independent, time-homogeneous additive noise [3]. The logarithmic counterexamples in [3] use noise amplitudes growing with the horizon; Section7 explicitly distinguishes uniformly almost-surely bounded stochastic gradients. The positive one-dimensional result in [2] assumes a nearly-linear subclass and a different step multiplier. These hypotheses do not give the displayed assertion for arbitrary adapted bounded oracles.

The logarithm-free general convex result in [5] uses a linearly decreasing step schedule. Its constant-step results retain a logarithmic loss or optimize a different multiplier. The August2026 [*Anytime Last Iterates in Fixed Dimension* project](https://github.com/andotheror/anytime-last-iterates-fixed-dimension) explicitly treats deterministic directions; its scientific README was checked, while its complete paper was not reviewed here.

A generic $`O(\log T/\sqrt T)`$ upper bound leaves the proposed gap. Taking $`F_T(x)=x/(2\sqrt T)`$, $`x_1=1`$ and $`g_t=1/(2\sqrt T)`$ gives $`x_{T+1}=1/2`$ and gap $`1/(4\sqrt T)`$, confirming the possible scale without proving the upper bound.

No matching complete resolution was located in the recorded bounded searches. The [source/model review](../FURTHER_problems/_tracking/parallel/complex-bayesian/bounded-gradient-1d-last-sgd-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-bounded-gradient-1d-sgd-review.json), [semantic comparison](../FURTHER_problems/_tracking/sgd-bounded-oracle-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/sgd-bounded-oracle-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/sgd-bounded-oracle-coordinator-review-2026-10-19.json) record their extent and limitations. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

The latest 2026 one-dimensional SGD paper explicitly says its logarithmic counterexamples use gradients of size sqrt(T) and do not settle uniformly almost-surely bounded gradients. Its iid additive-noise positive theorem, deterministic results, smooth interpolation and different schedules do not cover arbitrary adapted bounded oracles with the specified constant step.

Comparators and current-status sources: [status source 1](https://arxiv.org/html/2606.24879); [status source 2](https://arxiv.org/abs/2610.25469); [status source 3](https://arxiv.org/abs/2607.15980); [status source 4](https://arxiv.org/abs/2312.08531). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-676c31fc0999ee6e** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
