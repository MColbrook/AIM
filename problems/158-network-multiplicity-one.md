# 158. Multiplicity one at planar network singularities

**Area:** Grain-boundary evolution

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Let $`\Gamma(t)`$ be a smooth embedded finite network in a bounded smooth strictly convex planar domain. Its interior vertices are triple junctions with $`120^\circ`$ angles, its boundary endpoints are fixed, and each edge moves with normal velocity equal to its curvature. Let $`T<\infty`$ be its first singular time and $`x_0`$ an interior singular point.

Must every self-similarly shrinking limit obtained from the parabolic rescalings

```math
\Gamma_j(s)=\lambda_j\bigl(\Gamma(T+s/\lambda_j^2)-x_0\bigr),\qquad\lambda_j\to\infty,\quad s<0,
```

be embedded and have multiplicity one? Multiplicity counts how many rescaled arcs converge to the same limiting arc; it is retained by taking limits of the associated arclength varifolds.

## Application

Multiple hidden sheets at a collapsing grain boundary obstruct a geometric rule for continuing the evolution after a singular event.

## References

1. Carlo Mantegazza, Matteo Novaga, Alessandra Pluda and Felix Schulze, *Evolution of networks with multiple junctions*, Astérisque 452 (2024). [Author text](https://people.dm.unipi.it/novaga/papers/mantegazza/tripunto/network-survey.pdf). Open Problem 9.1 (M1), §15 item 2 in the linked author version; numbering differs in earlier drafts.

2. Carlo Mantegazza, Matteo Novaga and Alessandra Pluda, *Type-0 singularities in the network flow—evolution of trees*, Journal für die reine und angewandte Mathematik 792 (2022), 189–221. [Article](https://doi.org/10.1515/crelle-2022-0055). Introduction and results for networks with few junctions give partial control.

## Status review

**Claimed outcome:** Kaiwen Jin's proposed counterexample constructs one smooth embedded network with six triple junctions and four fixed boundary endpoints. At its first singular time, the two exterior rays of the shrinking tangent flow each carry two copies of arclength. This refutes the multiplicity-one clause if the argument is accepted.

**Known cases:** Multiplicity one is established for networks with at most two triple junctions and for the separated tree class of Mantegazza, Novaga and Pluda, Theorem 2.11. The proposed example has six triple junctions and two bounded cells.

**Evidence:** [Counterexample manuscript](../research/solutions/158-network-multiplicity-one/paper/article.pdf) and [comparison with the original statement](../research/solutions/158-network-multiplicity-one/TARGET_COMPARISON.md).

**Review:** The author-side workflow used AI assistance, including one AI reader and one AI referee on an earlier draft, followed by a revision. The reviewers used separate contexts in a shared workspace. Independent mathematical review remains outstanding.
