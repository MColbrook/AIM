# 575. The limit law of the most visited site of a planar random walk

**Area:** Probability, extreme values and Brownian multiplicative chaos
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`(S_k)`$ be simple nearest-neighbour random walk on $`\mathbb Z^2`$, with $`S_0=0`$. For integers $`N\ge2`$, set

```math
\tau_N=\inf\{k\ge0:S_k\notin[-N,N]^2\},\qquad
\ell_N(x)=\sum_{k=0}^{\tau_N-1}\mathbf1_{\{S_k=x\}},\qquad
 a_N=\frac2{\sqrt\pi}\log N-\frac1{\sqrt\pi}\log\log N.
```

Specify a random measure $`\mu`$ as follows. Let $`B`$ be standard planar Brownian motion from $`0`$, killed at its first exit $`\tau`$ from $`D=(-1,1)^2`$, and let

```math
L_{x,\varepsilon}(\tau)=\lim_{r\downarrow0}\frac1{2r}
\int_0^\tau\mathbf1_{\{\varepsilon-r\le|B_s-x|\le\varepsilon+r\}}\,ds.
```

Set this local time to zero when the circle is not contained in $`D`$. As finite measures on $`D`$, in the weak topology and in probability, define

```math
\mu(dx)=\sqrt{\frac\pi2}\lim_{\varepsilon\downarrow0}
|\log\varepsilon|\varepsilon^2
\exp\!\left(2\sqrt{L_{x,\varepsilon}(\tau)/\varepsilon}\right)\mathbf1_D(x)dx.
```

This is Jego's critical Brownian measure: Theorem 1.1 gives $`0<\mu(D)<\infty`$ almost surely. Do there exist deterministic $`c_1,c_2>0`$ such that, for every $`t\in\mathbb R`$,

```math
\lim_{N\to\infty}\mathbb P\!\left\{\max_x\sqrt{\ell_N(x)}-a_N\le t\right\}
=\mathbb E\!\left[\exp\{-c_1\mu(D)e^{-c_2t}\}\right]?
```

This is the scalar maximum consequence displayed in [1, Conjecture 1].

## Application

The most frequently visited site measures extreme concentration of a stochastic trajectory. Its proposed fluctuation law connects a lattice occupation field to a continuum random measure. Biskup's discussion [2, Section 5.3] places this question alongside other extreme-value problems for logarithmically correlated fields, where clustering and a random shift distinguish the limit from independent-variable statistics.

## References

1. A. Jego, [*Critical Brownian multiplicative chaos*](https://doi.org/10.1007/s00440-021-01051-7), Probability Theory and Related Fields **180** (2021), 495–552; Section 1.1, Eqs. (1.1)–(1.4), Theorem 1.1, and Section 1.2, Conjecture 1, pp. 497–501. [Author version v2](https://arxiv.org/html/2005.14610v2), revised 11 April 2021.
2. M. Biskup, [*Extremal properties of the random walk local time*](https://arxiv.org/html/2502.09853v1), arXiv:2502.09853v1 (2025), Section 5.3, “Frequent points and cover time scaling”.
3. A. Jego, [*Characterisation of Planar Brownian Multiplicative Chaos*](https://doi.org/10.1007/s00220-022-04570-z), Communications in Mathematical Physics **399** (2023), 971–1019; introduction and main-results scope.
4. O. Louidor and S. Saglietti, [*A Limit in Law for the Cover Time and Last Visited Vertex of Wired Planar Domains*](https://arxiv.org/html/2602.21277v1), arXiv:2602.21277v1 (2026), Section 1.1, Theorem I; Section 1.2.2.
5. O. Collin and S. Popov, [*Deviation probabilities for global events in two dimensions (I): independent excursions*](https://arxiv.org/html/2610.26640v1), arXiv:2610.26640v1 (2026), Section 2.3, Corollary 2.6.

## Status review

**Checked 2026-10-23.** The primary 2025 discussion [2] still poses the frequent-point limit law. Its all-sites extremal-process discussion anticipates decorations; the present entry retains only [1]'s explicitly displayed scalar consequence. The definition above uses the stated relation $`m=\sqrt{2/\pi}\mu`$ between the two critical normalizations in [1]. The audit records a missing-square-root inconsistency in [2, Eq. (5.19)]; that display is not used to define this problem.

The 2023 result [3] covers the subcritical regime. The 2026 theorem [4] concerns cover time and the last vertex for a walk returning through a wired boundary. The independent-excursion inequalities [5] give leading-order and deviation estimates. These statements do not establish the displayed first-exit maximum law.

Current author updates, later-proof/counterexample queries and public proof-announcement checks found no matching resolution in their checked extent. The all-status AIM and FURTHER comparison is recorded in the accompanying audit. The current Prove2Me page could not be retrieved; indexed searches and the existing findings were checked, with that access gap retained. These are bounded literature checks, not a claim of exhaustive knowledge.

[Owner/source audit](../FURTHER_problems/_tracking/jego-scalar-maximum-owner-status-2026-10-23.json) · [Duplicate audit](../FURTHER_problems/_tracking/jego-scalar-maximum-duplicate-review-2026-10-23.json) · [Independent review](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/jego-scalar-max-local-time-independent-check-20261023.json).


### Online recheck, 2026-10-30

The first-exit maximum of planar random-walk local time is distinct from the wired-domain cover-time/last-vertex law. Searches found no matching complete scalar-maximum fluctuation theorem.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2502.09853); [status source 2](https://arxiv.org/abs/2602.21277); [status source 3](https://arxiv.org/abs/2005.14610). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-4009a70c4e53c8bd** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
