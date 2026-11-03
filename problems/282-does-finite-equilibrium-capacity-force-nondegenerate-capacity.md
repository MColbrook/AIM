# 282. Does finite equilibrium capacity force nondegenerate capacity?

**Area:** Chemical reaction networks and nonlinear dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix finitely many reactions $`y_r\to y'_r`$, with $`y_r,y'_r\in\mathbb N_0^s`$. For positive rates $`\kappa_r`$, write $`x^y=\prod_{i=1}^s x_i^{y_i}`$ and put
```math
f_\kappa(x)=\sum_r\kappa_rx^{y_r}(y'_r-y_r),\qquad
S=\mathrm{span}\{y'_r-y_r\}.
```

A positive equilibrium in a class $`P=(x_0+S)\cap(0,\infty)^s`$ is a zero of $`f_\kappa`$ in $`P`$. It is nondegenerate when $`Df_\kappa(x)|_S:S\to S`$ is invertible.

Let $`C_+(G)`$ and $`C_{\rm nd}(G)`$ be the maximum numbers of distinct positive equilibria and nondegenerate positive equilibria in one class, respectively, maximizing over positive rates and positive $`x_0`$.

The **Nondegeneracy Conjecture** asks whether
```math
C_+(G)<\infty\quad\Longrightarrow\quad C_+(G)=C_{\rm nd}(G).
```

The network stays fixed; rates and class may change. Nondegeneracy does not assert stability.

## Application

The question concerns whether maximal equilibrium multiplicity in a biochemical model can be realized without singular equilibria.

## References

1. B. Joshi and A. Shiu, [*Which small reaction networks are multistationary?*](https://doi.org/10.1137/16M1069705), SIAM J. Appl. Dyn. Syst. **16** (2017), 802–833, Conjecture 2.3; [author preprint](https://arxiv.org/pdf/1603.06441v2).
2. E. Feliu, O. Henriksson and B. Pascual-Escudero, [*The Generic Geometry of Steady State Varieties*](https://doi.org/10.1137/25M1731289), SIAM J. Appl. Algebra Geom. **10** (2026), 519–548; [final preprint](https://arxiv.org/pdf/2412.17798v3), Introduction and Theorem 5.2.

## Status review


**Known cases:** The 2026 generic-geometry theorem gives nondegenerate multistationarity under extra conditions and only a bounded gain from degenerate roots; it does not equate the complete finite equilibrium capacity with nondegenerate capacity for every fixed network.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The one-dimensional stoichiometric case is known [2]. Reference 2 proves a two-equilibrium result under additional hypotheses and explicitly leaves the general count unresolved. Its conclusion $`\ell_{\rm nd}+\min(\ell_{\rm deg},2)`$ does not cover an arbitrary number of degenerate equilibria.

The [independent source/status review](../FURTHER_problems/_tracking/C150-source672893-first75000-A30-priority-20261027/focused-reaction-network-nondegeneracy/ROOT-EXACT-PRIMARY-CURRENT-AND-SEMANTIC-DUPLICATE-GATES-PASS.json) records current and announced-resolution searches and all-status AIM/OpenAI/FURTHER comparisons. No matching resolution or duplicate was located. These are bounded AI checks, not human peer review or a certificate of openness.


### Online recheck, 2026-10-30

The 2026 generic-geometry theorem gives nondegenerate multistationarity under extra conditions and only a bounded gain from degenerate roots; it does not equate the complete finite equilibrium capacity with nondegenerate capacity for every fixed network.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2412.17798); [status source 2](https://doi.org/10.1137/25M1731289); [status source 3](https://arxiv.org/abs/1603.06441). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-0d5c9b396045b1bc** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
