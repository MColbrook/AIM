# 428. The sharp first Steklov eigenvalue with fixed boundary area

**Area:** Spectral geometry and shape optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

For an integer $`n\ge3`$, let $`\mathcal D_n`$ consist of nonempty bounded connected open sets $`\Omega\subset\mathbb R^n`$ with smooth boundary. Allow arbitrary topology and any number of boundary components. Set $`A(\Omega)=\mathcal H^{n-1}(\partial\Omega)`$ and let $`\sigma_1(\Omega)`$ be the first positive Steklov eigenvalue:
```math
\Delta u=0\quad\hbox{in }\Omega,\qquad
\partial_\nu u=\sigma u\quad\hbox{on }\partial\Omega.
```

Equivalently,
```math
\sigma_1(\Omega)=\inf_{\substack{u\in H^1(\Omega),\ \int_{\partial\Omega}u=0\\
\int_{\partial\Omega}u^2>0}}
\frac{\int_\Omega|\nabla u|^2}{\int_{\partial\Omega}u^2}.
```

Determine exactly, for each $`n\ge3`$,
```math
C_n=\sup_{\Omega\in\mathcal D_n}\sigma_1(\Omega)A(\Omega)^{1/(n-1)}.
```

The target is the sharp constant, including sharpness through approximating domains. A smooth maximizing domain need not exist. The product is invariant under dilation, so the problem is equivalent to fixing total boundary area.

## Application

The constant measures the greatest fundamental boundary relaxation frequency obtainable by changing the shape of a Euclidean medium while keeping its total boundary area fixed.

## References

1. A. Fraser and R. Schoen, [*Shape optimization for the Steklov problem in higher dimensions*](https://arxiv.org/abs/1711.04381), v1 (2017), Introduction, pp.1–2, Theorem 1.1 and Proposition 2.1; *Advances in Mathematics* **348** (2019), 146–162. [DOI](https://doi.org/10.1016/j.aim.2019.03.011).
2. D. Vinokurov, [*Geometric bounds for Steklov and weighted Neumann eigenvalues on Euclidean domains*](https://arxiv.org/html/2604.03418), v3 (2026), Introduction, Eqs.(1.1)–(1.3) and the paragraph immediately before Definition 1.1.
3. D. Chen, H. Liu and C. Yang, [*Isoperimetric bounds for the weighted Neumann and Steklov eigenvalues in dimensions three through six*](https://arxiv.org/html/2609.33555), v1 (2026), Section 1.1 and Corollary 1.4.

## Status review

Reference 1 gives a finite universal upper bound and examples showing that the ball is not optimal, even among contractible domains. Reference 2 explicitly reconfirms that the sharp boundary-area-only constant remains unknown in general.

Recent sharp results in references 2–3 concern the different mixed normalization
$`\sigma_1(\Omega)A(\Omega)|\Omega|^{(2-n)/n}`$.
They do not determine the displayed supremum. Convex-domain results also impose a restriction absent here.

The [coordinating review](../FURTHER_problems/_tracking/focused-C198-Steklov-Lachaume-two-precise-gates-C-20261028/ROOT-STEKLOV-INDEPENDENT-PRIMARY-NORMALIZATION-CURRENT-AND-FINAL-REVIEW.json) records primary theorem comparisons, current-resolution and announcement searches, semantic duplicate checks and access limitations. Bounded searches do not prove continued openness.


### Online recheck, 2026-10-30

The 2026 sharp mixed boundary-area/volume normalization is different from sigma1 times boundary area^(1/(n-1)). Fixed-volume product, convex-only, exterior and manifold-metric results do not determine this supremum over all smooth Euclidean domains.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2604.03418); [status source 2](https://arxiv.org/abs/2609.33555); [status source 3](https://arxiv.org/abs/1711.04381). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-12f901dd5cb5dc2c** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
