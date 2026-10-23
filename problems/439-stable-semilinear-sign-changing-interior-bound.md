# 439. Interior bounds for stable elliptic states with sign-changing reaction laws

**Area:** Semilinear elliptic PDEs and reaction equilibria

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-23
## Problem statement

For each $`d\in\{6,7,8,9\}`$, does there exist $`C_d<\infty`$ such that, for every $`f\in C^1(\mathbb R)`$ and every $`u\in C^2(B_1)`$ satisfying

```math
-\Delta u=f(u),\qquad \int_{B_1} f'(u)\varphi^2\le\int_{B_1}|\nabla\varphi|^2\quad(\varphi\in C_c^\infty(B_1)),
```

one has

```math
\|u\|_{L^\infty(B_{1/2})}\le C_d\|u\|_{W^{1,2}(B_1)}?
```

Here $`B_r\subset\mathbb R^d`$ is a centered ball, stability means the displayed nonnegative second-variation inequality, and no sign assumption is imposed on $`f`$ or $`u`$. The constant must be independent of the reaction law.

## Application

Stable stationary reaction-diffusion patterns can have both production and depletion regimes. A uniform estimate would rule out concentration in dimensions below ten without requiring the reaction to have one sign.

## References

1. X. Cabré, [Stable solutions to reaction-diffusion elliptic problems](https://arxiv.org/abs/2603.03161), lecture survey (2026), §3.5.4.
2. F. Peng, Y. R.-Y. Zhang and Y. Zhou, [Interior Hölder regularity for stable solutions to semilinear elliptic equations up to dimension 5](https://arxiv.org/abs/2204.06345), preprint (2022), main interior estimate and discussion of dimensions 6–9.

## Status review

Reviewed 23 October 2026 against the target at [`8729eab`](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/439-stable-semilinear-sign-changing-interior-bound.md). Claim: affirmative interior bound for stable solutions in dimensions 6–9.

[Proof or source](https://arxiv.org/pdf/2610.21641v1) · [Resolution report and AI review](../research/literature_reports/2026-10-23-clopen-aim-439.md). The linked report records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument was read by two AI referees, not by an independent human reviewer, and no peer-reviewed publication is established; the claim awaits independent review.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The survey identifies the missing interior boundedness estimate in dimensions 6–9 when f may change sign. The Peng–Zhang–Zhou theorem handles dimensions at most five with a W1,2 norm. Review-date searches for sign-changing stable solutions and later higher-dimensional interior estimates found no proof of the displayed universal bound. Entire-space Liouville theorems under special assumptions on the zeros of f have different hypotheses.
