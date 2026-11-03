# 886. Uniform finite-ensemble accuracy under detectability

**Area:** Nonlinear filtering and data assimilation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix integers $`d,q\geq1`$, a real matrix $`A\in\mathbb R^{d\times d}`$, an observation matrix $`H\in\mathbb R^{q\times d}`$, and symmetric positive-definite matrices $`R,P_0\in\mathbb R^{d\times d}`$. Suppose $`(A,H)`$ is detectable: there exists $`L\in\mathbb R^{d\times q}`$ such that every eigenvalue of $`A-LH`$ has negative real part. Let $`m_0\in\mathbb R^d`$.

The signal and observation satisfy the Itô equations

```math
dX_t=AX_t\,dt+R^{1/2}dB_t,\qquad dZ_t=HX_t\,dt+dW_t,\qquad X_0\sim\mathcal N(m_0,P_0),\quad Z_0=0.
```

Here $`B,W`$ are independent standard Brownian motions of dimensions $`d,q`$, independent of $`X_0`$. The exact conditional mean and covariance are the Kalman–Bucy solution

```math
dm_t=Am_t\,dt+P_tH^\top(dZ_t-Hm_t\,dt),\qquad
\dot P_t=AP_t+P_tA^\top+R-P_tH^\top HP_t,\qquad(m_0,P_0)\text{ as above}.
```

For an integer $`N\geq2`$, initialize $`\xi_0^1,\ldots,\xi_0^N`$ independently from $`\mathcal N(m_0,P_0)`$, independently of the signal and all Brownian motions, and define

```math
m_t^N=\frac1N\sum_{i=1}^N\xi_t^i,\qquad P_t^N=\frac1{N-1}\sum_{i=1}^N(\xi_t^i-m_t^N)(\xi_t^i-m_t^N)^\top.
```

Use the unmodified square-root ensemble Kalman–Bucy particle dynamics

```math
d\xi_t^i=A\xi_t^i\,dt+R^{1/2}dB_t^i+
P_t^NH^\top\left[dZ_t-\frac12H(\xi_t^i+m_t^N)\,dt\right],\qquad1\leq i\leq N,
```

where the $`B^i`$ are mutually independent standard $`d`$-dimensional Brownian motions, independent of the other noises and initial values.

Do constants $`C<\infty`$ and an integer $`N_0\geq d+2`$, depending on the fixed model and initial law but independent of $`t,N`$, always exist such that

```math
\sup_{t\geq0}\left(\mathbb E|m_t^N-m_t|+
\mathbb E\|P_t^N-P_t\|_{\mathrm{op}}\right)\leq\frac C{\sqrt N}
\qquad\text{for every integer }N\geq N_0?
```

The expectations average over both observations and the ensemble. A negative answer must give fixed admissible model data for which this bound fails for arbitrarily large $`N`$. No stability of $`A`$ itself or positive definiteness of $`H^\top H`$ is assumed. The particle system has stochastic process noise; replacing it by deterministic optimal-transport dynamics changes the question.

This is a precise nondegenerate-process-noise instance of Taghvaei–Mehta's expected detectability extension, Remark3.7 and equation(16). It retains the source's expectation-of-norm error, rather than adding a squared-error requirement.

## Application

An ensemble filter weights noisy observations using a sample covariance. A uniform error estimate would justify its accuracy over arbitrarily long observation records when some state directions are unobserved but dynamically stable. The constants may depend on the dimension; this is not a dimension-free claim.

## References

