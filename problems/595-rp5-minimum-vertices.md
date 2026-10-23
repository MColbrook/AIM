# 595. The minimum vertex number of a triangulation of real projective 5-space

**Area:** Computational topology and triangulated manifolds

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-23

## Problem statement

A triangulation of $`\mathbb{RP}^5`$ means a finite simplicial complex whose geometric realization is homeomorphic to real projective $`5`$-space. Let

```math
\mu_5=\min\{f_0(K): |K|\cong\mathbb{RP}^5\},
```

where $`f_0(K)`$ is the number of vertices. Prove or disprove that

```math
\mu_5=24.
```

The minimum is taken over all simplicial triangulations, without a symmetry or polytopal-realizability requirement.

## Application

Minimal triangulations provide small combinatorial models for topological computation and test the strength of lower bounds derived from cohomology. Resolving this case would extend the dimensions in which the exact minimum vertex number of real projective space is known.

## References

1. D. Guyer, S. Steinerberger and Y. Yang, [An Efficient Triangulation of $`\mathbb{RP}^5`$](https://doi.org/10.1007/s00454-026-00882-2), *Discrete & Computational Geometry* (2026), Conjecture 3.1. [arXiv:2603.07808v2](https://arxiv.org/abs/2603.07808), 20 September 2026.
2. F. Frick, K. Hosseini, E. Myzelev, A. Narnapatti and A. Vasileuski, [Superpolynomial lower bounds for vertex numbers of real projective space triangulations via a topological Figiel–Lindenstrauss–Milman theorem](https://arxiv.org/abs/2609.10402), arXiv:2609.10402 (2026).

## Status review

Reviewed 23 October 2026 against the target at [`8729eab`](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/595-rp5-minimum-vertices.md). Claim: affirmative, the minimum is 24 vertices.

[Proof or source](https://arxiv.org/pdf/2610.25171v1) · [Resolution report and AI review](../research/literature_reports/2026-10-23-clopen-aim-595.md). The linked report records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument was read by two AI referees, not by an independent human reviewer, and no peer-reviewed publication is established; the claim awaits independent review.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The source supplies a $`24`$-vertex example; the classical lower bound gives $`22`$. Its 20 September 2026 revision retains the minimality conjecture. The new asymptotic lower bound [2] concerns growth with dimension and does not give the required $`24`$-vertex lower bound in dimension five. The recent $`44`$-vertex construction for $`\mathbb{RP}^6`$ answers a different question and is not being admitted as open. Current searches found no matching resolution or duplicate.
