# 1034. The sharp curvature Schrödinger inequality for closed loops

**Area:** Spectral geometry and elastic loops
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-03

## Problem statement

Let $`\gamma:\mathbb R/(2\pi\mathbb Z)\to\mathbb R^3`$ be any smooth unit-speed closed curve, so $`|\gamma'(s)|=1`$, and define its curvature by $`\kappa(s)=|\gamma''(s)|`$. Self-intersections are allowed; planarity and convexity are not assumed.

Prove or disprove that every $`f\in H^1_{\mathrm{per}}(0,2\pi)`$ satisfies
```math
\int_0^{2\pi}\bigl(|f'(s)|^2+\kappa(s)^2|f(s)|^2\bigr)\,ds
\geq \int_0^{2\pi}|f(s)|^2\,ds.
```

Equivalently, the least eigenvalue of
```math
H_\gamma=-\frac{d^2}{ds^2}+\kappa(s)^2
```

with periodic boundary conditions should be at least $`1`$. The unit circle and a known family of noncircular ovals attain $`1`$. The question asks for the universal bound, without adding an equality-classification requirement.

## Application

This operator arises when determining the tension in a dynamical elastic loop. The inequality would provide a sharp uniform coercivity estimate for that operator over closed curves of fixed length. The curvature potential here has a positive sign.

## References

1. Almut Burchard and Lawrence E. Thomas, *On an isoperimetric inequality for a Schrödinger operator depending on the curvature of a loop*, Journal of Geometric Analysis **15** (2005),543–563, [published article](https://doi.org/10.1007/BF02922244); [author versionmath/0505123v1](https://arxiv.org/abs/math/0505123v1), Introduction, equation1.1 and Theorem1.1, physical pp.1–4.
2. Helmut Linde, *An improved bound for the ground state of a Schrödinger operator on a loop*, [arXiv:2504.20229v2](https://arxiv.org/abs/2504.20229v2),24May2025, Introduction and Theorems2.1–2.2.
3. Durvudkhan Suragan, *An Improved Bound for the Ovals Problem*, [arXiv:2609.10775v1](https://arxiv.org/abs/2609.10775v1),9September2026, Introduction, Theorem1.1, Corollary1.2 and the endpoint-condition discussion in §5/AppendixA.
4. OpenAI, *Sharp one-dimensional Lieb–Thirring constants*, [announced preprint](https://github.com/openai/math/blob/main/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf),23September2026, Theorem1.1.
5. M. J. Colbrook, [*A certified lower bound for the ovals problem*](../research/solutions/1034-ovals-certified-lower-bound/aim1034.pdf), 3 November 2026. [TeX source](../research/solutions/1034-ovals-certified-lower-bound/aim1034.tex), [package and reproduction](../research/solutions/1034-ovals-certified-lower-bound/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-spectral-batch/1034-review.md).

## Status review

**Known cases:** The circle and the known oval family attain one. The new universal bound is $`\lambda_1(H_\gamma)\ge C_0>0.96221`$ for the full smooth closed spatial-curve class, with a reproducible outward-rounded certificate. Thus $`C_0\le\inf_\gamma\lambda_1(H_\gamma)\le1`$.

**Remaining target:** Raise the universal lower bound to one for every smooth closed spatial curve of length $`2\pi`$, or construct a counterexample. No optimality claim is made for the new bound.

**Reviewed result, 2026-11-03:** A certified universal lower bound greater than 0.96221 holds for the curvature operator on the full smooth closed-curve class. The [manuscript](../research/solutions/1034-ovals-certified-lower-bound/aim1034.pdf) and [individual audit](../research/solution_reviews/2026-11-03-spectral-batch/1034-review.md) record the proof, checked references and exact target comparison. Review was performed by Codex (AI).

### Earlier status check, 2026-10-30

The earlier review concerned the conjectured constant one for all smooth closed spatial curves, with no convexity restriction. The September 2026 near-sharp estimate remains below one; planar convex verification notebooks and one-dimensional Lieb-Thirring constants do not prove this full geometric assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Burchard–Thomas prove local minimality of the oval family rather than the full global assertion. Linde improves the analytic lower bound to $`0.81`$. Suragan announces the stronger bound
```math
\lambda_1(H_\gamma)\geq\frac{\sqrt\pi}{2}
\left(\frac{\Gamma(7/6)}{\Gamma(5/3)}\right)^3<1,
```

which still leaves a gap to the conjectured value.

The announced sharp Lieb–Thirring theorem concerns a related real-line spectral inequality. The inspected cumulative-density reduction imposes zero endpoint values, whereas a smooth loop has a positive periodic ground-state amplitude. Thus that theorem does not automatically establish the present periodic inequality. This distinction was independently checked; neither announcement's complete proof was certified here.

No matching complete resolution or equivalent AIM/FURTHER entry was located in the bounded searches and comparisons. The [coordinator review](../FURTHER_problems/_tracking/benguria-loss-coordinator-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/benguria-loss-current-review-2026-10-19.json), [duplicate review](../FURTHER_problems/_tracking/benguria-loss-duplicates-review-2026-10-19.json) and [independent scope audit](../FURTHER_problems/_tracking/parallel/continuum/benguria-loss-loop-independent-scope-audit-2026-10-19.json) record exact reading extents and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f883c76cd5abf98d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
