# 734. Generalized reaction–diffusion solutions from arbitrary integrable data

**Area:** Reaction–diffusion equations and chemical transport
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge2`$, $`N\ge2`$, and let $`\Omega\subset\mathbb R^n`$ be a bounded connected domain with smooth boundary. Fix $`d_i,m_i>0`$ and locally Lipschitz reaction functions $`f_i:[0,\infty)^N\to\mathbb R`$, $`1\le i\le N`$. Suppose that, for all $`s\in[0,\infty)^N`$:

1. $`f_i(s)\ge0`$ whenever $`s_i=0`$;
2. there are fixed $`a_i>0`$ and $`K\ge0`$ such that

```math
F_a(s):=\sum_{i=1}^N a_i f_i(s)
\le K\left(1+\sum_{i=1}^Na_i s_i\right);
```

3. there are nonnegative $`\phi_i\in C^1([0,\infty))`$ with $`\phi_i'>0`$ on $`(0,\infty)`$ and exponents $`0<\beta_j<m_j+1`$ such that

```math
f_i(s)\ge-\phi_i(s_i)\left(1+\sum_{j\ne i}s_j^{\beta_j}\right).
```

For every nonnegative initial vector $`u_0\in L^1(\Omega)^N`$, does the Neumann problem

```math
\partial_tu_i=d_i\Delta(u_i^{m_i})+f_i(u),\qquad
\partial_\nu(u_i^{m_i})=0,\qquad u_i(0)=u_{0i}
```

admit a global generalized solution in the following precise sense?

The components $`u_i:\Omega\times(0,\infty)\to[0,\infty)`$ are measurable. For every $`T<\infty`$, $`u_i,F_a(u)\in L^1(\Omega\times(0,T))`$ and, for almost every $`t>0`$,

```math
\int_\Omega\sum_i a_i u_i(t)
\le\int_\Omega\sum_i a_i u_{0i}
+\int_0^t\!\int_\Omega F_a(u).
```

For every smooth $`\rho:[0,\infty)\to\mathbb R`$ with compactly supported derivative, $`\rho'\le0`$ and $`\rho''\ge0`$, set

```math
P_i(s)=\int_0^s\sigma^{(m_i-1)/2}\sqrt{\rho''(\sigma)}\,d\sigma,
\qquad
Q_i(s)=\int_0^s\sigma^{m_i-1}\rho'(\sigma)\,d\sigma.
```

Require $`\rho'(u_i)f_i(u)\in L^1(\Omega\times(0,T))`$ and $`\nabla P_i(u_i)\in L^2(\Omega\times(0,T);\mathbb R^n)`$ for every finite $`T`$. For every nonnegative $`\varphi\in C_c^\infty(\overline\Omega\times[0,\infty))`$ with $`\partial_\nu\varphi=0`$ on the boundary, require

```math
-\int_0^\infty\!\int_\Omega \rho(u_i)\partial_t\varphi
-\int_\Omega\rho(u_{0i})\varphi(0)
\le -d_i m_i\int_0^\infty\!\int_\Omega\varphi|\nabla P_i(u_i)|^2
+d_i m_i\int_0^\infty\!\int_\Omega Q_i(u_i)\Delta\varphi
+\int_0^\infty\!\int_\Omega \rho'(u_i)f_i(u)\varphi.
```

The initial condition is encoded by this inequality and the mass bound. No additional strong $`L^1`$ initial trace, full distributional equality, or $`L^{m_i+1}`$ space–time integrability up to $`t=0`$ is imposed.

## Application

The components model nonnegative species concentrations. Finite total mass is a natural assumption for highly concentrated initial mixtures; an answer would determine whether the generalized model can start from these data without assuming additional spatial integrability or an entropy structure.

## References

1. J. Lankeit and M. Winkler, [*Global existence in reaction–diffusion systems with mass control under relaxed assumptions merely referring to cross-absorptive effects*](https://doi.org/10.1007/s00028-022-00768-9), Journal of Evolution Equations **22** (2022), article 14. Theorem 1.1, Remark (iii) on pp. 3–4, and Definitions 2.1–2.2 on pp. 8–9. [Final PDF](https://d-nb.info/1258702177/34).
2. E.-H. Laamri and B. Perthame, [*Reaction-diffusion systems with initial data of low regularity*](https://doi.org/10.1016/j.jde.2020.06.042), Journal of Differential Equations **269** (2020), 9310–9335. [Preprint](https://arxiv.org/abs/1908.09693).
3. K. Fellner, J. Fischer, M. Kniely and B. Q. Tang, [*Global Renormalised Solutions and Equilibration of Reaction–Diffusion Systems with Nonlinear Diffusion*](https://doi.org/10.1007/s00332-023-09926-w), Journal of Nonlinear Science **33** (2023), article 66.

## Status review


**Known cases:** Generalized existence from merely L1 data is weaker than classical existence but is still beyond the source integrability thresholds. Entropy-dissipating renormalized systems, logarithmic-entropy data and restricted diffusion exponents impose additional conditions absent here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Generalized existence from merely L1 data is weaker than classical existence but is still beyond the source integrability thresholds. Entropy-dissipating renormalized systems, logarithmic-entropy data and restricted diffusion exponents impose additional conditions absent here.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00028-022-00768-9); [comparison source 2](https://d-nb.info/1258702177/34); [comparison source 3](https://doi.org/10.1016/j.jde.2020.06.042); [comparison source 4](https://arxiv.org/abs/1908.09693); [comparison source 5](https://doi.org/10.1007/s00332-023-09926-w). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check:** No matching complete resolution was located in the reviewed primary sources and searches through 18 October 2026. Coordinator admission review remains pending.

The source proves existence if $`u_0\in L^r`$: $`r>1`$ in dimension two and $`r\ge2n/(n+2)`$ in higher dimensions. It explicitly asks whether integrability alone suffices. Dimension one is already included in its theorem. The present statement retains its generalized solution notion rather than promoting it to a weak or classical solution. In the source's displayed (2.3), the coefficient of the $`Q_i\Delta\varphi`$ term is printed $`d_1m_i`$; the PDE and proof (3.23) use $`d_im_i`$, which is used here.

The 2023 renormalized existence theorem assumes an entropy inequality and finite initial logarithmic entropy, as well as $`0<m_i<2`$. Those additional assumptions are absent here. The inspected earlier low-regularity theorems impose additional full-growth or $`H^{-1}`$ hypotheses. The 2026 Hopf–Tang bulk–interface theorem also assumes Boltzmann entropy dissipation and finite initial logarithmic entropy, and does not supply the assertion above.

The [primary packet](../FURTHER_problems/_tracking/parallel/continuum/lankeit2022-l1-data-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-lankeit2022-l1-data-review.json), [semantic comparison](../FURTHER_problems/_tracking/lankeit-l1-data-duplicates-review-2026-10-18.json), [catalogue review](../FURTHER_problems/_tracking/lankeit-l1-data-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/lankeit-l1-data-coordinator-review-2026-10-18.json) preserve evidence and access limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-29fd60f466cebea3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
