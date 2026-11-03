# 834. Controlled global Coulomb gauges in ordinary Lorentz weak L4

**Area:** Gauge theory and geometric analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a compact Riemannian four-manifold $`(M,g)`$. For each finite $`\Lambda>0`$, does there exist $`C(M,\Lambda)<\infty`$ with the following property?

Every $`W^{1,2}`$ connection $`\nabla`$ on an $`\mathrm{SU}(2)`$ principal bundle over $`M`$, with $`\|F_\nabla\|_{L^2(M)}\le\Lambda`$, admits a global, possibly singular $`W^{1,(4,\infty)}`$ section as in Theorem A of [1], such that its connection form $`\alpha`$ satisfies

```math
d^*\alpha=0\quad\text{in distributions},\qquad
\|\alpha\|_{L^{4,\infty}(M)}\le C(M,\Lambda).
```

Here the norm is the ordinary Lorentz weak norm

```math
\|\alpha\|_{L^{4,\infty}(M)}
=\sup_{t>0} t\,\mathrm{Vol}_g\{x:|\alpha(x)|>t\}^{1/4}.
```

There is no curvature-smallness or Yang–Mills equation assumption. Singular sections are allowed; a smooth global trivialization and a prescribed singular set are not required.

## Application

Such a gauge would combine a global estimate controlled by curvature with an elliptic gauge condition, providing a useful analytic framework for compactness and geometric evolution problems with concentrated curvature.

## References

1. M. Petrache and T. Rivière, [Global gauges and global extensions in optimal spaces](https://doi.org/10.2140/apde.2014.7.1851), *Analysis & PDE* **7**(8) (2014). [Author manuscript](https://people.math.ethz.ch/~riviere/pdf/pub/petrache-riviere-global-gauge.pdf), Definition 1.2, Theorem A and Open Problem 1.3, pp.3–5.
2. Y. Wang, [Sharp Estimate of Global Coulomb Gauge](https://arxiv.org/html/1808.01685v1), *Communications on Pure and Applied Mathematics* **73**(12) (2020), 2556–2633, DOI [10.1002/cpa.21939](https://doi.org/10.1002/cpa.21939). Inspected preprint: Definition 1.1, Remark 1.2 and Theorem 1.2.
3. R. Caniato and T. Rivière, [Coulomb Gauges and Regularity for Stationary Weak Yang–Mills Connections in Supercritical Dimension](https://arxiv.org/pdf/2411.19910v3) (2025 revision), Appendix A, Propositions A.1–A.2.

## Status review


**Known cases:** The original global gauge theorem lacks the Coulomb condition; Wang controls a different integrability-radius space rather than the ordinary Lorentz norm. Small-curvature gauge estimates do not cover every finite curvature-energy bound. The conjunction requested remains unmatched.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The original global gauge theorem lacks the Coulomb condition; Wang controls a different integrability-radius space rather than the ordinary Lorentz norm. Small-curvature gauge estimates do not cover every finite curvature-energy bound. The conjunction requested remains unmatched.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Open Problem 1.3 asks for the conjunction displayed above. Theorem A of [1] gives the ordinary weak-L4 estimate without the Coulomb requirement. Wang supplies a Coulomb gauge controlled in a different space defined by an integrability radius, and explicitly states that this does not answer the ordinary Lorentz question. The later appendix results in [3] require small curvature; they do not cover arbitrary $`\Lambda`$.

Checks through 29 October 2026 found no matching complete resolution or announcement. The ordinary Lorentz norm and Wang's distinct function space were compared explicitly, together with the permissible singular section and the absence of a small-energy assumption.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b8fe9561e90cae5f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
