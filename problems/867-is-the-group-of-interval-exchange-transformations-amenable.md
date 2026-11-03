# 867. Is the group of interval exchange transformations amenable?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

An interval exchange transformation cuts the circle $`\mathbb R/\mathbb Z`$ into finitely many half-open arcs and translates those arcs to rearrange them. Under composition these transformations form a group $`\mathrm{IET}`$. Does $`\mathrm{IET}`$ admit a left-invariant finitely additive probability measure on all its subsets; equivalently, is $`\mathrm{IET}`$ amenable?

The question concerns the full group. It is already known that each subgroup whose translation angles have rational rank at most two is amenable; that result does not cover arbitrary interval exchanges.

## Application

Interval exchanges model flows in rational polygonal billiards and are central to ergodic theory. A positive answer would rule out non-abelian free subgroups of $`\mathrm{IET}`$, answering a question of Katok. A negative answer would exhibit a non-amenable finitely generated subgroup of interval exchanges.

## References

1. K. Juschenko, N. Matte Bon, N. Monod and M. de la Salle, [*Extensive amenability and an application to interval exchanges*](https://arxiv.org/html/1503.04977v1), *Ergodic Theory and Dynamical Systems* **38** (2018), 195–219, [DOI 10.1017/etds.2016.32](https://doi.org/10.1017/etds.2016.32), Question 1.6 and Theorem 1.9. Defines the group, asks the question and proves the rational-rank-at-most-two case.
2. N. Guelman and I. Liousse, [*Some elementary amenable subgroups of interval exchange transformations*](https://arxiv.org/html/2601.23054v1) (2026), introduction and Theorems 1–3. Records the lack of a known non-amenable finitely generated IET subgroup and establishes amenability for particular families.
3. [Prove2Me mission: IET amenability](https://prove2.me/missions/1797b6d3-635c-4c94-a69c-2f8ffe113bf4), cached full mission description from 21 October 2026. Discovery route and formalization plan; the mathematical status was checked against the primary papers above.

## Status review


**Known cases:** The January 2026 subgroup theorem covers selected elementary-amenable families. The source rational-rank-at-most-two result is also restricted, and the Prove2Me mission remains a question/formalization route rather than a matching proved full-group amenability theorem.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The January 2026 subgroup theorem covers selected elementary-amenable families. The source rational-rank-at-most-two result is also restricted, and the Prove2Me mission remains a question/formalization route rather than a matching proved full-group amenability theorem.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2018 paper poses the full-group question explicitly. The 2026 paper treats special subgroups and still describes the absence of a known non-amenable finitely generated example. Bounded later-result and announcement searches through 22 October 2026 found no proof or counterexample for the full group. Local AIM and FURTHER problem-text searches found no duplicate. This is a literature search, not a certificate of openness; the [audit](../FURTHER_problems/_tracking/w002-iet-amenability-status-2026-10-22.json) records its limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f9e546460c67450d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
