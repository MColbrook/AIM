# 248. The Calabi–Croke inequality for smooth Riemannian two-spheres

**Area:** Riemannian geometry; geometric variational problems
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`g`$ be any smooth Riemannian metric on the closed two-sphere $`S^2`$. Write $`A(g)=\int_{S^2}dA_g`$ for its area, and define

```math
\ell_{\min}(g)=\inf\{\mathrm{Length}_g(\gamma):
\gamma\text{ is a nonconstant periodic }g\text{-geodesic}\}.
```

Periodic geodesics return with the same position and velocity. They need not be simple curves, and no noncontractibility condition is imposed.

**Question.** Does every such metric satisfy

```math
\ell_{\min}(g)^2\le 2\sqrt3\,A(g)?
```

There is no curvature, symmetry, convex-embedding or Zoll assumption. The metric is Riemannian and smooth everywhere. This question asks for the inequality, without an equality classification.

The constant is suggested by the singular sphere obtained by gluing two unit equilateral Euclidean triangles along their boundaries. Its area is $`\sqrt3/2`$ and its shortest periodic geodesic has length $`\sqrt3`$. This model is not itself a smooth metric in the quantified class.

## Application

This is an extremal question about how total area limits the length of the shortest periodic geodesic on a sphere. It asks for a sharp universal geometric bound without curvature information. No direct engineering application is asserted.

## References

1. A. Jabbour and S. Sabourau, *Sharp upper bounds on the length of the shortest closed geodesic on complete punctured spheres of finite area*, **Revista Matemática Iberoamericana 38** (2022), 1051–1065, [published PDF](https://ems.press/content/serial-article-files/39032), p.1052, equation (1.1) and surrounding discussion; [DOI](https://doi.org/10.4171/RMI/1362). The complete published text was read.
2. G. Buro and L. Merlin, *A Finsler counterexample to the Croke conjecture for the systolic ratio on the 2-sphere*, [arXiv:2106.01849v1](https://arxiv.org/pdf/2106.01849v1), pp.1–2, Theorem 1 and Remark 2, and §5. Its constructed Finsler metrics retain six singularities.
3. A. Abbondandolo and G. Benedetti, *On the local systolic optimality of Zoll contact forms*, **Geometric and Functional Analysis 33** (2023), 299–363, [published article](https://doi.org/10.1007/s00039-023-00624-z), Theorem 1 and Corollary 1.

## Status review

Reference [1] explicitly distinguishes this closed-sphere conjecture from its sharp theorem for complete three-punctured spheres. Removing points from a smooth closed metric does not produce a complete punctured metric, so that theorem is not an immediate proof of the displayed inequality.

The counterexample in [2] concerns a different metric class and retains singular points. It does not refute the smooth Riemannian statement. Reference [3] proves local optimality near Zoll metrics; it does not give the global bound over all metrics.

Bounded searches through 17 October 2026 located no matching proof, counterexample or complete announcement. The review packet records the primary statements and comparisons with retained AIM problems and announced results. Independent selected-primary review passed. All186cached catalogue pages were compared using six target aliases; the four returned contexts concern different questions.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/calabi-croke-smooth-sphere-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-calabi-croke-smooth-sphere-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/calabi-croke-prove2-0130-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/calabi-croke-coordinator-review-2026-10-17.json) record exact source and current-search coverage.


### Online recheck, 2026-10-30

The global smooth Riemannian S2 inequality is distinct from singular Finsler counterexamples, punctured-sphere sharp bounds and local Zoll optimality. The 2026 geodesic-dynamics primary discussion retains Calabi's bound as a conjecture.

Comparators and current-status sources: [status source 1](https://www.math.uchicago.edu/~wilkinso/papers/GDRFinalDraft1-16-2026.pdf); [status source 2](https://arxiv.org/abs/2106.01849); [status source 3](https://doi.org/10.1007/s00039-023-00624-z). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-b93463a5ef71e8ee** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
