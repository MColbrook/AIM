# 698. Brown–Shields cyclicity in the classical Dirichlet space

**Area:** Complex analysis, potential theory and operator theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Write $`\mathbb D=\{z\in\mathbb C:|z|<1\}`$ and $`\mathbb T=\partial\mathbb D`$. The classical Dirichlet space is

```math
\mathcal D=\left\{f(z)=\sum_{n\geq0}a_nz^n:
\|f\|_{\mathcal D}^2=\sum_{n\geq0}(n+1)|a_n|^2<\infty\right\}.
```

A nonzero holomorphic function is *outer* if, up to a unimodular constant, it has the representation

```math
f(z)=\exp\!\left(\int_{\mathbb T}\frac{\zeta+z}{\zeta-z}
\log h(\zeta)\,dm(\zeta)\right),
```

where $`h>0`$ almost everywhere, $`\log h\in L^1(m)`$, and $`m`$ is normalized arclength measure. Define its radial boundary zero set by

```math
Z(f)=\{\zeta\in\mathbb T:\lim_{r\uparrow1}f(r\zeta)=0\}.
```

For every outer $`f\in\mathcal D`$ with $`Z(f)`$ of logarithmic capacity zero, must

```math
\overline{\{pf:p\in\mathbb C[z]\}}^{\,\mathcal D}=\mathcal D?
```

Equivalently, do polynomials $`p_k`$ exist with $`\|p_kf-1\|_{\mathcal D}\to0`$? Capacity zero means that every compact subset supports no probability measure with finite logarithmic energy $`\iint\log(1/|\zeta-\eta|)\,d\nu(\zeta)d\nu(\eta)`$. No boundary continuity or geometric regularity of $`Z(f)`$ is assumed.

## Application

The question seeks a boundary criterion for approximation by polynomial multiples of one analytic function. It connects logarithmic potential theory with the invariant subspaces of the Dirichlet shift $`f\mapsto zf`$. The necessity of the two conditions is already known [1].

## References

1. O. El-Fallah, K. Kellay and T. Ransford, [*On the Brown–Shields conjecture for cyclicity in the Dirichlet space*](https://arxiv.org/abs/0809.4557v1), *Advances in Mathematics* **222** (2009), 2196–2214, [DOI](https://doi.org/10.1016/j.aim.2009.07.011). Introduction and §2 give the exact target and definitions; the introduction attributes the conjecture to Brown–Shields (1984), Question 12.
2. A. Aleman and S. Richter, [*Cyclicity and iterated logarithms in the Dirichlet space*](https://arxiv.org/abs/2409.20298v2), *Proceedings of the American Mathematical Society* **154** (2026), 783–791. Introduction and the discussion following Theorem 1.4 retain the general conjecture.
3. C. Bellavita, E. Dellepiane, A. Hartmann and J. Mashreghi, [*Infinitely supported harmonically weighted Dirichlet spaces which are de Branges–Rovnyak spaces*](https://arxiv.org/abs/2509.04907v1), [DOI](https://doi.org/10.1016/j.jfa.2026.111558). Theorem 10.1 has additional hypotheses on the weighted space and boundary intersection.
4. H. Bahajji-El Idrissi, O. El-Fallah, Y. Elmadani and A. Hanine, [*Superharmonically Weighted Dirichlet Spaces*](https://arxiv.org/abs/2605.13787v1), preprint (2026), §§1 and 6. The stated regularity and measure hypotheses restrict its cyclicity results.

## Status review


**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current weighted Dirichlet-space papers have additional space, measure or zero-set hypotheses. They do not settle Brown-Shields cyclicity for arbitrary outer functions in the classical Dirichlet space with radial zero set of logarithmic capacity zero.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known cases:** Source [1] proves cyclicity under stronger geometric conditions on an unrestricted-liminf zero set, including a regular generalized-Cantor-set case. Those assumptions are absent here. The newer sufficient conditions in [2–4] do not establish the arbitrary classical case.

**Current checks:** The dated [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/brown-shields-review.json) records primary-source reading, later-result searches, version checks and comparisons against every AIM status and retained entry. The complete 186-page Prove2Me listing snapshot was also [cross-checked](../FURTHER_problems/_tracking/prove2me-catalogue-review.json); its generic “cyclicity” matches concern unrelated trace identities, finite groups, constraint satisfaction and limit cycles.

No matching active solution announcement or duplicate was found. This is a dated literature-status assessment; individual Prove2Me proof projects and every proof in the cited literature have not been exhaustively audited.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-755b6e65c7ca9eb5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
