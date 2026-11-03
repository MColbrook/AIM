# 964. Power concavity of fractional torsion on convex domains

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`d\ge2`$, every $`\alpha\in(0,1)\cup(1,2)`$, and every nonempty bounded open convex set $`D\subset\mathbb R^d`$, let $`u_D`$ be the continuous solution of the restricted fractional Dirichlet problem

```math
(-\Delta)^{\alpha/2}u_D=1\quad\hbox{in }D,
\qquad u_D=0\quad\hbox{on }\mathbb R^d\setminus D.
```

The operator acts on the zero extension to all of $`\mathbb R^d`$:

```math
(-\Delta)^{\alpha/2}f(x)
=c_{d,\alpha}\,\mathrm{PV}\!\int_{\mathbb R^d}
\frac{f(x)-f(y)}{|x-y|^{d+\alpha}}\,dy,
\qquad
c_{d,\alpha}=\frac{2^\alpha\Gamma((d+\alpha)/2)}
{\pi^{d/2}|\Gamma(-\alpha/2)|}.
```

Set $`p_\alpha=1`$ when $`0<\alpha<1`$, and $`p_\alpha=1/\alpha`$ when $`1<\alpha<2`$. Must $`u_D^{p_\alpha}`$ be concave on $`D`$? Equivalently, must

```math
u_D((1-t)x+ty)^{p_\alpha}
\ge (1-t)u_D(x)^{p_\alpha}+t u_D(y)^{p_\alpha}
```

hold for all $`x,y\in D`$ and $`0\le t\le1`$?

These are the two regimes of Kulczycki's Conjecture 7.2. The exterior condition specifies the restricted fractional Laplacian, rather than a spectral fractional power of the Dirichlet Laplacian.

## Application

The function $`u_D(x)`$ is the expected exit time from $`D`$ for an isotropic symmetric $`\alpha`$-stable process. The question asks for uniform shape information about this lifetime across convex domains and nonlocal diffusion orders.

## References

1. T. Kulczycki, [*On concavity of solutions of the Dirichlet problem for the equation $`(-\Delta)^{1/2}\varphi=1`$ in convex planar regions*](https://doi.org/10.4171/JEMS/695), Journal of the European Mathematical Society 19 (2017), 1361–1420. Equations (3)–(4), Theorem 1.5, Conjecture 7.2 and Remark 7.3; native PDF pages 2–3 and 57–58.
2. M. Gallo and M. Squassina, [*Concavity and perturbed concavity for p-Laplace equations*](https://doi.org/10.1016/j.jde.2025.113452), Journal of Differential Equations 440 (2025), 113452, §7.3, pages 55–56. Restates the conjectured exponent as $`\min\{1/(2s),1\}`$ for operator order $`2s=\alpha`$.
3. J. Li and S. Shi, [*Strict Concavity of the Torsion Function for the Restricted Half-Laplacian in Bounded Convex Domains*](https://arxiv.org/abs/2608.19586v2), preprint (2026), Theorem 1.1. Announces the separate $`\alpha=1`$ case in every dimension.
4. N. De Nitti, X. Fernández-Real, F. Grube and H. Prasad, [*Superharmonicity of the fractional ground state*](https://arxiv.org/abs/2608.11686v2), preprint (2026), Theorem 1.1 and Proposition 1.7. Concerns an eigenfunction equation with right-hand side $`\lambda u`$.

## Status review


**Known cases:** The half-Laplacian announcement covers alpha=1, explicitly excluded here. The eigenfunction equation and local p-Laplace concavity results are different; the two non-half fractional torsion regimes remain unaddressed in the matching results.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The half-Laplacian announcement covers alpha=1, explicitly excluded here. The eigenfunction equation and local p-Laplace concavity results are different; the two non-half fractional torsion regimes remain unaddressed in the matching results.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Balls satisfy the proposed concavity by the explicit torsion formula in Kulczycki's Remark 1.3. The classical $`\alpha=2`$ square-root-concavity theorem is also known. The separate half-Laplacian case $`\alpha=1`$ is excluded from this target because Li–Shi announce its resolution.

For $`1<\alpha<2`$, ordinary concavity can fail on narrow convex cones; the conjecture asks for concavity after taking the smaller power $`1/\alpha`$. Kulczycki's Remark 7.3 also rules out improving the exponent uniformly over all bounded convex domains. The inequalities in Theorem 1.5 do not establish the requested power concavity.

The 2025 discussion and its perturbative eigenfunction results, and the 2026 ground-state results and counterexamples, do not give the asserted constant-forcing torsion theorem for arbitrary convex domains. Searches for proofs, counterexamples and 2025–2026 announcements located no matching resolution of these two regimes. This records the scope of the literature check; it does not certify the complete proofs of the cited preprints.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fd42b218cf0091e1**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
