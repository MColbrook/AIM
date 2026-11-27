# 483. Automatic conservation laws for renormalized nonlinear diffusion

**Area:** Nonlinear diffusion PDEs; chemical mass conservation

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Let $`\Omega\subset\mathbb R^d`$ be smooth and bounded, $`N\ge2`$, $`d_i>0`$, and $`m_i\in(0,2)`$, with at least one $`m_i\ne1`$. Let $`f:[0,\infty)^N\to\mathbb R^N`$ be locally Lipschitz and quasi-positive ($`f_i(z)\ge0`$ if $`z_i=0`$), and assume

```math
\sum_i f_i(z)(\log z_i+\mu_i)\le C\sum_i(1+z_i\log z_i)\qquad(z_i>0)
```

for some constants $`C\ge0`$ and $`\mu_i\in\mathbb R`$. Take nonnegative finite-entropy initial data $`u_0`$.

Consider nonnegative functions $`u_i\in L^\infty(0,T;L^1(\Omega))`$, $`u_i^{m_i/2}\in L^2(0,T;H^1(\Omega))`$ for every finite $`T`$, satisfying the following truncated form of $`\partial_tu_i=d_i\Delta u_i^{m_i}+f_i(u)`$ with no-flux boundary conditions. For every smooth $`\xi`$ with compactly supported $`D\xi`$, every smooth space-time test $`\psi`$ on the closed domain, and almost every $`T`$,

```math
\begin{aligned}
\int_\Omega\xi(u(T))\psi(T)-\int_\Omega\xi(u_0)\psi(0)-\int_0^T\!\int_\Omega\xi(u)\partial_t\psi
={}&-\sum_{i,j}d_i m_i\int_0^T\!\int_\Omega\psi\xi_{ij}(u)u_i^{m_i-1}\nabla u_i\cdot\nabla u_j\\
&-\sum_i d_i m_i\int_0^T\!\int_\Omega\xi_i(u)u_i^{m_i-1}\nabla u_i\cdot\nabla\psi
+\sum_i\int_0^T\!\int_\Omega\xi_i(u)f_i(u)\psi.
\end{aligned}
```

The flux is interpreted as $`u_i^{m_i-1}\nabla u_i=(2/m_i)u_i^{m_i/2}\nabla u_i^{m_i/2}`$, and the gradient product as

```math
u_i^{m_i-1}\nabla u_i\cdot\nabla u_j=\frac4{m_i m_j}u_i^{m_i/2}u_j^{1-m_j/2}\nabla u_i^{m_i/2}\cdot\nabla u_j^{m_j/2}.
```

Does this identity alone imply, for every $`q\in\mathbb R^N`$ with $`q\cdot f(z)=0`$ for all $`z\ge0`$,

```math
\sum_i q_i\int_\Omega u_i(t)=\sum_i q_i\int_\Omega u_{i,0}\qquad\text{for almost every }t>0?
```

Neither this conservation law nor an entropy inequality is added as a solution axiom. Finite entropy of the initial data means $`\sum_i\int u_{i,0}(1+|\log u_{i,0}|)<\infty`$, with $`0|\log0|=0`$.

## Application

The question asks whether the weakest available continuum formulation itself preserves chemical invariants when diffusion degenerates, rather than requiring conservation as an additional selection rule.

## References

1. K. Fellner, J. Fischer, M. Kniely and B. Q. Tang, *Global renormalised solutions and equilibration of reaction–diffusion systems with nonlinear diffusion*, J. Nonlinear Sci. **33**, 66 (2023), Definition 1.1, identities (1.4)–(1.6), and Remark 1.2. [Article](https://doi.org/10.1007/s00332-023-09926-w).
2. J. Fischer, *Weak-strong uniqueness of solutions to entropy-dissipating reaction-diffusion equations*, Nonlinear Analysis **159** (2017), 181–207, linear-diffusion renormalization arguments. [Preprint](https://arxiv.org/abs/1703.00730).

## Status review

**Previous literature check (2026-09-22):** Open in cited literature; no later resolution located.

Remark 1.2 explicitly asks whether the truncated identity entails the conservation and entropy laws for nonlinear diffusion. The present entry isolates conservation as one definite assertion and retains the source’s exponent interval. For linear diffusion, or for bounded solutions, the implication is known; neither restriction is imposed here. Searches on 2026-09-22 for nonlinear diffusion, renormalized solutions, and automatic mass conservation found no later resolution. Existence of solutions constructed to satisfy conservation does not establish the implication for every solution of the truncated identity.

**Proposed resolution (2026-11-27).** The linked manuscript gives a five-component counterexample on an interval. It verifies the full truncated identity with a locally Lipschitz, quasi-positive, entropy-controlled reaction and finite-entropy initial data. For the reaction invariant $`q=(1,1,0,0,0)`$, the mass exceeds the prescribed initial value on a positive-time interval. The target comparison describes the AI-assisted proof and manuscript checks. The claim awaits the collection’s assessment.

[Proof](../research/solutions/483-nonlinear-diffusion-mass-conservation/paper.pdf) · [Target comparison and review scope](../research/solutions/483-nonlinear-diffusion-mass-conservation/target-comparison.md)
