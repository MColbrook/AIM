# AIM 682: target comparison

**Decision:** Partially resolved.

**Established:** The Le Roy equivalence and all degrees at most five are proved.

**Scope / remaining target:** Arbitrary noninteger exponents at least two in degrees six and above remain unresolved here.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 682. Real-rootedness of real powers of binomial coefficients

**Area:** Polynomial zeros and coefficient transformations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`n\ge1`$ and real $`\gamma\ge2`$, does

```math
B_{n,\gamma}(x)=\sum_{k=0}^n\binom nk^{\gamma}x^k
```

have only real zeros? Repeated zeros are allowed. The constant and leading coefficients are one, so any real zeros are strictly negative. Powers act on the ordinary coefficients of $`(1+x)^n`$.

The target concerns these exact finite polynomials for every degree. It does not ask for a limiting zero distribution or for preservation on every real-rooted input polynomial.
