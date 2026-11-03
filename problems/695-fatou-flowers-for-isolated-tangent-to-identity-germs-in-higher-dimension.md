# 695. Fatou flowers for isolated tangent-to-identity germs in higher dimension

**Area:** Local holomorphic dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$ and let $`f:(\mathbb C^n,0)\to(\mathbb C^n,0)`$ be a holomorphic germ with $`Df(0)=I`$ and with $`0`$ an isolated fixed point. Write
```math
f(z)=z+P_\nu(z)+O(\|z\|^{\nu+1}),\qquad \nu\ge2,
```
where $`P_\nu`$ is a nonzero vector of homogeneous polynomials of degree $`\nu`$.

Must $`f`$ admit a Fatou flower tangent to some direction $`[v]\in\mathbb P^{n-1}(\mathbb C)`$, in the following sense? For some sufficiently small $`\delta>0`$, let $`\Delta_1,\ldots,\Delta_{\nu-1}`$ be the connected components of
```math
D_{\delta,\nu}=\{\zeta\in\mathbb C:|\zeta^{\nu-1}-\delta|<\delta\}.
```
For each $`j`$ there should be an injective holomorphic map $`\varphi_j:\Delta_j\to\mathbb C^n\setminus\{0\}`$ such that:

- $`\varphi_j`$ extends continuously to $`0`$ with $`\varphi_j(0)=0`$;
- its image lies in a common neighborhood on which $`f`$ is represented and is forward invariant under $`f`$;
- $`f^{\circ k}`$ tends to $`0`$ uniformly on compact subsets of that image as $`k\to\infty`$;
- $`[\varphi_j(\zeta)]\to[v]`$ in projective space as $`\zeta\to0`$ within $`\Delta_j`$.

These are the curve and flower requirements in Definition16 of Abate's published source. No extra pairwise-disjointness condition on the images, robustness under blow-ups, formal asymptotic expansion, analytic invariant curve through $`0`$, or nondegeneracy of $`[v]`$ is added. The direction is allowed to depend on the germ.

## Application

Parabolic curves describe trajectories attracted to a fixed point whose linearization is the identity. A general existence theorem would provide a basic geometric description of this local dynamics even when linear stability and nondegenerate-direction methods supply no information.

## References

1. Marco Abate, [*Open problems in local discrete holomorphic dynamics*](https://doi.org/10.1007/s13324-011-0017-y), *Analysis and Mathematical Physics* **1** (2011), 261–287. Definition 16 and Theorems 14–15 on p. 275; OP13 on p. 276. [Author preprint](https://arxiv.org/abs/1107.4876v1). Published e-offprint and preprint were read separately.
2. Lorena López-Hernanz, [*Local dynamics of tangent to the identity biholomorphisms in dimension two*](https://arxiv.org/abs/2610.01520v1), inspected v1, 1 October 2026; related publication *Publications mathématiques de Besançon* (2026), 129–147, [DOI](https://doi.org/10.5802/pmb.74). Selected Theorems 3.3, 3.5, 4.1, 4.3 and Remarks 4.2, 4.4 were compared; journal-body parity was not verified.
3. Marco Abate and Francesca Tovena, [*Parabolic curves in $`\mathbb C^3`$*](https://people.dm.unipi.it/abate/articoli/artric/files/ParabolicCurves.pdf), *Abstract and Applied Analysis* (2003), no. 5, 275–294. Selected introduction and definitions of the linked author version distinguish robust curves from ordinary parabolic curves.

## Status review


**Known cases:** The October survey still retains dimensions at least three with only degenerate characteristic directions. Dimension two, a nondegenerate direction, or a stronger formal separatrix hypothesis does not give the unrestricted flower assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The October survey still retains dimensions at least three with only degenerate characteristic directions. Dimension two, a nondegenerate direction, or a stronger formal separatrix hypothesis does not give the unrestricted flower assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Dimension two is known. A nondegenerate characteristic direction gives a flower in every dimension by the Écalle–Hakim theorem quoted in [1]. The remaining question includes germs whose characteristic directions are all degenerate.

The October 2026 survey [2], Remark 4.4, retains the higher-dimensional parabolic-curve/manifold existence question. Its results conditional on an invariant formal curve do not supply such a curve for every germ, and the resulting attracting manifolds can have dimension greater than one. The failures of two proof strategies described there are not counterexamples to general existence. Likewise, the examples in [3] without robust curves still have ordinary parabolic curves.

The exact flower definition and its quantifiers above come from [1]. The current retention in [2] concerns the underlying existence extension; it is not asserted to restate every flower-domain or petal-count requirement verbatim. No matching complete solution or announcement was located in the recorded bounded checks. This does not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/abate-fatou-flower-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-abate-fatou-flower-review.json), [current comparisons](../FURTHER_problems/_tracking/abate-fatou-flower-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/abate-fatou-flower-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/abate-fatou-flower-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/abate-fatou-flower-coordinator-review-2026-10-19.json) record the checked scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-702597abb179b593**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
