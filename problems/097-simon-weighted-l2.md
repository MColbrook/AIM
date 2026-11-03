# 097. Simon’s multidimensional weighted square-integrability conjecture

**Area:** Quantum scattering and transport

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

For every $`d\ge2`$, let $`V:\mathbb R^d\to\mathbb R`$ be bounded and measurable with

```math
\int_{\mathbb R^d}\frac{|V(x)|^2}{(1+|x|)^{d-1}}\,dx<\infty.
```

For $`H=-\Delta+V`$ on $`H^2(\mathbb R^d)\subset L^2(\mathbb R^d)`$, prove or disprove that the absolutely continuous spectral part has infinite multiplicity at Lebesgue-almost every energy $`E>0`$. Thus the target concerns the multiplicity of propagating states, and does not exclude additional singular spectrum.

## Application

It asks how little spatial decay of an electric potential suffices to preserve the infinitely many scattering channels of a free particle.

## References

1. B. Simon, [Tosio Kato’s work on non-relativistic quantum mechanics: part 2](https://doi.org/10.1007/s13373-018-0121-5), Bulletin of Mathematical Sciences (2018), Conjecture 20.2: weighted condition and infinite multiplicity.
2. S. Denisov and A. Kiselev, [Spectral Properties of Schrödinger Operators with Decaying Potentials](https://services.math.duke.edu/~kiselev/dec.pdf), survey (2007), §5, equation (5.1): multidimensional open problem and partial results.

3. S. Becker and M. Yang, [*Lenses make many points: Pure point spectrum disproves Simon’s L² conjecture*](https://arxiv.org/abs/2610.31637), arXiv:2610.31637v1 (22 October 2026), Theorem 1.1. [Primary manuscript](https://arxiv.org/pdf/2610.31637v1).

## Status review

**Resolution update (3 November 2026):** Counterexample. Becker and Yang’s Theorem 1.1 constructs smooth bounded nonnegative potentials with the required weighted square integrability, but with no continuous spectral subspace at all. Its weight $`|x|^{1-d}`$ is stronger than the displayed $`(1+|x|)^{1-d}`$ condition. The counterexample therefore answers this problem negatively.

[Proof](https://arxiv.org/pdf/2610.31637v1) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-a/097.json). The theorem hypotheses and current announcement were checked.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

The one-dimensional square-integrability theory does not settle the multidimensional assertion. The cited survey discusses additional structure or decay assumptions under which positive results hold. Recent searches returned further special-model results, but no proof for all bounded potentials satisfying precisely this weighted condition.

**Search audit:** “Simon multidimensional L2 conjecture absolutely continuous spectrum”; “weighted L2 decaying potential Simon conjecture 2025 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
