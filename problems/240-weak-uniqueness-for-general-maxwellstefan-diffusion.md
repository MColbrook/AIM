# 240. Weak uniqueness for general Maxwell–Stefan diffusion

**Area:** Multicomponent diffusion / cross-diffusion PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^3=(\mathbb R/\mathbb Z)^3`$, $`n\ge3`$, $`T>0`$, and fix arbitrary constants $`D_{ij}=D_{ji}>0`$ for $`i\ne j`$. Let $`c^0=(c_1^0,\ldots,c_n^0)`$ be measurable, with $`c_i^0\ge0`$ and $`\sum_i c_i^0=1`$ almost everywhere. There are no reactions or bulk advection.

Consider concentrations $`c_i`$, weighted velocities $`q_i`$, and fluxes $`J_i=\sqrt{c_i}\,q_i`$ on $`\mathbb T^3\times(0,T)`$ satisfying

```math
0\le c_i\le1,\qquad \sum_i c_i=1,\qquad \sum_i J_i=0,
\qquad \nabla c_i=-\sum_{j\ne i}\frac{c_jJ_i-c_iJ_j}{D_{ij}}.
```

The flux relation holds in distributions. Require $`q_i=0`$ almost everywhere on $`\{c_i=0\}`$ and

```math
c_i\in C([0,T];L^2(\mathbb T^3)),\qquad
\sqrt{c_i}\in L^2(0,T;H^1(\mathbb T^3)),\qquad
q_i\in L^2(\mathbb T^3\times(0,T);\mathbb R^3).
```

Mass conservation and the initial condition mean that, for every smooth periodic $`\phi`$ compactly supported before $`T`$,

```math
\int_{\mathbb T^3}c_i^0\phi(0)\,dx+
\int_0^T\int_{\mathbb T^3}
(c_i\partial_t\phi+J_i\cdot\nabla\phi)\,dx\,dt=0,
\qquad c_i(0)=c_i^0.
```

Use the physical entropy admissibility condition

```math
H(c(t))+\frac12\sum_{i=1}^n\sum_{j\ne i}
\int_0^t\int_{\mathbb T^3}
\frac{|\sqrt{c_j}q_i-\sqrt{c_i}q_j|^2}{D_{ij}}\,dx\,ds
\le H(c^0),
\qquad H(c)=\int_{\mathbb T^3}\sum_i c_i(\log c_i-1)\,dx,
```

for almost every $`t\in(0,T)`$, with $`0\log0=0`$.

Must any two such solutions with the same $`c^0`$ have identical concentrations and fluxes? Prove uniqueness for every choice above, or construct two admissible solutions for which it fails. No bound on $`J_i`$ in $`L^\infty`$ and no smooth positive reference solution is assumed.

## Application

Maxwell–Stefan equations describe coupled transport in gas mixtures, membranes and electrochemical devices. Global weak existence permits rough compositions and vanishing species. Uniqueness in this physical finite-dissipation class would make that evolution unambiguous without first establishing global classical regularity.

## Status review


**Known cases:** The general entropy weak-class target removes bounded-flux or smooth-reference assumptions. The current renormalized theorem requires bounded fluxes; whole-space weak existence and additive-friction strong results do not give arbitrary-coefficient weak uniqueness including vacuum.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The general-coefficient weak uniqueness problem is explicitly retained in the published 2024 introduction of Georgiadis–Jüngel. The torus formulation above uses the weak class of Georgiadis–Kim–Tzavaras, with finite dissipation up to the initial time and the natural entropy inequality made explicit. Their Theorem 6 and Corollary 7 establish uniqueness when both solutions additionally have essentially bounded molar fluxes; their §8 distinguishes that hypothesis from the estimates supplied by weak existence. The present question asks to remove that extra regularity assumption within the entropy-admissible class.

Chen–Jüngel prove weak uniqueness for a special family of diffusion coefficients. General weak–strong results require one positive spatially Lipschitz reference solution. The 2026 whole-space theorem gives weak existence, while the September 2026 strong theorem assumes additive friction $`D_{ij}^{-1}=g_i+g_j`$ and uniformly positive regular data. These statements do not establish the requested arbitrary-coefficient weak uniqueness. AIM 479 asks global classical continuation on a bounded domain with positive smooth data; the question here concerns uniqueness for rough weak solutions, including vacuum, on the torus.

The [June 2024 ReaDiNet workshop abstract](https://readinet.math.cnrs.fr/program_IRN_Clermont2024.pdf), p. 7, announced weak uniqueness without specifying its regularity class. The later July 2024 full theorem by the same author and collaborators explicitly requires bounded fluxes. The review compares these actual statements; it does not infer an unrestricted theorem from the workshop abstract.



### Online recheck, 2026-10-30

The general entropy weak-class target removes bounded-flux or smooth-reference assumptions. The current renormalized theorem requires bounded fluxes; whole-space weak existence and additive-friction strong results do not give arbitrary-coefficient weak uniqueness including vacuum.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2311.10465); [status source 2](https://arxiv.org/abs/2606.25536); [status source 3](https://arxiv.org/abs/2609.06732). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References

- S. Georgiadis and A. Jüngel, *Global existence of weak solutions and weak–strong uniqueness for nonisothermal Maxwell–Stefan systems*, Nonlinearity **37** (2024), 075016, §1.2 p. 4 (the isothermal weak uniqueness question). [Published article](https://repositum.tuwien.at/bitstream/20.500.12708/199837/1/Georgiadis-2024-Nonlinearity-vor.pdf), [DOI](https://doi.org/10.1088/1361-6544/ad4c49).
- A. Jüngel and I. V. Stelzer, *Existence analysis of Maxwell–Stefan systems for multicomponent mixtures*, SIAM Journal on Mathematical Analysis **45**(4) (2013), 2421–2440, [DOI](https://doi.org/10.1137/120898164). [Original preprint](https://arxiv.org/pdf/1211.2394v1), Theorems 1–2 and entropy estimates in §3.
- S. Georgiadis, H. Kim and A. E. Tzavaras, *Renormalized solutions for the Maxwell–Stefan system with an application to uniqueness of weak solutions*, [arXiv:2311.10465v2](https://arxiv.org/pdf/2311.10465v2) (9 July 2024), Definition 1 pp. 6–7, Theorem 6 and Corollary 7 p. 8, §8 p. 25.
- X. Chen and A. Jüngel, *A note on the uniqueness of weak solutions to a class of cross-diffusion systems*, [DOI](https://doi.org/10.1007/s00028-017-0420-4), Corollary 5 (special coefficient family).
- M. Heitzinger and A. Jüngel, *Weak–strong uniqueness for general cross-diffusion systems with volume filling*, [arXiv:2509.25978v1](https://arxiv.org/html/2509.25978v1), Definitions 1–2 and Theorem 1.
- S. Georgiadis, *Global existence of weak solutions for the Maxwell–Stefan system in the whole space*, [arXiv:2606.25536v1](https://arxiv.org/html/2606.25536v1), Definition 1 and Theorem 2.
- D. Bothe, *Global strong solutions for Maxwell–Stefan diffusion with additive friction coefficients*, [arXiv:2609.06732v1](https://arxiv.org/html/2609.06732v1), Definition 2.1 and Theorem 14.2.

[Source review](../FURTHER_problems/_tracking/parallel/continuum/maxwell-stefan-weak-uniqueness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-maxwell-stefan-weak-uniqueness-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/maxwell-stefan-weak-uniqueness-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/maxwell-stefan-prove2me0156-review.json) and [coordinator review](../FURTHER_problems/_tracking/maxwell-stefan-weak-uniqueness-coordinator-review-2026-10-17.json) record the checked scope and remaining access/version gaps. These are dated literature checks, not a guarantee that no solution exists.

## Collection provenance

Promoted from retained further problem **FURTHER-0556eb414144efb3** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
