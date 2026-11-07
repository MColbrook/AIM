# AIM 724: target comparison

**Decision:** Solved.

**Established:** For every fixed $L>2$, the capacity of ambient ball centers with local mass at least $r^L$ tends to the support capacity. This implies the requested iterated limit.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 724. Is polynomial local mass almost necessary for regular orthogonal polynomials?

**Area:** Orthogonal polynomials and logarithmic potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mu`$ be a nonzero finite positive Borel measure on $`\mathbb C`$ with compact support $`S`$ and positive logarithmic capacity $`\mathrm{cap}(S)`$. Let $`p_n(z)=\kappa_n z^n+\cdots`$ be its orthonormal polynomials, normalized by $`\kappa_n>0`$. Assume that $`\mu`$ is regular in the Stahl–Totik sense:

```math
\lim_{n\to\infty}\kappa_n^{1/n}=\frac{1}{\mathrm{cap}(S)}.
```

Write $`B(z,r)=\{w\in\mathbb C:|w-z|<r\}`$. For $`L>0`$ and $`0<r<1`$, put

```math
C_L(r)=\mathrm{cap}\bigl(\{z\in\mathbb C:\mu(B(z,r))\ge r^L\}\bigr),
```

using logarithmic capacity for Borel sets. Must every such measure satisfy

```math
\lim_{L\to\infty}\;\liminf_{r\downarrow0} C_L(r)
=\mathrm{cap}(S)?
```

This is the explicit question in the notes to Chapter 4 of [1], printed p. 238. The order of the limits is part of the target. It does not require a single finite $`L`$ for which the full limit as $`r\downarrow0`$ equals $`\mathrm{cap}(S)`$. No absolute continuity, interval support, or Dirichlet regularity of $`S`$ is assumed.
