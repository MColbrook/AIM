# 746. Global weak existence for nonlocal quantum drift–diffusion–Poisson

**Area:** Quantum semiconductor transport
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`I=(0,1)`$, and let $`H_0=-\partial_{xx}`$ act on the complex Hilbert space $`L^2(I)`$ with domain
```math
D(H_0)=\{\psi\in H^2(I):\psi(0)=\psi(1),\ \psi'(0)=\psi'(1)\}.
```
Write $`H^1_{\rm per}(I)=\{v\in H^1(I):v(0)=v(1)\}`$, and write $`H^{-1}_{\rm per}`$ for its dual. There is no prescribed external potential. All physical constants are fixed to one.

A density operator is a nonnegative self-adjoint trace-class operator $`\rho`$ on $`L^2(I)`$. Its spatial density $`n[\rho]`$ is defined by
```math
\mathrm{Tr}(M_\varphi\rho)=\int_I\varphi(x)n[\rho]\,(x)\,dx
\quad(\varphi\in L^\infty(I)),
```
where $`M_\varphi`$ denotes multiplication by $`\varphi`$. Put
```math
\mathcal E_+=\{\rho\ge0:\rho\text{ is trace-class},\
H_0^{1/2}\rho H_0^{1/2}\text{ is trace-class}\},
\qquad
\|\rho\|_{\mathcal E}=\mathrm{Tr}\rho+
\mathrm{Tr}(H_0^{1/2}\rho H_0^{1/2}).
```
Products in this definition are understood through their nonnegative trace-class extensions.

For a nonnegative $`n\in H^1_{\rm per}(I)`$, define the extended constrained energy
```math
\mathcal K(n)=\inf_{\substack{\rho\in\mathcal E_+\\n[\rho]=n}}
\left\{\mathrm{Tr}(\rho\log\rho-\rho)+
\mathrm{Tr}(H_0^{1/2}\rho H_0^{1/2})\right\},
```
using $`0\log0=0`$ and $`\inf\varnothing=+\infty`$. No minimizer is asserted for an arbitrary nonnegative $`H^1`$ density. For the strictly positive initial densities below, the constrained problem has a unique minimizer and finite value. Let $`V[n]\in H^1_0(I)`$ be the unique weak solution of
```math
-V[n]''=n,\qquad V[n]\,(0)=V[n]\,(1)=0,
```
and define
```math
\mathcal F(n)=\mathcal K(n)+
\frac12\int_I|V[n]'|^2\,dx.
```

For every real $`n_0\in H^1_{\rm per}(I)`$ with $`\min_{[0,1]}n_0>0`$ and $`\int_I n_0=1`$, does there exist a global weak solution $`(n,A,V)`$ with the following properties on every finite interval $`[0,T]`$?

```math
\begin{aligned}
n&\ge0,\qquad
n\in L^\infty(0,T;H^1_{\rm per})\cap H^1(0,T;H^{-1}_{\rm per})
\cap C([0,T];L^2(I)),\qquad n(0)=n_0,\quad \int_I n(t)=1,\\
A&\in L^2(0,T;H^1_{\rm per}(I)),\qquad
V\in L^\infty(0,T;H^1_0(I)),\qquad -V''=n,\\
\rho(t)&=\exp[-(H_0+A(t))]\in L^\infty(0,T;\mathcal E_+),\qquad
H_0\rho H_0\in L^2(0,T;\mathcal J_1).
\end{aligned}
```

Here $`A`$ is real, $`\mathcal J_1`$ is the trace-class space with trace norm, and the exponential is defined by spectral functional calculus. Almost everywhere in time, require $`n=n[\rho]`$ and require $`\rho(t)`$ to attain the constrained infimum $`\mathcal K(n(t))`$. For every real $`\varphi\in C^1([0,T];H^1_{\rm per}(I))`$ with $`\varphi(T)=0`$, require
```math
\int_0^T\!\int_I n\,\partial_t\varphi\,dx\,dt+
\int_I n_0\varphi(0)\,dx+
\int_0^T\!\int_I n\,\partial_x(A-V)\,\partial_x\varphi\,dx\,dt=0.
```
Finally, require the free-energy inequality
```math
\mathcal F(n(t))+\int_0^t\!\int_I
n(s,x)|\partial_x(A-V)(s,x)|^2\,dx\,ds
\le\mathcal F(n_0)
```
for almost every $`t\ge0`$. The question imposes no smallness condition on $`\mathcal F(n_0)-\min\mathcal F`$, and does not prescribe a positive lower bound uniform in time.

## References

Olivier Pinaud, *The quantum drift-diffusion model: Existence and exponential convergence to the equilibrium*, **Annales de l'Institut Henri Poincaré C** 36 (2019), 811–836, [doi:10.1016/j.anihpc.2018.10.002](https://doi.org/10.1016/j.anihpc.2018.10.002), [published PDF](https://www.numdam.org/item/10.1016/j.anihpc.2018.10.002.pdf). The explicit question of removing the initial smallness assumption is on printed page 813. Equations (3), (5)–(7), (16) and Theorem 3.1 specify the model and solution class. The formulation above fixes the allowed external potential to zero, fixes the mass to one, and asks for the energy inequality supplied as an equality in the theorem under its smallness hypothesis.

## Application

This quantum model represents semiconductor charge transport through a spatially nonlocal quantum equilibrium, coupled to the electrostatic potential. Global existence for large initial departures from equilibrium would extend the mathematical foundation beyond the perturbative regime.

## Status review


**Known cases:** The Matthes-Rott discrete limit identifies the nonlinear constitutive relation only while the limiting density is positive and omits self-consistent Poisson coupling. Fourth-order local DLSS contraction does not settle arbitrary-data global nonlocal quantum drift-diffusion-Poisson in the displayed Gibbs class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The Matthes-Rott discrete limit identifies the nonlinear constitutive relation only while the limiting density is positive and omits self-consistent Poisson coupling. Fourth-order local DLSS contraction does not settle arbitrary-data global nonlocal quantum drift-diffusion-Poisson in the displayed Gibbs class.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.anihpc.2018.10.002); [comparison source 2](https://www.numdam.org/item/10.1016/j.anihpc.2018.10.002.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves global weak existence when the initial relative free energy is small enough to maintain a positive lower density bound. The 2025 spatial discretization of Matthes–Rott treats a model without the self-consistent Poisson potential: it produces a global limit density, but identifies the quantum constitutive relation and the full evolution only on intervals where that limit stays strictly positive. Its authors explicitly state that loss of positivity for general data has not been excluded. This is different from global existence in the class above. Checked on 18 October 2026: bounded current-result and announcement searches, an independent selected-primary audit, semantic comparisons and the current all-status catalogue scan found no exact resolution or duplicate at their recorded extents. The extended-infimum definition above avoids asserting a finite-energy constrained minimizer for every nonnegative $`H^1`$ density; that overbroad wording in the source is not certified.

The [source packet](../FURTHER_problems/_tracking/parallel/continuum/nonlocal-qdd-poisson-large-data-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-nonlocal-qdd-poisson-review.json), [semantic comparison](../FURTHER_problems/_tracking/nonlocal-qdd-poisson-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/nonlocal-qdd-poisson-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/nonlocal-qdd-poisson-coordinator-review-2026-10-18.json) record evidence and limits. These AI checks do not assert human peer review or exhaustive proof verification.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7809cf78bf581b91**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
