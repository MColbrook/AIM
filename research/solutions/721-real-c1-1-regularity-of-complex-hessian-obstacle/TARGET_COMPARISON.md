# AIM 721: target comparison

**Decision:** Solved.

**Established:** The complex $m$-Hessian obstacle envelope is locally $C^{1,1}$ in all real coordinates for every $1\le m\le n$, under the stated strict defining-function assumption. The penalized Bellman estimates are uniform in both approximation parameters.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 721. Real C¹,¹ regularity of complex Hessian obstacle envelopes

**Area:** Complex analysis, potential theory and nonlinear obstacle problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\Subset\mathbb C^n`$ be a bounded smooth strongly $`m`$-pseudoconvex domain, where $`2\le m\le n`$. Thus $`\Omega`$ admits a smooth defining function $`\rho`$ that is strictly $`m`$-subharmonic near $`\overline\Omega`$ and satisfies $`|\nabla\rho|>0`$ on its boundary. For real $`h\in C^2(\overline\Omega)`$, define

```math
P_{m,\Omega}h=\left(\sup\{v\in\mathrm{SH}_m(\Omega):v\le h\text{ on }\Omega\}\right)^*.
```

Here the star denotes upper semicontinuous regularization, and $`\mathrm{SH}_m`$ is the standard class of $`m`$-subharmonic functions. For smooth functions, this means that the first $`m`$ elementary symmetric functions of the eigenvalues of the complex Hessian are nonnegative.

Must $`P_{m,\Omega}h`$ have locally Lipschitz first derivatives with respect to all real coordinates, that is,

```math
P_{m,\Omega}h\in C^{1,1}_{\mathrm{loc}}(\Omega)?
```
