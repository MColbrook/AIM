# 984. A translation-invariant noncrossing Poisson matching in the plane

**Area:** Probability and statistics / stochastic geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`R`$ and $`B`$ be independent homogeneous Poisson point processes of intensity one in $`\mathbb R^2`$. Thus the number of points of either colour in a bounded Borel set $`A`$ has Poisson distribution with mean equal to the Euclidean area of $`A`$.

Does there exist a joint probability law for $`(R,B,M)`$, retaining this independent law for $`(R,B)`$, with the following properties?

1. $`M`$ is a simple matching point process on $`\mathbb R^2\times\mathbb R^2`$. Almost surely, its pairs $`(r,b)`$ match each red point to exactly one blue point and each blue point to exactly one red point.
2. Almost surely, the closed straight line segments $`[r,b]`$ and $`[r',b']`$ are disjoint for every two distinct matched pairs.
3. The joint law is invariant under every translation: for each $`t\in\mathbb R^2`$, translating all red points, blue points and both endpoints of every pair by $`t`$ preserves the law.

Construct such a law or prove that none exists. This is Question 1 of reference 1, originally posed by Yuval Peres.

Additional randomness is allowed: $`M`$ need not be a deterministic function of $`R`$ and $`B`$. No cost-minimality, moment bound, rotational symmetry or ergodicity assumption is imposed. The requirement that $`M`$ be a point process on the product space does not require that only finitely many drawn segments meet each compact set in the plane.

## Application

This asks whether two independent homogeneous random populations can be paired without geometric crossings while treating every location alike. It separates geometric compatibility and spatial symmetry from the stronger demand to minimize transportation cost.

## References

1. A. E. Holroyd, *Geometric properties of Poisson matchings*, **Probability Theory and Related Fields** 150(3–4) (2011), 511–527. [Published article](https://doi.org/10.1007/s00440-010-0282-y), Question 1 on p. 513; definitions on p. 512 and the discussion of additional randomness on pp. 514–515. [arXiv:0909.0575v1](https://arxiv.org/abs/0909.0575), submitted 3 September 2009, native PDF pages 1–5.
2. A. E. Holroyd, S. Janson and J. Wästlund, *Minimal matchings of point processes*, **Probability Theory and Related Fields** 184 (2022), 571–611. [Published article](https://doi.org/10.1007/s00440-022-01151-y), Theorem 7 and its following discussion.
3. M. Huesmann, F. Mattesini and F. Otto, *There is no stationary $`p`$-cyclically monotone Poisson matching in 2D*, [arXiv:2311.17687v1](https://arxiv.org/abs/2311.17687) (2023), Questions 1.1–1.2 and Theorem 1.3; [publication DOI](https://doi.org/10.1214/24-EJP1171).
4. V. Armegioiu, M. Goldman, F. Grotto and D. Trevisan, *Exact Asymptotics for the 2D Euclidean Random Matching Problem*, [arXiv:2609.08717v2](https://arxiv.org/abs/2609.08717), 11 October 2026, §1.1 and Theorem 1.1.

## Status review


**Known cases:** Translation-invariant noncrossing perfect matching allows additional randomness and has no cost optimality restriction. Nonexistence of stationary cyclically monotone/cost-minimal matchings and finite-box asymptotics do not exclude every noncrossing law.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Translation-invariant noncrossing perfect matching allows additional randomness and has no cost optimality restriction. Nonexistence of stationary cyclically monotone/cost-minimal matchings and finite-box asymptotics do not exclude every noncrossing law.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original article constructs noncrossing matchings when translation invariance is dropped, and invariant variants with one colour or unequal intensities. These do not give the equal-intensity two-colour law requested here.

Reference 2 constructs translation-invariant two-colour $`\gamma`$-minimal matching schemes in $`\mathbb R^2`$ for $`\gamma<1`$. Its theorem does not assert noncrossing segments or cover the length-minimizing case $`\gamma=1`$. Reference 3 proves nonexistence with the additional finite-rematching cost-minimality condition for $`p>1`$; its introduction explicitly leaves the question of noncrossing matchings unresolved.

The finite-sample torus cost asymptotics in reference 4 do not provide a stationary perfect matching of two infinite Poisson processes in the plane. Existence of finite noncrossing matchings alone does not establish a suitable infinite-volume law.

Bounded current-literature, announcement and all-status duplicate checks found no matching complete resolution or existing AIM/FURTHER entry. The intake source predates January 2022; later sources are used to check status. The [owner review](../FURTHER_problems/_tracking/C123-0909.0575-planar-Poisson-matching-Q1-focused-owner-ready-A-END-20261026.json) and [independent review](../FURTHER_problems/_tracking/C123-planar-Poisson-root-independent-formulation-current-allstatus-PASS-END-20261026.json) retain primary-source bindings, version and access limits, dated searches and semantic comparisons.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-abb4d8b736b6e253**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
