# 402. Smooth invertibility of weighted geodesic X-ray normal operators

**Area:** Inverse problems and imaging
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a compact **simple** Riemannian manifold with smooth boundary, and let $`\rho`$ be a boundary defining function on $`M`$. For a scalar function $`f`$, write $`I_0f`$ for its integrals along maximal geodesics and $`I_0^\sharp`$ for the corresponding backprojection adjoint. Let $`\partial_+SM`$ be the incoming unit vectors at the boundary. An $`\alpha`$-boundary defining function ($`\alpha`$-bdf) $`t`$ on $`\partial_+SM`$ satisfies the parity condition under the geodesic scattering relation specified in [1, Definition 4.4].

For **every** $`\gamma>-1`$, does there exist an $`\alpha`$-bdf $`t`$ such that

```math
I_0^\sharp\,t^{-2\gamma-1}I_0\rho^\gamma:
C^\infty(M)\longrightarrow C^\infty(M)
```


is an isomorphism? Here $`I_0\rho^\gamma`$ denotes $`f\mapsto I_0(\rho^\gamma f)`$. This is Conjecture 2.11 of Mazzeo and Monard [1, printed p. 820]. It asks for *some* suitable $`t`$ for each $`(M,g),\rho,\gamma`$, not for every choice of weight.

## Application

The geodesic X-ray transform models measurements along rays in tomography. A smoothly invertible weighted normal operator would give a reconstruction route with boundary behavior built into the function spaces. The original paper proves that the displayed operator maps smooth functions to smooth functions [1, Lemma 2.10]; its conjecture asks whether the inverse exists and is smooth on every simple manifold.

## References

1. R. Mazzeo and F. Monard, [*Double b-fibrations and desingularization of the X-ray transform on manifolds with strictly convex boundary*](https://www.numdam.org/item/10.5802/jep.266.pdf), *Journal de l'École polytechnique — Mathématiques* **11** (2024), 809–847, [DOI 10.5802/jep.266](https://doi.org/10.5802/jep.266), Proposition 2.9, Lemma 2.10, Conjecture 2.11 (printed p. 820), and Definition 4.4.
2. R. K. Mishra, F. Monard and Y. Zou, [*The $`C^\infty`$-isomorphism property for a class of singularly-weighted X-ray transforms*](https://doi.org/10.1088/1361-6420/aca8cb), *Inverse Problems* **39** (2023), no. 2, 024001. This proves the all-$`\gamma>-1`$ result on the Euclidean disk and certain constant-curvature simple disks.
3. J. Kay and F. Monard, [*Singularly weighted X-ray tensor tomography*](https://doi.org/10.1088/1361-6420/ae7d4d), *Inverse Problems* **42** (2026), 065011; [arXiv:2511.08871](https://arxiv.org/abs/2511.08871). Its tensor results concern the Euclidean disk and do not establish the displayed scalar isomorphism on arbitrary simple manifolds.

## Status review


**Known cases:** The all-gamma singular-weight isomorphism theorem is known on disks and selected constant-curvature models. Tensor results on the Euclidean disk and asymptotically hyperbolic surfaces do not provide a suitable alpha-boundary-defining weight for every simple compact manifold.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The [bounded source, status and duplicate audit](../FURTHER_problems/_tracking/weighted-xray-normal-operator-status-2026-10-22.json) checks the original conjecture, known special cases, later work and announcements through 22 October 2026. No result covering every simple $`(M,g)`$ and every $`\gamma>-1`$ was located. This is a bounded search assessment, not a proof of open status.


### Online recheck, 2026-10-30

The all-gamma singular-weight isomorphism theorem is known on disks and selected constant-curvature models. Tensor results on the Euclidean disk and asymptotically hyperbolic surfaces do not provide a suitable alpha-boundary-defining weight for every simple compact manifold.

Comparators and current-status sources: [status source 1](https://doi.org/10.5802/jep.266); [status source 2](https://doi.org/10.1088/1361-6420/aca8cb); [status source 3](https://arxiv.org/abs/2511.08871). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-fcf10ad4d26ace72** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
