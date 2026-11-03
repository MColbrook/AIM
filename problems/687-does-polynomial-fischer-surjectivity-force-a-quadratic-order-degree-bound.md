# 687. Does polynomial Fischer surjectivity force a quadratic-order degree bound?

**Area:** Complex analysis and potential theory; polyharmonic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge2`$, $`k\ge1`$ be integers and let $`\psi\in\mathbb R[x_1,\ldots,x_n]`$ be a nonzero polynomial. Write $`\Delta=\sum_{j=1}^n\partial_{x_j}^2`$. Suppose that the linear map

```math
F_{\psi,k}:\mathbb R[x_1,\ldots,x_n]\longrightarrow\mathbb R[x_1,\ldots,x_n],\qquad q\longmapsto\Delta^k(\psi q)
```

is surjective. Must $`\deg\psi\le2k`$?

Equivalently, suppose that **every** real polynomial $`f`$ admits real polynomials $`q_f,h_f`$ with $`f=\psi q_f+h_f`$ and $`\Delta^k h_f=0`$. Does the same degree bound follow? No bound on the degrees of $`q_f`$ or $`h_f`$ is assumed. Coefficients are real, and the question asks a necessary condition, not a characterization by degree alone.

## Application

Polynomial decompositions give exact finite solutions to boundary problems for the Laplace and polyharmonic operators, which occur in potential theory, elasticity and slow viscous flow. For $`k=1`$, the conjecture would imply geometric rigidity for bounded admissible domains with polynomial Dirichlet solvability. The algebraic question also covers polynomials whose zero sets need not bound any such domain.

## References

1. E. Lundberg and H. Render, *The Khavinson–Shapiro conjecture and polynomial decompositions*, Journal of Mathematical Analysis and Applications **376** (2011), 506–513, [DOI](https://doi.org/10.1016/j.jmaa.2010.09.069). [Institutional author manuscript](https://researchrepository.ucd.ie/rest/bitstreams/14687/retrieve), Conjecture1.2, Proposition2.2 and Theorems1.3/3.2.
2. H. Render, *A characterization of the Khavinson–Shapiro conjecture via Fischer operators*, Potential Analysis **45** (2016), 539–543; [eligible preprint](https://arxiv.org/abs/1511.01894v1), Theorem1 and the following real-coefficient conjecture.
3. F. Shao and W. Zhan, *Proof of the planar Khavinson–Shapiro conjecture*, [preprintv1](https://arxiv.org/abs/2608.29909v1) (2026), Theorems1.1–1.2. Its algebraic Theorem1.2 also implies the real-polynomial planar case $`n=2,k=1`$.

## Status review


**Known cases:** The newer planar result addresses n=2 and k=1. The target ranges over every dimension and every polyharmonic order; complex-coefficient counterexamples and bounded-degree surjectivity assumptions differ.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The newer planar result addresses n=2 and k=1. The target ranges over every dimension and every polyharmonic order; complex-coefficient counterexamples and bounded-degree surjectivity assumptions differ.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the bound under an additional uniform degree condition on the decompositions, and supplies further sufficient structural hypotheses. That degree condition is absent here. Complex-coefficient counterexamples do not meet the real-coefficient hypothesis. The 2026 algebraic planar theorem implies the case $`n=2,k=1`$: apply the decomposition to $`|z|^2`$, obtain a divisor of $`zw-H(z)-H^*(w)`$, and use additive separation. This is an announced resolution of that case, without certifying its full proof. The all-dimensional, all-order conjecture remains the broader target.

The [smooth three-dimensional Khavinson–Shapiro problem](720-polynomial-dirichlet-solvability-characterizes-smooth-three-dimensional-ellipsoids.md) already in this catalogue is related: its geometric hypotheses select a narrower $`k=1`$ class. This question is the full real-polynomial, all-order algebraic conjecture; the two should be cross-linked and not treated as equivalent without a converse reduction.

Selected independent, current-status, semantic and catalogue checks through 18 October 2026 found no matching full resolution of the general family. The actual15-page institutional author version was read completely; parity with the8-page final2011 publisher body is not certified. No claim of proof certification or historical novelty is made.

The [primary review](../FURTHER_problems/_tracking/parallel/complex-bayesian/polyharmonic-fischer-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-polyharmonic-fischer-review.json), [semantic comparison](../FURTHER_problems/_tracking/polyharmonic-fischer-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/polyharmonic-fischer-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/polyharmonic-fischer-coordinator-review-2026-10-18.json) preserve the evidence and access limits. The coordinator review records the square-free-divisor reduction for the announced planar case. These are AI checks, not human peer review.

The [paired-polynomial Fischer conjecture on all entire functions](710-are-polynomial-fischer-operators-bijective-on-all-entire-functions.md) uses the differential operator determined by the whole polynomial. Its whole-polynomial differential operator and entire-function space differ from those in this fixed-Laplacian polynomial degree-converse problem.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-452fbe2c811e2e20**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
