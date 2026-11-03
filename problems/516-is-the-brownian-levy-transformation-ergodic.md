# 516. Is the Brownian Lévy transformation ergodic?

**Area:** Stochastic analysis and ergodic theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`W=C_0([0,\infty),\mathbb R)`$ carry standard Wiener measure $`\mathbb P`$ and its completed Borel sigma-algebra. Here paths start at zero, and the Borel structure comes from uniform convergence on compact intervals. Write $`B_t(\omega)=\omega(t)`$.

The **Lévy transformation** is the almost-surely defined path-space map

```math
(TB)_t=\int_0^t\mathrm{sgn}(B_s)\,dB_s
       =|B_t|-L_t^0(B),\qquad t\ge0,
```


where the integral is Itô's and $`L^0`$ is symmetric semimartingale local time in Tanaka's normalization. Choose a measurable version and extend it arbitrarily on its exceptional null set. The convention for $`\mathrm{sgn}(0)`$ does not affect the map almost surely. Its output is again standard Brownian motion, so $`T`$ preserves $`\mathbb P`$.

**Is $`T`$ ergodic?** Precisely, must every measurable $`A\subseteq W`$ satisfying

```math
\mathbb P\bigl(A\mathbin{\triangle}T^{-1}A\bigr)=0
```


have $`\mathbb P(A)\in\{0,1\}`$?

This is the one-sided, zero-drift continuous Brownian transformation on the entire half-line. It does not additionally ask for mixing or exactness.

## Application

The question asks whether repeated nonlinear transformations of Brownian noise leave any nontrivial invariant event, connecting stochastic integration with ergodic theory.

## References

1. D. Revuz and M. Yor, [*Continuous Martingales and Brownian Motion*](https://link.springer.com/chapter/10.1007/978-3-662-21726-9_7), first edition (1991), Chapter VI, Notes and Comments, Section 2, Question 1, p. 257; Exercise 2.32, p. 231.
2. L. E. Dubins, M. Émery and M. Yor, [*On the Lévy transformation of Brownian motions and continuous martingales*](https://www.numdam.org/item/SPS_1993__27__122_0/), Séminaire de Probabilités XXVII (1993), 122–132, Introduction.
3. V. Prokaj, [*Some sufficient conditions for the ergodicity of the Lévy transformation*](https://arxiv.org/html/1206.2485v3), arXiv:1206.2485v3 (2013), §§2.1–2.2.
4. V. Prokaj, [*On the exactness of the Lévy-transformation*](https://arxiv.org/html/1407.2974v2), arXiv:1407.2974v2 (2014), condition (4) and Theorem 1.
5. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, [*Limit theorems and ergodicity for general bootstrap random walks*](https://doi.org/10.1214/22-EJP818), Electronic Journal of Probability **27** (2022), paper 92; [preprint](https://arxiv.org/html/2010.16000v2), Introduction and §5.

## Status review

Prokaj's results give sufficient conditions for mixing or exactness; they do not establish those conditions for this transformation. The 2022 paper explicitly distinguishes the continuous open question from its discrete results. Density of iterated paths in a topology also does not by itself settle measurable ergodicity.

The [independent review](../FURTHER_problems/_tracking/B062-Revuz-Yor-thirteen-new-native-scientific-C-20261027/ROOT-LEVY-EXACT-MODEL-CURRENT-AND-SEMANTIC-DUPLICATE-GATES-PASS.json) records current and announced-resolution searches and all-status AIM/OpenAI/FURTHER comparisons. It also links an earlier unadmitted occurrence of the same question. The existing two-sided positive-drift Brownian queue problem concerns a different map. No matching resolution or canonical duplicate was located in these bounded AI checks; they are not human peer review or a certificate of openness.


### Online recheck, 2026-10-30

The continuous Brownian half-line Lévy transformation is the target. Density/topological recurrence and sufficient conditions for exactness do not prove its ergodicity; no newer complete announcement found.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1206.2485); [status source 2](https://www.numdam.org/article/SPS_1993__27__122_0.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-05a9c1280279133e** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
