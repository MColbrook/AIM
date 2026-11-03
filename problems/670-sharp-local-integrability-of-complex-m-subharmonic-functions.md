# 670. Sharp local integrability of complex m-subharmonic functions

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb C^n`$ be a domain and $`1<m<n`$. Write $`\mathrm{SH}_m(\Omega)`$ for the complex $`m`$-subharmonic functions: for a smooth function, the first $`m`$ elementary symmetric functions of the complex Hessian eigenvalues are nonnegative; for a nonsmooth function, use the standard current definition.

Is it true that every $`u\in\mathrm{SH}_m(\Omega)`$ satisfies

```math
u\in L^p_{\mathrm{loc}}(\Omega)\qquad\text{for every }p<\frac{nm}{n-m}\,?
```

There is no boundedness, finite-energy or compact-singularity assumption. The strict exponent is essential: the complex Hessian fundamental solution $`-|z|^{-2(n-m)/m}`$ belongs locally to $`L^p`$ exactly below $`nm/(n-m)`$.

## Application

The conjecture asks for the optimal universal control of singularities in complex Hessian potential theory. Such local integrability bounds feed into capacity estimates and the regularity theory for complex Hessian equations.

## References

1. Z. Błocki, *Weak solutions to the complex Hessian equation*, Annales de l'Institut Fourier **55** (2005), 1735–1756, printed p. 1737, equation (1.2) and the following conjecture; Proposition 1.3 gives the earlier bound. [Original PDF](https://www.numdam.org/item/10.5802/aif.2137.pdf).
2. S. Dinew and S. Kołodziej, *A priori estimates for complex Hessian equations*, Analysis & PDE **7** (2014), 227–244; sharp integrability with compact singularities. [Publisher PDF](https://msp.org/apde/2014/7-1/apde-v7-n1-p08-p.pdf).
3. P. Åhag and R. Czyż, *Poincaré- and Sobolev-type inequalities for complex m-Hessian equations*, Results in Mathematics **75** (2020), article 63, Corollary 5.8; the Cegrell energy class. [Publisher](https://link.springer.com/article/10.1007/s00025-020-01189-1).
4. P. Åhag and R. Czyż, *Continuity of solutions to complex Hessian equations via the Dinew–Kołodziej estimate*, Annales Fennici Mathematici **50** (2025), 201–214, printed p. 202; later partial-status statement. [Publisher PDF](https://afm.journal.fi/article/download/160119/103868/389202).
5. G. Lin, *Some Integrability Properties of m-Subharmonic Functions*, arXiv:2607.21144v2 (2026), §6, printed p. 8; further conditional results and explicit current-status discussion. [Preprint](https://arxiv.org/pdf/2607.21144v2).

## Status review


**Known cases:** Lin v2 retains the sharp strict exponent as a conjecture and supplies capacity or finite-energy conditions, not every local m-subharmonic function. Quaternionic, compact-Hermitian weaker-exponent and false-endpoint statements are distinct. No matching complete result or announcement found. Clarify the standard exclusion of the identically minus-infinite function when preparing the canonical page.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Lin v2 retains the sharp strict exponent as a conjecture and supplies capacity or finite-energy conditions, not every local m-subharmonic function. Quaternionic, compact-Hermitian weaker-exponent and false-endpoint statements are distinct. No matching complete result or announcement found. Clarify the standard exclusion of the identically minus-infinite function when preparing the canonical page.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2607.21144); [comparison source 2](https://arxiv.org/html/2607.21144v2); [comparison source 3](https://arxiv.org/abs/2503.19678). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 21 October 2026. The extreme cases $`m=1`$ and $`m=n`$ are known. Błocki proved the weaker universal range $`p<n/(n-m)`$. The 2014 and 2020 works reach the conjectured exponent for functions with compact singularities or in a finite-energy class, respectively. The 2025 journal article and 2026 preprint still identify the arbitrary-local case as open. The false critical-endpoint claim is excluded from this question.

No equivalent target was found in AIM or the admitted FURTHER list. The [dated status and duplicate audit](../FURTHER_problems/_tracking/blocki-sharp-m-subharmonic-integrability-status-2026-10-21.json) records the bounded later-result search; it cannot rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-025a611aa93f9e95**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
