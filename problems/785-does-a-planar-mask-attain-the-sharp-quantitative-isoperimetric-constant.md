# 785. Does a planar mask attain the sharp quantitative isoperimetric constant?

**Area:** Geometric analysis and shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a planar set $`E`$ of positive finite area and finite perimeter, let $`B`$ be a disk with $`|B|=|E|`$. Define its normalized isoperimetric deficit and Fraenkel asymmetry by
```math
\delta(E)=\frac{P(E)-P(B)}{P(B)},\qquad
 \lambda(E)=\min_{x\in\mathbb R^2}\frac{|E\mathbin\triangle (B+x)|}{|E|}.
```

The quotient $`F(E)=\delta(E)/\lambda(E)^2`$ is considered for sets that differ from every disk by positive area. Cicalese and Leonardi [1] conjecture that a *mask* is a global minimizer:
```math
\inf_{E\subset\mathbb R^2\!,\ E\text{ not a disk}}F(E)
 \stackrel{?}{=}
 \inf_{M\in\mathcal M_{\rm mask}}F(M).
```

Here $`\mathcal M_{\rm mask}`$ is the planar family described in [1] and [2, Section 5]: two perpendicular reflection axes, two optimal disks for $`\lambda`$, and boundary pieces forming eight circular arcs. Does this family contain an unrestricted optimizer, and hence yield the sharp constant in $`\lambda(E)^2\leq C\delta(E)`$? The frequently quoted ratio near $`0.39314`$ is a numerical candidate, not an exact proved global value.

## Application

Identifying the optimal shape would determine the best constant in a stability form of the planar isoperimetric inequality. This quantifies how perimeter excess controls a set's area-distance from the nearest disk and distinguishes unrestricted geometry from the known convex-case optimizer.

## Known results and scope

The existence of an unrestricted planar minimizer is known [2, Theorem 1.1]. The best convex-set ratio is attained by a stadium and is larger than the mask candidate [2, Introduction]. The 2015 paper proves qualitative properties and states symmetry and exactly two optimal disks as unproved steps toward mask identification [2, Section 5]. A 2025 paper proves results for a **different**, barycentric distance with a diameter bound while still referring to the Fraenkel-asymmetry mask as conjectured [3, Introduction].

## References

1. M. Cicalese and G. P. Leonardi, [*Best constants for the isoperimetric inequality in quantitative form*](https://arxiv.org/pdf/1101.0169v1), arXiv:1101.0169v1; *Journal of the European Mathematical Society* **15** (2013), 1101–1129. Introduction and the mask discussion around Figure 2 state the global conjecture.
2. C. Bianchini, G. Croce and A. Henrot, [*On the quantitative isoperimetric inequality in the plane*](https://arxiv.org/pdf/1507.08189), arXiv:1507.08189 (2015), Theorem 1.1 and Section 5, Conjecture 1 and Figure 7. The paper proves existence and gives the three-parameter mask description.
3. G. Croce and A. Henrot, [*Optimal sets for the quantitative isoperimetric inequality in the plane with the barycentric distance*](https://arxiv.org/pdf/2511.15232), arXiv:2511.15232 (2025), Introduction after Theorem 1.2. The different barycentric-distance theorem explicitly preserves the Fraenkel-mask conjecture as an open comparison.

## Status review


**Known cases:** The source concerns an unrestricted optimizer for the deficit divided by squared Fraenkel asymmetry. The primary 2025 quantitative-isoperimetry lecture still lists the mask conjecture; barycentric asymmetry, convex-only classes and existence of an optimizer do not identify it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source concerns an unrestricted optimizer for the deficit divided by squared Fraenkel asymmetry. The primary 2025 quantitative-isoperimetry lecture still lists the mask conjecture; barycentric asymmetry, convex-only classes and existence of an optimizer do not identify it.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1101.0169v1); [comparison source 2](https://arxiv.org/pdf/1507.08189); [comparison source 3](https://arxiv.org/pdf/2511.15232). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

No matching complete proof, counterexample or announced resolution of unrestricted Fraenkel-mask optimality was located in bounded searches through 21 October 2026. The 2015 existence theorem and 2025 barycentric-distance result do not identify the unrestricted minimizer. AIM and admitted FURTHER pages contain no equivalent target. These are bounded checks, not proof of exhaustive absence of a solution.

The [primary-source audit](../FURTHER_problems/_tracking/planar-isoperimetric-mask-primary-2026-10-21.json), [current-status audit](../FURTHER_problems/_tracking/planar-isoperimetric-mask-status-2026-10-21.json), and [duplicate/scope audit](../FURTHER_problems/_tracking/planar-isoperimetric-mask-duplicates-2026-10-21.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4a42d7c05d79981c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
