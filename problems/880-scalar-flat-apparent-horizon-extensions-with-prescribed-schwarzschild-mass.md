# 880. Scalar-flat apparent-horizon extensions with prescribed Schwarzschild mass

**Area:** Mathematical relativity / scalar curvature
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\gamma`$ be a smooth Riemannian metric on $`\mathbb S^2`$ for which the lowest eigenvalue of $`-\Delta_\gamma+K_\gamma`$ is positive, where $`K_\gamma`$ is its Gauss curvature. Write $`A=\mathrm{area}_\gamma(\mathbb S^2)`$. For every $`m>\sqrt{A/(16\pi)}`$, does there exist a smooth Riemannian metric $`G`$ on $`M=\mathbb S^2\times[0,\infty)`$ with all the following properties?

- $`(M,G)`$ is complete as a manifold with boundary and has one asymptotically flat end.
- $`R_G=0`$ everywhere, and $`\partial M`$ is minimal with induced metric isometric to $`\gamma`$.
- Outside a compact set, $`G`$ is isometric to an exterior region of the mass-$`m`$ Schwarzschild metric

```math
G_m=\left(1-\frac{2m}{r}\right)^{-1}dr^2+r^2g_{\mathbb S^2},\qquad r>2m,
```

  where $`g_{\mathbb S^2}`$ is the unit round metric.
- There is a global smooth foliation of $`M`$ by spheres, starting at $`\partial M`$, whose interior leaves have strictly positive mean curvature toward the end and which eventually coincides with the standard Schwarzschild spheres.

The strict inequality on $`m`$ is part of the question; equality is not requested. The spectral condition allows metrics whose Gauss curvature is negative on part of the sphere.

## Application

These would be time-symmetric vacuum initial data with a prescribed apparent-horizon geometry and an exactly Schwarzschild exterior. The question asks whether one can retain the sharp mass flexibility of the known construction while eliminating its region of positive scalar curvature.

## References

1. A. Carlotto, *The general relativistic constraint equations*, Living Reviews in Relativity **24** (2021), article2, corrected publication2022/2024. OpenProblem3.21, p.104, and Theorem3.20, p.103. [Published survey](https://doi.org/10.1007/s41114-020-00030-z).
2. C. Mantoulidis and R. Schoen, *On the Bartnik mass of apparent horizons*, Classical and Quantum Gravity **32** (2015),205002. Initial extension theorem and following vacuum question. [DOI](https://doi.org/10.1088/0264-9381/32/20/205002), [eligible preprint v3](https://arxiv.org/abs/1412.0382v3).
3. P. Miao and N. Xie, *Bartnik mass via vacuum extensions*, International Journal of Mathematics **30** (2019),1940006. Theorem1.3 and Remark1.1. [DOI](https://doi.org/10.1142/S0129167X19400068), [eligible preprint v2](https://arxiv.org/abs/1907.02039v2).

## Status review


**Known cases:** The nonnegative-scalar-curvature construction permits positive scalar curvature in a collar. Miao-Xie achieve scalar-flat minimal-boundary extensions for positive Gauss curvature but not the entire spectral class with prescribed Schwarzschild mass and global mean-convex foliation. Exterior gluing alone leaves interior scalar curvature unchanged.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The nonnegative-scalar-curvature construction permits positive scalar curvature in a collar. Miao-Xie achieve scalar-flat minimal-boundary extensions for positive Gauss curvature but not the entire spectral class with prescribed Schwarzschild mass and global mean-convex foliation. Exterior gluing alone leaves interior scalar curvature unchanged.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check: 17 October2026.** Carlotto explicitly asks for the scalar-flat analogue of the full extension theorem. Mantoulidis–Schoen provide all the listed geometric and mass properties with nonnegative scalar curvature, positive somewhere in their construction. Miao–Xie obtain scalar-flat extensions with minimal boundary and mass arbitrarily close to $`\sqrt{A/(16\pi)}`$ when $`K_\gamma>0`$, but do not require an exactly Schwarzschild exterior or give the full spectral class here.

Ordinary exterior scalar-curvature gluing preserves the scalar curvature in the untouched interior; applying it to the known nonnegative-curvature extension does not remove that interior region. Recent local static-vacuum extension and mass-stability results impose perturbative hypotheses around existing data and do not provide the displayed unrestricted construction.

The independent selected-primary audit passed, and the cached all-status catalogue comparison found no matching listing among the checked aliases. Coordinator review of the exact formulation, current theorem scope and duplicate comparisons passed.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/scalar-flat-horizon-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-scalar-flat-horizon-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/scalar-flat-horizon-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/scalar-flat-horizon-prove2-0154-review.json) and [coordinator review](../FURTHER_problems/_tracking/scalar-flat-horizon-coordinator-review-2026-10-17.json) preserve source versions and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-97d0206d85c24016**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
