# 873. Scalar-flat realization of extendible Bartnik boundary data

**Area:** Mathematical relativity / scalar curvature
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\gamma`$ be a smooth Riemannian metric on $`\mathbb S^2`$, and let $`H:\mathbb S^2\to(0,\infty)`$ be smooth. Suppose these data are realized as the induced boundary metric and boundary mean curvature of a smooth connected Riemannian three-manifold $`(M,g)`$ with the following properties:

- Its boundary is identified with $`\mathbb S^2`$, and it is complete as a manifold with boundary.
- It has exactly one asymptotically flat end: outside a compact set there are coordinates in which, for some $`\tau>1/2`$,

```math
\partial^\alpha(g_{ij}-\delta_{ij})=O(r^{-\tau-|\alpha|}),\qquad |\alpha|\le2.
```

- Its scalar curvature satisfies $`R_g\ge0`$ and $`R_g\in L^1(M,dV_g)`$.

Mean curvature is the trace of the second fundamental form for the unit normal pointing into the exterior manifold, toward its asymptotically flat end.

Must there exist a smooth connected manifold $`(\widetilde M,\widetilde g)`$ with the same completeness and asymptotic properties, whose boundary has exactly the metric $`\gamma`$ and mean curvature $`H`$, but with

```math
R_{\widetilde g}\equiv0?
```

The topology of $`\widetilde M`$ need not equal that of $`M`$. Compact minimal surfaces are allowed, and no bound on the ADM mass is prescribed. This is the strictly mean-convex spherical case of Anderson's Conjecture 2.4.

## Application

In time-symmetric general relativity, nonnegative scalar curvature represents a nonnegative matter density, while scalar-flat data describe vacuum. The question asks whether boundary geometry already compatible with an exterior containing matter can also be realized by a vacuum exterior. It concerns a basic existence condition in the Bartnik quasi-local mass programme.

## References

1. M. T. Anderson, *Recent progress and problems on the Bartnik quasi-local mass*, Pure and Applied Mathematics Quarterly **15** (2019), 851–873. Conjecture 2.4, p. 859. [Published article](https://doi.org/10.4310/PAMQ.2019.v15.n3.a4), [eligible preprint v1](https://arxiv.org/abs/1903.03822v1), Conjecture 2.4, p. 6.
2. P. Miao and N. Xie, *Bartnik mass via vacuum extensions*, International Journal of Mathematics **30** (2019), 1940006. Theorems 1.1–1.3 and Remark 1.1. [Published article](https://doi.org/10.1142/S0129167X19400068), [preprint v2](https://arxiv.org/abs/1907.02039v2).
3. S. McCormick, *The asymptotically flat scalar-flat Yamabe problem with boundary*, Journal of Geometric Analysis **27** (2017), 2269–2277. The separate boundary-metric and mean-curvature prescriptions. [Published article](https://doi.org/10.1007/s12220-017-9760-0), [preprint](https://arxiv.org/abs/1603.05318).
4. A. Ellithy, *Local Well-posedness of the Bartnik Static Extension Problem near Schwarzschild spheres*, Calculus of Variations and Partial Differential Equations **65** (2026), article 7; published online 4 December 2025. [Published article](https://doi.org/10.1007/s00526-025-03175-3).
5. Z. An and L.-H. Huang, *Strict Stability of the ADM Mass and Static Vacuum Extensions*, preprint (2026). Theorem 2. [arXiv v1](https://arxiv.org/abs/2609.28101v1).

## Status review


**Known cases:** Existing scalar-flat extensions require positive intrinsic Gauss curvature or local perturbation of a static background. Separate prescriptions of the boundary metric or mean curvature do not preserve both simultaneously. Capacity-maximization results solve a different extremal problem.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Existing scalar-flat extensions require positive intrinsic Gauss curvature or local perturbation of a static background. Separate prescriptions of the boundary metric or mean curvature do not preserve both simultaneously. Capacity-maximization results solve a different extremal problem.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check: 18 October 2026.** The exact question is retained in the published 2019 source. Shi–Tam and Miao–Xie provide scalar-flat extensions when $`K_\gamma>0`$; arbitrary smooth intrinsic metrics in the displayed conditional problem are not covered by that hypothesis. The later static-extension results above apply to sufficiently small perturbations of existing background data. Later counterexamples to unrestricted static-vacuum extension concern the stronger static system and do not give a counterexample to scalar-flat realization alone.

A conformal correction with boundary value one preserves $`\gamma`$ but generally changes $`H`$ through its normal derivative. Prescribing mean curvature instead leaves the boundary conformal metric free. Neither separate prescription establishes the simultaneous exact-data assertion here.

The all-status AIM/OpenAI statement comparison found no duplicate at its recorded extent. The cached Prove2Me comparison checked all 186 listing pages with six aliases and found no match. The existing [scalar-flat apparent-horizon problem](880-scalar-flat-apparent-horizon-extensions-with-prescribed-schwarzschild-mass.md) has minimal boundary and prescribed mass, foliation and Schwarzschild-tail requirements; its target differs from this conditional positive-mean-curvature realization question.

The [source and current-results review](../FURTHER_problems/_tracking/coordinator-relativity/scalar-flat-realization-review-2026-10-18.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-scalar-flat-realization-review.json), [semantic comparison](../FURTHER_problems/_tracking/coordinator-relativity/scalar-flat-realization-duplicates-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/coordinator-relativity/scalar-flat-realization-catalogue-2026-10-18.json) and [coordinator decision](../FURTHER_problems/_tracking/coordinator-relativity/scalar-flat-realization-coordinator-2026-10-18.json) record the exact reading extents. The complete published 23-page survey has not been compared with its 14-page preprint; its published question was checked directly. These checks do not certify absence of every later result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-042d2def81f9ad6a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
