# 941. Maximal clamped-plate compliance under a variable bounded load

**Area:** Shape optimization / fourth-order elasticity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`N\ge3`$ and a volume $`m>0`$. Let $`\Omega\subset\mathbb R^N`$ be any nonempty open set with $`|\Omega|=m`$; disconnected and unbounded finite-measure competitors are allowed. Define $`H^2_0(\Omega)`$ as the closure of $`C^\infty_c(\Omega)`$ in $`H^2(\Omega)`$. For a measurable real load $`\rho:\Omega\to[-1,1]`$, let $`u_{\Omega,\rho}\in H^2_0(\Omega)`$ be the unique weak solution

```math
\int_\Omega\Delta u_{\Omega,\rho}\,\Delta\phi\,dx
=\int_\Omega\rho\phi\,dx
\qquad(\phi\in H^2_0(\Omega)).
```

Thus the operator is the clamped bilaplacian with **zero lateral compression or tension**. On a smooth boundary the conditions are $`u=\partial_nu=0`$. Define the compliance

```math
\mathcal C(\Omega,\rho)
=\int_\Omega\rho u_{\Omega,\rho}\,dx
=\int_\Omega|\Delta u_{\Omega,\rho}|^2\,dx.
```

If $`B_R`$ is a ball of volume $`m`$, prove or disprove

```math
\mathcal C(\Omega,\rho)
\le\mathcal C(B_R,1)
=\frac{|\mathbb S^{N-1}|R^{N+4}}
 {N^2(N+2)^2(N+4)}
```

for every such $`\Omega`$ and $`\rho`$. The comparison on the right uses the constant load $`1`$; its deflection is

```math
u_{B_R,1}(x)=\frac{(R^2-|x|^2)^2}{8N(N+2)}.
```

No sign condition is imposed on the deflection. No convexity, connectedness, or smoothness assumption is imposed on the competing set beyond the stated weak formulation. The displayed inequality, rather than a classification of every equality case, is the target.

## Application

Compliance measures work done by the transverse load in a linear bending model. The question asks whether a ball under a uniform load already gives the largest response when both shape and every bounded signed load are allowed to vary. The higher-dimensional formulation is the analytic extension of the physical two-dimensional plate problem.

## Known results

Ashbaugh–Bucur–Laugesen–Leylekian prove this assertion in dimensions one and two. They also prove the constant-load inequality in every dimension. Their published Open Problem 1 asks for the extension to higher dimensions and to curved spaces; the statement above isolates its Euclidean higher-dimensional part.

The first-eigenvalue clamped-plate and first-buckling-load conjectures concern different Rayleigh quotients. An estimate only for $`\rho\equiv1`$ does not control all signed loads, because the clamped bilaplacian is not positivity preserving on arbitrary domains. The source's two-ball relaxation has a better value at two equal balls in higher dimensions; that relaxation is not itself a counterexample on a physical competing domain.

## References

1. M. S. Ashbaugh, D. Bucur, R. S. Laugesen and R. Leylekian, *Fourth Order Saint-Venant Inequalities: Maximizing Compliance and Mean Deflection Among Clamped Plates*, Communications in Mathematical Physics **406** (2025), article 256. [DOI](https://doi.org/10.1007/s00220-025-05439-7), [published 35-page PDF](https://link.springer.com/content/pdf/10.1007/s00220-025-05439-7.pdf). Exact Open Problem 1, p. 24; weak/energy definitions, pp. 4–6 and 21; Theorem 5.1, p. 22; ball formula, pp. 6–7. This published version is eligible through registered journal J027; its January 2025 arXiv submission is after the separate W001 cutoff.
2. P. Freitas and R. Leylekian, *Extremal problems for clamped plates under tension*, Journal de Mathématiques Pures et Appliquées **208** (2026), 103867. [DOI](https://doi.org/10.1016/j.matpur.2026.103867), [author version](https://arxiv.org/abs/2507.07040). Model (3) and Theorem B optimize the response to the constant load $`1`$ for $`\Delta^2-\tau\Delta`$, $`\tau\ge0`$. They do not state the variable-load inequality above.

## Status review


**Known cases:** The load may vary measurably in [-1,1], in every dimension N>=3. The 2025 and 2026 ball-maximality results assume constant load or a different tension model; no matching variable-load result found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The load may vary measurably in [-1,1], in every dimension N>=3. The 2025 and 2026 ball-maximality results assume constant load or a different tension model; no matching variable-load result found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Current primary-source and announcement searches on 17 October 2026 found no matching resolution of the stated variable-load assertion. The 2026 tension result and known constant-load inequalities have narrower load classes. Independent selected-primary review passed. All 186 cached catalogue pages were checked with six aliases; the four matching windows concern shallow-water control. This compares listing descriptions rather than every mission proof.

The associated mean and total deflection bounds follow from the bounded-load compliance bound by the Cauchy–Schwarz inequality for the positive inverse operator; they are not counted separately here.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/plate-variable-load-compliance-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-plate-variable-load-compliance-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/plate-compliance-duplicate-query-receipt.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/continuum/plate-variable-load-prove2me0134-review.json) and [coordinator review](../FURTHER_problems/_tracking/plate-variable-load-coordinator-review-2026-10-17.json) record scope and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-3c8e393f9656b29e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
