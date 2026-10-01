# 457. Finite-density time sampling of an infinite observation window

**Area:** Operator evolution and stable dynamical sampling

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`\mathcal H`$ be a separable complex Hilbert space, let $`A`$ be bounded and normal, and let $`(g_j)_{j\in J}`$ be a countable Bessel family: $`\sum_j|\langle f,g_j\rangle|^2\le B_0\|f\|^2`$. Define $`A^t`$ by spectral calculus using $`z^t=|z|^te^{it\arg z}`$, $`\arg z\in(-\pi,\pi]`$, with $`0^t=0`$ for $`t>0`$ and $`A^0=I`$. Suppose

```math
m\|f\|^2\le\sum_j\int_0^\infty|\langle f,A^tg_j\rangle|^2\,dt\le M\|f\|^2\qquad(f\in\mathcal H)
```

for some $`0<m\le M<\infty`$. Must there be a locally finite set $`T\subset[0,\infty)`$ with

```math
D^+(T)=\limsup_{L\to\infty}\sup_{a\ge0}\frac{\#(T\cap[a,a+L])}{L}<\infty
```

and constants $`0<m_T\le M_T<\infty`$ such that

```math
m_T\|f\|^2\le\sum_{t\in T}\sum_j|\langle f,A^tg_j\rangle|^2\le M_T\|f\|^2\qquad(f\in\mathcal H)?
```

No time-dependent weights may be inserted in the discrete sum.

## Application

The measurements represent fixed sensors observing a linearly evolving field. The question asks whether stable continuous observation for arbitrarily long times can always be implemented with a finite average temporal sampling rate.

## References

1. A. Aldroubi, L. X. Huang and A. Petrosyan, [Frames induced by the action of continuous powers of an operator](https://doi.org/10.1016/j.jmaa.2019.05.066), *Journal of Mathematical Analysis and Applications* **478** (2019), 1059–1084, time-discretization theorems; [preprint](https://arxiv.org/abs/1801.10103).
2. A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, [Dynamical Sampling: A Survey](https://doi.org/10.1007/s44007-026-00215-y), *La Matematica* **5** (2026), article 37, Theorem 2.12, Open Problem 1, and §5.2(B).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The May 2026 survey explicitly asks for a discrete time set of finite upper Beurling density on the infinite window. Finite-window sampling and infinite-window results under exponential stability do not settle this general case. Searches through the review date located no later resolution. The question concerns infinite-dimensional sampling stability, rather than a finite matrix algorithm.
