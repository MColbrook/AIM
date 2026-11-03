# 915. Polynomial endpoint Lorentz bounds for multilinear forms

**Area:** Functional analysis / multilinear coefficient inequalities
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For integers $`m,n\ge1`$, let $`T:(\mathbb C^n)^m\to\mathbb C`$ be a complex multilinear form, with
```math
\|T\|=\sup_{\|x^{(j)}\|_\infty\le1,\;1\le j\le m}
|T(x^{(1)},\ldots,x^{(m)})|.
```

Arrange the $`n^m`$ numbers $`|T(e_{i_1},\ldots,e_{i_m})|`$ in nonincreasing order as $`a_1^*,\ldots,a_{n^m}^*`$, where $`e_i`$ are standard basis vectors. Put $`p_m=2m/(m+1)`$.

Does a constant $`\delta>0`$, independent of $`m,n,T`$, exist such that
```math
\sum_{k=1}^{n^m}a_k^*
\left(k^{1/p_m}-(k-1)^{1/p_m}\right)
\le m^\delta\|T\|
```
for every $`m,n,T`$? The left side uses the published endpoint Lorentz norm. Its degree-one optimal constant is $`1`$.

## Application

Such bounds would strengthen dimension-free coefficient estimates used in high-dimensional holomorphic analysis and Dirichlet series.

## References

1. A. Defant and M. Mastyło, *Bohnenblust–Hille inequalities for Lorentz spaces via interpolation*, **Analysis & PDE 9** (2016), 1235–1258. Definitions (1),(2), p. 1236; Problem 1, p. 1237; Theorems 6 and 12. [DOI](https://doi.org/10.2140/apde.2016.9.1235); [published text](https://msp.org/apde/2016/9-5/apde-v9-n5-p07-p.pdf).
2. D. M. Pellegrino and E. V. Teixeira, *Polynomial Growth of Complex Polynomial Bohnenblust–Hille Constants*, [arXiv:2608.16584v3](https://arxiv.org/abs/2608.16584v3), 28 September 2026. Equation (1.1) and Theorem A.

## Status review


**Known cases:** Polynomial growth for ordinary coefficient norms and subpolynomial bounds in larger Lorentz spaces do not control the endpoint Lorentz norm with second index one. Recent exact-contractivity results restricted to a fixed monomial support also have another scope.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Polynomial growth for ordinary coefficient norms and subpolynomial bounds in larger Lorentz spaces do not control the endpoint Lorentz norm with second index one. Recent exact-contractivity results restricted to a fixed monomial support also have another scope.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves a finite endpoint bound with exponential degree dependence. Its polynomial bounds in larger Lorentz spaces do not settle Problem 1. The recent polynomial result in [2] controls the ordinary coefficient norm, without endpoint Lorentz control. Bounded primary-literature and announcement checks found no exact complete resolution through the date above.

## Duplicate check

Compared with 1,703 all-status AIM/OpenAI entries, 898 local findings and 533 admitted pages. Boolean influence questions and existing Hardy–Dirichlet problems have different targets.

## Review provenance

An independent reviewer and the coordinator checked the precise norm, quantifiers, partial results and current claims. This records a bounded status review; it does not certify the proofs of recent announcements.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-970fc654af384048**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
