# 759. Full interior regularity for the nondegenerate symmetric p-Laplace system

**Area:** Nonlinear elasticity / elliptic regularity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, $`1<p<\infty`$, $`p\ne2`$, and let $`B_1\subset\mathbb R^n`$ be the open unit ball. For $`u\in W^{1,p}(B_1;\mathbb R^n)`$ write

```math
e(u)=\frac{\nabla u+\nabla u^{\mathsf T}}2,
\qquad A(P)=(1+|P|^2)^{(p-2)/2}P,
```

where $`|P|`$ is the Frobenius norm. Suppose $`u`$ solves the homogeneous system weakly:

```math
\int_{B_1} A(e(u)):e(\varphi)\,dx=0
\quad\text{for every }\varphi\in C_c^\infty(B_1;\mathbb R^n).
```

Is every such $`u`$ of class $`C^{1,\alpha}_{\mathrm{loc}}(B_1;\mathbb R^n)`$ for some $`\alpha\in(0,1)`$? Prove this assertion, or produce an admissible weak solution for which it fails. No boundary condition, pressure, or divergence-free constraint is imposed.

## Application

The symmetric gradient is the infinitesimal strain in elasticity. This system is the Euler–Lagrange equation of the convex elastic energy

```math
\int_{B_1}\frac{(1+|e(u)|^2)^{p/2}-1}{p}\,dx.
```

Its regularity theory also enters fracture models with nonlinear constitutive laws. The constant $`1`$ removes degeneracy or singularity at zero strain; the question already arises in this nondegenerate setting.

## Status review


**Known cases:** The full-gradient p-Laplace system differs from this symmetric-gradient Carreau system. Current Sobolev strain and stress estimates and partial regularity do not give C1-alpha regularity at every higher-dimensional interior point.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The full-gradient p-Laplace system differs from this symmetric-gradient Carreau system. Current Sobolev strain and stress estimates and partial regularity do not give C1-alpha regularity at every higher-dimensional interior point.

Additional comparison sources: [comparison source 1](https://doi.org/10.1142/S0219199719500263); [comparison source 2](https://arxiv.org/pdf/1804.09945v1); [comparison source 3](https://doi.org/10.1007/s00526-024-02666-z); [comparison source 4](https://arxiv.org/html/2603.17036v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Conti–Focardi–Iurlano explicitly pose the full regularity question for $`n\ge3`$, even with a positive nondegeneracy parameter. Their Theorem 4.7 gives partial regularity outside a singular set of dimension at most $`\max\{n-q,0\}`$ for some $`q>2`$; their planar result gives full regularity. The present question concerns every interior point in higher dimensions.

Behn–Diening (2024) prove global Sobolev regularity for the natural nonlinear strain quantity and explicitly retain the higher-dimensional $`C^{1,\alpha}`$ question. Behn–Cianchi–Diening–Peng (2026) prove local $`W^{1,2}`$ regularity of the stress in specified $`p`$-ranges, including the nondegenerate Carreau law used here. This does not establish the stated full interior regularity. The standard full-gradient vectorial $`p`$-Laplace system, and the scalar $`p`$-Laplace equation, have different structure.

## References

- S. Conti, M. Focardi and F. Iurlano, *A note on the Hausdorff dimension of the singular set of solutions to elasticity type systems*, Communications in Contemporary Mathematics **21**(6) (2019), 1950026, 58 pp., [DOI](https://doi.org/10.1142/S0219199719500263). Exact open question: [arXiv:1804.09945v1](https://arxiv.org/pdf/1804.09945v1), §1 p. 3 and §4 p. 20; prototype and assumptions §2.1; partial regularity Theorem 4.7.
- L. Behn and L. Diening, *Global regularity for nonlinear systems with symmetric gradients*, Calculus of Variations and Partial Differential Equations **63** (2024), 60, [DOI](https://doi.org/10.1007/s00526-024-02666-z), introduction and Theorems 1.1 and 2.4.
- L. Behn, A. Cianchi, L. Diening and F. Peng, *Maximal Sobolev regularity of the stress tensor for the symmetric gradient p-Laplace system*, [arXiv:2603.17036v1](https://arxiv.org/html/2603.17036v1) (17 March 2026), introduction, Theorem 1.2 and equations (1.10)–(1.11).

The independent selected-primary audit and scoped catalogue comparison passed. [Owner review](../FURTHER_problems/_tracking/parallel/continuum/symmetric-plaplace-full-regularity-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-symmetric-plaplace-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/symmetric-plaplace-navigation-duplicate-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/symmetric-plaplace-prove2me0154-review.json) and [coordinator review](../FURTHER_problems/_tracking/symmetric-plaplace-coordinator-review-2026-10-17.json) preserve exact source versions and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e5c4790e54b5c493**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
