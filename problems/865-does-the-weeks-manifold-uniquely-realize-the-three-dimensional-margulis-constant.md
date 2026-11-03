# 865. Does the Weeks manifold uniquely realize the three-dimensional Margulis constant?

**Area:** Hyperbolic geometry and low-dimensional topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an orientable finite-volume hyperbolic 3-manifold $`M=\mathbb{H}^3/\Gamma`$, let $`\mu(M)`$ be the supremum of numbers $`\varepsilon`$ such that, whenever two elements of $`\Gamma`$ both move a point of $`\mathbb{H}^3`$ less than $`\varepsilon`$, they commute. Define the three-dimensional Margulis constant by

```math
\mu_3=\inf_{M}\mu(M),
```


where the infimum runs over all such $`M`$. Let $`W`$ be the Weeks manifold.

**Question.** Is $`\mu_3=\mu(W)=0.77442660700998\ldots`$? If so, is $`W`$ the **unique** manifold attaining this infimum, up to isometry?

## Application

The value controls the uniform thick–thin decomposition of hyperbolic 3-manifolds. An exact minimizer would make quantitative geometric bounds sharper and identify the extremal manifold.

## References

1. *K3: A New Problem List in Low-Dimensional Topology*, [author-approved preliminary PDF](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf), Chapter 3, Problem 3.23, printed pp. 146–147. The problem asks for the constant and uniqueness of the Weeks realization.
2. M. Goerner, R. C. Haraway III, N. R. Hoffman and M. Trnkova, [*Verified Length Spectrum and Margulis number for Hyperbolic 3-Manifolds*](https://arxiv.org/html/2609.26663v1), arXiv:2609.26663v1 (2026), Section 1.4, Theorem 1.2, Corollary 1.3, Conjecture 1.4 and Remark 1.5.
3. D. Futer, [*In search of the Margulis constant*](https://ems.press/content/serial-article-files/46997?nt=1), *Oberwolfach Reports* **20** (2023), 183–186, Conjecture 1 and Theorem 2. The symmetric case does not settle the full problem.

## Status review


**Known cases:** The September 2026 verified census calculation gives an upper bound for the universal Margulis constant and a minimum among selected censuses. Its global equality remains Conjecture 1.4; neither that calculation nor the symmetric-pair theorem proves global uniqueness of the Weeks realization.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September 2026 verified census calculation gives an upper bound for the universal Margulis constant and a minimum among selected censuses. Its global equality remains Conjecture 1.4; neither that calculation nor the symmetric-pair theorem proves global uniqueness of the Weeks realization.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 paper computes $`\mu(W)`$ and verifies its minimum in specified finite censuses, with one closed census manifold excluded for a technical reason. Its global conclusion is an **upper bound** for $`\mu_3`$, and it explicitly states equality as a conjecture. The book also asks for uniqueness, which is stronger. The 2023 symmetric-case theorem restricts the pairs of isometries and does not prove the unrestricted conjecture. Targeted later proof and announcement searches through 2026-10-21 found no global resolution. The [status and duplicate receipt](../FURTHER_problems/_tracking/margulis-weeks-constant-status-2026-10-21.json) records the bounded review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f71fd439084c903d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
