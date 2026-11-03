# 999. Uniqueness for stationary fractional stochastic Burgers below the critical threshold

**Area:** Rough paths and singular stochastic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$, let $`A=-\partial_x^2`$ act on mean-zero functions, and fix $`1/2<\theta<3/4`$. Consider the formally written equation

```math
du_t=-A^\theta u_t\,dt+\partial_x(u_t^2)\,dt
       +\sqrt2 A^{\theta/2}\,dW_t,
```

where $`W`$ is cylindrical Brownian motion on $`L^2_0(\mathbb T)`$. The stationary marginal distribution is mean-zero spatial white noise with covariance the identity on $`L^2_0`$.

For every $`T>0`$, is the law on $`C([0,T],\mathcal S'(\mathbb T))`$ unique among the following stationary controlled solutions? The process $`u`$ has the white-noise marginal at every time. If $`\Pi_N`$ retains Fourier modes $`0<|k|\le N`$, the integrated nonlinearity is

```math
B_t(f)=\lim_{N\to\infty}\int_0^t
\langle\partial_x((\Pi_Nu_s)^2),f\rangle\,ds
```

in probability in $`C([0,T])`$, for each smooth mean-zero test function $`f`$. It has a continuous distribution-valued version, starts at zero, and has zero quadratic variation after testing. The process

```math
M_t(f)=u_t(f)-u_0(f)+\int_0^t u_s(A^\theta f)\,ds-B_t(f)
```

is a continuous martingale in the natural forward filtration, with quadratic variation $`2t\|A^{\theta/2}f\|_2^2`$. The same martingale condition holds in the natural backward filtration for
$`\widehat u_t=u_{T-t}`$ and
$`\widehat B_t=-(B_T-B_{T-t})`$.

This asks for uniqueness in law; existence in this range is known. The time-reversal condition is part of the question. No Markov assumption or selection by a particular approximation is imposed.

## Application

The equation describes stationary fluctuations of a noisy conservation law. Uniqueness would establish whether those fluctuations determine an intrinsic continuum model when dissipation is weaker than the threshold covered by current uniqueness theory.

## References

1. M. Gubinelli and M. Jara, *Regularization by noise and stochastic Burgers equations*, [arXiv:1208.6551v2](https://arxiv.org/abs/1208.6551), 9 April 2013. See the introduction, pp. 2–3; Definitions 1–2, pp. 4–5; Theorem 1, pp. 14–15; and Definition 3 and Theorem 2, p. 15. The paper establishes existence for $`\theta>1/2`$.
2. M. Gubinelli and N. Perkowski, *The infinitesimal generator of the stochastic Burgers equation*, Probability Theory and Related Fields **178** (2020), 1067–1124, [DOI:10.1007/s00440-020-00996-5](https://doi.org/10.1007/s00440-020-00996-5). This develops uniqueness above $`\theta=3/4`$.
3. L. Gräfner, *Energy solutions of singular stochastic partial differential equations*, [2025 dissertation repository record](https://refubium.fu-berlin.de/handle/fub188/49538). The critical and subcritical uniqueness results leave the range specified here.
4. N. Perkowski, *Energy Solutions of Singular SPDEs*, Proceedings of the International Congress of Mathematicians 2026, Vol. 6, pp. 81–101, [DOI:10.1137/25M1807393](https://doi.org/10.1137/25M1807393). Example 2.9(i) and Section 6 describe the known $`\theta\ge3/4`$ uniqueness range and the remaining supercritical question.

## Status review


**Known cases:** The precise stationary controlled solution class includes time reversal. The known critical/subcritical theta>=3/4 uniqueness and Caputo-time or other noise Burgers equations do not cover theta between one half and three quarters.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The precise stationary controlled solution class includes time reversal. The known critical/subcritical theta>=3/4 uniqueness and Caputo-time or other noise Burgers equations do not cover theta between one half and three quarters.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed through 16 October 2026. The source question is eligible under W001 because its first arXiv submission was in August 2012. Current primary sources explicitly leave $`1/2<\theta<3/4`$ open. The classical $`\theta=1`$ equation, critical endpoint, deterministic Burgers equations, and equations with a different diffusion/noise balance do not resolve this target.

The existing AIM comparisons include AIM 067 (deterministic shock control), AIM 351 (deterministic entire profiles), and AIM 170 (first-passage percolation); none asks this question. The separate held GJ14 lead concerns the classical equation in a weaker class without time reversal and is distinct. The 372-family OpenAI announcement snapshot contains no matching Burgers or energy-solution target. The coordinator completed the target-specific 186-page Prove2Me comparison: no matching target was found; Gubinelli matches concern unrelated regularity-structure background. A September 2026 Kuo–Matetski paper uses a Caputo time derivative and temporally integrated noise in a different function class, rather than the stationary ordinary-time model here.

The normalization above uses noise $`\sqrt2 A^{\theta/2}`$ consistently with unit white-noise covariance. The original manuscript's backward drift is written here with its zero-at-time-zero increment. Detailed review evidence: [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/fractional-burgers-supercritical-uniqueness.json). Searches are bounded checks, not proof that no later announcement exists.

A September 2026 existence-and-uniqueness paper on a space-time fractional Burgers-type equation assumes a Caputo time derivative of order strictly below one. It does not resolve the ordinary-time, white-noise-invariant model stated here.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-77e5a6e8462e8e86**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
