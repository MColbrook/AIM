# 185. The strong Markov property for continuum dynamical percolation

**Area:** Probability, stochastic processes and critical phenomena
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathcal H_{\mathbb C}`$ be the Schramm–Smirnov space of planar percolation configurations. A configuration records which compact planar quadrilaterals are crossed: a quadrilateral is an embedded copy of the unit square with two distinguished opposite sides, and a crossing connects these sides inside the quadrilateral. Elements of $`\mathcal H_{\mathbb C}`$ are closed hereditary collections of such quadrilaterals, with the quad-crossing topology of [1, §2] and [2]. Hereditary means that a crossed quadrilateral also forces every quadrilateral whose crossing is implied by it to be crossed. The full-plane topology can be obtained from the corresponding bounded-domain topologies by the weighted restriction metric in [1, (9.7)].

On the triangular lattice of mesh $`\eta`$, initially colour sites independently black or white with probability $`1/2`$. Each site has an independent clock of rate
```math
r(\eta)=\frac{\eta^2}{\alpha_4^\eta(\eta,1)},
```

where $`\alpha_4^\eta(\eta,1)`$ is the critical probability of four alternating black and white arms from scale $`\eta`$ to scale $`1`$. At each ring resample that site's colour independently and fairly. Regard the hexagonal cells as a point of $`\mathcal H_{\mathbb C}`$.

Let $`X=(X_t)_{t\ge0}`$ be the stationary càdlàg scaling limit of these dynamics given by [1, Theorem 9.8], with initial law $`\mathbb P_\infty`$, the critical percolation scaling-limit law. Use the particular Borel Markov semigroup $`(P_s)_{s\ge0}`$ constructed in [1, §11.1], including its convention that starting configurations outside the full-measure set where the cutoff construction converges are made absorbing. Here $`P_sf(\omega)`$ is the expectation of $`f`$ at time $`s`$ under that specified extension started at $`\omega`$.

Write
```math
\mathcal F_t=\sigma(X_u:0\le u\le t)
```

for the natural filtration. **Is this stationary process strong Markov?** More explicitly, for every almost surely finite $`(\mathcal F_t)`$-stopping time $`\tau`$, every $`s\ge0`$, and every bounded Borel function $`f:\mathcal H_{\mathbb C}\to\mathbb R`$, does
```math
\mathbb E\!\left[f(X_{\tau+s})\mid\mathcal F_\tau\right]
=(P_sf)(X_\tau)
\quad\text{almost surely}?
```


The question concerns the stationary law and the published exceptional-state extension. It does not require a strong Markov family for every initial configuration, and does not replace the natural filtration by an extra right-continuous augmentation.

## Application

A positive answer would justify restarting the continuum critical dynamics at observation times chosen from its own past. Such times can depend on macroscopic connectivity events, rather than being fixed in advance.

## Known results and scope

Garban–Pete–Schramm prove the ordinary Markov property and reversibility under $`\mathbb P_\infty`$. Their Remark 11.9 observes that the process is not Feller in the quad-crossing topology. Thus the stopping-time assertion is additional to the established deterministic-time Markov property.

Their proof defines a full-measure set $`B`$ of starting configurations for which the cutoff dynamics converge, and makes configurations in $`B^c`$ absorbing. Whether exceptional configurations can be reached at stopping times matters for this fixed extension. The sentence in that proof referring to “this set $`B`$” as polar appears to have the complement omitted: the relevant exceptional set is $`B^c`$, whereas $`\mathbb P_\infty(B)=1`$.

Garban–Holden–Sepúlveda–Sun obtain mixing for the homogeneous process as part of their Liouville dynamical-percolation results [3, Theorem 1.4 and Remark 1.5 in the cited preprint]. This answers the older mixing question, rather than Question 11.10. Their selected convergence statements assert a Markov property; no strong Markov assertion is made there.

The 2026 Voronoi-percolation announcements [4] concern static critical crossings, expected pivotal counts, and joint near-critical crossing thresholds under a monotone coupling. Those selected main statements do not establish the stopped resampling-dynamics identity above.

## References

1. C. Garban, G. Pete and O. Schramm, *The scaling limits of near-critical and dynamical percolation*, Journal of the European Mathematical Society **20** (2018), no. 5, 1195–1268, [DOI](https://doi.org/10.4171/JEMS/786), [publisher PDF](https://ems.press/content/serial-article-files/32294?nt=1). Definitions and full-plane extension: §§1.3, 2 and 9.3; Markov property and question: §11.1 and Question 11.10. Latest arXiv version: [arXiv:1305.5526v4](https://arxiv.org/pdf/1305.5526v4) (2017).
2. O. Schramm and S. Smirnov, with an appendix by C. Garban, *On the scaling limits of planar percolation*, Annals of Probability **39** (2011), no. 5, 1768–1814, [DOI](https://doi.org/10.1214/11-AOP659), [author-hosted published PDF](https://www.unige.ch/~smirnov/papers/glue-j.pdf).
3. C. Garban, N. Holden, A. Sepúlveda and X. Sun, *Liouville dynamical percolation*, Probability Theory and Related Fields **180** (2021), 621–678, [DOI](https://doi.org/10.1007/s00440-021-01057-1). Actual selected theorem statements checked in [arXiv:1905.06940v2](https://arxiv.org/pdf/1905.06940v2) (2019), pp. 3–5; the published version's metadata and abstract were checked separately.
4. OpenAI, 2026 preprint announcements: [critical Voronoi crossing law](https://github.com/openai/math/blob/main/preprints/Cardys-formula-for-critical-Poisson-Voronoi-percolation-September-23-2026/paper.pdf), [pivotal amplitude](https://github.com/openai/math/blob/main/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/voronoi-pivotal-amplitude.pdf), and [quenched near-critical universality](https://github.com/openai/math/blob/main/preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf).

## Status review

Selected original definitions, the full-plane extension and exact question, selected current comparator main statements, official version histories, and the closest all-status AIM/FURTHER targets were checked on 24 October 2026. Bounded current and announcement searches found no matching resolution. Public AIM and OpenAI metadata were refreshed; Prove2Me checking was limited to target navigation on its public homepage.

The published Liouville-paper body was unavailable in the public subscription preview; its latest public preprint and the publisher's metadata and abstract were inspected separately. No published/preprint byte parity, full external proof verification, Lean verification, or whole-site completeness is claimed.


### Online recheck, 2026-10-30

The question is the stationary continuum scaling limit with its specified exceptional-state extension and natural filtration. Ordinary Markov, Liouville variants and Voronoi crossing/universality results do not establish this exact strong Markov assertion.

Comparators and current-status sources: [status source 1](https://doi.org/10.4171/JEMS/786); [status source 2](https://math.univ-lyon1.fr/~garban/Fichiers/memoirHDR.pdf); [status source 3](https://arxiv.org/abs/1905.06940). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-a1f1b07a98664724** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
