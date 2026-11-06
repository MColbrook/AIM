# 049 — Global conductivity uniqueness for the p-Laplacian in higher dimensions

**Area:** Nonlinear inverse problems / electrical materials

**Status:** ✅ SOLVED

**Last checked:** 2026-11-06

## Problem statement

Fix $`n\geq3`$, $`1<p<\infty`$, $`p\ne2`$, and a bounded connected smooth domain $`\Omega\subset\mathbb R^n`$. Let $`\gamma_j\in C^\infty(\overline\Omega)`$ be strictly positive. For boundary data $`f`$, solve

```math
\nabla\cdot(\gamma_j|\nabla u|^{p-2}\nabla u)=0,
\qquad u|_{\partial\Omega}=f,
```

and define the nonlinear Dirichlet-to-Neumann map $`\Lambda_{\gamma_j,p}f=\gamma_j|\nabla u|^{p-2}\partial_\nu u`$, interpreted weakly on the trace space of $`W^{1,p}(\Omega)`$.

Prove or disprove that equality of these maps for all boundary data implies $`\gamma_1=\gamma_2`$. Do not assume an ordering, smallness, analyticity, or invariance in one direction.

## Application

The power-law constitutive relation models nonlinear conducting media. The question asks whether nonlinear boundary response identifies their spatial material coefficient.

## References

1. C.-Y. Guo, M. Kar and M. Salo, *Inverse problems for p-Laplace type equations under monotonicity assumptions* (2016). [Paper](https://arxiv.org/abs/1602.02591).
2. M. Kar, J. Railo and P. Zimmermann, *The fractional p-biharmonic systems: optimal Poincaré constants, unique continuation and inverse problems*, Calculus of Variations **62** (2023), 130, introduction. [Paper](https://doi.org/10.1007/s00526-023-02468-9).
3. C. I. Cârstea and A. Feizmohammadi, *Two uniqueness results in the inverse boundary value problem for the weighted p-Laplace equation*, Forum of Mathematics, Sigma **13** (2025), e147, Theorems 1.2–1.3 and Corollary 1.1. [Paper](https://doi.org/10.1017/fms.2025.10095).
4. M. J. Colbrook, *Global uniqueness for the weighted p-Calderón problem*, preprint (6 November 2026), Theorem 1.1, p. 2. [Zenodo record](https://zenodo.org/records/24017133), DOI [10.5281/zenodo.24017133](https://doi.org/10.5281/zenodo.24017133). [PDF](https://zenodo.org/api/records/24017133/files/weighted_p_calderon.pdf/content).

## Status review

**Resolution:** Colbrook's Theorem 1.1 in reference 4 states a complete affirmative resolution of the original target.

**Statement comparison:** The theorem covers every bounded connected smooth domain in dimension at least three, every known exponent between one and infinity other than two, and arbitrary smooth strictly positive scalar weights. Equality of the full weak nonlinear Dirichlet-to-Neumann maps on the complete trace space implies equality of the weights. It adds no ordering, smallness, analyticity, or directional-invariance assumption.

**Review scope:** Recorded as solved following the maintainer's resolution report. The [dated scope review](../research/solution_reviews/2026-11-06-049-zenodo-review.md) compares the deposited preprint's Theorem 1.1, weak-map definition and smoothness convention with this entry. This AI-assisted statement comparison is not a complete independent audit of the proof or Lean verification.

**Source and date:** Public Zenodo preprint, DOI 10.5281/zenodo.24017133, deposited 6 November 2026; checked on the same date. Earlier restricted results remain listed in references 1–3 for context.
