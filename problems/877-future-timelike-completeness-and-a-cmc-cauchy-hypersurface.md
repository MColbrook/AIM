# 877. Future timelike completeness and a CMC Cauchy hypersurface

**Area:** Mathematical relativity and Lorentzian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge4`$ and let $`(M^d,g)`$ be a connected, smooth, time-oriented Lorentzian manifold without boundary, with signature $`(-,+,\ldots,+)`$. Assume that:

- $`M`$ is globally hyperbolic and has a compact Cauchy hypersurface. A Cauchy hypersurface meets every inextendible causal curve exactly once.
- $`\mathrm{Ric}_g(X,X)\ge0`$ for every timelike tangent vector $`X`$ (the strong energy condition).
- Every future-inextendible timelike geodesic has infinite future proper-time length.

Must $`M`$ contain a compact smooth spacelike Cauchy hypersurface $`S`$ with constant mean curvature?

Here the mean curvature is $`H=\mathrm{tr}_hK`$, where $`h`$ is the induced Riemannian metric and $`K(X,Y)=g(\nabla_X\nu,Y)`$ for the future-directed unit normal $`\nu`$. No past geodesic completeness or sign condition on an initial hypersurface is assumed. This is Conjecture 2 of [1], within its standing spacetime dimensions.

## Application

Constant-mean-curvature (CMC) initial data simplify the Einstein constraint equations and provide useful gauges for their evolution. The question asks whether future completeness and the focusing condition alone ensure such a global slice in spatially closed cosmological models [1, 2].

## References

1. G. J. Galloway, [*Existence of CMC Cauchy surfaces and spacetime splitting*](https://math.miami.edu/~galloway/papers/CMCBart.pdf), *Pure and Applied Mathematics Quarterly* **15**(2) (2019), 667–682, [DOI](https://doi.org/10.4310/pamq.2019.v15.n2.a2). Conjecture 2, p. 675; definitions, pp. 669–670.
2. G. J. Galloway and E. Ling, [*A CMC existence result for expanding cosmological spacetimes*](https://arxiv.org/abs/2410.16619v3), arXiv:2410.16619v3 (15 February 2026). Conjecture 2 and Theorem 3. The authors state that this revision agrees with the published version; the separate final journal body was not independently obtained.
3. E. Ling and A. Ohanyan, [*Examples of cosmological spacetimes without CMC Cauchy surfaces*](https://doi.org/10.1007/s11005-024-01843-7), *Letters in Mathematical Physics* **114** (2024), 96. Conjecture 1.4 and Theorem 4.3.
4. E. Minguzzi, [*Bartnik's splitting conjecture and the cosmological wall: a Cauchy Busemann function approach*](https://arxiv.org/abs/2610.17092v1), arXiv:2610.17092v1 (12 October 2026). Introduction, especially the completeness assumptions in Section 1.4.

## Status review


**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The CMC theorem for an initially nonnegatively expanding Cauchy slice adds a sign hypothesis absent from the future-complete conjecture. The timelike-sectional-curvature and conditional Busemann results are also restricted. The announced June Bartnik proof is still withdrawn, and would in any case need comparison with the stronger future-only CMC target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known cases:** Existence follows under nonpositive timelike sectional curvature [1, Theorem 11]. The newer result [2, Theorem 3] assumes an additional smooth spacelike Cauchy hypersurface with $`H\ge0`$. The question asks for existence without that initial sign condition.

**Related conjecture:** Bartnik's cosmological splitting conjecture assumes completeness in both time directions and asks for a global static product. The future-only CMC conjecture above would imply Bartnik's conjecture in the same spacetime dimensions $`d\ge4`$, but drops its past-completeness assumption. A spacetime that is complete only to the future need not be a product with the whole real time axis [4, Section 1.4].

**Recent comparisons:** The constructions in [3] have no CMC Cauchy hypersurface but do not satisfy the universal future-completeness hypothesis. The conditional Busemann and splitting results in [4] do not establish this target. The June 2026 announced Bartnik proof, [arXiv:2606.03873v3](https://arxiv.org/abs/2606.03873v3), was explicitly withdrawn by its authors.

**Review:** Independent selected-primary review passed. The dated review packet records the all-status catalogue comparison and the remaining separate final-journal parity limit.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/future-cmc-existence-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-future-cmc-existence-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/future-cmc-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/future-cmc-prove2-0150-review.json) and [coordinator review](../FURTHER_problems/_tracking/future-cmc-coordinator-review-2026-10-17.json) record the checked scope.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-660e024dc5e82e0f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
