# 668. Harmonic-prior predictive dominance with unknown variance

**Area:** Bayesian statistical prediction and uncertainty quantification
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`m\ge k\ge3`$ and let $`N`$ be a positive integer with $`n=mN>k`$. Fix a real $`m\times k`$ matrix $`\widetilde X`$ of full column rank and put $`X=\mathbf1_N\otimes\widetilde X`$. Observe

```math
Y\sim N_n(X\beta,sI_n),
```

and predict the density $`p_{\beta,s}`$ of an independent future vector $`Z\sim N_m(\widetilde X\beta,sI_m)`$, where both $`\beta\in\mathbb R^k`$ and the common variance $`s>0`$ are unknown. Consider the improper priors, with densities relative to $`d\beta\,ds`$,

```math
\pi_H(\beta,s)=(\beta^T\widetilde X^T\widetilde X\beta)^{1-k/2}s^{-2},
\qquad \pi_R(\beta,s)=s^{-1}.
```

For each $`-1<\alpha<1`$, define the generalized Bayes predictive density by normalizing, as a function of $`z`$,

```math
q_{\pi,\alpha}(z\mid y)\ \propto\ 
\left[\mathbb E_{\pi(\beta,s\mid y)}
 p_{\beta,s}(z)^{(1-\alpha)/2}\right]^{2/(1-\alpha)}.
```

For probability densities $`q,p`$, use the loss

```math
D_\alpha(q,p)=\frac4{1-\alpha^2}
\left(1-\int_{\mathbb R^m}q(z)^{(1+\alpha)/2}
 p(z)^{(1-\alpha)/2}\,dz\right)
```

and the frequentist risk

```math
R_\alpha(\beta,s;q)=\mathbb E_{Y\mid\beta,s}
 D_\alpha(q(\cdot\mid Y),p_{\beta,s}).
```

**For every allowed design, $`N`$ and $`\alpha`$, does $`q_{\pi_H,\alpha}`$ dominate $`q_{\pi_R,\alpha}`$: risk no larger for every $`(\beta,s)`$, and strictly smaller for at least one parameter?** Prove or disprove this assertion.

The posterior and normalization are defined almost surely under the sampling model when $`n>k`$. Arbitrary definitions on the exceptional null set of observations do not affect the risk.

This is Problem 1 of Maruyama–Strawderman, retaining their replicated-design assumption (AS1). The prior $`\pi_H`$ is fixed; the predictive rule changes with $`\alpha`$. Unknown variance is essential. In this convention ordinary KL loss is the endpoint $`\alpha=-1`$, and reverse KL is $`\alpha=1`$.

## Application

A full predictive distribution describes uncertainty in future measurements. This question asks whether a shrinkage prior retains its risk advantage when forecasts are evaluated using different divergence losses and the noise variance must also be inferred. It concerns a specified statistical risk, rather than a general calibration guarantee.

## References

1. Y. Maruyama and W. E. Strawderman, *Bayesian predictive densities for linear regression models under alpha-divergence loss: some results and open problems*, IMS Collections **8** (2012), 42–56, [DOI](https://doi.org/10.1214/11-IMSCOLL803); [author preprint](https://arxiv.org/pdf/1002.3786v1), equations (1.1)–(1.11), assumption (AS1), and Problem 1, pp.1–3. Locators refer to this preprint.
2. A. Boisbunon and Y. Maruyama, *Inadmissibility of the best equivariant predictive density in the unknown variance case*, Biometrika **101** (2014), 733–740, [DOI](https://doi.org/10.1093/biomet/asu024); [latest preprint located](https://arxiv.org/pdf/1308.2765v3), Theorems 3.1–3.2.
3. Y. Maruyama, T. Matsuda and T. Ohnishi, *Harmonic Bayesian Prediction under alpha-Divergence*, IEEE Transactions on Information Theory **65** (2019), 5352–5366, [DOI](https://doi.org/10.1109/TIT.2019.2915245); [accepted author manuscript](https://yuzo-maruyama.github.io/Maruyama_Matsuda_Ohnishi_2019_IEEE_TIT.pdf), §I and Theorem 2.2. This manuscript explicitly treats known variances and is not the final typeset version.
4. E. George, G. Mukherjee and K. Yano, *Optimal Shrinkage Estimation of Predictive Densities Under alpha-Divergences*, Bayesian Analysis **16** (2021), 1139–1155, [DOI](https://doi.org/10.1214/21-BA1264); [published article](https://par.nsf.gov/servlets/purl/10314998), §2 and §6.

## Status review


### Online recheck, 2026-10-30

The fixed harmonic prior and replicated unknown-variance experiment are essential. Known-covariance harmonic prediction and ordinary-KL unknown-variance results have different hypotheses or endpoint loss. Fresh searches including indexed proof venues found no full interior-alpha unknown-variance dominance theorem or counterexample.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1002.3786); [comparison source 2](https://yuzo-maruyama.github.io/Maruyama_Matsuda_Ohnishi_2019_IEEE_TIT.pdf); [comparison source 3](https://yuzo-maruyama.github.io/research.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original source explicitly leaves this question open. Its endpoint results and its solution of Problem 2-1 do not settle the interior interval. Boisbunon–Maruyama treat ordinary KL loss. The 2019 harmonic-prior results assume known variances; the 2021 oracle-risk results also assume known variances and identify unknown covariance as future work. Neither establishes the stated fixed-prior, unknown-variance comparison.

Current searches on 17 October 2026 found no later complete resolution or announcement. This is bounded literature evidence. The original and 2014 main preprints were read completely; the 2021 published main article was read completely. Separate supplements and publisher parity gaps are recorded in the evidence packet. An independent selected-primary audit confirmed the prior measure, replicated design, loss orientation, alpha-specific rule, almost-sure posterior propriety and finite normalization. All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. In particular, retained AIM 662 concerns Gaussian variational covariance ordering for a fixed target, and AIM 347 concerns density-learning algorithms.

The fresh Prove2Me snapshot reconciles 4,629 listings over 186 pages. All 26 matching target contexts were read: 25 concern Euler–Maruyama numerical schemes, and one concerns confidence bounds for bounded losses. They do not announce the stated prediction result. Other filtering aliases in the combined scan were reviewed separately; this does not certify every mission proof.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/predictive-harmonic-alpha-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-predictive-harmonic-alpha-review.json) and [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/predictive-alpha-prove2me-batch0082-review.json) record exact passages, current searches and version limits. The original published 2012 body remains a parity gap; the eligible 2010 primary preprint contains the explicit question. These dated checks found no matching complete resolution or announcement.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c0ba18618b159b21**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
