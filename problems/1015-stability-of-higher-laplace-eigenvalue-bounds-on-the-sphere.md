# 1015. Stability of higher Laplace eigenvalue bounds on the sphere

**Area:** Spectral geometry and spectral optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`g_0`$ be the round metric of curvature one on $`S^2`$, with area measure $`dv_{g_0}`$ and total area $`4\pi`$. A nonzero finite positive Radon measure $`\mu`$ is **admissible** if the identity on smooth functions extends to a compact bounded operator
```math
W^{1,2}(S^2,g_0)\longrightarrow L^2(S^2,\mu).
```

Define its eigenvalues, counting multiplicities and starting with $`\lambda_0=0`$, by
```math
\lambda_k(S^2,\mu)=
\inf_{\substack{E\subset C^\infty(S^2;\mathbb R)\\
\dim E=\dim_{L^2(\mu)}E=k+1}}
\ \sup_{0\ne f\in E}
\frac{\int_{S^2}|\nabla f|_{g_0}^2\,dv_{g_0}}
     {\int_{S^2} f^2\,d\mu},
\qquad
\bar\lambda_k(S^2,\mu)=\lambda_k(S^2,\mu)\mu(S^2).
```

The equality of dimensions requires the image of $`E`$ in $`L^2(\mu)`$ to retain its dimension.

For every fixed integer $`k\ge3`$, is there a constant $`c_k>0`$, independent of $`\mu`$, such that every admissible measure satisfying $`\lambda_k(S^2,\mu)=2`$ admits a conformal automorphism $`\Phi:S^2\to S^2`$, distinct points $`p_1,\ldots,p_m`$, and positive integers $`\alpha_1,\ldots,\alpha_m`$, where
```math
1\le m\le k-1,\qquad \sum_{i=1}^m\alpha_i=k-1,
```

for which
```math
8\pi k-\bar\lambda_k(S^2,\mu)
\ \ge\
c_k\left\|
dv_{g_0}+\sum_{i=1}^m4\pi\alpha_i\delta_{p_i}-\Phi_*\mu
\right\|_{(C^1(S^2))^*}^{\,2}?
```

Here $`\delta_p`$ is unit point mass, $`\Phi_*\mu(A)=\mu(\Phi^{-1}(A))`$, and
```math
\|\nu\|_{(C^1)^*}
=\sup_{\|f\|_\infty+\|\nabla f\|_\infty\le1}
\left|\int_{S^2}f\,d\nu\right|.
```

An equivalent $`C^1`$ norm changes only the constant.

This is the remaining $`k\ge3`$ portion of Conjecture 1.7 in the 2021 preprint, renumbered Conjecture 1.8 in the accepted version. The case $`k=2`$ is already Theorem 1.7 of that version. The constant may depend on $`k`$; uniformity over all $`k`$ is not requested. Integer weights allow several bubbles to concentrate at the same point. The comparison measure may contain Dirac masses even though $`\mu`$ is admissible.

## Application

The estimate would quantify how spectral data close to the optimal higher eigenvalue bound constrain the geometry of a surface. It would identify, in a weak measure distance and after conformal reparametrization, the round component and concentrated bubbles arising in nearly optimal spectral metrics.

## References

- [Mikhail Karpukhin, Mickaël Nahon, Iosif Polterovich and Daniel Stern, *Stability of isoperimetric inequalities for Laplace eigenvalues on surfaces*, arXiv:2106.15043v1 (29 June 2021)](https://arxiv.org/abs/2106.15043v1), Section 1.2 and Conjecture 1.7.
- [Author accepted version, pp. 2–6](https://discovery.ucl.ac.uk/10205710/1/stability_submit_v2.pdf), definition (1.4), Theorem 1.7, Conjecture 1.8 and Remark 1.9. Published in *Journal of Differential Geometry* **129** (2025), no. 2, 415–490; [DOI 10.4310/jdg/1738163208](https://doi.org/10.4310/jdg/1738163208). The [institutional record](https://discovery.ucl.ac.uk/id/eprint/10205710/) identifies this PDF as the accepted manuscript.

- [Zuoqin Wang and Qingwei Zeng, *Improvements of Classical Eigenvalue Inequalities I: Quantitative Hersch-deficit and the Joint Spectral Range on the Two-Sphere*, arXiv:2609.32443v1 (26 September 2026)](https://arxiv.org/html/2609.32443v1), Theorems 1.1–1.4. These concern reciprocal-sum and low-eigenvalue deficits, rather than the higher-index bubbling estimate above.
- [Denis Vinokurov, *Maximizing higher eigenvalues in dimensions three and above*, arXiv:2506.09328v3 (30 July 2026)](https://arxiv.org/html/2506.09328v3), Theorem 1.1. Its source manifolds have dimension at least three.

## Status review


**Known cases:** The residual starts at k>=3 and asks quantitative distance to an integer-weighted bubble measure. Low-index Hersch deficits and higher-dimensional eigenvalue optimization do not establish this higher-index sphere stability.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The residual starts at k>=3 and asks quantitative distance to an integer-weighted bubble measure. Low-index Hersch deficits and higher-dimensional eigenvalue optimization do not establish this higher-index sphere stability.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The September 2026 Wang–Zeng estimates control a reciprocal-sum deficit near the single round measure; their geometric theorem does not give the integer-weight bubbling estimate for $`k\ge3`$. Vinokurov\'s higher-eigenvalue realization theorem applies in source dimension at least three, whereas the question here is on $`S^2`$.

The accepted manuscript retains the conjecture for general $`k`$, while establishing the case $`k=2`$. Its discussion explains why the $`W^{-1,2}`$ norm used for some first eigenvalue results cannot be substituted here: a Dirac mass does not belong to that dual space.

Current author publication lists and selected newer main statements were checked through 23 October 2026. The 2025 work on the second variation of Laplace eigenvalues concerns critical metrics and torus optimization; the October 2026 Morse-index paper treats particular free-boundary and closed minimal surfaces. The revised 2025 Dirichlet-spectrum stability paper concerns Euclidean domains with boundary and estimates relative to a ball. These statements do not establish the sphere-measure estimate above.

Searches covered the exact title, conjecture numbers in both versions, the authors, higher eigenvalue stability, bubbling, later proofs and counterexamples, and indexed Prove2Me results. The current OpenAI Math overview was also checked for relevant aliases. No matching complete resolution was located; these bounded checks do not prove that no solution exists.

An all-status AIM and FURTHER comparison returned buckling ratios, Steklov multiplicity and maximizer questions, feedback stabilization, and thermal insulation. Their complete matched statements concern different operators, domains or conclusions. No equivalent problem was identified among those records. The [dated audit](../FURTHER_problems/_tracking/sphere-eigenvalue-stability-independent-peer-2026-10-23.json) records the independent statement comparison, additional September 2026 result, final duplicate checks and source-access limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-23a295b582937de3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
