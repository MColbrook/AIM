# 571. Counting half-integral polygons with collinear interior lattice points

**Area:** Discrete geometry and lattice-point enumeration

**Status:** ✅ SOLVED

**Last checked:** 2026-10-21

## Problem statement

A half-integral polygon is a two-dimensional convex polygon $`P\subset\mathbb R^2`$ whose vertices belong to $`\tfrac12\mathbb Z^2`$. Integral polygons are included. Two polygons are considered equivalent when $`P'=UP+b`$ for some $`U\in\mathop{\mathrm{GL}}\nolimits_2(\mathbb Z)`$ and $`b\in\mathbb Z^2`$.

For each integer $`i\ge3`$, let $`N(i)`$ be the number of these equivalence classes for which $`P`$ has exactly $`i`$ interior lattice points and all of those points lie on one line. Prove or disprove that

```math
N(i)=\frac{i+1}{1260}\left(512i^6+12928i^5+137740i^4+685145i^3+1582743i^2+1665222i+710640\right)
```

for every $`i\ge3`$.

## Application

Exact enumeration supplies benchmark collections for algorithms on rational polytopes and for classifications of the toric geometric objects encoded by polygons. The conjecture would replace enumeration of billions of examples by a closed formula for this family.

## References

1. M. Bohnert and J. Springer, [Classifying Rational Polygons with Small Denominator and Few Interior Lattice Points](https://doi.org/10.1007/s00454-026-00822-0), *Discrete & Computational Geometry* **76** (2026), 1238–1265, Section 2 and Conjecture 3.7. [arXiv:2410.17244](https://arxiv.org/abs/2410.17244).
2. J. Springer and M. Bohnert, [Half-integral polygons with few interior lattice points](https://doi.org/10.5281/zenodo.13928298), computational dataset (2024).
3. J. Springer, [RationalPolygons.jl](https://github.com/justus-springer/RationalPolygons.jl), reference implementation of rational-polygon classification algorithms.

## Status review

**Resolution reviewed 2026-10-21:** Kaiwen Jin's [manuscript](../research/solutions/571-half-integral-collinear-count/paper/manuscript.pdf), originally submitted in [PR 122](https://github.com/MColbrook/AIM/pull/122), establishes the displayed formula for every requested interior-point count. The unchanged original proof and [PR 176 replay supplement](https://github.com/MColbrook/AIM/pull/176) received a [new proof and supplement audit](../research/solution_reviews/2026-10-21-active-prs/176-proof-review.md).

The maintainer review independently recomputed all 608 distinct complete Normaliz rational series, covering all 618 cell members, with zero reused cached results and zero failures. All full rational functions and original gradings match; reaggregation verifies all four action sums, Burnside's identity and the polynomial identity. The [acceptance review](../research/solution_reviews/2026-10-21-active-prs/176-review.md), [execution summary](../research/solution_reviews/2026-10-21-active-prs/571-independent-replay-summary.json) and [complete execution bundle](../research/solution_reviews/2026-10-21-active-prs/571-independent-replay-bundle.json) preserve the scope and receipts. This completes the gate left open by the [15 October review](../research/solution_reviews/2026-10-15-active-prs/571-review.md).

**Literature check:** No earlier matching all-parameter resolution was found on 21 October 2026. Bohnert–Springer [1] states the formula as Conjecture 3.7; its finite verification range and related finite classifications are distinguished from this complete identity. Integral polygons remain included, and equivalence continues to use integer translations.

The result retains its disclosed reliance on trusted exact Normaliz enumeration. It is not a second enumeration algorithm, an independently checked simplicial-decomposition certificate, human peer review or Lean verification.
