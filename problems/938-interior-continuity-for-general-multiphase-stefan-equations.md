# 938. Interior continuity for general multiphase Stefan equations

**Area:** Degenerate parabolic PDEs / phase transitions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge3`$, let $`E\subset\mathbb R^N`$ be open, and let $`T>0`$. Let $`\beta:\mathbb R\rightrightarrows\mathbb R`$ be a maximal monotone graph with domain $`\mathbb R`$, bounded on bounded sets:
```math
\sup_{|s|\le M}\sup_{v\in\beta(s)}|v|<\infty\qquad(M>0).
```
Assume that some $`\alpha_0>0`$ satisfies
```math
(v_1-v_2)(s_1-s_2)\ge\alpha_0|s_1-s_2|^2
\quad\bigl((s_i,v_i)\in\beta,\ i=1,2\bigr).
```
Thus finite jumps, accumulating singularities and singular continuous parts are allowed; no prescribed formula for $`\beta`$ is imposed.

Let $`\mathbf A:E\times(0,T)\times\mathbb R\times\mathbb R^N\to\mathbb R^N`$ be measurable in $`(x,t)`$, continuous in $`(z,\xi)`$ for almost every $`(x,t)`$, and satisfy, for fixed $`0<\lambda\le\Lambda<\infty`$,
```math
\mathbf A(x,t,z,\xi)\cdot\xi\ge\lambda|\xi|^2,
\qquad |\mathbf A(x,t,z,\xi)|\le\Lambda|\xi|.
```

Consider any locally bounded
```math
u\in L^2_{\mathrm{loc}}\bigl((0,T);W^{1,2}_{\mathrm{loc}}(E)\bigr)
```
with a measurable selection $`w(x,t)\in\beta(u(x,t))`$, weakly continuous as a map into $`L^2_{\mathrm{loc}}(E)`$, satisfying
```math
\int_E w\varphi\,dx\Big|_{t_1}^{t_2}
+\int_{t_1}^{t_2}\!\int_E
\left[-w\,\partial_t\varphi+
\mathbf A(x,t,u,\nabla u)\cdot\nabla\varphi\right]dx\,dt=0.
```
Here $`0<t_1<t_2<T`$, and $`\varphi`$ is any smooth test function with spatial support compactly contained in $`E`$, defined on $`[t_1,t_2]`$.

Must $`u`$ have a representative jointly continuous on $`E\times(0,T)`$?

This is the homogeneous, quadratic-growth subproblem of the general question in [1]. It concerns interior continuity of every bounded energy weak solution. No boundary regularity, Hölder exponent or uniform modulus over all graphs is requested.

## Application

The temperature is $`u`$, while $`w`$ represents enthalpy. A graph with several jumps models several phase changes. The question asks whether rough, spatially and temporally varying diffusion can produce a temperature discontinuity when the enthalpy graph has unrestricted singularities.

## Known progress and scope

The original source proves continuity in two space dimensions for general graphs, and in higher dimensions for particular diffusion operators or enthalpy graphs [1]. Part I and Part II of Gianazza–Liao cover broad but structured graphs, including finitely many singularities within a bounded temperature range [2,3]. Part III allows general strongly monotone graphs but assumes $`p\ge\max\{2,N\}`$ for diffusion with $`p`$-growth [4]. With the solution/approximation framework stated there, its theorem does not include $`p=2<N`$.

The 2026 improvement of Stefan continuity moduli treats a single-jump enthalpy and $`p>2`$ [5]. These results do not establish the stated arbitrary-graph, quadratic-growth assertion. A bounded search found no matching later proof or announced solution; this is not a guarantee that none exists.

## References

1. E. DiBenedetto, J. M. Urbano and V. Vespri, *Current issues on singular and degenerate evolution equations*, Coimbra Preprint 03–24 (2003), [author-department manuscript](https://www.mat.uc.pt/preprints/ps/p0324.pdf#page=11), §1.4 and §5, especially (5.1)–(5.3), (5.15)–(5.16), Theorems 5.6–5.7 and §5.4.6. An associated chapter appears in *Handbook of Differential Equations: Evolutionary Equations*, vol. I, pp.169–286, [DOI](https://doi.org/10.1016/S1874-5717(04)80005-7). The eligible source here is the 2003 manuscript; edition parity is not assumed.
2. U. Gianazza and N. Liao, *Continuity of the temperature in a multi-phase transition problem*, Math. Ann. 384 (2022), 211–245; online 2021, [DOI](https://doi.org/10.1007/s00208-021-02255-x), (1.2)–(1.5), Theorem 1.1 and §1.2.
3. U. Gianazza and N. Liao, *Continuity of the temperature in a multi-phase transition problem. Part II*, Interfaces Free Bound. 26 (2024), 625–674, [DOI](https://doi.org/10.4171/IFB/522), (1.2)–(1.8), Theorem 1.1 and §1.2.
4. U. Gianazza and N. Liao, *Continuity of the Temperature in a Multi-Phase Transition Problem. Part III*, J. Anal. Math. 150 (2023), 583–607, [DOI](https://doi.org/10.1007/s11854-023-0283-2), (1.2)–(1.5), Theorem 1.1 and §1.2.
5. U. Gianazza, N. Liao and J. M. Urbano, *Improved Moduli of Continuity for Degenerate Phase Transitions*, Ann. PDE 12, 27 (2026), [DOI](https://doi.org/10.1007/s40818-026-00253-3); [arXiv:2408.11555v1](https://arxiv.org/html/2408.11555v1), (1.1)–(1.3), Theorem 1.1. The selected arXiv body and publisher metadata were checked separately; final-layout parity is not asserted.

## Status review


**Known cases:** Arbitrary strongly monotone graphs may include accumulating jumps and singular continuous parts. The cited 2026 phase-transition estimates concern structured graphs; no matching all-graph theorem or full announcement found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Arbitrary strongly monotone graphs may include accumulating jumps and singular continuous parts. The cited 2026 phase-transition estimates concern structured graphs; no matching all-graph theorem or full announcement found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check:** The original general question and the quadratic-growth residual were checked against the stated source hypotheses. The cited later theorems cover structured graphs, different growth ranges, or different coefficient and solution assumptions; none of the checked statements covers this entire formulation. Bounded searches through 25 October 2026 located no matching full proof or announced solution.

**Duplicate check:** The all-status AIM/OpenAI index and the 887-record FURTHER findings export were compared by scientific target. Scalar enthalpy-graph continuity is distinct from fractional-pressure or time-memory porous-medium flow, Maxwell-Stefan systems, classical interface control, and stability of melting profiles. The independent root comparison is retained in the tracking records.

**Limits:** The live Prove2Me check and the older linear-comparator full-body route remain recorded access gaps. No exhaustive absence, full proof audit, or edition parity is claimed.

**Admission review:** 25 October 2026. The recorded primary-statement, current-status and semantic duplicate checks were completed before admission. Public AIM-head and complete OpenAI-CONTENTS comparisons were refreshed without a change. The dated, bounded search and access limits above remain part of this assessment.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2225ba9dafbab48f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
