# 1056. Can higher Sobolev norms blow up for non-rational half-wave maps on the circle?

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider the half-wave maps equation on the one-dimensional torus $`\mathbb T=\mathbb R/2\pi\mathbb Z`$,
```math
\partial_t u=u\times |D|u,\qquad u:\mathbb R\times\mathbb T\longrightarrow\mathbb S^2.
```

For $`s>1/2`$ and non-rational initial data $`u_0\in H^s(\mathbb T;\mathbb S^2)`$, let $`u(t)`$ be the globally defined critical-space solution. Can $`\|u(t)\|_{H^s}`$ become infinite at a finite time, or grow without bound as $`|t|\to\infty`$? More broadly, does the flow preserve $`H^s`$ globally for non-rational data? The finite-time question includes the classical local $`H^s`$ range $`s>3/2`$; global well-posedness at $`1/2<s\leq3/2`$ also entails a lower-regularity local question.

The question concerns the circle $`\mathbb T`$, not the real-line companion equation. Here rational means rational in $`z=e^{ix}`$. At critical regularity $`H^{1/2}`$, a global continuous flow and almost periodicity are already known. Uniform bounds on all higher Sobolev norms have been established for rational initial data.

## Application

The critical-space flow is controlled, but its higher regularity may behave differently. The question tests whether the integrable structure prevents creation of arbitrarily fine spatial scales beyond the rational solution class.

## References

1. Enno Lenzmann (joint work with Patrick Gérard), *The half-wave maps equation is globally well-posed in* $`H^{1/2}`$ *on* $`\mathbb T`$, in [*Oberwolfach Report 10/2026: Nonlinear Waves and Dispersive Equations*](https://doi.org/10.4171/OWR/2026/10), printed pp. 668–671, open question on p. 670.
2. Patrick Gérard and Enno Lenzmann, [*The half-wave maps equation on* $`\mathbb T`$*: Global well-posedness in* $`H^{1/2}`$ *and almost periodicity*](https://arxiv.org/html/2602.20895v3), arXiv:2602.20895v3 (July 2026), Theorem 2.4 and following Remark. The report's arXiv identifier has a transposed digit; this is the matching paper by title and authors.

## Status review


**Known cases:** The circle flow with nonrational data needs higher Sobolev control. The July 2026 critical-space almost-periodicity and rational-data higher bounds do not imply regularity or uniform bounds for all higher-Sobolev data.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The circle flow with nonrational data needs higher Sobolev control. The July 2026 critical-space almost-periodicity and rational-data higher bounds do not imply regularity or uniform bounds for all higher-Sobolev data.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Theorem 2.4 bounds higher $`H^s`$ norms uniformly in time for rational data. The subsequent Remark explicitly leaves non-rational data and global $`H^s`$ well-posedness open. The authors' global $`H^{1/2}`$ flow and almost periodicity in that space do not settle higher $`H^s`$ behavior. Bounded current searches and an independent source-and-scope audit on 21 October 2026 found no matching complete announcement. This is a live-status assessment, not a proof of unsolvedness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-afb75af63a0ec558**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
