# 1017. Fractal Weyl upper bound for hyperbolic manifolds with cusps

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X=\Gamma\backslash\mathbb H^{n+1}`$ be a smooth noncompact hyperbolic manifold, where $`\Gamma`$ is a geometrically finite discrete isometry group, and suppose $`X`$ has a cusp. Use the nonnegative Laplacian and the spectral parameter in

```math
(\Delta_X-n^2/4-\sigma^2)^{-1}.
```


Let $`\mathcal R(X)`$ contain its eigenvalue parameters and resonances, with the source's multiplicities. Let $`K\subset T^*X`$ consist of the maximally extended, bounded, unit-speed geodesics and set $`m=\dim_H K`$.

Does every $`C_0>0`$ admit $`C_1=C_1(X,C_0)>0`$ such that, for every $`r\in\mathbb R`$,

```math
\#\{\sigma\in\mathcal R(X):|\sigma-r|\le C_0\}
\le C_1(1+|r|)^{(m-1)/2}?
```


The window is a fixed complex disk centered on the real spectral axis. The exponent has no epsilon loss, and the constant need not be uniform over manifolds. This is the cusped restriction of Datchev's published conjecture. It does not impose the paper's separate nontrapping assumptions or replace $`m`$ by a limit-set dimension formula.

## Application

The estimate would bound the number of high-frequency scattering modes by the geometry of bounded rays. Cusps permit long excursions and complicate the connection between trapped dynamics and resonance counts.

## Status review


**Known cases:** Cusps, the exact trapped-set dimension exponent and no epsilon loss are essential. Convex-cocompact resonance improvements and selected Hecke-triangle results do not cover every cusped geometrically finite manifold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Cusps, the exact trapped-set dimension exponent and no epsilon loss are essential. Convex-cocompact resonance improvements and selected Hecke-triangle results do not cover every cusped geometrically finite manifold.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source identifies no-cusp quotients and surfaces with cusps but no funnels as known cases. The mixed cusp-and-funnel surface class and higher-dimensional cusp geometries motivate the proposed target. Selected later convex-cocompact counting theorems omit cusps. Cusped partial estimates also exist: the checked Hecke-family result allows an epsilon loss, and a primary Pohl extended-abstract excerpt reports a cumulative bound with a logarithmic factor for certain geometrically finite cusped classes. These observations do not establish the exact displayed estimate for the whole class.

A finite current and announcement review through 25 October 2026 located no matching full result. This is a bounded literature assessment, not proof of openness or verification of the cited proofs. The published printed909 formula was visually checked; the older 2012 preprint has a different displayed normalization and is not substituted for it.

## References

1. K. Datchev, [Resonance free regions for nontrapping manifolds with cusps](https://msp.org/apde/2016/9-4/apde-v9-n4-p06-s.pdf), Analysis & PDE9(4),2016,907–953, conjecture printed909 and known cases printed910.
2. F. Naud, A. Pohl and L. Soares, [Fractal Weyl bounds and Hecke triangle groups](https://arxiv.org/abs/1810.04489), v1,2018, Theorem1.1 and Corollaries1.2–1.3; selected theorem reading by the book peer.
3. L. Soares, [Resonance counting and spectral gaps for hyperbolic surfaces via Fourier decay](https://arxiv.org/html/2610.17276v1), v1,12October2026, Introduction and Theorem1.2; convex-cocompact scope.
4. A. Pohl, [OW2319 extended abstract](https://user.math.uni-bremen.de/apohl/files/Pohl_extended_abstract_OW2319.pdf), primary indexed theorem excerpt observed by root; full body access timed out, so exact broader theorem scope remains unverified here.

**Admission review:** 25 October 2026. The recorded primary-statement, current-status and semantic duplicate checks were completed before admission. Public AIM-head and complete OpenAI-CONTENTS comparisons were refreshed without a change. The dated, bounded search and access limits above remain part of this assessment.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-49dcd1f94b436809**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
