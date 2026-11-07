# AIM 691: target comparison

**Decision:** Solved.

**Established:** An explicit Hermitian metric on $\mathbb P^1\times E$ has a nonanalytic locus of collapsing analytic subvarieties, while the total volume stays bounded below. Equality with the singular set alone is not decided.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 691. Finite-time singularities of the Chern–Ricci flow

**Area:** Complex analysis, geometric analysis and nonlinear PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a connected compact complex manifold of complex dimension $`n\ge2`$, with an arbitrary smooth Hermitian metric $`\omega_0`$. Let $`\omega(t)`$ be its maximal smooth Chern–Ricci flow

```math
\partial_t\omega(t)=-\mathrm{Ric}^{\mathrm{Ch}}(\omega(t)),\qquad \omega(0)=\omega_0,
```


on $`[0,T)`$, where $`0<T<\infty`$. In holomorphic coordinates, $`\mathrm{Ric}^{\mathrm{Ch}}(\omega)=-i\partial\bar\partial\log\det(g)`$ for $`\omega=i g_{j\bar k}\,dz_j\wedge d\bar z_k`$.

Define the singular set $`\Sigma`$ as the complement of points admitting a neighborhood $`U`$ on which $`\omega(t)`$ converges locally smoothly, as $`t\uparrow T`$, to a smooth positive Hermitian metric. For each irreducible closed analytic subvariety $`V\subseteq X`$ of positive complex dimension $`k`$, set

```math
\mathrm{Vol}_t(V)=\frac1{k!}\int_V\omega(t)^k,
\qquad
\Sigma_0=\bigcup_{\mathrm{Vol}_t(V)\to0\text{ as }t\uparrow T} V.
```


Integration is over the regular locus of $`V`$, equivalently against its integration current, and $`V=X`$ is allowed. Must

```math
\Sigma=\Sigma_0,
```


and must this common set be a closed complex analytic subvariety of $`X`$? No Kähler, Gauduchon or mass-bound hypothesis is imposed.
