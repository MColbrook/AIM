# 661. Large Lipschitz graph pieces from single-scale projections

**Area:** Geometric measure theory and harmonic analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix integers $`2\le n<d`$. For every $`\delta>0`$ and $`C_0\ge1`$, do there exist constants
```math
L=L(n,d,\delta,C_0)\ge1,\qquad
\theta=\theta(n,d,\delta,C_0)>0
```

with the following property?

Let $`E\subset\mathbb R^d`$ be closed and $`n`$-Ahlfors–David regular with constant at most $`C_0`$: writing $`\mathcal H^n`$ for $`n`$-dimensional Hausdorff measure,
```math
C_0^{-1}r^n\le\mathcal H^n(E\cap B(x,r))\le C_0r^n
\quad(x\in E,\ 0<r<\mathrm{diam}E).
```

The diameter may be infinite. Here $`B(x,r)`$ is an open Euclidean ball.

Let $`G(d,n)`$ be the set of $`n`$-dimensional linear subspaces of $`\mathbb R^d`$, and let $`\pi_V`$ denote orthogonal projection onto $`V`$. Suppose that for some $`V_0\in G(d,n)`$,
```math
\mathcal H^n\!\left(\pi_V(E\cap B(0,1))\right)\ge\delta
\quad\text{whenever }\|\pi_V-\pi_{V_0}\|_{\mathrm{op}}<\delta .
```

Must there be an $`n`$-dimensional $`L`$-Lipschitz graph $`\Gamma\subset\mathbb R^d`$ such that
```math
\mathcal H^n(E\cap\Gamma)\ge\theta?
```

Precisely, such a graph has the form $`\Gamma=\{v+g(v):v\in W\}`$, where $`W\in G(d,n)`$ and $`g:W\to W^\perp`$ is $`L`$-Lipschitz. The graph's orientation is free. The constants are chosen before $`E`$ and $`V_0`$.

This is the $`n\ge2`$ residual of [1, Question 1]. The conclusion follows the source: its measured intersection is $`E\cap\Gamma`$, without an additional restriction to $`B(0,1)`$.

## Application

The problem asks whether lower bounds on the sizes of nearby orthogonal shadows of a rough set force a quantitatively large patch represented by one Lipschitz graph. Such graph pieces provide geometric structure useful in harmonic analysis and the analysis of singular integrals.

## References

1. T. Orponen, *Plenty of big projections imply big pieces of Lipschitz graphs*, Inventiones mathematicae **226** (2021), 653–709, [DOI:10.1007/s00222-021-01055-z](https://doi.org/10.1007/s00222-021-01055-z). Question 1 and equation (1.7) in §1.3; definitions in §1 and the operator-norm Grassmannian metric in §2. [Author manuscript, latest v3](https://arxiv.org/abs/2008.08843v3).
2. D. Dąbrowski, *Favard length and quantitative rectifiability* (2024), [arXiv:2408.03919v1](https://arxiv.org/abs/2408.03919v1), Theorem 1.1, Remark 1.4 and §1.1. Announces a solution of the planar branch and explicitly discusses higher-dimensional counterparts.
3. D. Dąbrowski, *Quantitative Besicovitch projection theorem for irregular sets of directions*, Proceedings of the London Mathematical Society **130** (2025), e70037, [DOI:10.1112/plms.70037](https://doi.org/10.1112/plms.70037); [latest author version](https://arxiv.org/abs/2211.16911v2), Theorem 1.7 and §1.3. Records related results under stronger projected-measure hypotheses.

## Status review

Orponen's Theorem 1.6 proves the corresponding implication when the projection lower bound is available uniformly in every ball and at every scale. The question above assumes it only in $`B(0,1)`$.

The planar case $`n=1,d=2`$ is covered by the announcement in [2], whose §1.1 explicitly answers the planar version of [1, Question 1]. It is excluded from this entry. Remark 1.4 of [2] identifies higher-dimensional counterparts as a possible extension. This entry makes no separate assertion about the branches $`n=1,d>2`$.

The $`L^\infty`$ or averaged $`L^2`$ bounds for projected Hausdorff measures in [3] are stronger than lower bounds on the measure of projected sets. They do not by themselves establish the displayed projection-only target. The later publication date of [3] was not treated as overriding the planar announcement in [2].

Bounded searches through 24 October 2026 located no matching complete resolution of the stated $`n\ge2`$ residual. The cited preprint's planar result was treated as an announced result; no independent certification of its full proof is claimed.

Selected original definitions and current main statements were checked, including the different Riesz-transform and qualitative rectifiability targets. Version histories and all-status repository matches were compared. Prove2Me checks covered targeted indexed searches and its homepage; no exhaustive site audit, publisher/preprint byte parity or full external proof verification is claimed.


### Online recheck, 2026-10-30

The all-scales big-projection theorem is known and the planar single-scale branch is announced. Neither the planar theorem nor stronger projected-measure bounds settle the n>=2 single-scale projected-set lower-bound question.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2008.08843); [status source 2](https://arxiv.org/abs/2408.03919); [status source 3](https://arxiv.org/abs/2211.16911). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c15ec6d2cd76af6a** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
