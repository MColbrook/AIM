# 334. Competitive exclusion in a chemostat with unequal removal rates

**Area:** Mathematical biology and microbial competition

**Status:** 🔵 OPEN

**Last checked:** 2026-09-18

## Problem statement

Consider $`n\ge1`$ microbial species competing for one growth-limiting nutrient in a well-mixed continuous culture. Let $`D>0`$ be the nutrient dilution rate, $`S_{\mathrm{in}}>0`$ the feed concentration, and $`d_i>0`$ the removal rate of species $`i`$. For each species let $`f_i:[0,\infty)\to[0,\infty)`$ be $`C^1`$, with $`f_i(0)=0`$ and $`f_i'(s)>0`$ for $`s>0`$. Suppose each equation $`f_i(\lambda_i)=d_i`$ has a finite positive solution and, after relabelling,

```math
0<\lambda_1<\lambda_2\le\cdots\le\lambda_n,
\qquad \lambda_1<S_{\mathrm{in}}.
```

For $`n=1`$, only the conditions on $`\lambda_1`$ apply. With constant yields absorbed into the biomass variables, the nutrient concentration $`S(t)`$ and species concentrations $`x_i(t)`$ satisfy

```math
\dot S=D(S_{\mathrm{in}}-S)-\sum_{i=1}^n f_i(S)x_i,
\qquad
\dot x_i=(f_i(S)-d_i)x_i\quad(1\le i\le n).
```

Prove or disprove that, for every such system and every initial state $`S(0)\ge0`$, $`x_i(0)>0`$, its solution satisfies

```math
\lim_{t\to\infty}S(t)=\lambda_1,
\qquad
\lim_{t\to\infty}x_1(t)=\frac{D(S_{\mathrm{in}}-\lambda_1)}{d_1},
\qquad
\lim_{t\to\infty}x_i(t)=0\quad(i\ge2).
```

Thus the species requiring the lowest nutrient concentration for zero net growth would exclude all competitors. The constants $`d_i`$ may differ from one another and from $`D`$. Growth depends only on nutrient concentration; neither variable yields nor direct density-dependent interference is included. This is Hsu's Open problem 1 for model (2.9), under hypothesis (H), with the constant feed written as $`S_{\mathrm{in}}`$ to distinguish it from the initial concentration.

## Application

Chemostat models describe microbial competition in continuously supplied cultures and bioreactors. A break-even concentration measures the nutrient level at which a population replaces its losses. Species-specific removal incorporates differences in losses or retention that a common washout rate omits. The problem asks whether this equilibrium-based ranking predicts the eventual winner for arbitrary increasing growth laws and all initially present populations. A resolution would establish, or identify a limitation of, that prediction in this single-resource model.

## References

