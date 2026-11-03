# 413. Energy-admissible weak solutions of the undamped hyperbolic p-Laplacian from smooth data

**Area:** Nonlinear wave equations and continuum mechanics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge2`$, let $`\Omega\subset\mathbb R^n`$ be any bounded domain with smooth boundary, and let $`p>2`$. For arbitrary real-valued $`u_0,u_1\in C_c^\infty(\Omega)`$, does
```math
u_{tt}-\mathrm{div}(|\nabla u|^{p-2}\nabla u)=0
\quad\text{in }\Omega\times(0,\infty),\qquad
u|_{\partial\Omega}=0,\quad (u,u_t)|_{t=0}=(u_0,u_1)
```

have a global energy-admissible ordinary weak solution?

Here this means a function $`u`$ for which, for every finite $`T>0`$,
```math
u\in L^\infty(0,T;W_0^{1,p}(\Omega))
\cap W^{1,\infty}(0,T;L^2(\Omega)),
\qquad u(0)=u_0\ \text{in }L^2(\Omega),
```

and, for every $`\varphi\in C_c^\infty(\Omega\times[0,\infty))`$,
```math
\int_0^\infty\!\!\int_\Omega
\left(-u_t\varphi_t+
|\nabla u|^{p-2}\nabla u\cdot\nabla\varphi\right)\,dx\,dt
=\int_\Omega u_1\varphi(x,0)\,dx.
```

Require also, for almost every $`t>0`$,
```math
\frac12\|u_t(t)\|_{L^2}^2+\frac1p\|\nabla u(t)\|_{L^p}^p
\le
\frac12\|u_1\|_{L^2}^2+\frac1p\|\nabla u_0\|_{L^p}^p.
```

The nonlinear flux in this identity must be the actual constitutive flux of $`u`$. A Young-measure average flux alone does not meet the definition.

This is a proposed energy-admissible smooth-data specialization of the broad weak-existence challenge in Benešová–Kampschulte–Schwarzacher, Remark 1.5. The broad source question does not spell out the initial-data quantifiers or the precise energy inequality imposed here. This formulation does not claim equivalence with that broad question or with the variable-exponent Young-measure model in Amorim–Antontsev (2013). The broader rough-data proposal is kept on hold separately.

## Application

The equation models a nonlinear elastic restoring force without viscous damping. Global energy weak solutions would provide an evolution beyond possible breakdown of a smooth solution.

## References

1. B. Benešová, M. Kampschulte and S. Schwarzacher, [*A variational approach to hyperbolic evolutions and fluid-structure interactions*](https://ems.press/content/serial-article-files/48230), J. Eur. Math. Soc. **26** (2024), 4615–4697, Remark 1.5, p.4626. DOI: [10.4171/JEMS/1353](https://doi.org/10.4171/JEMS/1353). The [2020 preprint](https://arxiv.org/html/2008.04796v1) states the corresponding challenge in Remark 3.10.
2. M. Dreher, [*The Wave Equation for the p-Laplacian*](https://www.math.uni-konstanz.de/~dreher/papers/D-11.pdf), author preprint dated 20 July 2005, Theorems 1.2–1.5 and Proposition 9.1. The published article is Hokkaido Math. J. **36** (2007), 21–52, DOI: [10.14492/hokmj/1285766660](https://doi.org/10.14492/hokmj/1285766660).
3. A. Češík and S. Schwarzacher, [*Stability and convergence of in time approximations of hyperbolic elastodynamics via stepwise minimization*](https://arxiv.org/abs/2305.19880), latest v4, 2024; J. Differential Equations **415** (2025), 434–486.

## Status review

The JEMS source identifies ordinary weak existence without dissipation as open and explains why a variational limit alone can give only a measure-valued nonlinear flux. Smoothness of the initial data is a separate restriction of the present proposal.

Dreher proves local high-regularity existence and gives a one-dimensional smooth-solution breakdown result under additional hypotheses. These results do not establish global energy weak existence or its failure for the multidimensional problem above. The later stepwise-minimization results checked by the coordinator retain a higher-order linear spatial regularizer and stronger spatial regularity. Damped, forced and higher-order models were excluded by comparing their equations.

The [owner audit](../FURTHER_problems/_tracking/journal1167-p-Laplacian-owner-scope-current-audit-2026-10-23.json) and [smooth-data addendum](../FURTHER_problems/_tracking/journal1181-p-Laplacian-smooth-data-scope-audit-2026-10-23.json) record the bounded current searches, duplicate checks and source-access limits. Independent source, current-status and all-status semantic duplicate reviews found no complete resolution of this explicitly stated energy-admissible formulation. These are bounded literature checks, rather than a proof of continued openness.

The [independent scope review](../FURTHER_problems/_tracking/undamped-p-laplacian-smooth-energy-independent-peer-2026-10-23.json) and [duplicate review](../FURTHER_problems/_tracking/undamped-p-laplacian-smooth-energy-duplicate-review-2026-10-23.json) record the final checks. The separate rough-data proposal remains on hold.


### Online recheck, 2026-10-30

Current hyperbolic p-Laplacian results add damping, sources or higher-order regularization. Local classical existence and measure-valued limits do not give or refute a global ordinary constitutive-flux, energy-admissible weak solution for every smooth multidimensional datum.

Comparators and current-status sources: [status source 1](https://doi.org/10.4171/JEMS/1353); [status source 2](https://arxiv.org/abs/2305.19880); [status source 3](https://www.math.uni-konstanz.de/~dreher/papers/D-11.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-97a20263f834f6da** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
