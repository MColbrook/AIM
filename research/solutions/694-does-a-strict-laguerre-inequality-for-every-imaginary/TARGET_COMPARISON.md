# AIM 694: target comparison

**Decision:** Partially resolved.

**Established:** The strict translated Laguerre criterion is proved when the Gaussian coefficient is positive.

**Scope / remaining target:** The case of Gaussian coefficient zero remains unresolved here.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 694. Does a strict Laguerre inequality for every imaginary translate force real zeros?

**Area:** Entire functions and zero distribution
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`f`$ be a real entire function in the class $`S(A)`$ of Csordas and Escassut for some finite $`A\geq0`$. Thus $`f`$ has their genus-at-most-one canonical-product form, possibly multiplied by $`e^{-az^2+bz}`$ with $`a\geq0`$ and $`b\in\mathbb R`$, and all its zeros lie in the horizontal strip $`|\mathrm{Im}z|\leq A`$. For real $`\mu`$, put

```math
f_\mu(x)=f(x+i\mu)+f(x-i\mu),\qquad
L[g]\,(x)=(g'(x))^2-g(x)g''(x).
```


If $`L[f_\mu]\,(x)>0`$ for **every** real $`x`$ and **every nonzero** real $`\mu`$, must all zeros of $`f`$ be real, equivalently must $`f`$ belong to the Laguerre–Pólya class? This is Conjecture 3.5 of the source. The precise canonical-product and convergence assumptions are those of its Definition 1.1; the horizontal-strip condition alone is not the complete definition of $`S(A)`$.
