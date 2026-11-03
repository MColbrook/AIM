# 943. Bounded-potential Schrödinger observability on higher-dimensional tori

**Area:** Schrödinger equations and control theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge4`$, let $`\mathbb T^d=\mathbb R^d/(2\pi\mathbb Z)^d`$, and fix a real, time-independent potential $`V\in L^\infty(\mathbb T^d;\mathbb R)`$. On complex $`L^2(\mathbb T^d)`$, define the self-adjoint operator
```math
H_V=-\Delta+V,\qquad D(H_V)=H^2(\mathbb T^d).
```

For every nonempty open set $`\omega\subset\mathbb T^d`$ and every $`T>0`$, does a finite constant $`C=C(d,V,\omega,T)`$ exist such that
```math
\|u_0\|_{L^2(\mathbb T^d)}^2
\le C\int_0^T\int_\omega
  |e^{-itH_V}u_0(x)|^2\,dx\,dt
\qquad\text{for all }u_0\in L^2(\mathbb T^d)?
```


The constant may depend on the fixed potential, observation set and time. No uniform bound over all bounded potentials, geometric control condition, regularity beyond essential boundedness, or positive lower bound on $`T`$ is imposed.

The free case is known in all dimensions. Bounded Riemann-integrable potentials are also covered in all dimensions, and arbitrary bounded potentials are covered in dimensions at most three [1–3]. The remaining question concerns arbitrary bounded measurable potentials in dimensions at least four.

## Application

This estimate controls the global initial $`L^2`$ state by its space-time observation on a spatial subregion. Through the Hilbert uniqueness method, it gives internal exact controllability for the corresponding linear Schrödinger equation [1,3]. The observation is the wave field in $`L^2`$; no phase reconstruction from intensity-only data is asserted.

## References

1. J. Bourgain, N. Burq and M. Zworski, *Control for Schrödinger operators on 2-tori: rough potentials*, J. Eur. Math. Soc. **15** (2013), 1597–1628, DOI [10.4171/JEMS/399](https://doi.org/10.4171/JEMS/399). Abstract, equation (1.2), Theorem 2 and Theorem 3.
2. J. Bourgain, *On the Control Problem for Schrödinger Operators on Tori*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics **2116** (2014), 97–105, DOI [10.1007/978-3-319-09477-9_8](https://doi.org/10.1007/978-3-319-09477-9_8). Three-dimensional bounded-potential result; see also [3, §1.5.2].
3. N. Burq and H. Zhu, *Observability of Schrödinger propagators on tori in rough settings*, [arXiv:2509.23965v2](https://arxiv.org/abs/2509.23965v2), 22 October 2025. Section 1.1, Theorem 1.2 and §1.5.2/Table 1.2.
4. K. Le Balc’h and J. Yu, *Quantitative observability of the Schrödinger equation in the torus from open sets*, [arXiv:2605.02480v3](https://arxiv.org/abs/2605.02480v3), 16 September 2026. The current version replaces the earlier potential claim in [v1](https://arxiv.org/abs/2605.02480v1); the official version history reports its loss after a proof gap.
5. G. Wang and M. Wang, *Controllable subspaces and real-part observability for Schrödinger equations on $`\mathbb T^d`$*, [arXiv:2608.04357v1](https://arxiv.org/abs/2608.04357v1), 5 August 2026. Section 1.2 and Theorem 1.1 assume continuous real potentials.
6. N. Burq, P. Germain, M. Sorella and H. Zhu, *Trace and observability inequalities for Laplace eigenfunctions on the torus*, Forum Math. Sigma **14** (2026), e47, DOI [10.1017/fms.2026.10199](https://doi.org/10.1017/fms.2026.10199). Stationary free-Laplacian estimates under conditions on the observation measure.

## Status review


**Known cases:** The official current arXiv record explicitly says the earlier bounded-potential theorem was lost because of a proof gap. Its stale v1 abstract is not an active resolution; continuous/Riemann-integrable and low-dimensional potential results are narrower.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The official current arXiv record explicitly says the earlier bounded-potential theorem was lost because of a proof gap. Its stale v1 abstract is not an active resolution; continuous/Riemann-integrable and low-dimensional potential results are narrower.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Earlier review status:** Open with partial progress in lower dimensions and for more regular potentials.

Checked on 24 October 2026. The original 2013 higher-dimensional question is retained with $`d\ge4`$: Bourgain’s later result settles the three-dimensional bounded-potential case [2,3]. Burq–Zhu’s current Theorem 1.2 imposes a specified approximation/algebra condition on the potential; it does not claim all bounded potentials [3].

A matching general result was claimed in Le Balc’h–Yu’s May 2026 v1, Theorem 1.2. Its v2 was withdrawn, and the official September v3 notice explicitly reports that the potential result was lost because of a proof gap. The actual v3 main theorem concerns $`V=0`$ [4]. Stale indexed copies of the v1 abstract therefore do not establish a current resolution. Wang–Wang’s real-part control theorem assumes continuous $`V`$ [5]; the stationary estimates in [6] concern a different model.

Current primary statements and version histories were inspected. Bounded current and announcement searches found no remaining matching complete solution or counterexample. Indexed Prove2Me queries found no matching entry; direct live-site access remains limited by the recorded timeouts. These searches do not prove that no unindexed result exists.

All-status comparisons distinguish AIM386’s dynamic boundary problem, AIM403’s sharp fast-control cost on an interval, AIM445’s time-dependent localization question on $`\mathbb R^3`$, and the recorded modified-Hautus counterexample. No equivalent AIM/OpenAI or FURTHER target was found in the inspected scientific comparisons. Only selected source and comparison passages were read; complete proofs were not certified.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-50129761e82a8bb6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
