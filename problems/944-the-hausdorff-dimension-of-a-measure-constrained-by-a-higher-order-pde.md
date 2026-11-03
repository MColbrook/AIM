# 944. The Hausdorff dimension of a measure constrained by a higher-order PDE

**Area:** Geometric measure theory and PDE-constrained measures
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`U\subset\mathbb R^d`$ be open and let $`\mathcal A=\sum_{|\gamma|\leq k}A_\gamma\partial^\gamma`$ be a constant-coefficient linear differential operator from $`\mathbb R^m`$ to $`\mathbb R^n`$, with at least one nonzero order-$`k`$ coefficient. Write $`\mathbb A^k(\xi)=\sum_{|\gamma|=k}A_\gamma\xi^\gamma`$ for its principal symbol. For $`0\leq\ell\leq d-1`$ define

```math
\mathcal N_{\mathcal A}^{\ell}=\bigcup_{\pi\in\mathrm{Gr}(\ell,d)}\ \bigcap_{\xi\in\pi^\perp}\ker\mathbb A^k(\xi),\qquad
\ell_{\mathcal A}^{*}=\min\{\ell:\mathcal N_{\mathcal A}^{\ell}\ne\{0\}\}.
```


At the elliptic endpoint, use the natural convention $`\mathcal N_{\mathcal A}^{d}=\mathbb R^m`$; the source explicitly writes the cone formula only for $`\ell<d`$. If a nonzero $`\mathbb R^m`$-valued Radon measure $`\mu`$ on $`U`$ obeys $`\mathcal A\mu=0`$ distributionally, must

```math
\dim_H\mu\geq\ell_{\mathcal A}^{*}?
```


Here $`\dim_H\mu=\sup\{s:|\mu|\ll\mathcal H^s\}`$ is the lower Hausdorff dimension used in the source. The displayed dimension inequality is the target; endpoint absolute continuity at $`\ell_{\mathcal A}^{*}`$ would require a separate argument.

## Application

PDE constraints restrict how a singular measure can concentrate. A positive answer would make the rectifiability threshold from the principal symbol a sharp general lower bound on dimension, including higher-order systems where existing wave-cone bounds are weaker.

## Known results and scope

The cited paper obtains the sharp threshold for first-order systems and second-order scalar operators. Its cubic scalar example $`\partial_1^3+\partial_2^3+\partial_3^3`$ has the existing lower threshold $`\ell_{\mathcal A}=1`$ but $`\ell_{\mathcal A}^{*}=2`$, illustrating the unresolved gap. Later quantitative estimates for first-order operators and results requiring a fixed polar or additional symbol condition do not supply the bound for arbitrary higher-order $`\mathcal A`$-free measures.

## References

1. A. Arroyo-Rabasa, G. De Philippis, J. Hirsch and F. Rindler, [*Dimensional estimates and rectifiability for measures satisfying linear PDE constraints*](https://link.springer.com/article/10.1007/s00039-019-00497-1), *Geometric and Functional Analysis* **29** (2019), 639–658, Eq. (1.1), Eq. (1.8) and Conjecture 1.6. [arXiv:1811.01847v2](https://arxiv.org/abs/1811.01847v2).
2. D. Bate and S. Weigt, [*Alberti representations, rectifiability of metric spaces and higher integrability of measures satisfying a PDE*](https://arxiv.org/html/2501.02948v1), arXiv:2501.02948v1 (2025), Theorem 2.7 and Corollary 2.9 (additional polar and symbol hypotheses).
3. G. De Philippis, L. Gennaioli, A. Pigati and F. Rindler, [*Scale-invariant bounds on thin sets for measures satisfying a first-order PDE and the anisotropic Michael–Simon inequality*](https://arxiv.org/html/2609.34573v1), arXiv:2609.34573v1 (2026), Introduction and Theorem 1.3 (first-order scope).

## Status review


**Known cases:** The September 2026 theorem is first-order. June complex-elliptic BV-A dimensional estimates impose another symbol setting and do not cover all higher-order constrained measures with the stated cone threshold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September 2026 theorem is first-order. June complex-elliptic BV-A dimensional estimates impose another symbol setting and do not cover all higher-order constrained measures with the stated cone threshold.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The publisher's full HTML retains Conjecture 1.6 and its precise threshold. Targeted later-primary and announcement searches through 23 October 2026 found no theorem or announced counterexample covering the general higher-order statement; the cited later results have narrower hypotheses. A semantic check found no matching AIM or admitted FURTHER problem. This is a bounded status review, not a proof of absence. Publisher HTML was checked; a native published-PDF validation gap remains, so PDF byte parity is not claimed. The [source and status audit](../FURTHER_problems/_tracking/hambrook-taylor-afree-admission-audit-2026-10-23.json) records the comparison and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-66f3c1cc70607c16**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
