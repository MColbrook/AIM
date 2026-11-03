# 630. Must a closed nonconstant CPE metric be Einstein?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^n,g)`$ be a closed connected smooth Riemannian manifold of dimension $`n\ge3`$, with volume $`1`$ and constant scalar curvature $`s`$. Suppose there exists a **nonconstant** real smooth function $`f`$ satisfying the critical point equation
```math
\mathrm{Hess}_g f-(\Delta_g f)g-f\mathrm{Ric}_g
=\mathrm{Ric}_g-\frac{s}{n}g,
```

where $`\Delta_g f=\mathrm{tr}_g\mathrm{Hess}_g f`$.

Must $`g`$ be Einstein, that is, $`\mathrm{Ric}_g=(s/n)g`$?

Tracing gives $`\Delta_gf=-sf/(n-1)`$. Since $`f`$ is nonconstant and $`M`$ is closed, $`s>0`$ and $`\int_Mf\,dV_g=0`$. If the Einstein conclusion holds, the equation becomes
```math
\mathrm{Hess}_gf=-\frac{s}{n(n-1)}fg,
```

and Obata's theorem makes $`(M,g)`$ a round sphere up to scaling. Thus this is also a sphere-rigidity question.

No curvature sign, stability, Bach-flatness, symmetry, or lower bound $`f\ge-1`$ is assumed. The nonconstant condition matters: the degenerate constant potential $`f=-1`$ on a scalar-flat metric is outside this question.

## Application

The equation comes from the total scalar-curvature functional restricted to metrics of fixed volume and constant scalar curvature. The conjecture asks whether this constrained variational problem produces any additional non-Einstein critical metrics.

## References

1. G. Yun and S. Hwang, *Gap theorems on critical point equation of the total scalar curvature with divergence-free Bach tensor*, [primary preprint](https://arxiv.org/abs/1809.00178). Introduction, Eq. (1.1), and the named Besse conjecture; its proved results have extra hypotheses.
2. G. Colombo, L. Mari and M. Rigoli, *Einstein-type structures, Besse's conjecture and a uniqueness result for a $`\varphi`$-CPE metric in its conformal class* (2022). [Primary preprint, v2](https://arxiv.org/abs/2201.00263v2); [DOI](https://doi.org/10.1007/s12220-022-01000-3). Introduction, Conjectures 1–2, including the explicit nonconstant formulation and constant-potential caveat.
3. G. Yun and S. Hwang, *Critical Point Equation on three-dimensional manifolds and the Besse Conjecture*, [official preprint record](https://arxiv.org/abs/2208.10887). The claimed resolution was withdrawn in November 2022 because of a proof error.
4. P. G. LeFloch and L. Rozoy, *Uniqueness of Kottler spacetime and the Besse conjecture* (2010). [Primary article](https://doi.org/10.1016/j.crma.2010.09.010). Theorem 2.2 concerns the homogeneous static adjoint equation with a regular-level-set assumption, rather than the inhomogeneous CPE above.

## Status review


**Known cases:** Current CPE results impose dimension, curvature, contact or stability hypotheses. An Einstein classification assumes the desired conclusion and cannot prove it for every nonconstant CPE metric; withdrawn full claims are not accepted.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 30 October 2026. The exact source equations, nonconstant formulation and official withdrawal were read. The older static theorem and later results under curvature, stability or contact-geometry assumptions do not give the unrestricted implication stated here.

Bounded current searches found no matching active complete resolution or announcement. Semantic checks against AIM, current saved OpenAI announcements and private findings found no equivalent target. In particular, classification results that already assume an Einstein metric do not establish that a CPE metric is Einstein. These checks are not a proof of openness; selected primary statements were compared without a complete proof audit.


### Online recheck, 2026-10-30

Current CPE results impose dimension, curvature, contact or stability hypotheses. An Einstein classification assumes the desired conclusion and cannot prove it for every nonconstant CPE metric; withdrawn full claims are not accepted.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2201.00263); [status source 2](https://arxiv.org/abs/2208.10887); [status source 3](https://arxiv.org/abs/2211.04840). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-5463a2fc1e2b0f58** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
