# 962. Connectedness of planar cubic elliptic solution sets

**Area:** Nonlinear elliptic equations and control
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be any nonempty bounded smooth open set. Define

```math
\mathcal S(\Omega)=\{u\in C^2(\overline\Omega;\mathbb R):-\Delta u=u^3\text{ in }\Omega\}.
```

No boundary values are prescribed. Is $`\mathcal S(\Omega)`$ connected in the norm topology

```math
\|u\|_{C^2(\overline\Omega)}=\sum_{|\alpha|\le2}\sup_{x\in\overline\Omega}|D^\alpha u(x)|?
```

Connectedness alone is asked. No sign condition or geometric restriction such as star-shapedness or simple connectedness is imposed.

## Application

The set describes all steady states available to a self-amplifying reaction--diffusion equation when its boundary values can vary. Its topology matters for quasistatic boundary control. The source develops this connection in one dimension; an unrestricted higher-dimensional controllability theorem is not asserted here.

## References

1. Jean-Michel Coron, *Control and Nonlinearity*, AMS Mathematical Surveys and Monographs **136** (2007), [doi:10.1090/surv/136](https://doi.org/10.1090/surv/136), Open Problem7.16, printed page233. [Author copy](https://www.ljll.fr/~coron/Documents/Coron-book.pdf), physical PDF page248. The complete source chapter7 has been read; the rest of the book and publisher/errata parity remain separate obligations.

## Status review


**Known cases:** The solution space has arbitrary boundary traces and arbitrary smooth domains. The elementary scaling path applies to star-shaped domains; fixed-boundary multiplicity and local approximation do not show connectedness here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The solution space has arbitrary boundary traces and arbitrary smooth domains. The elementary scaling path applies to star-shaped domains; fixed-boundary multiplicity and local approximation do not show connectedness here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on18October2026. Bounded current-result and announcement searches, an independent selected-primary audit, semantic comparisons with all-status AIM/OpenAI/FURTHER entries and two catalogue scans found no exact resolution or duplicate at their recorded extents.

For a domain star-shaped about $`x_0\in\Omega`$, the path $`u_t(x)=t u(x_0+t(x-x_0))`$ solves the same equation and converges to zero in $`C^2`$ as $`t\downarrow0`$. The domain contraction is essential. Fixed-Dirichlet uniqueness or multiplicity, whole-space positive Lane--Emden nonexistence and local Runge approximation concern different questions.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/B281-cubic-elliptic-connectedness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-B281-cubic-elliptic-connectedness-review.json), [semantic comparison](../FURTHER_problems/_tracking/cubic-elliptic-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/cubic-elliptic-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/cubic-elliptic-coordinator-review-2026-10-18.json) record exact evidence and access limits. These AI checks do not assert human peer review or exhaustive proof verification.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f90aa36e8beb09ea**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
