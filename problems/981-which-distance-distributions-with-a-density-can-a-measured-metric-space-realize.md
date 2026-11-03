# 981. Which distance distributions with a density can a measured metric space realize?

**Area:** Probability, statistics and learning
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`f`$ be any probability density on $`[0,\infty)`$ whose associated probability law has $`0`$ in its support. Does there exist a **deterministic** complete separable metric space $`(S,d)`$ with a Borel probability measure $`\mu`$ such that, for independent $`X,Y\sim\mu`$, the distance $`d(X,Y)`$ has density $`f`$ [1, Problem 1.7]?

Aldous, Blanc and Curien call such a distance law *feasible*. They prove feasibility for finitely supported laws that charge $`0`$ and derive approximation and random-space results for certain densities, but leave this deterministic general-density question open [1]. Gross subsequently proved feasibility for every discrete law with $`0`$ in its support and for densities on $`[0,1]`$ bounded above and away from zero. Gross restates the general-density question as Problem 1.3 [2].

## Application

This is an inverse problem in probability and random geometry: it asks which one-dimensional laws can be encoded by distances between two independent samples from a single measured metric space. A characterization would clarify how much of a metric space can be prescribed through its pairwise-distance statistics.

## References

1. D. Aldous, G. Blanc and N. Curien, [*The distance problem on measured metric spaces*](https://afst.centre-mersenne.org/item/10.5802/afst.1835.pdf), *Ann. Fac. Sci. Toulouse Math.* **34** (2025), no. 5, 1345–1365, DOI: [10.5802/afst.1835](https://doi.org/10.5802/afst.1835), Problem 1.7 on printed p. 1347.
2. R. Gross, [*The distance problem via subadditivity*](https://ahl.centre-mersenne.org/item/10.5802/ahl.254.pdf), *Ann. Henri Lebesgue* **8** (2025), 1023–1035, DOI: [10.5802/ahl.254](https://doi.org/10.5802/ahl.254), Theorems 1.1–1.2 and Problem 1.3.

## Status review


**Known cases:** The realization must be one deterministic complete separable measured metric space for every density with zero in its support. The latest discrete and bounded-positive-density theorem and author July status note leave the general density case open.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The realization must be one deterministic complete separable measured metric space for every density with zero in its support. The latest discrete and bounded-positive-density theorem and author July status note leave the general density case open.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded audit](../FURTHER_problems/_tracking/j282-aldous-blanc-curien-distance-density-status-2026-10-22.json) compared the original statement with the later partial results and a [July 2026 status note by Gross](https://sarcasticresonance.wordpress.com/2026/07/01/the-distance-problem-is-still-open/). Targeted later-result, announcement and duplicate searches through 22 October 2026 found no resolution of the exact general-density question.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-84ead59799865473**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
