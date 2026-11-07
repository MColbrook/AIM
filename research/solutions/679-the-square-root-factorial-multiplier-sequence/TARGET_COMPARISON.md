# AIM 679: target comparison

**Decision:** Solved.

**Established:** $\{\sqrt{k}/k!\}_{k\ge0}$ is a multiplier sequence; its exponential generating function has simple negative nonzero zeros with explicit quadratic localization.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 679. The square-root factorial multiplier sequence

**Area:** Polynomial zero preservation and entire functions
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

For every real polynomial $`p(x)=\sum_{k=0}^m a_kx^k`$ with only real zeros, must

```math
Tp(x)=\sum_{k=0}^m\frac{\sqrt{k}}{k!}a_kx^k
```

have only real zeros or be identically zero? The constant coefficient is annihilated: $`\gamma_0=0`$, and $`\gamma_k=\sqrt{k}/k!`$ for $`k\ge1`$.

Equivalently, does the entire function

```math
\Phi(z)=\sum_{k=0}^{\infty}\frac{\sqrt{k}}{(k!)^2}z^k
```

belong to the Laguerre–Pólya class with nonnegative coefficients, meaning that it is a locally uniform limit of real polynomials whose zeros are all nonpositive? Another equivalent formulation asks whether every Jensen polynomial

```math
J_n(x)=\sum_{k=0}^n\binom nk\frac{\sqrt{k}}{k!}x^k,\qquad n\ge1,
```

has only real zeros. Zeros at the origin are allowed. These are equivalent formulations of one question.
