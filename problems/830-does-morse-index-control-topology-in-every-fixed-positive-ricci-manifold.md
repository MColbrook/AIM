# 830. Does Morse index control topology in every fixed positive-Ricci manifold?

**Area:** Geometric analysis and minimal hypersurfaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^m,g)`$, $`m\ge3`$, be a fixed smooth closed connected Riemannian manifold with $`\mathrm{Ric}_g>0`$. Is there a constant $`C=C(M,g)>0`$ such that every smooth closed embedded minimal hypersurface $`\Sigma^{m-1}\subset M`$ satisfies
```math
\mathrm{index}(\Sigma)\ge C\,b_1(\Sigma;\mathbb R)?
```

Here $`b_1`$ is the dimension of first real homology, and the Morse index is the largest dimension of a space of smooth normal variations on which the second variation of area is negative definite. This definition also applies to one-sided hypersurfaces, using sections of the normal bundle.

The ambient metric is fixed; $`C`$ is independent of $`\Sigma`$, with no area bound. Only the first Betti number is requested.

## Application

Minimal hypersurfaces describe critical points of the area functional. This bound would control their first topological complexity measure using the number of independent deformations that decrease area, helping classify interfaces obtained by variational methods.

## Known progress and scope

The conjecture holds for numerous special ambient spaces. Kajigaya–Kunikawa prove it for unstable hypersurfaces in compact semisimple symmetric spaces, hence for all two-sided hypersurfaces there; their result does not cover arbitrary positive-Ricci metrics. Chen adds certain isoparametric ambient examples.

Máximo–Reiser–Semola's 2026 counterexamples have index one and unbounded first Betti number while the ambient manifolds and metrics vary. They refute a dimension-only bound, and do not refute the fixed-$`(M,g)`$ statement above. Bounds whose constants also depend on an area upper bound likewise leave this target open.

## References

1. L. Ambrozio, A. Carlotto and B. Sharp, [Comparing the Morse index and the first Betti number of minimal hypersurfaces](https://doi.org/10.4310/jdg/1519959621), *Journal of Differential Geometry* **108** (2018), 379–410. [Preprint v2](https://arxiv.org/abs/1601.08152v2), Conjecture, printed page 3.
2. T. Kajigaya and K. Kunikawa, [Index estimate by first Betti number of minimal hypersurfaces in compact symmetric spaces](https://doi.org/10.1007/s00526-025-03189-x), *Calculus of Variations and Partial Differential Equations* **65** (2026), article 21. [Latest preprint v2](https://arxiv.org/abs/2410.11585v2), introduction, Theorem 1.1 and Corollaries 1.2–1.3.
3. N. Chen, [ACS condition on minimal isoparametric hypersurfaces of positive Ricci curvature in unit spheres](https://arxiv.org/html/2603.09705v2), 23 March 2026, introduction and Theorem 1.2.
4. D. Máximo, P. Reiser and D. Semola, [Ricci curvature and minimal hypersurfaces with large Betti numbers](https://doi.org/10.1007/s00526-026-03283-8), *Calculus of Variations and Partial Differential Equations* **65** (2026), article 120. [Latest preprint v2](https://arxiv.org/html/2507.17305v2), Theorems A–B.

5. A. Song, [Morse index, Betti numbers and singular set of bounded area minimal hypersurfaces](https://arxiv.org/html/1911.09166v3), version3,23August2022, Theorem1. The area-dependent constant leaves the unrestricted target above open.

## Status review


**Known cases:** The 2026 index-one counterexamples vary the ambient manifold and metric. They refute a dimension-only estimate, but do not refute this fixed-ambient conjecture. Symmetric-space and ACS special cases and estimates with an area-dependent constant leave the target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 index-one counterexamples vary the ambient manifold and metric. They refute a dimension-only estimate, but do not refute this fixed-ambient conjecture. Symmetric-space and ACS special cases and estimates with an area-dependent constant leave the target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original precise formulation appears in the 2016 preprint, and the March 2026 primary source restates it while proving additional special cases. Bounded current and announcement searches through 28 October 2026 found no resolution for a general fixed positive-Ricci ambient metric. Searches and the varying-ambient counterexample comparison are evidence of current status, not a proof that no later resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b2322ac3ab3a8eb6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
