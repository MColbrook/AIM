# 091. The planar self-avoiding-walk displacement exponent

**Area:** Polymer models

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\mathcal W_N`$ be the finite set of nearest-neighbor walks $`\omega:\{0,\ldots,N\}\to\mathbb Z^2`$ with $`\omega(0)=0`$ and $`\omega(i)\ne\omega(j)`$ for $`i\ne j`$. Give every walk in $`\mathcal W_N`$ equal probability, and write

```math
R_N^2=\frac1{|\mathcal W_N|}
\sum_{\omega\in\mathcal W_N}|\omega(N)|^2.
```

Prove or disprove

```math
\lim_{N\to\infty}\frac{\log R_N^2}{\log N}=\frac32.
```

Thus the root-mean-square displacement would be $`N^{3/4+o(1)}`$. This asks only for the exponent, not existence of a multiplicative asymptotic constant or convergence of the entire path to SLE.

## Application

Self-avoidance models the excluded-volume effect in a polymer chain. The exponent predicts how the typical size of a planar polymer grows with its length.

## References

- [Gordon Slade, *The self-avoiding walk: A brief survey* (2011), critical-exponent discussion](https://doi.org/10.4171/072-1/9).
- [Hugo Duminil-Copin and Alan Hammond, *Self-avoiding walk is sub-ballistic* (Communications in Mathematical Physics, 2013), introduction](https://www.ihes.fr/~duminil/publi/Subballisticity.pdf).

- I. Hueter, [*Proof of the Conjecture that the Planar Self-Avoiding Walk has Root Mean Square Displacement Exponent 3/4*](https://arxiv.org/abs/math/0108077), arXiv:math/0108077v2 (17 August 2001), Theorem 2 and Corollaries 1–2, pp. 27–28. This older claim has a limit-transfer gap identified below.

## Status review

**Announcement check (3 November 2026):** The older Hueter manuscript claims the stated square-lattice exponent, but its transfer from weak to strict self-avoidance is not justified by the estimates quoted in Corollary 1. The lower constant may tend to zero as the repulsion parameter tends to infinity; selecting a slowly increasing parameter with walk length does not establish the required interchange of limits. Corollary 2 relies on that same transfer. A [separate check of this inference](../research/solution-status-audit-2026-11-03/lane-a/091.json) confirms the gap. The problem remains open in this catalogue. The September OpenAI announcement concerns the diameter of honeycomb-lattice walks, which does not settle the displayed square-lattice endpoint second moment.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

The cited survey and sub-ballisticity theorem leave the planar 3/4 exponent conjectural. Numerical confirmation and conditional SLE predictions are not proofs for the finite uniform walk measure. The search also located a 2001 preprint claiming this exponent; the later cited literature still treats it as open. No accepted resolution was located in the 2026 search.

Status-search topics (2026-09-08): `self avoiding walk 3/4 conjecture site.arxiv.org`; `self-avoiding walk exponent 3/4 2026`; `self-avoiding walk SLE conjecture 2026`. This is a literature search, not a proof that no solution exists.
