# 815. Constant nonzero Bismut holomorphic sectional curvature

**Area:** Hermitian differential geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,J,g)`$ be a compact connected Hermitian manifold of complex dimension $`n\ge2`$, without boundary. Thus $`J`$ is an integrable complex structure and $`g(Ju,Jv)=g(u,v)`$. Write $`\omega(u,v)=g(Ju,v)`$ for its fundamental two-form.

Let $`\nabla^B`$ be its **Bismut connection**, also called the Strominger connection: it is the unique connection preserving $`g`$ and $`J`$ whose torsion tensor $`T^B`$ has $`g(T^B(u,v),w)`$ totally alternating. Let $`H^B`$ denote its holomorphic sectional curvature.

Suppose there exists one real constant $`c\ne0`$ such that
```math
H^B_p(v)=c
\qquad\text{for every }p\in M
\text{ and every nonzero }v\in T^{1,0}_pM.
```

Must $`g`$ be Kähler, equivalently $`d\omega=0`$?

The same constant is required at every point and in every complex tangent direction. This is the Bismut connection question for the given metric. It does not assume local conformal Kählerness, parallel torsion, or any extra curvature symmetry. Complex dimension two is known; the unresolved part concerns higher dimensions.

## Application

The Bismut connection provides a natural metric connection on complex manifolds with torsion. The question asks whether a nonzero constant holomorphic curvature forces that torsion to disappear, extending the rigidity of complex space forms to Hermitian geometry.

## Known progress

Chen and Zheng prove the conjecture for compact complex surfaces, as well as for left-invariant Hermitian metrics on complex nilmanifolds with nilpotent complex structure, and for Bismut Kähler-like metrics (whose Bismut curvature has the Kähler curvature symmetries), under the hypotheses of their Theorems 1–4.

Their August 2026 paper retains the general assertion as Conjecture 3 and proves it for all compact locally conformally Kähler manifolds (Theorem 3). That additional geometric assumption leaves the general question open.

Their September 2026 paper proves the assertion whenever the Bismut torsion is parallel (Theorem 2 and Corollary 4). The parallel-torsion hypothesis is additional; the general question above makes no such assumption.

The restriction $`c\ne0`$ is essential: standard isosceles Hopf manifolds provide non-Kähler metrics with zero Bismut holomorphic sectional curvature. Allowing the direction-independent value to vary with the point would give a different assertion.

## References

1. S. Chen and F. Zheng, *On Strominger space forms*, [arXiv:2111.07108v1](https://arxiv.org/abs/2111.07108v1), Conjecture 2 and curvature conventions, native p. 2; Theorems 1–4, native pp. 3–4. [Latest v2](https://arxiv.org/abs/2111.07108v2), revised 15 July 2022. Published in *The Journal of Geometric Analysis* **32** (2022), article 141, [doi:10.1007/s12220-022-00882-7](https://doi.org/10.1007/s12220-022-00882-7).
2. S. Chen and F. Zheng, *Locally conformally Kähler manifolds with constant Levi-Civita or Bismut holomorphic sectional curvature*, [arXiv:2608.01893v2](https://arxiv.org/abs/2608.01893v2), revised 7 August 2026, Conjecture 3 and Theorem 3, native p. 2.

3. S. Chen and F. Zheng, *Hermitian connections with parallel torsion and constant holomorphic sectional curvature*, [arXiv:2609.33374v1](https://arxiv.org/abs/2609.33374v1), submitted 27 September 2026, Theorem 2 and Corollary 4, native p. 3.

## Status review


**Known cases:** The new Bismut Hermitian-Einstein examples impose a Ricci condition, not constant Bismut holomorphic sectional curvature. The 2026 BTP results mainly concern Chern curvature with parallel torsion; the locally conformally Kahler Bismut result is a restricted class. None covers arbitrary compact Hermitian manifolds with nonzero constant Bismut holomorphic sectional curvature.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The new Bismut Hermitian-Einstein examples impose a Ricci condition, not constant Bismut holomorphic sectional curvature. The 2026 BTP results mainly concern Chern curvature with parallel torsion; the locally conformally Kahler Bismut result is a restricted class. None covers arbitrary compact Hermitian manifolds with nonzero constant Bismut holomorphic sectional curvature.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the original question, the latest original revision, current primary comparison statements, and all-status AIM/FURTHER records, the OpenAI announcement catalogue, and bounded indexed and live-returned Prove2Me material. No matching proof, counterexample or announced resolution of the general assertion was located in the bounded searches. The Chern and Levi-Civita connection problems and positive-bisectional-curvature uniformization concern different hypotheses. Selected native windows and access limits are retained in the review records; no whole-paper proof audit or exhaustive literature claim is made.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-933bf49159697a88**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
