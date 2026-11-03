# 989. Can aggregation preserve fat-shattering dimension with one logarithm in the number of classes?

**Area:** Statistical learning theory and combinatorial complexity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega`$ be a set, $`k\ge1`$, $`\gamma>0`$, and $`F_i\subseteq\mathbb R^\Omega`$ for $`1\le i\le k`$. Write $`\mathrm{fat}_\gamma(F)`$ for the usual $`\gamma`$-fat-shattering dimension, with a separate real threshold at each point. For an aggregation rule $`G:\mathbb R^k\to\mathbb R`$, define

```math
G(F_1,\ldots,F_k)=\{x\mapsto G(f_1(x),\ldots,f_k(x)):f_i\in F_i\}.
```


Assume $`G`$ **commutes with shifts**, $`G(u-r\mathbf 1)=G(u)-r`$ for every $`u\in\mathbb R^k`$ and $`r\in\mathbb R`$, and **commutes with truncation** in the exact sense of [1, equations (20)–(21)]. For clarity, let $`T_\gamma(t)`$ be $`0`$ for $`t\le-\gamma`$, $`1`$ for $`t\ge\gamma`$, and $`?`$ otherwise; set $`D(0)=\{0\}`$, $`D(1)=\{1\}`$ and $`D(?)=\{0,1\}`$. Truncation commutation means that, for every $`\gamma,u`$ and every choice $`b_i\in D(T_\gamma(u_i))`$,

```math
G(b_1,\ldots,b_k)\in D\bigl(T_\gamma(G(u))\bigr).
```


**Is there a universal constant $`C>0`$ such that**, whenever $`\mathrm{fat}_\gamma(F_i)\le d`$ for every $`i`$,

```math
\mathrm{fat}_\gamma\bigl(G(F_1,\ldots,F_k)\bigr)
\le C d k\mathrm{Log}(k),
\qquad \mathrm{Log}(k)=\log(\max\{e,k\})?
```


The constant must work for every permitted $`G`$, $`\Omega`$, $`k`$, $`d`$, $`\gamma`$ and collection of real-valued classes. This is exactly the published open problem (28) in [1, printed p. 17]. The case $`d=0`$ is already covered by its Theorem 1.

## Application

The fat-shattering dimension controls the complexity of real-valued hypothesis classes in statistical learning. Aggregation combines predictors or loss classes, for example by taking a pointwise maximum, minimum or median. The proposed estimate would give a sharp general bound for these operations using only the complexity of their constituent classes, without the extra logarithm in the known general estimate [1, §§1.2 and 5].

## Known results and scope

Theorem 1 of [1] proves $`35D_\gamma\log^2(126D_\gamma)`$ for $`D_\gamma=\sum_i\mathrm{fat}_\gamma(F_i)>0`$ and zero when $`D_\gamma=0`$. For maxima of unrestricted affine classes, Theorems 7–8 show matching order $`d k\mathrm{Log}(k)`$; this special case does not prove the general bound. The paper explains that an earlier claimed sharp estimate relied on an erroneous disambiguation argument [1, §5].

The later scale-sensitive learning result [2, Proposition 3] proves qualitative preservation of $`\gamma`$-uniform convergence under 1-Lipschitz aggregation of bounded $`[0,1]`$-valued classes. It does not state the universal quantitative bound at the same fat-shattering scale asked for here. The adjacent Conjecture 11 in [1] is a different lower-bound statement and is outside this page.

## References

1. I. Attias and A. Kontorovich, [*Fat-Shattering Dimension of $`k`$-fold Aggregations*](https://www.jmlr.org/papers/volume25/21-1193/21-1193.pdf), *Journal of Machine Learning Research* **25** (2024), article 144, 1–29; Theorem 1, equations (7), (20)–(21), and open problem (28).
2. S. Aiyer, Y. Mansour, S. Moran, H. Shao and T. Waknine, [*Scale-Sensitive Shattering: Learnability and Evaluability at Optimal Scale*](https://arxiv.org/pdf/2605.13684v2), arXiv:2605.13684v2 (2026), Proposition 3 and §4.4.

## Status review


**Known cases:** A single logarithm and the source exact truncation/shift rules are required for every aggregation. New scale-sensitive learning estimates and maximum-only statements do not give this precise general bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A single logarithm and the source exact truncation/shift rules are required for every aggregation. New scale-sensitive learning estimates and maximum-only statements do not give this precise general bound.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [coordinator audit](../FURTHER_problems/_tracking/j135-fat-shattering-aggregation-eq28-coordinator-audit-2026-10-23.json) and [independent source review](../FURTHER_problems/_tracking/journal0876-j135-aggregation-eq28-independent-audit-2026-10-23.json) record the source passages, exact hypotheses, later-result comparison, bounded proof and announcement searches, and AIM/FURTHER duplicate check. These checks do not certify that every later result has been found, nor credit a complete reading of the article or journal.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dbf7a0173db5c55c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
