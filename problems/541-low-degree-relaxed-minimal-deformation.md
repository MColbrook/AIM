# 541. Low-degree convergence of relaxed minimal-deformation surface elements

**Area:** Numerical analysis of evolving surfaces

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-21

## Problem statement

Let $`\Gamma^0\subset\mathbb R^3`$ be a smooth closed oriented surface and let $`u:\mathbb R^3\times[0,T]\to\mathbb R^3`$ be smooth. Assume that the relaxed minimal-deformation equations

```math
\partial_tX=v,\qquad v\cdot(n\circ X)=(u\circ X)\cdot(n\circ X),\qquad \partial_tX-\Delta_{\Gamma^0}X=\kappa(n\circ X)
```

have a smooth solution with $`X(\cdot,0)=\mathop{\mathrm{id}}\nolimits`$, where $`\Gamma(t)=X(\Gamma^0,t)`$, $`n`$ is its unit normal, and $`X(\cdot,t)`$ and its inverse are smooth throughout $`[0,T]`$. The scalar $`\kappa`$ is a constraint multiplier.

Fix $`k\in\{1,2,3\}`$. Let $`\Gamma_h^0`$ be degree-$`k`$ nodal interpolants of $`\Gamma^0`$ on an admissible, shape-regular, quasi-uniform family of curved triangular meshes. For each curved triangle $`K`$, let $`K_f`$ be its flat triangle with the same vertices and let $`F_K:K_f\to K`$ be its polynomial parametrization. Assume

```math
\max_K\bigl(\|F_K\|_{W^{k,\infty}(K_f)}+\|F_K^{-1}\|_{W^{1,\infty}(K)}\bigr)\le C_0,
```

where $`C_0`$ is independent of $`h`$, as in [1, (2.1)]. Let $`S_h`$ be the continuous degree-$`k`$ parametric finite element space on $`\Gamma_h^0`$.

Use exactly the semidiscrete scheme [1, (2.2)]: find $`(X_h,v_h,\kappa_h)\in S_h^3\times S_h^3\times S_h`$, initially $`X_h=\mathop{\mathrm{id}}\nolimits`$, such that $`\partial_tX_h=v_h`$ and

```math
\int_{\Gamma_h^0}(v_h-u(X_h,t))\cdot N_h\,\chi=0\qquad(\chi\in S_h),
```



```math
\int_{\Gamma_h^0}v_h\cdot\eta+\int_{\Gamma_h^0}\nabla_{\Gamma_h^0}X_h:\nabla_{\Gamma_h^0}\eta=\int_{\Gamma_h^0}\kappa_hN_h\cdot\eta\qquad(\eta\in S_h^3).
```

Here $`N_h=\widetilde n_h\circ X_h`$ and $`\widetilde n_h`$ is the elementwise geometric unit normal of $`X_h(\Gamma_h^0)`$; it can jump across element edges. All integrals are exact, and no normal averaging or additional stabilization is introduced.

Does this scheme admit a unique solution with nondegenerate evolving elements on $`[0,T]`$ for all sufficiently small $`h`$, and satisfy

```math
\sup_{0\le t\le T}\|X_h^\ell(\cdot,t)-X(\cdot,t)\|_{L^2(\Gamma^0)}\longrightarrow0\qquad(h\to0)
```

for every such smooth solution and mesh family, for each $`k=1,2,3`$? The lift uses the closest-point projection $`a_h:\Gamma_h^0\to\Gamma^0`$, with $`X_h^\ell=X_h\circ a_h^{-1}`$. Establish convergence with a quantitative error bound, or exhibit a counterexample under these assumptions. The three degrees form one convergence question.

## Application

Tangential mesh motion can preserve element quality during simulations of moving surfaces. Low-degree elements are inexpensive and widely used; a convergence theorem would justify the RMD method in this practical regime before the smooth surface develops a singularity.

## References

1. G. Gao, B. Li and R. Tang, [Convergent finite element approximations of surface evolution with relaxed minimal deformation](https://doi.org/10.1007/s00211-026-01529-3), Numerische Mathematik **158** (2026), 671–714; equations (1.5), (2.1)–(2.2), Theorem 2.1 and §7. [Author manuscript](https://libuyang.com/NM-15.pdf).
2. T. Huang, B. Li and R. Tang, [A convergent finite element method with minimal deformation rate for mean curvature flow](https://arxiv.org/abs/2602.14405v1), preprint (2026); equations (1.6)–(1.8) and Theorem 2.1 concern a different MDR scheme.

## Status review

**Partial progress reviewed 2026-10-21:** Kaiwen Jin's [manuscript](../research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.pdf), [PR 172](https://github.com/MColbrook/AIM/pull/172) at `71ed609ac0d213f399348e2bf6669767b8444ca0`, establishes distinct results for degrees one and three. The degree-two question remains open.

**Known cases:** For degree one, Theorem 2.2 gives one fixed smooth torus, a fixed tangential rigid rotation and an admissible alternating mesh family whose original discrete solutions are unique and nondegenerate on a common positive interval, yet the uniform-in-time lifted L2 map error has a positive lower limit. It does not claim failure for every linear mesh family. For degree three, Theorem 6.1 proves unique nondegenerate evolution throughout each prescribed smooth-solution interval and a lifted map-error bound $`C_T h^3\sqrt{1+|\log h|}`$ for every original admissible cubic family.

**Remaining target:** Establish convergence with a quantitative bound, or an admissible original-scheme counterexample, for degree two.

The [first independent AI review](../research/solution_reviews/2026-10-21-active-prs/172-review.md) reconstructs the complete cubic proof and independently checks the linear cell-level forcing calculation. A [second independent review](../research/solution_reviews/2026-10-21-active-prs/172-second-review.md) reconstructs the linear theorem's mesh-uniform inverse bounds, analytic estimates, common existence interval and fixed-time nonconvergence argument. Neither is human peer review or Lean verification.

**Literature check:** No earlier matching proved solution was found on 21 October 2026. Gao–Li–Tang [1] proves the original RMD convergence result for degrees at least four and leaves lower degrees open. A [2024 conference abstract by Buyang Li](https://aimsconference.org/AIMS-Conference/conf-reg2024/ts/detail1.php?abs_no=14) announces cubic convergence; the later published RMD paper still leaves that case unresolved, so the announcement alone is not treated as an available complete proof. Huang–Li–Tang [2] concerns a different MDR scheme with a projected normal. The reviews document these prior contributions and their exact scope.
