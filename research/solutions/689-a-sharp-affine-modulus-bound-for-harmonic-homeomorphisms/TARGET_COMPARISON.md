# AIM 689: target comparison

**Decision:** Solved.

**Established:** A small explicit harmonic perturbation of the critical circular-annulus map violates the proposed bound even after optimizing over all real affine transformations.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 689. A sharp affine-modulus bound for harmonic homeomorphisms

**Area:** Complex analysis and geometric function theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega,\Omega^*\subset\mathbb C`$ be nondegenerate doubly connected domains: each is connected and open, and each of the two components of its complement in the Riemann sphere contains more than one point. Define
```math
\mathrm{Mod}(\Omega)=\log(R/r)
```

when $`\Omega`$ is conformally equivalent to $`\{z:r<|z|<R\}`$, where $`0<r<R<\infty`$. Define its affine modulus by
```math
\mathrm{Mod}_{\rm aff}(\Omega^*)
=\sup_{\phi}\mathrm{Mod}(\phi(\Omega^*)),
\qquad \phi(z)=az+b\overline z+c,\quad |a|^2-|b|^2\ne0.
```

The supremum ranges over all invertible real affine maps and may be infinite.

If a harmonic homeomorphism $`h:\Omega\to\Omega^*`$ exists, must
```math
\mathrm{Mod}_{\rm aff}(\Omega^*)
\ge \log\cosh\bigl(\mathrm{Mod}(\Omega)\bigr)
```

hold? Here harmonic means that both real coordinate functions of $`h`$ are harmonic.

No boundary smoothness, boundedness, finite energy, prescribed boundary correspondence, symmetry or orientation is assumed. This asks for a universal necessary condition. It is one family across all such domain pairs, including the circular-annulus case.
