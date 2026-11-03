# 998. Smooth perturbations at the same high irregularity exponents

**Area:** Rough paths and regularisation by noise
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge1`$, parameters $`\rho>1/2`$, $`1/2<\gamma<1`$ and $`0<\delta<1`$. For a continuous path $`w:[0,1]\to\mathbb R^d`$, define

```math
\|\Phi^w\|_{\gamma,\rho}
=\sup_{\substack{\xi\in\mathbb R^d\setminus\{0\}\\0\le s<t\le1}}
|\xi|^\rho(t-s)^{-\gamma}
\left|\int_s^t e^{i\xi\cdot w(r)}\,dr\right|.
```

Suppose $`w\in C^\delta([0,1];\mathbb R^d)`$ and $`\|\Phi^w\|_{\gamma,\rho}<\infty`$. Must

```math
\|\Phi^{w+\varphi}\|_{\gamma,\rho}<\infty
\qquad\text{for every }\varphi\in C^\infty([0,1];\mathbb R^d)?
```

Smoothness on the closed interval means smooth extendibility to a neighborhood. The bound may depend on the particular paths and all fixed parameters. The question preserves the **same** two exponents and concerns **every** eligible deterministic path. It imposes no probability model, adaptedness or stronger polynomial-phase irregularity premise.

## Application

The decay of these oscillatory occupation integrals measures the smoothing supplied by a path to irregular differential equations. Preserving the estimate under smooth trends would distinguish fine irregularity from a smooth background signal without weakening the available exponents.

## References

1. Lucio Galeati and Massimiliano Gubinelli, [*Prevalence of $`\rho`$-irregularity and related properties*](https://arxiv.org/abs/2004.00872v2), inspected accepted author version v2, 20 April 2023. Definition 3 on physical p. 8; Section 5.4 on pp. 47–50, particularly the conjecture paragraph on p. 48 and Theorem 85 on p. 49. Published in *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **60** (2024), 2415–2467, [DOI](https://doi.org/10.1214/23-AIHP1399). The final 53-page body was not checked for parity with the inspected 58-page version.
2. Lucio Galeati and Máté Gerencsér, [*Solution theory of fractional SDEs in complete subcritical regimes*](https://doi.org/10.1017/fms.2024.136), *Forum of Mathematics, Sigma* (2025), Section 9, Assumption 9.2 and Theorem 9.3. Selected published statements concern adapted perturbations of fractional Brownian motion.
3. Romito and Tolomeo, [*Yet another notion of irregularity through small ball estimates*](https://arxiv.org/abs/2207.02716v1), inspected v1; related published [DOI](https://doi.org/10.1016/j.spa.2026.104895), *Stochastic Processes and their Applications* **195** (2026), article 104895. Selected Propositions 3.1 and 3.3 concern stronger occupation-measure hypotheses and an exponent loss; final-body parity remains unchecked.

## Status review


**Known cases:** Every deterministic irregular path and exactly the same two exponents are required. Stronger polynomial-phase premises, exponent-loss estimates and probabilistic adapted-perturbation theorems do not settle this stability assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every deterministic irregular path and exactly the same two exponents are required. Stronger polynomial-phase premises, exponent-loss estimates and probabilistic adapted-perturbation theorems do not settle this stability assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source [1] explicitly retains this smooth-perturbation expectation under its standing assumption $`\rho>1/2`$. Lemma 83 proves estimates with a loss in the spatial exponent. Theorem 85 gives preservation of every smaller spatial exponent under the stronger hypothesis of strong irregularity, with a possibly different time exponent. Neither supplies the displayed same-pair assertion for every eligible path.

The earlier unrestricted low-$`\rho`$ formulation has a smooth-path counterexample, recorded separately in the research log. That example does not meet the present hypotheses. Almost-sure or prevalent statements, including the selected stochastic result [2], also have different quantifiers. The stronger Besov hypotheses and positive exponent loss in [3] do not prove this endpoint assertion.

No matching complete solution or announcement was located in the recorded bounded checks. This does not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/rho-smooth-shift-endpoint-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-rho-smooth-shift-endpoint-review.json), [current comparisons](../FURTHER_problems/_tracking/rho-smooth-shift-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/rho-smooth-shift-duplicates-review-2026-10-19.json), [catalogue check](../FURTHER_problems/_tracking/rho-smooth-shift-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/rho-smooth-shift-coordinator-review-2026-10-19.json) record the checked scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4e24d3efdc0d9bdf**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
