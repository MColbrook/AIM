# 956. Smooth monotone approximation in higher dimensions

**Area:** Sobolev spaces, nonlinear potential theory and variational approximation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, let $`\Omega\subset\mathbb R^n`$ be bounded and open, and let $`1<p<\infty`$. A continuous real-valued function is **Lebesgue monotone** if its maximum and minimum on $`\overline V`$ are attained on $`\partial V`$ for every nonempty open $`V\Subset\Omega`$.

For every Lebesgue-monotone $`u\in C(\Omega)\cap W^{1,p}(\Omega)`$, do there exist Lebesgue-monotone functions $`u_j\in C^\infty(\Omega)\cap W^{1,p}(\Omega)`$ satisfying

```math
u_j-u\in W^{1,p}_0(\Omega),\qquad
\sup_\Omega|u_j-u|+\|u_j-u\|_{W^{1,p}(\Omega)}\longrightarrow0?
```


Here $`W^{1,p}_0`$ is the closure of $`C_c^\infty(\Omega)`$, so boundary equality is specified without assuming a regular boundary. Strong Sobolev convergence already implies convergence of the $`p`$-Dirichlet energies. There is **no requirement that each approximant have energy at most that of $`u`$**.

## Application

Such approximants would allow smooth recovery sequences for scalar variational problems while preserving a maximum-and-minimum principle and the Sobolev boundary class. Ordinary mollification need not preserve this monotonicity.

## Known results and scope

Ntalampekos's Question 1.8 asks for higher-dimensional extensions of planar results. Zhong's 2026 preprint announces $`C^{1,\alpha}_{\mathrm{loc}}`$ monotone approximation in every dimension, with fixed Sobolev boundary values. It also announces negative results for manifold level sets and for a discrete smoothness exception under an exact nonincreasing-energy constraint.

The same preprint's §1.4 explicitly leaves general higher-dimensional $`C^\infty`$ approximation with only energy convergence unsettled. The question here isolates that residual; it imposes neither a manifold-level condition nor exact energy nonincrease. It concerns scalar functions, rather than the vector-valued Sobolev homeomorphisms in AIM 153.

## References

1. D. Ntalampekos, [*Monotone Sobolev Functions in Planar Domains: Level Sets and Smooth Approximation*](https://doi.org/10.1007/s00205-020-01563-x), *Archive for Rational Mechanics and Analysis* **238** (2020), 1199–1230. Definition 1.2, Theorem 1.6 and Question 1.8 in the [arXiv body](https://arxiv.org/html/1911.06619v1); [NSF-hosted author manuscript](https://par.nsf.gov/servlets/purl/10219730), p. 4.
2. D. Zhong, [*Monotone Sobolev functions: approximation, critical points, and level sets*](https://arxiv.org/abs/2609.34295v1), preprint (2026), Theorems A and F and §1.4, especially its final paragraph. Its announced results have not been independently proof-verified here.

## Status review


**Known cases:** Zhong Theorem A gives C1-alpha approximation in all dimensions; smooth density is planar. Section 1.4 explicitly says general higher-dimensional C-infinity approximation with convergence of energies is not settled. Theorem F requires a one-sided energy bound absent here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Zhong Theorem A gives C1-alpha approximation in all dimensions; smooth density is planar. Section 1.4 explicitly says general higher-dimensional C-infinity approximation with convergence of energies is not settled. Theorem F requires a one-sided energy bound absent here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source questions, exact later theorem scopes and latest arXiv versions were checked. Bounded resolution and announcement searches found no answer to this residual. Semantic review distinguished AIM 153 and found no matching admitted FURTHER entry; the OpenAI result catalogue describes the different homeomorphism target. The [audit](../FURTHER_problems/_tracking/higher-dimensional-monotone-smoothing-review-2026-10-23.json) records evidence and access limits. No whole-paper reading or complete-proof certification is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d04a4748c6d48d84**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
