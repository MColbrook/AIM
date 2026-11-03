# 674. One shared value with multiplicity among four meromorphic shared values

**Area:** Complex analysis and value distribution
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`f,g`$ be nonconstant meromorphic functions on $`\mathbb C`$, and let $`a_1,a_2,a_3,a_4`$ be four distinct points of the Riemann sphere $`\widehat{\mathbb C}`$. Suppose
```math
f^{-1}(\{a_j\})=g^{-1}(\{a_j\}),\qquad j=1,2,3,4.
```

Suppose also that the multiplicities agree at every point of the common $`a_4`$-fibre. For a finite value $`a`$, its multiplicity is the zero order of $`f-a`$ or $`g-a`$; for $`a=\infty`$, it is the pole order. Common empty fibres are permitted and satisfy this condition vacuously.

Must the multiplicities agree at every point of each of the other three common fibres?

There is no restriction on growth, periodicity, derivatives or difference equations. This asks whether one value shared **counting multiplicities** (CM), together with three further values shared **ignoring multiplicities** (IM), forces all four values to be shared CM. It does not assert $`f=g`$; distinct Möbius-related functions are allowed. The case $`f=g`$ is immediate.

## Application

This is a foundational question in value distribution: how much information about a meromorphic function is encoded by the locations where it assumes a few specified values? The issue is whether multiplicity information at just one value forces it at the other three.

## References

1. N. Steinmetz, [*Reminiscence Of An Open Problem: Remarks On Nevanlinna's Four-Value-Theorem*](https://arxiv.org/abs/1102.3383v1), sole arXiv v1, 16 February 2011, physical pp. 2–4 and 8; rescaling cautions on p. 16. This is the discovery source.
2. X.-M. Li, Q.-F. Zhai and H.-X. Yi, [*On a question of Gary G. Gundersen concerning meromorphic functions sharing three distinct values IM and a fourth value CM*](https://arxiv.org/html/2402.03248v8), arXiv v8, 6 January 2026, Question 1, Theorem 7 and Section 5, Conjecture 1. Announced partial progress; its complete proof has not been independently certified here.
3. N. Steinmetz, [*Algebraic curves and meromorphic functions sharing pairs of values*, preprint](https://arxiv.org/html/2410.01624v1), sole v1, 2 October 2024, Introduction and Section 3, hypothesis (H). Associated publication: *Annales Fennici Mathematici* **50** (2025), 79–95, [DOI](https://doi.org/10.54330/afm.157535). Complete final-body parity has not been checked.

## Status review


**Known cases:** The current v8 primary retains the two-infinite-order case as Conjecture 1. Its finite-order theorem, the two-CM theorem, and five-shared-pair results do not settle one-CM/three-IM at arbitrary growth. Fresh later-result and public-venue searches found no matching complete announcement.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current v8 primary retains the two-infinite-order case as Conjecture 1. Its finite-order theorem, the two-CM theorem, and five-shared-pair results do not settle one-CM/three-IM at arbitrary growth. Fresh later-result and public-venue searches found no matching complete announcement.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/2402.03248v8); [comparison source 2](https://arxiv.org/abs/1102.3383). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source [1] explicitly leaves the one-CM/three-IM question open. Its established two-CM/two-IM theorem requires an additional multiplicity-preserving value. Gundersen's classical four-IM counterexample has unequal multiplicities at all four shared values and therefore does not refute the displayed question.

The latest inspected revision [2] announces a positive answer when at least one function has finite Nevanlinna order. Its concluding Conjecture 1 explicitly retains the case of two distinct infinite-order functions. The all-growth question is kept as one family, with this partial progress recorded here.

The formal main hypothesis (H) in [3] requires **four finite IM pairs plus one CM pair**, a total of five shared pairs. Our hypothesis supplies only three finite diagonal pairs after moving the CM value to infinity. The introduction contains a stronger-sounding phrase about reducing the three-IM/one-CM problem to computer algebra; its formal theorems were inspected separately and do not announce the displayed conclusion. Results requiring a derivative, a difference-polynomial relation or restricted growth likewise do not settle arbitrary pairs.

The complete pinned 17-page discovery preprint was read for question discovery, with an independent selected audit of the precise question and current progress. Its associated 2012 final body has not been compared throughout. The official 2025 PDF returned an access challenge; its complete final-body parity remains a recorded gap. No matching complete resolution or announcement was found in the bounded current searches and semantic duplicate checks. No exhaustive absence or certification of every cited proof is claimed.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/four-values-one-cm-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-four-values-one-cm-review.json), [current comparisons](../FURTHER_problems/_tracking/parallel/complex-bayesian/four-values-one-cm-current-comparisons.json), [duplicate review](../FURTHER_problems/_tracking/four-values-one-cm-duplicates-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/four-values-one-cm-coordinator-review-2026-10-19.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0f12b1070afae869**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
