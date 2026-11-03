# 1054. Exponential decay for all amplitudes of a damped semilinear wave

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

This is the compact-geometry case of the question following Theorems 1.1–1.2 in [1]. Fix a connected compact smooth three-dimensional Riemannian manifold $`\Omega`$, with homogeneous Dirichlet conditions if it has boundary. Choose $`\beta\ge0`$ so that $`-\Delta_g+\beta`$ is coercive on $`H_0^1(\Omega)`$.

Let $`f:\mathbb R\to\mathbb R`$ be real analytic, with $`f(0)=0`$, $`sf(s)\ge0`$, and, for some fixed $`C>0`$ and $`1\le p<5`$,

```math
|f(s)|\le C(1+|s|)^p,\qquad |f'(s)|\le C(1+|s|)^{p-1}.
```


Let $`\gamma\in L^\infty(\Omega)`$ be nonnegative and bounded below by $`\alpha>0`$ on an open set $`\omega`$ satisfying geometric control: every unit-speed generalized geodesic of some fixed length meets $`\omega`$. For

```math
u_{tt}-\Delta_g u+\gamma u_t+\beta u+f(u)=0,
\qquad (u,u_t)|_{t=0}\in H_0^1(\Omega)\times L^2(\Omega),
```


define

```math
E(t)=\frac12\int_\Omega(|u_t|^2+|\nabla_g u|^2+\beta|u|^2)\,dV_g
+\int_\Omega\int_0^{u(t,x)}f(s)\,ds\,dV_g.
```


For each fixed admissible choice of these objects, do there exist $`K\ge1`$ and $`\lambda>0`$ such that

```math
E(t)\le K e^{-\lambda t}E(0)\qquad(t\ge0)
```


for every initial state, with no energy ceiling?

## Application

The estimate would give a fixed relative-energy decay guarantee for nonlinear vibrations of arbitrarily large amplitude.

## References

1. R. Joly and C. Laurent, [*Stabilization for the semilinear wave equation with geometric control condition*](https://arxiv.org/abs/1205.2459v4), *Analysis & PDE* **6**(5) (2013), 1089–1119, [DOI](https://doi.org/10.2140/apde.2013.6.1089). Equations (1-1)–(1-5), Theorem 1.1 and the second following remark, printed pp. 1090–1091.
2. C. Laurent and C. Loyola, [*Global propagation of analyticity and unique continuation for semilinear waves*](https://jep.centre-mersenne.org/articles/10.5802/jep.348/), *Journal de l’École polytechnique — Mathématiques* **13** (2026), 1323–1387, Theorem 1.4 and following discussion, printed p. 1327, [DOI](https://doi.org/10.5802/jep.348).

## Status review


**Known cases:** Both exponential rate and prefactor must be uniform over all initial energy. The final 2026 unique-continuation/stabilization theorem keeps dependence on the data bound; linear and semiglobal estimates do not settle this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Both exponential rate and prefactor must be uniform over all initial energy. The final 2026 unique-continuation/stabilization theorem keeps dependence on the data bound; linear and semiglobal estimates do not settle this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. The known estimate in [1] permits constants depending on an initial-energy bound. The open remark discusses a possible uniform rate and asks about the prefactor; no claim that uniformity of the rate was proved is made here. This page explicitly restricts the broader question to compact geometry.

The final 2026 theorem [2] retains a constant depending on the data bound. No matching complete proof or announcement was found in bounded searches. AIM 256 asks about exact endpoint control in a fixed time, a different conclusion.

The [coordinator review](../FURTHER_problems/_tracking/semilinear-wave-uniform-decay-coordinator-review-2026-10-23.json), [independent review](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/joly-laurent-amplitude-uniform-independent-bounded-check-20261023.json), [owner scope review](../FURTHER_problems/_tracking/journal1117-uniform-stabilization-scope-status-audit.json) and [duplicate audit](../FURTHER_problems/_tracking/semilinear-wave-uniform-decay-all-status-duplicate-precheck-2026-10-23.json) record exact reading extents and search limits. These are bounded reviews, not exhaustive absence or complete-proof certificates.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a55a388354636e8d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