1. A. Taghvaei and P.G. Mehta, [A survey of feedback particle filter and related controlled interacting particle systems (CIPS)](https://doi.org/10.1016/j.arcontrol.2023.03.006), *Annual Reviews in Control*55(2023),356–378. [Final published author-deposited PDF](https://par.nsf.gov/servlets/purl/10464982), §3.3, equations(14)–(16), Remark3.7, printed361/physical6.
2. A.N. Bishop and P. Del Moral, [On the mathematical theory of ensemble (linear-Gaussian) Kalman–Bucy filtering](https://doi.org/10.1007/s00498-023-00357-2), *Mathematics of Control, Signals, and Systems*35(2023),835–903. [Author-hosted published PDF](https://people.bordeaux.inria.fr/pierre.delmoral/math-EnKF-2023.pdf), §§5.2–5.3 and8.1/8.4, especially physical34–35,56–58,63. The source distinguishes covariance fluctuation, mean error, and trajectory contraction.
3. X. Chen and S.S.-T. Yau, [On the stability of linear feedback particle filter](https://jag.math.tsinghua.edu.cn/Publications/Control/428.pdf), *Asian Journal of Mathematics*27(2023),95–120, Assumptions1–3 and Theorem4.9.
4. X. Chen, J. Kang and S.S.-T. Yau, [Time-varying feedback particle filter](https://doi.org/10.1016/j.automatica.2024.111740), *Automatica*167(2024),111740; [author-hosted final PDF](https://jag.math.tsinghua.edu.cn/Publications/Control/448.pdf), Assumptions1–4 and Theorems3–5.
5. P. Del Moral, B. Nasri and B. Rémillard, [Fluctuations and long-time stability of multivariate ensemble Kalman filters](https://arxiv.org/html/2601.17392v2), arXiv:2601.17392v2,27January2026, equations(5)–(17), Theorem2.1.
6. F. Hoffmann, S. Park and A.M. Stuart, [Large-time behavior and accuracy of the Mean-Field Ensemble Kalman Filter in the Linear Detectable Setting](https://arxiv.org/html/2606.07729v1), arXiv:2606.07729v1,5June2026, equation(1.19), Theorem3.13 and Corollary3.16.
7. X. Cheng, D. Sanz-Alonso and N. Waniorek, [Time-uniform accuracy of ensemble Kalman filters with localization](https://arxiv.org/html/2609.23927v1), arXiv:2609.23927v1,20September2026, §§2.1–2.3.

## Status review


**Known cases:** The 2026 detectable mean-field theorem has no finite ensemble sampling error. Discrete-generation or localized-filter theorems change the dynamics or time horizon. Existing mean-error estimates need stronger stability/full-observation restrictions than detectability of the original continuous square-root particle model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 detectable mean-field theorem has no finite ensemble sampling error. Discrete-generation or localized-filter theorems change the dynamics or time horizon. Existing mean-error estimates need stronger stability/full-observation restrictions than detectability of the original continuous square-root particle model.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The final2023 survey explicitly states that the complete detectability extension remains open. Known square-root particle estimates in the inspected2023/2024 papers impose stable drift and full-rank scalar observation precision; their deterministic transport alternative has different dynamics. Bishop–Del Moral's mean estimates have additional stability or time-horizon restrictions, which are retained in the review.

The inspected2026 discrete-generation results concern prediction/update chains, and the continuous-time mean-field result concerns conditional laws with deterministic Riccati covariance. Neither displayed model supplies the uniform finite-ensemble estimate above. The September2026 localization paper uses a discrete perfect-model signal. No uniform-in-step-size passage to this particle system is inferred.

The18October2026 cached Prove2Me comparison checked186 listing pages,4638missions. The four detectability contexts all concern dark-matter nuclear recoil detection. This is a description-level comparison, not a review of every mission proof. The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-enkbf-detectability-review.json) and [coordinator review](../FURTHER_problems/_tracking/enkbf-detectability-coordinator-review-2026-10-18.json) passed at their recorded extents. These checks preserve the finite-ensemble dynamics and distinguish current mean-field, discrete-time and fixed-horizon results; they do not certify every cited proof.

The August 2026 [multilevel localized EnKBF paper](https://doi.org/10.3934/fods.2026023), final equations (2.9)–(2.10), proves fixed-horizon bounds (Theorems 2.1 and 2.3); its localized estimate is explicitly a conjecture (3.5, Remarks 3.6–3.7). It supplies no uniform-in-time detectability result. The 2026 [near-linear EnKF accuracy paper](https://doi.org/10.1137/25M1732544) studies discrete prediction/update dynamics; no passage with constants uniform in time and discretization is inferred.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6bd477ec337952af**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
