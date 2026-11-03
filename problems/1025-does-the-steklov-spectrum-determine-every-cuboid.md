# 1025. Does the Steklov spectrum determine every cuboid?

**Area:** Spectral geometry and inverse problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For any integer $`d\ge3`$ and $`a=(a_1,\ldots,a_d)\in(0,\infty)^d`$, set

```math
\Omega_a=\prod_{j=1}^d(-a_j,a_j)\subset\mathbb R^d.
```

Write $`0=\sigma_0(\Omega_a)<\sigma_1(\Omega_a)\le\sigma_2(\Omega_a)\le\cdots`$ for the unweighted Steklov eigenvalues, repeated with multiplicity. The boundary condition is $`\partial_\nu u=\sigma u`$ on the entire boundary, with outward normal. Precisely, $`\sigma`$ is an eigenvalue when some nonzero real $`u\in H^1(\Omega_a)`$ satisfies

```math
\int_{\Omega_a}\nabla u\cdot\nabla v\,dx
=\sigma\int_{\partial\Omega_a}u v\,dS
\quad\text{for every }v\in H^1(\Omega_a).
```

**If $`\sigma_k(\Omega_a)=\sigma_k(\Omega_b)`$ for every $`k\ge0`$, must the multisets $`\{a_1,\ldots,a_d\}`$ and $`\{b_1,\ldots,b_d\}`$ coincide?** Equivalently, must the two cuboids be Euclidean isometric?

This is the unresolved higher-dimensional part of [1, Conjecture 1.9]. All side lengths are positive and unrestricted; scale is retained. The hypothesis uses the exact infinite spectrum, not just finitely many eigenvalues or asymptotic coefficients.

## Application

The Steklov spectrum describes harmonic boundary response. This question tests whether the complete idealized response identifies a rectangular medium's side lengths, before considering reconstruction from finite or noisy measurements.

## References

1. A. Girouard, J. Lagacé, I. Polterovich and A. Savo, *The Steklov spectrum of cuboids*, Mathematika **65** (2019), 272–310, [DOI](https://doi.org/10.1112/S0025579318000414); [author manuscript](https://arxiv.org/html/1711.03075v2), §§1.1–1.2 and 1.5, Corollaries 1.7–1.8 and Conjecture 1.9. The original v1 numbers the conjecture 1.8.
2. T. Hu, J. Shi and Q. Tang, *Strictly Convex Steklov-Isospectral Plane Domains*, [arXiv:2608.10557v2](https://arxiv.org/html/2608.10557v2), Theorem 1.1.2. Announced counterexamples in a different geometric class.
3. E. B. Dryden, C. Gordon, J. Moreno, J. Rowlett and C. Villegas-Blas, *The Steklov Spectrum of Convex Polygonal Domains II: Investigating Spectral Determination*, J. Geom. Anal. **36** (2026), 346, [DOI and full text](https://doi.org/10.1007/s12220-026-02597-5), §1 and Theorem 4.1.

## Status review


**Known cases:** All positive side lengths in every dimension at least three are included. Rectangles, cubes, planar polygons and smooth planar isospectral examples do not decide arbitrary cuboid determination.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

All positive side lengths in every dimension at least three are included. Rectangles, cubes, planar polygons and smooth planar isospectral examples do not decide arbitrary cuboid determination.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 2026-10-29. Source [1] settles rectangles and shows that a cube is determined among all cuboids. The remaining question is arbitrary cuboids in $`d\ge3`$. The smooth strictly convex planar pairs in [2] do not belong to this class; [3] concerns planar polygons.

Bounded exact-question, author, proof/counterexample and 2025–2026 searches located no complete or announced resolution of the cuboid conjecture. All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. [Owner review](../FURTHER_problems/_tracking/focused-Steklov-cuboid-isospectral-rigidity-C242-C-20261029/OWNER-EXACT-UNWEIGHTED-FULL-STEKLOV-CUBOID-SPECTRAL-ISOMETRY-PRIMARY2026-SCOPE-AND-DUPLICATE-PROPOSAL.json) and [coordinating review](../FURTHER_problems/_tracking/focused-Steklov-cuboid-isospectral-rigidity-C242-C-20261029/ROOT-EXACT-CUBOID-CURRENT-PLANAR-COUNTEREXAMPLE-SCOPE-AND-FINAL-ADMISSION-REVIEW.json) preserve the source, version, access and independent model checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ab61f2addb846336**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
