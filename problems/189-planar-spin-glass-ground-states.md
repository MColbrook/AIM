# 189. Uniqueness of the planar spin-glass ground-state pair

**Area:** Disordered magnetic materials

**Status:** 🔵 OPEN

**Last checked:** 2026-11-03

## Problem statement

For each nearest-neighbor edge $`e`$ of $`\mathbb Z^2`$, sample $`J_e`$ independently from the standard Gaussian distribution. A spin configuration $`\sigma\in\{-1,1\}^{\mathbb Z^2}`$ is a ground state if flipping any finite set of spins cannot decrease its energy; explicitly,

```math
\sum_{\{x,y\}\in\partial_E A}J_{\{x,y\}}\sigma_x\sigma_y\ge0
\quad\text{for every finite }A\subset\mathbb Z^2,
```

where $`\partial_E A`$ contains edges with exactly one endpoint in $`A`$. Is it almost surely true that the set of all ground states is exactly $`\{\sigma,-\sigma\}`$ for some $`\sigma`$? The assertion concerns all infinite-volume ground states, without restricting the boundary conditions used to construct them.

## Application

The number of stable zero-temperature phases determines whether a two-dimensional spin glass has a simple or complex energy landscape.

## References

- [Paul Dario, Matan Harel and Ron Peled, *Quantitative Disorder Effects in Low-Dimensional Spin Systems* (2024)](https://doi.org/10.1007/s00220-024-05081-9), §§2.3.2 and 9, ground-state uniqueness discussion.
- [Louis-Pierre Arguin and Michael Damron, *On the number of ground states of the Edwards–Anderson spin glass model* (2014)](https://www.numdam.org/item/10.1214/12-AIHP499.pdf), introduction and restricted results.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2024 paper explicitly retains uniqueness of the ground-state pair as a conjecture. Uniqueness with finite-volume continuous couplings, half-plane theorems, and statements about particular translation-covariant state selections are weaker than the full-plane assertion here.

Itoi’s [arXiv:2012.11801v6](https://arxiv.org/html/2012.11801v6) appends an erratum restricting its uniqueness theorem to finite lattices: the infinite-volume convergence used in the argument was assumed and is not proved. That claim therefore does not settle the question above.

Search topics checked on 2026-09-08: two dimensional Edwards Anderson Gaussian ground state pair uniqueness solved 2025 2026.
