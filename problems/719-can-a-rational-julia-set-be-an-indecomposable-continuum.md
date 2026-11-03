# 719. Can a rational Julia set be an indecomposable continuum?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\widehat{\mathbb C}`$ be the Riemann sphere. Does there exist a rational map

```math
R=\frac{p}{q}:\widehat{\mathbb C}\longrightarrow\widehat{\mathbb C},
\qquad p,q\in\mathbb C[z],\quad \gcd(p,q)=1,\quad
\max\{\deg p,\deg q\}\ge2,
```

whose **entire Julia set** $`J(R)`$ is an indecomposable continuum?

Here $`J(R)`$ is the complement of the open set on which the iterates $`\{R^n:n\ge0\}`$ form a normal family, with convergence measured in the spherical metric. A continuum is a nonempty compact connected metric space. It is **indecomposable** if it cannot be expressed as the union of two proper compact connected subsets. For a rational map of degree at least two, the Julia set is perfect and nondegenerate.

Thus one rational map of any degree at least two gives a positive answer; a negative answer must exclude every such map. The coefficients are unrestricted complex numbers. Connectedness is part of the requested conclusion. No polynomial, hyperbolicity, local-connectivity or no-buried-point hypothesis is imposed.

This is the first clause of Question 14 in reference 1. Its second clause concerns an indecomposable *subcontinuum* with nonempty relative interior; that is a separate question in the unrestricted rational case.

## Application

The question tests the topological complexity possible for the instability set of rational iteration. It links holomorphic dynamics with the geometry of continua and arises in work on Makienko's conjecture.

## References

1. C. P. Curry, J. C. Mayer, J. Meddaugh and J. T. Rogers Jr., [Any counterexample to Makienko's conjecture is an indecomposable continuum](https://arxiv.org/html/0805.3323v1), arXiv:0805.3323v1, §3, Question 14, first clause. Published in *Ergodic Theory and Dynamical Systems* **29**(3) (2009), 875–883, [doi:10.1017/S014338570800059X](https://doi.org/10.1017/S014338570800059X).
2. J. Iglesias, A. Portela, Á. Rovella and J. Xavier, [Non-locally connected spaces I: Coverings and branched coverings on metric spaces](https://arxiv.org/html/2607.18143v2), arXiv:2607.18143v2, 22 August 2026, Introduction and §7, Propositions 4–5 and Remark 7.
3. E. Gomes, [Indecomposable continua and the Julia sets of pseudo-polynomials](https://doi.org/10.3934/dcds.2024172), *Discrete and Continuous Dynamical Systems* **45**(8) (2025), 2471–2484. The earlier author version, [arXiv:2312.17447v1](https://arxiv.org/html/2312.17447v1), is entitled *Indecomposable continua and the Julia sets of polynomial-like mappings*; see Theorem 1.1 and Corollary 1.2 there.

## Status review


**Known cases:** The rational question is about the entire Julia set, not an indecomposable subcontinuum. Exclusion of the Knaster continuum, polynomial-like criteria and obstructed topological branched coverings do not decide unrestricted rational existence.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The rational question is about the entire Julia set, not an indecomposable subcontinuum. Exclusion of the Knaster continuum, polynomial-like criteria and obstructed topological branched coverings do not decide unrestricted rational existence.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/0805.3323v1); [comparison source 2](https://doi.org/10.1017/S014338570800059X); [comparison source 3](https://arxiv.org/html/2607.18143v2); [comparison source 4](https://doi.org/10.3934/dcds.2024172); [comparison source 5](https://arxiv.org/html/2312.17447v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Reference 2 still states the general rational-map question and excludes the Knaster continuum as one particular candidate. It explains why a known topological branched-covering example, which has a Thurston obstruction, does not give a rational example. The prime-end criteria in reference 3 are characterizations rather than a decision of the general existence question; that comparison uses the published abstract and the earlier author version.

Current literature, complete-announcement and all-status duplicate checks found no matching complete resolution. Selected definitions and theorem scopes were checked independently. The review records retain the historical-rendering and published-body parity gaps.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d13ffa7af57a9e59**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
