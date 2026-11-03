# 972. Almost-everywhere hyperbolicity for a flat-top unimodal family

**Area:** One-dimensional dynamical systems and ergodic theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`\alpha\geq1`$ and define a family of maps on $`[-1,1]`$ by

```math
g_b(x)=-1+b\left(1-e^{-1-|x|^{-\alpha}}\right)\quad(x\ne0),
\qquad g_b(0)=b-1,
```

with $`0<b<2`$. These parameters make $`g_b`$ a self-map of $`[-1,1]`$. The critical point at $`0`$ is infinitely flat. Is $`g_b`$ **hyperbolic for Lebesgue-almost every $`b`$** in this interval? Here hyperbolic means that $`g_b`$ has an attracting periodic orbit whose basin has a uniformly hyperbolic repelling complement, as in Dobbs [1, Conjecture 1.4]. The displayed interval gives a concrete self-map subfamily of the paper's parameter family.

## Application

This family is a model for nonlinear dynamics with extremely flat turning points. The conjecture would distinguish typical attracting periodic behavior in parameter space from the conservative or neutral alternatives left open by the existing invariant-measure theorem.

## Why this is not settled by the known theorem

Dobbs [1, Corollary 1.3] proves that for $`\alpha>1`$ these maps have no ergodic absolutely continuous invariant probability measure with a **positive** Lyapunov exponent. That statement alone does not force an attracting periodic orbit for almost every parameter: the paper explicitly discusses the remaining possibility of conservative dynamics or an invariant measure with zero or negative exponent. The conjecture is a parameter-measure statement, stronger than topological density of hyperbolic maps.

Flat-critical maps under a **non-recurrent Misiurewicz assumption** have later statistical results [2, 3], but those hypotheses and conclusions do not cover the almost-every-parameter assertion here.

## References

1. N. Dobbs, [*On cusps and flat tops*](https://aif.centre-mersenne.org/item/10.5802/aif.2858.pdf), *Annales de l'Institut Fourier* **64** (2014), 571–605, Conjecture 1.4 and Corollary 1.3, printed pp. 573–574.
2. H. Takahasi, [*Equilibrium states at freezing phase transition in unimodal maps with flat critical point*](https://arxiv.org/abs/1707.06435), arXiv:1707.06435 (2017); different non-recurrent setting.
3. Y. M. Chung and H. Takahasi, [*Large deviation principle for $`S`$-unimodal maps with flat critical point*](https://arxiv.org/abs/1708.03695), arXiv:1708.03695 (2017); different non-recurrent setting.

## Status review


**Known cases:** An infinitely flat critical point is essential. Polynomial unimodal typical-dynamics results and fixed nonrecurrent-map thermodynamic theorems do not imply almost-everywhere hyperbolicity for this family.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

An infinitely flat critical point is essential. Polynomial unimodal typical-dynamics results and fixed nonrecurrent-map thermodynamic theorems do not imply almost-everywhere hyperbolicity for this family.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-body, later-result and duplicate audit](../FURTHER_problems/_tracking/flat-top-unimodal-hyperbolicity-status-2026-10-21.json) records the precise map, the distinction from Dobbs's theorem, and the bounded status searches. It found no complete proof or counterexample through 21 October 2026; this does not rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-28cfaa2ec9a95b5b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
