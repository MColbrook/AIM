# 958. Can ACF blow-up slopes vary while the interface normal stays fixed?

**Area:** Two-phase free boundaries and blow-up limits
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`u_+,u_-\geq0`$ be continuous on a ball $`B_2\subset\mathbb{R}^n`$, $`n\geq2`$, subharmonic on their respective positive sets, with disjoint positive sets and $`u_+(0)=u_-(0)=0`$. Suppose the Alt–Caffarelli–Friedman functional

```math
J(r)=r^{-4}\left(\int_{B_r}|\nabla u_+|^2|x|^{2-n}\,dx\right)\left(\int_{B_r}|\nabla u_-|^2|x|^{2-n}\,dx\right)
```


has a strictly positive limit as $`r\downarrow0`$. Subsequential blow-ups at the origin have the two-plane form $`c_+(x\cdot\nu)_+`$ and $`c_-(x\cdot\nu)_-`$ with $`c_+,c_->0`$ and a unit normal $`\nu`$.

Can one find such a pair for which *every* subsequential blow-up has the same normal $`\nu`$, but the amplitude pair $`(c_+,c_-)`$ differs between two subsequences?

## Application

Blow-ups describe the local geometry and growth of a two-phase interface. The question separates uniqueness of the tangent direction from uniqueness of the two phases' growth rates at a single point.

## References

1. E. Salato, [*A self-contained proof of the Alt-Caffarelli-Friedman monotonicity formula*](https://www.aimsciences.org/article/doi/10.3934/dcdss.2025156?viewType=HTML), *Discrete and Continuous Dynamical Systems - S* **20** (2026), 319–340; online 10 November 2025. See equations (1)–(2) and the explicit Problem in §6, p. 339.
2. M. Allen and D. Kriventsov, [*A spiral interface with positive Alt-Caffarelli-Friedman limit at the origin*](https://doi.org/10.2140/apde.2020.13.201), *Analysis & PDE* **13** (2020), 201–214. Their example varies the interface normal while keeping the slopes fixed; the converse is the question above.
3. M. Allen, D. Kriventsov and R. Neumayer, [*Rectifiability and uniqueness of blow-ups for points with positive Alt–Caffarelli–Friedman limit*](https://doi.org/10.1007/s00208-024-03077-3), *Mathematische Annalen* (2025/2026). It proves uniqueness at almost every point in the positive-limit set, not at every prescribed point.

## Status review


**Known cases:** Almost-everywhere blowup uniqueness leaves exceptional points. A rotating normal with fixed slopes does not answer the requested fixed-normal, varying-slope construction.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Almost-everywhere blowup uniqueness leaves exceptional points. A rotating normal with fixed slopes does not answer the requested fixed-normal, varying-slope construction.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The spiral construction demonstrates nonuniqueness of the normal with fixed slopes. The later almost-everywhere uniqueness theorem allows exceptional points, so it does not settle the fixed-normal, variable-slope construction. The [bounded exact-source, current-status and duplicate review](../FURTHER_problems/_tracking/acf-fixed-normal-variable-slope-status-2026-10-21.json) found no full published or announced resolution and no matching AIM/FURTHER entry.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e09a9c5e050ea1f5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
