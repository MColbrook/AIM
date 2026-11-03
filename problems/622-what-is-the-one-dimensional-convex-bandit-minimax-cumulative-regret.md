# 622. What is the one-dimensional convex-bandit minimax cumulative regret?

**Area:** Optimization and information
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`K=[0,1]`$ and let $`\mathcal F_b`$ be all convex functions $`f:K\to[0,1]`$, without an added smoothness or Lipschitz condition. In each of $`n`$ rounds a learner chooses $`X_t\in K`$ and observes only $`Y_t=f_t(X_t)+\varepsilon_t`$, with conditionally centred subgaussian noise as in Lattimore's Assumption 1.4. Its cumulative regret is
```math
\mathrm{Reg}_n=\sum_{t=1}^n f_t(X_t)-\inf_{x\in K}\sum_{t=1}^n f_t(x).
```


Determine the exact order, up to absolute constants, of the minimax expected cumulative regret as $`n\to\infty`$ in each of these regimes:

1. **Stochastic:** $`f_t=f`$ for one fixed unknown $`f\in\mathcal F_b`$.
2. **Adversarial:** an arbitrary sequence $`f_1,\ldots,f_n\in\mathcal F_b`$, at least for an oblivious adversary; clarify whether allowing an adversary to adapt to past observations changes the answer.

Do the stochastic and adversarial minimax orders agree? Lattimore asks this in Section 14.xii and reports an $`O(\sqrt n\log n)`$ cumulative-regret upper bound in dimension one. Earlier adversarial work establishes the scale $`\widetilde\Theta(\sqrt n)`$, which leaves the exact logarithmic dependence unresolved. The same question can be stated on any fixed nondegenerate compact interval by an affine change of variables.

## Application

The result would quantify the cost of learning a convex objective from one noisy function value at each decision. It would show whether changing objectives during learning imposes an unavoidable extra regret cost in the simplest continuous action space.

## References

1. T. Lattimore, [*Bandit Convex Optimisation*](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf), Cambridge University Press (2026), [DOI 10.1017/9781009607551](https://doi.org/10.1017/9781009607551), Definition 1.1 and Section 1.2 for the model, Section 14.xii, printed p. 239, for the explicit question. The [publisher record](https://www.cambridge.org/core/books/bandit-convex-optimisation/56ADFCEAC21DB8E828667D64706A0ED0) confirms the edition.
2. S. Bubeck, O. Dekel, T. Koren and Y. Peres, [*Bandit Convex Optimization: $`\sqrt T`$ Regret in One Dimension*](https://arxiv.org/abs/1502.06398), 2015. Its adversarial minimax result is $`\widetilde\Theta(\sqrt n)`$; it does not determine the exact logarithmic factor asked for in [1].

## Status review


**Known cases:** The one-dimensional minimax result is sharp up to logarithms; the requested exact order includes those factors for noisy bounded convex losses. Higher-dimensional hidden-curvature bounds and pseudo-1D models do not remove the remaining logarithmic uncertainty.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Bounded primary-result and announcement searches through 22 October 2026 found no matching exact minimax determination. The book cites a 2020 *thresholding bandit* simple-regret result beside this question; that result uses a different objective, so it is not used here as an exact lower bound for continuous convex-bandit cumulative regret. Local AIM/FURTHER searches found no equivalent listing. The [audit](../FURTHER_problems/_tracking/d003-one-dimensional-bandit-cumulative-regret-status-2026-10-22.json) records the source, scope and search limits.


### Online recheck, 2026-10-30

The one-dimensional minimax result is sharp up to logarithms; the requested exact order includes those factors for noisy bounded convex losses. Higher-dimensional hidden-curvature bounds and pseudo-1D models do not remove the remaining logarithmic uncertainty.

Comparators and current-status sources: [status source 1](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf); [status source 2](https://arxiv.org/abs/1502.06398); [status source 3](https://arxiv.org/abs/1603.04350). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-7003808a838ce848** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
