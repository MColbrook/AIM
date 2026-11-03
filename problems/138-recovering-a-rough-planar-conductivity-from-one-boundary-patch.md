# 138. Recovering a rough planar conductivity from one boundary patch

**Area:** Inverse problems and imaging
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded connected domain with $`C^\infty`$ boundary, and let $`\Gamma\subset\partial\Omega`$ be any nonempty relatively open set. Suppose $`\gamma_1,\gamma_2\in L^\infty(\Omega;\mathbb R)`$ satisfy
```math
0<c\le\gamma_j(x)\le C<\infty\quad\text{for almost every }x\in\Omega,
 \qquad j=1,2.
```

For $`f\in C_c^\infty(\Gamma;\mathbb R)`$, extended by zero to the rest of the boundary, let $`u_{j,f}\in H^1(\Omega)`$ be the unique weak solution of
```math
\nabla\cdot(\gamma_j\nabla u_{j,f})=0,
 \qquad \mathrm{Tr}u_{j,f}=f.
```

For $`h\in C_c^\infty(\Gamma;\mathbb R)`$, define the local voltage-to-current measurement by
```math
B_j(f,h)=\int_\Omega\gamma_j\nabla u_{j,f}\cdot\nabla v_h\,dx,
```

where $`v_h\in H^1(\Omega)`$ is any function of trace $`h`$. The weak equation makes this independent of the chosen extension.

**Problem.** Does
```math
B_1(f,h)=B_2(f,h)\quad\text{for every }f,h\in C_c^\infty(\Gamma;\mathbb R)
 \quad\Longrightarrow\quad\gamma_1=\gamma_2\ \text{almost everywhere in }\Omega?
```

No continuity, known partition, agreement near the boundary, or prior boundary values of either conductivity are assumed. The domain need not be simply connected. Both voltages and current observations use the same arbitrary patch.

## Application

In electrical impedance imaging, part of an object's surface may be inaccessible. This asks whether ideal measurements on one accessible patch can distinguish arbitrary bounded heterogeneous planar conductors without assuming a known outer layer.

## References

1. C. Kenig and M. Salo, *Recent progress in the Calderón problem with partial data*, [primary author manuscript](https://users.jyu.fi/~salomi/pub/calderon_partial_survey3.pdf), §8, Question 3, p. 32; [arXiv:1302.4218](https://arxiv.org/abs/1302.4218). The opening section defines the weak local Cauchy data.
2. G. Uhlmann and P. Zimmermann, *Fractional Calderón problem with $`L^\infty`$-conductivities*, [arXiv:2610.17524v1](https://arxiv.org/html/2610.17524v1), 13 October 2026, equations (1.8)–(1.14) and §1.1. This recent result concerns a different nonlocal operator and exterior observations.

3. K. Astala, M. Lassas and L. Päivärinta, *Calderón’s inverse problem for anisotropic conductivity in the plane*, Communications in Partial Differential Equations **30** (2005), 207–224; [primary preprint](https://arxiv.org/html/math/0401410v1), §2.3 and Theorem 2.3.
4. K. Astala and L. Päivärinta, *Calderón’s inverse conductivity problem in the plane*, Annals of Mathematics **163** (2006), 265–299; [published record](https://annals.math.princeton.edu/2006/163-1/p05). This is the full-boundary result.

## Status review


**Known cases:** Full-boundary rough planar uniqueness, local smooth uniqueness and fractional exterior-data results have different hypotheses. The earlier anisotropic planar local theorem uses both local DN and ND maps; it does not establish this one arbitrary-patch map for L-infinity conductivities.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The source asks this precise question separately from higher-dimensional and smooth local-data problems. Full-boundary planar rough uniqueness and sufficiently regular planar local uniqueness leave the displayed combination of rough coefficients and arbitrary local data unresolved in the checks made here. Results imposing homogeneity near the whole boundary use an assumption absent above.

Checks through 17 October 2026 distinguish the question from AIM 046's three-dimensional full-boundary counterexample, AIM 048's smooth higher-dimensional same-patch problem, and fractional exterior-data uniqueness. No complete resolution of this precise statement was located. The independent selected-primary audit and catalogue comparison support inclusion at their recorded extents; this is a literature check, not a proof of openness. [Review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/planar-rough-local-calderon-review.json).

Reference3 requires both local voltage-to-current and current-to-voltage maps. Its reflection proof uses the two maps for different solution families. Inverting a compressed boundary map does not supply the second datum; planar harmonic conjugation instead relates the conductivity to its reciprocal. Thus that result does not already prove the displayed one-map statement.

All six returned contexts from the186-page combined catalogue scan were read by the owner and coordinator. The closest announcement concerns three-dimensional full-boundary nonuniqueness, with the planar full-boundary theorem cited as background. No equivalent local planar target was found; complete mission proofs were not audited.

[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-planar-rough-local-calderon-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/planar-calderon-prove2-0119-review.json) and [coordinator review](../FURTHER_problems/_tracking/planar-local-calderon-coordinator-review-2026-10-17.json) preserve exact assumptions, version limits and bounded current searches.


### Online recheck, 2026-10-30

Full-boundary rough planar uniqueness, local smooth uniqueness and fractional exterior-data results have different hypotheses. The earlier anisotropic planar local theorem uses both local DN and ND maps; it does not establish this one arbitrary-patch map for L-infinity conductivities.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.17524); [status source 2](https://arxiv.org/abs/math/0401410); [status source 3](https://arxiv.org/abs/1302.4218). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-b42858ef6d500422** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
