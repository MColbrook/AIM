# 739. A bounded-domain nonlocal-to-local limit for degenerate Cahn–Hilliard diffusion

**Area:** Diffusion and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\in\{2,3\}`$ and let $`\Omega\subset\mathbb R^d`$ be any bounded connected $`C^\infty`$ domain; convexity is not assumed. Fix a nonnegative radial $`\omega\in C_c^\infty(B_1(0))`$, positive near the origin, with $`\int\omega=1`$. Set
```math
\omega_\varepsilon(z)=\varepsilon^{-d}\omega(z/\varepsilon),\qquad
\kappa=\frac1{2d}\int_{\mathbb R^d}|z|^2\omega(z)\,dz,
```
```math
B_\varepsilon v(x)=\varepsilon^{-2}\int_\Omega\omega_\varepsilon(x-y)(v(x)-v(y))\,dy,
\qquad F(s)=s^2(s-1)^2.
```
This is a regional operator: $`v`$ is not extended outside $`\Omega`$. Fix $`u^0\in C^\infty(\overline\Omega)`$ with $`u^0\ge0`$ and $`u^0\not\equiv0`$. Zeros of $`u^0`$ are allowed.

**Question.** Can one choose, for every sufficiently small $`\varepsilon>0`$, a global nonnegative energy weak solution of
```math
\partial_tu_\varepsilon=\mathrm{div}(u_\varepsilon\nabla\mu_\varepsilon),\qquad
\mu_\varepsilon=B_\varepsilon u_\varepsilon+F'(u_\varepsilon),\qquad
\nu\cdot u_\varepsilon\nabla\mu_\varepsilon=0,
\qquad u_\varepsilon(0)=u^0,
```
so that, for some sequence $`\varepsilon_j\downarrow0`$ and one global nonnegative weak solution $`u`$, 
```math
u_{\varepsilon_j}\longrightarrow u\quad\text{strongly in }L^2(0,T;H^1(\Omega))
\quad\text{for every finite }T>0,
```
where
```math
\partial_tu=\mathrm{div}(u\nabla\mu),\qquad
\mu=-\kappa\Delta u+F'(u),\qquad
\partial_\nu u=0,\quad u\partial_\nu\mu=0,\qquad u(0)=u^0?
```
Here $`\nu`$ is the exterior unit normal. The assertion asks for a suitable choice of nonlocal weak solutions; it does not quantify over every weak family.

## Meaning of the nonlocal energy weak solution

The following requirements apply on every finite time interval. Require
```math
u_\varepsilon\in L^\infty(0,T;L^4(\Omega))\cap L^2(0,T;H^1(\Omega)),
\qquad u_\varepsilon\nabla u_\varepsilon\in L^2((0,T)\times\Omega).
```
Define
```math
c_\varepsilon(x)=\varepsilon^{-2}\int_\Omega\omega_\varepsilon(x-y)\,dy,
```
```math
J_\varepsilon=u_\varepsilon\Big[(c_\varepsilon+F''(u_\varepsilon))\nabla u_\varepsilon
+u_\varepsilon\nabla c_\varepsilon
-\varepsilon^{-2}\int_\Omega\nabla\omega_\varepsilon(x-y)u_\varepsilon(y)\,dy\Big].
```
These products are defined as integrable functions. Require $`J_\varepsilon=\sqrt{u_\varepsilon}\,g_\varepsilon`$ for some $`g_\varepsilon\in L^2((0,T)\times\Omega;\mathbb R^d)`$ that is zero on $`\{u_\varepsilon=0\}`$. Equivalently, the weighted flux $`J_\varepsilon/\sqrt{u_\varepsilon}`$ is square-integrable, with the zero convention at vacuum. Then $`J_\varepsilon\in L^2(0,T;L^{8/5}(\Omega))`$.

For every smooth $`\varphi`$ on $`[0,T]\times\overline\Omega`$ vanishing near $`T`$, without any spatial boundary restriction, require
```math
\int_0^T\!\int_\Omega u_\varepsilon\partial_t\varphi
+\int_\Omega u^0\varphi(0)
=\int_0^T\!\int_\Omega J_\varepsilon\cdot\nabla\varphi.
```
This identity gives the no-flux boundary condition, conservation of $`\int_\Omega u_\varepsilon`$, and $`\partial_tu_\varepsilon\in L^2(0,T;(W^{1,8/3}(\Omega))')`$. Use its continuous dual-space representative for the initial trace. Require, for almost every $`t>0`$,
```math
E_\varepsilon(u_\varepsilon(t))+\int_0^t\!\int_\Omega|g_\varepsilon|^2
\le E_\varepsilon(u^0),
```
```math
E_\varepsilon(v)=\int_\Omega F(v)
+\frac1{4\varepsilon^2}\int_{\Omega\times\Omega}\omega_\varepsilon(x-y)|v(x)-v(y)|^2\,dx\,dy.
```
No $`\varepsilon`$-uniform entropy or gradient estimate is included in these requirements. The variable coefficient $`c_\varepsilon`$ and its derivative must be retained near the boundary.

## Meaning of the limiting weak solution

For every finite $`T`$, require
```math
u\in L^\infty(0,T;H^1(\Omega)\cap L^4(\Omega))\cap L^2(0,T;H^2(\Omega)),
\quad u\nabla u\in L^2((0,T)\times\Omega),
\quad \partial_tu\in L^2(0,T;(W^{1,8/3}(\Omega))').
```
Require the initial dual-space trace $`u^0`$ and $`\partial_\nu u=0`$ in the Sobolev trace sense for almost every time. For every smooth $`\varphi`$ vanishing near $`T`$ and satisfying $`\partial_\nu\varphi=0`$, require
```math
\int_0^T\!\int_\Omega u\partial_t\varphi+\int_\Omega u^0\varphi(0)
=\kappa\int_0^T\!\int_\Omega
\big[\Delta u\nabla u\cdot\nabla\varphi+u\Delta u\Delta\varphi\big]
+\int_0^T\!\int_\Omega uF''(u)\nabla u\cdot\nabla\varphi.
```
This encodes the second no-flux condition without presupposing third derivatives of $`u`$ or a boundary trace of $`\nabla\mu`$.

## Application

Finite-range interaction models approximate interfacial energies in phase separation and cell adhesion. This question asks whether the local fourth-order model remains the correct limit near impermeable physical walls, including for data with vacuum.

## Status review


**Known cases:** The exact regional bounded-domain operator, vacuum-allowing linear mobility and strong L2-time H1-space limit are essential. Constant mobility, periodic geometry, different dynamic boundaries and stochastic regular-potential results do not supply this statement.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact regional bounded-domain operator, vacuum-allowing linear mobility and strong L2-time H1-space limit are essential. Constant mobility, periodic geometry, different dynamic boundaries and stochastic regular-potential results do not supply this statement.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.jde.2023.03.057); [comparison source 2](https://arxiv.org/pdf/2208.08955v3); [comparison source 3](https://doi.org/10.1016/j.jde.2024.05.022); [comparison source 4](https://doi.org/10.1016/j.na.2025.113870); [comparison source 5](https://arxiv.org/abs/2407.03844). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves strong $`L^2H^1`$ convergence on a flat torus and explicitly asks how to recover the extra Neumann condition on a bounded domain. Its periodic entropy argument does not directly apply to the regional operator. Abels–Hurm prove bounded-domain operator convergence and convergence for **constant mobility**, with a given sufficiently regular local solution. Elbar–Skrzeczkowski's later Flory–Huggins result retains periodic geometry. Neither comparison establishes the present degenerate mobility with vacuum and physical walls.

The coefficient $`\kappa`$ is defined directly by the second moment to avoid a normalization inconsistency between the earlier source's displayed moment convention and its displayed local coefficient. The published 2023 article's complete body has not been accessed; the complete 33-page author version has been reviewed. Checked 17 October 2026. Independent selected-primary review checked the regional flux, its boundary correction, the second-moment constant, the energy weak class, the existence-selection quantifier and both limiting boundary conditions. No missing uniform entropy or gradient estimate is inserted as an assumption.

Dated current searches found no matching complete result or announcement. All-status AIM/OpenAI and FURTHER comparisons found no equivalent target: AIM 480 concerns weak uniqueness, AIM 481 concerns whole-space finite propagation, and AIM 469 concerns a different second-order cross-diffusion limit. The fresh Prove2Me snapshot reconciles 4,629 listings on 186 pages; the seven recorded target aliases return no matching context. This is a public listing check, not a review of every mission proof.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/bounded-degenerate-ch-limit-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-bounded-degenerate-ch-review.json) and [fresh catalogue receipt](../FURTHER_problems/_tracking/bounded-ch-fresh-catalogue-review.json) record the exact extents and access limits. The 2024 constant-mobility comparison was read in full by the source reviewer; other status comparisons have the selected extents recorded there. Negative searches remain bounded evidence.

## References

1. C. Elbar and J. Skrzeczkowski, *Degenerate Cahn–Hilliard equation: From nonlocal to local*, Journal of Differential Equations **364** (2023), 576–611. [DOI](https://doi.org/10.1016/j.jde.2023.03.057); [author version v3](https://arxiv.org/pdf/2208.08955v3), §1.4, PDF pp. 8–9.
2. H. Abels and C. Hurm, *Strong nonlocal-to-local convergence of the Cahn–Hilliard equation and its operator*, Journal of Differential Equations **402** (2024), 593–624. [DOI](https://doi.org/10.1016/j.jde.2024.05.022), Theorems 4.1 and 5.1.
3. C. Elbar and J. Skrzeczkowski, *Nonlocal-to-local convergence of the Cahn–Hilliard equation with Flory–Huggins potential and degenerate mobility*, Nonlinear Analysis **261** (2025), 113870. [DOI](https://doi.org/10.1016/j.na.2025.113870); [author version](https://arxiv.org/abs/2407.03844), Theorem 1.2.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b04d757e7a4c4057**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
