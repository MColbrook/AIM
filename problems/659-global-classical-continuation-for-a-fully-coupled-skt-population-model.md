# 659. Global classical continuation for a fully coupled SKT population model

**Area:** Population dynamics / cross-diffusion PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^3=(\mathbb R/\mathbb Z)^3`$. Fix arbitrary constants $`d_1,d_2>0`$ and $`a_{ij},r_i,s_{ij}\geq0`$, for $`i,j\in\{1,2\}`$. For smooth strictly positive initial densities $`u_1^0,u_2^0`$ on $`\mathbb T^3`$, consider the periodic system

```math
\begin{aligned}
\partial_tu_1&=\Delta[(d_1+a_{11}u_1+a_{12}u_2)u_1]
 +u_1(r_1-s_{11}u_1-s_{12}u_2),\\
\partial_tu_2&=\Delta[(d_2+a_{21}u_1+a_{22}u_2)u_2]
 +u_2(r_2-s_{21}u_1-s_{22}u_2),\qquad (u_1,u_2)|_{t=0}=(u_1^0,u_2^0).
\end{aligned}
```

Does its unique maximal local nonnegative strong solution continue through every finite time, for every such choice of coefficients and data? Precisely, is

```math
(u_1,u_2)\in C([0,T];H^4(\mathbb T^3)^2)
\cap L^2(0,T;H^5(\mathbb T^3)^2)
```

for every finite $`T`$? With smooth data this asks for classical continuation. No smallness, equality $`d_1=d_2`$, dominance of self diffusion, or triangularity assumption is imposed; in particular both cross coefficients $`a_{12},a_{21}`$ may be positive. Uniform bounds as $`t\to\infty`$ are not an additional requirement.

This is a three-dimensional positive-data instance of the possible-blowup question discussed in [1, §1.2], with its exact model and coefficient assumptions from [1, (1.9)]. The source gives local strong solutions and a Sobolev blowup criterion. Choosing the displayed fixed Sobolev class specifies the continuation target.

## Application

The densities describe two competing populations whose dispersal responds to their own crowding and the other population. The problem asks whether this smooth continuum model remains regular over every finite observation interval, including large spatial variations in the initial populations.

## References

1. Isabelle Gallagher and Ayman Moussa, [*The Cauchy problem for quasi-linear parabolic systems revisited*](https://jep.centre-mersenne.org/articles/10.5802/jep.319/), *Journal de l’École polytechnique — Mathématiques* **12** (2025), 1633–1676. §1.2, equations (1.9)–(1.10), Theorem 3 and §1.4 give the question, model, local theorem and strong spaces. [Published PDF](https://jep.centre-mersenne.org/item/10.5802/jep.319.pdf).
2. Isabelle Gallagher and Ayman Moussa, [*Corrigendum: The Cauchy problem for quasi-linear parabolic systems revisited*](https://jep.centre-mersenne.org/articles/10.5802/jep.349/), *Journal de l’École polytechnique — Mathématiques* **13** (2026), 1389–1391. Corrects §7.4 of [1], concerning local critical Besov well-posedness.
3. Alexandre Bertolino, [*Refined Blow-Up Criteria and Global Solutions for Triangular Cross-Diffusion Systems*](https://arxiv.org/abs/2607.01857), July 2026 preprint, v1. The diffusion hierarchy is a material restriction.
4. Yuan Lou and Michael Winkler, [*Global Existence and Uniform Boundedness of Smooth Solutions to a Cross-Diffusion System with Equal Diffusion Rates*](https://doi.org/10.1080/03605302.2015.1052882), *Communications in Partial Differential Equations* **40** (2015), 1905–1941. Theorem 1.1 assumes equal base diffusivities in a bounded convex domain of dimension at most three.

## Status review


**Known cases:** The general periodic fully coupled three-dimensional SKT continuation question survives the 2026 local corrigendum. Triangular diffusion, equal base diffusivities, diagonal models or approximation conditional on a smooth reference impose extra assumptions.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The published source [1] explicitly discusses the unresolved possibility of blowup for SKT strong solutions in its periodic setting. Its linked 2026 correction [2] repairs a local endpoint proof. The recent global results in [3] retain triangular diffusion. The equal-rate result [4] does not cover arbitrary $`d_1,d_2`$.

The review also checked the coefficient restrictions in Dung Le’s 2006 global theorem, the actual diagonal-diffusion model in the latest version of arXiv:2306.06045, and the assumed smooth-reference hypothesis in the October 2026 regularization announcement arXiv:2610.22079. None establishes this unrestricted fully coupled continuation target. AIM 324, 469 and 479 concern, respectively, chemotaxis consumption, a superlinear weak localization limit, and Maxwell–Stefan diffusion; their equations and questions differ.

Independent selected-primary audits checked the full coupling, normal ellipticity, nonnegative coefficients, local strong theory and the finite-time continuation class. The fresh Prove2Me snapshot reconciles 4,629 distinct listings over 186 pages; its only returned SKT-family context is unchanged from the reviewed Hilbert16/Petrovskii limit-cycle listing and is unrelated. The catalogue comparison concerns public listing descriptions, not every mission proof.

The original published article and its separate 2026 correction were read in full for question discovery. Recent comparison papers were read only to the extent recorded in the [source review](../FURTHER_problems/_tracking/parallel/continuum/skt-global-classical-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-skt-review.json). These bounded checks found no matching resolution or complete announcement. The precise fixed-dimensional Sobolev formulation above is a specified instance of the source’s open direction. See also the [fresh catalogue comparison](../FURTHER_problems/_tracking/fresh-catalogue-riccati-skt-rank-review.json).


### Online recheck, 2026-10-30

The general periodic fully coupled three-dimensional SKT continuation question survives the 2026 local corrigendum. Triangular diffusion, equal base diffusivities, diagonal models or approximation conditional on a smooth reference impose extra assumptions.

Comparators and current-status sources: [status source 1](https://doi.org/10.5802/jep.319); [status source 2](https://doi.org/10.5802/jep.349); [status source 3](https://arxiv.org/abs/2607.01857). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-7d3599ac0ca013fb** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
