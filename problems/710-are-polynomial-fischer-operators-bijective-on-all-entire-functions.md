# 710. Are polynomial Fischer operators bijective on all entire functions?

**Area:** Complex analysis and potential theory; holomorphic partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$ and let $`E(\mathbb C^d)`$ denote all entire holomorphic functions, without a growth restriction. For a nonzero polynomial $`P(z)=\sum_\alpha a_\alpha z^\alpha`$, define

```math
P^*(z)=\sum_\alpha\overline{a_\alpha}z^\alpha,
\qquad P^*(D)=\sum_\alpha\overline{a_\alpha}\partial_z^\alpha.
```

Must the operator

```math
F_P:E(\mathbb C^d)\longrightarrow E(\mathbb C^d),
\qquad F_P(q)=P^*(D)(Pq)
```

be a bijection for every such $`P`$? Thus every entire forcing $`g`$ should have exactly one entire solution $`q`$ to $`P^*(D)(Pq)=g`$.

The operator uses the whole coefficient-conjugated polynomial, not only its leading homogeneous part. The zero polynomial is excluded. Nonzero constants are immediate affirmative cases.

## Application

The operator encodes global division for holomorphic differential equations: divide an entire function by a polynomial and choose a remainder in the kernel of a related constant-coefficient differential operator. The polynomial zero set can be singular and carry multiplicity. The question extends beyond polynomial data and Gaussian square-integrable classes.

## References

1. J. M. Aldaz and H. Render, *A Fischer type decomposition theorem from the apolar inner product*, Analysis and Mathematical Physics **13** (2023), article 91, [published article](https://doi.org/10.1007/s13324-023-00844-4), Conjecture 11 (II), physical p. 14.
2. A. Meril and A. Yger, *Problèmes de Cauchy globaux*, Bulletin de la Société Mathématique de France **120** (1992), 87–111, [DOI](https://doi.org/10.24033/bsmf.2180), introduction and Theorem 3.
3. J. M. Aldaz and H. Render, *Fischer decompositions for entire functions of sufficiently low order*, Journal of Mathematical Analysis and Applications **546** (2025), article 129201; [preprint v3](https://arxiv.org/abs/2403.10419v3), Theorem 1. Its leading-part operator and growth assumptions differ.

## Status review


**Known cases:** Current Fischer decompositions impose growth restrictions, use only the principal homogeneous part or give existence without uniqueness. The target uses the whole conjugated polynomial and every entire forcing, with uniqueness.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Current Fischer decompositions impose growth restrictions, use only the principal homogeneous part or give existence without uniqueness. The target uses the whole conjugated polynomial and every entire forcing, with uniqueness.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s13324-023-00844-4); [comparison source 2](https://doi.org/10.24033/bsmf.2180); [comparison source 3](https://arxiv.org/abs/2403.10419v3). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Homogeneous polynomials give bijections on all entire functions. The one-variable case is known. Meril–Yger prove injectivity for degree at most two in all dimensions, and bijectivity for that degree class in dimension two. The general statement is retained as open in the 2023 primary.

Fock-space orthogonal decompositions do not automatically extend to every entire function. The Newman–Shapiro weighted-approximation counterexample concerns general entire generators and a Hilbert-space closure problem; it does not provide a polynomial counterexample here. The [real-polynomial degree conjecture for $`\Delta^k(\psi q)`$](687-does-polynomial-fischer-surjectivity-force-a-quadratic-order-degree-bound.md) is also a different target.

Selected independent, current-status, semantic and catalogue checks through 18 October 2026 found no matching full resolution. A 2012 convolution/interpolation paper has only bounded indexed coverage; its full body remains an access gap. Actual 2025 author statements concern one-variable interpolation and do not announce the general multivariable result. No proof certification or historical novelty is claimed.

The [primary review](../FURTHER_problems/_tracking/parallel/complex-bayesian/entire-fischer-bijection-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-entire-fischer-bijection-review.json), [semantic comparison](../FURTHER_problems/_tracking/entire-fischer-bijection-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/entire-fischer-bijection-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/entire-fischer-bijection-coordinator-review-2026-10-18.json) record the checked scope and access limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9e9d5a2c9d052248**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
