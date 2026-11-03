# 884. Completeness under conformal changes of compact Lorentzian spaceforms

**Area:** Mathematical relativity / Lorentzian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a closed connected smooth manifold of dimension $`n\geq2`$, and let $`g_0`$ be a smooth Lorentzian metric of constant sectional curvature. For an arbitrary $`u\in C^\infty(M;\mathbb R)`$, set

```math
g=e^{2u}g_0.
```


**Must $`(M,g)`$ be geodesically complete?** Explicitly, for every $`x\in M`$ and $`v\in T_xM`$, must the maximal solution of

```math
\nabla^g_{\dot\gamma}\dot\gamma=0,\qquad \gamma(0)=x,\qquad \dot\gamma(0)=v
```


be defined for every affine parameter $`t\in\mathbb R`$?

The constant curvature assumption is on $`g_0`$; the rescaled metric need not have constant curvature. There is no homogeneity or Killing-field assumption on the compact quotient and no restriction to one sign of the constant curvature. The conformal factor is a single globally defined smooth positive function. Local conformal flatness alone is a different condition.

## Application

Conformal changes preserve light cones and unparameterized null trajectories, while geodesic completeness records whether freely moving trajectories persist for all affine times. This question isolates whether a smooth change of scale can create geodesic incompleteness on a compact Lorentzian spaceform. It is a mathematical model of the distinction between causal structure and affine dynamics, without a claim that compact Lorentzian manifolds describe a physical universe.

## Known cases and limitations

The constant-curvature metric $`g_0`$ is complete. Null completeness is preserved by smooth conformal changes on a compact manifold, because the parameter-change factor is bounded above and away from zero. The question therefore concerns possible timelike or spacelike incompleteness.

Completeness is also known when the rescaled metric is globally conformal to a compact homogeneous Lorentzian metric, or admits an everywhere timelike conformal Killing field. Constant curvature gives local homogeneity, which does not supply either global hypothesis automatically on a compact quotient. The existence of incomplete compact Lorentzian metrics by itself does not provide a counterexample in this globally prescribed conformal class.

## References

1. M. Sánchez, *On the completeness of trajectories for some mechanical systems*, in *Geometry, Mechanics, and Dynamics*, Fields Institute Communications **73** (2015), 343–372. [Eligible author version](https://arxiv.org/abs/1303.6150), v2, §4.4, Question 1, physical p.24, and Theorems 6–8, pp.21–22. Exact author version checked; full published chapter not compared.
2. K. Burns and V. S. Matveev, *Open problems and questions about geodesics*, Ergodic Theory and Dynamical Systems **41** (2021), 641–684. [Eligible author version](https://arxiv.org/abs/1308.5417), v3, §9.3, Question 9.3.2, physical p.27. Restates the same question.
3. A. Burtscher, *A conformal Hopf–Rinow theorem for semi-Riemannian spacetimes*. [Latest checked author version](https://arxiv.org/abs/2309.08682), v5 (2025), introduction, Theorems 1.2 and 1.6 and the discussion of geodesic completeness. The result concerns completeness of a null-distance metric and global hyperbolicity; it does not give full geodesic completeness in the question above.

## Status review


**Known cases:** Null completeness is conformally preserved here, while full affine geodesic completeness is stronger. Timelike conformal Killing fields or global homogeneous metrics are additional assumptions not implied by local constant curvature on a compact quotient. Null-distance completeness is another conclusion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Null completeness is conformally preserved here, while full affine geodesic completeness is stronger. Timelike conformal Killing fields or global homogeneous metrics are additional assumptions not implied by local constant curvature on a compact quotient. Null-distance completeness is another conclusion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The exact question is stated in both source surveys. Bounded literature and announcement searches on 17 October 2026 located no complete proof or counterexample for this precise global conformal class. General null-distance completeness theorems and results on compact manifolds with special Killing fields have different conclusions or hypotheses. Independent selected-primary review passed. All 186 cached catalogue pages were checked with five target aliases, with no matches. This is a listing-description comparison, not every mission proof.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/conformal-lorentz-completeness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-conformal-lorentz-completeness-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/conformal-lorentz-completeness-duplicate-snapshot.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/conformal-lorentz-prove2-0134-review.json) and [coordinator review](../FURTHER_problems/_tracking/conformal-lorentz-coordinator-review-2026-10-17.json) record evidence and version limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f023bd067be9fed5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
