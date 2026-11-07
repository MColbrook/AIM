# AIM 707: target comparison

**Decision:** Solved.

**Established:** An explicit Gauduchon Chern--Ricci flow on a non-K\"ahler elliptic bundle converges smoothly after normalization while its normalized full Chern curvature grows at least as $c\sqrt t$.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 707. Smooth Chern–Ricci collapse on non-Kähler elliptic bundles

**Area:** Complex geometry and geometric partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a connected compact non-Kähler complex surface with a holomorphic elliptic bundle $`f:M\to\Sigma`$, where $`\Sigma`$ is a compact Riemann surface of genus at least two. Here a bundle is locally biholomorphic over the base to $`E\times U`$ for a fixed elliptic curve $`E`$. Let $`\omega_0`$ be an arbitrary smooth positive Gauduchon metric, so $`\partial\bar\partial\omega_0=0`$.

Let $`\omega(t)`$ be the unnormalized Chern–Ricci flow

```math
\partial_t\omega=-\mathrm{Ric}^{\mathrm{Ch}}(\omega),\qquad \omega(0)=\omega_0,
\qquad \mathrm{Ric}^{\mathrm{Ch}}(\omega)=-i\partial\bar\partial\log\det(g).
```

This flow exists for all $`t\ge0`$ in the stated setting. Write $`\omega_\Sigma`$ for the unique Kähler metric on $`\Sigma`$ with $`\mathrm{Ric}(\omega_\Sigma)=-\omega_\Sigma`$. Is it true that

```math
\frac{\omega(t)}t\longrightarrow f^*\omega_\Sigma
\quad\text{in }C^\infty(M),
\qquad
\sup_M\left|\mathrm{Rm}^{\mathrm{Ch}}\!\left(\frac{\omega(t)}t\right)\right|_{\omega(t)/t}\le C
\quad(t\ge t_0)
```

for some finite $`C`$ and $`t_0>0`$? The constants may depend on the bundle and the entire initial metric. The curvature is the full curvature tensor of the Chern connection, measured in the evolving normalized metric. Smooth tensor convergence is measured in any fixed smooth background metric; the limit is semipositive and vanishes in the fibre directions.

The requested conclusions are global smooth convergence and bounded normalized curvature. Uniform convergence and Gromov–Hausdorff convergence are already known. Smooth convergence restricted to individual fibres does not supply all transverse and mixed derivatives. No restriction of $`\omega_0`$ to a special $`\partial\bar\partial`$ class is imposed.
