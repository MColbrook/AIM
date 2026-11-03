# 990. Sharp propagation of chaos from transport control of initial correlations

**Area:** Probability, interacting diffusions and mean-field approximation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`T>0`$ and $`d\geq1`$, and let $`E=C([0,T];\mathbb R^d)`$. Write $`\|x\|_t=\sup_{s\leq t}|x(s)|`$. Let $`b_0:[0,T]\times E\to\mathbb R^d`$ and $`b:[0,T]\times E^2\to\mathbb R^d`$ be Borel maps depending only on paths up to the indicated time. Suppose that some $`L<\infty`$ satisfies

```math
|b_0(t,x)-b_0(t,x')+b(t,x,y)-b(t,x',y')|
\leq L\bigl(\|x-x'\|_t+\|y-y'\|_t\bigr)
```

for every $`t,x,x',y,y'`$, and that $`\int_0^T|b_0(t,0)+b(t,0,0)|\,dt<\infty`$.

Let $`\mu_0\in\mathcal P_2(\mathbb R^d)`$ satisfy a quadratic transport inequality: for some $`\eta_0<\infty`$,

```math
W_2^2(\nu,\mu_0)\leq\eta_0 H(\nu\mid\mu_0)
\qquad\text{for every }\nu\in\mathcal P_2(\mathbb R^d).
```

Here $`H(\nu\mid\mu)=\int\log(d\nu/d\mu)\,d\nu`$ if $`\nu\ll\mu`$, and $`+\infty`$ otherwise. For each $`n\geq2`$, let $`P_0^n`$ be an exchangeable probability law on $`(\mathbb R^d)^n`$, and write $`P_0^{n,k}`$ for its first $`k`$ coordinates. Assume that a constant $`C_0<\infty`$, independent of $`n,k`$, satisfies

```math
W_2^2(P_0^{n,k},\mu_0^{\otimes k})\leq C_0(k/n)^2
\qquad(n\geq2,\ 1\leq k\leq n).
```

With independent standard $`d`$-dimensional Brownian motions independent of the initial vector, consider

```math
dX_t^{i,n}=\left[b_0(t,X^{i,n})+
\frac1{n-1}\sum_{j\ne i}b(t,X^{i,n},X^{j,n})\right]dt+dB_t^i,
\qquad \mathrm{Law}(X_0^{1,n},\ldots,X_0^{n,n})=P_0^n.
```

Let $`\mu`$ be the path law of the unique McKean–Vlasov solution

```math
dY_t=\left[b_0(t,Y)+\int_E b(t,Y,y)\,\mu(dy)\right]dt+dB_t,
\qquad \mathrm{Law}(Y_0)=\mu_0,
```

and let $`P^{n,k}`$ be the joint path law of the first $`k`$ interacting particles. Is there a finite $`C`$, depending on the fixed coefficients, $`T,d,\mu_0`$ and $`C_0`$, but independent of $`n,k`$ and of the particular initial family satisfying the displayed bound, such that

```math
W_{2,T}^2(P^{n,k},\mu^{\otimes k})\leq C(k/n)^2
\qquad(n\geq2,\ 1\leq k\leq n)?
```

The distance on initial $`k`$-vectors uses the ordinary Euclidean norm, without division by $`k`$. The path distance $`W_{2,T}`$ uses

```math
d_{k,T}(x,y)=\sup_{0\leq t\leq T}
\left(\sum_{i=1}^k|x_i(t)-y_i(t)|^2\right)^{1/2}.
```

No initial relative-entropy bound or absolute continuity of $`P_0^n`$ is assumed. All initial marginal transport bounds are required, rather than just a bound for one fixed marginal.

## Application

Interacting diffusions approximate nonlinear probability evolutions in granular media and particle simulation. A sharp transport estimate would justify such approximations when the initial particles have small correlations measured geometrically, including initial laws for which an entropy estimate is unavailable.

## References

