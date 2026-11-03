# 022. The regular-polygon Steklov conjecture

**Area:** Boundary spectral optimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-11-03

## Problem statement

Fix an integer $`n\ge3`$ and $`L>0`$. For a convex planar polygon $`P`$ with at most $`n`$ sides and perimeter $`L`$, let $`\sigma_1(P)`$ be the first positive Steklov eigenvalue, defined weakly by

```math
\Delta u=0\text{ in }P,\qquad\partial_\nu u=\sigma u\text{ on }\partial P.
```

Let $`R_n`$ be the regular $`n`$-gon with perimeter $`L`$. Prove or disprove $`\sigma_1(P)\le\sigma_1(R_n)`$, with equality only for $`P`$ congruent to $`R_n`$.

## Application

Steklov modes describe a membrane with mass concentrated on its boundary and the response encoded by a Dirichlet-to-Neumann operator. The problem optimizes its fundamental boundary mode under manufacturing constraints.

## References

1. Z. Cheng, C. Gui, Y. Hu, Q. Li and R. Yao, [Monotonicity of the first nonzero Steklov eigenvalue of regular N-gon with fixed perimeter](https://arxiv.org/abs/2603.25116), preprint (2026), Conjectures 1.1–1.2.
2. N. Nigam (problem proposer), [Open problems from the miniconference on sharp eigenvalue estimates for partial differential operators](https://publish.illinois.edu/eigenvalues2020/files/2020/04/Open-problems.pdf), April 2020, Open Problem 8.
3. M. J. Colbrook, [*The square maximizes the first Steklov eigenvalue among parallelograms*](../research/solutions/022-parallelogram-steklov/aim022.pdf), 3 November 2026. [TeX source](../research/solutions/022-parallelogram-steklov/aim022.tex), [package and reproduction](../research/solutions/022-parallelogram-steklov/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-spectral-batch/022-review.md).

## Status review

**Known cases:** The existing triangle theorem remains recorded in the [triangle solution package](../research/solutions/022-steklov-triangle/PROOF.md). In addition, the square uniquely maximizes the first positive Steklov eigenvalue among all nondegenerate parallelograms of a fixed perimeter.

**Remaining target:** The regular-polygon comparison and its equality characterization remain open for arbitrary convex polygons with at most $`n`$ sides when $`n\ge4`$, including non-parallelogram quadrilaterals.

**Reviewed result, 2026-11-03:** The square uniquely maximizes the first positive Steklov eigenvalue among parallelograms of a fixed perimeter. The [manuscript](../research/solutions/022-parallelogram-steklov/aim022.pdf) and [individual audit](../research/solution_reviews/2026-11-03-spectral-batch/022-review.md) record the proof, checked references and exact target comparison. Review was performed by Codex (AI).

**Review (2026-10-02):** [Independent Codex AI audit](../research/solution_reviews/2026-10-02-active-prs/022-triangles-review.md) of [PR #20](https://github.com/MColbrook/AIM/pull/20), including fresh certificate reproduction and additional checks. This is not human peer review or proof-assistant verification. The audit records a minor arithmetic-precision documentation correction.

### Previous status review

**Literature check:** Open in cited literature; no later resolution located.

The March 2026 paper explicitly says the extremal conjecture remains open even for triangles. Its theorem compares regular polygons as n varies; it does not compare an arbitrary polygon with a regular one. This provides recent direct status evidence for the precise convex class.

**Search audit:** “Steklov regular polygon conjecture 2025 2026”; “polygonal Weinstock conjecture proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
