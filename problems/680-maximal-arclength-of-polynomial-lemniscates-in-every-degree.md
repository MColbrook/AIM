# 680. Maximal arclength of polynomial lemniscates in every degree

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge1`$ be an integer and let
```math
p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0,\qquad a_j\in\mathbb C,
```

be any monic polynomial. Define its unit lemniscate and its Euclidean arclength by
```math
L(p)=\{z\in\mathbb C:|p(z)|=1\},\qquad \ell(L(p))=\mathcal H^1(L(p)).
```

Is it always true that
```math
\ell(L(p))\le \ell(L(z^n-1))?
```

Here $`\mathcal H^1`$ is one-dimensional Hausdorff measure: all components of the geometric level set are counted, without parametrization multiplicity. No connectedness, root-location bound, additional coefficient normalization or regular-value assumption is imposed. The question asks for the inequality in every positive degree; it does not add a classification of equality cases.

## Application

This asks for the sharp geometric bound on the boundary length of polynomial sublevel sets. These sets are basic objects in complex analysis, approximation theory and logarithmic potential theory.

## References

1. A. Fryntov and F. Nazarov, [*New estimates for the length of the Erdős–Herzog–Piranian lemniscate*](https://arxiv.org/abs/0808.0717v1), arXiv:0808.0717v1 (2008), equation (1), physical p. 1, and the introduction on pp. 1–2. This eligible original states the exact conjecture and proves local and asymptotic partial results.
2. A. Eremenko and W. Hayman, [*On the length of lemniscates*, author manuscript](https://www.math.purdue.edu/~eremenko/dvi/erdos23.pdf), introduction and Lemmas 4–6. The degree-two case is settled; restrictions on extremizers are reductions, not assumptions on all competitors.
3. T. Tao, [*The maximal length of the Erdős–Herzog–Piranian lemniscate in high degree*](https://arxiv.org/abs/2512.12455v2), arXiv:2512.12455v2 (2025), Conjecture 1.1, Theorem 1.1(iv) and Remark 1.3, physical pp. 1–5.

## Status review


**Known cases:** Tao proves the maximizer only in sufficiently high degree. The author blog, current problem discussion and computational repository still leave degrees outside the established cases; an initial small-degree certification claim does not cover every remaining degree. Minimal area and shortest-path lemniscate papers answer different questions. No complete all-degree announcement located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Tao proves the maximizer only in sufficiently high degree. The author blog, current problem discussion and computational repository still leave degrees outside the established cases; an initial small-degree certification claim does not cover every remaining degree. Minimal area and shortest-path lemniscate papers answer different questions. No complete all-degree announcement located.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2512.12455); [comparison source 2](https://terrytao.wordpress.com/2025/12/15/the-maximal-length-of-the-erdos-herzog-piranian-lemniscate-in-high-degree/); [comparison source 3](https://www.erdosproblems.com/forum/thread/114); [comparison source 4](https://github.com/MendozaLab/erdos-experiments). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Degree one is immediate, and degree two has a primary proof in [2]. Tao's latest version proves the sharp inequality for all sufficiently large degrees. Its constants are effective but the threshold is not optimized or supplied as a numerical bound. This leaves a bounded-degree verification task for the full universal assertion.

Located 2026 announcements concern individual small degrees or numerical searches. A current computational repository explicitly corrects its earlier certification claim to incomplete numerical evidence. These sources do not announce a complete all-degree resolution; no claim is made here that every particular small degree remains open, or that their proofs have been independently certified.

The actual original and current theorem statements were read. Bounded current searches and all-status AIM/FURTHER/OpenAI statement comparisons found no matching complete resolution or equivalent listed target. The existing curve-diffusion lifespan question involving Bernoulli's lemniscate concerns a different geometric evolution, and the plurisubharmonic sublevel-volume question concerns a different measure and class of functions. This review does not certify every cited proof or establish exhaustive absence of a later result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-19b859adfab2934a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
