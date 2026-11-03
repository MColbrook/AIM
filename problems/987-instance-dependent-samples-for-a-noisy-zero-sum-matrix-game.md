# 987. Instance-dependent samples for a noisy zero-sum matrix game

**Area:** Probability, statistics and learning
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let the unknown payoff matrix of a two-player zero-sum game be $`A\in\mathbb R^{n\times m}`$. A learner chooses an entry $`(i,j)`$ at each round and observes $`A_{ij}+\eta_t`$, where the noise is zero-mean and $`1`$-subgaussian. For $`\varepsilon>0`$ and $`0<\delta<1`$, how many adaptive entry samples are necessary and sufficient, as a function of the particular matrix $`A`$, to return an $`\varepsilon`$-Nash equilibrium with probability at least $`1-\delta`$?

Writing $`\Delta_n`$ for the probability simplex, a pair $`(x_*,y_*)\in\Delta_n\times\Delta_m`$ is $`\varepsilon`$-Nash here when, for every $`x\in\Delta_n`$ and $`y\in\Delta_m`$,
```math
x^\top Ay_*\le x_*^\top Ay_*+\varepsilon,\qquad x_*^\top Ay\ge x_*^\top Ay_*-\varepsilon.
```

The original author asks for a tight characterization, ideally $`\Theta(H_1(A,\varepsilon)\log(1/\delta)+H_2(A,\varepsilon))`$ with the instance-dependent functions $`H_1,H_2`$ identified. They are **unknown functions to find**, not inputs already specified by the paper. The displayed source model calls the noise zero-mean and $`1`$-subgaussian without explicitly spelling out an independence assumption.

## Application

Two game matrices of the same size can have very different equilibrium margins. A sharp instance-dependent bound would say when noisy payoff queries can identify an approximate equilibrium substantially faster than the generic worst-case guarantee.

## References

1. A. Maiti, [*Open Problem: Optimal Instance-Dependent Sample Complexity for finding Nash Equilibrium in Two Player Zero-Sum Matrix games*](https://proceedings.mlr.press/v291/maiti25b.html), *Proceedings of the 38th Conference on Learning Theory*, PMLR **291** (2025), 6230–6234, §2–3; [publisher PDF](https://raw.githubusercontent.com/mlresearch/v291/main/assets/maiti25b/maiti25b.pdf).
2. A. Maiti, K. Jamieson and L. J. Ratliff, [*Instance-dependent Sample Complexity Bounds for Zero-sum Matrix Games*](https://proceedings.mlr.press/v206/maiti23a.html), AISTATS 2023, PMLR **206**, for smaller game classes and related instance bounds.
3. J. Jiang and M. Zhang, [*An LP-Based Approach for Bilinear Saddle Point Problem with Instance-dependent Guarantee and Noisy Feedback*](https://arxiv.org/abs/2602.12513), arXiv:2602.12513 (2026), introduction and §1.1–1.2, for a general-dimensional upper bound on a distinct $`\varepsilon`$-bias target.

## Status review


**Known cases:** Necessary and sufficient instance-dependent samples for general mixed possibly nonunique Nash equilibria are required. Pure equilibria, n-by-two games, regret bounds and epsilon-bias upper bounds do not characterize this target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Necessary and sufficient instance-dependent samples for general mixed possibly nonunique Nash equilibria are required. Pure equilibria, n-by-two games, regret bounds and epsilon-bias upper bounds do not characterize this target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Maiti records progress for strict pure equilibria and certain $`n\times2`$ games, while asking for the general, possibly nonunique-equilibrium case. Jiang and Zhang provide an instance-dependent general-dimensional *upper bound* for estimating an equilibrium with $`\varepsilon`$ bias; their paper distinguishes that target from the high-probability $`\varepsilon`$-Nash criterion above and does not characterize its general instance-optimal complexity. A separate September 2026 Nash-*regret* announcement also has a different online objective. Bounded searches through 22 October 2026 found no complete matching characterization or exact AIM/FURTHER duplicate. The [status](../FURTHER_problems/_tracking/noisy-matrix-game-instance-complexity-2026-10-22-status.json) and [duplicate](../FURTHER_problems/_tracking/noisy-matrix-game-instance-complexity-2026-10-22-duplicates.json) audits record the scope of these checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c73d3439aeaff8f4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
