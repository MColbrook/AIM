# 919. Can the double-logarithmic loss be removed from the bilinear Hilbert transform's edge estimate?

**Area:** Harmonic analysis and multilinear singular integrals
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a fixed nondegenerate parameter $`\boldsymbol\beta=(\beta_1,\beta_2,\beta_3)`$, meaning that its components are pairwise distinct, define the trilinear form

```math
\Lambda_{\boldsymbol\beta}(f_1,f_2,f_3)
=\int_{\mathbb R}\mathrm{p.v.}\int_{\mathbb R}
f_1(x-\beta_1t)f_2(x-\beta_2t)f_3(x-\beta_3t)
\,\frac{dt}{t}\,dx.
```


Let $`\boldsymbol\alpha=(\alpha_1,\alpha_2,\alpha_3)`$ satisfy $`\sum_j\alpha_j=1`$, one $`\alpha_j=-1/2`$, and both other components be strictly below $`1`$. For every triple of measurable finite-measure sets $`F_1,F_2,F_3\subset\mathbb R`$, does there exist a subset $`F'_j\subset F_j`$ with $`|F'_j|\ge |F_j|/2`$ such that

```math
|\Lambda_{\boldsymbol\beta}(f_1,f_2,f_3)|
\le C_{\boldsymbol\beta,\boldsymbol\alpha}
\prod_{k=1}^{3}|F_k|^{\alpha_k}
```


for **all** $`|f_k|\le\mathbf1_{F_k}`$ when $`k\ne j`$ and all $`|f_j|\le\mathbf1_{F'_j}`$? The subset may depend on the sets, while the constant must not depend on their measures. The parameter is fixed; uniformity as two $`\beta_j`$ coalesce is a different question.

The source calls this Conjecture 1, a generalized restricted weak-type estimate on the short open sides of its exponent hexagon. Its Corollary 4 proves the same bound with an extra factor involving $`\log\log(e^e+|F_j|/\min_{k\ne j}|F_k|)`$. At the midpoint $`\boldsymbol\alpha=(3/4,3/4,-1/2)`$, the question is whether that factor can be removed entirely.

## Application

A positive answer would identify the sharp restricted weak-type boundary behavior of the bilinear Hilbert transform at output exponent $`2/3`$. The analogous Walsh-model quartile operator admits a stronger bound, but its perfect frequency-and-space localization is absent for the continuous transform.

## References

- F. Di Plinio and C. Thiele, [*Endpoint bounds for the bilinear Hilbert transform*](https://arxiv.org/html/1403.5978v1), *Trans. Amer. Math. Soc.* **368** (2016), 3931–3972, [DOI 10.1090/tran/6548](https://doi.org/10.1090/tran/6548). See Introduction, definition (1.3), Conjecture 1 and Corollary 4 (1.7).
- C. Demeter and F. Di Plinio, [*Endpoint bounds for the quartile operator*](https://arxiv.org/abs/1206.3798), *J. Fourier Anal. Appl.* **19** (2013), 836–856. This treats the Walsh model, not the continuous bilinear Hilbert transform.
- G. Uraltsev and M. Warchalski, [*The full range of uniform bounds for the bilinear Hilbert transform*](https://arxiv.org/abs/2205.09851), preprint (2022). Its uniform bounds have output exponent strictly greater than $`2/3`$.

## Status review


**Known cases:** The continuous-transform source still distinguishes the log-corrected endpoint theorem from its log-free conjecture. Walsh/quartile endpoint bounds and continuous uniform estimates with output exponent strictly above two-thirds do not remove the boundary double-log factor.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The continuous-transform source still distinguishes the log-corrected endpoint theorem from its log-free conjecture. Walsh/quartile endpoint bounds and continuous uniform estimates with output exponent strictly above two-thirds do not remove the boundary double-log factor.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper explicitly separates its log-corrected Corollary 4 from the log-free Conjecture 1. A bounded search through 22 October 2026 checked the [current publications of Di Plinio](https://sites.google.com/view/fdiplinio/home/publications), [current papers of Thiele](https://www.math.uni-bonn.de/people/thiele/papers/), later primary endpoint work and online announcements. No result settling this exact continuous-transform boundary bound was found. The 2022 uniform interior-range theorem and related rough-integral endpoint results have different exponent or operator hypotheses. This is bounded negative evidence, not a guarantee that no solution exists. The [exact source-body receipt](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0202-remote-attested-review.json), [status comparison](../FURTHER_problems/_tracking/bht-endpoint-2026-10-22-status.json) and [duplicate audit](../FURTHER_problems/_tracking/bht-endpoint-2026-10-22-duplicates.json) record the checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a2c1f51da746cb70**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
