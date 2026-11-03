# 631. Rank-one and quasiconvex relaxation of two quadratic wells in the plane

**Area:** Calculus of variations / composite materials
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`m\ge2`$ be any integer. Equip $`M=\mathbb R^{2\times m}`$ with the Frobenius inner product $`F:G=\sum_{i,j}F_{ij}G_{ij}`$. Let $`L_1,L_2:M\to M`$ be arbitrary self-adjoint strictly positive-definite linear maps, let $`F_1,F_2\in M`$, and let $`k_1,k_2\in\mathbb R`$. Define

```math
W(F)=\min\{W_1(F),W_2(F)\},\qquad
W_j(F)=(F-F_j):L_j(F-F_j)+k_j.
```

For $`Q=(0,1)^2`$, define the periodic relaxation

```math
QW(F)=\inf_{\varphi\in C^\infty_{\mathrm{per}}(Q;\mathbb R^m)}
\int_Q W(F+\nabla\varphi(x))\,dx,
\qquad (\nabla\varphi)_{ij}=\partial_i\varphi_j.
```

Let $`RW`$ be the largest rank-one-convex function below $`W`$. Explicitly, a function $`g:M\to\mathbb R`$ is rank-one convex if

```math
g((1-t)A+tB)\le(1-t)g(A)+tg(B)
\quad(0\le t\le1,\ \mathrm{rank}(A-B)\le1).
```

Must $`QW(F)=RW(F)`$ for every $`F\in M`$ and every choice above?

The question permits different, anisotropic quadratic forms. It imposes no frame indifference, symmetry of $`F`$, fixed volume fraction or restriction to a single loading. The scalar case $`m=1`$ reduces to ordinary convex relaxation and is omitted as known. The displayed periodic formula is the quasiconvex relaxation for these finite continuous quadratic-growth energies.

## Application

The relaxed energy describes the lowest energy achievable by arbitrarily fine planar mixtures. Rank-one relaxation corresponds to repeated compatible layering. Equality would show that such layers suffice energetically for two quadratic phases, even with coupled fields and arbitrary phase anisotropy. It does not claim that a finite number of layers realizes every infimum.

## References

1. G. W. Milton, [*Some open problems in the theory of composites*](https://arxiv.org/abs/2008.03394v1), eligible preprint v1 (2020), §2, Problem 1, equations (2.1)–(2.5); published in Philosophical Transactions of the Royal Society A **379** (2021), 20200115, [DOI](https://doi.org/10.1098/rsta.2020.0115), Problem 2.1.

2. Y. Grabovsky and L. Truskinovsky, [*Marginal material stability*](https://faculty.cst.temple.edu/~yury/binodal.pdf), Journal of Nonlinear Science **23**(5) (2013), 891–969, DOI 10.1007/s00332-013-9173-6, §5, equations (5.1)–(5.2). This comparison concerns symmetric-strain isotropic wells.

## Status review

The complete 28-page 2020 version and all 114 references have been read for question discovery. The affine rank-one definition above is stated directly: the source's printed (2.5) repeats the same matrix argument in its three terms. This display defect does not change the surrounding explicit envelope-equality question. Known special two-well energies, general rank-one convexity counterexamples and full three-dimensional elastic G-closure questions require separate scope comparisons. Checked 18 October 2026. Bounded current-result and announcement searches, independent selected-primary comparison, semantic catalogue comparisons and the current all-status listing scan found no exact resolution or duplicate at their recorded extents. The 2021 final indexed question matches the target; its complete body and preprint parity have not been certified. The known symmetric-strain isotropic class in [2] does not establish the arbitrary anisotropic full-gradient assertion above.

The [primary inventory](../FURTHER_problems/_tracking/coordinator-composites/milton2008-full-question-review-2026-10-18.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-milton-two-quadratic-wells-review.json), [semantic comparison](../FURTHER_problems/_tracking/two-quadratic-wells-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/two-quadratic-wells-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/two-quadratic-wells-coordinator-review-2026-10-18.json) record evidence and limits. These AI checks do not assert human peer review.


### Online recheck, 2026-10-30

The target allows distinct arbitrary anisotropic positive quadratic forms on full gradients. Results for symmetric strains, compatible finite-well sets, or one quadratic form do not establish the stated universal envelope equality; no complete newer resolution located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2008.03394); [status source 2](https://arxiv.org/abs/2012.02871); [status source 3](https://journalofconvexanalysis.com/articles/jca04016/). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-be4685dda927af2d** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
