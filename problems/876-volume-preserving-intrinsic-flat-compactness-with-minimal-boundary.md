# 876. Volume-preserving intrinsic-flat compactness with minimal boundary

**Area:** Scalar geometry and mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix positive constants $`D,V,A`$. Let $`(M_j,g_j)`$ be any sequence of smooth compact connected oriented Riemannian three-manifolds with smooth nonempty boundary. Assume
```math
\mathrm{Scal}_{g_j}\ge0,\qquad
\mathrm{diam}_{g_j}(M_j)\le D,\qquad
\mathrm{Vol}_{g_j}(M_j)\le V,\qquad
\mathrm{Area}_{g_j}(\partial M_j)\le A.
```
Every boundary component is minimal and weakly stable. Explicitly, its mean curvature is zero and
```math
\int_{\Sigma}\bigl(|\nabla_{\Sigma}\phi|^2-
(|\mathrm{II}_{\Sigma}|^2+\mathrm{Ric}_{g_j}(\nu,\nu))\phi^2\bigr)\,d\mu_{\Sigma}\ge0
\quad\text{for every }\phi\in C^\infty(\Sigma).
```
Here $`\nu`$ is a unit normal to the boundary. Assume also that the interior of $`M_j`$ contains no smooth closed embedded minimal surface; no orientability condition is imposed on a hypothetical interior surface.

Give $`M_j`$ its intrinsic length distance $`d_j`$, using curves in $`M_j`$, and the three-dimensional integral current $`T_j`$ obtained by integration with the chosen orientation. Is there a subsequence and a three-dimensional integral current space $`M_\infty=(X_\infty,d_\infty,T_\infty)`$, possibly the zero current space, such that
```math
d_{\mathcal F}\bigl((M_{j_k},d_{j_k},T_{j_k}),M_\infty\bigr)\longrightarrow0,
\qquad
\mathrm{Vol}_{g_{j_k}}(M_{j_k})\longrightarrow\mathbf M(T_\infty)?
```
The distance $`d_{\mathcal F}`$ is the Sormani–Wenger intrinsic flat distance, defined by taking flat distances after distance-preserving embeddings into a common complete metric space. The quantity $`\mathbf M`$ is Ambrosio–Kirchheim mass, including the limit current's multiplicity and metric area factor. No positive lower volume bound is imposed. Weak stability allows a zero eigenvalue in the second variation; strict stability or global area minimization is not required.

## Application

Minimal surfaces represent horizons in time-symmetric mathematical relativity. This question asks whether regions without interior horizons can lose volume through cancellation in a weak geometric limit. Volume preservation also helps control limiting volumes of balls and spectral quantities.

## References

1. Christina Sormani and participants at the IAS workshop, [*Conjectures on Convergence and Scalar Curvature*](https://arxiv.org/abs/2103.10093v1), Conjecture 5.1, equations (101)–(103) and the following paragraph, pp. 29–30; Sections 3.1 and 3.3 give current and volume conventions. The question above retains only volume preservation, with connectedness and nonempty boundary explicit.
2. Stefan Wenger, [*Compactness for manifolds and integral currents with bounded diameter and volume*](https://doi.org/10.1007/s00526-010-0346-y), Calculus of Variations and Partial Differential Equations **40** (2011), 423–448, Theorem 1.2. The source survey states its application to this class.
3. Brian Allen and Edward Bryden, [*Volume above distance below with boundary II*](https://doi.org/10.1007/s10455-025-09989-w), Annals of Global Analysis and Geometry **67** (2025), 12; [preprint](https://arxiv.org/abs/2406.11541v1), Theorem 1.1. This requires volume convergence and comparison to a prescribed smooth metric as hypotheses.
4. Liam Mazurowski and Xuan Yao, [*Scalar curvature under weak limits of manifolds*](https://arxiv.org/abs/2605.03136v1), Theorem 1 (2026). This concerns scalar-curvature preservation for closed manifolds, with total volume convergence already assumed.

## Status review


**Known cases:** Wenger compactness gives a convergent subsequence but only lower semicontinuity of mass. Later scalar-preservation or boundary-VADB results assume volume convergence; they cannot establish the missing equality here. Drawstring counterexamples in other geometries do not satisfy the full minimal-boundary and no-interior-minimal-surface hypotheses.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Wenger compactness gives a convergent subsequence but only lower semicontinuity of mass. Later scalar-preservation or boundary-VADB results assume volume convergence; they cannot establish the missing equality here. Drawstring counterexamples in other geometries do not satisfy the full minimal-boundary and no-interior-minimal-surface hypotheses.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Wenger's theorem already gives an intrinsic-flat convergent subsequence under the diameter, volume and boundary-area upper bounds. Lower semicontinuity gives only

```math
\mathbf M(T_\infty)\le\liminf_{k\to\infty}\mathrm{Vol}_{g_{j_k}}(M_{j_k}).
```

The requested equality is additional. The source explicitly singles out volume preservation as a useful question in its own right. Its broader conjecture also asks for geodesic, tangent-cone and generalized scalar-curvature properties, which this entry does not request.

The boundary VADB theorem [3] and the 2026 scalar-preservation theorem [4] assume volume convergence to a prescribed limit. They therefore do not supply the missing volume equality here. Selected current drawstring examples preserve volume and concern closed manifolds; selected warped-product compactness theorems impose a special closed-product geometry. No matching complete resolution was located in the recorded bounded searches.

The [source and current review](../FURTHER_problems/_tracking/parallel/continuum/nomin-boundary-volume-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-nomin-boundary-volume-review.json), [semantic comparison](../FURTHER_problems/_tracking/nomin-volume-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/nomin-volume-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/nomin-volume-coordinator-review-2026-10-19.json) record the checks and their limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-656a9c8e684532af**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
