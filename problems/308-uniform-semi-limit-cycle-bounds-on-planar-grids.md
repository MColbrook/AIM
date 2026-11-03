# 308. Uniform semi-limit-cycle bounds on planar grids

**Area:** Dynamical systems; piecewise-affine flows
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix nonnegative integers $`r,s`$. Choose any $`r`$ distinct horizontal lines and $`s`$ distinct vertical lines in $`\mathbb R^2`$. They partition the plane into open rectangles (possibly unbounded), edges and vertices.

Consider any globally continuous vector field $`X:\mathbb R^2\to\mathbb R^2`$ whose restriction to each cell is affine: $`X(z)=A_Cz+b_C`$ on a cell $`C`$. The affine restrictions agree along shared boundaries. Such a field is globally Lipschitz, so its ordinary differential equation $`\dot z=X(z)`$ has a unique complete flow $`\varphi_t`$.

A **semi-limit cycle** means a nonconstant periodic orbit $`\gamma`$ for which some point $`z\notin\gamma`$ satisfies $`\omega(z)=\gamma`$ or $`\alpha(z)=\gamma`$, where
```math
\omega(z)=\{w:\varphi_{t_j}(z)\to w\text{ for some }t_j\to+\infty\},
```

and $`\alpha(z)`$ is defined with $`t_j\to-\infty`$. Thus an annulus of periodic orbits around a center does not by itself give semi-limit cycles.

Does there exist a finite number $`N(r,s)`$ bounding the number of distinct semi-limit cycles of every such field, uniformly over all line positions and all affine coefficients?

Only existence of a finite bound is requested. This is the grid conjecture in Panazzolo's Section 5.5, where “piecewise linear” includes affine terms. The separate conjecture for a fixed definable cell decomposition is not substituted for this uniform statement.

## Application

Continuous piecewise-affine systems model switching and saturation in feedback circuits and control systems. A bound determined by the number of grid lines would constrain how many attracting or repelling periodic regimes such a model can support as its coefficients and thresholds vary.

## References

1. D. Panazzolo, *Tame semiflows for piecewise linear vector fields*, Annales de l'Institut Fourier **52** (2002), 1593–1628. [DOI and journal record](https://doi.org/10.5802/aif.1928); [primary text](https://www.numdam.org/item/10.5802/aif.1928.pdf). Definition 4.1 and Section 5.5, pp. 1626–1627.
2. E. D. de Almeida, *O-minimal Theory: A tool to study the finiteness of limit cycles of piecewise vector fields*, 2026 V Symposium on Planar Vector Fields, [poster abstract](https://www.gsd.uab.cat/symp2026/data/uploads/abstracts/edutra-poster-lleida.pdf). Its piecewise-constant result is described as a first step toward the piecewise-linear conjecture; its flow conventions are not supplied.
3. R. Huzak and O. H. Perez, *An Unbounded Number of Canard Limit Cycles in Linear Regularizations of Piecewise Linear Systems*, Journal of Nonlinear Science **36** (2026), article 61. [Primary article](https://doi.org/10.1007/s00332-026-10281-9). Its variable smooth regularizations are a different class from the continuous fixed-grid affine fields here.

## Status review

Checked 30 October 2026. The source's continuity assumption, full grid partition and semi-limit-cycle definition were read directly. Two-zone results and the 2026 piecewise-constant announcement do not settle the arbitrary-grid question. The unbounded-cycle regularization construction was also checked: its starting fields are discontinuous and its smoothed transition strip is not affine on a fixed finite grid.

Bounded current searches found no matching complete resolution or announcement. Semantic checks against AIM, the current saved OpenAI announcements and private findings found no equivalent target. Announced polynomial-vector-field bounds do not automatically extend to this class. These checks are not a proof of openness; no complete proof audit of the cited articles is claimed.


### Online recheck, 2026-10-30

Checked current Panazzolo-related work and the 2026 unbounded-canard paper. Holomorphic saddle loops, discontinuous switching fields and smooth regularizations do not give a uniform bound or counterexample for globally continuous affine fields on a fixed rectangular grid.

Comparators and current-status sources: [status source 1](https://www.numdam.org/item/10.5802/aif.1928.pdf); [status source 2](https://doi.org/10.1007/s00332-026-10281-9); [status source 3](https://nonsper.math.cnrs.fr/activities/). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-fa6f8a64c29d7089** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
