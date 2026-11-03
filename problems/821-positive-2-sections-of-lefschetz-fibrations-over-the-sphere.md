# 821. Positive 2-sections of Lefschetz fibrations over the sphere

**Area:** Symplectic topology and smooth four-manifolds
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`f:X\to S^2`$ be a relatively minimal positive Lefschetz fibration. Here $`X`$ is a closed, connected, oriented smooth four-manifold; regular fibers are connected; critical values are distinct; the critical locus is nonempty; and each singularity has the orientation-compatible complex local model $`f(u,v)=uv`$. Relative minimality means that no fiber contains an embedded sphere of self-intersection $`-1`$.

Must there be a possibly disconnected embedded closed oriented surface $`S\subset X\setminus\mathrm{Crit}(f)`$ such that $`f|_S:S\to S^2`$ is a degree-two simple branched covering with positive branch points? Positivity means that, in compatible local coordinates, $`f(z,w)=z`$ and $`S=\{z=w^2\}`$. No genus bound is imposed on $`S`$.

## Application

The question asks whether two sheets always suffice to represent a fibration over the sphere by an embedded branched surface transverse to its regular fibers.

## Known progress

Baykur–Hamada's Theorem B supplies multisections of some degree. Their degree criterion, Theorem 6 and Corollary 8, reduces the question to whether the fiber divisibility
```math
m(f)=\min\{A\mathbin{\cdot}[F]>0:A\in H_2(X;\mathbb Z)\}
```

always divides two. Their section counterexamples do have 2-sections. Thus failure of an ordinary section does not settle this question. The stronger proposed primitivity of every fiber class has a documented proof gap.

## References

1. R. İ. Baykur, R. C. Kirby and D. Ruberman (eds.), *K3: A New Problem List in Low-Dimensional Topology*, Mathematical Surveys and Monographs **295**, AMS, 2026, Problem 2.22, Remark (3), [author copy](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf), physical p. 104.
2. R. İ. Baykur and N. Hamada, *Sections, pseudosections, and multisections of Lefschetz fibrations*, [arXiv:2610.01776v1](https://arxiv.org/pdf/2610.01776v1), 1 October 2026. See conventions on p. 3, §2.4, Theorem 6, Corollary 8, Remark 10 and Question 20 on p. 30; [version history](https://arxiv.org/abs/2610.01776).

- [Baykur and Hamada, revised preprint v2 (29 October 2026), Question 21 on p.33](https://arxiv.org/abs/2610.01776v2). Added in the 2026-10-30 recheck.

## Status review


**Known cases:** The revised 29 October 2026 preprint v2 was read at its renumbered Question 21, page 33. It explicitly retains the 2-section question and its equivalence to fiber divisibility dividing two. New sectionless examples still admit 2-sections; the stronger primitivity assertion still has a documented gap.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The revised 29 October 2026 preprint v2 was read at its renumbered Question 21, page 33. It explicitly retains the 2-section question and its equivalence to fiber divisibility dividing two. New sectionless examples still admit 2-sections; the stronger primitivity assertion still has a documented gap.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/2610.01776v2). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The coordinating review independently read the cited preprint's definitions, degree criterion and exact remaining question. The current version record showed only v1. Bounded searches on 25 October 2026 found no subsequent matching proof, counterexample or complete announcement. The positivity and nonempty-critical-locus conditions are essential: statements about achiral fibrations or arbitrary surface bundles have different scope.

Semantic comparison covered the pinned all-status index of 665 local AIM entries, 666 current public AIM entries and 372 OpenAI problem families, together with all 903 preceding local findings. No equivalent target was located. The obtained preliminary book text and current primary preprint support this formulation; published-book parity and a full audit of the preprint's proofs are not claimed.

The revision posted on 29 October 2026 retains this question as Question 21 on p.33. The fiber-divisibility criterion remains, and the primitivity assertion is still described as having a proof gap. The earlier source discussion above concerns v1.


## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-98822a4854b32aa7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
