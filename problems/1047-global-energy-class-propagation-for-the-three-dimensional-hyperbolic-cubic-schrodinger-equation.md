# 1047. Global energy-class propagation for the three-dimensional hyperbolic cubic Schrödinger equation

**Area:** Nonlinear waves, fluids and kinetic equations; dispersive PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`L=\partial_{x_1}^2+\partial_{x_2}^2-\partial_z^2`$ on $`\mathbb R^3`$. For every complex-valued $`u_0\in H^1(\mathbb R^3)`$, consider

```math
i\partial_tu+Lu+|u|^2u=0,\qquad u(0)=u_0.
```

Write $`[0,T_{\max})`$ for the maximal forward interval of its standard local mild solution, with

```math
u\in C([0,T_{\max});H^1(\mathbb R^3))
\cap L^{8/3}_{\mathrm{loc}}([0,T_{\max});W^{1,4}(\mathbb R^3)),
```

and the Duhamel identity

```math
u(t)=e^{itL}u_0+i\int_0^t e^{i(t-s)L}(|u(s)|^2u(s))\,ds.
```

Prove or disprove that $`T_{\max}=\infty`$ for every such datum. Equivalently, can the finite-time $`H^1`$ blow-up alternative ever occur? The domain is the full Euclidean space in all three spatial directions; no symmetry, smallness, or periodic direction is assumed.

## Application

Normal group-velocity dispersion in a Kerr optical medium produces one dispersive direction with the opposite sign to the two transverse directions. This question tests whether that mixed dispersion can prevent finite-time collapse for arbitrary finite-energy pulse envelopes.

## References

1. É. Dumas, D. Lannes and J. Szeftel, *Variants of the Focusing NLS Equation: Derivation, Justification, and Open Problems Related to Filamentation*, in *Laser Filamentation*, Springer (2016), pp.19–75, §4.2, equation(69), Open Problem6; [author-hosted final chapter](https://david-lannes.perso.math.cnrs.fr/wp-content/uploads/2019/01/dumaslannesszeftel.pdf), printed61–62; [eligible preprint](https://arxiv.org/abs/1405.7308v2), pp.33–34; [chapter DOI](https://doi.org/10.1007/978-3-319-23084-9_2).
2. J.-C. Saut and Y. Wang, [*On the hyperbolic nonlinear Schrödinger equations*](https://doi.org/10.1186/s13662-024-03811-w), *Advances in Continuous and Discrete Models* (2024), article15, equations(1.9), §2.1 and Open Problem2.

## Status review


**Known cases:** The dispersion has two positive and one negative spatial direction on full R3. Elliptic focusing/defocusing cubic theorems, hyperbolic-space geometry and a solution constant in one infinite direction do not settle arbitrary H1 data here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The dispersion has two positive and one negative spatial direction on full R3. Elliptic focusing/defocusing cubic theorems, hyperbolic-space geometry and a solution constant in one infinite direction do not settle arbitrary H1 data here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This is the three-dimensional component of the cited global-existence question. AIM421 concerns the planar equation and asks for global $`L^2`$ scattering; it does not cover this three-dimensional energy-class target. The 2024 review explicitly retains the arbitrary-large-data three-dimensional question.

The conserved gradient energy has opposite signs and does not bound the full $`H^1`$ norm. Linear Strichartz estimates yield local well-posedness, but do not supply the missing large-data global bound. A solution constant in the negative-dispersion coordinate has infinite $`L^2(\mathbb R^3)`$ norm unless it vanishes, so a planar focusing blow-up inserted into a periodic direction does not directly settle this full-space problem.

Selected current-source, semantic, independent and catalogue checks through 18 October 2026 found no matching full resolution. Recent periodic, mixed-domain and fractional-dispersion results have different hypotheses. Only the three-dimensional component is added here. The rest of the final 2016 chapter remains a version-coverage gap.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/hyperbolic-nls3d-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-hyperbolic-nls3d-review.json), [semantic comparison](../FURTHER_problems/_tracking/hyperbolic-nls3d-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/hyperbolic-nls3d-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/hyperbolic-nls3d-coordinator-review-2026-10-18.json) record the checked scope and access limits. These are AI checks, not human peer review or certification of all cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-58f9f6cf3a0d2d73**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
