# 805. Must biharmonic hypersurfaces of the round sphere have constant mean curvature?

**Area:** Geometric analysis and biharmonic maps
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`m\geq4`$ and let $`f:M^m\to\mathbb S^{m+1}`$ be a smooth, connected, boundaryless, isometric immersion into the unit round sphere. Assume that $`f`$ is **proper biharmonic**: its bitension field vanishes but its mean-curvature vector is not identically zero. Here “proper” means *nonminimal*, not that $`f`$ is a proper map. **Must the length $`|\mathbf H|`$ of its mean-curvature vector be constant on $`M`$?** No compactness or completeness condition is imposed. A connected nonconstant-mean-curvature proper biharmonic hypersurface would refute the assertion.

For a choice of local unit normal, write $`H`$ for the signed scalar mean curvature and $`A`$ for the shape operator. In the convention of reference 3, the biharmonic equations are

```math
\Delta H+H\mathrm{tr}(A^2)=mH,\qquad 2A(\nabla H)+mH\nabla H=0.
```

Thus the question can also be approached by ruling out nonconstant solutions of this geometric system arising from an isometric hypersurface immersion. The formulation with $`|\mathbf H|`$ is independent of the normal choice.

## Application

Constant mean curvature is a first step toward classifying proper biharmonic hypersurfaces in spheres. It would remove one major unknown before testing whether every such hypersurface is locally one of the known small-sphere or product-of-spheres examples.

## References

1. A. Balmuş, S. Montaldo and C. Oniciuc, [*Classification results for biharmonic submanifolds in spheres*](https://arxiv.org/html/math/0701155), *Israel J. Math.* **168** (2008), 201–220, DOI [10.1007/s11856-008-1064-4](https://doi.org/10.1007/s11856-008-1064-4), closing conjecture. They conjecture constant mean curvature for all biharmonic submanifolds of spheres; the hypersurface question here is a narrower case.
2. D. Fetcu, E. Loubeau and C. Oniciuc, [*Bochner–Simons formulas and the rigidity of biharmonic submanifolds*](https://arxiv.org/html/1801.07879v1), arXiv:1801.07879v1 (2018), Introduction, Conjecture 1 and conventions; later published in *J. Geom. Anal.* **31** (2021), 1732–1755, DOI [10.1007/s12220-019-00323-y](https://doi.org/10.1007/s12220-019-00323-y). The paper gives conditional rigidity results, not the unrestricted assertion.
3. Y. Fu, M.-C. Hong and D. Yang, [*Biharmonic hypersurfaces in space forms*](https://arxiv.org/html/2610.04165v2), arXiv:2610.04165v2 (8 October 2026), Introduction, Proposition 2.1 and Theorems 1.1–1.4. They explicitly identify the unrestricted spherical, arbitrary-dimensional case as open while proving restricted results.

## Status review


**Known cases:** The October 2026 biharmonic hypersurface preprint treats nonpositive ambient curvature. Its minimality conclusions do not prove constant mean curvature for arbitrary proper biharmonic hypersurfaces in the positively curved unit sphere. Restricted principal-curvature cases do not cover the target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The October 2026 biharmonic hypersurface preprint treats nonpositive ambient curvature. Its minimality conclusions do not prove constant mean curvature for arbitrary proper biharmonic hypersurfaces in the positively curved unit sphere. Restricted principal-curvature cases do not cover the target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original conjecture covers every codimension; this entry isolates its hypersurface case. The October 2026 source states that the unrestricted arbitrary-dimensional case remains open. Its nonpositive-curvature theorem concerns Euclidean and hyperbolic space forms, whereas its spherical results impose pointwise or scalar-curvature conditions and do not settle the unrestricted question. Low-dimensional and other geometric subclasses are known; this entry does not reopen those cases. Dated searches for a later proof, counterexample or announcement and a semantic check of AIM and FURTHER found no complete matching resolution or duplicate. The [audit](../FURTHER_problems/_tracking/biharmonic-sphere-cmc-audit-2026-10-23.json) records exact source passages and the limits of the search.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-796e110dc76eb7a4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
