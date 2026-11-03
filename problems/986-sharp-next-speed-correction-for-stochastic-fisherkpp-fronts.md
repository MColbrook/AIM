# 986. Sharp next speed correction for stochastic Fisher–KPP fronts

**Area:** Stochastic partial differential equations and population fronts
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On the real line, consider the stochastic Fisher–KPP equation
```math
\partial_t u_\epsilon
=\partial_x^2u_\epsilon+u_\epsilon(1-u_\epsilon)
+\epsilon\sqrt{u_\epsilon(1-u_\epsilon)}\,\dot W,
\qquad t>0,\ x\in\mathbb R,
```
where $`\dot W`$ is Gaussian space–time white noise with covariance
$`\delta(t-s)\delta(x-y)`$, and the stochastic integral is interpreted in the Itô–Walsh sense. Fix the continuous initial profile
```math
u_\epsilon(0,x)=
\begin{cases}
1,&x\leq0,\\
1-x,&0<x<1,\\
0,&x\geq1.
\end{cases}
```

For each $`\epsilon>0`$, take the $`[0,1]`$-valued solution, which is unique in law. Its right edge and deterministic asymptotic speed are
```math
R_\epsilon(t)=\sup\{x\in\mathbb R:u_\epsilon(t,x)>0\},
\qquad
v_\epsilon=\lim_{t\to\infty}\frac{R_\epsilon(t)}t
\quad\text{almost surely}.
```
The compact-interface property and existence of this speed are known; see [3, Theorem 2.1], which recalls the results of [4].

For $`0<\epsilon<e^{-1}`$, set $`L_\epsilon=\log(\epsilon^{-2})`$. Is it true that
```math
\lim_{\epsilon\downarrow0}
\frac{L_\epsilon^3}{\log L_\epsilon}
\left(v_\epsilon-2+\frac{\pi^2}{L_\epsilon^2}\right)
=6\pi^2\,?
```

This is a precise canonical case of the next-order prediction in [2, Eq. (1.28)], based on the phenomenological theory in [1]. The factor $`\log|\log\epsilon|`$ used there equals $`\log(L_\epsilon/2)`$, so replacing it by $`\log L_\epsilon`$ gives the same limit. The constant $`2`$ is the deterministic minimal Fisher–KPP travelling-wave speed; no support-edge speed at zero noise is being defined.

## Application

The equation models the spread of an advantageous genetic type along a one-dimensional habitat, including demographic fluctuations. The proposed coefficient would quantify the next effect of weak noise on the invasion speed beyond the established leading slowdown.

## References

1. É. Brunet, B. Derrida, A. H. Mueller and S. Munier, *Phenomenological theory giving the full statistics of the position of fluctuating pulled fronts*, Physical Review E 73(5) (2006), 056126. [DOI](https://doi.org/10.1103/PhysRevE.73.056126), [author version](https://arxiv.org/abs/cond-mat/0512021). The prediction is phenomenological.
2. C. Mueller, L. Mytnik and J. Quastel, *Effect of noise on front propagation in reaction-diffusion equations of KPP type*, Inventiones Mathematicae 184(2) (2011), 405–453. [DOI](https://doi.org/10.1007/s00222-010-0292-5), [arXiv version](https://arxiv.org/abs/0902.3423v1). Equation (1.28) is on p. 6 of this arXiv version; Theorem 1.1 is on p. 8. The Fisher drift and Wright–Fisher variance are Eqs. (1.9)–(1.10).
3. C. Barnes, L. Mytnik and Z. Sun, *Effect of small noise on the speed of reaction-diffusion equations with non-Lipschitz drift*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 60(4) (2024), 2382–2414. [DOI](https://doi.org/10.1214/23-AIHP1393), [author-hosted article](https://zhenyao-sun.github.io/Files/Papers/2024AIHP.pdf). See Theorem 2.1 for the solution and speed, and Theorem 1.1 for the separate non-Lipschitz-drift estimates.
4. C. Mueller, L. Mytnik and L. Ryzhik, *The Speed of a Random Front for Stochastic Reaction–Diffusion Equations with Strong Noise*, Communications in Mathematical Physics 384 (2021), 699–732. [DOI](https://doi.org/10.1007/s00220-021-04084-0).
5. P. Maillard, *Speed and fluctuations of N-particle branching Brownian motion with spatial selection*, Probability Theory and Related Fields 166 (2016), 1061–1173. [DOI](https://doi.org/10.1007/s00440-016-0701-9), [arXiv:1304.0562v4](https://arxiv.org/abs/1304.0562v4) (2018), Theorem 1.1 and §1.3.

## Status review


**Known cases:** The precise next logarithmic correction for the stochastic Wright-Fisher-noise equation is needed. Leading Brunet-Derrida speed estimates, deterministic Bramson delays and non-Lipschitz drift front results do not identify this limit.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The precise next logarithmic correction for the stochastic Wright-Fisher-noise equation is needed. Leading Brunet-Derrida speed estimates, deterministic Bramson delays and non-Lipschitz drift front results do not identify this limit.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The leading Brunet–Derrida correction is proved in [2], with remainder $`O(\log L_\epsilon/L_\epsilon^3)`$. Those bounds do not determine the displayed coefficient. The matched power-law estimates in [3] concern drifts comparable to $`u^p`$ with $`p<1`$; they do not settle this sharper Fisher-drift limit.

The particle-model theorem in [5] concerns finite-dimensional fluctuations on time scales of order $`\log^3N`$. Its §1.3 explicitly distinguishes that result from a stationary long-time speed limit. It does not establish the displayed SPDE limit.

Current and announced-resolution searches on 27 October 2026 located no matching complete solution. The all-status AIM collection, indexed OpenAI announcements and developing collection were checked for equivalent formulations. These are bounded negative checks; the dated review records exact versions and the limits of access and reading.

Review evidence: [dated source, current-status and duplicate-comparison record](../FURTHER_problems/_tracking/C133-073-noisy-KPP-next-speed-coefficient-C-gate-20261027/KPP-OWNER-READY-PROPOSAL.json).

Independent review: [exact formulation, speed normalization and all-status model comparison](../FURTHER_problems/_tracking/C133-KPP-root-independent-admission-gate-20261027/ROOT-INDEPENDENT-MODEL-SPEED-NORMALIZATION-CURRENT-AND-DUPLICATE-PASS.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b3b560471ca4b36b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
