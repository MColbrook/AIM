# 888. A uniform Monte Carlo rate for the extended ensemble Kalman–Bucy filter

**Area:** Nonlinear filtering and data assimilation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d,q\geq1`$, let $`R_1\in\mathbb R^{d\times d}`$ and $`R_2\in\mathbb R^{q\times q}`$ be symmetric positive definite, and let $`B\in\mathbb R^{q\times d}`$ satisfy $`B^TR_2^{-1}B=\rho I_d`$ with $`\rho>0`$. Let $`A:\mathbb R^d\to\mathbb R^d`$ be $`C^2`$, with bounded Jacobian, and suppose

```math
\lambda:=-\sup_x\lambda_{\max}(DA(x)+DA(x)^T)>0,
\qquad \|DA(x)-DA(y)\|_{\mathrm{op}}\leq\kappa|x-y|
```

for a fixed $`\kappa>0`$. Define

```math
\lambda_S=\lambda/\rho,\qquad
\lambda_R=\lambda/\mathrm{tr}(R_1),\qquad
\lambda_K=\lambda/\kappa,\qquad
\lambda_{R,S}=\frac{\lambda_R\sqrt{\lambda_S}}{8e}
\left(1+\frac{2}{\lambda_R\lambda_S}\right)^{-1},
\qquad
\delta=\min\{e\lambda_{R,S},\tfrac12\sqrt{\lambda_S}\}.
```

Assume

```math
\min\{\lambda_K\lambda_R/4,\lambda_{R,S},\lambda_S/4\}>1,
\qquad \delta\geq4.
```

Take $`X_0\sim\mathcal N(m_0,P_0)`$, with $`P_0`$ positive definite and

```math
\mathrm{tr}(P_0)^2\leq
\frac{\lambda_S}{\lambda_R}
\left(\frac12+\frac{1}{\lambda_R\lambda_S}\right).
```

The signal and its observation are

```math
dX_t=A(X_t)\,dt+R_1^{1/2}\,dW_t,\qquad
dY_t=BX_t\,dt+R_2^{1/2}\,dV_t,\qquad Y_0=0.
```

Here $`W,V`$ are independent standard Brownian motions of dimensions $`d,q`$, independent of $`X_0`$. Define the extended Kalman–Bucy mean and covariance by

```math
d\widehat m_t=A(\widehat m_t)\,dt+
P_tB^TR_2^{-1}(dY_t-B\widehat m_t\,dt),
\qquad
\dot P_t=DA(\widehat m_t)P_t+P_tDA(\widehat m_t)^T+R_1-P_tB^TR_2^{-1}BP_t,
\qquad (\widehat m_0,P_0)=(m_0,P_0).
```

For $`N\geq2`$, let $`\xi_0^1,\ldots,\xi_0^N`$ be independent samples from $`\mathcal N(m_0,P_0)`$, independent of the signal and all driving noises, and set

```math
m_t^N=\frac1N\sum_{i=1}^N\xi_t^i,
\qquad p_t^N=\frac1{N-1}\sum_{i=1}^N
(\xi_t^i-m_t^N)(\xi_t^i-m_t^N)^T.
```

Use the particle dynamics

```math
d\xi_t^i=
\big[A(m_t^N)+DA(m_t^N)(\xi_t^i-m_t^N)\big]dt
+R_1^{1/2}dW_t^i
+p_t^NB^TR_2^{-1}\big[dY_t-B\xi_t^i\,dt+R_2^{1/2}dV_t^i\big],
```

where all $`W^i,V^i`$ are mutually independent standard Brownian motions, independent of the signal noises and initial values. The limiting comparison particle $`\zeta^1`$ starts at $`\xi_0^1`$ and solves

```math
d\zeta_t^1=
\big[A(\widehat m_t)+DA(\widehat m_t)(\zeta_t^1-\widehat m_t)\big]dt
+R_1^{1/2}dW_t^1
+P_tB^TR_2^{-1}\big[dY_t-B\zeta_t^1\,dt+R_2^{1/2}dV_t^1\big].
```

For probability laws on a Euclidean space, write $`W_r`$ for the $`r`$-Wasserstein distance. On mean–matrix pairs use the norm $`\|(m,P)\|^2=|m|^2+\|P\|_F^2`$. Are there finite constants $`C,N_0`$, depending on the fixed model and initial law but independent of $`N`$ and $`t`$, such that every integer $`N\geq N_0`$ satisfies

```math
\sup_{t\geq0}
\max\left\{
W_\delta\big(\mathrm{Law}(m_t^N,p_t^N),
                  \mathrm{Law}(\widehat m_t,P_t)\big),
W_2\big(\mathrm{Law}(\xi_t^1),\mathrm{Law}(\zeta_t^1)\big)
\right\}\leq C N^{-1/2}?
```

All laws here are unconditional, averaging over observations as well as the ensemble. A negative answer must give admissible fixed model data for which no such constants exist.

This is a restricted form of the explicit optimal-rate conjecture following Theorem 2.3 of Del Moral–Kurtzmann–Tugaut. Gaussian initialization and a bounded Jacobian are imposed explicitly in this formulation. The particle drift is the linearization at the empirical mean displayed above; replacing it by $`A(\xi_t^i)`$ changes the question. The target is approximation of the extended filter and its comparison diffusion, rather than exact nonlinear Bayesian filtering.

## Application

An ensemble approximates the covariance used to weight incoming noisy measurements. A uniform $`N^{-1/2}`$ bound would quantify how ensemble size controls sampling error during arbitrarily long filtering runs for a stable nonlinear signal.

## References

1. P. Del Moral, A. Kurtzmann and J. Tugaut, [*On the stability and the uniform propagation of chaos of a class of extended ensemble Kalman–Bucy filters*](https://doi.org/10.1137/16M1087497), SIAM Journal on Control and Optimization **55** (2017), 119–155. [Author preprint v2](https://arxiv.org/pdf/1606.08256v2), models (1)–(5), assumptions (7), (15), (20), Theorem 2.3 and the explicit conjecture immediately afterwards, physical PDF pp. 4–6, 10–15. The read copy has 39 pages and body date 7 August 2018 despite its October 2016 arXiv version header; journal pagination is different.
2. P. Del Moral, A. Kurtzmann and J. Tugaut, [*On the stability and the concentration of extended Kalman–Bucy filters*](https://arxiv.org/pdf/1606.08251v2), model (1), physical PDF p. 4, and Theorems 1.1–1.2, pp. 9–11. The companion model explicitly assumes Gaussian initialization. These theorems concern the limiting filter, without a particle number.
3. S. W. Ertel, [*On the mean field theory of ensemble Kalman filters for SPDEs*](https://doi.org/10.1137/24M1658954), SIAM/ASA Journal on Uncertainty Quantification **13** (2025); [preprint v4](https://arxiv.org/pdf/2306.16863v4), Theorem 24 and Remarks 25–26, physical pp. 22–25.
4. E. Calvello, P. Monmarché, A. M. Stuart and U. Vaes, [*Accuracy of the ensemble Kalman filter in the near-linear setting*](https://doi.org/10.1137/25M1732544), SIAM Journal on Numerical Analysis **64** (2026), 391–429, §§1.1–1.2 and 2.1, model (2.1).

## Status review


**Known cases:** The source endpoint remains conjectural beyond its unspecified uniform N-to-negative-beta estimate. Conventional nonlinear or transport ensemble filters have different drift/noise or discrete dynamics; finite-horizon results do not give uniform time control of both unconditional Wasserstein errors for this extended linearization-at-the-mean system.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source endpoint remains conjectural beyond its unspecified uniform N-to-negative-beta estimate. Conventional nonlinear or transport ensemble filters have different drift/noise or discrete dynamics; finite-horizon results do not give uniform time control of both unconditional Wasserstein errors for this extended linearization-at-the-mean system.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves a uniform rate $`N^{-\beta}`$ for some $`0<\beta\leq1/2`$ and explicitly conjectures the endpoint $`\beta=1/2`$. Its theorem does not establish that endpoint. The formulation above retains its quantitative stability and initial-covariance restrictions and adds the stated regularity and initialization restrictions.

Ertel treats the conventional nonlinear deterministic ensemble filter, with bounded observation functions in the quantitative theorem, finite time intervals and fractional moments below the mean-square endpoint. Calvello and collaborators treat discrete time; their finite-horizon accuracy theorem does not provide the present uniform continuous-time estimate. Existing linear-Gaussian results do not cover a nonlinear Jacobian evaluated at the evolving ensemble mean.

The 17 October 2026 searches and current catalogue comparison found no resolution of this precise question. The closest retained FURTHER problem concerns contraction of a linear-model matrix Riccati diffusion under common noise, with a fixed ensemble size, and asks no optimal sampling rate. Independent selected-primary review checked the exact constants, squared trace restriction, comparison-particle drift, both unconditional Wasserstein targets and the quantitative hypotheses. It also checked that Gaussian initialization and bounded signal Jacobian do not make the covariance-dependent particle coefficients globally Lipschitz or turn the nonlinear model into the known linear case.

Further selected 2026 comparisons include [a nonlinear-law constant-noise framework](https://arxiv.org/abs/2603.10988) and [a discrete transport-filter Monte Carlo theorem](https://arxiv.org/abs/2606.25346). Their inspected assumptions or finite-horizon restrictions do not supply this continuous-time endpoint.

All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. The fresh Prove2Me snapshot reconciles 4,629 distinct listings on 186 pages. All 70 target contexts were read, merging overlap without losing matched text; the returned optimization, gas, graphon and game estimates concern different models. This comparison covers public listing descriptions, not every mission proof.

The [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/extended-ensemble-optimal-rate-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-extended-ensemble-optimal-rate-review.json) and [fresh catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/EnEKF-prove2-batch0082-review.json) preserve exact extents. The original 39-page author text and companion 33-page text were read in full by the source reviewer; parity with the final 2017 journal edition remains unchecked. Some later comparisons are selected readings only. These dated checks found no matching complete resolution or announcement and do not certify every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a81af787ee12a3e9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
