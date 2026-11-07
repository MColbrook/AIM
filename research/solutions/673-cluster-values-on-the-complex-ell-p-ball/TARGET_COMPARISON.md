# AIM 673: target comparison

**Decision:** Solved.

**Established:** Every value of a character over an interior point of the complex $\ell^p$ ball is a weak cluster value in the same ball, for $1<p<\infty$. The exact tail-radius estimate and origin approximation are proved directly.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 673. Cluster values on the complex $`\ell_p`$ ball

**Area:** Complex analysis and potential theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`1<p<\infty`$, $`p\ne2`$, and let $`B`$ be the open unit ball of $`X=\ell_p(\mathbb N;\mathbb C)`$. Let $`A_u(B)`$ be the Banach algebra of holomorphic functions on $`B`$ that are uniformly continuous in the norm of $`X`$, with the supremum norm. Its spectrum $`M`$ consists of nonzero continuous multiplicative linear functionals. For $`z\in B`$, define

```math
M_z=\{\varphi\in M:\varphi(x^*)=x^*(z)\text{ for every }x^*\in X^*\}.
```

For $`f\in A_u(B)`$ let $`Cl_B(f,z)`$ consist of all limits of $`f(x_\alpha)`$ along nets $`x_\alpha\in B`$ converging weakly to $`z`$. Is it true that, for every $`f\in A_u(B)`$ and every $`z\in B`$ with $`z\ne0`$,

```math
Cl_B(f,z)=\{\varphi(f):\varphi\in M_z\}?
```

The inclusion from left to right always holds. Equality is known at $`z=0`$, and for all points when $`p=2`$. The unit-sphere case is also known; the question concerns nonzero interior points for the non-Hilbert spaces.
