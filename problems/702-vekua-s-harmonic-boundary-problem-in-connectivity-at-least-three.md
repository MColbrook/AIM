# 702. Vekua's harmonic boundary problem in connectivity at least three

**Area:** Potential theory and free boundary problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-07

## Problem statement

Let $`n\ge3`$, and let $`\Omega\subset\mathbb R^2`$ be a bounded connected open set whose boundary consists of $`n`$ pairwise disjoint real-analytic Jordan curves $`\Gamma_1,\ldots,\Gamma_n`$. Is it impossible to find a nonconstant real function
```math
u\in C^2(\Omega)\cap C^1(\overline\Omega)
```

and constants $`c_j,d_j\in\mathbb R`$ satisfying
```math
\Delta u=0\quad\hbox{in }\Omega,
\qquad
u=c_j,\quad \partial_\nu u=d_j\quad\hbox{on }\Gamma_j,
\qquad j=1,\ldots,n,
```

where $`\nu`$ is the outward unit normal of $`\Omega`$?

Equivalently, does existence of such a nonconstant solution force the connectivity to be at most two? The constants may differ between components, and the normal derivatives may have different signs and magnitudes. No positivity, ordering, symmetry or convexity is assumed. This is one family across all $`n\ge3`$, including the triply connected case.

This deliberately asks the analytic-boundary restriction of the original Vekua conjecture. Constant functions are excluded. In this regularity class, if one $`d_j`$ vanishes, constant Dirichlet and zero normal data on that analytic component force $`u`$ to be constant by harmonic Cauchy uniqueness. Thus a nonconstant solution automatically has every $`d_j\ne0`$.

## Application

A harmonic potential that is constant on each boundary represents an equilibrium field around conducting boundary components. Constant normal derivative on each component further requires uniform flux density there. The question asks whether three or more boundary components can support such a configuration when their potential and flux constants may differ. The analogous stream function describes an irrotational planar flow with constant speed separately along each boundary.

## References

