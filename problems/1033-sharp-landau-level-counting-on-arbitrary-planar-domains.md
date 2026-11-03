# 1033. Sharp Landau-level counting on arbitrary planar domains

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a nonempty open set with $`0<|\Omega|<\infty`$, and let $`B>0`$. Set $`A(x)=\tfrac12(-x_2,x_1)`$ and let $`H_{B,\Omega}^{\mathrm D}`$ be the Dirichlet magnetic Laplacian $`(-i\nabla-BA)^2`$: its quadratic form is the closure of

```math
q_B[u]=\int_\Omega|(-i\nabla-BA)u|^2\,dx,\qquad u\in C_c^\infty(\Omega),
```


in the magnetic form norm. Write $`N_\Omega(B,\lambda)`$ for its number of eigenvalues **strictly below** $`\lambda`$, counted with multiplicity.

Is it true, for every such $`\Omega`$, every $`B>0`$ and every $`\lambda>0`$, that

```math
N_\Omega(B,\lambda)\le \frac{B|\Omega|}{2\pi}\,\#\{k\in\mathbb Z_{\ge0}:B(2k+1)<\lambda\}\,?
```


The right side is the area times the integrated density of states of the full-plane Landau Hamiltonian. Both counting conventions are strict, including when $`\lambda`$ is a Landau level. The potential is the restriction of the displayed globally defined symmetric gauge; extra Aharonov–Bohm fluxes are not part of the question.

## Application

This would give a sharp area bound on the number of confined quantum states below any energy in a constant perpendicular magnetic field. Integrating the counting inequality also gives the corresponding Landau-level bounds for positive-order Riesz means.

## Known results and scope

Frank, Loss and Weidl prove this counting bound for finite-area tiling domains and explicitly ask whether it extends to arbitrary domains. For arbitrary finite-area domains they establish the associated Riesz-mean bound at orders $`\gamma\ge1`$; their counterexamples to a different, field-independent semiclassical constant do not disprove the displayed Landau-level bound.

The latest checked Frank–Larson–Pfeiffer preprint strengthens the arbitrary-domain Landau-level estimate at $`\gamma\ge1`$, with a remainder. Its theorem does not cover the counting order $`\gamma=0`$. Recent nonmagnetic Pólya announcements concern $`-\Delta`$ rather than this constant-field estimate.

## References

1. R. L. Frank, M. Loss and T. Weidl, [*Pólya’s conjecture in the presence of a constant magnetic field*](https://ems.press/content/serial-article-files/31694?nt=1#page=5), *Journal of the European Mathematical Society* **11** (2009), no. 6, 1365–1383, [doi:10.4171/JEMS/184](https://doi.org/10.4171/JEMS/184). Definitions and magnetic symbol on printed p. 1368; Theorem 2.2, equations (2.6)–(2.9), and the question on printed p. 1369.
2. R. L. Frank, S. Larson and P. Pfeiffer, [*Improved semiclassical eigenvalue estimates for the Laplacian and the Landau Hamiltonian*](https://arxiv.org/html/2502.02388v2), arXiv:2502.02388v2 (6 December 2025), Theorem 2.

## Status review


**Known cases:** The assertion is the exact Landau-level counting bound on every finite-area open set. Tiling classes, nonmagnetic Polya bounds and positive-order Riesz means do not give the arbitrary-domain zeroth-order bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The assertion is the exact Landau-level counting bound on every finite-area open set. Tiling classes, nonmagnetic Polya bounds and positive-order Riesz means do not give the arbitrary-domain zeroth-order bound.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 24 October 2026. Bounded current and announcement searches found no matching solution, and the closest AIM and FURTHER targets concern different operators, Riesz orders or shape comparisons. The live Prove2Me page timed out; indexed searches found no matching entry. These checks cannot rule out unindexed work.

The [dated independent review](../FURTHER_problems/_tracking/JEMS184-Landau-counting-independent-coordinator-admission-review-20261024.json) records the source, current-result and duplicate comparisons.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f336bd4505867e25**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
