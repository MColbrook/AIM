# 603. No suboptimal local minima in relaxed two-phase elastic compliance

**Area:** Continuous optimization / structural design
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge2`$, let $`\Omega\subset\mathbb R^N`$ be a bounded open set, and let $`f\in L^2(\Omega;\mathbb R^N)`$. Write $`\mathbb S^N`$ for the real symmetric matrices. Fix two constant isotropic Hooke tensors
```math
AE=2\mu_AE+\left(\kappa_A-\frac{2\mu_A}{N}\right)\mathrm{tr}(E)I,\qquad
BE=2\mu_BE+\left(\kappa_B-\frac{2\mu_B}{N}\right)\mathrm{tr}(E)I,
```

where
```math
0<\mu_A\le\mu_B,\qquad 0<\kappa_A\le\kappa_B.
```

For a fixed $`\ell\in\mathbb R`$, define
```math
F_\ell(\tau)=\min\{A^{-1}\tau:\tau+\ell,\ B^{-1}\tau:\tau\}.
```

The colon is the Frobenius inner product. On $`Y=(0,1)^N`$, define the symmetric divergence-quasiconvex envelope by the periodic cell formula
```math
QF_\ell(\tau)=
\inf_{\substack{\eta\in L^2_{\rm per}(Y;\mathbb S^N)\\
\mathrm{div}\eta=0,\ \int_Y\eta\,dy=0}}
\int_Y F_\ell(\tau+\eta(y))\,dy .
```

Divergence is taken row by row in distributions. The perturbations are periodic; replacing them by arbitrary nonperiodic fields is not part of this definition.

Set
```math
\mathcal S_f=\{\tau\in L^2(\Omega;\mathbb S^N):-\mathrm{div}\tau=f\text{ in }\mathcal D'(\Omega)\},\qquad
\mathcal I_\ell(\tau)=\int_\Omega QF_\ell(\tau(x))\,dx.
```

Prove or disprove that every local minimizer of $`\mathcal I_\ell`$ on $`\mathcal S_f`$, in the strong $`L^2`$ norm, is a global minimizer. Explicitly, if $`\tau_0\in\mathcal S_f`$ and some $`\varepsilon>0`$ satisfy
```math
\mathcal I_\ell(\tau_0)\le\mathcal I_\ell(\tau)
\quad\text{for all }\tau\in\mathcal S_f\text{ with }
\|\tau-\tau_0\|_{L^2}<\varepsilon,
```

must this inequality hold for every $`\tau\in\mathcal S_f`$?

The statement uses the source's clamped displacement formulation: the underlying elastic state has $`u\in H^1_0(\Omega;\mathbb R^N)`$. There is no additional prescribed boundary traction on $`\tau`$. The multiplier is fixed and the stress formulation has no separate volume constraint. The nontrivial range is $`\ell<0`$: with phase $`A`$ weaker, $`\ell\ge0`$ selects the quadratic $`B^{-1}\tau:\tau`$ and is convex.

## Application

This conjecture concerns the continuum energy landscape for distributing two elastic materials under a given load. A positive answer would rule out nonglobal norm-local energy traps in this relaxed structural-design model. It would not, by itself, prove convergence of an arbitrary numerical algorithm.

## Context

Allaire states the conjecture in Remark 4.1.18, printed286. Theorem 4.1.15, Eq. 4.44, gives the relaxed stress problem; Eq. 4.43 and Remark 4.1.16 fix the integrand and periodic envelope. The source proves existence of global relaxed minimizers, which does not settle the local-versus-global question. Its separate uniqueness question has negative examples and is not requested here.

The cited conductivity discussion, Remark 3.2.26, proves an affine-boundary, force-free result on star-shaped domains, and warns that general quasiconvex integrands can have nonglobal local minima on an annulus. That generic warning is not a counterexample for this particular elastic integrand. The conjecture above retains the bounded-open-set scope written in chapter4, rather than asserting a theorem for all quasiconvex functions.

## References

- G.Allaire, *Shape Optimization by the Homogenization Method*, Applied Mathematical Sciences 146, Springer (chapter copyright2002), chapter4, pp261–263,282–286, Eqs. 4.43–4.46 and Remark 4.1.18. [Primary chapter](https://doi.org/10.1007/978-1-4684-9286-6_4).
- Same book, chapter3, pp240–241, Remark 3.2.26, for the norm-local interpretation and limited affine-boundary argument. [Primary chapter](https://doi.org/10.1007/978-1-4684-9286-6_3).
- M.Abdelhamid and A.Czekanski, *Revisiting Non-Convexity in Topology Optimization of Compliance Minimization Problems*, arXiv2107.04468v2 (2022), §§2–4: finite-dimensional SIMP/variable-thickness and penalization analysis, with a different use of quasiconvexity. [Primary version](https://arxiv.org/html/2107.04468v2).
- Y.Grabovsky and L.Truskinovsky, *A class of nonlinear elasticity problems with no local but many global minimizers*, arXiv2301.01870v2 (2023), Theorem 2.5 and Eq. 2.20: a gradient-energy theorem requiring a convex-plus-null-Lagrangian structure and Lipschitz minimizers. It does not state this general prescribed-divergence stress result. [Primary version](https://arxiv.org/html/2301.01870v2).
- I.P.A.Papadopoulos, *Numerical analysis of the SIMP model for the topology optimization problem of minimizing compliance in linear elasticity*, Numerische Mathematik 157 (2025),213–248, §§2.5–2.6 and Theorems4–6: approximation of isolated minimizers for regularized/filtered SIMP. [Published primary body](https://doi.org/10.1007/s00211-024-01438-3).

- M. Tyburec, M. Stingl and S. Ma, *Towards realizable free material optimization via energy bound hierarchy*, arXiv:2602.23180v2 (revised 20 October 2026), Theorem 3.10, native pp. 23–25: equality of global continuum optimal values and sequential-laminate attainment in a two-dimensional plane-stress setting with a volume budget. This does not assert that every norm-local stress minimizer of (4.44) is global. [Latest primary version](https://arxiv.org/abs/2602.23180v2).

## Status review

Current-status and duplicate review: bounded exact/variant searches found no complete proof, counterexample or complete announcement for the displayed target. The actual current OpenAI public contents/overview were byte-checked on 26 October 2026 and match the complete 372-family/719-constituent statement projection. The full 1703-entry all-status index and all 930 local findings were screened by target-bearing text. Nearby AIM 233 asks for the full elastic G-closure; it does not ask whether local stress minimizers of this single-load functional are global. No whole-paper proof certification or 719-PDF audit is claimed.


### Online recheck, 2026-10-30

New light-structure relaxation results and free-material global-value/laminate results do not prove absence of suboptimal strong-L2 local stress minima for this fixed multiplier, ordered-isotropic two-phase relaxed compliance functional.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/978-1-4684-9286-6_4); [status source 2](https://arxiv.org/abs/2609.08732); [status source 3](https://arxiv.org/abs/2602.23180). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-529a37c7cbeba24c** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
