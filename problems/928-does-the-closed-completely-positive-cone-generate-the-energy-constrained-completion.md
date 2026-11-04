# 928. Does the closed completely positive cone generate the energy-constrained completion?

**Area:** Operators, matrices and computation
**Status:** ✅ SOLVED
**Last checked:** 2026-11-04

## Problem statement

Let $`\mathcal H_A,\mathcal H_B`$ be separable complex Hilbert spaces, with $`\mathcal H_A`$ infinite-dimensional. Let $`G\ge0`$ be self-adjoint on $`\mathcal H_A`$, with compact resolvent, minimum eigenvalue zero and eigenvalues tending to infinity. Write $`\mathcal T_1(\mathcal H)`$ for trace-class operators.

Let $`Y`$ be the real vector space of Hermiticity-preserving complex-linear maps $`T:\mathcal T_1(\mathcal H_A)\to\mathcal T_1(\mathcal H_B)`$ with finite ordinary diamond norm. Fix $`E>0`$, and equip $`Y`$ with
```math
\|T\|_{\diamond,E}^{G}
 =\sup_{\substack{\rho\ge0,\ \mathrm{Tr}\rho=1\\
 \mathrm{Tr}((G\otimes I_R)\rho)\le E}}
 \|(T\otimes\mathrm{id}_R)(\rho)\|_1,
```

where $`\rho`$ acts on $`\mathcal H_A\otimes\mathcal H_R`$ and $`\mathcal H_R`$ is an infinite-dimensional separable ancillary space.

Let $`X_G`$ be the completion of $`Y`$ in this norm, and let $`C_G`$ be the closure in $`X_G`$ of the cone of completely positive maps belonging to $`Y`$. Is
```math
X_G=C_G-C_G?
```

The question asks for an exact difference of two elements of the closed cone. Density of such differences is already known. No trace-preservation condition is imposed.

## Application

This asks whether limits of quantum operations controlled on energy-constrained inputs retain a decomposition into positive components with the same approximation property.

## References

- M. E. Shirokov, *On completion of the cone of completely positive linear maps with respect to the energy-constrained diamond norm*, **Lobachevskii Journal of Mathematics** 40(10) (2019), 1549–1568. [Published article](https://doi.org/10.1134/S1995080219100238); [author manuscript](https://arxiv.org/html/1810.10922v2), Theorems 1B and 3B, equation (31), and the conjecture in §5.
- L. van Luijk, *Energy-Limited Quantum Dynamics*, **Communications in Mathematical Physics** 406 (2025), article 120. [Published article](https://doi.org/10.1007/s00220-025-05282-w), Lemma 2.19(6), the following paragraph and footnote 11.

- M. J. Colbrook, [*Generating the energy-constrained completion by completely positive maps*](../research/solutions/928-energy-constrained-positive-cone/aim928.pdf), 3 November 2026. [TeX source](../research/solutions/928-energy-constrained-positive-cone/aim928.tex), [package and reproduction](../research/solutions/928-energy-constrained-positive-cone/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-operators-batch/928-review.md).

## Status review

**Outcome:** Affirmative proof.

**Resolution:** The specified closed completely positive cone generates the entire energy-constrained completion; the norm also satisfies an exact infimum formula. The [manuscript](../research/solutions/928-energy-constrained-positive-cone/aim928.pdf) and [individual audit](../research/solution_reviews/2026-11-03-operators-batch/928-review.md) give the complete proof, checked sources and exact target comparison. Review was performed by Codex (AI).

**Scope:** The norm formula is an infimum over decompositions; attainment for every element of the completion is not claimed.

### Earlier literature review, 2026-10-30

The CP components must lie in the closed cone obtained by completing ordinary bounded CP maps. Van Luijk Lemma 2.19(6) allows a larger finite-energy-norm cone and therefore does not prove generation of this particular closed cone.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. Shirokov identifies the closed cone with $`\mathfrak F_G^0`$ and the completion with $`\mathfrak Y_G`$. The 2025 theorem gives positive components in the larger finite-energy-constrained-norm cone. It does not require each component to belong to $`C_G`$; that additional requirement is the residual question here.

Current searches found no matching complete resolution or announcement. Semantic comparisons with all-status AIM/OpenAI records and the developing collection distinguished finite-dimensional channel decompositions, channel capacity and Trotter approximation. No equivalent target was located. This is a dated, bounded literature check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c9fe61540d4c4717**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
