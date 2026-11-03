# 971. Three-fold complete mixability of a planar convex body's uniform law

**Area:** Probability, coupling and convex geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`C\subset\mathbb R^2`$ be any compact convex set with nonempty interior. Write $`U_C`$ for its uniform probability law and $`b_C`$ for its centroid:

```math
U_C(A)=\frac{|A\cap C|}{|C|},\qquad
b_C=\frac1{|C|}\int_C x\,dx.
```

Here $`|\cdot|`$ denotes planar Lebesgue area. Does there always exist a Borel probability measure $`H`$ on $`C^3`$ with all three coordinate marginals equal to $`U_C`$ and

```math
H\{(x_1,x_2,x_3):x_1+x_2+x_3=3b_C\}=1?
```

Equivalently, can three dependent points, each uniform on $`C`$, always have an exactly constant sum? The value of that sum is forced by taking expectations. No independence, deterministic transport, boundary smoothness or symmetry is required.

This is the planar, three-fold case of Wang's Open Problem 5. The source asks the broader question in every dimension $`d`$, with every number of points $`n\ge d+1`$. This entry does not assert that the planar three-fold case is equivalent to that entire programme.

## Application

Constant-sum couplings express an extreme form of negative dependence, useful in variance reduction and risk aggregation. For this geometric question, three individually uniform samples would have a sample mean exactly equal to the body's centroid.

## References

1. Ruodu Wang, [*Current open questions in complete mixability*](https://arxiv.org/abs/1411.6190v3), Definitions 1–3 and Section 2.5, Open Problem 5, physical pp. 3–4 and 16–17 of the inspected 24-page version. Published in Probability Surveys **12** (2015), 13–32, [DOI 10.1214/14-PS250](https://doi.org/10.1214/14-PS250). Final-edition body parity remains pending; the served arXiv version's header and internal date differ, as recorded in the source review.
2. Ruodu Wang, [author's working-paper guide to joint mixability and negative dependence](https://www.math.uwaterloo.ca/~wang/pages/WPS3.html), especially WP08 and the later results on other questions in the survey.
3. Peter Keevash and Jeck Lim, [*On the largest sum-free subset of the lattice cube*](https://arxiv.org/html/2605.00816v1), Definitions 1.2–1.3 and Theorem 1.5 (2026). This comparison concerns uniform measures on cube slices.
4. Andrzej Komisarski and Jacques Labuschagne, [*The Distributions of the Mean of Random Vectors with Fixed Marginal Distribution*](https://doi.org/10.1007/s10959-023-01277-2), abstract and Theorem 1. This comparison constructs a common marginal rather than prescribing the uniform law of an arbitrary convex body.

## Status review


**Known cases:** A prescribed uniform law on an arbitrary planar convex body must admit three marginals with constant vector sum. Scalar mixability and cube-slice or constructed-marginal results do not establish this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A prescribed uniform law on an arbitrary planar convex body must admit three marginals with constant vector sum. Scalar mixability and cube-slice or constructed-marginal results do not establish this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

No matching complete resolution or announced solution was located in the recorded bounded checks. Triangles have an elementary construction: cyclically permute a uniform point's barycentric coordinates. Disks have a construction using rotations by $`120`$ degrees; affine transformations give ellipses.

The source observes that each one-dimensional projection of a planar convex body's uniform law has a concave density and can be mixed separately. Those separate couplings need not come from a compatible joint law of planar points. A generic triangulation also produces different triangle centroids, so combining its couplings does not automatically give the required constant sum.

The newer cube-slice coupling result applies to a particular family of measures, often with distinct marginals. The result allowing averages to have arbitrary distributions chooses its common marginal. Neither inspected statement proves the displayed assertion for a prescribed arbitrary $`U_C`$.

The [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/planar-convex-uniform-three-mixability-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-planar-convex-three-mixability-review.json), [current comparisons](../FURTHER_problems/_tracking/convex-body-mixability-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/convex-body-mixability-duplicates-review-2026-10-19.json), [split catalogue review](../FURTHER_problems/_tracking/convex-body-mixability-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/convex-body-mixability-coordinator-review-2026-10-19.json) record the checks and their limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-277fb00b925fc5fd**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
