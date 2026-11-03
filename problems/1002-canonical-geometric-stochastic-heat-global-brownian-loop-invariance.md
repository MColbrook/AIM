# 1002. Canonical geometric stochastic heat: global Brownian-loop invariance

**Area:** Singular stochastic equations and geometric probability
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Prove or disprove the following compact-manifold instance of Conjectures 4.5 and 4.7 of Bruned, Gabriel, Hairer and Zambotti, *Geometric stochastic heat equations*.

Let $`(M,g)`$ be any smooth compact connected Riemannian manifold without boundary, and let $`R_g`$ be its scalar curvature, with curvature convention
```math
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
```

Write $`S^1=\mathbb R/\mathbb Z`$. Choose smooth vector fields $`\sigma_1,\ldots,\sigma_m`$ such that
```math
\sum_i\sigma_i\otimes\sigma_i=g^{-1},\qquad
\sum_i\nabla_{\sigma_i}\sigma_i=0.
```

Such a collection exists by taking the tangent projections of the coordinate vectors of a smooth isometric embedding. Let $`\xi_1,\ldots,\xi_m`$ be independent standard space-time white noises on $`\mathbb R_+\times S^1`$.

Consider the **canonical BGHZ solution** of
```math
\partial_tu
=\nabla_{\partial_xu}\partial_xu
+\frac18\mathrm{grad}_gR_g(u)
+\sqrt2\sum_i\sigma_i(u)\xi_i.
\tag{1}
```

Here “canonical” means the specific local solution theory of Theorem 1.6 of the pinned arXiv v3, with its finite renormalization fixed by the three conditions in that theorem; an arbitrary finite curvature counterterm is not allowed. For the displayed noise normalization apply that theorem with metric $`g/2`$, vector fields $`\sqrt2\sigma_i`$, and smooth drift $`\frac18\mathrm{grad}_gR_g`$. Constant metric rescaling leaves the Levi-Civita connection unchanged. Equivalently, this is the canonical theory used in equation (4.4) and Conjectures 4.5/4.7. Its law is independent of the chosen embedding and vector-field representation. The formal products in (1) have this meaning, rather than an unrenormalized classical or Stratonovich interpretation.

Let $`p_t(x,y)`$ be the heat kernel with respect to Riemannian volume of the diffusion with generator $`\frac12\Delta_g`$, and put
```math
Z=\int_M p_1(x,x)\,d\mathrm{vol}_g(x).
```

Define the Brownian loop probability $`\mu_g`$ by choosing its starting point with density $`Z^{-1}p_1(x,x)`$, then taking the time-one Brownian bridge from that point back to itself. For every $`0<\alpha<\frac12`$, it is supported on $`C^\alpha(S^1,M)`$.

Is it true that, for every such $`(M,g)`$ and every $`0<\alpha<\frac12`$, the maximal canonical solution of (1) is nonexplosive from every deterministic $`u_0\in C^\alpha(S^1,M)`$, and $`\mu_g`$ is invariant for its Markov semigroup? Explicitly, if $`u(0)\sim\mu_g`$ independently of the driving noises, must $`u(t)\sim\mu_g`$ for every $`t\ge0`$?

This asks for globality and invariance, with the coefficient $`1/8`$ fixed. It includes no uniqueness assertion across distinct free homotopy components of loop space. In the paper's noise-one convention, the corresponding scalar-curvature coefficient is $`1/32`$, as explained in Remark 1.7.

## Application

This would identify the canonical stochastic dynamics that preserves Brownian loops on a curved target. It is a precise stochastic-quantization question for the one-dimensional nonlinear sigma model.

## References

1. Y. Bruned, F. Gabriel, M. Hairer and L. Zambotti, *Geometric stochastic heat equations*. [arXiv:1902.02884v3](https://arxiv.org/pdf/1902.02884v3), Theorem 1.6 and Remark 1.7, physical page 11; Conjectures 4.5 and 4.7 and Remark 4.6, physical pages 43–44. Related final publication: *J. Amer. Math. Soc.* **35** (2022), 1–80, [DOI 10.1090/jams/977](https://doi.org/10.1090/jams/977); its body has not been compared with the pinned 93-page v3.

## Status review


**Known cases:** The specific canonical renormalization and scalar-curvature coefficient must agree, with globality for all deterministic Holder starts. Dirichlet-form invariant constructions and local geometric solution theory do not alone identify that canonical global process.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The specific canonical renormalization and scalar-curvature coefficient must agree, with globality for all deterministic Holder starts. Dirichlet-form invariant constructions and local geometric solution theory do not alone identify that canonical global process.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source establishes the canonical local solution and explicitly conjectures globality and loop-measure invariance with the displayed curvature coefficient. Dirichlet-form constructions of invariant diffusions do not by themselves identify that exact canonical solution. Current selected primary comparisons found no matching complete resolution. The independent audit, semantic comparisons and all186 cached catalogue bindings passed; the supplied aliases matched no catalogue descriptions. These bounded checks do not prove that no solution exists. The final80-page edition and cited-body gaps remain recorded.

The [primary review](../FURTHER_problems/_tracking/parallel/rough-filtering/bghz-brownian-loop-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-bghz-brownian-loop-review.json), [semantic comparison](../FURTHER_problems/_tracking/bghz-brownian-loop-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/bghz-brownian-loop-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/bghz-brownian-loop-coordinator-review-2026-10-19.json) record evidence and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c0c84d688b02fd34**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
