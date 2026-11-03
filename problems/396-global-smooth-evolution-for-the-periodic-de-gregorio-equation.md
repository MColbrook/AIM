# 396. Global smooth evolution for the periodic De Gregorio equation

**Area:** Nonlocal transport and mathematical fluid dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$ and let $`\omega_0\in C^\infty(\mathbb T;\mathbb R)`$ be arbitrary. Consider
```math
\partial_t\omega+u\partial_x\omega=\omega\partial_xu,\qquad
\partial_xu=H\omega,\qquad
\omega(0,x)=\omega_0(x).
```

Here $`H`$ is the periodic Hilbert transform:
```math
\widehat{Hf}(k)=-i\,\mathrm{sgn}(k)\widehat f(k),
\qquad \mathrm{sgn}(0)=0.
```

Fix the velocity by $`\widehat u(0)=0`$ and
$`\widehat u(k)=-|k|^{-1}\widehat\omega(k)`$ for $`k\ne0`$.

Does every such datum generate a unique smooth solution on $`[0,T]\times\mathbb T`$ for every finite $`T>0`$?

This is the inviscid equation with transport coefficient exactly one. There is no smallness, oddness, sign or zero-mean assumption on $`\omega_0`$. Growth as $`t\to\infty`$ is allowed.

## Application

The model isolates the competition between transport and vortex stretching. Understanding whether transport prevents finite-time singularities offers a tractable setting for studying mechanisms that also arise in three-dimensional fluid dynamics.

## References

1. J. Chen, [*On the regularity of the De Gregorio model for the 3D Euler equations*](https://doi.org/10.4171/JEMS/1399), Journal of the European Mathematical Society **27** (2025), 1619–1677. Equation (1.2), introduction at printed p.1620 and Theorems 1–3. [Published PDF](https://ems.press/content/serial-article-files/50203); [arXiv:2107.04777v2](https://arxiv.org/abs/2107.04777v2), 28 December 2021.
2. T. M. Elgindi, [*Dynamics of Ideal Fluid Flows*](https://doi.org/10.1137/25M1807137), Proceedings of the International Congress of Mathematicians 2026, Volume 5, pp.285–306, Section 6.2.
3. M. M. G. Pascual-Caballo, [*On the instability of De Gregorio excited states*](https://arxiv.org/abs/2610.03287v1), 2 October 2026, Theorems 1.1–1.2 and Section 1.2.
4. D. Huang, X. Qin, X. Wang and D. Wei, [*Self-similar finite-time blowups with smooth profiles of the generalized Constantin–Lax–Majda model*](https://arxiv.org/abs/2305.05895v5), version 5, 28 August 2024, equation (1.1), the definition of interior smoothness and Theorem 1.1.

## Status review


**Known cases:** The current periodic smooth-data De Gregorio problem is broader than symmetry/sign classes. Instability of excited states, lower-regularity periodic blowup and real-line self-similar profiles do not resolve arbitrary smooth data on the circle.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Checked 2026-10-23.** The general smooth-data conjecture is stated in [1]; its global theorem has a symmetry/sign restriction. Its lower-regularity periodic blow-up and smooth real-line blow-up do not answer the displayed question. The period and velocity gauge above are equivalent normalizations, checked by spatial rescaling and a time-dependent rotation.

The current survey [2] still expects smooth global regularity on the circle. The equations here follow [1,3]; [2]'s displayed $`H(u)`$ appears to be a typographical error.

Theorem 1.2 of [3] proves that small $`H^2`$ perturbations can leave a fixed $`H^1`$ neighborhood of an excited state. Finite escape from a neighborhood is not a finite-time singularity. The self-similar profiles of [4] are on the real line; “smooth” there includes smoothness only inside a compact support.

Independent review and all-status AIM/FURTHER comparisons found no equivalent entry. Bounded current proof and announcement searches found no matching complete resolution. Prove2Me's direct-access gap remains recorded; indexed queries are not a whole-site check.

[Coordinator review](../FURTHER_problems/_tracking/de-gregorio-circle-coordinator-review-2026-10-23.json) · [Duplicate review](../FURTHER_problems/_tracking/de-gregorio-circle-duplicate-review-2026-10-23.json) · [Independent review](../FURTHER_problems/_tracking/arxiv2703-De-Gregorio-independent-peer-audit-2026-10-23.json).


### Online recheck, 2026-10-30

The current periodic smooth-data De Gregorio problem is broader than symmetry/sign classes. Instability of excited states, lower-regularity periodic blowup and real-line self-similar profiles do not resolve arbitrary smooth data on the circle.

Comparators and current-status sources: [status source 1](https://doi.org/10.4171/JEMS/1399); [status source 2](https://arxiv.org/abs/2610.03287); [status source 3](https://arxiv.org/abs/2305.05895). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-e7a2717430ad22cf** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
