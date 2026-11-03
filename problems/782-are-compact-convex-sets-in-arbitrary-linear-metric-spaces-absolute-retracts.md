# 782. Are compact convex sets in arbitrary linear metric spaces absolute retracts?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`E`$ be a metrizable topological vector space, without assuming local convexity, and let $`C\subset E`$ be compact and convex. Must $`C`$ be an **absolute retract**? That means that whenever $`C`$ is embedded as a closed subset of a metrizable space $`Y`$, there is a continuous retraction $`Y\to C`$.

The question asks for the absolute-retract property of every such $`C`$. It does not ask only whether continuous self-maps of $`C`$ have fixed points.

**Editorial clarification:** Make the intended nonempty compact-convex convention explicit.

## Application

The absolute-retract property lets continuous maps into $`C`$ extend from closed subsets of metrizable spaces. A positive answer would bring this extension theory to compact convex sets even when the surrounding vector space has no locally convex topology.

## References

1. T. Banakh, R. Cauty and M. Zarichnyi, *Open problems in infinite-dimensional topology*, in [*Open Problems in Topology II*](https://www.sciencedirect.com/book/9780444522085/open-problems-in-topology-ii), Elsevier (2007), Chapter 56, Question 5.1, printed p. 605. The [contributor-hosted book PDF](https://carmamaths.org/resources/jon/Preprints/Books/Open%20Probs%20in%20Top/open2.pdf) contains the checked passage; full published-text parity remains unverified.
2. Lê Hoàng Trí and Nguyễn Hoàng Thanh, [*Some remarks on the AR-problem*](https://math.ac.vn/public/uploads/files/0903389.pdf), *Acta Mathematica Vietnamica* **34** (2009), 389–400, pp. 389–390, Problems 1.1–1.2 and Theorems 1.3–1.4.
3. Lê Hoàng Trí and Trần Lê Thương, [*The AR-property of compact convex sets in metric linear spaces with a basis*](https://jst-ud.vn/jst-ud/article/download/8125/5698), *The University of Danang Journal of Science and Technology* **20** (11.1) (2022), 39–42.

- [G. X. Yuan, May 2026 author-uploaded correction and supporting lemmas for the claimed general AR theorem](https://www.researchgate.net/publication/404399495_A_Refined_Construction_of_Partition_of_Unity_Yuan_Dominant_d-Gap_Lemma_on_Compact_Hausdorff_TVSs). Added in the 2026-10-30 recheck.

## Status review


**Known cases:** The current full-scope Yuan claim was inspected through its supporting Lemmas A.1-A.2 and Theorems A.6-A.7. Lemma A.1 is false even for a connected interval with a two-member proper open cover: any subordinate partition has a tie by the intermediate value theorem. Refinement cannot repair this, because a unique maximal index would be locally constant and hence constant on a connected interval. Therefore this argument does not establish the claimed general AR theorem. Existing locally convex and basis cases remain partial progress.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current full-scope Yuan claim was inspected through its supporting Lemmas A.1-A.2 and Theorems A.6-A.7. Lemma A.1 is false even for a connected interval with a two-member proper open cover: any subordinate partition has a tie by the intermediate value theorem. Refinement cannot repair this, because a unique maximal index would be locally constant and hence constant on a connected interval. Therefore this argument does not establish the claimed general AR theorem. Existing locally convex and basis cases remain partial progress.

Additional comparison sources: [comparison source 1](https://www.sciencedirect.com/book/9780444522085/open-problems-in-topology-ii); [comparison source 2](https://carmamaths.org/resources/jon/Preprints/Books/Open%20Probs%20in%20Top/open2.pdf); [comparison source 3](https://math.ac.vn/public/uploads/files/0903389.pdf); [comparison source 4](https://jst-ud.vn/jst-ud/article/download/8125/5698); [comparison source 5](https://www.researchgate.net/publication/404399495_A_Refined_Construction_of_Partition_of_Unity_Yuan_Dominant_d-Gap_Lemma_on_Compact_Hausdorff_TVSs). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2022 article explicitly treats the unrestricted problem as unresolved and proves the absolute-retract property when the linear metric space has a Schauder basis, including some spaces that are not locally convex. Dugundji's classical theorem handles locally convex spaces, while Cauty's noncompact counterexample does not apply to compact $`C`$. Searches through 22 October 2026 found no announced unrestricted resolution or exact AIM/FURTHER duplicate. These are bounded checks, recorded in the [status](../FURTHER_problems/_tracking/compact-convex-AR-2026-10-22-status.json) and [duplicate](../FURTHER_problems/_tracking/compact-convex-AR-2026-10-22-duplicates.json) audits; the contributor-hosted chapter's full published-text parity remains unverified.

A 2026 general AR claim was also checked in the author-uploaded text [additional reference]. Its Theorem A.7 uses Lemma A.1, which asserts a subordinate continuous partition of unity with a unique largest component everywhere for every finite open cover. This lemma is false. Take K=[0,1] with the relative-open cover U1=[0,2/3), U2=(1/3,1]. For any subordinate partition (phi1,phi2), phi1(0)=1 and phi1(1)=0, so some point has phi1=phi2=1/2. Refining the cover cannot avoid the obstruction: a unique largest index is locally constant, hence constant on connected K, forcing one proper cover member to contain K. Thus the proposed proof does not resolve the general question. This is a specific obstruction to that argument, not a counterexample to the AR conjecture.


## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-385efa0ef5fffe9e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
