# 879. Real-energy nullspace on nontrapping Lorentzian scattering spaces

**Area:** Mathematical relativity and spectral theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a connected compact smooth manifold with boundary, $`\dim M\ge2`$, and $`g`$ a smooth Lorentzian scattering metric. Locally its tangent frame is $`x^2\partial_x,x\partial_{y_j}`$, where $`x`$ defines the boundary. Let $`G`$ denote the dual metric quadratic form.

Impose the full source/sink hypotheses of Vasy, Section 2: the rescaled Hamilton flow has normally radial sources $`L_-`$ and sinks $`L_+`$ at base infinity, transverse to fiber infinity. Every characteristic orbit outside these sets tends to $`L_+`$ forward and $`L_-`$ backward, both on $`G=0`$ at fiber infinity and on $`G=\lambda`$ at base infinity.

For each real $`\lambda\ne0`$ satisfying these assumptions, must
```math
u\in\dot C^\infty(M),\qquad (\square_g-\lambda)u=0
\quad\Longrightarrow\quad u=0?
```

Here $`\dot C^\infty(M)`$ means smooth functions vanishing to every order at the boundary. Proposition 7 identifies this with the scalar Feynman/anti-Feynman nullspace question in Remark 6. The zero-energy threshold is excluded.

## Application

Injectivity removes the finite-dimensional obstruction to global limiting Feynman propagators for curved-spacetime wave equations.

## References

1. A. Vasy, [*Essential self-adjointness of the wave operator and the limiting absorption principle on Lorentzian scattering spaces*](https://arxiv.org/html/1712.09650v1), Sections 2 and 4, Theorem 5, Remark 6, Proposition 7; *Journal of Spectral Theory* **10** (2020), 439–461. [DOI](https://doi.org/10.4171/JST/301).
2. K. Taira, [*Limiting absorption principle and equivalence of Feynman propagators on asymptotically Minkowski spacetimes*](https://arxiv.org/html/2012.07946v2), Theorems 1.1 and 1.4; *Communications in Mathematical Physics* **388** (2021), 625–655. [DOI](https://doi.org/10.1007/s00220-021-04196-7).
3. Q. Jia, M. Molodyk and E. Sussman, [*The essential self-adjointness of the wave operator on radiative spacetimes*](https://doi.org/10.1007/s00220-025-05532-x), *Communications in Mathematical Physics* **407** (2026), 36, Theorems A–B.
4. M. Molodyk and A. Vasy, [*The Feynman propagator for massive Klein-Gordon fields on radiative asymptotically flat spacetimes*](https://arxiv.org/html/2510.04308v2), Theorem 1.1 and Sections 2.5 and 5.

## Status review


**Known cases:** Essential self-adjointness and nonreal resolvent invertibility do not exclude a rapidly decaying real-energy nullspace. Taira leaves possible embedded eigenvalues without extra assumptions. Radiative asymptotically flat invertibility theorems impose more structured asymptotics and causality than the general source/sink scattering model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Essential self-adjointness and nonreal resolvent invertibility do not exclude a rapidly decaying real-energy nullspace. Taira leaves possible embedded eigenvalues without extra assumptions. Radiative asymptotically flat invertibility theorems impose more structured asymptotics and causality than the general source/sink scattering model.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Taira's general limiting-absorption theorem retains possible embedded eigenvalues; their exclusion requires additional hypotheses. The 2026 self-adjointness/nonreal-parameter theorem does not settle real-energy injectivity. Molodyk–Vasy establish invertibility for more structured asymptotically flat geometries with additional causal assumptions.

The [coordinating review](../FURTHER_problems/_tracking/focused-scattering-wave-real-nullspace-J060-C182-C-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, latest-version, current-resolution/announcement and semantic duplicate checks, with an independent formulation review. The formulation uses the archived preprint's numbering; full published-body parity was not established. These bounded checks do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8d9fe01bb0bb14f0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
