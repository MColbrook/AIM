# 973. Near-quadratic logarithmic slowdown bounds for planar random media

**Area:** Probability and transport in random environments
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

At each $`x\in\mathbb Z^2`$, sample an independent, identically distributed probability vector $`\omega_x=(\omega_x(e))_{e\in\{\pm e_1,\pm e_2\}}`$. Assume uniform ellipticity: $`\omega_x(e)\geq\kappa>0`$ almost surely for every $`e`$. Given the sampled environment, start $`X_0=0`$ and use transition probabilities
```math
P_\omega(X_{n+1}=x+e\mid X_n=x)=\omega_x(e).
```

Let $`\mathbb P^0`$ denote the annealed law, averaging over the environment and the walk.

Assume condition $`(T)`$ in a direction $`\ell_0\in S^1`$: for every unit vector $`\ell`$ in some neighborhood of $`\ell_0`$, there are $`c_\ell,C_\ell,L_\ell>0`$ such that
```math
\mathbb P^0(H_{-L}^{\ell}<H_L^{\ell})
 \leq C_\ell e^{-c_\ell L}\quad(L\geq L_\ell),
```

where $`H_L^\ell=\inf\{n\geq0:X_n\cdot\ell\geq L\}`$ and
$`H_{-L}^\ell=\inf\{n\geq0:X_n\cdot\ell\leq-L\}`$.
Under this assumption the limiting velocity $`v=\lim_{n\to\infty}X_n/n`$ is deterministic and nonzero.

For every $`a\in[0,v]\setminus\{v\}`$, every $`0<\varepsilon<\|v-a\|_\infty`$, and every $`0<\alpha<2`$, do constants $`C,c>0`$ exist such that
```math
\mathbb P^0\!\left(\left\|X_n/n-a\right\|_\infty<\varepsilon\right)
 \leq C\exp\!\left[-c(\log n)^\alpha\right]
 \quad\text{for every integer }n\geq3?
```

Constants may depend on the environment law, direction, $`a,\varepsilon,\alpha`$, but not on $`n`$.

This is the planar $`(T)`$ subcase of the extension conjectured in [1, Section 1.8]. It concerns the original annealed slowdown event.

## Application

The estimate would quantify unusually slow transport through an independently disordered planar medium, despite its positive macroscopic velocity.

## Known progress

Berger [1, Theorem 1.5] proves the corresponding family with $`\alpha<d`$ for $`d\geq4`$, and explicitly conjectures the extension to dimensions two and three. The hypothesis there is $`(T_\gamma)`$; the exponential slab bound above implies it for every fixed $`\gamma<1`$ when $`L`$ is large.

Peretz [2, Theorem 1.8] obtains a related regeneration-time tail estimate in dimension three; Remark 1.9 leaves the planar regeneration case open. His regeneration convention differs from Berger's. No equivalence of those definitions or their first-time tail events is needed or asserted here. The invariant-measure theorem [2, Theorem 1.5] concerns a different conclusion.

## References

1. N. Berger, *Slowdown estimates for ballistic random walk in random environment*, J. Eur. Math. Soc. **14** (2012), 127–174, [doi:10.4171/JEMS/298](https://doi.org/10.4171/JEMS/298). Model and Definitions 4–7 on pp. 127–129; Theorem 1.5 and Section 1.8 on p. 131.
2. T. Peretz, *Environment viewed from the particle and slowdown for ballistic RWRE in low dimensions*, [arXiv:2204.12238v2](https://arxiv.org/html/2204.12238v2), 3 August 2025. Definitions 1.1 and 1.3, Theorems 1.2, 1.5 and 1.8, Remark 1.9. This checked version supplies the current comparison.

## Status review


**Known cases:** The planar (T) slowdown event is the original annealed position event with every logarithmic exponent below two. Current low-dimensional invariant-environment and regeneration bounds do not establish the displayed full slowdown estimate.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The planar (T) slowdown event is the original annealed position event with every logarithmic exponent below two. Current low-dimensional invariant-environment and regeneration bounds do not establish the displayed full slowdown estimate.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original published statement, its low-dimensional conjecture and the later primary theorem statements were checked directly on 24 October 2026. Bounded searches found no matching complete solution or announcement. AIM/OpenAI and FURTHER comparisons found distinct qualitative transience/ballisticity questions. The complete linked OpenAI proof and final EJP publisher body were not accessible in this check; no full-proof or final-version parity claim is made. The Prove2Me homepage timed out; inspected indexed missions concerned different one-dimensional models. These limitations remain recorded in the review log.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2a0cbff65951d823**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
