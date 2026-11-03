# 733. Global positive classical solutions of sixth-order quantum diffusion

**Area:** Higher-order quantum diffusion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`d\in\{2,3\}`$, and let $`\mathbb T^d=(\mathbb R/\mathbb Z)^d`$. For every real $`n_0\in H^2(\mathbb T^d)`$ with $`\min_{\mathbb T^d}n_0>0`$ and $`\int_{\mathbb T^d}n_0\,dx=1`$, consider
```math
\partial_tn=\nabla\cdot\bigl(n\nabla\Phi(n)\bigr),
\qquad n(0,\cdot)=n_0,
```
where
```math
\Phi(n)=\frac12\sum_{i,j=1}^d(\partial_{ij}\log n)^2
+\frac1n\sum_{i,j=1}^d\partial_{ij}\bigl(n\partial_{ij}\log n\bigr).
```
All spatial conditions are periodic. There are no lower-order diffusion, drift or confinement terms.

Does the unique positive classical solution extend to every finite time? Precisely, is its maximal lifetime $`T_*`$ always infinite, with
```math
n\in C([0,\infty);H^2(\mathbb T^d))
\cap C^\infty((0,\infty)\times\mathbb T^d),\qquad
\inf_{[0,T]\times\mathbb T^d}n>0\quad(T<\infty)?
```
No smallness assumption on the datum or its entropy or energy is imposed.

## Application

This equation describes a sixth-order quantum correction to charge-density diffusion. Its singular logarithmic expression is classical while the density stays positive. Global nonnegative weak solutions are known, but do not themselves exclude finite-time vacuum in the classical evolution.

## Source and progress

Theorem 3 of Bukal–Jüngel–Matthes, *Annales de l'Institut Henri Poincaré C* 30 (2013), 337–365, gives a unique local positive classical solution for these data. It proves that any finite maximal lifetime has a limiting profile in $`H^2`$ whose minimum is zero. The sentence immediately following the theorem, printed p.340, explicitly asks whether that loss of positivity can occur. Their Theorem 1 supplies global nonnegative weak solutions in these dimensions; Theorem 2 gives exponential convergence to the constant state for their constructed weak solutions. Neither conclusion excludes finite-time vacuum.

Matthes–Rott, arXiv:2108.10537v1, proves existence of weak solutions on the whole space using minimizing movements and computes a linearization at a Gaussian equilibrium. Its introduction explicitly says that its approximations carry no positivity information. That result concerns a different domain and solution concept. The 2026 canonical semigroup announcement for the fourth-order DLSS equation concerns the Fisher-information flow, rather than the sixth-order log-Hessian flow displayed here.

## References

- M. Bukal, A. Jüngel and D. Matthes, [A multidimensional nonlinear sixth-order quantum diffusion equation](https://doi.org/10.1016/j.anihpc.2012.08.003), *Ann. Inst. H. Poincaré Anal. Non Linéaire* 30 (2013), 337–365. [Published PDF](https://ems.press/content/serial-article-files/16278), equation (1), Theorem 3 and following question, pp.337–340.
- D. Matthes and E.-M. Rott, [Gradient flow structure of a multidimensional nonlinear sixth-order quantum-diffusion equation](https://arxiv.org/abs/2108.10537), 2021; *Pure and Applied Analysis* 3 (2021), 727–764, [DOI](https://doi.org/10.2140/paa.2021.3.727), actually published February 2022.

## Status review


**Known cases:** The original quantum sixth-order theorem gives local strictly positive classical solutions and global weak nonnegative solutions. Positivity until every finite time for arbitrary positive H2 data in dimensions two and three is not supplied by fourth-order DLSS contraction or discretization results.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The original quantum sixth-order theorem gives local strictly positive classical solutions and global weak nonnegative solutions. Positivity until every finite time for arbitrary positive H2 data in dimensions two and three is not supplied by fourth-order DLSS contraction or discretization results.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.anihpc.2012.08.003); [comparison source 2](https://ems.press/content/serial-article-files/16278); [comparison source 3](https://arxiv.org/abs/2108.10537); [comparison source 4](https://doi.org/10.2140/paa.2021.3.727). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 18 October 2026. The independent selected-primary audit, bounded current-results and announcement searches, semantic comparisons and all-status catalogue review passed at their recorded extents. The final 2013 source was read in full by the discovery reviewer; full parity with the published follow-up remains unverified.

The [source packet](../FURTHER_problems/_tracking/parallel/continuum/sixth-quantum-global-positivity-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-sixth-quantum-global-positivity-review.json), [semantic comparison](../FURTHER_problems/_tracking/sixth-quantum-positivity-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/sixth-quantum-positivity-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/sixth-quantum-positivity-coordinator-review-2026-10-18.json) record exact scopes and access limits. These AI literature and formulation checks are not human peer review or certification of every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-077cba7d3c4a2308**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
