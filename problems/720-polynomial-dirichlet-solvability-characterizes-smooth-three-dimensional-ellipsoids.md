# 720. Polynomial Dirichlet solvability characterizes smooth three-dimensional ellipsoids

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a nonempty bounded connected open set with $`C^\infty`$ boundary. Suppose that, for every polynomial $`p\in\mathbb R[x_1,x_2,x_3]`$, there is a polynomial $`h\in\mathbb R[x_1,x_2,x_3]`$ such that

```math
\Delta h=0\quad\text{on }\mathbb R^3,\qquad h=p\quad\text{on }\partial\Omega.
```

Must there exist $`a\in\mathbb R^3`$ and a real symmetric positive-definite matrix $`Q`$ such that

```math
\Omega=\{x\in\mathbb R^3:(x-a)^TQ(x-a)<1\}?
```

No bound on the degree of $`h`$ in terms of the degree of $`p`$ is assumed. Neither convexity nor symmetry of $`\Omega`$ is assumed. This is the smooth three-dimensional case of the Khavinson–Shapiro conjecture. Ellipsoids, including balls, have the stated polynomial extension property.

## Application

The Laplace equation models electrostatic potential and steady temperature. The question asks which three-dimensional shapes allow every polynomial boundary input to have an exact finite polynomial solution.

## References

1. H. Render, *A characterization of the Khavinson-Shapiro conjecture via Fischer operators*, [eligible preprint v1](https://arxiv.org/abs/1511.01894v1) (2015), introduction, property (KS), and Theorem 1.
2. F. Shao and W. Zhan, *Proof of the planar Khavinson–Shapiro conjecture*, [preprint v1](https://arxiv.org/abs/2608.29909v1) (2026), Theorem 1.1. A complete claim for two-dimensional Jordan domains; it does not assert the three-dimensional result here.

3. E. Lundberg and H. Render, *The Khavinson–Shapiro conjecture and polynomial decompositions*, Journal of Mathematical Analysis and Applications **376** (2011), 506–513, [DOI](https://doi.org/10.1016/j.jmaa.2010.09.069), Theorem 1.3, which assumes additional uniform degree control.
4. H. Render, *The Khavinson–Shapiro conjecture for domains with a boundary consisting of algebraic hypersurfaces*, [v1](https://arxiv.org/abs/1511.01747v1) (2015), Theorems 1–2.

## Status review


**Known cases:** The August Shao-Zhan announcement is planar. Restricting a three-dimensional harmonic polynomial to a plane need not preserve harmonicity, so it does not settle the smooth three-dimensional Khavinson-Shapiro assertion without a degree bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The August Shao-Zhan announcement is planar. Restricting a three-dimensional harmonic polynomial to a plane need not preserve harmonicity, so it does not settle the smooth three-dimensional Khavinson-Shapiro assertion without a degree bound.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1511.01894v1); [comparison source 2](https://arxiv.org/abs/2608.29909v1); [comparison source 3](https://doi.org/10.1016/j.jmaa.2010.09.069); [comparison source 4](https://arxiv.org/abs/1511.01747v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source poses the all-dimensional conjecture without a degree bound. Fischer-operator reductions and degree-controlled results impose substantive additional conditions. The 2026 planar proof claim must be distinguished from the displayed three-dimensional question. The independent selected-primary audit, bounded current-results and announcement searches, semantic comparisons and catalogue scan passed at their recorded extents. The planar claim is recorded as an announced resolution, without certifying its full proof. Plane sections of a three-dimensional harmonic polynomial need not be harmonic, so the planar theorem does not automatically apply. The real-coefficient requirement also excludes the known complex Fischer-operator examples.

The [source and current-results packet](../FURTHER_problems/_tracking/coordinator-potential/khavinson-shapiro-3d-review-2026-10-18.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-khavinson-shapiro-3d-review.json), [semantic comparison](../FURTHER_problems/_tracking/khavinson-shapiro3d-duplicates-review-2026-10-18.json) and [catalogue receipt](../FURTHER_problems/_tracking/khavinson-shapiro3d-catalogue-review-2026-10-18.json) record the exact review extents and limits. These AI literature and formulation checks are not human peer review or certification of every cited proof.

The related [general polyharmonic Fischer degree conjecture](687-does-polynomial-fischer-surjectivity-force-a-quadratic-order-degree-bound.md) asks about all real polynomial divisors and all orders, including cases without a domain boundary. Its status notes record an announced planar algebraic subcase; it is not equivalent to this three-dimensional geometric question.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d20103502e4aa38d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
