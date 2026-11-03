# 951. Does the fractional Laplacian recover all singular variation?

**Area:** Nonlocal analysis and functions of bounded variation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge1`$ be an integer and let $`u\in BV(\mathbb R^N;\mathbb R)`$: thus $`u\in L^1(\mathbb R^N)`$ and its distributional derivative is a finite vector-valued Radon measure. Decompose

```math
Du=\nabla u\,\mathcal L^N+D^s u,
```


where $`D^s u`$ is singular with respect to Lebesgue measure and includes both the jump and Cantor parts.

For $`0<\alpha<1`$, use the scalar fractional Laplacian

```math
(-\Delta)^{\alpha/2}u(x)
=c_{N,\alpha}\int_{\mathbb R^N}
 \frac{u(x)-u(y)}{|x-y|^{N+\alpha}}\,dy,
\qquad
c_{N,\alpha}
=\frac{2^{\alpha-1}\alpha\,\Gamma((N+\alpha)/2)}
 {\pi^{N/2}\Gamma((2-\alpha)/2)}.
```


This agrees with the Fourier multiplier $`(2\pi|\xi|)^\alpha`$ under the convention $`\widehat u(\xi)=\int e^{-2\pi i x\cdot\xi}u(x)\,dx`$. For these $`u,\alpha`$, the integral gives an $`L^1`$ function and is absolutely convergent for almost every $`x`$.

Is it true for **every** such $`N`$ and $`u`$ that

```math
\lim_{\alpha\uparrow1}(1-\alpha)
 \bigl\|(-\Delta)^{\alpha/2}u\bigr\|_{L^1(\mathbb R^N)}
=\frac{2}{\pi}|D^s u|(\mathbb R^N)?
```


The absolute value is taken after the inner integral defining the operator. This is the scalar fractional-Laplacian branch of [1, Open Problem 1.3, p. 3], extending its Corollary 1.2 from special functions of bounded variation to all of $`BV`$. The domain is the whole Euclidean space; no compact support, positivity or extra regularity is assumed.

## Application

The identity would separate singular variation from ordinary gradients through a nonlocal energy. This is relevant to variational descriptions of discontinuities and to energies used in image analysis.

## References

1. A. C. Ponce and D. Spector, *On formulae decoupling the total variation of BV functions*, Nonlinear Analysis **154** (2017), 241-257. [DOI](https://doi.org/10.1016/j.na.2016.08.028), [latest preprint v2](https://arxiv.org/abs/1603.08663v2), [Corollary 1.2 and Open Problem 1.3](https://arxiv.org/pdf/1603.08663v2#page=3).
2. J. Xiao and C. Yue, *A trace principle for fractional Laplacian with an application to image process*, 2024 preprint, equation (1.11). [Preprint DOI](https://doi.org/10.21203/rs.3.rs-3997393/v1), [manuscript](https://assets-eu.researchsquare.com/files/rs-3997393/v1_covered_2c5af16e-5824-44de-b6ce-1571f70f35ce.pdf?c=1714011066).
3. G. E. Comi and G. Stefani, *A distributional approach to fractional Sobolev spaces and fractional variation: asymptotics I*, published online 20 June 2022, Theorems 4.7 and 4.9. [DOI](https://doi.org/10.1007/s13163-022-00429-y), [open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10147820/).

## Status review


**Known cases:** The scalar fractional-Laplacian norm has cancellation inside the integral and the Cantor part is essential. SBV formulae, fractional-gradient variation and absolute Taylor-remainder results do not establish this all-BV identity.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The scalar fractional-Laplacian norm has cancellation inside the integral and the Cantor part is essential. SBV formulae, fractional-gradient variation and absolute Taylor-remainder results do not establish this all-BV identity.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Ponce and Spector prove the displayed identity for $`SBV`$, where the Cantor derivative vanishes. Their Open Problem 1.3 asks whether the preceding identities extend to all $`BV`$. Their Theorem 1.4 already treats all $`BV`$ for an absolute Taylor-remainder functional, which has different cancellation properties.

The 2024 preprint [2] repeats the scalar identity for $`SBV`$. The vector fractional-gradient convergence in [3] tends to the full variation $`|Du|`$; it does not establish the displayed scalar limit for $`|D^s u|`$.

The [source, current-literature and duplicate review](../FURTHER_problems/_tracking/focused-BV-singular-fractional-limit-OpenProblem13-A-20261028/EXACT-SCALAR-BV-LIMIT-PRIMARY-CURRENT-976VIA975PLUS1-609P-1704PUBLIC-FOUR-SELECTOR-PROPOSAL-NO-ADMISSION.json) and [independent review](../FURTHER_problems/_tracking/focused-BV-singular-fractional-limit-OpenProblem13-A-20261028/ROOT-EXACT-SCALAR-BV-LIMIT-CURRENT-AND-SEMANTIC-PASS-20261028.json) record the inspected models and limits. No matching complete solution or announcement was located. These are bounded AI checks, not human peer review or a certificate of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b0bafeea5be477c5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
