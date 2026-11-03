# 809. Boundary volume in the conformal orbit of a free boundary minimal submanifold

**Area:** Minimal submanifolds and conformal geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every pair of integers $`3\le k<n`$, let $`\Sigma`$ be a compact connected smooth $`k`$-manifold with nonempty boundary, and let
```math
X:\Sigma\longrightarrow\overline{B^n}
```

be a smooth immersion. Give $`\Sigma`$ the induced Euclidean metric $`g=X^*g_{\mathrm E}`$. Assume
```math
X^{-1}(S^{n-1})=\partial\Sigma,\qquad
\Delta_gX=0,\qquad dX(\eta)=X\quad\hbox{on }\partial\Sigma,
```

where $`\eta`$ is the outward unit conormal of $`\partial\Sigma`$ in $`\Sigma`$. Thus $`X`$ is a free boundary minimal immersion into the unit ball.

For every conformal diffeomorphism $`f:\overline{B^n}\to\overline{B^n}`$, must
```math
\mathrm{Vol}_{k-1}\!\left(\partial\Sigma,
   ((f\circ X)^*g_{\mathrm E})|_{T\partial\Sigma}\right)
\le
\mathrm{Vol}_{k-1}\!\left(\partial\Sigma,g|_{T\partial\Sigma}\right)
```

hold? The volumes are computed on the parameter manifold, so that an immersed boundary is counted with its multiplicity. No orientability, embeddedness, topology, or first-Steklov-eigenvalue hypothesis is imposed.

Equivalently, for every $`y\in\mathbb R^n`$ with $`|y|>1`$, ask whether
```math
\int_{\partial\Sigma}
 \left(\frac{|y|^2-1}{|X-y|^2}\right)^{k-1}\,dA_g
\le \int_{\partial\Sigma}dA_g.
```

This is the higher dimensional part of Fraser–Schoen's Conjecture 3.7 in *Minimal surfaces and eigenvalue problems* (2013), restated as Open Question 9 in Li's survey arXiv:1907.05053v3, pages 25–26. The case $`k=2`$ is known. The known second-order decrease at the identity does not establish the inequality for every conformal diffeomorphism. This question concerns boundary volume; the separate question about the interior $`k`$-volume is not included.

## Application

Free-boundary minimal submanifolds describe stationary area configurations meeting a container orthogonally. The inequality would identify a global extremal property of their boundaries and connect free-boundary geometry with conformal-volume and spectral estimates.

## References

1. Ailana Fraser and Richard Schoen, *Minimal surfaces and eigenvalue problems*, Contemporary Mathematics **599** (2013), 105–121. [Author version](https://arxiv.org/abs/1304.0851v1), Conjecture 3.7 and Theorems 3.3, 3.8.
2. Martin Man-Chun Li, *Free boundary minimal surfaces in the unit ball: recent advances and open questions*. [Latest author version](https://arxiv.org/abs/1907.05053v3), 2 July 2020, Open Question 9, physical pp.25–26. The entire 30-page version was read for discovery; final proceedings parity remains separate.
3. Jonathan J. Zhu, *Free boundary and capillary minimal surfaces in spherical caps II: Low energy*. [Inspected scientific HTML](https://arxiv.org/html/2512.20857v1), Introduction §1.1, Theorem 1.5 and Remarks 5.4, 5.9–5.10. The official record lists a sole December 2025 version while the served HTML bears an August 2026 internal date; PDF/HTML identity is unverified.

## Status review


**Known cases:** The requested quantity is boundary volume for dimensions at least three. The two-dimensional theorem and higher-dimensional second-variation inequality do not prove the global comparison along all conformal ball maps. Spherical-cap modified functionals have another target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The requested quantity is boundary volume for dimensions at least three. The two-dimensional theorem and higher-dimensional second-variation inequality do not prove the global comparison along all conformal ball maps. Spherical-cap modified functionals have another target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The two-dimensional boundary-length inequality is known. In higher dimensions, the original source establishes a local second-variation conclusion. Such local information does not give the inequality for every conformal map, whose image generally ceases to be Euclidean minimal.

The inspected Zhu result maximizes a modified energy in spherical caps under dimensional or hemisphere restrictions. Its relevant higher-dimensional Euclidean limits involve coordinate-dependent boundary integrals. The text explicitly distinguishes and retains this boundary-volume question. Recent conformal-domain instability theorems and embedded-annulus classification claims address different quantities or classes.

Bounded current searches found no matching complete result or announcement. AIM108 and109 concern annulus uniqueness and a first Steklov eigenvalue, respectively. Canonical and FURTHER comparisons found no equivalent target. The sole returned catalogue-description window concerned conformally compact Ricci geometry and was read in full; linked proof bodies remain pending.

The [coordinator review](../FURTHER_problems/_tracking/fbms-boundary-conformal-volume-coordinator-review-2026-10-19.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-fbms-boundary-conformal-volume-review.json), [current checks](../FURTHER_problems/_tracking/fbms-boundary-conformal-volume-current-root-review-2026-10-19.json) and [duplicate comparison](../FURTHER_problems/_tracking/fbms-boundary-conformal-volume-duplicates-review-2026-10-19.json) preserve scope and access limits. These are AI checks, not human peer review or an exhaustive absence certificate. A displayed integration-domain inconsistency in the original second-variation formula is recorded in the audit; no disputed formula is used in the proposed target.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-805d2a1e8241c6b3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
