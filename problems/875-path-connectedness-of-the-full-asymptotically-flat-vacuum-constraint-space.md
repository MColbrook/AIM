# 875. Path connectedness of the full asymptotically flat vacuum constraint space

**Area:** Mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`0<\alpha<1`$ and the standard coordinates on $`\mathbb R^3`$. Write $`\delta`$ for the Euclidean metric. Let $`\mathcal C_\alpha`$ consist of pairs $`(g,k)`$, where $`g`$ is a positive-definite Riemannian metric and $`k`$ is a symmetric covariant two-tensor, satisfying

```math
g-\delta\in C^{2,\alpha}_{-1},\qquad k\in C^{1,\alpha}_{-2},
```

and the vacuum Einstein constraint equations with zero cosmological constant,

```math
R_g+(\mathrm{tr}_g k)^2-|k|_g^2=0,
\qquad
\mathrm{div}_g\bigl(k-(\mathrm{tr}_g k)g\bigr)=0.
```

These equations are understood classically with the displayed local Hölder regularity. Give $`\mathcal C_\alpha`$ the topology induced by $`C^{2,\alpha}_{-1}\times C^{1,\alpha}_{-2}`$, without quotienting by coordinate changes.

For completeness, $`C^{m,\alpha}_{-q}`$ means finite weighted Hölder norm, applied componentwise to tensors. One choice of norm, with $`\rho(x)=(1+|x|^2)^{1/2}`$ and Euclidean derivatives, is

```math
\sum_{j=0}^{m}\sup_x\rho(x)^{j+q}|D^ju(x)|
+\sup_{x\ne y}\min\{\rho(x),\rho(y)\}^{m+\alpha+q}
\frac{|D^m u(x)-D^m u(y)|}{|x-y|^\alpha}.
```

**Is $`\mathcal C_\alpha`$ path connected for every fixed $`\alpha\in(0,1)`$?** Equivalently, can every pair be joined to $`(\delta,0)`$ by a path of vacuum solutions continuous in these weighted norms?

No condition $`\mathrm{tr}_gk=0`$ is imposed. The manifold has one asymptotically flat end and no boundary. This is the path-connectedness part of [1, Open Problem 4.18]. Its momentum variable $`\pi=k-(\mathrm{tr}_gk)g`$ gives the same topology: in three dimensions $`k=\pi-\tfrac12(\mathrm{tr}_g\pi)g`$.

## Application

The constraints describe admissible initial states for the vacuum Einstein evolution. Path connectedness asks whether these states can be continuously deformed into the Euclidean initial state while preserving both constraint equations and the specified asymptotic behavior [1, 2]. It concerns the global structure of the constraint space.

## References

1. A. Carlotto, [*The general relativistic constraint equations*](https://doi.org/10.1007/s41114-020-00030-z), *Living Reviews in Relativity* **24** (2021), 2; current publisher PDF notes corrected publications in 2022 and 2024. Open Problem 4.18, actual PDF p. 123, and Appendix B.
2. F. C. Marques, [*Deforming three-manifolds with positive scalar curvature*](https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n2-p03-p.pdf), *Annals of Mathematics* **176** (2012), 815–863, [DOI](https://doi.org/10.4007/annals.2012.176.2.3). Theorem 1.4, the following full-space discussion, and Section 9 (weighted norms p. 855 and Theorem 9.7).
3. A. Carlotto and C. Li, [*Constrained deformations of positive scalar curvature metrics, II*](https://doi.org/10.1002/cpa.22153), *Communications on Pure and Applied Mathematics* **77** (2024), 795–862. Theorem 1.5 and Section 7, especially the trace-free hypothesis in the definition preceding Proposition 7.15.
4. R. Gicquaud and J. Glöckle, [*On the topology of the space of vacuum initial data sets*](https://arxiv.org/abs/2609.39987v1), arXiv:2609.39987v1 (30 September 2026). Theorem 1.1 and the discussion following its proof concern closed manifolds; this is a current-status comparator.

## Status review


**Known cases:** Maximal-data path connectedness and contractibility retain trace-free extrinsic curvature. The recent high-dimensional closed-manifold topology theorem concerns another manifold and topology. No path from arbitrary nonmaximal one-ended data into the maximal subspace is supplied.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Maximal-data path connectedness and contractibility retain trace-free extrinsic curvature. The recent high-dimensional closed-manifold topology theorem concerns another manifold and topology. No path from arbitrary nonmaximal one-ended data into the maximal subspace is supplied.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. Marques proves path connectedness of the **maximal** subspace, which requires $`\mathrm{tr}_gk=0`$ [2]. The later contractibility theorem [3] also retains that condition and works in its stated weighted Sobolev setting. These results do not supply paths from arbitrary nonmaximal data into that subspace.

The recent topology theorem [4] concerns closed spin manifolds in dimension at least six and nontrivial higher homotopy groups. It does not settle path connectedness for one-ended data on $`\mathbb R^3`$.

The formulation, independent selected-primary audit, announcement comparisons and scoped catalogue checks passed. These are dated literature checks; the review records distinguish selected passages from full-paper reading.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/af-vacuum-path-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-af-vacuum-path-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/af-vacuum-path-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/af-vacuum-path-prove2-0151-review.json) and [coordinator review](../FURTHER_problems/_tracking/af-vacuum-path-coordinator-review-2026-10-17.json) record the evidence and its limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-626315d0cecdf3ff**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
