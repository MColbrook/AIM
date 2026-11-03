# 736. Global strong aggregation–diffusion without detailed balance

**Area:** Nonlocal PDEs / population dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix integers $`d\ge1`$, $`n\ge2`$ and constants $`D_i>0`$. Let $`u_i^0\in C_c^\infty(\mathbb R^d)`$ be nonnegative and not identically zero. For every ordered pair $`i,j`$, let $`K_{ij}:\mathbb R^d\to\mathbb R`$ be bounded, compactly supported, even and of bounded variation. Thus $`K_{ij}(x)=K_{ij}(-x)`$ almost everywhere and its distributional gradient is a finite vector measure. The kernels may have either sign. No relation between $`K_{ij}`$ and $`K_{ji}`$ is imposed; positive weights satisfying $`\pi_iK_{ij}=\pi_jK_{ji}`$ need not exist.

Does the Cauchy problem on $`\mathbb R^d`$

```math
\partial_tu_i=D_i\Delta u_i+\nabla\cdot\left(u_i\sum_{j=1}^n\nabla(K_{ij}*u_j)\right),\qquad u_i(0)=u_i^0,
```

admit a unique global nonnegative strong solution for every such choice, with no smallness restriction on the masses $`m_i=\int u_i^0`$?

Convolution is over $`\mathbb R^d`$ and $`\nabla(K_{ij}*u_j)=K_{ij}*\nabla u_j`$ in distributions. The strong class is fixed as follows. For every finite $`T`$, require componentwise

```math
u_i\in L^\infty((0,T)\times\mathbb R^d)
\cap L^\infty(0,T;L^1(\mathbb R^d)\cap H^1(\mathbb R^d))
\cap L^2(0,T;H^2(\mathbb R^d)),
\qquad \nabla\sqrt{u_i}\in L^2((0,T)\times\mathbb R^d),
```

```math
\partial_tu_i\in L^{4/3}(0,T;W^{-1,q}(\mathbb R^d)),\qquad
q=\begin{cases}2d/(2d-1),&d\ne2,\\6/5,&d=2.\end{cases}
```

Require $`u_i(t)\to u_i^0`$ in $`L^2`$ as $`t\downarrow0`$ and, for every $`\phi\in L^4(0,T;W^{1,q'}(\mathbb R^d))`$, where $`1/q+1/q'=1`$,

```math
\int_0^T\langle\partial_tu_i,\phi\rangle\,dt
+D_i\int_0^T\!\int_{\mathbb R^d}\nabla u_i\cdot\nabla\phi
=-\int_0^T\!\int_{\mathbb R^d}u_i\sum_j(K_{ij}*\nabla u_j)\cdot\nabla\phi.
```

Uniqueness concerns this whole class. Bounds may depend on $`T`$, all data and kernels; no uniform-in-time estimate is requested. This is a compact-kernel, smooth-data subfamily of the explicit general question in [1, §5, question 2].

## Application

These equations model populations whose movement responds to densities sensed in a spatial neighbourhood. Ordered interaction kernels allow each species to respond differently to the other. Discontinuous top-hat kernels, given by signed constants on balls and zero outside, are included. Global existence would justify evolution of these finite-range sensing models at arbitrary population masses. [1,3]

## References

1. José A. Carrillo, Yurij Salmaniw and Jakub Skrzeczkowski, *Well-posedness of aggregation-diffusion systems with irregular kernels*, Annales de l'Institut Henri Poincaré C43(2026),1201–1258, DOI10.4171/AIHPC/173. [Published PDF](https://ems.press/content/serial-article-files/53532?nt=1). Equation(1.2), hypotheses(H1)–(H6), Definitions3.1/3.3, Theorems4.1–4.4 and §5 final question(2), printed1252.
2. Valeria Giunta, Thomas Hillen, Mark A. Lewis and Jonathan R. Potts, *Positivity and global existence for nonlocal advection-diffusion models of interacting populations*, AIMS Mathematics10(9)(2025),21254–21272, DOI10.3934/math.2025949. [Published PDF](https://www.aimspress.com/aimspress-data/math/2025/9/PDF/math-10-09-949.pdf). Introduction and Theorems2/4/5: kernels are twice differentiable with bounded gradient.
3. Hao Wang and Yurij Salmaniw, *Open problems in PDE models for knowledge-based animal movement via nonlocal perception and cognitive mapping*, Journal of Mathematical Biology86(2023),71, DOI10.1007/s00285-023-01905-9. [Eligible preprintv3](https://arxiv.org/abs/2201.09150v3). Model(2.10), OpenProblem1 and§5.1; the final69-page version has not been read here.

4. Y. Chen, B. Niu and H. Wang, [*Well-Posedness and Pattern Formation in a Two-Species Reaction–Diffusion System with Nonlocal Perception*](https://doi.org/10.1111/sapm.70186), Studies in Applied Mathematics **156**(2) (2026), e70186, assumptions H1–H5 and Theorems 2.6–2.9.

## Status review


**Known cases:** The unresolved part is arbitrary-mass global existence for sign-changing compact BV kernels without detailed balance. Smooth W2-infinity kernels, small-mass bounds, torus bifurcation and conditional uniqueness are narrower or different conclusions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The unresolved part is arbitrary-mass global existence for sign-changing compact BV kernels without detailed balance. Smooth W2-infinity kernels, small-mass bounds, torus bifurcation and conditional uniqueness are narrower or different conclusions.

Additional comparison sources: [comparison source 1](https://ems.press/content/serial-article-files/53532?nt=1); [comparison source 2](https://www.aimspress.com/aimspress-data/math/2025/9/PDF/math-10-09-949.pdf); [comparison source 3](https://arxiv.org/abs/2201.09150v3); [comparison source 4](https://doi.org/10.1111/sapm.70186). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 18 October 2026. Reference [1] explicitly retains the nonbalanced systems question. Its arbitrary-mass existence theorem assumes detailed balance; its alternative theorem assumes small masses relative to diffusivities and kernel norms. Theorem 4.10 already proves uniqueness conditional on existence in the stated strong class without either restriction. The unresolved content here is therefore global existence at arbitrary mass.

The smooth-kernel result [2] does not cover discontinuous BV kernels. Mollifying a top-hat gives derivative bounds that need not be uniform, so that theorem alone does not supply the required limiting estimates. Reference [4] assumes a small-mass inequality in H5 for its weak and strong existence results; its classical-solution statement upgrades the strong solution already obtained. Its two-dimensional periodic cross-only model also has narrower scope. Current torus bifurcation and dynamic-memory theorems were compared at their actual model and hypothesis level; no exact general resolution was located.

The final 58-page primary article, all six figures and all 75 references were read for question discovery. Current comparisons and the independent audit have the selected extents recorded in the accompanying receipts; they do not certify every cited proof or all edition/correction families.

The [source packet](../FURTHER_problems/_tracking/parallel/continuum/irregular-kernel-no-balance-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-irregular-kernel-no-balance-review.json), [semantic comparison](../FURTHER_problems/_tracking/irregular-kernel-systems-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/irregular-kernel-systems-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/irregular-kernel-systems-coordinator-review-2026-10-18.json) record the evidence and its limits. These AI checks do not assert human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-60456ace402b9334**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
