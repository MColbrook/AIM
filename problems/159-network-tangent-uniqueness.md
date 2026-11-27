# 159. Uniqueness of the limiting shape at a network singularity

**Area:** Grain-boundary evolution

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Consider a finite embedded planar network moving by curvature, with only $`120^\circ`$ triple junctions and fixed endpoints on the boundary of a smooth strictly convex domain. At an interior singular point $`(x_0,T)`$, set

```math
\widetilde\Gamma(t)=\frac{\Gamma(t)-x_0}{\sqrt{2(T-t)}}.
```

Is the limiting shrinker independent of the sequence $`t_j\uparrow T`$ used to obtain it? Precisely, must all locally convergent subsequences of the rescaled networks have the same limiting arclength varifold, including its integer multiplicities? No rotation of the limit is allowed when comparing subsequences.

## Application

A unique limiting shape would make the local geometry of a grain-rearrangement event predictable as observation resolution changes.

## References

1. Carlo Mantegazza, Matteo Novaga, Alessandra Pluda and Felix Schulze, *Evolution of networks with multiple junctions*, Astérisque 452 (2024). [Author text](https://people.dm.unipi.it/novaga/papers/mantegazza/tripunto/network-survey.pdf). Open Problem 7.25 and §15 item 3 in the linked author version explicitly ask for uniqueness of blow-up limits.

2. Alessandra Pluda and Marco Pozzetta, *Łojasiewicz–Simon inequalities for minimal networks: stability and convergence*, Mathematische Annalen (2023). [Article](https://doi.org/10.1007/s00208-023-02714-7). Conditional convergence results illustrate the role of a nondegenerate limiting network.

## Status review

**Claimed outcome:** Kaiwen Jin gives a proof of local weak uniqueness of the tangent arclength varifold at each interior finite-time singularity. The proof includes the integer multiplicities and compares the limits in the fixed coordinates of the statement.

**Known case:** Pluda and Pozzetta's [Theorem 1.1](https://arxiv.org/abs/2204.11675v2) gives smooth convergence for an endpoint-free graph with a nonempty compact nondegenerate blow-up on the same graph. The claim here uses the original local weak varifold topology.

**Literature check:** A targeted search for general degenerate or multiply covered planar network blow-up uniqueness, including recent primary sources, located the restricted results described above and no earlier proof of this exact statement.

**Evidence:** [Manuscript](../research/solutions/159-network-tangent-uniqueness/paper/article.pdf) and [statement comparison](../research/solutions/159-network-tangent-uniqueness/TARGET_COMPARISON.md).

**Review:** Separate AI roles assessed the proof and read a frozen draft in a shared environment. The author revised the draft after the reader and referee reports. Independent external review is outstanding.
