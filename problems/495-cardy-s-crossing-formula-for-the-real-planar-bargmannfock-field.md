# 495. Cardy's crossing formula for the real planar Bargmann–Fock field

**Area:** Probability, smooth Gaussian fields and continuum percolation
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`f:\mathbb R^2\to\mathbb R`$ be the real analytic version of the centered stationary Gaussian field with covariance
```math
\mathbb E[f(x)f(y)]=\exp\!\left(-\frac{|x-y|^2}{2}\right).
```

This is the real planar Bargmann–Fock field. For $`\varepsilon>0`$, put $`f_\varepsilon(x)=f(x/\varepsilon)`$.

For each fixed aspect ratio $`\rho>0`$, let
```math
D_\rho=(0,\rho)\times(0,1),\qquad Q_\rho=\overline{D_\rho}.
```

Let $`C_{\varepsilon,\rho}`$ be the event that there exists a continuous curve $`\gamma:[0,1]\to Q_\rho`$ such that
```math
\gamma(0)\in\{0\}\times[0,1],\qquad
\gamma(1)\in\{\rho\}\times[0,1],\qquad
f_\varepsilon(\gamma(t))\ge0\quad(0\le t\le1).
```

Thus the curve crosses the rectangle from left to right inside the zero-level nonnegative excursion set.

Label the corners in counterclockwise order by
```math
a=(0,1),\quad b=(0,0),\quad c=(\rho,0),\quad d=(\rho,1).
```

Let $`\phi_\rho:D_\rho\to\mathbb H`$ be the conformal map, continuously extended to the boundary in the Riemann sphere, normalized by
```math
\phi_\rho(a)=0,\qquad\phi_\rho(c)=1,\qquad\phi_\rho(d)=\infty,
\qquad \eta_\rho=\phi_\rho(b)\in(0,1).
```

**For every $`\rho>0`$, prove or disprove**
```math
\lim_{\varepsilon\downarrow0}\mathbb P(C_{\varepsilon,\rho})
=\frac{\Gamma(2/3)}{\Gamma(1/3)\Gamma(4/3)}
\eta_\rho^{1/3}\,{}_2F_1\!\left(\frac13,\frac23;\frac43;\eta_\rho\right).
```

Here $`\Gamma`$ is the gamma function and $`{}_2F_1`$ is the Gauss hypergeometric function. The requested limit is pointwise for each fixed aspect ratio.

This is the rectangular-crossing subquestion in the second bullet of Beliaev's Conjecture 6.4 [1]. The square case $`\rho=1`$ already has crossing probability $`1/2`$ at every scale, by planar crossing duality, sign symmetry and rotation symmetry; the displayed right-hand side is also $`1/2`$. The open target concerns the full family of aspect ratios.

## Application

The formula would predict large-scale connectivity of positive regions in a smooth random medium from the conformal shape of the observation window. This field also appears as the local scaling limit of the Kostlan ensemble of real random polynomials, connecting the question to the geometry of typical real algebraic curves [1].

## Status review

The critical excursion level is known to be zero. Russo–Seymour–Welsh estimates already give a positive lower bound on each fixed-aspect-ratio crossing probability uniformly in scale [2, Theorems 1.3–1.4]. These estimates leave the exact limiting probability in the question above undetermined.

The field here is real-valued, has covariance $`e^{-|x-y|^2/2}`$, and has dependent signs. AIM 090 asks for independent square-lattice bond crossings. The currently listed OpenAI families 223 and 224 describe square-lattice random-cluster and Poisson–Voronoi results respectively; no matching Gaussian-field Cardy assertion was identified in their descriptions and constituent abstracts. The present question uses the same Cardy function, with the normalization in [3, Corollary 2.3].



### Online recheck, 2026-10-30

Checked Beliaev's Gaussian-field discussion and recent Cardy searches. Lattice/random-cluster Cardy results and Bargmann–Fock RSW bounds do not identify the exact Gaussian-field rectangle limit.

Comparators and current-status sources: [status source 1](https://arxiv.org/html/2207.13448); [status source 2](https://projecteuclid.org/journals/probability-surveys/volume-20/issue-none/Smooth-Gaussian-fields-and-percolation/10.1214/23-PS24.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References
1. Dmitry Beliaev, [*Gaussian fields and percolation*, arXiv:2207.13448v1](https://arxiv.org/pdf/2207.13448v1), 27 July 2022: §2.2, p. 8, defines the field; Conjecture 6.4, p. 31, asks for its Cardy crossing formula. The later publication is *Smooth Gaussian fields and percolation*, **Probability Surveys 20** (2023), 897–937, [DOI 10.1214/23-PS24](https://doi.org/10.1214/23-PS24). This review checked the exact arXiv v1 body; the complete published PDF and parity between editions were unavailable.
2. Alejandro Rivera and Hugo Vanneuville, [*The critical threshold for Bargmann–Fock percolation*](https://ahl.centre-mersenne.org/item/10.5802/ahl.29.pdf), **Annales Henri Lebesgue 3** (2020), 169–215, DOI 10.5802/ahl.29, Theorems 1.3–1.4, p. 172.
3. Mikhail Khristoforov, Mikhail Skopenkov and Stanislav Smirnov, [*A Generalization of Cardy's and Schramm's Formulae*](https://doi.org/10.1007/s00220-025-05255-z), **Communications in Mathematical Physics 406**, article 105 (2025), Corollary 2.3. Its percolation model is critical site percolation on the triangular lattice.

## Collection provenance

Promoted from retained further problem **FURTHER-4cdedd0d0ac7c490** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
