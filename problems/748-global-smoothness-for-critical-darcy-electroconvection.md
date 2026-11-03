# 748. Global smoothness for critical Darcy electroconvection

**Area:** Electrochemistry and electrohydrodynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2`$. Write $`\Lambda=(-\Delta)^{1/2}`$, $`R=\nabla\Lambda^{-1}`$ and let $`\mathbb P`$ be the Leray projection onto divergence free periodic vector fields. The multipliers of $`\Lambda`$ and $`R`$ at the zero Fourier mode are zero, and the multiplier of $`\mathbb P`$ there is the identity.

For arbitrary real $`q_0\in C^\infty(\mathbb T^2)`$ with $`\int_{\mathbb T^2}q_0\,dx=0`$, consider

```math
\partial_tq+u\cdot\nabla q+\Lambda q=0,
\qquad u=-\mathbb P(qRq),
\qquad q(0)=q_0.
```

Does the unique local smooth solution remain smooth for all positive time? There is no smallness restriction on $`q_0`$. A precise continuation target is

```math
\sup_{0\le t\le T}\|q(t)\|_{H^3(\mathbb T^2)}<\infty
\quad\text{for every finite }T.
```

This is the critical dissipation exponent $`\Lambda`$, with no external magnetic field or added viscosity. The velocity is fixed instantaneously by the quadratic constitutive law above.

The source explicitly states that arbitrary data global smoothness remains open. Global weak solutions and global regularity for sufficiently small data are known. The corresponding result with stronger dissipation $`\Lambda^\alpha`$, $`\alpha>1`$, does not include this critical case. The critical surface quasigeostrophic equation has a different, linear velocity law.

## Application

The scalar $`q`$ represents surface charge in a thin conductive fluid sheet. Its three dimensional electric field produces forces on the sheet, while Darcy friction models flow through a porous medium. The question asks whether arbitrary smooth initial charge patterns produce a regular evolution throughout this electrohydrodynamic model.

## References

1. E. Abdo, P. Constantin, M. Ignatova and Q. Lin, *Electroconvection in a magnetic field*, Discrete and Continuous Dynamical Systems **54** (2026), 61–86. [DOI](https://doi.org/10.3934/dcds.2026023), [primary author manuscript](https://web.math.princeton.edu/~const/acil9.pdf), [arXiv](https://arxiv.org/abs/2508.07439v1). The author manuscript, PDF p. 3, equations (1.17)–(1.20) with $`B=0`$, explicitly states the open problem. All 22 pages were read; parity with the 26-page published version has not been checked.
2. E. Abdo and M. Ignatova, *On electroconvection in porous media*, Indiana University Mathematics Journal **72** (2023), 2593–2630. [DOI](https://doi.org/10.1512/iumj.2023.72.9572), [primary preprint](https://arxiv.org/abs/2204.00689v1). Equations (1)–(8), Section 9 and Theorem 7 specify the periodic model and small data result; Section 10 treats strictly stronger dissipation. All 28 preprint pages were read; parity with the 38-page published version has not been checked.

## Status review


**Known cases:** The source critical quadratic Darcy velocity law differs from linear-velocity SQG and from Nernst-Planck systems. Supercritical-power dissipation, small smooth data and the August weak entropy theorem do not yield arbitrary-data critical smoothness.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source critical quadratic Darcy velocity law differs from linear-velocity SQG and from Nernst-Planck systems. Supercritical-power dissipation, small smooth data and the August weak entropy theorem do not yield arbitrary-data critical smoothness.

Additional comparison sources: [comparison source 1](https://doi.org/10.3934/dcds.2026023); [comparison source 2](https://web.math.princeton.edu/~const/acil9.pdf); [comparison source 3](https://arxiv.org/abs/2508.07439v1); [comparison source 4](https://doi.org/10.1512/iumj.2023.72.9572); [comparison source 5](https://arxiv.org/abs/2204.00689v1); [comparison source 6](https://arxiv.org/html/2608.24312v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Current literature and announcement searches on 17 October 2026 located no matching resolution. The August 2026 entropy paper [arXiv:2608.24312v1](https://arxiv.org/html/2608.24312v1) concerns weak solutions and moment bounds, not arbitrary data smoothness. The AIM catalogue and OpenAI announcement snapshot had no matching target; the complete Prove2Me listing description scan returned no target aliases. An independent cross-review checked the exact constitutive law, Fourier signs, zero modes and continuation target against primary statements. See the [source review](../FURTHER_problems/_tracking/parallel/continuum/darcy-electroconvection-global-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-darcy-review.json). These are problem-scope and status checks; they do not certify every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ccbd62517f9f46d2**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
