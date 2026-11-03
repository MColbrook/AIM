# 385. Scalar geodesic tomography on nontrapping surfaces with conjugate points

**Area:** Geometric inverse problems / tomography
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a compact connected smooth Riemannian surface with nonempty smooth boundary. Assume the boundary is strictly convex: with outward unit normal $`\nu`$, its second fundamental form $`g(\nabla_w\nu,w)`$ is positive for every nonzero boundary tangent vector $`w`$. Assume also that every unit-speed geodesic issued from the interior meets the boundary in finite time in both time directions. Conjugate points in the interior are allowed.

For every maximal unit-speed geodesic $`\gamma:[0,\ell_\gamma]\to M`$ with boundary endpoints, and every real $`f\in C^\infty(M)`$ (smooth up to the boundary), define

```math
I_0f(\gamma)=\int_0^{\ell_\gamma}f(\gamma(t))\,dt.
```

**Does $`I_0f(\gamma)=0`$ for every such geodesic imply $`f\equiv0`$ on $`M`$?** The metric is known, and the transform is unweighted and unattenuated. The question is qualitative injectivity for every metric with the stated geometry.

## Application

These measurements model integrating a scalar density or perturbation along rays in a known medium. Interior focusing produces conjugate points, which can occur even when every ray exits. The question asks whether full ray data still distinguish all smooth scalar densities.

## Known scope and relationship to existing problems

This is Open problem 5 in Chapter 15 of the source book. The simple-surface case, which excludes conjugate points, is known. Injectivity is also proved for real-analytic nontrapping surface geometry, and for piecewise constant unknowns under the stated smooth geometry. Neither result covers arbitrary smooth functions on arbitrary smooth metrics. Injectivity on piecewise constants cannot be extended merely by taking a dense limit without an appropriate uniform inverse estimate.

AIM 119 asks for a local theorem using only short rays near a convex boundary point. The book explains that such a local theorem would imply the present global result by layer stripping; this global question does not require that stronger local-data theorem. AIM 120 instead asks to recover the unknown metric from nonlinear lens data. A nonlinear uniqueness assertion alone does not imply injectivity of its linearization. AIM 056 concerns higher-dimensional tensor fields.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions*, Cambridge University Press, 2023, Chapter 15, §15.1, Open problem 5. [DOI](https://doi.org/10.1017/9781009039901). Exact question checked in the [author manuscript](https://users.jyu.fi/~salomi/pub/GIP2D_driver.pdf), printed p. 339 / PDF p. 355; final published body not compared.
2. M. Mazzucchelli, M. Salo and L. Tzou, *A general support theorem for analytic double fibration transforms*, [arXiv:2306.05906v1](https://arxiv.org/abs/2306.05906v1), 2023, Theorem 1.4. [Author PDF](https://users.jyu.fi/~salomi/pub/MazzucchelliSaloTzou2023.pdf).
3. J. Ilmavirta and J. Railo, *Geodesic ray transform with matrix weights for piecewise constant functions*, Ann. Acad. Sci. Fenn. Math. 45 (2020), 1095–1102, Theorem 1.1 and Table 1. [Published PDF](https://www.acadsci.fi/mathematica/Vol45/vol45pp1095-1102.pdf), [DOI](https://doi.org/10.5186/aasfm.2020.4558).
4. H. Chihara, S. R. Jathar and J. Railo, *The matrix weighted real-analytic double fibration transforms*, Annales Fennici Mathematici 51 (2026), 353–376; [arXiv:2506.24067v2](https://arxiv.org/abs/2506.24067v2), Corollary 1.6. [DOI](https://doi.org/10.54330/afm.185114). Latest preprint statement checked; final publisher body inaccessible during this review.

## Status review


**Known cases:** Real-analytic or piecewise-constant injectivity, higher-dimensional convex-foliation results and microlocal cancellation of singularities do not prove qualitative unweighted injectivity for every smooth nontrapping surface allowing conjugate points.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Current primary texts were checked on 17 October 2026. The 2026 matrix-weighted result retains real-analytic geometry, and its introduction still identifies the smooth nontrapping conjecture. Recent microlocal results about cancellation of singularities do not themselves produce either an exact nonzero smooth kernel or general injectivity. No matching complete proof or counterexample was located in the bounded current search. Independent review passed, and all 24 matching windows in the 186-page catalogue scan concerned other questions. The [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/nontrapping-scalar-review.json) records exact extents and access gaps.

[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-nontrapping-scalar-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/nontrapping-scalar-duplicate-snapshot.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/rough-filtering/nontrapping-scalar-prove2-0133-review.json) and [coordinator review](../FURTHER_problems/_tracking/nontrapping-scalar-coordinator-review-2026-10-17.json) record further evidence and limitations.


### Online recheck, 2026-10-30

Real-analytic or piecewise-constant injectivity, higher-dimensional convex-foliation results and microlocal cancellation of singularities do not prove qualitative unweighted injectivity for every smooth nontrapping surface allowing conjugate points.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2506.24067); [status source 2](https://arxiv.org/abs/2306.05906); [status source 3](https://arxiv.org/abs/1402.5559). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-387c2faf2696000a** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
