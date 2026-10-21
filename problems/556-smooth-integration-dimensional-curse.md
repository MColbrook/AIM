# 556. Does integration of uniformly derivative-bounded analytic functions suffer the dimensional curse?

**Area:** Numerical integration and information-based complexity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-21

## Problem statement

For each $`d\ge1`$, define

```math
F_d=\{f\in C^\infty([0,1]^d):\|D^\alpha f\|_\infty\le1\text{ for every }\alpha\in\mathbb N_0^d\},\qquad
I_d(f)=\int_{[0,1]^d}f(x)\,dx.
```

The derivative condition includes $`\alpha=0`$ and every mixed derivative, with the same bound one at all orders.

Let $`n(\varepsilon,d)`$ be the smallest number of exact function evaluations needed by a deterministic algorithm to approximate $`I_d(f)`$ with absolute error at most $`\varepsilon`$ for every $`f\in F_d`$. Sampling may be adaptive and reconstruction may be nonlinear; there is no restriction to positive quadrature weights.

Does this integration problem suffer from the curse of dimensionality? Specifically, do there exist $`\varepsilon_0\in(0,1)`$, $`c>0`$ and $`\rho>1`$ such that

```math
n(\varepsilon_0,d)\ge c\rho^d
```

for infinitely many dimensions $`d`$?

## Application

This problem tests whether uniformly controlling derivatives of every order is enough to prevent exponential sampling cost for high-dimensional integration. It would clarify what analytic regularity alone can guarantee before extra structure or randomness is imposed.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 8.1, equation (8.5) and the discussion following Proposition 8.3.
2. E. Novak and F. Pillichshammer, [Intractability results for integration in tensor product spaces](https://arxiv.org/abs/2404.17163), arXiv:2404.17163. Section 5.2 compares related classes of infinitely smooth functions.

## Status review

**Existing solution identified 2026-10-21:** [Esra Sengelen Sevim's paper](https://doi.org/10.1016/j.jco.2026.102074), Theorem 1.1, resolves the full stated integration question. The problem remains **Solved**.

The earlier DOI record predates [PR 83](https://github.com/MColbrook/AIM/pull/83). The [priority and scope review](../research/solution_reviews/2026-10-21-yui-prior-art/556-prior-solution.md) records the exact target match and dates. The later contributor manuscript is removed and its package entry point is now an [attribution note](../research/solutions/556-uniform-derivative-integration/README.md). The 13 October AI audit is retained as history and superseded for attribution.
