# AIM 690: target comparison

**Decision:** Solved.

**Established:** Every radial Nevanlinna function on the $\ell^1$ polydisc extends uniquely and Fr\'echet holomorphically to the Hilbert polydisc. The latter is exactly the domain of continuous polynomial evaluation for the logarithmic metric.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 690. A Smirnov function without a Hilbert-domain holomorphic extension

**Area:** Infinite-variable complex analysis and function spaces
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^\infty`$ have normalized product Haar measure $`m`$, and let $`\mathcal P`$ be the analytic polynomials depending on finitely many coordinates. Define $`N_*(\mathbb T^\infty)`$ as the closure of $`\mathcal P`$ for the metric
```math
d_0(f,g)=\int_{\mathbb T^\infty}\log(1+|f-g|)\,dm.
```

For $`q=1,2`$, put $`D_q^\infty=\ell^q(\mathbb C)\cap\mathbb D^\infty`$, with its $`\ell^q`$ topology. Every $`f\in N_*(\mathbb T^\infty)`$ has a canonical holomorphic representative $`F`$ on $`D_1^\infty`$.

Does there exist such an $`f`$ for which there is **no** Fréchet-holomorphic function $`G:D_2^\infty\to\mathbb C`$ satisfying $`G|_{D_1^\infty}=F`$?
