# 1023. Reznikov's geodesic-period decay conjecture

**Area:** Spectral geometry and hyperbolic surfaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a smooth compact boundaryless hyperbolic surface $`(M,g)`$ of curvature $`-1`$ and a periodic geodesic $`\gamma`$, parametrized by arc length over one full period. For each eigenfunction, use the normalization
```math
-\Delta_g e_\lambda=\lambda^2 e_\lambda,\qquad
\int_M |e_\lambda|^2\,dV_g=1.
```

Does every $`\varepsilon>0`$ admit a constant $`C=C(M,\gamma,\varepsilon)`$ such that
```math
\left|\int_\gamma e_\lambda\,ds\right|
\le C\lambda^{-1/2+\varepsilon},\qquad \lambda\ge1?
```

The bound must hold for every normalized eigenfunction. The geodesic is fixed as the frequency varies; immersed closed geodesics are permitted. No arithmetic or Hecke hypothesis is imposed. Here $`\lambda`$ is the square root of the Laplace eigenvalue.

## Application

Period integrals measure the net oscillation of an eigenmode along a closed trajectory. The conjecture quantifies cancellation at high frequency beyond currently known logarithmic decay.

## References

1. Y. Xi, [*Improved Generalized Periods estimates on Riemannian Surfaces with Nonpositive Curvature*](https://arxiv.org/html/1711.09864v3), Conjecture 1.1, Eq.(1.3), v3 (2018); *Mathematische Zeitschrift* **309**, article 41 (2025). [DOI](https://doi.org/10.1007/s00209-024-03670-x).
2. A. Reznikov, *A uniform bound for geodesic periods of eigenfunctions on hyperbolic surfaces*, *Forum Mathematicum* **27** (2015), 1569–1590. [DOI](https://doi.org/10.1515/forum-2012-0185).
3. J. Hou, [*Bounds for the periods of eigenfunctions on arithmetic hyperbolic 3-manifolds over surfaces*](https://doi.org/10.1007/s00209-025-03914-4), Theorem 1.1, *Mathematische Zeitschrift* **312**, article 38 (2026).

## Status review


**Known cases:** The geodesic is fixed while the eigenfunction frequency grows. The September 2026 effective equidistribution theorem averages closed geodesics, rather than giving this individual period decay for every eigenfunction.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The geodesic is fixed while the eigenfunction frequency grows. The September 2026 effective equidistribution theorem averages closed geodesics, rather than giving this individual period decay for every eigenfunction.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Mean-square period bounds do not give this individual estimate. Recent nonvanishing results fix the automorphic form and vary the geodesic. Hou's power saving concerns arithmetic three-dimensional manifolds and two-dimensional integration surfaces; it does not settle this target.

The [coordinating review](../FURTHER_problems/_tracking/focused-C206-toric-and-Reznikov-two-precise-gates-C-20261028/ROOT-INDEPENDENT-THREE-MODEL-PRIMARY-CURRENT-AND-DUPLICATE-FINAL-REVIEW.json) records primary passages, independent model review, current searches and all-status semantic duplicate checks. The exact statement uses the official preprint; complete published-edition parity was not established. Bounded searches do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-929e78209e13f6e6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
