# 781. Must every Finsler two-sphere have a simple closed geodesic?

**Area:** Finsler geometry and geodesic dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`F:TS^2\to[0,\infty)`$ be a smooth, strongly convex Finsler metric. In particular, **do not assume reversibility**: $`F(x,v)`$ may differ from $`F(x,-v)`$. Must $`(S^2,F)`$ have at least one closed geodesic $`\gamma:S^1\to S^2`$ whose image is an embedded circle?

Here *simple* means no self-intersections. It is stronger than *prime*, which merely means that the closed geodesic is not an iterate of a shorter one. This is the general Finsler-sphere question stated in [1, Remark 5.3].

## Application

The distinction between embedded and merely prime periodic geodesics affects the topology of Finsler geodesic flows. In the reversible setting considered by [1, Corollary 5.2], a single simple closed geodesic also helps distinguish when a periodic geodesic flow is *simple Zoll*: every geodesic is simple and closed.

## Known results and scope

Bangert and Long prove that every Finsler two-sphere has at least two distinct **prime** closed geodesics [2]. Their theorem permits self-intersections and therefore does not answer this question. De Philippis, Marini, Mazzucchelli and Suhr prove that every **reversible** Finsler two-sphere has at least three simple closed geodesics [3, Theorem 1.3]. Their hypothesis excludes the remaining, possibly nonreversible case. Katok's examples show that a nonreversible Finsler two-sphere can have only two closed geodesics [3, Introduction]; that count alone is not a counterexample to the existence of one simple geodesic.

## References

1. U. Frauenfelder, C. Lange and S. Suhr, [*A Hamiltonian version of a result of Gromoll and Grove*](https://aif.centre-mersenne.org/item/10.5802/aif.3247.pdf), *Annales de l'Institut Fourier* **69** (2019), no. 1, 409–419, Remark 5.3, p. 415. [DOI](https://doi.org/10.5802/aif.3247).
2. V. Bangert and Y. Long, [*The existence of two closed geodesics on every Finsler 2-sphere*](https://arxiv.org/pdf/0709.1243v2), *Mathematische Annalen* **346** (2010), 335–366, Theorem 1.1.
3. G. De Philippis, M. Marini, M. Mazzucchelli and S. Suhr, [*Closed geodesics on reversible Finsler 2-spheres*](https://arxiv.org/pdf/2002.00415v2), *Journal of Fixed Point Theory and Applications* **24** (2022), article 19, Theorem 1.3 and Introduction. [DOI](https://doi.org/10.1007/s11784-022-00962-9).

## Status review


**Known cases:** Reversibility is not assumed and simple means embedded image rather than merely prime. Three simple closed geodesics for reversible metrics and general closed-geodesic multiplicity do not supply one simple geodesic for every nonreversible Finsler sphere.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Reversibility is not assumed and simple means embedded image rather than merely prime. Three simple closed geodesics for reversible metrics and general closed-geodesic multiplicity do not supply one simple geodesic for every nonreversible Finsler sphere.

Additional comparison sources: [comparison source 1](https://aif.centre-mersenne.org/item/10.5802/aif.3247.pdf); [comparison source 2](https://doi.org/10.5802/aif.3247); [comparison source 3](https://arxiv.org/pdf/0709.1243v2); [comparison source 4](https://arxiv.org/pdf/2002.00415v2); [comparison source 5](https://doi.org/10.1007/s11784-022-00962-9). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-source, later-result and semantic-duplicate review](../FURTHER_problems/_tracking/finsler-simple-closed-geodesic-status-2026-10-21.json) distinguishes simple from prime geodesics and general from reversible metrics. No proof, counterexample or announced settlement for the stated universal claim was located in the bounded search through 21 October 2026.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-357f3f25c08ac72a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
