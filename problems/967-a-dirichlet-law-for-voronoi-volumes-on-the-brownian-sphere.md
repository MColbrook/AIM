# 967. A Dirichlet law for Voronoi volumes on the Brownian sphere

**Area:** Probability; continuum random geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,d,\mu)`$ be the ordinary unit-area Brownian sphere, also called the Brownian map. It is the random compact metric probability space obtained as the measured Gromov–Hausdorff–Prokhorov scaling limit of uniform rooted planar quadrangulations, with uniform vertex probability measure and graph distances scaled by $`n^{-1/4}`$ for $`n`$ faces. A fixed conventional multiplicative constant in the metric does not affect the cells below.

For each fixed integer $`k\ge3`$, conditional on $`(M,d,\mu)`$, sample $`X_1,\ldots,X_k`$ independently with common law $`\mu`$. Define the labeled strict Voronoi cells and their masses by
```math
C_i=\{z\in M:d(z,X_i)<d(z,X_j)\text{ for every }j\ne i\},
\qquad V_i=\mu(C_i).
```

Distance ties have zero $`\mu`$-measure almost surely, so $`\sum_iV_i=1`$.

**Does the joint law, averaging over both the random sphere and the sampled sites, satisfy**
```math
(V_1,\ldots,V_k)\ \overset{d}=\ \mathrm{Dirichlet}(1,\ldots,1)
\qquad\text{for every }k\ge3?
```

Equivalently, $`(V_1,\ldots,V_{k-1})`$ should have constant density $`(k-1)!`$ on
```math
\{(v_1,\ldots,v_{k-1}):v_i>0,\ \textstyle\sum_{i<k}v_i<1\},
\qquad V_k=1-\sum_{i<k}V_i.
```

The labels follow the sampling order. The asserted distribution is averaged over the sphere as well as the sites; no conditional distribution given the sphere is prescribed.

This is the genus-zero, $`k\ge3`$ branch of Conjecture 4 in [1], also stated for the Brownian sphere in [2].

## Application

The masses quantify how independent typical sites divide the area of a continuum random surface. Their law connects stochastic geometry with scaling limits of random maps and two-dimensional random geometry.

## References

1. Guillaume Chapuy, [*On tessellations of random maps and the $`t_g`$-recurrence*](https://doi.org/10.1007/s00440-018-0865-6), **Probability Theory and Related Fields 174** (2019), 477–500. Checked [arXiv:1603.07714v2](https://arxiv.org/html/1603.07714v2), revised 17 September 2018: equation (3), Theorems 2–3 and Conjecture 4.
2. Jean-François Le Gall, [*Geometry of Brownian surfaces*](https://seminaire-poincare.pages.math.cnrs.fr/2023/02.pdf), **Séminaire Poincaré XXIV** (2023), 1–32, §3.4, p. 15.
3. Zhenyao Sun, [*A marked scheme representation for Voronoi volumes in the Brownian map*](https://arxiv.org/html/2610.34255v1), arXiv:2610.34255v1, 25 October 2026. Sections 1.1–1.2, Theorem 1.1 and its following qualification; §2 addresses distance ties.
4. Mathieu Mourichoux, [*Constructing the Brownian sphere from a continuum random unicycle*](https://arxiv.org/html/2511.08524), arXiv:2511.08524, 2025. Proposition 3.16 and §6.2 provide a comparison with delayed cells in a distance-biased model.

## Status review


**Known cases:** The October 2026 marked-scheme representation supplies integral formulae rather than evaluating the entire joint Voronoi law. Delayed distance-biased cells and selected mixed moments do not identify the ordinary sphere law.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The October 2026 marked-scheme representation supplies integral formulae rather than evaluating the entire joint Voronoi law. Delayed distance-biased cells and selected mixed moments do not identify the ordinary sphere law.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Chapuy obtains moment identities consistent with the proposed law, including the three-site mixed moment $`\mathbb E[V_1V_2V_3]=1/60`$. These identities do not determine every joint distribution.

The October 2026 work [3] gives a scheme-integral representation of a negative-power transform of the same ordinary Voronoi volumes. It evaluates the diagonal parameter case and explicitly leaves the proposed Dirichlet law undetermined. This is partial progress toward the displayed target.

The Dirichlet $`(1/4,1/4)`$ law in [4] concerns delayed cells in a distance-biased two-pointed sphere. Results for continuum random trees concern another limiting space. These do not resolve the present sphere law. Current searches and comparisons with the all-status AIM, OpenAI and further-problem lists found no matching full solution or announced resolution; the review does not certify the external proofs or prove absence of a solution.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-097f07a047b0edb4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
