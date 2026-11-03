# 664. Sharp uniform approximation widths for small mixed Hölder smoothness

**Area:** Approximation theory and numerical analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge3`$ and a real number $`0<r<1/2`$. On the torus $`\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d`$, write
```math
\Delta_{h,j}f(x)=f(x+h e_j)-f(x),\qquad
\Delta_h^{E}f=\prod_{j\in E}\Delta_{h_j,j}f
```

for a nonempty subset $`E\subset\{1,\ldots,d\}`$; $`e_j`$ is the $`j`$th coordinate vector. Let $`\mathcal H_d^r`$ be the class of continuous complex-valued functions with
```math
\|f\|_\infty\le1,\qquad
\|\Delta_h^{E}f\|_\infty\le\prod_{j\in E}|h_j|^r
```

for every nonempty $`E`$ and every $`h_j\in[-\pi,\pi]`$ with $`j\in E`$. These conditions define a unit ball of dominating mixed Hölder smoothness, equivalently $`H_\infty^r=B^r_{\infty,\infty}`$ up to constants depending on $`d,r`$.

For $`n\ge2`$, define its Kolmogorov width in the uniform norm by
```math
d_n(\mathcal H_d^r)=\inf_{\substack{V\subset C(\mathbb T^d;\mathbb C)\text{ linear}\\\dim_{\mathbb C}V\le n}}
\ \sup_{f\in\mathcal H_d^r}\ \inf_{v\in V}\|f-v\|_\infty.
```

The approximating space $`V`$ is fixed for the whole class; the best coefficients may depend on $`f`$ without any sampling or continuity restriction.

**Is the known upper bound sharp?** More precisely, does every fixed pair $`(d,r)`$ admit $`c=c(d,r)>0`$ such that
```math
d_n(\mathcal H_d^r)\ge c\,n^{-r}(\log n)^{d-1+r}\qquad(n\ge2)?
```

The corresponding upper bound is known. The general lower bound quoted in the source has only $`(\log n)^{d-1}`$, leaving a logarithmic gap of exponent $`r`$. The two-dimensional case has the sharp order $`n^{-r}(\log n)^{1+r}`$ and is excluded here. The endpoint $`r=1/2`$ is also excluded.

This is the mixed Hölder instance of the source's question about sharpness of its small-smoothness width bounds. It concerns unrestricted linear approximation spaces, rather than a specified trigonometric space, a sparse grid, nonlinear parameter manifolds, or approximation measured in a stronger Besov norm.

## Application

Kolmogorov widths measure how well one fixed finite-dimensional approximation space can represent an entire class of functions. Determining this order would identify the best possible uniform error for reduced representations of functions with limited mixed regularity. These widths also enter upper bounds for recovering such functions from point samples.

## References

1. V. Temlyakov and T. Ullrich, [Bounds on Kolmogorov widths and sampling recovery for classes with small mixed smoothness](https://arxiv.org/abs/2012.09925), arXiv:2012.09925v1, definitions pp2/10–11, Theorem3.3, Theorem4.1 and OpenProblem2 on p21. Related publication: [Journal of Complexity67(2021),101575](https://doi.org/10.1016/j.jco.2021.101575).
2. V.N. Temlyakov and T. Ullrich, [Approximation of functions with small mixed smoothness in the uniform norm](https://arxiv.org/abs/2012.11983), arXiv:2012.11983v2, latest28October2021, Definition4.3/Lemma4.4, Theorem6.2 and Remark6.4; introduction explicitly asks whether these bounds are sharp for $`d>2`$. Related publication: [Journal of Approximation Theory277(2022),105718](https://doi.org/10.1016/j.jat.2022.105718).
3. K.V. Pozharska, [Orders of decay of entropy numbers and Kolmogorov width of mixed smoothness function classes](https://www.imath.kiev.ua/~young/youngconf2025/abstracts/Pozharska.pdf), official conference abstract,4–6June2025, Theorem2. Its sharp estimates use the stronger $`B_{q,1}`$ target norm; the abstract explicitly distinguishes the unresolved Lebesgue-norm problem.

## Status review

Reviewed18October2026 against both complete eligible preprints and selected current primary comparisons. Their final19-page and23-page journal editions have not been fully compared with the26-page and24-page preprints. The inspected final publisher introductions retain the open sharpness question; no final-edition proof parity is asserted.

The2025 results in $`B_{q,1}`$ measure approximation in a stronger norm, so their lower bounds do not automatically imply this uniform-norm lower bound. The2026 anisotropic-width results inspected here impose separate coordinate regularity and finite target exponents; those assumptions differ from the mixed-difference class above. Current weighted Wiener-space results concern other classes and approximation characteristics. Neither nonlinear sampling lower bounds nor sharp errors for one prescribed approximation method establish a Kolmogorov lower bound over every space $`V`$.

All AIM statuses and the project's existing findings were compared. AIM517 concerns local harmonic solution spaces of elliptic equations, and AIM542 concerns stable nonlinear manifold widths of isotropic Besov balls; neither is this target. The proposed Frolov problem concerns an integral functional on another mixed-smoothness class, rather than uniform approximation of a whole function. The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-mixed-holder-uniform-width-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/mixed-holder-width-prove2-0173-review.json) and [coordinator review](../FURTHER_problems/_tracking/mixed-holder-width-coordinator-review-2026-10-18.json) passed at their recorded extents. The current-status checks preserve the stated model and version limits; they do not certify every referenced proof.


### Online recheck, 2026-10-30

The d>=3 small-mixed-Holder question asks a Kolmogorov lower bound in the uniform target norm over every linear approximation space. Stronger Besov target norms, nonlinear sparse approximation and fixed-subspace errors do not supply it; no complete later result located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2012.09925); [status source 2](https://arxiv.org/abs/2012.11983); [status source 3](https://www.imath.kiev.ua/~young/youngconf2025/abstracts/Pozharska.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-06592f25a3b83569** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