1. D. Khavinson, A. Yu. Solynin and D. Vassilev, [*Overdetermined Boundary Value Problems, Quadrature Domains and Applications*](https://www.unm.edu/~vassilev/quadr.pdf), *Computational Methods and Function Theory* **5** (2005), 19–48, Section5, printed pp.30–32 / physical pp.12–14, especially the harmonic boundary problem and Theorem5.5.
2. C. Bénéteau and D. Khavinson, *The Isoperimetric Inequality via Approximation Theory and Free Boundary Problems*, *Computational Methods and Function Theory* **6** (2006), 253–274, Section5.2, physical pp.13–14 of the inspected author manuscript. Equation(5.2) explicitly requires nonzero real component fluxes; PDE(V) is followed by the no-solution conjecture in connectivity at least three. The original statement is also publicly accessible in [1].
3. C. Bénéteau, M. Fleeman, D. Khavinson and A. A. Sola, [*On the concept of inner function in Hardy and Bergman spaces in multiply connected domains*](https://arxiv.org/abs/1810.12987v1), sole arXiv v1, 30 October2018, physical p.9, Eq.(9) and the following paragraph. Associated publication: *Analysis and Mathematical Physics* **9** (2019), 839–866, [DOI](https://doi.org/10.1007/s13324-019-00319-5). The locators refer to the inspected preprint; final journal-body parity remains unchecked.
4. M. Traizet, [*Hollow vortices and minimal surfaces*](https://arxiv.org/html/1407.5308v1), Introduction, Problem(1), Hypothesis1 and Theorem1; associated publication [DOI](https://doi.org/10.1063/1.4927248). Its model requires an unbounded domain and common boundary gradient magnitude. The independent audit also checked the revised2015 author version.
5. D. Khavinson and E. Lundberg, [*A note on arclength null quadrature domains*](https://arxiv.org/html/2005.09822v2), latest v2, 4 September2021, Theorem2.2 and its remark; associated publication [DOI](https://doi.org/10.1112/blms.12615).
6. A. Abanov, C. Bénéteau, D. Khavinson and R. Teodorescu, [*A free boundary problem associated with the isoperimetric inequality*](https://arxiv.org/html/1601.03885v1), Theorem1.2(iv). Its classification concerns a different Poisson equation and common normal derivative.
7. H. Chen and B. Wu, [*Payne–Philippin's overdetermined problems on compact surfaces*](https://arxiv.org/html/2512.06740v3), latest v3, 5 May2026, Theorem5.1, Proposition5.3 and Theorem5.5. These retain a Steklov boundary relation; the higher-eigenvalue classification also requires no interior critical points.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/702-vekua-s-harmonic-boundary-problem-in-connectivity-at/main.pdf). Nonexistence is proved in connectivity three, with a critical-point multiplicity restriction at higher connectivity.

**Known cases:** Nonexistence is proved in connectivity three, with a critical-point multiplicity restriction at higher connectivity.

**Remaining target:** Connectivity four and higher remains unresolved here.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/702-review.md) checks the complete argument against this exact target and records the primary-source comparisons. The verified restricted results do not resolve the remaining target, so this entry remains partially resolved. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



**Previously recorded known cases:** Arbitrary componentwise boundary fluxes on a bounded domain are required. Steklov proportionality, a common signed normal derivative, and unbounded hollow-vortex constructions impose different conditions.

**Previously recorded remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Arbitrary componentwise boundary fluxes on a bounded domain are required. Steklov proportionality, a common signed normal derivative, and unbounded hollow-vortex constructions impose different conditions.

Additional comparison sources: [comparison source 1](https://www.unm.edu/~vassilev/quadr.pdf); [comparison source 2](https://arxiv.org/abs/1810.12987v1); [comparison source 3](https://doi.org/10.1007/s13324-019-00319-5); [comparison source 4](https://arxiv.org/html/1407.5308v1); [comparison source 5](https://doi.org/10.1063/1.4927248); [comparison source 6](https://arxiv.org/html/2005.09822v2); [comparison source 7](https://doi.org/10.1112/blms.12615); [comparison source 8](https://arxiv.org/html/1601.03885v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original sources [1–2] formulate the nontrivial harmonic problem and conjecture nonexistence for connectivity at least three. The discovery source [3] recalls it explicitly. Its loose phrase “non-zero solution” is interpreted through the original nonzero-flux formulation; a nonzero constant function is excluded from the target.

In connectivity two, [1, Theorem5.5] classifies the bounded Smirnov case as an annulus. On a circular annulus, $`u(z)=\log|z|`$ gives a nonconstant example with constant boundary values and separately constant, oppositely signed outward normal derivatives. Therefore the threshold is material.

Flux conservation requires
```math
\sum_{j=1}^n d_j\,\mathrm{length}(\Gamma_j)=0.
```

This rules out a common nonzero signed normal derivative on a bounded domain, but does not settle the question with arbitrary componentwise constants.

The hollow-vortex constructions [4] allow different signs but explicitly use unbounded domains and a common boundary gradient magnitude. Conformal inversion generally changes the normal derivative by a nonconstant scale along a boundary, so it does not turn those examples into counterexamples here. The arclength null-quadrature theorem [5] also necessarily concerns unbounded domains. The disk/annulus classification in [6] concerns $`\Delta u=1`$ and a common normal derivative, rather than the displayed harmonic system.

The May2026 classification [7] allows different boundary gradient magnitudes but requires $`\partial_\nu u=\sigma_1u`$, where $`\sigma_1`$ is the first nonzero Steklov eigenvalue. Arbitrary componentwise constants need not satisfy this relation after a common additive shift. Its higher-eigenvalue classification additionally assumes no interior critical points, and its general necessary identity does not exclude the target.

The complete pinned25-page discovery preprint was read for question discovery. Original sources and later comparisons received selected passage checks and an independent audit. No matching complete resolution or announcement was located in the recorded bounded searches or semantic comparisons against AIM, OpenAI results and this collection. Final2019 body parity and full reference/correction expansion remain tracked gaps; exhaustive absence and complete proof certification are not claimed.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/vekua-multiconnected-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-vekua-multiconnected-review.json), [latest-comparison audit](../FURTHER_problems/_tracking/parallel/rough-filtering/vekua-chen-wu-latest-selected-review.json), [current comparisons](../FURTHER_problems/_tracking/parallel/complex-bayesian/vekua-multiconnected-current-comparisons.json), [duplicate review](../FURTHER_problems/_tracking/vekua-multiconnected-duplicates-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/vekua-multiconnected-coordinator-review-2026-10-19.json) preserve the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8316cc5bc31839ee**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
