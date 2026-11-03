# 771. Stationary theta networks on Riemannian two-spheres

**Area:** Riemannian geometry / stationary length networks
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`g`$ be any smooth Riemannian metric on $`S^2`$. Must there exist two distinct points $`p,q\in S^2`$, positive lengths $`L_1,L_2,L_3`$, and three embedded unit-speed geodesic arcs

```math
\gamma_i:[0,L_i]\longrightarrow(S^2,g),\qquad
\gamma_i(0)=p,\quad\gamma_i(L_i)=q,
```

whose interiors are pairwise disjoint and satisfy

```math
\sum_{i=1}^3\dot\gamma_i(0)=0,
\qquad
\sum_{i=1}^3\bigl(-\dot\gamma_i(L_i)\bigr)=0?
```

Thus the union is an embedded graph homeomorphic to the Greek letter $`\Theta`$, with three edges and two triple junctions. The outgoing unit tangents at each junction meet at angles $`2\pi/3`$. The arcs need not minimize distance globally between $`p`$ and $`q`$. Their lengths must remain positive and the two vertices distinct.

## Application

The balance condition is the first-variation equation for the total length of three filaments of equal tension constrained to a curved surface. The question asks whether this particular nondegenerate equilibrium topology always occurs.

## Known results

Hass–Morgan prove that every positively curved Riemannian two-sphere has a stationary network of one of three types: theta, eyeglasses, or figure-eight. They obtain a theta network when the metric is sufficiently close to the round metric. Sciaraffia's 2024 theorem gives at least four theta networks for metrics on $`S^2`$ sufficiently close to the round metric in $`C^2`$.

The same 2024 paper explicitly notes that existence of a theta network is still unknown even for an arbitrary positively curved metric. That positive-curvature restriction is an important special case of the question above, rather than a second problem here.

## References

1. K. Burns and V. S. Matveev, *Open problems and questions about geodesics*, [arXiv:1308.5417v3](https://arxiv.org/pdf/1308.5417v3), §11 and Question 11.1.1, pp. 29–30. Published in *Ergodic Theory and Dynamical Systems* **41** (2021), 641–684, [DOI](https://doi.org/10.1017/etds.2019.73). The cited locator is for the latest eligible preprint; final-edition body parity is not certified.
2. J. Hass and F. Morgan, *Geodesic nets on the 2-sphere*, *Proceedings of the American Mathematical Society* **124** (1996), 3843–3850. [DOI](https://doi.org/10.1090/S0002-9939-96-03492-2). Original attribution; publisher access was blocked during this review, so the theorem comparison also uses the explicit account in Reference 3.
3. L. Sciaraffia, *Minimal Networks on Balls and Spheres for Almost Standard Metrics*, *The Journal of Geometric Analysis* **34** (2024), article 319. [Published article](https://doi.org/10.1007/s12220-024-01765-9), introduction immediately before Theorem 1.1, and §2 through Definition 2.2. The published HTML was read directly.

## Status review


**Known cases:** The target prescribes an embedded stationary theta graph for every smooth metric on S2. Almost-round metrics, generic geodesic-network density and closed geodesics do not impose this topology or both balanced triple vertices; singular doubled-polygon metrics are outside scope.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target prescribes an embedded stationary theta graph for every smooth metric on S2. Almost-round metrics, generic geodesic-network density and closed geodesics do not impose this topology or both balanced triple vertices; singular doubled-polygon metrics are outside scope.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1308.5417v3); [comparison source 2](https://doi.org/10.1017/etds.2019.73); [comparison source 3](https://doi.org/10.1090/S0002-9939-96-03492-2); [comparison source 4](https://doi.org/10.1007/s12220-024-01765-9). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Primary-source and announcement searches on 17 October 2026 located no proof or counterexample for the stated arbitrary smooth metric. Generic existence or density of stationary networks does not prescribe this topology for every metric. Infinitely many closed geodesics do not supply triple junctions satisfying the displayed balance conditions. The flat cone metrics on doubled polygons have singularities and do not constitute smooth counterexamples.

Independent selected-primary review passed. All 186 cached catalogue pages were compared with fourteen precise aliases; all six returned windows concern discrete graph cycle counts. This is a bounded listing-description comparison, not a review of every mission proof or every possible wording.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/sphere-theta-network-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-sphere-theta-network-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/positive-sphere-theta-broad-duplicate-snapshot.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/sphere-theta-prove2-0136-review.json) and [coordinator review](../FURTHER_problems/_tracking/sphere-theta-coordinator-review-2026-10-17.json) preserve exact evidence and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-18d40213b01b34fc**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
