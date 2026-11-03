# 803. Can a three-dimensional ancient Ricci flow have spatially unbounded curvature?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a connected smooth noncompact three-manifold $`M`$, without boundary, and a smooth family of complete Riemannian metrics $`g(t)`$, $`t\in(-\infty,0)`$, satisfying
```math
\partial_t g(t)=-2\mathrm{Ric}_{g(t)},\qquad
K_{g(t)}(\sigma)\ge0
```

for every tangent two-plane $`\sigma`$ and every $`t<0`$, such that for some interior time $`t_0<0`$,
```math
\sup_{p\in M}\left|\mathrm{Rm}_{g(t_0)}(p)\right|_{g(t_0)}=\infty?
```


Here completeness is required at every time. Unboundedness refers to the spatial supremum at a fixed time, rather than curvature growth as time approaches an endpoint. No noncollapsing, symmetry or uniform curvature-pinching hypothesis is imposed.

## Application

Ancient Ricci flows model geometry seen when studying singularities. This asks whether completeness and nonnegative sectional curvature alone can prevent arbitrarily large curvature far out in space.

## Known progress

Cabezas-Rivas and Wilking [1, Theorem1.4(a)] construct a complete nonnegatively curved three-dimensional **immortal** flow with spatially unbounded curvature at every time $`t\ge0`$. Their Remark8.5(b) explicitly leaves the ancient question open.

Yokota [2, Theorem1] proves constant-curvature rigidity for complete ancient three-dimensional flows under the stronger uniform Ricci-pinching assumption $`\mathrm{Ric}\ge\rho\,\mathrm{Scal}\,g\ge0`$, with a fixed $`\rho>0`$.

The classification of noncompact ancient $`\kappa`$-solutions [3, Definition5.5 and Theorem6.3] assumes bounded curvature and noncollapsing. It does not answer the question above.

## References

1. E. Cabezas-Rivas and B. Wilking, *How to produce a Ricci flow via Cheeger–Gromoll exhaustion*, Journal of the European Mathematical Society **17**(12) (2015), 3153–3194; Theorem1.4(a), Remark8.5(b), p.3187. [DOI](https://doi.org/10.4171/JEMS/582); [published PDF](https://ems.press/content/serial-article-files/32088?nt=1).
2. T. Yokota, *Complete ancient solutions to the Ricci flow with pinched curvature*, Communications in Analysis and Geometry **25**(2) (2017), 485–506; Theorem1. [DOI](https://doi.org/10.4310/CAG.2017.v25.n2.a8); [published PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2017/0025/0002/CAG-2017-0025-0002-a008.pdf).
3. S. Brendle, *Hamilton's Ricci Flow*, Proceedings of the International Congress of Mathematicians 2026, Volume2: Plenary Lectures, pp.25–34; Definition5.5 and Theorem6.3. [DOI](https://doi.org/10.1137/25M1799052). [Publisher text](https://epubs.siam.org/doi/full/10.1137/25M1799052).

## Status review


**Known cases:** Unbounded-curvature immortal flows are not ancient examples. Bounded-curvature ancient kappa-solution classification and boundary/end results do not settle spatially unbounded curvature at a fixed interior time under only nonnegative sectional curvature.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Unbounded-curvature immortal flows are not ancient examples. Bounded-curvature ancient kappa-solution classification and boundary/end results do not settle spatially unbounded curvature at a fixed interior time under only nonnegative sectional curvature.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original question and selected source definitions were checked, including the distinction between ancient and immortal flows. Targeted searches through 24 October 2026 found no matching published or announced complete solution. Later pinching, noncollapsing and compact-tangent-shrinker results impose additional hypotheses. The all-status AIM, external-result and FURTHER target comparison found no equivalent problem.

Targeted Prove2Me searches and the nearest accessible primary entry did not yield a matching solution. The homepage timed out; this is a bounded current-status review, not certification of the entire website or every proof in the literature.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-78d423a647c23d09**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
