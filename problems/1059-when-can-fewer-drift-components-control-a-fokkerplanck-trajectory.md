# 1059. When can fewer drift components control a Fokker–Planck trajectory?

**Area:** Control of parabolic partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\geq2`$, let $`\Omega\subset\mathbb R^d`$ be a smooth bounded domain, let $`T>0`$, and let $`\omega\subset\Omega`$ be a nonempty open actuator region. Fix a regular nonzero reference trajectory $`(\bar y,\bar u)`$ satisfying
```math
\partial_t\bar y=\Delta\bar y+\mathrm{div}(\bar u\bar y)
\quad\text{in }(0,T)\times\Omega,
\qquad \bar y=0\quad\text{on }(0,T)\times\partial\Omega.
```

For a constant matrix $`B\in\mathbb R^{d\times m}`$ with $`1\leq m<d`$, consider controls of the restricted form $`u=\bar u+Bv`$, where $`v\in L^\infty((0,T)\times\Omega)^m`$ is supported in $`(0,T)\times\omega`$. Characterize the pairs $`(\bar u,B)`$, together with any needed conditions on the reference trajectory and actuator region, for which the following local controllability property holds: for every $`\varepsilon>0`$ there is $`\eta>0`$ such that each initial datum $`y^0`$ with $`\|y^0-\bar y^0\|_{L^2(\Omega)}\leq\eta`$ admits such a perturbation $`v`$ with $`\|v\|_\infty\leq\varepsilon`$, and the resulting Dirichlet solution satisfies $`y(T)=\bar y(T)`$ and $`\|y-\bar y\|_{W(0,T)}\leq\varepsilon`$. Here $`W(0,T)=L^2(0,T;H_0^1(\Omega))\cap H^1(0,T;H^{-1}(\Omega))`$.

The task is to find a necessary and sufficient criterion for this property, under the regularity regime of [1, Theorem 1.3]. The stated goal is the characterization, not a claim that the particular sufficient rank test below is necessary.

## Application

The drift is a vector field with $`d`$ components, but an actuator may alter only $`m<d`$ combinations of them in one region. A sharp criterion would tell which reference flows allow this restricted intervention to steer nearby density profiles to the same terminal state.

## Known results

Theorem 1.3 of [1] gives a sufficient test: at one point $`(t_0,x_0)\in(0,T)\times\omega`$, the columns of $`B`$, together with all nonzero iterated directional derivatives of $`\bar u`$ along those columns, span $`\mathbb R^d`$. In Remark 1.4 the authors say this test may not be optimal and explicitly ask for a necessary and sufficient condition. Their Section 4 constructs an uncontrollable trajectory when the rank test fails in a particular way, without resolving the general converse.

## References

1. M. Duprez and P. Lissy, [*Bilinear local controllability to the trajectories of the Fokker–Planck equation with a localized control*](https://aif.centre-mersenne.org/item/10.5802/aif.3501.pdf), *Annales de l’Institut Fourier* **72** (2022), no. 4, 1621–1659, §1.2, equations (1.1), (1.4)–(1.6), Theorem 1.3 and Remark 1.4, printed pp. 1622 and 1624–1627. [DOI](https://doi.org/10.5802/aif.3501).
2. F. Alabau-Boussouira, P. Cannarsa and C. Urbani, [*Bilinear control of evolution equations with unbounded lower order terms. Application to the Fokker–Planck equation*](https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.567/), *Comptes Rendus Mathématique* **362** (2024), 511–545. Its time-only scalar-control setting is distinct from the localized reduced-component question above.

## Status review


**Known cases:** A necessary and sufficient reduced-component criterion is requested. The source rank test is only sufficient; time-only scalar bilinear control results have a different actuator model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A necessary and sufficient reduced-component criterion is requested. The source rank test is only sufficient; time-only scalar bilinear control results have a different actuator model.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source-body, later-work, status and duplicate review](../FURTHER_problems/_tracking/fokker-planck-reduced-drift-characterization-status-2026-10-21.json) checked the exact published question against later results and the existing AIM and FURTHER problems through 21 October 2026. No complete criterion for this setting was located; the search is bounded.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b8af69adc1aeae29**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
