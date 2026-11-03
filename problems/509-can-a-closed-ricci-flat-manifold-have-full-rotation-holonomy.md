# 509. Can a closed Ricci-flat manifold have full rotation holonomy?

**Area:** Riemannian geometry; Einstein metrics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Does there exist an integer $`n\geq4`$, a smooth closed connected simply connected $`n`$-manifold $`M`$, and a smooth Riemannian metric $`g`$ such that

```math
\mathrm{Ric}_g=0,
\qquad \mathrm{Hol}_p(g)=\mathrm{SO}(T_pM,g_p)?
```

Here **closed** means compact without boundary. The holonomy group consists of the linear maps obtained by Levi–Civita parallel transport around all piecewise smooth loops based at $`p`$. Simply connectedness makes full and restricted holonomy agree. The displayed full rotation group condition is independent of the choice of $`p`$ up to conjugacy.

Construct such a metric in some dimension, or prove that none exists. No stability, spin, complex structure, symmetry or prescribed topology assumption is added. In dimensions at most three Ricci-flat Riemannian metrics are flat, which rules out this closed simply connected case. The special-holonomy examples supplied by Calabi–Yau, hyperkähler, $`G_2`$ and $`\mathrm{Spin}(7)`$ constructions do not have the full rotation holonomy required here. The question asks about existence across all dimensions, rather than prescribing one manifold such as $`S^2\times S^2`$.

## Application

Ricci-flat metrics are stationary solutions of Ricci flow and the zero cosmological constant Riemannian Einstein equation. They also describe internal geometries in leading geometric models of vacuum compactification. In the dimensions used by those models, distinguishing full holonomy from special holonomy helps determine whether parallel spinors, and the associated supersymmetry, are forced. This geometric existence question makes no assertion about quantum stability or experimental predictions.

## References

1. B. S. Acharya, *Supersymmetry, Ricci flat manifolds and the String Landscape*, **Journal of High Energy Physics** 08 (2020), 128, §1.1, Table 1 and Conjecture 1, printed p.4 (physical p.5). [Published article](https://doi.org/10.1007/JHEP08(2020)128), [open final PDF](https://inspirehep.net/files/ba9e907afea3b41d0d9f2808e4284a09), [eligible preprint v3](https://arxiv.org/abs/1906.06886v3).
2. X. Dai, X. Wang and G. Wei, *On the stability of Riemannian manifold with parallel spinors*, **Inventiones Mathematicae** 161 (2005), 151–176, §5, Proposition 5.1 and the following open question, p.174. [Author copy of published article](https://web.math.ucsb.edu/~dai/paper/dwwInvent.pdf).
3. G. Cao-Labora and A. Rodríguez-Vázquez, *Inhomogeneous Einstein metrics on complex projective spaces*, arXiv:2608.16880v1 (2026), introduction, paragraph discussing zero Einstein constant. [Current primary discussion](https://arxiv.org/html/2608.16880v1#S1). This is a status reference; its positive Einstein metrics do not settle the Ricci-flat question.
4. M. Khuri, M. Reiris, G. Weinstein and S. Yamada, *Gravitational solitons and complete Ricci flat Riemannian manifolds of infinite topological type*, arXiv:2204.08048v2, Theorems 4–5. [Primary comparison](https://arxiv.org/abs/2204.08048v2). Their full-holonomy examples are noncompact, including after the stated partial compactifications.

## Status review

The primary 2020 publication states the generic-holonomy possibility explicitly, and the August 2026 primary discussion still identifies the compact simply connected special-holonomy question as open. Searches checked on 17 October 2026 found no complete proof, counterexample or matching announcement for the displayed compact problem. Negative searches do not prove universal openness.

Complete noncompact full-holonomy examples, flat nonsimply connected quotients, and positive Einstein examples have different hypotheses. Ricci-flow stability theorems conditional on properties of an existing Ricci-flat metric do not construct a full-holonomy compact example or rule all such examples out. No separate page is proposed for the contained $`S^2\times S^2`$ test or physically refined stability questions.

The existing AIM statements and retained statuses, pending/admitted/excluded FURTHER findings and imported OpenAI announcement families were compared semantically. The closest complex Monge–Ampère rigidity question concerns noncompact Kähler metrics with growth bounds; the Ricci-flow extension announcement concerns finite-time singularities. Neither is this closed metric existence question. Independent selected-primary review passed. Seven aliases were checked against all 186 cached catalogue pages without a matching listing; this does not claim review of every mission proof body.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/ricci-full-holonomy-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-ricci-full-holonomy-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/ricci-full-holonomy-duplicate-snapshot.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/ricci-full-holonomy-prove2-0139-review.json) and [coordinator review](../FURTHER_problems/_tracking/ricci-holonomy-coordinator-review-2026-10-17.json) retain exact source versions and scope limits.


### Online recheck, 2026-10-30

Complete noncompact full-holonomy examples and positive-Einstein constructions do not construct a closed simply connected Ricci-flat SO(n)-holonomy manifold or exclude all such manifolds.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1906.06886); [status source 2](https://arxiv.org/abs/2608.16880); [status source 3](https://arxiv.org/abs/2204.08048). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-3e256070aadbc752** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
