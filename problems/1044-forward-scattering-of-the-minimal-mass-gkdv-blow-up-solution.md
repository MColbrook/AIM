# 1044. Forward scattering of the minimal mass gKdV blow-up solution

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider the real focusing, mass-critical generalized Korteweg–de Vries equation on $`\mathbb R`$,
```math
u_t+(u_{xx}+u^5)_x=0,
\qquad Q(x)=\left(\frac{3}{\cosh^2(2x)}\right)^{1/4}.
```

Let $`S`$ be the distinguished solution constructed in Theorem 1.3(i) of [1]. It satisfies
```math
S\in C((0,\infty);H^1(\mathbb R)),\qquad
\|S(t)\|_2=\|Q\|_2,
```
and blows up in $`H^1`$ as $`t\downarrow0`$. Does there exist $`v_+\in L^2(\mathbb R)`$ such that
```math
\lim_{t\to+\infty}
\left\|S(t)-e^{-t\partial_x^3}v_+\right\|_{L^2(\mathbb R)}=0?
```

The linear group solves $`v_t+v_{xxx}=0`$. This asks about the positive-time branch of this particular threshold solution, with no time-dependent translation or rescaling in the limit. The solitary wave $`Q(x-t)`$ has the same mass but does not have the required backward blow-up.

## Application

This would describe a transition from concentration at the threshold mass to dispersive radiation. Corollary 1.5 of [1] also shows that scattering of $`S`$ would establish forward scattering for the paper's near-soliton **Exit** regime.

## References

1. Yvan Martel, Frank Merle and Pierre Raphaël, [*Blow up for the critical gKdV equation. II: Minimal mass dynamics*](https://doi.org/10.4171/JEMS/547), *Journal of the European Mathematical Society* **17** (2015), no. 8, 1855–1925. Theorem 1.3 is on printed p. 1858; the explicit scattering conjecture and its precise $`L^2`$ meaning are on p. 1859, immediately before Corollary 1.5 and in footnote 2. [Published text](https://ems.press/content/serial-article-files/32056?nt=1).
2. Matthew Kowalski and Minjie Shan, [*On dispersive decay for the generalized Korteweg–de Vries equation*](https://arxiv.org/abs/2510.01728), v1 (2025), introduction and §4. Its focusing small-data input and defocusing all-data bound do not supply the missing estimate for $`S`$.
3. Satoshi Masaki and Jun-ichi Segata, [*Scattering problem for the generalized Korteweg-de Vries equation*](https://arxiv.org/abs/2408.00261), v1 (2024), Theorems 1.6–1.7. These scattering statements assume $`8/5<\alpha<2`$ for the nonlinearity $`|u|^{2\alpha}u`$, excluding the quintic endpoint $`\alpha=2`$.

## Status review


**Known cases:** The target is positive-time L2 scattering of the specific backward-blowing-up minimal mass element. Same-mass solitons, small-data scattering, subcritical nonlinear powers and constructions of other blowup rates do not answer it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is positive-time L2 scattering of the specific backward-blowing-up minimal mass element. Same-mass solitons, small-data scattering, subcritical nonlinear powers and constructions of other blowup rates do not answer it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The existence, positive-time lifespan and uniqueness up to flow symmetries of the minimal-mass finite-time blow-up element are established in [1]. Positive-time $`H^1`$ membership alone does not give a finite forward scattering norm. Corollary 1.5 assumes the requested scattering.

Targeted literature and announcement searches through 24 October 2026 found no complete resolution for this specific solution. Later results checked concern small data, a different sign or exponent, conditional scattering, or backward blow-up asymptotics. The final 2026 journal version of [3] was inaccessible in this check, so its theorem statements were not verified against v1. Comparisons with the AIM list and the developing collection found no matching target.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-19e1bbc2cd6265de**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
