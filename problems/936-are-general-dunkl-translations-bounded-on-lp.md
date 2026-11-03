# 936. Are general Dunkl translations bounded on Lp?

**Area:** Harmonic analysis and reflection operators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`R\subset\mathbb R^d\setminus\{0\}`$ be a finite reduced root system, $`G`$ its reflection group, $`R_+`$ a positive subsystem, and $`k:R\to[0,\infty)`$ invariant under $`G`$. Set
```math
\sigma_\alpha x=x-2\frac{\langle\alpha,x\rangle}{|\alpha|^2}\alpha,
\quad w_k(x)=\prod_{\alpha\in R_+}|\langle\alpha,x\rangle|^{2k(\alpha)},
\quad d\mu_k=c_kw_k(x)\,dx,
```

where $`c_k^{-1}=\int e^{-|x|^2/2}w_k(x)\,dx`$. Define
```math
T_jf=\partial_jf+\sum_{\alpha\in R_+}k(\alpha)\alpha_j
\frac{f-f\circ\sigma_\alpha}{\langle\alpha,x\rangle}.
```

Let $`E_k(x,z)`$ be the normalized analytic kernel satisfying
$`T_jE_k(\cdot,z)=z_jE_k(\cdot,z)`$, $`E_k(0,z)=1`$. For
```math
\mathcal F_kf(\xi)=\int f(x)E_k(-i\xi,x)\,d\mu_k(x),
```

define $`\tau^y`$ initially on $`L^2(d\mu_k)`$ through
```math
\mathcal F_k(\tau^yf)(\xi)=E_k(iy,\xi)\mathcal F_kf(\xi).
```

For every such $`R,k`$, every finite $`1\le p<\infty`$, $`p\ne2`$, and every fixed $`y\in\mathbb R^d`$, does a finite $`C=C(R,k,p,y)`$ exist with
```math
\|\tau^yf\|_{L^p(d\mu_k)}\le C\|f\|_{L^p(d\mu_k)}
\quad(f\in\mathcal S(\mathbb R^d))?
```

Equivalently, does each translation extend boundedly to this $`L^p`$ space? Functions need not be radial. No uniform bound over $`y`$, positivity or contraction is required.

## Application

Such bounds would support convolution and potential estimates in harmonic analysis with reflection symmetries.

## References

1. D. V. Gorbachev, V. I. Ivanov and S. Yu. Tikhonov, *Riesz potential and maximal function for Dunkl transform*, [arXiv:1708.09733v1](https://arxiv.org/abs/1708.09733v1), 2017, Introduction, equations (1.2)–(1.4) and following question on p.4.
2. J. Dziubański and A. Hejna, *Remarks on Dunkl Translations of Non-radial Kernels*, Journal of Fourier Analysis and Applications **29** (2023), article52, [DOI:10.1007/s00041-023-10034-2](https://doi.org/10.1007/s00041-023-10034-2), Introduction and §§2.1–2.3; its question is stated for strictly positive multiplicities.

## Status review


**Known cases:** General fixed translations on nonradial functions are the target, including p=1. The September multiplier theorem adds dyadic Sobolev hypotheses; radial and product/rank-one translation results do not settle arbitrary root systems.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

General fixed translations on nonradial functions are the target, including p=1. The September multiplier theorem adds dyadic Sobolev hypotheses; radial and product/rank-one translation results do not settle arbitrary root systems.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The $`p=2`$ bound is known, and $`k=0`$ gives ordinary translations. The [2026 multiplier theorem](https://arxiv.org/html/2609.14298v1) imposes an additional dyadic Sobolev condition and does not itself settle this question. No matching complete or announced resolution was located in bounded checks through 28 October 2026.

The [source review](../FURTHER_problems/_tracking/focused-Dunkl-Lp-translation-C163-Root-20261028/ROOT-PRECISE-DUNKL-SOURCE-VERSION-CURRENT-ANNOUNCEMENT-GATE.json), [independent formulation check](../FURTHER_problems/_tracking/focused-Dunkl-Lp-translation-C163-Root-20261028/C-INDEPENDENT-FIXED-Y-FINITE-P-FORMULATION-AND-CURRENT-THEOREM-SCOPE-PEER-END.json) and [all-status comparison](../FURTHER_problems/_tracking/focused-Dunkl-Lp-translation-C163-Root-20261028/ROOT-FRESH-983MODELS616P-1704ROWS-EXACT-STRUCTURAL-DUPLICATE-GATE.json) retain the scope and limits. These are AI checks, not human peer review or a proof certificate.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ff542bf4be3462b0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
