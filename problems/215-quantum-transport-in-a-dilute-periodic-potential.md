# 215. Quantum transport in a dilute periodic potential

**Area:** Spectral theory, quantum dynamics and kinetic limits
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`d\ge2`$, a real $`W\in\mathcal S(\mathbb R^d)`$ and $`\lambda>0`$. On $`L^2(\mathbb R^d)`$ put
```math
V_r(x)=\sum_{m\in\mathbb Z^d}W((x+m)/r),\quad
H_r=-\frac{r^2}{8\pi^2}\Delta+\lambda V_r,\quad
U_r(s)=e^{-2\pi i sH_r/r}.
```

For a phase-space symbol $`a`$, define
```math
D_ra(x,y)=r^{d^2/2}a(r^{d-1}x,ry),\qquad Q_r(a)=\mathrm{Op}(D_ra),
```

where $`\mathrm{Op}(c)`$ has kernel
```math
\int_{\mathbb R^d}c((x+x')/2,y)e^{2\pi i(x-x')\cdot y}\,dy.
```

Do linear maps $`L_{W,\lambda}(t):L^1(\mathbb R^{2d})\to L^1(\mathbb R^{2d})`$ exist such that, for all $`t>0`$ and $`a,b\in\mathcal S(\mathbb R^{2d})`$,
```math
\lim_{r\downarrow0}\mathrm{Tr}\!\left[
 U_r(tr^{1-d})Q_r(a)U_r(tr^{1-d})^*Q_r(b)^*
\right]
=\int_{\mathbb R^{2d}}(L_{W,\lambda}(t)a)\,\overline b\,dx\,dy?
```

This is the existence component (i) of Griffin–Marklof Conjecture 1.1, with wavelength $`h=r`$ and fixed coupling. No damping or unproved lattice-statistics assumption is imposed.

## Application

The limit would justify a macroscopic transport description of wavepackets moving through a dilute crystal directly from microscopic quantum dynamics.

## References

1. J. Griffin and J. Marklof, [*Quantum transport in a low-density periodic potential: homogenisation via homogeneous flows*](https://arxiv.org/html/1805.06860), v2 (2019), Equations (1.2)–(1.11), Conjecture 1.1(i) and Theorem 1.1. *Pure and Applied Analysis* **1** (2019), 571–614; [DOI](https://doi.org/10.2140/paa.2019.1.571).
2. J. Griffin and J. Marklof, [*Quantum Transport in a Crystal with Short-Range Interactions: The Boltzmann–Grad Limit*](https://doi.org/10.1007/s10955-021-02797-z), *Journal of Statistical Physics* **184** (2021), 16, Theorem 1, Assumption 1 and Section 12.
3. J. Griffin, [*Derivation of the Linear Boltzmann Equation from the Damped Quantum Lorentz Gas with a General Scatterer Configuration*](https://doi.org/10.1007/s00023-022-01230-9), *Annales Henri Poincaré* **24** (2023), 843–869, Theorem 1 and its following limit-order discussion.

## Status review


**Known cases:** The low-density periodic quantum limit is known to low perturbative orders or conditional on lattice statistics, and with added damping. These are not the unconditional fixed-coupling h=r trace limit in the target.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Reference 1 proves convergence of the first three coupling-expansion coefficients; its remainder does not establish the fixed-coupling limit. Reference 2 derives a full random-flight model under an unproved Poisson-replacement assumption. Reference 3 includes damping and takes the two limits in a different order. Neither settles the displayed unconditional statement.

The source additionally predicts that the limiting transport generally differs from the linear Boltzmann equation. That separate prediction is not assumed here. The [coordinating review](../FURTHER_problems/_tracking/focused-periodic-quantum-transport-C193-Root-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records current-resolution, announcement and all-status semantic duplicate checks, with independent scaling review. Bounded checks do not prove continued openness.


### Online recheck, 2026-10-30

The low-density periodic quantum limit is known to low perturbative orders or conditional on lattice statistics, and with added damping. These are not the unconditional fixed-coupling h=r trace limit in the target.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1805.06860); [status source 2](https://arxiv.org/abs/2012.15312); [status source 3](https://doi.org/10.1007/s00023-022-01230-9). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-de737947d0dffb87** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
