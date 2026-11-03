# 887. Does a multivariate Riccati diffusion forget its initial covariance under common noise?

**Area:** Nonlinear filtering and data assimilation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$, let $`A\in\mathbb R^{d\times d}`$ be arbitrary, and let $`R,S`$ be real symmetric positive-definite $`d\times d`$ matrices. Write $`\mathcal S_d^+`$ for the positive-definite symmetric matrices. For an integer $`N\ge d+1`$, consider the Itô equation

```math
dP_t=(AP_t+P_tA^\top+R-P_tSP_t)\,dt
 +\frac{2}{\sqrt N}\bigl[P_t^{1/2}\,dM_t\,R^{1/2}\bigr]_{\mathrm{sym}},
\qquad P_0=Q\in\mathcal S_d^+.
```

Here $`M`$ is a $`d\times d`$ matrix of independent standard real Brownian motions, $`[B]_{\mathrm{sym}}=(B+B^\top)/2`$, and all matrix square roots are the principal positive square roots. Let $`P_t^{N,Q}`$ denote the unique strong positive-definite solution. In comparing different initial conditions, use **the same matrix Brownian motion and the displayed diffusion coefficient**.

Is the following assertion true? For every $`p\in[1,\infty)`$ and every compact $`K\subset\mathcal S_d^+`$, there is an integer $`N_0\ge d+1`$ such that for every integer $`N\ge N_0`$ there are constants $`C<\infty`$ and $`\lambda>0`$ satisfying

```math
\left(\mathbb E\left\|P_t^{N,Q_1}-P_t^{N,Q_2}\right\|_F^p\right)^{1/p}
\le C e^{-\lambda t}\|Q_1-Q_2\|_F
\qquad(t\ge0,\;Q_1,Q_2\in K)?
```

The constants may depend on $`A,R,S,d,p,K,N`$, but not on $`t,Q_1,Q_2`$. The threshold $`N_0`$ may depend on $`A,R,S,d,p,K`$. Prove this assertion or give admissible parameters for which it fails for arbitrarily large $`N`$.

This is a deliberately restricted quantitative version of the multivariate contraction question in Bishop–Del Moral, §8.4. It concerns the $`\kappa=0`$ covariance diffusion associated with the deterministic ensemble Kalman–Bucy filter. It imposes full-rank $`R,S`$ and restricts initial covariances to a compact subset of the positive cone; it makes no assertion about an optimal rate as $`N\to\infty`$.

## Application

An ensemble Kalman–Bucy filter estimates the covariance needed to weight incoming measurements. Contraction under shared noise would quantify how two such covariance estimates lose their dependence on their initial values, including for unstable linear signal dynamics. This is a stronger statement about coupled trajectories than convergence of their separate distributions to an invariant law.

## References

1. A. N. Bishop and P. Del Moral, [*On the mathematical theory of ensemble (linear-Gaussian) Kalman–Bucy filtering*](https://doi.org/10.1007/s00498-023-00357-2), Mathematics of Control, Signals, and Systems **35** (2023), 835–903. [Author-hosted published PDF](https://people.bordeaux.inria.fr/pierre.delmoral/math-EnKF-2023.pdf): equation (5.2), Theorem 5.1, scalar estimate (6.27), and §8.4, physical PDF pp. 21, 23, 45 and 62. The general multivariate direction is explicit; the precise compact-set assertion above is a formulation of its deterministic-ensemble special case.
2. A. N. Bishop and P. Del Moral, [*On the stability of matrix-valued Riccati diffusions*](https://doi.org/10.1214/19-EJP342), Electronic Journal of Probability **24** (2019), paper 84, 1–40. [Published institutional copy](https://opus.lib.uts.edu.au/rest/bitstreams/6b773bf0-99dc-4b30-a556-4a26dd2bfaef/retrieve): equations (1.3)–(1.5), Theorems 2.1 and 2.4, and §2.2.1. Here the noise parameter is $`\epsilon=2/\sqrt N`$ and $`\kappa=\varpi=0`$.
3. A. N. Bishop, P. Del Moral, K. Kamatani and B. Rémillard, [*On one-dimensional Riccati diffusions*](https://doi.org/10.1214/18-AAP1431), Annals of Applied Probability **29** (2019), 1127–1187. [Author manuscript v3](https://opus.lib.uts.edu.au/bitstream/10453/160470/2/1711.10065v3.pdf): Theorem 5.10 and Appendix B.5 give a common-noise scalar flow estimate in a weighted distance.
4. P. Del Moral, B. Nasri and B. Rémillard, [*Fluctuations and long-time stability of multivariate ensemble Kalman filters*](https://doi.org/10.1007/s42081-026-00361-1), Japanese Journal of Statistics and Data Science (2026); [arXiv:2601.17392v2](https://arxiv.org/html/2601.17392v2). Equations (5)–(17), Theorem 2.1 and §6.3 concern discrete-generation prediction/update steps.

## Status review


**Known cases:** Convergence of laws does not establish the displayed principal-root shared-Brownian coupling estimate. Scalar flow contractions are known, but discrete-generation fluctuation results and multivariate moment or deterministic-flow perturbation estimates do not give the common-noise Lipschitz contraction for all large ensemble sizes.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Convergence of laws does not establish the displayed principal-root shared-Brownian coupling estimate. Scalar flow contractions are known, but discrete-generation fluctuation results and multivariate moment or deterministic-flow perturbation estimates do not give the common-noise Lipschitz contraction for all large ensemble sizes.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2023 source explicitly leaves multivariate counterparts of its scalar covariance-flow contraction estimate open. Its weighted convergence-of-laws theorem does not specify the coupling required above. The 2026 discrete-generation result controls the error relative to the deterministic discrete Riccati recursion; the inspected statements do not establish this continuous-time shared-noise estimate. Scalar results are already known.

Current primary records and targeted searches through 17 October 2026 located no matching solution or complete announcement. Independent primary audits checked the equation, principal roots, positivity threshold, common-noise coupling and quantifiers. The all-status AIM/OpenAI and FURTHER comparisons found no equivalent target; AIM 319 concerns static output-feedback stabilization.

The fresh Prove2Me listing snapshot contains 4,629 distinct missions on 186 pages. All 14 relevant matching contexts are textually identical to previously reviewed unrelated contexts. This checks listing descriptions, not every mission proof. Scalar published-version parity and the published 2026 discrete-paper parity remain unchecked; those limitations do not identify a matching multivariate result. See the [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/matrix-riccati-contraction-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-riccati-review.json) and [fresh catalogue comparison](../FURTHER_problems/_tracking/fresh-catalogue-riccati-skt-rank-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-702a5ee91d9e691a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