1. Sze-Bi Hsu, *A survey of constructing Lyapunov functions for mathematical models in population biology*, Taiwanese Journal of Mathematics 9(2) (2005), 151–173. [Author manuscript](https://www.math.nthu.edu.tw/~sbhsu/0416.pdf), pp. 4–9: response assumptions, hypothesis (H), model (2.9) and Open problem 1.
2. Tewfik Sari and Frédéric Mazenc, *Global dynamics of the chemostat with different removal rates and variable yields*, Mathematical Biosciences and Engineering 8(3) (2011), 827–840, DOI [10.3934/mbe.2011.8.827](https://doi.org/10.3934/mbe.2011.8.827). [Full paper](https://www.aimspress.com/aimspress-data/mbe/2011/3/PDF/1551-0018_2011_3_827.pdf), p. 828, explicit open question; Theorems 2–3 and constant-yield model (7).
3. Bernold Fiedler and Sze-Bi Hsu, *Non-periodicity of chemostats: a multi-dimensional Bendixson-Dulac approach*. [Author manuscript dated April 25, 2008](https://www.math.nthu.edu.tw/~sbhsu/FiedlerHsu_08_04_25_%282%29.pdf), §1, model (1.6), Theorem 1.1 and condition (1.9); §6. Published in Journal of Mathematical Biology 59 (2009), 233–253.
4. Tewfik Sari, *Competitive exclusion for chemostat equations with variable yields*, [arXiv:1005.3611v2](https://arxiv.org/abs/1005.3611v2), July 28, 2011. Introduction and Theorems 1.2 and 4.1; citations here refer to this author version.
5. Alain Rapaport and Mario Veruete, *A new proof of the competitive exclusion principle in the chemostat*, [arXiv:1711.06928, version 2](https://arxiv.org/abs/1711.06928), November 30, 2017. §2, model (1), Assumptions 1–2 and Proposition 1.
6. Claudia Alvarez-Latuz, Terence Bayen and Jérôme Coville, *Global stability of perturbed chemostat systems*, Nonlinear Analysis: Real World Applications 88 (2026), 104509, DOI [10.1016/j.nonrwa.2025.104509](https://doi.org/10.1016/j.nonrwa.2025.104509). [Author version, arXiv:2501.08011v1](https://arxiv.org/pdf/2501.08011v1), January 14, 2025, §§2.1–2.4, assumptions (A1)–(A4) and Theorem 2.4.
7. Sze-Bi Hsu, *Mathematical Modeling and Mathematical Analysis in Mathematical Biology*, [2019 summer-course notes](https://www.math.nthu.edu.tw/~sbhsu/7-26-2019final%20lecture1-6.pdf), Lecture 1, pp. 8–10: equation (4), hypothesis (H) and the explicit open problem on p. 10.
8. Jean-Baptiste Burie, Arnaud Ducrot and Quentin Griette, *Epidemic models in measure spaces: persistence, concentration and oscillations*, Journal of Evolution Equations 25 (2025), article 32. [Full paper](https://link.springer.com/article/10.1007/s00028-025-01060-2), model (2.1), Assumption 2.1, Theorem 2.2 and §2.3, Claim 2.14.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Hsu states the question explicitly and retains it in his 2019 lectures. Sari–Mazenc independently identify the same unresolved constant-yield problem on p. 828, despite their paper's broader treatment of variable yields. Their discussion separates general increasing growth from the solved Michaelis–Menten case. A single species and a common removal rate are also covered by established results; the unresolved assertion includes arbitrary species-dependent rates and general increasing responses.

Sari–Mazenc Theorem 3 restates the Wolkowicz–Lu global-convergence result with an additional separation condition on response-function ratios. Sari's Theorems 1.2 and 4.1 likewise require extra inequalities comparing species. Those sufficient conditions are not assumed here. The notation differs between sources: Sari's net growth function already subtracts removal, whereas $`f_i`$ in this entry denotes gross growth.

Fiedler–Hsu Theorem 1.1 excludes positive nonstationary periodic solutions under its additional inequality (1.9). It neither applies without that inequality nor by itself proves convergence of every trajectory. Rapaport–Veruete Proposition 1 allows arbitrary increasing responses, but model (1) uses the same dilution rate in every species equation.

Alvarez-Latuz–Bayen–Coville Theorem 2.4 concerns sufficiently small mass-conserving species-conversion perturbations of a common-removal chemostat. Assumption (A4) requires the conversion terms to sum to zero. Arbitrary independent changes in removal cannot be absorbed into those terms. The perturbation threshold also depends on a compact set of initial states. The full author-version theorem and model were read; the 2026 publisher introduction and model preview confirm the setting, but the full journal text was not available.

Burie–Ducrot–Griette use growth linear in the resource, with a measure describing strains. Their Theorem 2.2 gives convergence when the maximal-fitness set has positive initial mass. The oscillation counterexample in §2.3 has infinitely many strains and no initial mass on that set. It does not refute the finite-species assertion here, and the linear response does not settle arbitrary increasing responses.

Current and unrestricted resolution, counterexample, correction and version searches are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/chemostat-unequal-removal-exclusion.json). A separated adversarial self-pass passed on September 18, 2026; no independent agent or human review is claimed. Access limitations and additional model comparisons are explicit in the ledger. This review does not certify the cited proofs independently.

The closest catalogue question, [competitive exclusion with unequal death rates](183-competing-contact-unequal-deaths.md), concerns a spatial stochastic contact process. [Carrying-simplex interior smoothness](../cut_problems/problems/300-carrying-simplex-interior.md) concerns geometric regularity for discrete population maps. Neither asks for this deterministic resource-mediated convergence theorem. The present family is counted once across species numbers, growth laws and removal parameters.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
