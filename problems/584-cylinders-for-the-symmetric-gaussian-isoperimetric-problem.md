# 584. Cylinders for the symmetric Gaussian isoperimetric problem

**Area:** Probability and statistics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\gamma_d`$ be standard Gaussian measure on $`\mathbb R^d`$. For a set $`E`$ of finite Gaussian perimeter, use

```math
P_\gamma(E)=(2\pi)^{-d/2}\int_{\partial^*E}e^{-|x|^2/2}\,d\mathcal H^{d-1}(x),
```


where $`\partial^*E`$ is its reduced boundary. Fix $`d\ge2`$ and $`a\in(0,1)`$. For $`1\le k\le d`$ and $`b\in(0,1)`$, let

```math
C_{k,b}=B^k_{r_k(b)}\times\mathbb R^{d-k},\qquad \gamma_k(B^k_{r_k(b)})=b,
```


where $`B^k_r`$ is the centered Euclidean ball. Does every centrally symmetric Borel set $`E=-E`$ with $`\gamma_d(E)=a`$ satisfy

```math
P_\gamma(E)\ \ge\ \min_{1\le k\le d}\big\{P_\gamma(C_{k,a}),\ P_\gamma(C_{k,1-a}^{\,c})\big\}?
```


Thus the question asks whether some round cylinder, or the complement of a round cylinder, minimizes perimeter at each prescribed Gaussian volume. Competitors need not be convex. Rotations are allowed and preserve the objective. No uniqueness statement or formula for the optimal $`k`$ is requested. Infinite-perimeter sets satisfy the bound automatically.

This is the inequality component of the cylinder/complement proposal discussed in [1, Introduction] and [2, Conjecture1.3]. Their surface-area convention differs from ours by the common factor $`\sqrt{2\pi}`$, which leaves this comparison unchanged.

## Application

The problem asks how a symmetry constraint changes Gaussian isoperimetry. It connects geometric variation, Gaussian concentration and the small-noise behavior of symmetric decision regions. The displayed objective is perimeter; it does not ask for an optimizer at every positive noise level [2,4].

## References

1. M. Barchiesi and V. Julin, [*Symmetry of minimizers of a Gaussian isoperimetric problem*](https://arxiv.org/html/1805.03161v1), Introduction and Eq.(1). *Probability Theory and Related Fields* **177** (2020), 217–256, [DOI](https://doi.org/10.1007/s00440-019-00947-9). This proves the symmetric-strip case for volume sufficiently close to one, and the complementary case near zero.
2. S. Heilman, [*Symmetric Convex Sets with Minimal Gaussian Surface Area*](https://www.stevenheilman.org/~heilman/papers/symperDv2.pdf), Problem1.1, Conjecture1.3 and the discussion following Theorem1.13. The conjecture concerns all symmetric sets; convexity appears in partial results.
3. S. Heilman, [*Convex Cylinders and the Symmetric Gaussian Isoperimetric Problem*](https://arxiv.org/html/2204.12003v1), Theorem2.4 and Section1.3. Its higher-dimensional product-minimality assumption and exceptional curvature case remain material.
4. S. Heilman, [*Stable Gaussian minimal bubbles*](https://doi.org/10.1007/s00526-026-03408-z), *Calculus of Variations and Partial Differential Equations* **65** (2026), 271, Section1.5, Problem1.17 and Theorem1.18. The symmetric-set theorem assumes eventual dimension-profile stabilization and additional curvature conditions.

## Status review


**Known cases:** Heilman's cylinder classification assumes product minimality and retains an exceptional curvature case. These conditions and the near-zero/one-volume strip cases leave the arbitrary fixed-dimension cylinder/complement inequality unresolved.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The [primary/current-source review](../FURTHER_problems/_tracking/focused-Gaussian-symmetric-cylinder-C279-Root-20261029/OWNER-EXACT-CYLINDER-COMPLEMENT-GAUSSIAN-PERIMETER-PRIMARY-CURRENT-REVIEW.json) and [semantic comparison](../FURTHER_problems/_tracking/focused-Gaussian-symmetric-cylinder-C279-Root-20261029/ROOT-ALL-STATUS-SEMANTIC-COMPARISON-AND-FINAL-REVIEW.json), checked29October2026, found no complete resolution, matching announcement or duplicate. The actual 2026 theorem retains extra assumptions and does not settle the stated fixed-dimension problem. Earlier ball-only proposals have counterexamples; the present question allows every cylinder dimension and complements.

The catalogue’s balanced Gaussian simplex problem optimizes a multi-class finite-noise objective. Its KLS and Simes questions also have different formal targets. No equivalence with those problems is asserted. This review covers selected primary statements and bounded current searches, rather than certification of all proofs or every possible reference.


### Online recheck, 2026-10-30

Heilman's cylinder classification assumes product minimality and retains an exceptional curvature case. These conditions and the near-zero/one-volume strip cases leave the arbitrary fixed-dimension cylinder/complement inequality unresolved.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2204.12003); [status source 2](https://doi.org/10.1007/s00526-026-03408-z); [status source 3](https://cvgmt.sns.it/media/doc/paper/3870/simm-iso.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-66091664200dfc8f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
