# 675. Gradient propagation of smallness below codimension one

**Area:** Elliptic PDE and quantitative unique continuation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`n\ge3`$, a bounded connected domain $`\Omega\subset\mathbb R^n`$, and a real symmetric uniformly elliptic matrix field $`A`$ with Lipschitz entries. For $`s>0`$, use Hausdorff content
```math
\mathcal C_{\mathcal H}^{s}(E)=
\inf\left\{\sum_j r_j^s:E\subset\bigcup_j B(x_j,r_j)\right\}.
```

Given $`0<\delta\le2`$ and $`m,\rho>0`$, let $`E,K\subset\Omega`$ satisfy
```math
\mathcal C_{\mathcal H}^{n-2+\delta}(E)>m,\qquad
\mathrm{dist}(E,\partial\Omega)>\rho,\quad
\mathrm{dist}(K,\partial\Omega)>\rho.
```

Does there exist $`C>0`$ and $`\gamma\in(0,1)`$, depending only on $`n,\Omega,A,\delta,m,\rho`$, such that every real weak solution
```math
\mathrm{div}(A\nabla u)=0,\qquad
M=\sup_\Omega|\nabla u|<\infty,
```

satisfies
```math
\sup_K|\nabla u|\le
C\left(\sup_E|\nabla u|\right)^\gamma M^{1-\gamma}?
```

Use the continuous interior gradient representative. Constants must be independent of the solution and the particular sets beyond the stated data. The coefficient field is fixed; no additional uniformity over coefficient fields or solution-dependent frequency bound is imposed. The endpoint $`\delta=0`$ is excluded.

## Application

This asks whether small measurements of a solution's gradient on a sufficiently large thin set quantitatively control its gradient elsewhere. Such estimates underpin unique continuation, inverse problems and observability.

## References

1. A. Logunov and E. Malinnikova, [*Quantitative propagation of smallness for solutions of elliptic equations*](https://arxiv.org/html/1711.10076), §1.6 Question 1, Eq.(5), standing assumptions (7)–(8), and Theorem 5.1 (2017 preprint).
2. B. Foster and J. M. Gallegos, [*Propagation of smallness near codimension two for gradients of harmonic functions*](https://arxiv.org/html/2508.21214), Theorem 1, following discussion, and Corollary 3 (2025).
3. K. Le Balc'h and J. Martin, [*Quantitative propagation of smallness and spectral estimates for the Schrödinger operator*](https://arxiv.org/html/2403.15299), Theorem 3.4; *Journal of Spectral Theory* **15** (2025), 245–278. [DOI](https://doi.org/10.4171/JST/543).

## Status review


**Known cases:** The reopened Foster-Gallegos primary gives the power estimate for harmonic functions and only a stretched-logarithmic modulus with general Lipschitz coefficients. Its explicit nonanalytic-coefficient limitation matches the remaining target; later elliptic interface or planar results do not cover every n>=3 and every positive delta. No full matching result located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The reopened Foster-Gallegos primary gives the power estimate for harmonic functions and only a stretched-logarithmic modulus with general Lipschitz coefficients. Its explicit nonanalytic-coefficient limitation matches the remaining target; later elliptic interface or planar results do not cover every n>=3 and every positive delta. No full matching result located.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/2508.21214); [comparison source 2](https://arxiv.org/abs/1711.10076). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Foster and Gallegos prove the power estimate for harmonic functions. They explicitly distinguish the remaining nonanalytic-coefficient question. For Lipschitz coefficients, their Corollary 3 provides a weaker stretched-logarithmic modulus, rather than a fixed positive power of the smallness. The known near-codimension-one theorem does not reach every $`\delta>0`$ here.

The [coordinating review](../FURTHER_problems/_tracking/focused-C206-toric-and-Reznikov-two-precise-gates-C-20261028/ROOT-INDEPENDENT-THREE-MODEL-PRIMARY-CURRENT-AND-DUPLICATE-FINAL-REVIEW.json) and [independent model review](../FURTHER_problems/_tracking/focused-C206-gradient-codimension-two-C-20261028/A-INDEPENDENT-REAL-LIPSCHITZ-GRADIENT-CONTENT-QUANTIFIERS-AND-HARMONIC-VS-LOG-MODULUS-MODEL-PEER.json) record exact hypotheses, current-result comparisons and semantic duplicate checks. No matching complete resolution or announcement for the general coefficient class was located. The precise statement uses the official original preprint; no complete ICM-edition parity is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0fe39e7092b83fca**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
