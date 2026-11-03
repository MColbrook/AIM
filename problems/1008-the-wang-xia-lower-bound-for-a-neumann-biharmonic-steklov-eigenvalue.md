# 1008. The Wang-Xia lower bound for a Neumann biharmonic Steklov eigenvalue

**Area:** Spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^n,g)`$, $`n\ge2`$, be a smooth connected compact Riemannian manifold with nonempty smooth boundary. Assume $`\mathrm{Ric}_g\ge0`$ and
```math
\mathrm{II}(X,X)\ge c\,|X|^2\qquad(X\in T\partial M)
```

for some $`c>0`$, where $`\mathrm{II}(X,X)=g(\nabla_X\nu,X)`$ uses the outward unit normal $`\nu`$. Let $`\lambda_1(\partial M)`$ be the first positive eigenvalue of $`-\Delta_{\partial M}`$ for the induced boundary metric.

With $`\Delta_g=\mathrm{div}_g\nabla_g`$, let $`\xi_1`$ be the first positive eigenvalue of
```math
\Delta_g^2u=0\quad\text{in }M,\qquad
\partial_\nu u=0,\quad\partial_\nu(\Delta_gu)+\xi u=0
\quad\text{on }\partial M.
```

Must
```math
\xi_1\ge\frac{n+2}{n-1}\,c\,\lambda_1(\partial M)
```

hold, with equality precisely for the Euclidean ball of radius $`1/c`$? No warped-product or sectional-curvature assumption is imposed.

## Application

The estimate would connect the response of a fourth-order boundary operator to boundary geometry and its intrinsic Laplace spectrum.

## References

1. Q. Wang and C. Xia, [*Sharp Lower Bounds for the First Eigenvalues of the Bi-Laplace Operator*](https://arxiv.org/abs/1802.05502), v5 (2020), equation (1.35) and the final conjecture, equation (3.58).
2. C. Xiong, [*On the Spectra of Three Steklov Eigenvalue Problems on Warped Product Manifolds*](https://doi.org/10.1007/s12220-022-00889-0), *Journal of Geometric Analysis* **32** (2022), article 153; [preprint](https://arxiv.org/abs/1902.00656), Conjecture 4 and Theorem 5.
3. Z. Lv, C. Xiong and Y. Zou, [*Scaling inequalities for Steklov eigenvalues in space forms and sharp eigenvalue estimates on warped product manifolds*](https://arxiv.org/abs/2512.22885), v1 (2025), Theorem 18 and Conjecture 21.

## Status review


**Known cases:** The arbitrary Ricci-nonnegative manifold with uniformly convex boundary is the target. The 2025 three-dimensional warped-product result and ordinary Steklov lower bounds do not establish this biharmonic assertion with rigidity.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The arbitrary Ricci-nonnegative manifold with uniformly convex boundary is the target. The 2025 three-dimensional warped-product result and ordinary Steklov lower bounds do not establish this biharmonic assertion with rigidity.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The warped-product case is known: the 2025 paper supplies the missing three-dimensional case and restates the arbitrary-manifold question as Conjecture 21. A weaker general lower bound is known. Results for ordinary Steklov, Dirichlet-type biharmonic Steklov, or interior buckling eigenvalues concern different operators.

For a Euclidean ball of radius $`r`$, the quantities are $`\xi_1=(n+2)/r^3`$, $`\lambda_1=(n-1)/r^2`$ and $`c=1/r`$, consistent with the proposed equality and scaling. No matching general proof, counterexample or complete-resolution announcement was located in bounded checks through the date above.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-045e3753c5c58e88**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
