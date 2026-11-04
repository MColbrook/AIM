# 651. Global convergence of the simple CRDT conformal-mapping iteration

**Area:** Numerical conformal mapping

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`P`$ be a bounded simple polygon with nonzero interior angles. Apply the boundary subdivision in [1, Section 3]: at each corner of angle at most $`\pi/4`$, insert the midpoints of the two equal sides of the largest inscribed isosceles corner triangle and protect the resulting two corner edges. In each pass, simultaneously trisect every unprotected edge $`e`$ for which the geodesic distance inside $`P`$ to a vertex other than its endpoints is less than $`|e|/(3\sqrt2)`$. Repeat until no such edge remains; the source proves termination.

Write $`z_1,\ldots,z_n`$ for the counterclockwise vertices after subdivision, and fix a constrained Delaunay triangulation. Each internal diagonal determines the union of its two neighboring triangles. Label that quadrilateral's counterclockwise vertices by $`z_{\kappa(i,1)},\ldots,z_{\kappa(i,4)}`$, with the diagonal joining the first and third vertices, for $`1\le i\le n-3`$. Set

```math
\rho(a,b,c,d)=\frac{(d-a)(b-c)}{(c-d)(a-b)},\qquad c_i=\log\left|\rho(z_{\kappa(i,1)},z_{\kappa(i,2)},z_{\kappa(i,3)},z_{\kappa(i,4)})\right|.
```

For $`\sigma\in\mathbb R^{n-3}`$, let $`w_1,\ldots,w_n`$ be the cyclically ordered points on the unit circle satisfying

```math
\rho(w_{\kappa(i,1)},w_{\kappa(i,2)},w_{\kappa(i,3)},w_{\kappa(i,4)})=-e^{\sigma_i}.
```

They exist and are unique up to disk automorphisms [1, Theorem 1]. If $`\theta_j`$ is the interior angle at $`z_j`$, form the Schwarz–Christoffel primitive

```math
f_\sigma(w)=\int_0^w\prod_{j=1}^n(1-\omega/w_j)^{\theta_j/\pi-1}\,d\omega,
```

using the analytic branches in the disk normalized to equal 1 at the origin, and set $`\zeta_j(\sigma)=f_\sigma(w_j)`$. Define

```math
F_i(\sigma)=\log\left|\rho(\zeta_{\kappa(i,1)}(\sigma),\zeta_{\kappa(i,2)}(\sigma),\zeta_{\kappa(i,3)}(\sigma),\zeta_{\kappa(i,4)}(\sigma))\right|-c_i.
```

This expression is independent of the chosen disk normalization whenever finite.

Let $`\sigma_*`$ be the log-cross-ratio vector of the true conformal prevertices of $`P`$. In exact arithmetic, with exact integrals, does

```math
\sigma^{(0)}=c,\qquad \sigma^{(k+1)}=\sigma^{(k)}-F(\sigma^{(k)})
```

remain well defined and converge to $`\sigma_*`$ for every such polygon and constrained Delaunay triangulation? This is the simple iteration in [1, equation (7)], with its prescribed initial guess and fixed triangulation. No claim about arbitrary initial vectors is included.

## Application

A convergence theorem would supply a mathematical guarantee for a numerical conformal-mapping procedure used in potential theory and mesh generation, including polygons with long narrow channels.

## References

1. T. A. Driscoll and S. A. Vavasis, [Numerical conformal mapping using cross-ratios and Delaunay triangulation](https://doi.org/10.1137/S1064827596298580), *SIAM Journal on Scientific Computing* 19(6) (1998), 1783–1803. [Full text](https://www.math.stonybrook.edu/~bishop/classes/math401.F09/crdt.pdf), Sections 3–7, especially equation (7), p.1794.
2. C. J. Bishop, [Bounds for the CRDT conformal mapping algorithm](https://doi.org/10.1007/BF03321771), *Computational Methods and Function Theory* 10(1) (2010), 325–366. [Author manuscript](https://www.math.stonybrook.edu/~bishop/papers/crdt.pdf), Section 7, Figure 26 and Question (3).

## Status review

The original numerical experiments suggest convergence and even a polygon-dependent residual contraction factor below 1. Bishop proves a uniform quasiconformal bound for the initial guess, but explicitly leaves convergence of the iteration unresolved. His paper also disproves the separate proposed uniform bound on differences of logarithmic cross-ratios; that disproved bound is not part of this problem.

Targeted literature and platform searches found no matching resolution. Native Zenodo, GitHub issues/PRs and Palomar checks were supplemented by indexed arXiv searches; the native arXiv API request returned HTTP406. Software releases and a recent unrelated SC solver do not announce a proof of this iteration. Searches are bounded, and no equivalent catalogue entry was found.
