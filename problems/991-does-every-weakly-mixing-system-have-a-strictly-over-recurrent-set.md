# 991. Does every weakly mixing system have a strictly over-recurrent set?

**Area:** Ergodic theory and recurrence
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,\mathcal B,\mu)`$ be a standard nonatomic probability space, and let $`T:X\to X`$ be invertible and measure preserving, modulo null sets. Assume $`T`$ is weakly mixing: for all measurable $`E,F`$,
```math
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}
\left|\mu(E\cap T^{-n}F)-\mu(E)\mu(F)\right|=0.
```


Must there exist a measurable set $`A`$ with $`0<\mu(A)<1`$ such that
```math
\mu(A\cap T^{-n}A)>\mu(A)^2
\qquad\text{for every integer }n\ge1?
```


The same set must work at every positive lag. This is the strict form posed in Adams--Bergelson--Sun, Question 1.6. Invertibility makes the corresponding negative-lag inequalities equivalent; the inequality at zero is automatic. The nonatomic setting excludes the trivial one-point system.

## Application

Weak mixing makes correlations approach independence after discarding a set of lags of density zero. The question asks whether some event can nevertheless have strictly positive excess self-correlation at every lag.

## What is known

Adams proves this for strongly mixing invertible transformations, even with arbitrarily small positive measure. Adams--Bergelson--Sun prove strict over-independence on a density-one set of lags for every weakly mixing system, and prove related Cesaro inequalities. Neither conclusion supplies the required inequality at every individual lag. Boshernitzan--Frantzikinakis--Wierdl pose the related non-strict over-recurrence question.

## References

1. T. Adams, V. Bergelson and W. Sun, [*Under- and over-independence in measure preserving systems*](https://arxiv.org/pdf/1807.02966), Question 1.6, Theorems 1.4 and 1.8. *Israel Journal of Mathematics* **235** (2020), 349--384. [DOI](https://doi.org/10.1007/s11856-020-1960-9).
2. T. M. Adams, [*Over Recurrence for Mixing Transformations*](https://arxiv.org/pdf/1701.04345), v2 (2019), Section 1 and Theorem 3.1; public preprint.
3. M. Boshernitzan, N. Frantzikinakis and M. Wierdl, [*Under-recurrence in the Khintchine recurrence theorem*](https://arxiv.org/pdf/1603.07720), definitions in Section 2 and Section 2.4, Problem 1. *Israel Journal of Mathematics* **222** (2017), 815--840. [DOI](https://doi.org/10.1007/s11856-017-1606-8).

## Status review


**Known cases:** Strict over-recurrence at every lag on the given arbitrary weakly mixing system is required. Strong mixing, one constructed weakly mixing example, multiplicative-subsequence nonrecurrence and density-one conclusions do not settle it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Strict over-recurrence at every lag on the given arbitrary weakly mixing system is required. Strong mixing, one constructed weakly mixing example, multiplicative-subsequence nonrecurrence and density-one conclusions do not settle it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Primary question, latest versions and partial theorem hypotheses were checked through 27 October 2026. No matching full or announced solution was found. No matching target was found in the all-status AIM/OpenAI comparison or existing further-problem list. This is a bounded literature review, not a proof of openness. Strong mixing, density-one inequalities, Cesaro inequalities, and existence on a changed extension do not settle this all-lag question on the given weakly mixing system.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e1f4d6e7e11d01dd**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
