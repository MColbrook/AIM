# 862. A three-condition criterion for extremal toric Poincaré metrics

**Area:** Kähler geometry and geometric analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,L)`$ be a smooth compact polarized toric variety with labelled Delzant momentum polytope $`\Delta`$. A torus-invariant divisor $`Z`$ corresponds to selected facets $`F=\bigcup_i F_i`$.

For any induced labelled polytope pair $`(P,G)`$, define its extremal affine function $`s_{(P,G)}`$ by requiring
```math
\mathcal L_{(P,G)}(h)=
\int_{\partial P\setminus G}h\,d\nu
-\frac12\int_P h s_{(P,G)}\,d\mu
```

to vanish for every affine $`h`$. Call the pair stable if $`\mathcal L_{(P,G)}(h)>0`$ for every convex piecewise-affine $`h`$ that is not affine. Here $`d\mu`$ is lattice Lebesgue measure and $`d\nu`$ is the facet measure determined by the primitive labels, as in the source.

Put $`G_i=F_i\cap\bigcup_{j\ne i}F_j`$. Assume:

1. $`(\Delta,F)`$ is stable.
2. Every $`(F_i,G_i)`$ is stable, using its induced labels and measures.
3. On each selected facet,
   ```math
s_{(F_i,G_i)}-s_{(\Delta,F)}|_{F_i}=c_i>0
```

   for a constant $`c_i`$.

Must $`X\setminus Z`$ admit a torus-invariant extremal Kähler metric of Poincaré type in $`c_1(L)`$?

Use Definition 1.1 of the source for Poincaré type: near a divisor chart $`Z=\{z_1\cdots z_k=0\}`$, the metric is quasi-isometric to
```math
\sqrt{-1}\left(\sum_{j=1}^k
\frac{dz_j\wedge d\bar z_j}{|z_j|^2(\log|z_j|)^2}
+\sum_{j=k+1}^n dz_j\wedge d\bar z_j\right).
```

It has a potential relative to a smooth form in the class, with logarithm-of-logarithm growth and all derivatives of its differential bounded in the model metric. Extremal means that the $`(1,0)`$ gradient of scalar curvature is holomorphic.

## Application

The criterion would turn a geometric existence problem on a noncompact manifold with cusp ends into explicit stability tests on its momentum polytope and facets.

## References

1. V. Apostolov, H. Auvray and L. M. Sektnan, [*Extremal Kähler Poincaré type metrics on toric varieties*](https://arxiv.org/html/1711.08424), Definitions 1.1 and 3.1, Conjecture 4.12, Eq.(41), and Remark 4.13; *Journal of Geometric Analysis* **31** (2021), 1223–1290. [DOI](https://doi.org/10.1007/s12220-019-00263-7).
2. Y. Xu, [*The uniqueness of Poincaré type extremal Kähler metric*](https://arxiv.org/html/2504.08203), Theorem 1.1 (2025).
3. X. Chen and Y. Xu, [*Poincaré type J-equation*](https://arxiv.org/html/2605.01179), Theorem 1.1 (2026).

## Status review


**Known cases:** Hirzebruch-surface constructions establish cases, while Donaldson metrics can have different asymptotics. The Poincare extremal uniqueness theorem and J-equation solvability do not prove existence from all three stated stability and boundary-affine conditions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Hirzebruch-surface constructions establish cases, while Donaldson metrics can have different asymptotics. The Poincare extremal uniqueness theorem and J-equation solvability do not prove existence from all three stated stability and boundary-affine conditions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper proves special cases including Hirzebruch surfaces. Its complete Donaldson metrics need not have Poincaré asymptotics. Recent uniqueness and J-equation theorems do not prove this existence criterion. Only sufficiency is asked; necessity at general divisor crossings is separate.

The [coordinating review](../FURTHER_problems/_tracking/focused-C206-toric-and-Reznikov-two-precise-gates-C-20261028/ROOT-INDEPENDENT-THREE-MODEL-PRIMARY-CURRENT-AND-DUPLICATE-FINAL-REVIEW.json) records exact signs, normalization, independent model review, current searches and semantic duplicate checks. The official preprint supplies the statement; complete published-edition parity was not established. No matching general resolution or complete announcement was located.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f0a8502fe113b9f4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
