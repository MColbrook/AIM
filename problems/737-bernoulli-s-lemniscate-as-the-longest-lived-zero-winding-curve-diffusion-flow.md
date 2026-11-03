# 737. Bernoulli's lemniscate as the longest-lived zero-winding curve diffusion flow

**Area:** Surface diffusion and geometric evolution
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\gamma_0:S^1\to\mathbb R^2`$ be any smooth regular closed immersed curve, with length $`L_0>0`$ and turning number zero:

```math
\frac1{2\pi}\int_{\gamma_0}\kappa\,ds=0.
```

Let $`\gamma:S^1\times[0,T)\to\mathbb R^2`$ be its maximal smooth regular evolution by curve diffusion,

```math
\partial_t\gamma\cdot\nu=-\partial_s^2\kappa.
```

Here $`s`$ is arclength, $`\nu`$ is a continuously chosen unit normal, and $`\kappa=\partial_s^2\gamma\cdot\nu`$ is the compatible signed curvature. Tangential velocities only change parametrization. Self-intersections are allowed. Here $`T`$ is the maximal time of geometric smooth immersed existence, allowing smooth reparametrization; an artificial degeneration of a tangential parametrization does not end the geometric evolution. It is not the first self-intersection time. There is no assumption of zero signed enclosed area, symmetry, or proximity to a particular curve.

Must every such flow satisfy

```math
T\le \frac{L_0^4}{3\cdot2^{11}K(-1)^4},
\qquad
K(-1)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1+\sin^2\theta}}\,?
```

The proposed bound is attained by a suitably scaled Bernoulli lemniscate. For the explicit regular immersion

```math
b(u)=\frac{(\cos u,\sin u\cos u)}{1+\sin^2u},
\qquad u\in\mathbb R/(2\pi\mathbb Z),
```

its length is $`4K(-1)`$ and its curve diffusion flow is, up to reparametrization, $`(1-24t)^{1/4}b`$, with maximal time $`1/24`$. Scaling lengths by $`a`$ scales time by $`a^4`$, giving the constant displayed above. The question asks only for this universal lifetime bound; it does not assert a classification of all shrinkers or of equality cases.

## Application

Curve diffusion describes interface relaxation driven by surface transport. It also governs the planar profiles of idealized cylindrical ribbons. A sharp lifespan bound would quantify how long an arbitrary zero-turning interface can remain smooth using its initial length alone.

## References

1. M. Edwards, A. Gerhardt-Bourke, J. McCoy, G. Wheeler and V.-M. Wheeler, *The shrinking figure eight and other solitons for the curve diffusion flow*, Journal of Elasticity **119** (2015), 191–211. [Article](https://doi.org/10.1007/s10659-014-9502-5); [primary manuscript](https://arxiv.org/abs/1505.02978). The explicit conjecture is on manuscript p.4; §2 gives the geometric conventions, and §6, Proposition13 and its following remarks, gives the parametrization, length and extinction time.
2. G. Wheeler, *Convergence for global curve diffusion flows*, Mathematics in Engineering **4**(1) (2022), 1–13. [Published article](https://doi.org/10.3934/mine.2022001). Page3 explicitly retains the same zero-winding lifespan conjecture, separately from Giga's embeddedness conjecture and Chou's Type-I conjecture.
3. B. Andrews and G. Wheeler, *Jellyfish exist*, [arXiv:2601.21227](https://arxiv.org/abs/2601.21227), §3.3–3.4, especially Proposition3.10 and Lemma3.13. The new epicyclic shrinkers have nonzero turning number $`p`$, so their existence does not by itself settle this zero-winding bound.

## Status review


**Known cases:** The lifespan target concerns the pure curve diffusion of arbitrary zero-turning immersed curves with the sharp Bernoulli constant. Shrinkers of nonzero turning number, cubic-curvature elastic terms and stability or immortal convergence do not give this lifetime bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The lifespan target concerns the pure curve diffusion of arbitrary zero-turning immersed curves with the sharp Bernoulli constant. Shrinkers of nonzero turning number, cubic-curvature elastic terms and stability or immortal convergence do not give this lifetime bound.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s10659-014-9502-5); [comparison source 2](https://arxiv.org/abs/1505.02978); [comparison source 3](https://doi.org/10.3934/mine.2022001); [comparison source 4](https://arxiv.org/abs/2601.21227). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check:** The conjecture is explicitly retained in the published2022 source. No proof or counterexample to this exact lifespan bound was located in the current primary-source checks on18October2026. The2026 epicyclic shrinkers concern nonzero turning number. Results on smooth convergence of immortal solutions, on length-constrained flows, or on flows with an additional cubic-curvature term do not give the proposed bound for arbitrary zero-winding initial curves.

**Repository comparison:** AIM223 concerns embedded curves throughout their regular evolution. This question concerns all zero-turning immersed curves and a sharp numerical upper bound on their lifetime. It is a different statement.

**Review state:** The selected-primary formulation audit passed, and all returned catalogue-description passages were checked in parallel. The final coordinator admission review passed on 18 October 2026. The final2015 article's full-body parity has not been certified; the explicit target is independently present in the fully read published2022 article.


The [discovery review](../FURTHER_problems/_tracking/parallel/continuum/curve-diffusion-lifespan-review.json), [independent audit](../FURTHER_problems/_tracking/cross-curve-diffusion-lifespan-2026-10-18.json), [parallel catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/curve-diffusion-lifespan-prove2me0168-review.json) and [coordinator decision](../FURTHER_problems/_tracking/curve-diffusion-lifespan-coordinator-review-2026-10-18.json) retain source versions and the exact scope of each check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8f09c7c42ac94240**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
