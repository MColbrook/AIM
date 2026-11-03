# 762. Maximum total number of lines on a smooth complex surface

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`d`$, let $`\mathcal H_d`$ consist of every smooth degree-$`d`$ hypersurface $`X\subset\mathbb P^3(\mathbb C)`$. A line means a complex projective line wholly contained in $`X`$, counted once as a geometric subset. The surface varies over all of $`\mathcal H_d`$.

Write $`L(X)`$ for the number of lines contained in $`X`$ and set

```math
L_d=\max_{X\in\mathcal H_d}L(X).
```


Determine $`L_d`$ for every integer $`d\ge5`$. In particular, determine the exact value of $`L_5`$.

These are finite attained integer maxima. There is no Fermat, symmetry, genericity or prescribed-configuration assumption, and intersecting lines are included.

## Application

This extremal question concerns the geometry and classification of complex projective surfaces and their configurations of degree-one curves. An answer requires a universal bound and an example attaining it.

## References

1. S. Andria, J. Rojas and W. Mangueira, [Maximal number of skew lines on Fermat surfaces](https://doi.org/10.4171/PM/2150), *Portugaliae Mathematica*83(2026),145-165, Introduction145-146. This states the general extremal questions as background; its own theorem concerns a fixed Fermat surface.
2. S. Boissiere and A. Sarti, [Counting lines on surfaces](https://numdam.org/item/ASNSP_2007_5_6_1_39_0.pdf), *Ann. Sc. Norm. Super. Pisa Cl. Sci.*(5)6(2007),39-52, Introduction.
3. S. Rams and M. Schutt, [Counting lines on surfaces, especially quintics](https://arxiv.org/html/1803.03548v2), Theorem1.2.
4. T. Bauer and S. Rams, [Counting lines on projective surfaces](https://arxiv.org/html/1902.05133v2), Theorem1.1.
5. X. Yu and Z. Zhu, [A smooth quintic surface with85lines and Picard number43](https://arxiv.org/html/2609.26862v1),22September2026, Introduction and Theorem1.1.

## Status review


**Known cases:** The objective counts all lines on smooth complex hypersurfaces, not pairwise-disjoint lines, lines of singularity or finite-characteristic surfaces. The current quintic bounds and general constructions leave the exact maxima unknown.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The objective counts all lines on smooth complex hypersurfaces, not pairwise-disjoint lines, lines of singularity or finite-characteristic surfaces. The current quintic bounds and general constructions leave the exact maxima unknown.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/PM/2150); [comparison source 2](https://numdam.org/item/ASNSP_2007_5_6_1_39_0.pdf); [comparison source 3](https://arxiv.org/html/1803.03548v2); [comparison source 4](https://arxiv.org/html/1902.05133v2); [comparison source 5](https://arxiv.org/html/2609.26862v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked26October2026. The known small-degree values are $`L_3=27`$ and $`L_4=64`$. The current quintic bounds are

```math
85\le L_5\le127.
```


Yu-Zhu construct85-line smooth quintics; Rams-Schutt give the universal127 upper bound. For general $`d\ge5`$, Fermat examples and Bauer-Rams give $`3d^2\le L_d\le11d^2-30d+18`$, with stronger constructions or bounds in particular degrees. None of these identifies the general maximum.

Current literature, version and complete announcement-statement comparisons found no matching exact resolution. The pairwise-disjoint-line extremum is a different objective. The positive-characteristic maximal-line theorem does not determine the complex maximum. Selected theorem passages were checked; this is not a certification of every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-043542eb7fc9e01a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
