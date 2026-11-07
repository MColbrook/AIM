# AIM 728: target comparison

**Decision:** Solved.

**Established:** Continuous roots of a $C^{n-1,1}$ polynomial curve have derivative in weak $L^{n/(n-1)}$, with a coefficient bound.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 728. Do continuous polynomial roots have weak endpoint derivative regularity?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq3`$, let $`I=(a,b)`$ be a bounded interval, and let

```math
P_t(z)=z^n+a_1(t)z^{n-1}+\cdots+a_n(t)
```


be a monic complex polynomial whose coefficients belong to $`C^{n-1,1}([a,b];\mathbb C)`$. For **every** continuous choice of a root $`\lambda:I\to\mathbb C`$, is

```math
\lambda'\in L^{n/(n-1),\infty}(I),\qquad
\sup_{s>0}s\,|\{t\in I:|\lambda'(t)|>s\}|^{(n-1)/n}<\infty?
```


The derivative exists almost everywhere by the known absolute-continuity theorem [2, Theorem 1]. This is the weak-Lebesgue endpoint question stated by Ghisi and Gobbino [1, §4] and again by Parusiński and Rainer [2, Open Problem 2]. The latter also ask for an explicit bound in terms of the coefficients and interval.

The distinction between **weak** and ordinary $`L^{n/(n-1)}`$ is essential: $`P_t(z)=z^n-t`$ has a root with derivative proportional to $`|t|^{1/n-1}`$, which misses ordinary endpoint integrability but has the critical weak-space scaling. The known theorem gives $`\lambda'\in L^q(I)`$ for every $`q<n/(n-1)`$ [2]; those separate bounds do not imply the weak endpoint.
