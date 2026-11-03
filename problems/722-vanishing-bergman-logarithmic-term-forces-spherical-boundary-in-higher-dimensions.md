# 722. Vanishing Bergman logarithmic term forces spherical boundary in higher dimensions

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$ and let $`\Omega\subset\mathbb C^n`$ be a nonempty bounded connected open set with $`C^\infty`$ strongly pseudoconvex boundary. Thus, for a real smooth defining function $`r<0`$ on $`\Omega`$, with $`r=0`$ and $`dr\ne0`$ on $`\partial\Omega`$, the Levi form of $`r`$ is positive on the nonzero complex tangent vectors at each boundary point.

Let $`A^2(\Omega)`$ be the space of square-integrable holomorphic functions with respect to Euclidean volume. Its diagonal Bergman kernel is

```math
K_\Omega(z,z)=\sum_{j=1}^\infty |f_j(z)|^2,
```

where $`(f_j)`$ is any orthonormal basis of $`A^2(\Omega)`$. Near the boundary, write its Fefferman expansion as

```math
K_\Omega(z,z)=\frac{\phi(z)}{(-r(z))^{n+1}}+\psi(z)\log(-r(z)),
\qquad \phi,\psi\in C^\infty(\overline\Omega).
```

Suppose that the logarithmic coefficient vanishes to infinite order on the entire boundary: for every integer $`N\ge1`$, there is $`C_N<\infty`$ such that

```math
|\psi(z)|\le C_N(-r(z))^N
```

for all $`z\in\Omega`$ sufficiently close to $`\partial\Omega`$. Must $`\partial\Omega`$ be **locally spherical**? This means that every boundary point has a neighbourhood CR diffeomorphic to an open part of the unit sphere $`S^{2n-1}\subset\mathbb C^n`$, preserving the induced complex tangent structure.

This is the higher-dimensional Ramadanov conjecture. The condition is independent of the smooth defining function and of the flat ambiguity in the logarithmic coefficient. No assumption that the Bergman metric is Kähler–Einstein, that the boundary is real analytic, or that the domain is simply connected is imposed. The conclusion is local CR equivalence, not a global biholomorphism with a ball. The known two-dimensional case is excluded from the question.

## Application

The Bergman kernel reproduces square-integrable holomorphic functions and encodes boundary geometry. The conjecture asks whether the absence of one type of kernel singularity identifies the local geometry of a sphere. It connects analytic function approximation spaces with inverse geometric characterisation.

## References

1. S. Nemirovski and R. Shafikov, [*Note on the paper of Fu and Wong on strictly pseudoconvex domains with Kähler–Einstein Bergman metrics*](https://arxiv.org/abs/math/0605706v1) (2006), §2, equation (1) and the following conjecture. Published under the title *Conjectures of Cheng and Ramadanov*, Russian Mathematical Surveys **61** (2006), 780–782, [DOI](https://doi.org/10.1070/RM2006v061n04ABEH004349).
2. M. Engliš and G. Zhang, [*Ramadanov conjecture and line bundles over compact Hermitian symmetric spaces*](https://users.math.cas.cz/~englis/66.pdf), Mathematische Zeitschrift **264** (2010), 901–912, especially the distinction between domains in $`\mathbb C^n`$ and disc bundles in complex manifolds.
3. X. Huang and M. Xiao, [*Bergman–Einstein metrics, a generalization of Kerner’s theorem and Stein spaces with spherical boundaries*](https://sites.math.rutgers.edu/~huangx/huang-xiao-crell-2021.pdf), Journal für die reine und angewandte Mathematik **770** (2021), 183–203, Theorem 1.1. This resolves the different question with the Kähler–Einstein hypothesis.

## Status review


**Known cases:** The current strong Ramadanov paper treats real ellipsoids in C2. Cheng metric rigidity, general complex-manifold examples and stronger metric hypotheses do not settle flat Bergman logarithmic coefficient implying spherical boundary in every dimension at least three.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current strong Ramadanov paper treats real ellipsoids in C2. Cheng metric rigidity, general complex-manifold examples and stronger metric hypotheses do not settle flat Bergman logarithmic coefficient implying spherical boundary in every dimension at least three.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/math/0605706v1); [comparison source 2](https://doi.org/10.1070/RM2006v061n04ABEH004349); [comparison source 3](https://users.math.cas.cz/~englis/66.pdf); [comparison source 4](https://sites.math.rutgers.edu/~huangx/huang-xiao-crell-2021.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original source explicitly distinguishes this conjecture from Cheng’s conjecture and proves an implication towards Cheng’s result. Later resolution of Cheng’s conjecture does not reverse that implication. Counterexamples for domains in general complex manifolds do not meet the displayed ambient-space assumption. The 2026 strong Ramadanov result for real ellipsoids in $`\mathbb C^2`$ does not cover the displayed higher-dimensional family. The independent selected-primary, bounded current-version and announcement, semantic and all-status catalogue gates passed at their recorded extents. Asymptotic Einstein criteria impose additional conditions on a metric invariant; the displayed flatness condition is not automatically that criterion. The original final three-page publication and the later Advances in Mathematics body remain access/parity gaps; no complete proof claim has been inferred from their indexed descriptions.

The [source/current-results packet](../FURTHER_problems/_tracking/coordinator-potential/ramadanov-review-2026-10-18.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-ramadanov-review.json), [semantic comparison](../FURTHER_problems/_tracking/ramadanov-duplicates-review-2026-10-18.json) and [catalogue receipt](../FURTHER_problems/_tracking/ramadanov-catalogue-review-2026-10-18.json) record exact review scopes. These AI formulation and literature checks are not human peer review or certification of all cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d4dd7c6c094d0700**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
