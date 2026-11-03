# 755. Uniqueness of a finite-toughness hydraulic-fracture similarity profile

**Area:** Hydraulic fracture; nonlocal degenerate diffusion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`K>0`$. For $`x,z\in(-1,1)`$ set

```math
G(x,z)=\frac1\pi\log\!\left(\frac{1-xz+\sqrt{(1-x^2)(1-z^2)}}{|x-z|}\right),\qquad
g(x,z)=\frac12\big[(z-x)G(x,z)+(z+x)G(x,-z)\big].
```

The products at $`z=x`$ and $`z=-x`$ use their continuous limits, and $`g(\pm1,z)=0`$. For an even continuous function $`U:\mathbb R\to[0,\infty)`$ supported on $`[-1,1]`$, positive on $`(-1,1)`$, define its signed tail by

```math
\mathcal T_U(z)=
\begin{cases}
\displaystyle\int_z^1U(y)\,dy,&z>0,\\
\displaystyle-\int_{-1}^zU(y)\,dy,&z<0.
\end{cases}
```

Its value at zero can be assigned arbitrarily in the following integral. Is there **at most one** such $`U`$ satisfying

```math
\lim_{x\to\pm1,\ |x|<1}\frac{U(x)}{\sqrt{1-x^2}}=K,
\qquad
U(x)=K\sqrt{1-x^2}+\int_{-1}^1g(x,z)
\frac{zU(z)+\tfrac32\mathcal T_U(z)}{U(z)^3}\,dz
\quad(-1<x<1)?
```

All integrals are ordinary absolutely convergent Lebesgue integrals. Existence in this class follows from the construction in [1, Proposition 2.3 and §4.2]. The question fixes both the positive normalized toughness $`K`$ and the support; the injection rate is an output, rather than an additional prescribed parameter.

Equivalently, this is the normalized even cubic-mobility profile equation
$`U^3\partial_x I(U)=xU+\tfrac32\mathcal T_U`$ in distributions in the interior (classically away from the injection point), with $`I=-(-\partial_{xx})^{1/2}`$ on the whole line and zero opening outside the interval. The integral formulation specifies the solution class without requiring smoothness across the injection point.

## Application

This is the physical no-slip, plane-strain model of a fluid-driven crack in an impermeable elastic medium, without fluid lag. Positive toughness imposes the square-root opening at the two crack tips. After undoing the normalization, the profiles give a crack whose length grows like $`t^{2/3}`$ and opening like $`t^{1/3}`$ under constant injection. Uniqueness would make the predicted profile independent of the existence construction. The separate question of obtaining a profile for every prescribed toughness and injection rate is not included here.

## References

1. Cyril Imbert and Antoine Mellet, *Self-Similar Solutions for a Fractional Thin Film Equation Governing Hydraulic Fractures*, Communications in Mathematical Physics **340** (2015), 1187–1229. [Published article](https://doi.org/10.1007/s00220-015-2459-9); [author manuscript](https://www.math.umd.edu/~mellet/publi/selfsimilar.pdf); [arXiv:1403.7491v2](https://arxiv.org/abs/1403.7491v2). Remark 1.2(4), §2.2, equations (22), (26), (29), (64), and Proposition 2.3.
2. Matías G. Delgadino and Mary Vaughan, *Continuous symmetrizations and uniqueness of solutions to nonlocal equations*, Analysis & PDE **18** (2025), 2325–2366. [Published article](https://doi.org/10.2140/apde.2025.18.2325); [published PDF](https://msp.org/apde/2025/18-10/apde-v18-n10-p01-p.pdf). Equations (1-8)–(1-9) and Theorem 1.5 concern a different stationary problem.

## Status review


**Known cases:** The finite-toughness cubic-mobility half-Laplacian profile fixes support and toughness but not injection rate. Numerical profiles, zero-toughness asymptotics and uniqueness for a linear-mobility fractional model do not give uniqueness in this Green integral class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The finite-toughness cubic-mobility half-Laplacian profile fixes support and toughness but not injection rate. Numerical profiles, zero-toughness asymptotics and uniqueness for a linear-mobility fractional model do not give uniqueness in this Green integral class.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00220-015-2459-9); [comparison source 2](https://www.math.umd.edu/~mellet/publi/selfsimilar.pdf); [comparison source 3](https://arxiv.org/abs/1403.7491v2); [comparison source 4](https://doi.org/10.2140/apde.2025.18.2325); [comparison source 5](https://msp.org/apde/2025/18-10/apde-v18-n10-p01-p.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Imbert–Mellet explicitly leave similarity-profile uniqueness open for both zero and positive toughness in Remark 1.2(4). The present statement isolates the positive-toughness physical mobility exponent $`3`$ and spells out their Green integral equation, with the support normalized to $`[-1,1]`$. The actual final published remark, model, Green formula and integral equation were checked against the complete author manuscript.

Theorem 1.5 of [2] proves uniqueness for compactly supported Lipschitz stationary profiles of a linear-mobility rescaled equation with $`0<s<1/2`$. It does not cover this cubic-mobility, $`s=1/2`$, point-injection equation with square-root tips. Numerical and asymptotic hydraulic-fracture profiles do not alone establish uniqueness in the displayed integral class. Searches on 17 October 2026 found no matching resolution or announced counterexample; this remains a scoped literature assessment, with independent selected-primary review and the scoped catalogue comparison completed.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/hydraulic-finite-toughness-uniqueness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-hydraulic-finite-toughness-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/hydraulic-profile-duplicate-query-receipt.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/hydraulic-prove2me0139-review.json) and [coordinator review](../FURTHER_problems/_tracking/hydraulic-profile-coordinator-review-2026-10-17.json) record the exact hypotheses and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-519616fb7e5dcd38**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
