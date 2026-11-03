# 749. Critical velocity control for a rigid body moving in a bounded viscous fluid

**Area:** Fluid–structure interaction
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected domain with smooth boundary. Let $`S\subset\mathbb R^3`$ be a bounded connected smooth rigid-body shape with centroid at the origin, $`\overline S\subset\Omega`$, and $`\Omega\setminus\overline S`$ connected. Its density is a positive constant $`\rho_S`$; the fluid density and viscosity are one. Put

```math
S(t)=h(t)+Q(t)S,\qquad F(t)=\Omega\setminus\overline{S(t)},\qquad
\rho(t,x)=1_{F(t)}(x)+\rho_S1_{S(t)}(x),
```

where $`Q(t)\in SO(3)`$, $`h(0)=0`$ and $`Q(0)=I`$. Fix a finite $`T>0`$ and require $`\mathrm{dist}(\overline{S(t)},\partial\Omega)\ge\delta`$ on $`[0,T]`$ for some $`\delta>0`$.

Use the velocity field $`u`$ on all of $`\Omega`$, extended inside the body by its rigid velocity. The weak incompressible Navier–Stokes/Newton system with no-slip conditions is defined as follows. Assume

```math
(h,Q)\in W^{1,\infty}(0,T;\mathbb R^3\times SO(3)),\qquad
u\in L^\infty(0,T;L^2(\Omega)^3)\cap L^2(0,T;H^1_0(\Omega)^3),
```

Require $`\nabla\cdot u=0`$, and, for almost every $`t`$,

```math
u(t,x)=\ell(t)+\omega(t)\times(x-h(t))\quad(x\in S(t)),\qquad
h'=\ell,\qquad Q'=\mathcal S(\omega)Q,
```

with $`\mathcal S(\omega)v=\omega\times v`$. Let $`a\in L^2(\Omega)^3`$ be divergence free, have zero outer normal trace and be a rigid velocity on $`S`$. For every test field

```math
\varphi\in H^1(0,T;L^2(\Omega)^3)\cap L^\infty(0,T;H^1_0(\Omega)^3),\quad
\nabla\cdot\varphi=0,\quad D\varphi=0\text{ in }S(t),\quad\varphi(T)=0,
```

require

```math
-\int_0^T\!\int_\Omega \rho u\cdot\bigl(\partial_t\varphi+(u\cdot\nabla)\varphi\bigr)
+2\int_0^T\!\int_\Omega Du:D\varphi
=\int_\Omega\rho(0,x)a(x)\cdot\varphi(0,x),
\qquad Du=\tfrac12(\nabla u+\nabla u^\top).
```

Thus the fluid equation has no applied force, and the body's linear and angular momentum are driven by the fluid stress. This formulation includes their initial velocities through the rigid part of $`a`$. It imposes equality of fluid and rigid-body velocities at the interface through $`u\in H^1_0(\Omega)^3`$.

**Does the condition**

```math
\mathrm*{ess\,sup}_{0<t<T}\|u(t,\cdot)\|_{L^3(F(t))}<\infty
```

**imply** $`h,Q\in C^\infty((0,T])`$ and $`u\in C^\infty(E)`$, where

```math
E=\{(t,x):0<t\le T,\ x\in\Omega\cap\overline{F(t)}\}?
```

Here smoothness includes the fluid side of the moving body interface, and derivatives at $`T`$ are interpreted from the left. This is the literal set $`E`$ in the source theorem: the outer container boundary and the initial time are excluded. Derivatives need not match those of the rigid extension across the body interface.

The critical norm may have any finite size. In particular, no smallness, strong time continuity in $`L^3`$, bounded body acceleration, or fluid-pressure regularity is assumed in addition.

## Application

This asks whether critical velocity measurements can rule out a loss of smoothness in the coupled motion of a rigid object and a surrounding viscous fluid before collision. The body responds dynamically to the fluid stresses rather than following a prescribed path.

## References

1. D. Maity and T. Takahashi, *Regularity of weak solutions of a fluid-rigid body interaction system in a bounded domain under the Prodi-Serrin condition*, Journal of Differential Equations **424** (2025), 726–759. [Published article](https://doi.org/10.1016/j.jde.2025.01.073), [primary author manuscript](https://hal.science/hal-04599986v1/document). Published Remark 1.7 explicitly asks whether Theorem 1.4 remains valid without its critical-norm smallness condition. Definition 1.1 and equations (1.1)–(1.16) give the model and weak class used here.
2. D. Maity and T. Takahashi, *Uniqueness and regularity of weak solutions of a fluid-rigid body interaction system under the Prodi-Serrin condition*, Discrete and Continuous Dynamical Systems **44** (2024), 718–742. [DOI](https://doi.org/10.3934/dcds.2023123). This whole-space rigid-ball result distinguishes critical weak uniqueness from critical regularity, for which a smallness hypothesis remains.

## Status review


**Known cases:** The unrestricted finite-size L-infinity-time L3-space endpoint before body contact is required. Known Serrin cases with q greater than three and small critical norm do not imply it; fixed exterior Oseen theory and small-body limits differ.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The unrestricted finite-size L-infinity-time L3-space endpoint before body contact is required. Known Serrin cases with q greater than three and small critical norm do not imply it; fixed exterior Oseen theory and small-body limits differ.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.jde.2025.01.073); [comparison source 2](https://hal.science/hal-04599986v1/document); [comparison source 3](https://doi.org/10.3934/dcds.2023123). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Theorem 1.3 of the first reference proves the conclusion under $`u\in L^r_tL^q_x`$ with $`2/r+3/q=1`$, $`q>3`$ and finite $`r`$. Theorem 1.4 treats $`L^\infty_tL^3_x`$ with a sufficiently small norm. Published Remark 1.7 separates the unrestricted critical endpoint from those proved cases. The question here concerns regularity before contact; it does not claim uniqueness of continuations through a collision.

Searches on 17 October 2026 have not located a matching resolution or announcement. Independent selected-primary review passed after matching the conclusion to the source’s literal set E. All186cached catalogue pages were compared using six aliases; the returned classical-fluid window concerns a different question.

The exact weak class and result are pinned to the author manuscript. Complete final34page published-body parity remains unchecked.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/fsi-critical-endpoint-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-fsi-critical-endpoint-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/fsi-endpoint-prove2me0130-review.json), [selected primary pages](../FURTHER_problems/_tracking/parallel/continuum/fsi-critical-endpoint-selected-source-pages.json) and [coordinator review](../FURTHER_problems/_tracking/fsi-critical-coordinator-review-2026-10-17.json) preserve coverage and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-760d8203411e01ae**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
