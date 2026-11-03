# 627. Generic one-to-one boundary parametrization of the SDP-exact distance region

**Area:** Algebraic geometry of continuous optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix $`2\le m\le n`$. Choose generic quadratic polynomials
```math
f_i(x)=x^TA_ix+2a_i^Tx+\alpha_i,\qquad i=1,\ldots,m,
```

with real symmetric $`n\times n`$ matrices $`A_i`$, vectors $`a_i`$, and scalars $`\alpha_i`$. Generic means outside a proper algebraic exceptional set of coefficients. Work over $`\mathbb C`$ in the projective construction below.

Let $`X\subset\mathbb P^n_{\mathbb C}`$ be the complete intersection
```math
x^TA_ix+2x_0a_i^Tx+\alpha_ix_0^2=0\quad(i=1,\ldots,m),
```

and let $`Y\subset\mathbb P^m_{\mathbb C}`$ be the hypersurface
```math
\det\!\left(\lambda_0I_n-\sum_{i=1}^m\lambda_iA_i\right)=0.
```

Consider
```math
F:X\times Y\longrightarrow\mathbb P^n_{\mathbb C},\qquad
([x_0:x],[\lambda_0:\lambda])\longmapsto
\left[\lambda_0x_0:\lambda_0x-\sum_{i=1}^m\lambda_i(A_ix+x_0a_i)\right].
```

For generic coefficients this map is base-point free. Is its fiber a single point over a dense open subset of its image, componentwise if the image is reducible?

Equivalently, is the degree of this projection one, so that its image hypersurface has degree
```math
m\,2^m\binom{n}{m}?
```

When $`m=n`$, $`X`$ is a finite set and the product is reducible; the question retains the componentwise generic-fiber meaning. It does not assert that arbitrary generic real data have a nonempty real feasible set or that every complex component occurs in its real boundary.

## Application

The construction describes the algebraic boundary of the region where the first semidefinite relaxation recovers the nearest point on a variety cut out by quadrics. Its degree measures the algebraic complexity of that exactness region.

## References

1. D. Cifuentes, C. Harris and B. Sturmfels, [*The geometry of SDP-exactness in quadratic optimization*](https://doi.org/10.1007/s10107-019-01399-8), *Mathematical Programming* **182** (2020), 399-428. Definition 3.2, Section 5, equations (24)-(26), Lemma 5.5, Theorem 5.6 and Conjecture 5.7; [preprint v2](https://arxiv.org/abs/1804.01796).

## Status review

The published article explicitly conjectures generic projection degree one for $`m\ge2`$, after deriving the degree formula divided by that unknown projection degree. Reported computations support the conjecture but do not prove all dimensions. The excluded hypersurface case $`m=1`$ has projection degree two.

Results on individual Voronoi cells, sufficient conditions for exactness, arbitrary quadratic-objective algebraic degrees, or discrete Max-Cut complexity have different conclusions. No matching complete proof, counterexample or complete-resolution announcement was located in bounded checks through the date above.


### Online recheck, 2026-10-30

The exactness-region degree formula divides by an unknown projection degree. Reported computations, local Voronoi results and generic quadratic-optimization algebraic degrees do not prove generic componentwise degree one for every 2<=m<=n.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1804.01796); [status source 2](https://doi.org/10.1007/s10107-019-01399-8). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-b02802c5cb142ede** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
