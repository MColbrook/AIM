# 778. The double-bubble conjecture in hyperbolic three-space

**Area:** Geometric analysis and interfacial energy
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb H^3`$ be complete simply connected hyperbolic three-space with sectional curvature $`-1`$. For every pair $`v,w>0`$, minimize
```math
P(E_1,E_2,E_0)=\tfrac12\bigl(\mathrm{Per}_g(E_1)+\mathrm{Per}_g(E_2)+\mathrm{Per}_g(E_0)\bigr)
```

over measurable partitions of $`\mathbb H^3`$, up to null sets, whose cells have finite perimeter and satisfy
```math
\mathrm{Vol}_g(E_1)=v,\qquad \mathrm{Vol}_g(E_2)=w,\qquad
E_0=\mathbb H^3\setminus(E_1\cup E_2).
```

Here perimeter is the total variation of the distributional derivative of the indicator with respect to the hyperbolic metric. Each interface is counted once. The competing cells need not be connected.

Prove or disprove that every minimizer is, up to null sets and an ambient hyperbolic isometry, the **standard double bubble** with these volumes. This configuration has two outer caps from geodesic spheres and an inner separating cap, all meeting along a common circle at $`120^\circ`$. The inner cap may lie on a geodesic sphere, an equidistant surface (a hyposphere), a horosphere or a totally geodesic plane. The standard configuration exists and is unique up to isometry for the prescribed volumes; its unrestricted global optimality is the question.

## Application

This is a basic test of how negative curvature changes the least interfacial energy required to separate two prescribed phases. It extends the classical soap-bubble perimeter problem to a non-Euclidean model space.

## References

1. J. Corneli, N. Hoffman, P. Holt, G. Lee, N. Leger, S. Moseley and E. Schoenfeld, *Double bubbles in S³ and H³*, Journal of Geometric Analysis **17** (2007), 189–212, [published article](https://doi.org/10.1007/BF02930720). The expanded [author version0811.3413v2](https://arxiv.org/abs/0811.3413v2), revised11December2008, gives the standard configuration in Lemma2.1, physicalp.5, and the volume-ratio result in Theorem6.4. The selected author passages were checked; complete published-body parity was not certified.
2. E. Milman, *Multi-Bubble Isoperimetric Problems*, Proceedings of the ICM2026, Vol.4, 678–697, [published survey](https://doi.org/10.1137/25M1804224); [latest author version2510.07078v2](https://arxiv.org/abs/2510.07078v2), revised31July2026. Sections2–3 define the competing clusters and standard bubbles; §9, problem(2), explicitly retains the hyperbolic double-bubble problem in dimension at least three.
3. E. Milman and J. Neeman, *The Structure of Isoperimetric Bubbles on Rⁿ and Sⁿ*, [2205.09102v4](https://arxiv.org/abs/2205.09102v4), revised20April2025, Theorem1.13. Its double-bubble theorem concerns Euclidean and spherical spaces.

## Status review


**Known cases:** The 2026 ICM primary survey retains the hyperbolic all-volume double-bubble question. Euclidean and spherical double-bubble classifications and the hyperbolic comparable-volume theorem do not cover every positive volume ratio.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 ICM primary survey retains the hyperbolic all-volume double-bubble question. Euclidean and spherical double-bubble classifications and the hyperbolic comparable-volume theorem do not cover every positive volume ratio.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/BF02930720); [comparison source 2](https://arxiv.org/abs/0811.3413v2); [comparison source 3](https://doi.org/10.1137/25M1804224); [comparison source 4](https://arxiv.org/abs/2510.07078v2); [comparison source 5](https://arxiv.org/abs/2205.09102v4). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reference[1] proves the conjecture when the smaller prescribed volume is at least85% of the larger. This is partial progress toward the all-volume target. The 2026 survey explicitly lists the general hyperbolic case as open. The Euclidean, spherical and Gaussian multi-bubble theorems have different ambient metrics; the spherical double-bubble case should not be presented as an additional open problem.

Current searches and the inspected AIM, OpenAI, FURTHER and cached website comparisons found no equivalent target or matching complete resolution announcement. AIM236 asks about four finite volumes in Euclidean three-space; this question concerns two finite volumes in hyperbolic three-space. The flat cubic-torus isoperimetric announcement also has a different metric and target.

The [primary scope review](../FURTHER_problems/_tracking/hyperbolic-double-bubble-primary-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/hyperbolic-double-bubble-current-review-2026-10-19.json), [duplicate comparisons](../FURTHER_problems/_tracking/hyperbolic-double-bubble-duplicates-review-2026-10-19.json), [website comparison](../FURTHER_problems/_tracking/hyperbolic-double-bubble-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/hyperbolic-double-bubble-coordinator-review-2026-10-19.json) record the bounded evidence. These checks do not certify that every possible resolution has been excluded or independently verify the complete cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2edfb33a7425b525**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
