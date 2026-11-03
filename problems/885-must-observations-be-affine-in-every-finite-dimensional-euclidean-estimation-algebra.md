# 885. Must observations be affine in every finite-dimensional Euclidean estimation algebra?

**Area:** Nonlinear filtering and data assimilation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n,m\ge1`$, and let $`f:\mathbb R^n\to\mathbb R^n`$ and $`h=(h_1,\ldots,h_m):\mathbb R^n\to\mathbb R^m`$ be real smooth functions. On the real vector space $`C^\infty(\mathbb R^n;\mathbb R)`$ define

```math
L_0\varphi=\frac12\Delta\varphi
-\sum_{i=1}^n f_i\partial_i\varphi
-(\mathrm{div}f)\varphi
-\frac12\sum_{j=1}^m h_j^2\varphi,
\qquad M_{h_j}\varphi=h_j\varphi.
```

Let $`E`$ be the smallest real vector space of differential operators containing $`L_0,M_{h_1},\ldots,M_{h_m}`$ and closed under $`[A,B]=AB-BA`$.

**If $`E`$ is finite-dimensional over $`\mathbb R`$, must every $`h_j`$ be affine on $`\mathbb R^n`$?** Equivalently, must $`h_j(x)=a_j\cdot x+b_j`$ for constant $`a_j\in\mathbb R^n`$ and $`b_j\in\mathbb R`$?

This is the weak Mitter conjecture in the smooth Euclidean identity-diffusion setting. No rank, observability, gradient-drift, polynomial-coefficient or constant-Wong-matrix condition is imposed. The question concerns these global differential operators; it does not additionally assert global nonexplosion for every associated stochastic system.

## Application

For a hidden diffusion $`dX_t=f(X_t)dt+dB_t`$ observed through $`dY_t=h(X_t)dt+dW_t`$, with independent Brownian noises, $`L_0`$ is the Stratonovich Zakai density operator. Its Lie algebra is a central object in constructing exact finite-dimensional nonlinear filters. The conjecture would constrain which observation laws are compatible with this algebraic reduction; it is not a claim classifying every possible finite-dimensional filtering representation.

## References

1. Xiaopei Jiao, Jiayi Kang and Ji Shi, [*Finite-dimensional filter with non-maximal rank*](https://bimsa.net/doc/publication/15097.pdf), Communications in Information and Systems25(4),757–785, header2025, DOI [10.4310/CIS.260128101407](https://doi.org/10.4310/CIS.260128101407). Conjecture4.1, printed770; model and definitions, printed760–763. DOI-associated2026 metadata and publisher-copy parity remain separately recorded.
2. Xiaopei Jiao and Stephen Shing-Toung Yau, [*Weak Form Mitter Conjecture on Nonmaximal Rank Estimation Algebra: State Dimension4 and Rank3*](https://jag.math.tsinghua.edu.cn/Publications/Control/466.pdf), Journal of Systems Science and Complexity38(1)(2025),27–78, [DOI](https://doi.org/10.1007/s11424-025-4138-z), Theorems4.5 and5.20.
3. Jie Chen and Stephen S. T. Yau, [*Finite-Dimensional Filters with Nonlinear Drift VII: Mitter Conjecture and Structure of eta*](https://doi.org/10.1137/S0363012994272836), SIAM Journal on Control and Optimization,1997; official abstract specifies maximal rank.
4. Jiayi Kang, Andrew Salmon and Stephen Shing-Toung Yau, [*Nonexistence of finite-dimensional estimation algebras on closed smooth manifolds*](https://arxiv.org/html/2410.08689v1), MainTheorems1–2,2024.

## Status review


**Known cases:** Ocone gives quadratic multiplication functions, not affine observations. Maximal-rank and dimension-four rank-three results add rank assumptions; compact-manifold nonexistence does not cover arbitrary Euclidean observations. No full weak-Mitter result under these general hypotheses was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Ocone gives quadratic multiplication functions, not affine observations. Maximal-rank and dimension-four rank-three results add rank assumptions; compact-manifold nonexistence does not cover arbitrary Euclidean observations. No full weak-Mitter result under these general hypotheses was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Source[1] explicitly states the weak conjecture. Its recalled Ocone theorem gives degree at most two for multiplication functions in $`E`$, which does not establish affine observations. The stronger assertion that every multiplication function in $`E`$ is affine is separately conjectural.

Known results include maximal rank[3] and state dimension4 with linear rank3[2]. The sufficient partial-Wong-matrix theorem in[2] also retains rank $`n-1`$. Shorthand about dimension4 in introductory prose must be read with the actual theorem's rank hypothesis. Novel filters with nonpolynomial Wong matrices in[1] still use affine observations.

The closed-manifold theorem[4] assumes compactness without boundary. Its noncompact extension requires two distinct critical points joined by a gradient trajectory; it does not cover every smooth Euclidean observation. These results do not establish the unrestricted implication displayed above.

No matching full resolution was located in the recorded bounded searches. The [full pinned-source review](../FURTHER_problems/_tracking/parallel/rough-filtering/jiao2026-nonmaximal-full-review.json), [model/current review](../FURTHER_problems/_tracking/parallel/rough-filtering/weak-mitter-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-weak-mitter-review.json), [semantic comparison](../FURTHER_problems/_tracking/weak-mitter-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/weak-mitter-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/weak-mitter-coordinator-review-2026-10-19.json) document their extent and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-5b9b6e16dabcf96e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