1. Daniel Lacker, *Hierarchies, entropy, and quantitative propagation of chaos for mean field diffusions*, Probability and Mathematical Physics **4** (2023), 377–432. [DOI](https://doi.org/10.2140/pmp.2023.4.377); [pinned author version](https://arxiv.org/abs/2105.02983v2), Corollary2.7 and the final paragraph immediately following it, physical page12. That paragraph explicitly poses the replacement of initial entropic chaos by its transport analogue.
2. Manuel Arnese and Daniel Lacker, *Sharp propagation of chaos for mean field Langevin dynamics, control, and games* (2026). [Primary text](https://arxiv.org/html/2603.10988v1), Theorem2.3, Corollary2.4 and Remark5.7. Its nonindependent-initialization extension retains an initial local relative-entropy hypothesis.
3. Armand Bernou, Mitia Duerinckx and Matthieu Ménard, *Creation of chaos for interacting Brownian particles*, Stochastic Processes and their Applications **193** (2026), 104849. [DOI](https://doi.org/10.1016/j.spa.2025.104849); [author version](https://arxiv.org/abs/2504.09917). Its sharp creation-of-chaos estimates use negative Sobolev norms; the Wasserstein comparison discussed in its introduction has a weaker rate.
4. Xing Huang, *Long Time Entropy-Cost type Propagation of Chaos* (latest author version, 2025). [Primary text](https://arxiv.org/html/2308.15181v8), Theorems2.1,3.1 and4.1. These replace initial entropy by a global initial transport cost, but retain a local error of order $`k/n`$ and a positive-time regularization cost.

- [Yuhao Lei, Sharp Wasserstein propagation of chaos from correlated initial data, Palomar entry (8 October 2026)](https://palomar-registry.org/entry?id=PALOMAR-2026-10-08-000001&version=1). Added in the 2026-10-30 recheck.

## Status review


**Known cases:** A new Palomar entry claims the sharp rate for correlated/singular initial laws but assumes bounded Markovian interactions and states fixed-time marginal Wasserstein estimates. The present target allows unbounded Lipschitz path-dependent interactions and asks a joint path-supremum transport bound. That announcement does not cover its full scope.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A new Palomar entry claims the sharp rate for correlated/singular initial laws but assumes bounded Markovian interactions and states fixed-time marginal Wasserstein estimates. The present target allows unbounded Lipschitz path-dependent interactions and asks a joint path-supremum transport bound. That announcement does not cover its full scope.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the sharp rate with an initial entropy hypothesis and explicitly asks whether initial transport control suffices. The later results checked here retain stronger initial information, use weaker metrics or rates, or concern empirical measures rather than the joint law of a fixed collection of particles. No complete resolution was located in the bounded literature and announcement checks through 17 October 2026.

This differs from the separate arbitrary-strength convex-interaction entropy question: the present question has a fixed finite horizon, general Lipschitz pairwise coefficients and possibly singular correlated initial laws. The stronger entropy assumption is the point at issue here.

The [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/initial-W2-chaos-review.json) records exact reading extents, current-status searches and duplicate comparisons. An independent selected-primary audit confirmed the initial hierarchy, unnormalized path metric, combined drift assumptions and uniform family quantifiers. The finite collection of small particle counts excluded by a source theorem can be absorbed into the constant using standard moment bounds; the sharp asymptotic question is unchanged.

All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. The fresh catalogue comparison accounts for all 22 matching listing windows; these concern generic transport, robust optimization or unrelated corollary numbers, rather than this particle-law question. Current listings were compared as descriptions, without certifying mission proofs.

The [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-initial-W2-review.json), [catalogue review](../FURTHER_problems/_tracking/parallel/rough-filtering/initial-W2-prove2-0094-review.json) and [coordinator status checks](../FURTHER_problems/_tracking/coordinator-selected-status-2026-10-17.json) preserve exact reading extents and implications. The original 54-page author version was read in full; parity with the final published body remains unchecked. Later comparison papers were read to the selected extents recorded in the packets. These bounded dated checks found no matching complete result or announcement.

A new Palomar entry claims the sharp rate for correlated/singular initial laws but assumes bounded Markovian interactions and states fixed-time marginal Wasserstein estimates. The present target allows unbounded Lipschitz path-dependent interactions and asks a joint path-supremum transport bound. That announcement does not cover its full scope. The formalization was not rebuilt in this review.


## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dc277d0d2f6f2a7d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
