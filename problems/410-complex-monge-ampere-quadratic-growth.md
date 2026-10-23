# 410. Quadratic-growth rigidity for the complex Monge–Ampère equation

**Area:** Nonlinear elliptic PDEs / geometric analysis

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-23

## Problem statement

Let $`n\ge2`$ and let $`u\in C^\infty(\mathbb C^n;\mathbb R)`$ be strictly plurisubharmonic, meaning that the Hermitian matrix $`(u_{i\bar j})`$ is positive definite. Use $`\partial_{z_j}=\tfrac12(\partial_{x_j}-i\partial_{y_j})`$. Suppose

```math
\det(u_{i\bar j})=1\quad\text{on }\mathbb C^n,
```

and for some $`C\ge1`$,

```math
C^{-1}(1+|z|^2)\le u(z)\le C(1+|z|^2)\qquad(z\in\mathbb C^n).
```

Must $`u`$ be a polynomial of degree two in the $`2n`$ real coordinates? Neither real convexity nor completeness of the metric $`(u_{i\bar j})`$ is assumed.

## Application

This equation constructs Ricci-flat Kähler metrics and is a central nonlinear elliptic model. The question isolates whether a coarse growth constraint alone controls the geometry, without requiring derivative bounds or a prescribed quadratic asymptote.

## References

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.4. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
2. Y. Wang, *A Liouville Theorem for the Complex Monge–Ampère Equation*, preprint (2013), main theorem assuming a quadratic asymptote with an o(|z|²) error. [arXiv:1303.2403](https://arxiv.org/abs/1303.2403).
3. H. Chen, J. Hu and L. Sheng, *Pogorelov interior estimates and a Liouville theorem for the complex Monge–Ampère equation*, preprint (16 September 2026), §1 discussion of Székelyhidi’s quadratic-growth question and Theorem 1.3. [Full text](https://arxiv.org/html/2609.18265v1).

## Status review

Reviewed 23 October 2026 against the target at [`8729eab`](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/410-complex-monge-ampere-quadratic-growth.md). Claim: affirmative quadratic rigidity under the two-sided growth bound.

[Proof or source](https://arxiv.org/pdf/2610.26016v1) · [Resolution report and AI review](../research/literature_reports/2026-10-23-clopen-aim-410.md). The linked report records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument was read by two AI referees, not by an independent human reviewer, and no peer-reviewed publication is established; the claim awaits independent review.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 source records the exact two-sided growth question and distinguishes known results requiring metric completeness. Its new rigidity theorem assumes real convexity, which is stronger than plurisubharmonicity and absent here. Searches through 22 September 2026 located no resolution under the displayed growth condition alone.
