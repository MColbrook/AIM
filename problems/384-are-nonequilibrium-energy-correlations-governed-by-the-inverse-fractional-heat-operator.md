# 384. Are nonequilibrium energy correlations governed by the inverse fractional heat operator?

**Area:** Anomalous heat transport and stochastic lattice dynamics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Consider the harmonic-chain momentum-exchange model of Kundu and coauthors [1, Section 2]: $`N`$ nearest-neighbor harmonic oscillators, random exchanges of adjacent momenta, and Langevin heat baths at the endpoints with distinct temperatures $`T_L`$ and $`T_R`$. Let $`e_i`$ be its local energy and let $`\mathrm{Cov}_{N,\mathrm{NESS}}`$ denote covariance in its nonequilibrium stationary state.

The associated operator $`L`$ on $`(0,1)`$ is the finite-domain fractional operator in [1, equations (7)–(9)]. It acts diagonally on the Neumann cosine functions $`\phi_m(x)=\sqrt2\cos(m\pi x)`$, $`m\geq1`$, with eigenvalues $`(m\pi)^{3/2}`$, while its **Dirichlet-domain** eigenfunctions $`\psi_n`$ and eigenvalues $`\mu_n>0`$ come from restricting this action to functions vanishing at the endpoints. Thus $`L`$ here is not the standard spectral Dirichlet fractional Laplacian.

**Is there a constant $`\nu>0`$ for which, for interior $`x\ne y`$, the large-$`N`$ long-range stationary energy covariance obeys**

```math
\lim_{N\to\infty}N\mathrm{Cov}_{N,\mathrm{NESS}}
   (e_{\lfloor Nx\rfloor},e_{\lfloor Ny\rfloor})
 =\frac{(T_L-T_R)^2}{\nu}\sum_{n\geq1}
   \frac{\psi_n(x)\psi_n(y)}{\mu_n}\,?
```


The equivalent distributional formulation subtracts the local same-site term $`T_{\mathrm{NESS}}(x)^2\delta(x-y)`$ before comparing the covariance kernel with $`L^{-1}`$ [1, equation (57)]. The source fits $`\nu\approx3.77`$ in its numerical normalization; proving an exact value is not assumed here.

## Application

Anomalous heat transport couples distant parts of a material even in steady state. This conjecture asks whether the same nonlocal operator governing the temperature profile also determines the spatial shape of its energy fluctuations.

## Known results and scope

The source derives the finite-domain fractional description of the steady temperature and current and gives numerical evidence for the distinct long-range correlation formula [1, Section 4.4]. It explicitly leaves a proof open. The first author's 2019 thesis [2, p. 85] repeats this status. A finite-time macroscopic energy result for a related bath-coupled harmonic system [3] does not identify the stationary second-covariance kernel in this conjecture.

## References

1. A. Kundu, C. Bernardin, K. Saito, A. Kundu and A. Dhar, [*Fractional diffusion equation description of an open anomalous heat conduction set-up*](https://arxiv.org/pdf/1808.10870v1), arXiv:1808.10870v1 (2018), Section 2 and Section 4.4, equation (57); published in *Journal of Statistical Mechanics: Theory and Experiment* (2019), 013205, doi:10.1088/1742-5468/aaf630.
2. A. Kundu, [*Analytically tractable models of one-dimensional anomalous heat transport*](https://thesis.icts.res.in/download/download_pdf/16), PhD thesis, Tata Institute of Fundamental Research (2019), Chapter 4, p. 85.
3. T. Komorowski and S. Olla, [*Boundary Thermalization in Superdiffusive Energy Transport*](https://link.springer.com/article/10.1007/s11040-026-09586-8), *Mathematical Physics, Analysis and Geometry* **29** (2026), article 45, doi:10.1007/s11040-026-09586-8.

## Status review

The [primary-passage receipt](../FURTHER_problems/_tracking/hcme-ness-correlations-primary-passages-2026-10-21.json) and [later-result and duplicate audit](../FURTHER_problems/_tracking/hcme-ness-correlations-status-2026-10-21.json) record the model, operator and status limits. Bounded searches found no complete proof, counterexample or announced resolution through 21 October 2026; they cannot exclude unindexed work.


### Online recheck, 2026-10-30

The August boundary-thermalization work studies macroscopic superdiffusive transport, not the exact nonequilibrium fourth-order stationary energy covariance in the proposed inverse-operator formula. Neither a profile hydrodynamic limit nor local equilibrium proves that nonlocal covariance assertion.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/s11040-026-09586-8); [status source 2](https://arxiv.org/abs/1808.10870). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-39b05ae501f1b2b5** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
