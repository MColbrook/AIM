# 1062. Late-time local mass and kinetic energy of Hartree atoms

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`Z>0`$. For any $`u_0\in H^1(\mathbb R^3;\mathbb C)`$, let $`u`$ be the global energy-space solution of

```math
i\partial_tu=-\Delta u-\frac Z{|x|}u+
\bigl(|\cdot|^{-1}*|u|^2\bigr)u,\qquad u(0)=u_0.
```


Define the set of stationary states

```math
\mathcal A_Z=\left\{\phi\in H^1(\mathbb R^3;\mathbb C):
-\Delta\phi-\frac Z{|x|}\phi+
\bigl(|\cdot|^{-1}*|\phi|^2\bigr)\phi=\lambda\phi
\text{ for some }\lambda\le0\right\},
```


where the equation is understood distributionally. Set

```math
M_Z=\sup_{\phi\in\mathcal A_Z}\|\phi\|_2^2,
\qquad K_Z=\sup_{\phi\in\mathcal A_Z}\|\nabla\phi\|_2^2.
```


These constants are finite. Must both inequalities

```math
\limsup_{t\to\infty}\int_{|x|\le r}|u(t,x)|^2\,dx\le M_Z,
\qquad
\limsup_{t\to\infty}\int_{|x|\le r}|\nabla u(t,x)|^2\,dx\le K_Z
```


hold for every $`u_0`$ and every $`r>0`$? This is published Conjecture 3 of [1]. The stationary set includes excited states, and the target has no radial or small-data restriction.

## Application

In this repulsive Hartree model of an atom, the nucleus attracts the electron density while that density repels itself. The question bounds the amount of matter and kinetic energy that can remain near the nucleus at late times, independently of the initial total mass and energy.

## References

1. E. Lenzmann and M. Lewin, [*Dynamical ionization bounds for atoms*](https://msp.org/apde/2013/6-5/apde-v6-n5-p07-p.pdf), *Analysis & PDE* **6**(5) (2013), 1183–1211, [DOI](https://doi.org/10.2140/apde.2013.6.1183). Equations (1-1), (1-3), (1-4), Conjecture 3 and Theorem 4, pp. 1184–1188. [Original arXiv record](https://arxiv.org/abs/1207.6898).

## Status review


**Known cases:** The target uses unaveraged late-time limsups bounded by actual stationary suprema for the nuclear Hartree equation. Time-averaged ionization estimates and other scattering models do not imply it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target uses unaveraged late-time limsups bounded by actual stationary suprema for the nuclear Hartree equation. Time-averaged ionization estimates and other scattering models do not imply it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. No proof or announced complete solution matching this target was found in bounded current searches. Theorem 4 of [1] gives time-averaged bounds; it does not establish these limsups. The kinetic target uses the actual stationary supremum $`K_Z`$.

The 2026 mass-critical Hartree scattering result concerns $`|x|^{-2}`$ interactions without a nuclear potential; the long-range linear scattering result also does not supply these bounds. Existing AIM 098/099 concern static fermionic atoms or molecules, AIM 201 concerns pseudo-relativistic boson-star uniqueness, and AIM 441 concerns a different coupled laser model. No equivalent target was found among admitted, pending or rejected FURTHER findings.

The [coordinator review](../FURTHER_problems/_tracking/hartree-dynamical-ionization-coordinator-review-2026-10-23.json), [independent review](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/hartree-dynamical-ionization-independent-bounded-check-20261023.json) and [all-status duplicate audit](../FURTHER_problems/_tracking/hartree-dynamical-ionization-all-status-duplicates-2026-10-23.json) record the exact passages, current source comparisons and search limits. These are selected-passage and status reviews, not exhaustive absence certificates or complete proof audits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e1032734b6c12b57**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
