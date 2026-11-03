# 605. Intermediate-time recovery of the physical measure under deterministic rounding

**Area:** Numerical dynamics and ergodic theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge2`$. Let $`\mathcal E_d`$ be the space of $`C^2`$ maps $`f:\mathbb T\to\mathbb T`$, where $`\mathbb T=\mathbb R/\mathbb Z`$, with degree $`d`$ and $`f'(x)>1`$ everywhere. Give this space its usual $`C^2`$ topology. Each such map has a unique absolutely continuous invariant probability measure $`\mu_f`$.

For $`N\ge1`$, put
```math
E_N=\{i/N:0\le i<N\},\qquad
\lambda_N=\frac1N\sum_{i=0}^{N-1}\delta_{i/N},\qquad
f_N=P_N\circ f|_{E_N},
```

where $`P_N`$ projects to a nearest grid point, with ties resolved by a fixed convention.

**Is there a residual subset $`\mathcal G_d\subseteq\mathcal E_d`$ such that, for every $`f\in\mathcal G_d`$ and every integer sequence $`m=m(N)`$ satisfying**
```math
\frac{\log N}{m(N)}\longrightarrow0,
\qquad \frac{m(N)}{\sqrt N}\longrightarrow0,
```

**one has**
```math
(f_N^{\,m(N)})_*\lambda_N\ \stackrel{*}{\rightharpoonup}\ \mu_f?
```

Residual means containing a countable intersection of open dense subsets. Convergence means convergence against every continuous test function. This asks about a single intermediate iterate of the initial uniform grid law; no time averaging or random rounding is introduced.

## Application

Finite precision turns a chaotic map into a finite-state deterministic system. The question asks whether its simulated distribution recovers the physical distribution during a growing time window before finite-state recurrence dominates.

## References

1. Pierre-Antoine Guihéneuf, [*Spatial discretizations of generic dynamical systems*](https://arxiv.org/abs/1603.06480), arXiv:1603.06480, submitted 2016. Checked PDF bears 25 October 2018; Conjecture 12.13, printed p. 260, and Definition 12.14/Theorem 12.15, p. 261. The served version/date discrepancy is retained explicitly.
2. Pierre-Antoine Guihéneuf and Maurizio Monge, [*Cramér distance and discretisations of circle expanding maps I: theory*](https://doi.org/10.1088/1361-6544/ace817), **Nonlinearity 36** (2023), 4810–4843. Checked [arXiv:2206.07991v3](https://arxiv.org/html/2206.07991v3), Theorem A and Corollaries 1.1–1.2.
3. Guihéneuf and Monge, [*Cramér distance and discretizations of circle expanding maps II: simulations*](https://arxiv.org/html/2206.08000v4), **Dynamical Systems 39** (2024), 108–140, §4. This later work is a status comparator.

## Status review

The original conjecture specifies generic ordinary $`C^2`$ expanding maps and the window $`\log N\ll m\ll\sqrt N`$. Its partial theorem covers a different, shorter regime. The Lipschitz-derivative notation introduced for that theorem does not replace the conjecture's $`C^2`$ topology.

The later theory proves asymptotics with iteration time fixed before the grid limit; its threshold for the grid size can depend on that time. It therefore does not establish the displayed assertion for every growing intermediate-time sequence. The simulations paper still presents the medium-time behavior as conjectural. Genericity is essential: for $`f(x)=2x\pmod1`$ and $`N=2^j`$, every grid point reaches zero after $`j`$ steps.


### Online recheck, 2026-10-30

The later circle-discretization theory fixes the iteration time before the grid limit. It does not prove generic convergence for every growing sequence log N << m << sqrt N; simulations are not such a theorem.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2206.07991); [status source 2](https://arxiv.org/abs/2206.08000); [status source 3](https://arxiv.org/abs/1603.06480). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ff1b16e1a12a2943** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
