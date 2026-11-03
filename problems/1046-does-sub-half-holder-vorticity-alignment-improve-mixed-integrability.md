# 1046. Does sub-half-Hölder vorticity alignment improve mixed integrability?

**Area:** Three-dimensional incompressible fluids and vortex stretching
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`u_0\in H^1(\mathbb R^3;\mathbb R^3)`$ be divergence-free and let $`u`$ be any Leray–Hopf solution on $`[0,T]`$ of the unforced, unit-viscosity three-dimensional Navier–Stokes equations on $`\mathbb R^3`$. Write $`\omega=\nabla\times u`$.

Do there exist fixed exponents $`0<\beta<1/2`$ and $`1\le s,r\le\infty`$ with

```math
\frac{2}{s}+\frac{3}{r}<\frac52
```

such that, whenever the vorticity directions obey a uniform coherence bound

```math
|\omega(x,t)\times\omega(y,t)|\le C|x-y|^\beta|\omega(x,t)|\,|\omega(y,t)|
```

for almost every $`x,y,t`$ and some finite constant $`C`$, one necessarily has $`\omega\in L^s(0,T;L^r(\mathbb R^3))`$? The exponents are chosen independently of the solution, data, $`T`$ and $`C`$. The product form states the source's sine-of-angle condition without dividing by zero-vorticity values.

## Application

The energy inequality gives $`\omega\in L^2_tL^2_x`$, which sits exactly on $`2/s+3/r=5/2`$. Any strict improvement in this scale would transfer geometric alignment into quantitative integrability. The known $`\beta=1/2`$ theorem gives regularity, while the question asks for a weaker alignment exponent and only an integrability gain.

## References

- H. Beirão da Veiga, [*Navier–Stokes equations: Some questions related to the direction of the vorticity*](https://doi.org/10.3934/dcdss.2019014), *Discrete Contin. Dyn. Syst. Ser. S* **12** (2019), 203–213, printed pp. 204–205, equations (4)–(6) and the explicitly labelled Problem. The source states the target for the vorticity $`\omega`$, not the velocity $`u`$.
- H. Beirão da Veiga, [*Open problems concerning the Hölder continuity of the direction of vorticity for the Navier–Stokes equations*](https://arxiv.org/abs/1604.08083), 2016 precursor. It gives the background for the half-Hölder threshold; the 2019 printed formulation above fixes the mixed-vorticity target used here.
- H. Beirão da Veiga and L. C. Berselli, [*On the regularizing effect of the vorticity direction in incompressible viscous flows*](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf), *Differential Integral Equations* **15** (2002), 345–356. This establishes the separate half-Hölder regularity threshold.
- Y. Do, A. Farhat, Z. Grujić and L. Xu, [*Oscillations and integrability of the vorticity in the 3D NS flows*](https://arxiv.org/abs/1801.09040), 2018. Its gain assumes additional blow-up-profile conditions.
- L. C. Berselli, [*On the vorticity direction and the regularity of 3D Navier–Stokes equations*](https://doi.org/10.1088/1361-6544/ace096), *Nonlinearity* **36** (2023), 4303–4313. Its small-jump criterion has a different directional hypothesis.

## Status review


**Known cases:** Fixed sub-half-Holder alignment exponents must force the specified improved mixed vorticity integrability for every unforced Leray-Hopf flow. Half-Holder regularity and conditional blowup-profile improvements do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Fixed sub-half-Holder alignment exponents must force the specified improved mixed vorticity integrability for every unforced Leray-Hopf flow. Half-Holder regularity and conditional blowup-profile improvements do not cover it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source's Proposition 1 assumes extra vorticity integrability and therefore does not prove the implication asked here. Later conditional/profile and small-jump results checked above have different premises. Searches through 22 October 2026 for the exact threshold, source question, later papers and announced claims found no matching full resolution. The [source-bound body receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0651-J346-cached-backfill-body-review.json), [status comparison](../FURTHER_problems/_tracking/vorticity-direction-integrability-status-2026-10-22.json) and [duplicate review](../FURTHER_problems/_tracking/vorticity-direction-integrability-duplicates-2026-10-22.json) record the scope and limits of these checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-3f514521b423ac52**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
