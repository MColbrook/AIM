# 754. No diffuse Cantor damage in cohesive fracture minimizers

**Area:** Fracture, damage and free-discontinuity problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^n`$ be bounded and Lipschitz, with $`n\ge2`$. Let $`F,G:[0,\infty)\to[0,\infty)`$ be continuously differentiable and increasing. Assume:

- $`F`$ is strictly convex and superlinear, with $`F(0)=F'(0)=0`$.
- $`G`$ is strictly concave, $`G(0)=0`$, and $`\sigma:=G'(0)>0`$.
- The following limit exists, possibly as minus infinity, and is negative:

```math
\lim_{s\downarrow0}\frac{G(s)-\sigma s}{s^2}<0.
```

Let $`e_M>0`$ be the unique solution of $`F'(e_M)=\sigma`$ and define

```math
\overline F(t)=
\begin{cases}
 F(t),&0\le t\le e_M,\\
 F(e_M)+\sigma(t-e_M),&t>e_M.
\end{cases}
```

For a scalar function $`u\in BV(\Omega)`$, write its distributional derivative as

```math
Du=\nabla u\,\mathcal L^n+[u]\nu_u\,
\mathcal H^{n-1}\!\restriction J_u+D^c u.
```

Here $`\nabla u`$ is the approximate gradient, $`J_u`$ its jump set, $`[u]`$ the difference of its one-sided traces and $`D^c u`$ its Cantor derivative. Consider

```math
\mathcal E(u)=\int_\Omega\overline F(|\nabla u|)\,dx
 +\int_{J_u}G(|[u]|)\,d\mathcal H^{n-1}
 +\sigma|D^c u|(\Omega).
```

Suppose $`\mathcal E(u)<\infty`$ and $`u`$ is a **local minimizer in the BV norm**: for some $`\eta>0`$, $`\mathcal E(u)\le\mathcal E(v)`$ whenever $`v\in BV(\Omega)`$, $`\mathrm{supp}(v-u)\Subset\Omega`$ and

```math
\|v-u\|_{BV}:=\|v-u\|_{L^1}+|D(v-u)|(\Omega)<\eta.
```

Must every such minimizer satisfy

```math
|D^c u|(\Omega)=0,\qquad |\nabla u|\le e_M\quad\text{almost everywhere}?
```

Thus the proposed assertion is membership in $`SBV(\Omega)`$ together with the yield-strain bound. No smoothness away from a prescribed crack is assumed. For example, the admissible pair $`F(t)=t^2/2`$, $`G(t)=1-e^{-t}`$ has $`\sigma=e_M=1`$.

## Application

This scalar energy models antiplane cohesive fracture. The Cantor term permits diffuse damage in the relaxed energy. Its absence at local minima would support a description by elastic strain and rectifiable cracks, with a maximum sustainable strain.

## References

1. G. Dal Maso and A. Garroni, *Gradient bounds for minimizers of free discontinuity problems related to cohesive zone models in fracture mechanics*, Calculus of Variations and Partial Differential Equations **31** (2008), 137–145. [DOI](https://doi.org/10.1007/s00526-006-0084-3); [author preprint](https://arxiv.org/abs/math/0507088), introduction equations (4)–(5), assumptions (a)–(b), equation (7) and Theorem 1.
2. B. Bourdin, G. A. Francfort and J.-J. Marigo, *The Variational Approach to Fracture*, Springer, 2008, §2.6, equation (2.30) and subsequent discussion. [Book DOI](https://doi.org/10.1007/978-1-4020-6395-4); [author manuscript](https://hal.science/hal-00551079/document). Also published in Journal of Elasticity **91** (2008), 5–148, [article DOI](https://doi.org/10.1007/s10659-007-9107-3); these are versions of one work.
3. V. Crismale and M. Friedrich, [*Quasistatic evolution of cohesive-type fracture*](https://arxiv.org/abs/2607.02261v1), 2026, §1, discussion of finite initial slope and the distinction from positive activation energy.

## Status review


**Known cases:** The target is every BV-norm local minimizer of this scalar cohesive energy, with finite initial surface slope and no activation gap. General Gamma-limits containing Cantor terms do not prove that minimizers have nonzero Cantor damage. One-dimensional and already-C1 results remain special cases.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is every BV-norm local minimizer of this scalar cohesive energy, with finite initial surface slope and no activation gap. General Gamma-limits containing Cantor terms do not prove that minimizers have nonzero Cantor damage. One-dimensional and already-C1 results remain special cases.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00526-006-0084-3); [comparison source 2](https://arxiv.org/abs/math/0507088); [comparison source 3](https://doi.org/10.1007/978-1-4020-6395-4); [comparison source 4](https://hal.science/hal-00551079/document); [comparison source 5](https://doi.org/10.1007/s10659-007-9107-3); [comparison source 6](https://arxiv.org/abs/2607.02261v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The one-dimensional conclusion is known. Reference 1 proves the gradient bound where a local minimizer is continuously differentiable. Assuming that regularity does not establish the assertion for arbitrary BV minimizers.

Reference 3 still describes higher-dimensional SBV regularity for zero activation and finite initial slope as unavailable. Its new evolution theorem assumes positive activation energy, which changes the model. General statements that cohesive energies can permit Cantor damage do not provide a minimizing counterexample under the hypotheses above.

Dated searches, the AIM collection across all statuses, the OpenAI announcement index and all 186 Prove2Me listing pages were compared. No equivalent problem or matching active complete-solution announcement was located. The vectorial Griffith weak-fourth-power problem concerns a different energy and target.

The [review packet](../FURTHER_problems/_tracking/parallel/continuum/cohesive-cantor-regularity-review.json) and [catalogue comparison](../FURTHER_problems/_tracking/prove2me-catalogue-review.json) record exact reading extents and limits. This is a bounded literature review, not a guarantee that no solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-19410d24fd493bfe**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
