# 1041. The Gell-Mann–Brueckner expansion for jellium in the thermodynamic limit

**Area:** Many-body physics, quantum information and wave analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider three-dimensional neutral Coulomb jellium with $`N`$ identical spinless fermions in a box $`\Lambda\subset\mathbb R^3`$, a uniform positive background of density $`\rho=N/|\Lambda|`$, and the fixed physical Coulomb interaction $`|x-y|^{-1}`$. Let $`e_J(\rho)`$ be the ground-state energy per unit volume after taking the thermodynamic limit at fixed $`\rho`$, including the background self-energy as in equation (1) of the report.

As $`\rho\to\infty`$, can one rigorously establish the predicted Gell-Mann–Brueckner correction through order $`\rho`$:
```math
e_J(\rho)=\frac35c_{\mathrm{TF}}\rho^{5/3}-c_{\mathrm D}\rho^{4/3}
       +c_1\rho\log\rho+c_2\rho+o(\rho),
```

with the corresponding predicted constants $`c_1,c_2`$ for this spinless model? The first two terms are established; the issue is a matching rigorous asymptotic for the correlation terms in the stated order of limits. The source specifies the structure of these terms but does not give numerical values for $`c_1,c_2`$, so none are asserted here.

## Application

The correction quantifies many-body electron correlation beyond the leading kinetic and exchange energies in the physical high-density regime. A proof would bridge rigorous mean-field results and the thermodynamic electron gas.

## References

1. François Visconti, *Ground state energy of a charged Fermi gas at high density*, in [*Oberwolfach Report 46/2025: Analysis of Many-body Quantum Systems*](https://doi.org/10.4171/OWR/2025/46), printed pp. 2533–2536, especially equations (1)–(2) and the open-question paragraph on p. 2536.
2. M. R. Christiansen, C. Hainzl and P. T. Nam, [*The Gell-Mann–Brueckner Formula for the Correlation Energy of the Electron Gas: A Rigorous Upper Bound in the Mean-Field Regime*](https://doi.org/10.1007/s00220-023-04672-2), *Communications in Mathematical Physics* **401** (2023), 1469–1529.
3. M. R. Christiansen, C. Hainzl and P. T. Nam, [*The Correlation Energy of the Electron Gas in the Mean-Field Regime*](https://arxiv.org/html/2405.01386v2), arXiv:2405.01386v2 (11 May 2026), cited by the report for its matching mean-field result.

## Status review


**Known cases:** The physical fixed Coulomb interaction is considered after the thermodynamic limit. The May 2026 mean-field theorem and author research account explicitly retain the distinction; neither proves these correlation terms in that order of limits.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The physical fixed Coulomb interaction is considered after the thermodynamic limit. The May 2026 mean-field theorem and author research account explicitly retain the distinction; neither proves these correlation terms in that order of limits.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The report explicitly says the Gell-Mann–Brueckner formula remains open for the thermodynamic limit. Its cited rigorous results put a density-dependent interaction prefactor on a fixed torus, so they do not establish the fixed-Coulomb thermodynamic expansion above. The latest arXiv version of the matching mean-field result and an independent exact-model audit confirm this difference. Bounded searches on 21 October 2026 found no complete matching announcement. This is a live-status assessment, not a proof of unsolvedness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f5341981fcc4d952**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
