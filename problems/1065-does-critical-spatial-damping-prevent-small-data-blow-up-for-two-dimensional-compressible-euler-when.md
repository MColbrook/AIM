# 1065. Does critical spatial damping prevent small-data blow-up for two-dimensional compressible Euler when its strength exceeds one?

**Area:** Nonlinear hyperbolic PDE and compressible flow
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`x\in\mathbb R^2`$, consider the isentropic compressible Euler system with critical space-dependent damping

```math
\rho_t+\nabla\!\cdot(\rho u)=0,\qquad
(\rho u)_t+\nabla\!\cdot(\rho u\otimes u)+\nabla(\rho^\gamma/\gamma)
+\frac{\mu\rho u}{1+|x|}=0,
```

where $`\gamma\ge2`$ and $`\mu>1`$. For smooth, compactly supported perturbations of the constant state, $`\rho(0,x)=1+\varepsilon\rho_0(x)>0`$ and $`u(0,x)=\varepsilon u_0(x)`$ with $`\mathrm{curl}u_0=0`$, does every sufficiently small $`\varepsilon>0`$ give a global classical solution? We retain the pressure normalization $`P=\rho^\gamma/\gamma`$ used for the cited paper's critical value $`\mu=1`$. A counterexample for any $`\mu>1`$ in this data class would refute the proposed spatial-damping analogue of the time-dependent threshold.

## Application

The cited paper proves finite-time blow-up for $`0<\mu\le1`$ at the critical spatial decay $`1/(1+|x|)`$, under a positive-moment condition on the initial perturbation. For the corresponding time-dependent damping $`\mu/(1+t)`$, small-data global existence is known on the $`\mu>1`$ side in two dimensions. Remark 1.2 of the spatial paper expects the same threshold and lifespan pattern but says this remains to be confirmed. The question above isolates the unproved global-existence side; it does not assert that the spatial and temporal equations are interchangeable.

## References

- J. Zhou, L. Ma and N.-A. Lai, [*Blow-up for the compressible Euler system with critical space-dependent damping in $`\mathbb R^2`$*](https://doi.org/10.3934/dcdss.2026153), *Discrete Contin. Dyn. Syst. Ser. S* **29** (2026), 673–687. See system (1) on printed p. 673, Theorem 1.1 on pp. 675–676 and Remark 1.2 on p. 676.
- F. Hou and H. Yin, [*On the global existence and blowup of smooth solutions to the multi-dimensional compressible Euler equations with time-depending damping*](https://doi.org/10.1088/1361-6544/aa6d93), *Nonlinearity* **30** (2017), 2485–2517. Its two-dimensional $`\mu>1`$ global result assumes curl-free initial velocity and **time**-dependent damping; it provides the comparison, not a solution of the spatial problem.

## Status review


**Known cases:** The damping is mu/(1+|x|) in two dimensions with mu>1. Critical time-damping, one-dimensional spatiotemporal models and blowup for mu<=1 do not decide the proposed spatial small-data threshold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The damping is mu/(1+|x|) in two dimensions with mu>1. Critical time-damping, one-dimensional spatiotemporal models and blowup for mu<=1 do not decide the proposed spatial small-data threshold.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source's Remark 1.2 is an expectation rather than a theorem. The 2026 paper settles a blow-up range $`0<\mu\le1`$ under additional data conditions, leaving the general small-data $`\mu>1`$ spatial case open within its analysis. Bounded searches through 22 October 2026 for the exact DOI/title, its authors, the critical $`1/(1+|x|)`$ coefficient, small-data global existence and announced follow-ups found no matching resolution. One-dimensional spatial or spatiotemporal damping results and two-dimensional **time**-damping results have different hypotheses. This bounded search does not certify exhaustive present-day openness. The [body receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0666-J346-cached-backfill-body-review.json), [status check](../FURTHER_problems/_tracking/euler-critical-spatial-damping-status-2026-10-22.json) and [duplicate check](../FURTHER_problems/_tracking/euler-critical-spatial-damping-duplicates-2026-10-22.json) record the scope.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f53021b2c4ee4885**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
