# 410. Quadratic-growth rigidity for the complex Monge–Ampère equation

**Area:** Nonlinear elliptic PDEs / geometric analysis

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

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

4. J. Chu and Y. Liu, [*Quadratic growth rigidity for the complex Monge–Ampère equation*](https://arxiv.org/abs/2610.26016), arXiv:2610.26016v1 (19 October 2026), Theorem 1.2. [Primary manuscript](https://arxiv.org/pdf/2610.26016v1).
5. J. Hu and L. Sheng, [*Interior C² Estimates and a Liouville Theorem for the Complex Monge–Ampère Equation*](https://arxiv.org/abs/2610.28375), arXiv:2610.28375v1 (20 October 2026), Theorem 1.1, Remark 1.2 and Appendix A, Theorem A.1. [Primary manuscript](https://arxiv.org/pdf/2610.28375v1).

## Status review

**Resolution update (3 November 2026):** Solved on the basis of an **unverified announcement**. Chu and Liu’s Theorem 1.2 asserts quadratic rigidity under precisely the displayed two-sided growth assumption, without real convexity, completeness or a prescribed quadratic asymptote. Hu and Sheng independently announce the same smooth conclusion in their Theorem 1.1 and Appendix A, Theorem A.1; the latter explicitly concludes that the potential is a real quadratic polynomial.

[Claimed solution](https://arxiv.org/pdf/2610.26016v1) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-b/410.json). The theorem hypotheses and current announcement were checked. The external proofs have not been independently verified end-to-end here; no Lean verification or human peer review is asserted.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

The September 2026 source records the exact two-sided growth question and distinguishes known results requiring metric completeness. Its new rigidity theorem assumes real convexity, which is stronger than plurisubharmonicity and absent here. Searches through 22 September 2026 located no resolution under the displayed growth condition alone.
