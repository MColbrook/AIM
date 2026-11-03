# 1064. Endpoint wave Strichartz estimate in the planar Friedlander model

**Area:** Wave propagation and dispersive PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega=(0,\infty)\times\mathbb R`$, with Lebesgue measure $`dx\,dy`$. Let $`A`$ be the nonnegative self-adjoint Dirichlet realization of
```math
A=-\partial_x^2-(1+x)\partial_y^2.
```

More precisely, $`A`$ is associated with the closure of
```math
\mathfrak a(f,f)=\int_\Omega\bigl(|\partial_xf|^2+(1+x)|\partial_yf|^2\bigr)\,dx\,dy,
\qquad f\in C_c^\infty(\Omega).
```

Thus the wave equation is $`\partial_t^2u+Au=0`$, with $`u|_{x=0}=0`$.

Fix $`\chi\in C_c^\infty((1/2,2))`$ which equals $`1`$ on $`[3/4,3/2]`$. Do there exist $`T_0,h_0,C>0`$ such that, for every $`0<h<h_0`$ and every $`f\in L^2(\Omega)`$,
```math
h^{4/5}\left\|e^{it\sqrt A}\chi(h\sqrt A)f\right\|_{L^5((0,T_0);L^\infty(\Omega))}
\le C\|f\|_{L^2(\Omega)}?
```

The constants may depend on $`\chi`$, but must be independent of $`h`$ and $`f`$. The estimate concerns the full spectrally localized flow, without an additional restriction to a microlocal region.

## Application

This measures how strongly reflected waves can concentrate near a convex boundary when their amplitude is averaged in time. The endpoint would sharpen estimates used to study nonlinear waves and boundary-generated caustics.

## References

1. Oana Ivanovici, *Counterexamples to the Strichartz inequalities for the wave equation in general domains with boundary*, Journal of the European Mathematical Society **14** (2012), 1357–1388. [Article](https://doi.org/10.4171/JEMS/335). Equations (1.1)–(1.3), Remark 1.8 and the question on p. 1361.
2. Oana Ivanovici, Gilles Lebeau and Fabrice Planchon, *New counterexamples to Strichartz estimates for the wave equation on a 2D model convex domain*, Journal de l’École polytechnique — Mathématiques **8** (2021), 1133–1157. [Article](https://doi.org/10.5802/jep.168), [arXiv v2](https://arxiv.org/abs/2008.02716v2). Theorems 1–2 and Remark 1.2.
3. Oana Ivanovici, Gilles Lebeau and Fabrice Planchon, *Strichartz estimates for the wave equation on a 2D model convex domain*, Journal of Differential Equations **300** (2021), 830–880. [Article](https://doi.org/10.1016/j.jde.2021.08.011), [arXiv v2](https://arxiv.org/abs/2008.03598v2). Remark 1.1 fixes the operator and measure; Theorem 1 gives the positive range.

## Known progress

For spatial exponent $`r=\infty`$, the cited counterexamples require $`q\ge5`$, while the general positive estimate in the model is proved for $`q\ge36/7`$. The scaling exponent is $`\beta=2(1/2-1/r)-1/q`$, hence $`\beta=4/5`$ at $`(q,r)=(5,\infty)`$. The sources leave the endpoint even in a particular microlocal region.

The formulation uses one frequency band, avoiding any additional question about summing bands into an unlocalized $`L^\infty`$ estimate. It uses the Friedlander Dirichlet form on $`dx\,dy`$, rather than the distinct Laplace–Beltrami realization on Riemannian volume.

## Status review


**Known cases:** The exact full-flow frequency-localized L5-time Linfinity-space Friedlander endpoint is required. The existing 36/7 positive range and q>=5 counterexample threshold leave the endpoint; Euclidean half-wave estimates use a different propagator.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact full-flow frequency-localized L5-time Linfinity-space Friedlander endpoint is required. The existing 36/7 positive range and q>=5 counterexample threshold leave the endpoint; Euclidean half-wave estimates use a different propagator.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded literature and announcement checks on 24 October 2026 located no resolution of this exact endpoint. The checked later Neumann wave and Schrödinger results have different hypotheses or evolutions. This is a source and theorem-scope review, not a proof of openness.


All-status AIM, OpenAI announcement and current FURTHER comparisons found no equivalent target. The expanded [Euclidean local-smoothing announcement](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/CONTENTS.md), compared on 26 October 2026, includes spatial dimension two. This target concerns the Friedlander Dirichlet operator and the exact frequency-localized $`L^5_tL^\infty_x`$ endpoint with $`L^2`$ input; the announcement states Euclidean estimates above the sharp Sobolev threshold and does not assert this boundary endpoint. Catalogue checks include partial and announced results as well as admitted problems.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ef73fcad5468ae5d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
