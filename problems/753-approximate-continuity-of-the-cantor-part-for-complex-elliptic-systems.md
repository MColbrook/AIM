# 753. Approximate continuity of the Cantor part for complex-elliptic systems

**Area:** Geometric measure theory / continuum material models
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge2`$, let $`V,W`$ be nonzero finite-dimensional real inner-product spaces, and let $`A_1,\ldots,A_n:V\to W`$ be linear maps. Define

```math
\mathcal Au=\sum_{j=1}^n A_j\partial_j u,
\qquad \mathbb A(\xi)=\sum_{j=1}^n\xi_j A_j.
```

Assume that the complexified symbol $`\mathbb A(\xi):\mathbb C\otimes V\to\mathbb C\otimes W`$ is injective for every $`\xi\in\mathbb C^n\setminus\{0\}`$. Let $`B_1\subset\mathbb R^n`$ be the open unit ball, and suppose

```math
u\in BV^{\mathcal A}(B_1)
:=\{v\in L^1(B_1;V):\mathcal Av\in\mathcal M(B_1;W)\}.
```

Here $`\mathcal M`$ denotes finite vector-valued Radon measures. Let $`C_u`$ be the set of $`x\in B_1`$ at which some $`z\in V`$ satisfies

```math
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r(x)}|u(y)-z|\,dy=0,
\qquad S_u=B_1\setminus C_u.
```

Let $`J_u`$ consist of the $`x\in B_1`$ for which some $`a\ne b`$ in $`V`$ and $`\nu\in\mathbb S^{n-1}`$ satisfy

```math
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r^+(x,\nu)}|u(y)-a|\,dy=0,
\quad
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r^-(x,\nu)}|u(y)-b|\,dy=0,
```

where $`B_r^\pm(x,\nu)=\{y\in B_r(x):\pm(y-x)\cdot\nu>0\}`$. Must

```math
|\mathcal Au|(S_u\setminus J_u)=0
```

hold for every such choice of $`n,V,W,\mathcal A,u`$? The unit-ball formulation is local and is equivalent to the corresponding statement on arbitrary open domains. No one-dimensional slicing or mixing hypothesis is imposed beyond complex ellipticity.

## Application

The full gradient, symmetric gradient and, in dimension at least three, deviatoric symmetric gradient belong to this class. The question asks whether the diffuse singular part of a generalized strain can charge points where a displacement has neither a single approximate value nor a jump. This matters when defining local energies that depend on the displacement as well as on its strain.

## References

1. A. Arroyo-Rabasa and A. Skorobogatova, *A look into some of the fine properties of functions with bounded $`\mathscr A`$-variation*, ESAIM: Control, Optimisation and Calculus of Variations **31** (2025), article50, 30pp. Conjecture2.12, p.9; Definitions1.1–1.3 and2.1. [DOI](https://doi.org/10.1051/cocv/2025003), [published institutional copy](https://www.research-collection.ethz.ch/bitstreams/340e9307-a903-44e8-b0a8-956825697e37/download), [eligible preprint, latest v4](https://arxiv.org/abs/1911.08474v4), where the same statement is Conjecture4, p.9.
2. M. Caroccia and N. Van Goethem, *Rigidity and Functional Properties of $`\mathrm{BD}_{\mathrm{dev}}(\Omega)`$*, Archive for Rational Mechanics and Analysis **250** (2026), article61. §1.6, Conjecture1.5 and §7 distinguish quasi-continuity from approximate continuity in the deviatoric case. [Current published article](https://doi.org/10.1007/s00205-026-02210-7).
3. A. Arroyo-Rabasa, *Slicing and fine properties for functions with bounded $`\mathcal A`$-variation*, arXiv:2009.13513v2 (2020). Results under an additional one-dimensional mixing condition. [Preprint](https://arxiv.org/abs/2009.13513v2).

## Status review


**Known cases:** Complex ellipticity alone is required, without the additional mixing or one-dimensional slicing hypothesis. The 2026 deviatoric-strain paper explicitly distinguishes approximate quasi-continuity from the stronger approximate continuity; fixed-polar plane-wave decompositions do not supply it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Complex ellipticity alone is required, without the additional mixing or one-dimensional slicing hypothesis. The 2026 deviatoric-strain paper explicitly distinguishes approximate quasi-continuity from the stronger approximate continuity; fixed-polar plane-wave decompositions do not supply it.

Additional comparison sources: [comparison source 1](https://doi.org/10.1051/cocv/2025003); [comparison source 2](https://www.research-collection.ethz.ch/bitstreams/340e9307-a903-44e8-b0a8-956825697e37/download); [comparison source 3](https://arxiv.org/abs/1911.08474v4); [comparison source 4](https://doi.org/10.1007/s00205-026-02210-7); [comparison source 5](https://arxiv.org/abs/2009.13513v2); [comparison source 6](https://arxiv.org/abs/2606.12061v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check: 17 October 2026.** The exact target is Conjecture2.12 in the 2025 published paper and Conjecture4 in its eligible preprint. It is known for full and symmetric gradients and for operators admitting the stated one-dimensional slicing theory. Complex ellipticity alone does not imply that mixing hypothesis. The published 2026 deviatoric-strain paper still explicitly poses its corresponding special case for $`n\ge3`$ and identifies its quasi-continuity conclusion as weaker than approximate continuity.

The 2026 plane-wave announcement [arXiv:2606.12061v1](https://arxiv.org/abs/2606.12061v1) gives fixed-polar and tangent decompositions. Its stated jump-density results do not supply approximate continuity at the remaining diffuse-strain points. Neither Hausdorff absolute continuity of $`|\mathcal Au|`$ nor a scale-dependent best constant supplies the displayed conclusion. This differs from the BD conjecture that $`\mathcal H^{n-1}(S_u\setminus J_u)=0`$: that asks a stronger measure conclusion for a particular operator whose strain-measure conclusion here is already known.

No matching resolution was located in the checked primary announcements. The independent selected-primary audit and scoped catalogue comparison passed. Reading extents, version differences and capacity-notation caveats are retained in the review records.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/complex-elliptic-cantor-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-complex-elliptic-cantor-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/complex-elliptic-cantor-duplicate-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/complex-elliptic-cantor-prove2me0153-review.json) and [coordinator review](../FURTHER_problems/_tracking/complex-elliptic-cantor-coordinator-review-2026-10-17.json) record the checks and their limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0bec0e600d5e27ed**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
