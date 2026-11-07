# AIM 702: target comparison

**Decision:** Partially resolved.

**Established:** Nonexistence is proved in connectivity three, with a critical-point multiplicity restriction at higher connectivity.

**Scope / remaining target:** Connectivity four and higher remains unresolved here.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 702. Vekua's harmonic boundary problem in connectivity at least three

**Area:** Potential theory and free boundary problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, and let $`\Omega\subset\mathbb R^2`$ be a bounded connected open set whose boundary consists of $`n`$ pairwise disjoint real-analytic Jordan curves $`\Gamma_1,\ldots,\Gamma_n`$. Is it impossible to find a nonconstant real function
```math
u\in C^2(\Omega)\cap C^1(\overline\Omega)
```

and constants $`c_j,d_j\in\mathbb R`$ satisfying
```math
\Delta u=0\quad\hbox{in }\Omega,
\qquad
u=c_j,\quad \partial_\nu u=d_j\quad\hbox{on }\Gamma_j,
\qquad j=1,\ldots,n,
```

where $`\nu`$ is the outward unit normal of $`\Omega`$?

Equivalently, does existence of such a nonconstant solution force the connectivity to be at most two? The constants may differ between components, and the normal derivatives may have different signs and magnitudes. No positivity, ordering, symmetry or convexity is assumed. This is one family across all $`n\ge3`$, including the triply connected case.

This deliberately asks the analytic-boundary restriction of the original Vekua conjecture. Constant functions are excluded. In this regularity class, if one $`d_j`$ vanishes, constant Dirichlet and zero normal data on that analytic component force $`u`$ to be constant by harmonic Cauchy uniqueness. Thus a nonconstant solution automatically has every $`d_j\ne0`$.
