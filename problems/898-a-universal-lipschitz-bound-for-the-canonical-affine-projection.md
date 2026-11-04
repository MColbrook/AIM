# 898. A universal Lipschitz bound for the canonical affine projection

**Area:** Banach space geometry and convex geometric analysis
**Status:** ✅ SOLVED
**Last checked:** 2026-11-04

## Problem statement

For each positive integer $`n`$, let $`K\subset\mathbb R^n`$ be an origin-symmetric compact convex body with nonempty interior. Put $`K`$ in isotropic position: Lebesgue volume satisfies $`|K|=1`$, and there is a number $`L_K>0`$ such that
```math
\int_K z_i z_j\,dz=L_K^2\delta_{ij}\qquad(1\leq i,j\leq n).
```

Equip $`\mathbb R^n`$ with the norm
```math
\|v\|_K=\inf\{t>0:v\in tK\}.
```

For a real Lipschitz function $`f:K\to\mathbb R`$, write
```math
\mathrm{Lip}_K(f)=
\sup_{\substack{x,y\in K\\x\ne y}}
\frac{|f(x)-f(y)|}{\|x-y\|_K}.
```


The canonical orthogonal projection of $`f`$ in $`L^2(K)`$ onto the restrictions of affine functions is
```math
P_K f(x)=\int_K f(z)\,dz+
\frac{1}{L_K^2}\left\langle x,\int_K z f(z)\,dz\right\rangle .
```

The formula uses $`|K|=1`$ and the covariance normalization above.

**Is there a universal finite constant $`C`$, independent of $`n`$, $`K`$ and $`f`$, such that**
```math
\mathrm{Lip}_K(P_K f)\leq C\mathrm{Lip}_K(f)?
```


The operator $`P_K`$ is specified. Choosing a different affine approximant, or bounding its $`L^2`$ approximation error, would not answer the question.

## Application

Affine least-squares projection is a natural linear way to replace a nonlinear function by an affine one. The question asks whether this operation controls the largest local slope uniformly over all finite-dimensional normed geometries. It arose in quantitative differentiation, where one seeks affine approximations of Lipschitz maps on balls. A positive answer would provide this control directly for intrinsic norm balls.

## Known results and scope

For a Euclidean ball, the estimate holds with constant $`1`$, by the reflection argument in Hytönen–Li–Naor, Lemma 10 (p. 6 of the linked author version). The difficulty is a bound independent of the shape and dimension of a general norm ball.

The scalar formulation is equivalent to the version for maps into any nonzero real Banach space. Indeed, $`P_K`$ commutes with bounded linear functionals on the target; applying the scalar inequality to every norm-one functional bounds each pointwise difference of the vector-valued projection. Conversely, scalar functions embed along any fixed unit vector. This is the operator norm identity in the source's equation (28).

The heat-flow estimates of Hytönen–Naor avoid this projection issue by using different approximating operators. Bizeul–Klartag's later regression results control polynomial approximation and statistical error in $`L^2`$ for Euclidean Lipschitz data under log-concave measures. They do not state the pointwise Lipschitz operator bound above. The 2026 theorem on affine approximation in finite Nagata dimension chooses an atlas and has dimension-dependent constants; its affine approximants are also different from $`P_K`$.

## References

1. T. Hytönen and A. Naor, *Heat flow and quantitative differentiation*, J. Eur. Math. Soc. 21 (2019), 3415–3466, [DOI](https://doi.org/10.4171/JEMS/906). Eligible source: [arXiv:1608.01915v1](https://arxiv.org/pdf/1608.01915v1), isotropic normalization p. 8, Question 19 and equations (27)–(28) p. 15, and Section 5.A pp. 28–29. The [author's 2017 version](https://web.math.princeton.edu/~naor/homepage%20files/UAAP-heat-flow.pdf) also retains Question 19.
2. P. Bizeul and B. Klartag, *Entropy and Learning of Lipschitz Functions under Log-Concave Measures*, [arXiv:2509.10355v1](https://arxiv.org/pdf/2509.10355v1) (2025), Theorems 1.2 and 1.4, pp. 2–5.
3. M. Jung, C. Petitjean, A. Prochazka and A. Quilis, *Affine Approximation in Finite Nagata Dimension and Applications to Lipschitz-free spaces*, [arXiv:2606.11723v1](https://arxiv.org/html/2606.11723v1) (2026), Introduction, Theorem A and the definition of affine maps relative to an atlas.
4. T. Hytönen, S. Li and A. Naor, *Quantitative affine approximation for UMD targets*, Discrete Analysis 2016:6, [DOI](https://doi.org/10.19086/da.614). [Author version](https://web.math.princeton.edu/~naor/homepage%20files/Quant-UAAP-UMD.pdf), Lemma 10, p. 6. The publisher and author versions have different page counts; this locator refers to the 37-page author PDF.

- M. J. Colbrook, [*Affine Lipschitz projections on nearly Euclidean convex bodies*](../research/solutions/898-affine-lipschitz-projection/aim898.pdf), 3 November 2026. [TeX source](../research/solutions/898-affine-lipschitz-projection/aim898.tex), [package and reproduction](../research/solutions/898-affine-lipschitz-projection/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-operators-batch/898-review.md).

## Status review

**Outcome:** Counterexample.

**Resolution:** Canonical affine-projection norms diverge on explicit symmetric convex bodies, including examples whose Banach-Mazur distance to a Euclidean ball tends to one. The [manuscript](../research/solutions/898-affine-lipschitz-projection/aim898.pdf) and [individual audit](../research/solution_reviews/2026-11-03-operators-batch/898-review.md) give the complete proof, checked sources and exact target comparison. Review was performed by Codex (AI).

### Earlier literature review, 2026-10-30

The specified L2 orthogonal affine projection is essential. Heat-flow affine approximants, L2 statistical regression estimates and Nagata-atlas approximants are different operators or different norms. No dimension-independent Lipschitz bound for this canonical projection was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 2026-10-24 against the eligible question and definitions, the later author version, selected current primary statements and official version histories, targeted resolution and Prove2Me searches, and all-status AIM/FURTHER comparisons. No matching resolution or announcement was located. Selected primary passages were checked; this is not a certification of every cited proof or an exhaustive literature search.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-33c9d5b84ab1a814**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
