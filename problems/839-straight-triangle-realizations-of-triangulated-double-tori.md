# 839. Straight-triangle realizations of triangulated double tori

**Area:** Geometric topology and polyhedral surfaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`K`$ be a finite abstract simplicial complex whose realization is a closed, connected, orientable surface of genus two. Does there always exist a choice of points $`p_v\in\mathbb R^3`$, one for each vertex $`v`$ of $`K`$, such that the map obtained by affine interpolation on every simplex is an embedding?

More explicitly, require every triangle to have three affinely independent vertex images and, writing
```math
P_\sigma=\mathrm{conv}\{p_v:v\in\sigma\},
```

require
```math
P_\sigma\cap P_\tau=P_{\sigma\cap\tau}
 \qquad\text{for every pair of simplices }\sigma,\tau\in K,
```

where $`P_\varnothing=\varnothing`$. All vertex images are distinct. Thus edges are straight segments, faces are flat triangles, and intersections are exactly those prescribed by $`K`$.

The given triangulation must be realized without subdivision or additional vertices. Vertex coordinates are free; no edge lengths or angles are prescribed.

## Application

This asks whether every abstract triangular mesh of a double torus can be displayed as an embedded surface in three-dimensional space while preserving its vertices, edges and faces. It separates the topology of a surface from the geometric constraints imposed by a particular mesh.

## References

1. H. Edelsbrunner and J. Harer, *Computational Topology: An Introduction*, supplied author draft with a 2008 preface, §X.3, printed p. 251 (native PDF p. 263). The draft asks the question for genera one through four. This source is an unfinished draft; its bytes and section numbering are not identified with the published 2010 edition. [Draft](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/edelcomp.pdf).
2. D. Archdeacon, C. P. Bonnington and J. A. Ellis-Monaghan, *How to exhibit toroidal maps in space*, Discrete & Computational Geometry **38** (2007), 573–594. The author draft dated 18 July 2004 explicitly asks the double-torus question as Question 10.4, and states the torus result as Corollary 1.2. [Article](https://doi.org/10.1007/s00454-007-1354-3). [Author draft](https://www.math.auckland.ac.nz/Research/Reports/Series/519.pdf).
3. S. Hougardy, F. H. Lutz and M. Zelke, *Polyhedra of genus 2 with 10 vertices and minimal coordinates*, arXiv:math/0507592v1 (2005). [Versioned preprint](https://arxiv.org/abs/math/0507592v1).
4. S. Hougardy, F. H. Lutz and M. Zelke, *Surface Realization with the Intersection Segment Functional*, native title of arXiv:math/0608538v2 (2009), especially the discussion of elementary subdivisions and edge expansions on pp. 9–11. The arXiv metadata uses “intersection edge functional”; the cited mathematical passage is in the versioned PDF. [Versioned preprint](https://arxiv.org/abs/math/0608538v2).

## Status review


**Known cases:** All ten-vertex genus-two triangulations are realizable, but this finite subfamily does not imply every triangulation is. Surface-graph framework rigidity and intrinsic holonomy-signature realizability do not embed the specified flat triangular complex without subdivision.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

All ten-vertex genus-two triangulations are realizable, but this finite subfamily does not imply every triangulation is. Surface-graph framework rigidity and intrinsic holonomy-signature realizability do not embed the specified flat triangular complex without subdivision.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The torus case is covered by reference 2. Its Question 10.4 separately identifies the double torus as the next case. The genus-two case is also explicitly included in reference 1.

Reference 3 realizes all 865 triangulations with the minimum number of vertices, namely ten. This is a finite subfamily of the problem above. Reference 4 explains why checking irreducible triangulations alone does not immediately settle the general question: geometric realizability is not automatically preserved by every inverse edge contraction. Reference 2's Theorem 10.5 concerns sufficiently large face-width and does not assert the conclusion for every triangulation.

The searches checked geometric and polyhedral realization, double tori, genus-two triangulations, nonrealizability and announced proofs or counterexamples. Recent planar-framework rigidity results concern realizations of a graph's one-skeleton and may place several vertices at the same location; they do not supply the surface embedding required here. The 2026 announcement on realizable holonomy signatures, arXiv:2608.01444v1, concerns intrinsic seamless parametrizations and quadrangulations, rather than embedding the given triangular complex into $`\mathbb R^3`$. Its abstract was inspected for this distinction; no full-proof review is claimed.

No matching resolution or announcement was found in these bounded searches. This does not certify the absence of unindexed work. A Prove2Me site search found no matching entry; live-site access remains a recorded gap.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c254ae769bec192b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
