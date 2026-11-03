# 812. What is the optimal power exponent for the four-corner Favard length?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`n\ge1`$, let
```math
C_n=\bigcup_{(a_1,\ldots,a_n)\in\{0,3\}^n}
\left[\sum_{j=1}^n a_j4^{-j},\ \sum_{j=1}^n a_j4^{-j}+4^{-n}\right],
\qquad K_n=C_n\times C_n.
```

For $`\pi_\theta(x,y)=x\cos\theta+y\sin\theta`$, define
```math
F_n=\frac1\pi\int_0^\pi |\pi_\theta(K_n)|\,d\theta,\qquad
\alpha_{\rm Fav}=\sup\left\{a\ge0:\ \exists C>0\
\forall n\ge1,\ F_n\le Cn^{-a}\right\}.
```

Here $`|\cdot|`$ is one-dimensional Lebesgue measure. Determine the exact value of $`\alpha_{\rm Fav}`$.

This is the power-exponent subproblem of the classical question about the decay of $`F_n`$, for this fixed deterministic construction. Determining the exponent need not determine logarithmic corrections or establish a bound at the supremum.

## Application

Favard length measures the average visible projection of a planar fractal. Up to normalization it also describes the probability that a randomly placed and oriented line hits the set. Quantitative projection estimates connect geometric measure theory, harmonic analysis and stochastic geometry.

## References

1. M. Bateman and A. Volberg, [*An estimate from below for the Buffon needle probability of the four-corner Cantor set*](https://arxiv.org/abs/0807.2953), arXiv:0807.2953v1 (2008), Section 1, definition (1.1) and Theorem 1. Published in *Mathematical Research Letters* **17** (2010), 959–967, [doi:10.4310/MRL.2010.v17.n5.a12](https://doi.org/10.4310/MRL.2010.v17.n5.a12).
2. T. Tao, [*Favard-length decay exponent*, Optimization Constants in Mathematics, constant 60](https://teorth.github.io/optimizationproblems/constants/60a.html), explicit supremum formulation; consulted 26 October 2026.
3. C. Marshall, [*Improved Power Laws for the Favard Length Problem in All Dimensions*](https://arxiv.org/abs/2509.02882v2), arXiv:2509.02882v2 (12 August 2026), Theorem 1.2 and Section 8.5.
4. Y. Lin, [*FavardLength*](https://github.com/CoolRmal/FavardLength/tree/66d2857d03e02e8b2f1488791787ba4352baa332), pinned public announcement and formal statements, commit 66d2857d03e02e8b2f1488791787ba4352baa332; README and Challenge.lean.
5. A. Chang, P. Shmerkin and V. Suomala, [*Sharp Favard Length of Random Cantor Sets*](https://doi.org/10.1007/s00039-026-00743-3), *Geometric and Functional Analysis* **36** (2026), 786–830, Section 1.1.

## Status review


**Known cases:** Recent improvements of power lower bounds for the admissible decay exponent do not determine its supremum. The log(n)/n lower bound on Favard length gives an upper constraint on the exponent, not matching sharpness. No complete determination of the optimal exponent was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Recent improvements of power lower bounds for the admissible decay exponent do not determine its supremum. The log(n)/n lower bound on Favard length gives an upper constraint on the exponent, not matching sharpness. No complete determination of the optimal exponent was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Bateman–Volberg prove $`F_n\ge c(\log n)/n`$, so $`\alpha_{\rm Fav}\le1`$. Exponent one is not admissible; its being the supremum would still be possible.

Marshall's current v2 gives $`F_n\lesssim_u n^{-1/5+u}`$ for each $`u>0`$. The pinned Lin repository announces the stronger admissible exponent $`156307/625000=0.2500912`$. These partial bounds do not determine $`\alpha_{\rm Fav}`$. We checked that announcement's definitions and theorem statements; we have not independently compiled or certified its proof.

The 2026 sharp results for random Cantor sets concern different constructions. The existing FURTHER problem about positive Favard length and analytic capacity concerns a general qualitative implication. Neither supplies this deterministic exponent.

Bounded searches of current papers, revisions, announcements and all-status AIM/FURTHER/OpenAI statements found no complete resolution or equivalent listed problem. The original arXiv body was read; parity with the final 2010 publication body remains unverified. The target is intentionally narrower than a complete sharp asymptotic formula.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8342a0aa285fd109**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
