# 784. Interior volume in the conformal orbit of a free boundary minimal submanifold

**Area:** Minimal submanifolds and conformal geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every pair of integers $`2\le k<n`$, let $`\Sigma`$ be a compact connected smooth $`k`$-manifold with nonempty boundary, and let $`X:\Sigma\to\overline{B^n}`$ be a smooth immersion. Write $`g=X^*g_{\mathrm E}`$ for its induced Euclidean metric, and assume
```math
X^{-1}(S^{n-1})=\partial\Sigma,\qquad
\Delta_gX=0,\qquad dX(\eta)=X\quad\text{on }\partial\Sigma,
```

where $`\eta`$ is the outward unit conormal. Thus $`X`$ is a free boundary minimal immersion into the Euclidean unit ball.

For every conformal diffeomorphism $`f:\overline{B^n}\to\overline{B^n}`$, is
```math
\mathrm{Vol}_{k}\bigl(\Sigma,(f\circ X)^*g_{\mathrm E}\bigr)
\le \mathrm{Vol}_{k}(\Sigma,g)?
```

Volumes are computed on the parameter manifold, counting immersion multiplicity. No embeddedness, orientability, topology, or spectral assumption is added.

Equivalently, does every $`y\in\mathbb R^n`$ with $`|y|>1`$ satisfy
```math
\int_\Sigma\left(\frac{|y|^2-1}{|X-y|^2}\right)^k dV_g
\le \int_\Sigma dV_g?
```

This is the nontrivial dimension range of Fraser–Schoen's Question 3.2 (2013), repeated as Open Question 8 on page 24 of Li's survey arXiv:1907.05053v3. Ko–Shao's latest version of *Free boundary minimal annuli in convex balls* (2026), Section 1.2.1, still identifies the corresponding surface-area question as open. The known decrease of boundary length for two-dimensional free boundary minimal surfaces concerns a different quantity.

## Application

Conformal families are used to construct minimal surfaces by variational methods. A sharp volume bound along these families would connect free-boundary geometry with conformal comparison and min–max constructions.

## References

1. Ailana Fraser and Richard Schoen, *Minimal surfaces and eigenvalue problems*, Contemporary Mathematics **599** (2013), 105–121. [Author version](https://arxiv.org/abs/1304.0851v1), Questions 3.2 and 3.9.
2. Martin Man-Chun Li, *Free boundary minimal surfaces in the unit ball: recent advances and open questions*. [Latest author version](https://arxiv.org/abs/1907.05053v3), 2 July 2020, Open Question 8, physical pp.24–26.
3. Dongyeong Ko and Guanhua Shao, *Free boundary minimal annuli in convex balls*. [Latest v2](https://arxiv.org/abs/2608.14679v2), 22 August 2026, §1.2.1, equations (5)–(6) and adjoining discussion.
4. Jonathan J. Zhu, *Free boundary and capillary minimal surfaces in spherical caps II: Low energy*. [Inspected HTML](https://arxiv.org/html/2512.20857v1), Introduction §1.1 and Remarks 5.9–5.10. Its official submission date and served HTML internal date differ; the scoped review records this without asserting PDF/HTML identity.

## Status review


**Known cases:** The desired sharp inequality concerns interior k-volume with immersion multiplicity. Boundary-volume decrease, its second variation and the coarse Willmore comparison do not imply it, since a conformal image need not remain minimal.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The desired sharp inequality concerns interior k-volume with immersion multiplicity. Boundary-volume decrease, its second variation and the coarse Willmore comparison do not imply it, since a conformal image need not remain minimal.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1304.0851v1); [comparison source 2](https://arxiv.org/abs/1907.05053v3); [comparison source 3](https://arxiv.org/abs/2608.14679v2); [comparison source 4](https://arxiv.org/html/2512.20857v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Ko–Shao explicitly retain the corresponding surface-area question. Their inspected Willmore comparison gives a coarse bound by twice the original area in the minimal case, which does not prove the requested sharp inequality. Zhu's spherical-cap theorem concerns a modified functional; its Euclidean limit recovers boundary-length information rather than interior area.

The [boundary-volume question](809-boundary-volume-in-the-conformal-orbit-of-a-free-boundary-minimal-submanifold.md) is a distinct functional. The identity $`k\mathrm{Vol}_k(\Sigma)=\mathrm{Vol}_{k-1}(\partial\Sigma)`$ holds for the original minimal immersion, but a general conformal image need not be Euclidean minimal. Boundary-volume control cannot be converted to the proposed inequality by reusing that identity.

Bounded current searches located no matching complete result or announcement. AIM108/109 concern annulus uniqueness and a first Steklov eigenvalue. All three returned catalogue-description windows were read; they concern Brennan integrability, numerical-range functional calculus and symplectic width. No equivalent target was identified. Linked proof bodies remain separate obligations.

The [coordinator review](../FURTHER_problems/_tracking/fbms-interior-conformal-volume-coordinator-review-2026-10-19.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-fbms-interior-conformal-volume-review.json), [current checks](../FURTHER_problems/_tracking/fbms-interior-conformal-volume-current-root-review-2026-10-19.json) and [duplicate comparison](../FURTHER_problems/_tracking/fbms-interior-conformal-volume-duplicates-review-2026-10-19.json) retain exact scope. The entire 30-page Li version was read for discovery; later comparisons were selected passages, with final-edition and version gaps retained. These are AI checks, not human peer review or an exhaustive absence certificate.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-3deba7294a5078ad**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
