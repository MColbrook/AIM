# 511. Markus's affine completeness conjecture

**Area:** Affine differential geometry; geometric structures
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a smooth, closed, connected, oriented manifold of dimension $`n\ge 1`$. Here closed means compact without boundary. Let $`\nabla`$ be a smooth connection on $`TM`$ with zero torsion and zero curvature. Suppose there is a nowhere vanishing smooth $`n`$-form $`\omega`$ such that

```math
\nabla\omega=0.
```

**Must every maximally extended affine geodesic be defined for all real times?** More explicitly, for every $`p\in M`$ and $`v\in T_pM`$, must the solution of

```math
\nabla_{\dot\gamma}\dot\gamma=0,
\qquad\gamma(0)=p,\qquad\dot\gamma(0)=v
```

have maximal interval of definition $`\mathbb R`$?

Flatness and zero torsion give local coordinates with affine transition maps. The parallel volume form makes their linear holonomy preserve volume. Equivalently, the developing map from the universal cover to $`\mathbb R^n`$ should be an affine diffeomorphism. No positive definite or indefinite metric preserved by $`\nabla`$ is assumed.

## Application

Affine geometry describes locally straight, constant-velocity motion without choosing a metric. This question asks whether preservation of volume prevents that motion from ending in finite affine time on a compact manifold. It concerns the global structure of a continuum geometric model.

## References

1. Raphaël V. Alexandre, *Closed ray affine manifolds*, [arXiv:2109.14417v1](https://arxiv.org/abs/2109.14417v1). General conjecture on pp.2 and16; developing-map and completeness definitions on pp.3–4; Corollary4.1 proves the restricted rank-one ray case.
2. Raphaël V. Alexandre, *Affine three-manifolds with centralizing holonomy*, [arXiv:2303.16665v1](https://arxiv.org/abs/2303.16665v1), pp.1–2. States the general conjecture and a three-dimensional result with an additional centralizing-holonomy assumption.

## Status review

The rank-one ray theorem imposes a special form on the linear holonomy. The three-dimensional centralizer theorem also retains an additional hypothesis. Neither asserts the displayed conclusion for every volume-preserving flat torsion-free connection.

A 2025 manuscript advertised a full affirmative proof, but its latest arXiv record explicitly withdraws it and reports an error in a Hessian computation: [arXiv:2506.14778v3](https://arxiv.org/abs/2506.14778v3), 7 September 2025. The withdrawn abstract still appears in search results and is not treated as a live resolution claim. This review does not independently certify its earlier argument.

Bounded searches on 17 October 2026 found no other matching complete proof or counterexample. The current AIM and retained FURTHER comparisons found no equivalent problem; the independent selected-primary audit and the scoped catalogue comparison passed. Negative searches do not establish openness.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/markus-completeness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-markus-completeness-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/markus-completeness-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/markus-completeness-prove2-0144-review.json) and [coordinator review](../FURTHER_problems/_tracking/markus-completeness-coordinator-review-2026-10-17.json) record the checked hypotheses, withdrawal and reading limits.


### Online recheck, 2026-10-30

The apparent full Markus proof remains withdrawn in the current official arXiv record (v3). Ray-holonomy, centralizing-holonomy and metric special cases do not settle arbitrary volume-preserving affine connections.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2506.14778); [status source 2](https://arxiv.org/abs/2109.14417); [status source 3](https://arxiv.org/abs/2303.16665). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-a290c6622b24f056** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
