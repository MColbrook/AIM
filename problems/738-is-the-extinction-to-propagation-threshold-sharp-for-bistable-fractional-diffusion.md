# 738. Is the extinction-to-propagation threshold sharp for bistable fractional diffusion?

**Area:** Fractional reaction-diffusion equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On the real line, consider $`u_t+(-\Delta)^\alpha u=f(u)`$ with $`0<\alpha<1`$, where $`f`$ is bistable, for example $`f(u)=r u(u-\theta)(1-u)`$ on $`0<u<1`$, with $`r>0`$ and $`0<\theta<1/2`$. Start from $`u(0,x)=(\theta+\varepsilon)\mathbf 1_{(-L,L)}(x)`$, where $`0<\varepsilon\leq1-\theta`$ and $`L>0`$.

For fixed $`\varepsilon`$, let $`L^{\mathrm{ext}}_\varepsilon`$ be the supremum of lengths for which $`u(t,\cdot)\to0`$ uniformly, and let $`L^{\mathrm{prop}}_\varepsilon`$ be the infimum of lengths for which $`u(t,\cdot)\to1`$ locally uniformly. Under the assumptions of Faye and Zhao, both thresholds are positive and finite. Must

```math
L^{\mathrm{ext}}_\varepsilon=L^{\mathrm{prop}}_\varepsilon
```


hold for every admissible $`\varepsilon`$, at least for the cubic bistable reaction above? This asks whether there is a single critical interval length separating extinction from propagation.

## Application

The equation models spatial invasion with long-range dispersal and an Allee-type reaction threshold. A sharp critical support size would determine exactly when a localized population dies out or spreads. Fractional dispersal is materially different from the ordinary Laplacian and from bounded convolution-kernel models.

## References

1. G. Faye and M. Zhao, [*The threshold phenomena for propagation in fractional Laplacian diffusion equations*](https://www.aimsciences.org/article/doi/10.3934/dcdss.2026099?viewType=HTML), *Discrete and Continuous Dynamical Systems - S*, early access 20 March 2026, DOI 10.3934/dcdss.2026099, introduction pp. 409-410 and Proposition 2.2 pp. 411-412. The publisher assigns the article to volume 31 (2027), pp. 407-430.
2. H. Zhang, Y. Li and X. Yang, [*Threshold solutions for nonlocal reaction diffusion equations*](https://arxiv.org/abs/2201.05049), *Communications in Mathematical Research* **38** (2022), 389-421. Its sharp transition uses a convolution-type dispersal operator.
3. L. Ma, H.-T. Niu and Z.-C. Wang, [*The spreading phenomenon of solutions for reaction-diffusion equations with fractional Laplacian*](https://doi.org/10.1016/j.aml.2025.109698), *Applied Mathematics Letters* **172** (2026), 109698. It proves spreading for sufficiently large initial support, without the sharp-threshold equality.

## Status review


**Known cases:** The question concerns equality of extinction and propagation thresholds for one-dimensional fractional diffusion at every amplitude. Local Laplacian sharp-threshold results and finite but separate fractional bounds do not establish it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The question concerns equality of extinction and propagation thresholds for one-dimensional fractional diffusion at every amplitude. Local Laplacian sharp-threshold results and finite but separate fractional bounds do not establish it.

Additional comparison sources: [comparison source 1](https://www.aimsciences.org/article/doi/10.3934/dcdss.2026099?viewType=HTML); [comparison source 2](https://arxiv.org/abs/2201.05049); [comparison source 3](https://doi.org/10.1016/j.aml.2025.109698). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Faye and Zhao establish separate finite extinction and propagation length thresholds and give quantitative bounds; their numerical figure suggests equality in a cubic example. The cited related results address different operators or only sufficiently large supports. A [bounded primary-source, announcement and duplicate review](../FURTHER_problems/_tracking/fractional-bistable-sharp-threshold-status-2026-10-21.json) found no full published or announced resolution and no matching AIM or FURTHER entry.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9d059c7a18c1a2fc**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
