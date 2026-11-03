# 1028. Sharp convex Pólya-functional bounds in dimensions three and higher

**Area:** Spectral shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each integer $`d\geq3`$, let $`\Omega\subset\mathbb R^d`$ range over nonempty bounded open **convex** sets. Let $`\lambda_1(\Omega)`$ be the first Dirichlet eigenvalue and let $`w_\Omega\in H^1_0(\Omega)`$ solve $`-\Delta w_\Omega=1`$. Define $`T(\Omega)=\int_\Omega w_\Omega\,dx`$ and

```math
F(\Omega)=\frac{\lambda_1(\Omega)T(\Omega)}{|\Omega|}.
```


Is it true that the sharp convex-domain bounds are

```math
\sup_{\Omega\text{ convex}}F(\Omega)=\frac{\pi^2}{12},\qquad
  \inf_{\Omega\text{ convex}}F(\Omega)=\frac{\pi^2}{2(d+1)(d+2)}?
```


The proposed supremum is approached by thin convex slabs; the proposed infimum by thin cone sets, as specified in Conjecture 4.2 of the source. The question concerns the constants, not whether a fixed domain attains either extremum.

## Application

The functional compares a domain's lowest vibration frequency with its torsional compliance per unit volume. Sharp constants would identify the limiting shapes giving the strongest and weakest coupling of these quantities within convex geometry.

## References

1. M. van den Berg, G. Buttazzo and A. Pratelli, [*On the relations between principal eigenvalue and torsional rigidity*](https://arxiv.org/html/1910.14593), *Communications in Contemporary Mathematics* **23** (2021), 2050093, [DOI](https://doi.org/10.1142/S0219199720500935), Section 4, Conjecture 4.2. The pinned arXiv v2 states both dimension-dependent convex bounds and the slab/cone limiting families.
2. Z. Deng, [*A Proof of a Conjecture on a Pólya Functional*](https://arxiv.org/html/2609.13221), arXiv:2609.13221v1 (2026), Abstract and Section 1. It announces both sharp bounds for bounded convex domains in **dimension two**, leaving the dimension range here separate.
3. M. van den Berg, V. Ferone, C. Nitsch and C. Trombetti, [*On Pólya's inequality for torsional rigidity and first Dirichlet eigenvalue*](https://arxiv.org/abs/1602.04618), *Integral Equations and Operator Theory* **86** (2016), 579–600. Its unrestricted open-set construction gives $`\sup F=1`$ for $`d\geq2`$; this is why convexity is essential here.
4. V. Amato, C. Nitsch, C. Trombetti and F. Villone, [*On some functionals involving torsional rigidity, principal eigenvalue and perimeter*](https://arxiv.org/html/2601.09592), *Potential Analysis* **65** (2026), article 25, Introduction and equations (1.7)–(1.11). It distinguishes the unrestricted and convex classes and studies a separate perimeter-normalized functional.

## Status review


**Known cases:** The residual is d>=3. The September 2026 announcement proves the planar convex case; unrestricted nonconvex domain constructions and perimeter-dependent functionals change the setting.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The residual is d>=3. The September 2026 announcement proves the planar convex case; unrestricted nonconvex domain constructions and perimeter-dependent functionals change the setting.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2014 conjecture with **all open sets** has a published negative answer; it is excluded in the [scoped review](../FURTHER_problems/_tracking/polya-functional-conjecture-3-3-exclusion-2026-10-21.json). The planar convex case has a 2026 claimed complete proof. Searches for matching higher-dimensional results, counterexamples and announcements through 2026-10-21, plus AIM/FURTHER semantic comparisons, found no complete answer for $`d\geq3`$. The [status and duplicate receipt](../FURTHER_problems/_tracking/convex-polya-high-dimensional-status-2026-10-21.json) records the checked sources and limits. This is a bounded literature review, not a certification that no unindexed solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e2ac8a41434df8db**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
