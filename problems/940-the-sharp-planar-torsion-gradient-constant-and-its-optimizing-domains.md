# 940. The sharp planar torsion-gradient constant and its optimizing domains

**Area:** Elliptic PDE and convex shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every nonempty bounded open convex domain $`\Omega\subset\mathbb R^2`$, let $`u_\Omega\in H^1_0(\Omega)`$ be the unique weak solution of
```math
-\Delta u_\Omega=1\quad\text{in }\Omega,\qquad u_\Omega=0\quad\text{on }\partial\Omega.
```

Thus $`\int_\Omega\nabla u_\Omega\cdot\nabla\varphi=\int_\Omega\varphi`$ for every $`\varphi\in H^1_0(\Omega)`$.

Determine the exact value
```math
c_* = \sup_{\substack{\Omega\subset\mathbb R^2\text{ bounded, open, convex}\\|\Omega|=1}}
\|\nabla u_\Omega\|_{L^\infty(\Omega)}
```

and characterize every attaining domain up to Euclidean isometry. The norm is the interior essential supremum of the Euclidean gradient magnitude. No boundary smoothness, strict convexity or symmetry is imposed on the competitors.

Equivalently, determine the sharp coefficient and all equality cases in
```math
\|\nabla u_\Omega\|_{L^\infty(\Omega)}\le c_*\sqrt{|\Omega|}.
```

Existence of an optimizer is already known. The remaining question is its exact value and complete geometric characterization.

## Application

In Saint-Venant torsion, this gradient measures shear stress in a beam cross section under a fixed twist/forcing normalization. The problem identifies the largest possible maximum stress among convex cross sections of prescribed area. Fixing the applied torque instead changes the shape functional by a torsional-rigidity factor.

## References

1. Jeremy G. Hoskins and Stefan Steinerberger, *Towards Optimal Gradient Bounds for the Torsion Function in the Plane*, Journal of Geometric Analysis **31** (2021),7812–7841, [published article](https://doi.org/10.1007/s12220-020-00553-5); [author version1912.08376v3](https://arxiv.org/abs/1912.08376v3), Introduction, especially pp.1–2.
2. Krzysztof Burdzy, Ilias Ftouhi and Phanuel Mariano, *Geometric properties of optimizers for the maximum gradient of the torsion function*, [arXiv:2512.09400v2](https://arxiv.org/abs/2512.09400v2),17December2025, Introduction and Theorems1.1–1.2.
3. Michiel van den Berg, Dorin Bucur and Mickael Nahon, *Shape optimisation of the maximum of the gradient of the torsion function on convex sets*, [arXiv:2610.08408v1](https://arxiv.org/abs/2610.08408v1),6October2026, Introduction, Theorem4 and §2.

## Status review


**Known cases:** The exact area-normalized constant and all optimizers are still required. October 2026 existence and symmetry results, perimeter-normalized statements and optimality among ellipses do not determine this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact area-normalized constant and all optimizers are still required. October 2026 existence and symmetry results, perimeter-normalized statements and optimality among ellipses do not determine this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper asks for the optimal constant and extremal domain. The later results establish attainment, $`C^1`$ boundary regularity and a flat boundary segment containing a maximum-gradient point. The October2026 paper also produces an axially symmetric area optimizer. Its stronger assertion that every optimizer has that symmetry concerns the perimeter constraint. These results do not supply the exact area-normalized value or classify all attaining domains.

Numerical pictures suggest shapes, but no exact rounded-D description, uniqueness claim or certified numerical value is included here. Current searches located no matching complete solution or announcement. Existing torsion-height, torsional-rigidity, eigenvalue and clamped-plate problems concern different functionals.

The [coordinator review](../FURTHER_problems/_tracking/torsion-gradient-coordinator-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/torsion-gradient-current-review-2026-10-19.json), [duplicate comparisons](../FURTHER_problems/_tracking/torsion-gradient-duplicates-review-2026-10-19.json) and [independent scope audit](../FURTHER_problems/_tracking/parallel/continuum/torsion-gradient-sharp-constant-independent-audit-2026-10-19.json) record the selected reading extents and limits. This is a bounded literature review, not proof that every possible resolution has been excluded.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2b0f5b042bac97f4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
