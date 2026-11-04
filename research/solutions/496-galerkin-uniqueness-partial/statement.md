# 496. Global uniqueness of fine-mesh semilinear Galerkin solutions

**Area:** Numerical PDEs and optimal control

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d=2`$ or $`3`$, be a bounded convex polygon or polyhedron. Fix real Lipschitz coefficients $`a_{ij}`$ on $`\overline\Omega`$ with

```math
\sum_{i,j=1}^d a_{ij}(x)\xi_i\xi_j\ge\Lambda|\xi|^2\qquad(\Lambda>0).
```

Let $`b\in L^p(\Omega;\mathbb R^d)`$, where $`p>2`$ if $`d=2`$ and $`p\ge3`$ if $`d=3`$, with $`\mathop{\mathrm{div}}\nolimits b\in L^2(\Omega)`$. Fix $`u\in L^2(\Omega)`$. Suppose $`f(x,t)`$ is measurable in $`x`$, continuous and nondecreasing in $`t`$, $`f(\cdot,0)\in L^2(\Omega)`$, and for every $`M>0`$ there is $`\phi_M\in L^2(\Omega)`$ such that

```math
|f(x,s)-f(x,t)|\le\phi_M(x)|s-t|\qquad(|s|,|t|\le M)
```

almost everywhere. No global growth bound on $`f`$ is imposed.

Take any conforming, shape-regular, quasi-uniform simplicial mesh family with maximum element diameter $`h\to0`$. Let $`V_h\subset H_0^1(\Omega)`$ be the continuous piecewise affine functions. Define

```math
a(v,w)=\int_\Omega\left(\sum_{i,j}a_{ij}\partial_i v\,\partial_j w+(b\cdot\nabla v)w\right)dx.
```

Does there exist $`h_0>0`$, depending on the fixed data and mesh family, such that for every $`h<h_0`$ there is exactly one $`y_h\in V_h`$ satisfying

```math
a(y_h,v_h)+\int_\Omega f(x,y_h)v_h\,dx=\int_\Omega u v_h\,dx\qquad(v_h\in V_h)?
```

Integrals are exact. Uniqueness is required among all discrete solutions, without an imposed uniform $`L^\infty`$ bound. A counterexample must retain fixed coefficients, reaction and forcing along arbitrarily fine meshes.

## Application

These equations discretize convection–diffusion–reaction states in PDE-constrained optimization. Global uniqueness would remove ambiguity in the discrete state assigned to a control; nonuniqueness would identify spurious branches that numerical optimization must exclude.

## References

1. E. Casas, M. Mateos and A. Rösch, [Numerical approximation of control problems of non-monotone and non-coercive semilinear elliptic equations](https://doi.org/10.1007/s00211-021-01222-7), Numerische Mathematik **149** (2021), 305–340; Assumptions 1–2, §3, equation (3.1), Theorems 3.5–3.7 and the explicit open question in the introduction.
2. E. Casas, M. Mateos and A. Rösch, [Analysis of control problems of nonmontone semilinear elliptic equations](https://arxiv.org/abs/1905.13493), ESAIM: Control, Optimisation and Calculus of Variations **26** (2020); continuous state equation.

## Status review

**Known cases:** Theorem 3.5 of [1] proves eventual global uniqueness when one $`\phi\in L^2`$ bounds both $`|f(x,t)|`$ and its global Lipschitz coefficient. Under the full assumptions, Theorem 3.7 proves existence and uniqueness within every sufficiently large fixed $`L^\infty`$ ball for sufficiently small $`h`$.

**Remaining target:** Exclude additional solutions outside those balls, or construct a fixed-data counterexample. Convergence of the bounded branch alone is insufficient.

The 23 September 2026 search found no matching full resolution or announcement. Later linear Neumann and coercive bilinear-control results have different hypotheses. Registry coverage is not exhaustive.
