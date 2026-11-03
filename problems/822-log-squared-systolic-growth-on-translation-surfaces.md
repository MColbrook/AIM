# 822. Log-squared systolic growth on translation surfaces

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

A closed translation surface is a connected orientable surface formed by gluing finitely many Euclidean polygons along paired sides by translations. Its flat metric has cone angles that are positive integer multiples of $`2\pi`$.

Let $`\mathrm{sys}(S)`$ be the length of a shortest noncontractible closed geodesic of $`S`$, with geodesics allowed to pass through cone points. Define
```math
\mathrm{SR}(S)=\frac{\mathrm{sys}(S)^2}{\mathrm{area}(S)}.
```

Do absolute constants $`c>0`$ and $`g_0\ge2`$ exist such that, for **every** integer $`g\ge g_0`$, some genus-$`g`$ translation surface satisfies
```math
\mathrm{SR}(S)\ge c\,\frac{(\log g)^2}{g}?
```

The ratio is invariant under scaling, so area one is an equivalent normalization. The surfaces may vary over all strata. The systole here is a closed-loop length, rather than the length of a shortest saddle connection.

## Application

The question measures how large the shortest essential loop can be relative to area as the topology of a flat surface becomes more complex. Translation surfaces also provide geometric models for polygonal billiards and straight-line dynamics.

## References

- T. Columbus, F. Herrlich, B. Muetzel and G. Weitze-Schmithüsen, [*Systolic geometry of translation surfaces*](https://arxiv.org/pdf/1809.10327v4), Experimental Mathematics 33(3) (2024), 357–378, [DOI:10.1080/10586458.2022.2108946](https://doi.org/10.1080/10586458.2022.2108946), Conjecture 1.6 and equation (2); the discovery version labels it Conjecture 1.8.
- P. Buser, E. Makover and B. Muetzel, [*Translation surfaces with large systoles*](https://arxiv.org/html/2403.14923v1), Theorem 1.2 and following paragraph; [publication DOI:10.1142/S1793525325500220](https://doi.org/10.1142/S1793525325500220).

## Status review


**Known cases:** The known large-systole translation-surface construction has order log(g)/(g log log(g)) on a subsequence of genera. Saddle-connection and hyperbolic-surface results do not yield the requested log-squared closed-loop systolic ratio in every sufficiently large genus.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known large-systole translation-surface construction has order log(g)/(g log log(g)) on a subsequence of genera. Saddle-connection and hyperbolic-surface results do not yield the requested log-squared closed-loop systolic ratio in every sufficiently large genus.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 2026-10-30. Known upper bounds have order $`(\log g)^2/g`$, also for the supremal homological systolic ratio. Since the ordinary systole is no larger than the homological one, the displayed lower construction would establish both order claims in the source conjecture.

The newer construction supplies only $`\log g/(g\log\log g)`$, and only for infinitely many genera. It explicitly retains the stronger conjectural order. Recent graph-embedding and deformation results using shortest saddle connections concern a different quantity.

Bounded current searches found no matching full resolution or announcement. Nearby full statements in AIM, this collection and the current OpenAI announcement index differ. Review evidence: [owner](../FURTHER_problems/_tracking/focused-translation-surface-log-squared-systolic-growth-C355-A-20261030/OWNER-EXACT-ALL-GENUS-TRANSLATION-SURFACE-LOG-SQUARED-SYSTOLIC-LOWER-GROWTH-PRIMARY-PARTIALS-CURRENT-SEMANTIC-PROPOSAL.json), [independent model check](../FURTHER_problems/_tracking/focused-translation-surface-log-squared-systolic-growth-C355-A-20261030/C-INDEPENDENT-CLOSED-LOOP-SYSTOLE-ALL-GENUS-ORDER-AND2024-SUBSEQUENCE-MODEL-PEER.json), [coordinating review](../FURTHER_problems/_tracking/ROOT-FINAL-all-genus-translation-surface-log-squared-systolic-growth-admission-20261030.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a335c018f2a6390a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
