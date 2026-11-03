# 672. Algebraicity of the three-dimensional two-source quadrature domain

**Area:** Potential theory and free boundary problems
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`e=(1,0,0)`$ and $`a>1`$. Set $`m_a=4\pi a^3/3`$, and use the Newtonian kernel $`N(x)=1/(4\pi|x|)`$, normalized by $`-\Delta N=\delta_0`$. Define

```math
\gamma_a(x)=-\frac{|x|^2}{6}-m_a N(x-e)-m_a N(x+e),
```

with $`\gamma_a=-\infty`$ at the poles. Let $`s_a`$ be the standard least superharmonic majorant on $`\mathbb R^3`$, with the usual potential-theoretic regularization, and let

```math
D_a=\{x:s_a(x)>\gamma_a(x)\}.
```

This specifies the canonical positive two-source quadrature domain, equivalently the smash sum of the overlapping radius-$`a`$ balls centered at $`e`$ and $`-e`$. Its uniform unit density satisfies

```math
\int_{D_a}h(x)\,dx=m_a\bigl(h(e)+h(-e)\bigr)
```

for integrable harmonic $`h`$. The obstacle construction, or equivalently the associated superharmonic quadrature inequality, selects the domain; the harmonic identity alone is not substituted for that specification.

**Question.** For every $`a>1`$, does there exist a nonzero polynomial $`P_a\in\mathbb R[x_1,x_2,x_3]`$ such that

```math
\partial D_a\subseteq\{x:P_a(x)=0\}?
```

The boundary is the entire topological boundary. No uniform degree bound or algebraic dependence of $`P_a`$ on $`a`$ is required. A negative answer requires one parameter $`a>1`$ for which no such polynomial exists.

This is an explicit three-dimensional, equal-positive-mass specialization of the higher-dimensional algebraicity question following Theorem 5.2 in Levine–Peres. It is a source-derived decision question, rather than a quotation of a positive conjecture.

## Application

Quadrature domains describe idealized incompressible growth and free boundaries determined by concentrated sources. The question asks whether a particularly simple three-dimensional source configuration has a boundary describable by one polynomial, as happens for its planar counterpart.

## References

1. Lionel Levine and Yuval Peres, [*Laplacian growth, sandpiles and scaling limits*](https://doi.org/10.1090/bull/1573), Bulletin of the American Mathematical Society **54** (2017), 355–382; [public author manuscript](https://lionellevine.github.io/laplacian-growth-bulletin.pdf), physical pp. 5–6 and 19–21, especially Theorem 5.2 and the following higher-dimensional algebraicity question. The 30-page author manuscript is the inspected version; final-edition parity remains pending.
2. Alexandre Eremenko and Erik Lundberg, [*Non-algebraic quadrature domains*](https://doi.org/10.1007/s11118-012-9297-6), Potential Analysis **38** (2013), 787–804; [author manuscript](https://www.math.purdue.edu/~eremenko/dvi/NonAlgQD.pdf), Theorem 3.1 and the concluding discussion.
3. Lavi Karp and Erik Lundberg, [*A four-dimensional Neumann ovaloid*](https://doi.org/10.4310/ARKIV.2017.v55.n1.a9), Arkiv för Matematik **55** (2017), 185–198, equation (3), Theorem 1 and Remark 2.
4. Hägg and Shapiro, [*Algebraic Cauchy transforms of real algebraic ovals*](https://arxiv.org/html/2606.06296v2), version 2, 5 August 2026, Introduction and Theorems 1.1–1.4. The inspected version's title differs from the abstract-page title.
5. Björn Gustafsson and Mihai Putinar, [*Quadrature Domains Packing*](https://doi.org/10.1007/s00365-026-09757-4), Constructive Approximation **64** (2026), 105–143, abstract and Section 2.2.

## Status review


### Online recheck, 2026-10-30

The target is the canonical three-dimensional equal-positive-point-source obstacle domain for every a>1. Four-dimensional Neumann ovaloids and nonalgebraic evaluation-plus-derivative domains, planar algebraic Schwarz reflections and approximate three-dimensional sink descriptions do not answer it. No matching exact three-dimensional algebraicity or nonalgebraicity proof found in the fresh searches.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s11118-012-9297-6); [comparison source 2](https://doi.org/10.4310/ARKIV.2017.v55.n1.a9); [comparison source 3](https://doi.org/10.1007/s00365-026-09757-4). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

No matching complete resolution or announced solution was located in the recorded bounded checks. The source's planar two-source boundary is a quartic, but rotating that curve does not give the required three-dimensional point-source quadrature identity.

Eremenko–Lundberg's nonalgebraic examples use a four-dimensional evaluation-plus-derivative functional. Karp–Lundberg's explicit positive two-source construction is also four-dimensional. Neither result by itself decides this three-dimensional positive-point question. A transcendental conformal parametrization alone would not prove the boundary nonalgebraic.

The 2026 Cauchy-transform and packing comparisons concern planar models. Boundary regularity and analyticity alone also do not settle polynomial algebraicity.

The [source/current review](../FURTHER_problems/_tracking/parallel/rough-filtering/neumann-ovaloid3d-algebraicity-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-neumann-ovaloid3d-algebraicity-review.json), [semantic comparison](../FURTHER_problems/_tracking/neumann-ovaloid-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/neumann-ovaloid-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/neumann-ovaloid-coordinator-review-2026-10-19.json) record the checked passages and remaining access/version limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0cc49330f5426343**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
