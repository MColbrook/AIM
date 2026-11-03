# 957. Full planar regularity of an optimal two-material interface at arbitrary contrast

**Area:** Free-boundary problems and optimal material design
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-03

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded connected open set, $`0<\alpha<\beta`$, $`0<V<|\Omega|`$, and $`u_0\in H^1(\Omega)`$. Among pairs $`(u,E)`$ with $`u-u_0\in H^1_0(\Omega)`$, $`E\subset\Omega`$ of finite perimeter, and $`|E|=V`$, minimize

```math
\mathcal F(u,E)=\int_\Omega\bigl(\alpha\mathbf 1_E+\beta\mathbf 1_{\Omega\setminus E}\bigr)|\nabla u|^2\,dx+P(E;\Omega).
```

Choose the canonical representative $`E^{(1)}`$ of points of density one, so that a change of $`E`$ on a null set cannot create an artificial topological singularity. **For every finite contrast $`\beta/\alpha>1`$, is $`\partial E^{(1)}\cap\Omega`$ locally a $`C^{1,\gamma}`$ curve for some $`\gamma>0`$?** Equivalently, can the singular part of the interior optimal interface always be ruled out in dimension two, without a contrast bound? A counterexample at some finite contrast would also settle the question negatively.

## Application

The perimeter term models the cost of the boundary between two conducting materials. Esposito–Fusco proved a small-contrast full-regularity result for the volume-constrained problem, but explicitly left larger contrast open. Lamberti–Lemenant subsequently proved full planar regularity when $`\beta<4\alpha`$, improving the earlier threshold, and gave a component-separation estimate at arbitrary contrast. Their published result explicitly describes unrestricted full regularity as an open question.

## References

1. L. Esposito and N. Fusco, [*A Remark on a Free Interface Problem with Volume Constraint*](https://journalofconvexanalysis.com/articles/jca18025/), *J. Convex Anal.* **18** (2011), no. 2, 417–426, especially introduction and final remark. [DOI](https://doi.org/10.68381/jca18025).
2. N. Fusco and V. Julin, [*On the regularity of critical and minimal sets of a free interface problem*](https://ems.press/journals/ifb/articles/13129), *Interfaces Free Bound.* **17** (2015), 117–142. Their partial-regularity result leaves full planar regularity open.
3. L. Lamberti and A. Lemenant, [*Quantitative Regularity Properties for the Optimal Design Problem*](https://doi.org/10.1007/s12220-026-02503-z), *J. Geom. Anal.* **36** (2026), article 261, Theorem 1.1. The [author full text](https://cvgmt.sns.it/media/doc/paper/7138/Optimal_Design_V2.pdf) states the exact functional and contrast bound.

## Status review


**Known cases:** The current quantitative theorem gives full planar regularity only for contrast strictly less than four, not all finite contrasts. No matching all-contrast theorem or counterexample found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current quantitative theorem gives full planar regularity only for contrast strictly less than four, not all finite contrasts. No matching all-contrast theorem or counterexample found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Targeted searches found no later all-contrast proof, counterexample, or public announcement. The 2026 theorem is partial progress, and the canonical representative avoids a null-set ambiguity. AIM and the admitted FURTHER list have no matching problem in the bounded semantic check. [Primary](../FURTHER_problems/_tracking/optimal-design-planar-full-regularity-primary-2026-10-20.json), [current-status](../FURTHER_problems/_tracking/optimal-design-planar-full-regularity-current-2026-10-20.json), [duplicate](../FURTHER_problems/_tracking/optimal-design-planar-full-regularity-duplicates-2026-10-20.json), and [decision](../FURTHER_problems/_tracking/optimal-design-planar-full-regularity-coordinator-2026-10-20.json) receipts record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dedab51c1ba79e9a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
