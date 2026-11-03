# 858. Infinitesimal rigidity of weakly convex decomposable polyhedra

**Area:** Geometric rigidity and structural mechanics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`P\subset\mathbb R^3`$ be a finite compact polyhedral body with nonempty interior, bounded by a connected embedded closed polyhedral surface. Write its original vertex set as $`V=\{p_1,\ldots,p_n\}`$. Assume:

- Every $`p_i`$ is an extreme point of $`\mathrm{conv}(V)`$ (weak convexity).
- The solid $`P`$ admits a finite conforming partition into nondegenerate closed tetrahedra with vertices in $`V`$, covering $`P`$, with disjoint interiors and intersections that are common faces, edges or vertices (decomposability).

Let $`S`$ be the induced triangulation of $`\partial P`$. For every assignment of velocities $`q_i\in\mathbb R^3`$ satisfying

```math
(p_i-p_j)\cdot(q_i-q_j)=0
 \quad\text{for every edge }ij\text{ of }S,
```


must there exist $`a,\omega\in\mathbb R^3`$ such that

```math
q_i=a+\omega\times p_i\qquad(1\le i\le n)?
```


Only boundary edges constrain the flex; interior tetrahedralization edges may vary. No genericity, star-shapedness, codecomposability or ball-topology assumption is imposed. The original Definition 1.8 specifies the boundary-triangulation convention and its independence of the chosen vertex-preserving boundary triangulation [1].

## Application

This would give a geometric criterion excluding first-order mechanisms in nonconvex triangulated shells and bar frameworks, extending the classical convex rigidity theorem.

## Known progress

Published Theorem 1.7 proves the triangular-face case with an additional weak codecomposability hypothesis: a containing convex polyhedron $`Q`$ has every original vertex of $`P`$ among its vertices, and $`Q\setminus P`$ can be tetrahedralized using only vertices of $`Q`$. For nontriangular faces, compatible interior and exterior boundary triangulations matter [1, p.174].

The 2024 experiments retain the general conjecture; apparent flexible examples fail one of its hypotheses [2, Sections 3.2–3.4]. The 2026 generic rigidity theorem concerns different constraints and does not cover every exceptional realization [3, Theorem 1.2 and Table 1].

## References

1. I. Izmestiev and J.-M. Schlenker, *Infinitesimal rigidity of polyhedra with vertices in convex position*, Pacific Journal of Mathematics 248 (2010), no.1, 171–190, [DOI](https://doi.org/10.2140/pjm.2010.248.171), [published text](https://msp.org/pjm/2010/248-1/pjm-v248-n1-p10-p.pdf), Conjecture 1.5 and pp.172–175. [Original arXiv:0711.1981v1](https://arxiv.org/pdf/0711.1981v1), Definition 1.8, p.3.
2. J. Kevo, *Are All Weakly Convex and Decomposable Polyhedral Surfaces Infinitesimally Rigid?*, Rose-Hulman Undergraduate Mathematics Journal 25 (2024), no.1, Article 6, [journal page](https://scholar.rose-hulman.edu/rhumj/vol25/iss1/6/), [arXiv:2311.06934v2](https://arxiv.org/html/2311.06934v2).
3. M. Himmelmann, B. Schulze and M. Winter, *Rigidity of polytopes with edge length and coplanarity constraints*, [arXiv:2505.00874v3](https://arxiv.org/pdf/2505.00874v3) (2026), Theorem 1.2 and Table 1.

## Status review


**Known cases:** The available rigidity theorem adds weak codecomposability, and recent experimental work does not prove the full weakly convex decomposable conjecture. Edge-and-coplanarity rigidity results constrain more than the boundary-edge velocity equations in this target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The available rigidity theorem adds weak codecomposability, and recent experimental work does not prove the full weakly convex decomposable conjecture. Edge-and-coplanarity rigidity results constrain more than the boundary-edge velocity equations in this target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Independent primary-statement review and current searches on 25 October 2026 found no matching complete proof, counterexample or announcement. All 1,703 pinned AIM/OpenAI statement records and all 912 preceding local findings were included in duplicate review. This is a bounded status check, not certification of the cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e7c0230007bf449f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
