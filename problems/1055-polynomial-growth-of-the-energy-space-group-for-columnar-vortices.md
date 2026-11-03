# 1055. Polynomial growth of the energy-space group for columnar vortices

**Area:** Incompressible fluid mechanics and hydrodynamic stability
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`W\in C^2([0,\infty);[0,\infty))`$ be a vorticity profile with
```math
W(0)=2,\quad W'(0)=0,\quad W'(r)<0\ (r>0),\quad
\lim_{r\to\infty}r^3W'(r)=0,\quad
\int_0^\infty W(r)r\,dr<\infty.
```
Define
```math
\Omega(r)=\frac1{r^2}\int_0^rW(s)s\,ds,\quad
V(r)=r\Omega(r),\quad
\Phi(r)=2\Omega(r)W(r),\quad
J(r)=\frac{\Phi(r)}{\Omega'(r)^2}\quad(r>0).
```
Assume also $`J'(r)<0`$ for every $`r>0`$ and $`rJ'(r)\to0`$ as $`r\to\infty`$. These assumptions imply $`W(r)>0`$, $`\Omega(r)>0`$, and $`\Omega'(r)<0`$ for $`r>0`$.

The field $`U=V(r)e_\theta`$ is a stationary solution of the incompressible Euler equations on $`\mathbb R^3`$. On the real energy space
```math
X=\{u\in L^2(\mathbb R^3;\mathbb R^3):\nabla\!\cdot u=0\text{ in distributions}\},
```
let $`G_W(t)`$, $`t\in\mathbb R`$, be the strongly continuous evolution group of the linearized equations
```math
\begin{aligned}
\partial_tu_r+\Omega\partial_\theta u_r-2\Omega u_\theta&=-\partial_rp,\\
\partial_tu_\theta+\Omega\partial_\theta u_\theta+Wu_r&=-r^{-1}\partial_\theta p,\\
\partial_tu_z+\Omega\partial_\theta u_z&=-\partial_zp,\\
r^{-1}\partial_r(ru_r)+r^{-1}\partial_\theta u_\theta+\partial_zu_z&=0.
\end{aligned}
```
Here the group is the energy-space realization established by Gallay and Smets, with pressure enforcing the divergence constraint; no extra regularity of the initial vector in $`X`$ is imposed.

Does every such $`W`$ admit constants $`C_W\ge1`$ and $`N_W\in\mathbb N_0`$ such that
```math
\|G_W(t)\|_{X\to X}\le C_W(1+|t|)^{N_W}
\qquad\text{for every }t\in\mathbb R?
```
The constants may depend on the entire profile. Perturbations have no symmetry restriction.

## Application

A polynomial bound would quantify how disturbances can amplify around a stable vortex column. It would strengthen spectral stability into an estimate on transient energy growth, relevant to vortex models in atmospheric flows and engineering.

## References

1. Thierry Gallay, [*Stability of vortices in ideal fluids: The Legacy of Kelvin and Rayleigh*](https://www.aimsciences.org/aimsmath-upload/book/202172319108234.pdf), in *Hyperbolic Problems: Theory, Numerics, Applications*, AIMS Series on Applied Mathematics **10** (2020), 42–59. Theorem 3.3 on p. 57 and Section 4, second bullet, p. 58. The linked PDF is the publisher's complete proceedings; this chapter occupies physical pp. 54–71.
2. Thierry Gallay and Didier Smets, [*On the linear stability of vortex columns in the energy space*](https://arxiv.org/abs/1811.07584v2), *Journal of Mathematical Fluid Mechanics* **21** (2019), article 48, [DOI](https://doi.org/10.1007/s00021-019-0453-2). Theorem 1.1, Remark 1.3 and assumptions H1–H2 of the inspected v2.
3. Dallas Albritton and Wojciech S. Ożański, [*Linear and nonlinear instability of vortex columns*](https://arxiv.org/abs/2310.20674v3), v3, 8 December 2025, [published DOI](https://doi.org/10.4171/JEMS/1749). Its instability criteria concern vortices with an axial component.
4. Shuang Miao, Siqi Ren and Zhifei Zhang, [*Asymptotic linear stability of columnar vortices driven by Coriolis force*](https://arxiv.org/abs/2603.17268v1), 18 March 2026; selected model assumptions and Theorem 1.1 compared.

## Status review


**Known cases:** The all-mode energy-space group needs polynomial growth for every allowed profile. Spectral stability gives only subexponential information; axial-flow instabilities and Coriolis models have different base flows.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The all-mode energy-space group needs polynomial growth for every allowed profile. Spectral stability gives only subexponential information; axial-flow instabilities and Coriolis models have different base flows.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The known full-energy-space estimate is

```math
\|G_W(t)\|_{X\to X}\le C_{\varepsilon,W}e^{\varepsilon|t|}
\quad\text{for every }\varepsilon>0.
```

It supplies no quantitative control of the constant as epsilon tends to zero. Neither imaginary spectrum nor this subexponential bound automatically gives a polynomial bound. No uniform boundedness or nonlinear stability is requested here.

The formulation retains the explicit stronger decay condition $`r^3W'(r)\to0`$ from [2]. The published survey [1] instead displays $`rW'(r)\to0`$. This difference is recorded: the target uses the established group class from [2], and its other quantifiers match the polynomial-growth question in [1].

The instability results in [3] require an axial-flow condition absent from this target. The selected results in [4] concern axisymmetric perturbations, a different asymptotic base profile and weighted higher-regularity data; they do not give the unrestricted $`X\to X`$ bound. No matching complete solution or announcement was located in the recorded bounded checks. This does not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/columnar-vortex-polynomial-review.json), [selected independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-columnar-vortex-polynomial-review.json), [current comparisons](../FURTHER_problems/_tracking/columnar-vortex-polynomial-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/columnar-vortex-polynomial-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/columnar-vortex-polynomial-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/columnar-vortex-polynomial-coordinator-review-2026-10-19.json) record the checked scope and its limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-abdae4130d440600**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
