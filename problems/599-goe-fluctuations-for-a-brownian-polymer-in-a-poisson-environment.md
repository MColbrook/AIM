# 599. GOE fluctuations for a Brownian polymer in a Poisson environment

**Area:** Probability, random media and statistical mechanics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`B`$ be standard Brownian motion from zero in $`\mathbb R`$, independent of a Poisson point process $`\omega`$ on $`(0,\infty)\times\mathbb R`$ with intensity $`\nu\,ds\,dx`$. Fix $`\nu,r>0`$ and $`\beta\in\mathbb R\setminus\{0\}`$. Define

```math
V_t(B)=\{(s,x):0<s\le t,\ |x-B_s|\le r/2\},
\qquad Z_t=\mathbb E_B\exp\{\beta\,\omega(V_t(B))\}.
```

The expectation averages the Brownian path with the environment fixed. Its endpoint is unrestricted. Write

```math
p(\beta,\nu,r)=\lim_{t\to\infty}\frac1t\log Z_t
```

for the known deterministic quenched free energy. For each fixed parameter triple, does there exist a deterministic nonzero constant $`\sigma(\beta,\nu,r)`$ such that, under the law of the environment,

```math
\frac{\log Z_t-p(\beta,\nu,r)t}
 {\sigma(\beta,\nu,r)t^{1/3}}
\ \xrightarrow[t\to\infty]{\mathrm{law}}\ \chi_1,
```

where $`\chi_1`$ has the standard Tracy–Widom GOE law?

The interval around the path has length $`r`$. All parameters remain fixed as time grows, and the centering uses the quenched growth rate. The source states an unspecified scale; nonzero is required for the denominator, and no additional sign restriction is imposed here. This question does not include endpoint conditioning or a parameter-scaling limit.

## Application

This tests KPZ universality for a continuous path interacting with non-Gaussian space-time impurities. It would identify the scale and distribution of fluctuations between environments beyond the exactly solvable polymer models.

## References

1. C. Cosco, *The Intermediate Disorder Regime for Brownian Directed Polymers in Poisson Environment*, [arXiv:1804.09571v2](https://arxiv.org/html/1804.09571v2), Sections 1.1–1.2, Conjecture 1.1. Published in Indagationes Mathematicae 30(5) (2019), 805–839.
2. F. Comets and C. Cosco, *Brownian Polymers in Poissonian Environment: a survey*, [arXiv:1805.10899v2](https://arxiv.org/html/1805.10899v2), revised 19 June 2023, Section 2.3 and Conjecture 10.1.1.
3. D. Dauvergne and L. Zhang, *Characterization of the directed landscape from the KPZ fixed point*, [arXiv:2412.13032v3](https://arxiv.org/html/2412.13032v3), Introduction, Theorem 1.6 and the following polymer discussion.

## Status review

The original paper poses this conjecture and the 2023 survey repeats it. Intermediate-disorder convergence changes model parameters. The newer directed-landscape framework requires prior KPZ-fixed-point convergence and does not supply the missing fixed-parameter result for this model.

Bounded searches for proofs, counterexamples, corrections and announced solutions found no matching complete resolution as of the check date. Current all-status AIM/OpenAI entries and the developing collection were compared semantically. AIM 287 concerns a Gaussian lattice polymer with fixed endpoint and a GUE limit; half-line white-noise KPZ rate questions also differ.

The [coordinating review](../FURTHER_problems/_tracking/focused-Brownian-Poisson-free-endpoint-GOE-C267-A-20261029/ROOT-FINAL-FIXED-PARAMETER-GOE-PRIMARY-CURRENT-SEMANTIC-REVIEW.json) records the independent model check and current comparisons. The exact latest original author version and survey passages were read; the full published 2019 body was unavailable, so parity with it is not asserted.


### Online recheck, 2026-10-30

Fixed nonzero parameters and a free Brownian endpoint are essential. Intermediate-disorder limits and directed-landscape results conditional on KPZ convergence do not prove the GOE fluctuation conjecture for this Poisson polymer.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1805.10899); [status source 2](https://arxiv.org/abs/1804.09571); [status source 3](https://arxiv.org/abs/2412.13032). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-73791f1a02124ba6** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
