# 948. Sharpness of the Beran conductivity upper bound at fixed three-point parameter

**Area:** Homogenization, composite materials, and variational bounds
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider statistically homogeneous, geometrically isotropic two-phase composites in $`\mathbb R^3`$, with isotropic phase conductivities $`\sigma_1 I`$ and $`\sigma_2 I`$, where $`\sigma_1>\sigma_2>0`$. Geometric isotropy means that all phase correlation functions are invariant under rotations, as in Milton, §15.6. Only geometries with a deterministic homogenized scalar conductivity are included. Assemblages and limits with separated microscopic scales are allowed through the closure below.

For a geometry $`G`$, write $`f_1=f(G)\in(0,1)`$ for its phase-1 volume fraction and $`f_2=1-f_1`$. Normalize its three-point microstructural parameter $`\zeta_1=\zeta(G)`$ by the contrast expansion for that same geometry:
```math
\sigma_G^*(1+t,1)
=1+f_1t-\frac{f_1f_2}{3}t^2
+\frac{f_1f_2(f_2+2\zeta_1)}9t^3+O(t^4).
```

This is the parameter in Milton's equation (15.33); it satisfies $`0\leq\zeta_1\leq1`$. Put $`\zeta_2=1-\zeta_1`$.

The Beran bound, equation (26.5), states that
```math
\sigma_G^*(\sigma_1,\sigma_2)\leq
U(f_1,\zeta_1;\sigma_1,\sigma_2)
:=f_1\sigma_1+f_2\sigma_2
-\frac{f_1f_2(\sigma_1-\sigma_2)^2}
{f_2\sigma_1+f_1\sigma_2+2(\zeta_1\sigma_1+\zeta_2\sigma_2)}.
```

For fixed $`\sigma_1,\sigma_2`$, let $`\mathcal A_{\sigma_1,\sigma_2}`$ be the closure in $`\mathbb R^3`$ of the triples
```math
\bigl(f(G),\zeta(G),\sigma_G^*(\sigma_1,\sigma_2)\bigr)
```

realized by the admissible geometries above.

**Is the Beran upper bound universally sharp in this joint attainable closure?** Precisely, for every $`f\in(0,1)`$, $`\zeta\in[0,1]`$, and $`\sigma_1>\sigma_2>0`$, is
```math
\bigl(f,\zeta,U(f,\zeta;\sigma_1,\sigma_2)\bigr)
\in\mathcal A_{\sigma_1,\sigma_2}?
```

Equivalently, can one find admissible geometries whose volume fractions tend to $`f`$, whose three-point parameters tend to $`\zeta`$, and whose effective conductivities tend to this bound? The question concerns sharpness using only these parameters, rather than a bound for one prescribed full correlation function or one restricted cell model.

## Application

The answer would identify whether volume fraction and one three-point statistic suffice to determine the largest effective conductivity allowed by this bound, or whether a stricter universal constraint on composite design is needed.

## References

1. G. W. Milton, *The Theory of Composites*, Cambridge University Press, 2002, §§14.2 and 15.6, equation (15.33), and §26.2, equation (26.5), printed p. 555 (native PDF p. 580). [Author-hosted book](https://www.math.utah.edu/~milton/TheoryCompositesNOPRINT.pdf).
2. C. Kern, O. D. Miller and G. W. Milton, *Tight Bounds on the Effective Complex Permittivity of Isotropic Composites and Related Problems*, Physical Review Applied **14**, 054068 (2020), equation (7) and the discussions of attainability in §§II and V. [Published article](https://doi.org/10.1103/PhysRevApplied.14.054068). [Latest arXiv revision, v2 (2023)](https://arxiv.org/abs/2006.03830v2).
3. K. J. Deshmukh and G. W. Milton, *Bounds on the Uniaxial Effective Complex Permittivity of Two-phase Composites and Optimal or Near Optimal Microstructures*, arXiv:2507.09398v1 (2025), §§1 and 7. [Preprint](https://arxiv.org/abs/2507.09398v1).

## Status review


**Known cases:** Universal attainment in the joint (fraction, three-point parameter, conductivity) closure is needed. Partial first-arc attainment, second-arc improvement and uniaxial complex-permittivity results have different targets.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Universal attainment in the joint (fraction, three-point parameter, conductivity) closure is needed. Partial first-arc attainment, second-arc improvement and uniaxial complex-permittivity results have different targets.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Milton explicitly asks whether equation (26.5) can be improved away from special attainable cases. Those examples are historical evidence of partial sharpness; no exhaustive list of currently known attainable parameter values is asserted here.

The upper bound above is the first-arc expression in Kern–Miller–Milton, equation (7), with $`u_1=(f_2+2\zeta_1)/3`$ and $`u_2=(f_1+2\zeta_2)/3`$. Their partial attainment and numerical approximation of that arc do not establish universal sharpness. Their optimal improvement of the second arc addresses a different bound. The latest arXiv revision retains this distinction. Deshmukh–Milton concerns uniaxial permittivity and two-dimensional sensitivity bounds; its conclusion still discusses gaps in the analogous isotropic arc construction.

Targeted searches through 24 October 2026 did not locate a proof, announced full resolution, or a strict universal improvement of this fixed-parameter upper bound. This records the scope of the literature check, not a certification of every proof in the cited works.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8d8806fcaa64eb1d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
