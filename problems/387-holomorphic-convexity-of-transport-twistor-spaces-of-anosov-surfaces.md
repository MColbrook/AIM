# 387. Holomorphic convexity of transport twistor spaces of Anosov surfaces

**Area:** Geometric inverse problems / complex geometry
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a smooth, connected, closed, oriented Riemannian surface whose geodesic flow $`\phi_t`$ on the unit tangent bundle $`SM`$ is Anosov. Thus there is an invariant splitting

```math
T(SM)=\mathbb RX\oplus E^s\oplus E^u
```

and constants $`C,\lambda>0`$ such that $`\|d\phi_t|_{E^s}\|\le Ce^{-\lambda t}`$ and $`\|d\phi_{-t}|_{E^u}\|\le Ce^{-\lambda t}`$ for $`t\ge0`$, where $`X`$ generates the flow.

Equip the open unit disk bundle

```math
Z^\circ=\{(x,v)\in TM:g_x(v,v)<1\}
```

with its **transport twistor complex structure**, defined below. Is $`Z^\circ`$ holomorphically convex? Explicitly, for every nonempty compact $`K\subset Z^\circ`$, must the holomorphic hull

```math
\widehat K=\{z\in Z^\circ: |f(z)|\le\sup_K|f|
                  \text{ for every }f\in\mathcal O(Z^\circ)\}
```

be compact in $`Z^\circ`$? Here $`\mathcal O(Z^\circ)`$ contains all holomorphic functions, with no prescribed behaviour at the unit circle boundary. Prove this for every such surface or give a counterexample within this class.

For completeness, the complex structure can be specified without choosing a global coordinate chart. Let $`V`$ generate positive rotations in the fibres of $`SM`$, put $`H=[V,X]`$ and $`\eta_\pm=(X\mp iH)/2`$, and let $`I`$ be rotation by $`\pi/2`$ on $`TM`$. For $`\mathbb D=\{\omega\in\mathbb C:|\omega|<1\}`$ define

```math
p:SM\times\mathbb D\longrightarrow Z^\circ,
\qquad p(x,v,\omega)=(x,(\Re\omega)v+(\Im\omega)Iv).
```

The transport complex structure is the integrable structure with

```math
T^{0,1}Z^\circ
=dp\bigl(\mathrm{span}_{\mathbb C}
       \{\omega^2\eta_++\eta_-,\partial_{\bar\omega}\}\bigr).
```

The indicated distribution descends through $`p`$. It is nondegenerate for $`|\omega|<1`$.

## Application

Transport twistor spaces translate geodesic transport equations and invariant distributions into complex geometry. Their holomorphic functions provide a framework for tensor tomography and rigidity questions. Holomorphic convexity would give compact holomorphic hulls in this setting.

Bohr–Lefeuvre–Paternain explicitly ask this question. Their Theorem 1.2 and Proposition 4.11 give many interior holomorphic functions through distributional first integrals. Functions extending smoothly to the circle boundary are constant in the Anosov case, so that smaller algebra must not replace $`\mathcal O(Z^\circ)`$ in the question.

The compact zero section is a holomorphic curve. Consequently $`Z^\circ`$ is never Stein for a closed base surface; this does not rule out holomorphic convexity. The same source proves holomorphic convexity for flat tori and failure for sphere bases. Those cases are outside the Anosov hypothesis.

## References

- J. Bohr, T. Lefeuvre and G. P. Paternain, *Invariant distributions and the transport twistor space of closed surfaces*, Journal of the London Mathematical Society **109** (2024), e12894, 39 pp. [DOI](https://doi.org/10.1112/jlms.12894), [published manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/31b16d40-bdbf-4103-b8aa-21e3a35b67a3/content). Exact question: p. 5; construction: §3.1, pp. 13–14; relevant progress: Theorem 1.2 and Proposition 4.11.
- J. Bohr, F. Monard and G. P. Paternain, *Biholomorphism rigidity for transport twistor spaces*, Proceedings of the Royal Society A **481** (2025), 20240809. [DOI](https://doi.org/10.1098/rspa.2024.0809). Its rigidity theorem classifies biholomorphisms between the associated spaces; it does not assert holomorphic convexity.

## Status review

**Status checked: 17 October 2026.** The current local blow-down and Zoll magnetic results have different hypotheses or complex structures and do not give the displayed universal holomorphic-hull conclusion. Detailed selected-source comparisons and scoped catalogue comparison: [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/anosov-twistor-convexity-review.json). The independent selected-primary audit, scoped catalogue comparison and coordinator review passed.

[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-anosov-twistor-convexity-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/anosov-convexity-duplicate-navigation.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/rough-filtering/batch-0155-deployment-validation.json) and [coordinator review](../FURTHER_problems/_tracking/anosov-convexity-coordinator-review-2026-10-17.json) record the exact checks and reading limits.


### Online recheck, 2026-10-30

Current transport-twistor biholomorphism rigidity, local blow-downs and constant-curvature/perturbative coordinate results do not imply compact holomorphic hulls for every compact subset of every Anosov-surface transport twistor interior.

Comparators and current-status sources: [status source 1](https://doi.org/10.1112/jlms.12894); [status source 2](https://doi.org/10.1098/rspa.2024.0809); [status source 3](https://doi.org/10.3842/SIGMA.2026.045). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-f40000a5ac400fd8** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
