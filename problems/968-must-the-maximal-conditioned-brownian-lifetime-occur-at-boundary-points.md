# 968. Must the maximal conditioned Brownian lifetime occur at boundary points?

**Area:** Probability and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded, smooth, simply connected domain, and let $`G_\Omega`$ be the Dirichlet Green function of $`-\Delta`$. For distinct $`x,y\in\Omega`$ define

```math
L_\Omega(x,y)=\frac{\int_\Omega G_\Omega(x,z)G_\Omega(z,y)\,dz}{G_\Omega(x,y)}.
```


This is, up to the standard Brownian-generator normalization, the expected lifetime of Brownian motion started at $`x`$, conditioned to approach $`y`$ before exit. Does the supremum of $`L_\Omega(x,y)`$ over interior pairs equal the supremum of its limits at pairs of boundary points? Equivalently, can a pair of interior points give a strictly larger value than every boundary pair? For a general smooth domain, “opposite” is not an extra formal condition; only the boundary location is asserted.

## Application

The quotient compares a twice-iterated Green function with the ordinary Green function. Its maximum controls a positivity threshold for a coupled elliptic problem and describes the longest possible expected lifetime of the conditioned diffusion.

## Known scope

The boundary-pair property holds for disks and balls. For planar simply connected domains, an older theorem proves that **if one starting point is already on the boundary**, moving the other to the boundary does not lower the supremum. That does not settle the global interior-pair comparison. Multiply connected planar domains and simply connected domains in higher dimensions can violate the broader claim, which is why the question here is restricted to the planar simply connected case.

## References

1. G. Sweers, [*Positivity for the Navier bilaplace, an anti-eigenvalue and an expected lifetime*](https://www.aimsciences.org/article/doi/10.3934/dcdss.2014.7.839), *Discrete and Continuous Dynamical Systems - S* **7** (2014), 839–855, Section 5, Conjectures 3–4.
2. M. Erven, [*On the Lifetime of a Conditioned Brownian Motion*](https://kups.ub.uni-koeln.de/4565/), doctoral thesis, University of Cologne (2012), Section 3.5.2, Conjecture 3.33 and the multiply connected counterexample.
3. G. Sweers, [*On a conjecture for the 3G-function*](https://www.math.uni-hamburg.de/projekte/dmv2015/abstracts.html), DMV Annual Meeting abstract (2015), explicitly separates the open planar question from higher-dimensional counterexamples.
4. P. Griffin, T. McConnell and G. Verchota, [*Conditioned Brownian motion in simply connected planar domains*](https://www.numdam.org/article/AIHPB_1993__29_2_229_0.pdf), *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **29** (1993), 229–249; a partial boundary-start result.

## Status review


**Known cases:** The domain is smooth, planar and simply connected. Disk/lens and boundary-start results are partial; multiply connected and higher-dimensional counterexamples do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The domain is smooth, planar and simply connected. Disk/lens and boundary-start results are partial; multiply connected and higher-dimensional counterexamples do not cover it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

A [bounded source, announcement and semantic-duplicate review](../FURTHER_problems/_tracking/conditioned-brownian-planar-boundary-lifetime-status-2026-10-21.json) found no matching complete proof or counterexample for the stated smooth planar simply connected scope and no equivalent AIM/FURTHER problem. This search cannot rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-129bff4fcc8adc60**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
