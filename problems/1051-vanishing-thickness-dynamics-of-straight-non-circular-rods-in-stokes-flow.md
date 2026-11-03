# 1051. Vanishing-thickness dynamics of straight non-circular rods in Stokes flow

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider several separated rigid filaments in a smooth three-dimensional background flow governed by the steady Stokes equations. Each filament has fixed volumetric density and thickness $`\varepsilon\to0`$. Höfer, Prange and Sueur [1, Theorem 3.4] establish the limiting coupled fluid–solid dynamics for smooth centre-lines with **nowhere-vanishing curvature**.

Can a corresponding convergence theorem, including the limiting rotational dynamics, be proved when the centre-lines are **line segments and the rod cross-sections are non-circular**? This is the delicate subcase of their Open Problem 3.6 [1, p. 345]. In this geometry, the resistance to spinning about a rod's axis is of order $`\varepsilon^2`$, while the nondegenerate resistance modes in the original analysis scale as $`|\log\varepsilon|^{-1}`$. Thus the limiting resistance matrix used for the curved case cannot simply be inverted for every rotational degree of freedom.

## Application

Straight fibres with non-circular cross-sections occur in suspensions and microfluidic models. A rigorous limit would distinguish their orientation and spin effects from those captured by curved-filament asymptotics, while controlling the fluid–solid coupling as the thickness vanishes.

## References

1. R. M. Höfer, C. Prange and F. Sueur, [*Motion of several slender rigid filaments in a Stokes flow*](https://www.numdam.org/item/10.5802/jep.184.pdf), *Journal de l'École polytechnique — Mathématiques* **9** (2022), 327–380, [DOI 10.5802/jep.184](https://doi.org/10.5802/jep.184). Theorem 3.4 (printed p. 339), Section 3.8 and Open Problem 3.6 (printed p. 345).
2. N. S. Borker and D. L. Koch, [*Slender body theory for particles with non-circular cross-sections*](https://doi.org/10.1017/jfm.2019.625), *Journal of Fluid Mechanics* **877** (2019), 1098–1133. Related force/resistance asymptotics and straight-rod motions in imposed shear; this does not establish the multi-body finite-density limit in [1].

## Status review


**Known cases:** The multi-body finite-density limit must include axial rotation of straight noncircular rods. Curved-filament limits and prescribed-flow resistance approximations do not address the degenerate rotational mode.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The multi-body finite-density limit must include axial rotation of straight noncircular rods. Curved-filament limits and prescribed-flow resistance approximations do not address the degenerate rotational mode.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded source, status and duplicate audit](../FURTHER_problems/_tracking/straight-noncircular-stokes-filament-status-2026-10-22.json) checks the original problem against later work, announcements and the AIM/FURTHER catalogues through 22 October 2026. No theorem covering this precise Newton–Stokes limit was located. This is a bounded search assessment, not proof of open status.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-84d9f1f53f8973ec**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
