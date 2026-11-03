# 860. Does positive magnetic curvature force contact type on a magnetic energy level of the sphere?

**Area:** Magnetic dynamics and contact geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`g`$ be a smooth Riemannian metric on $`S^2`$, with area form $`\mu`$, Gaussian curvature $`K`$, and rotation $`\jmath`$ by $`\pi/2`$. Let $`\sigma=f\mu`$ be a smooth symplectic magnetic form, so (after orienting $`S^2`$) $`f>0`$. On $`TS^2`$ equip the kinetic-energy Hamiltonian $`E(x,v)=\tfrac12|v|_g^2`$ with the twisted symplectic form $`\omega_\sigma=d\alpha-\pi^*\sigma`$, where $`\alpha`$ is the metric pullback of the Liouville form. For $`c>0`$ put $`\Sigma_c=E^{-1}(c)`$ and $`m=\sqrt{2c}`$. The source defines the magnetic curvature on the unit tangent bundle by

```math
K_m(x,v)=m^2K(x)-m\,df_x(\jmath v)+f(x),\qquad |v|_g=1.
```

**Benedetti's Conjecture 1.2.** If $`K_m>0`$ everywhere on $`SS^2`$, must $`\Sigma_c`$ be of contact type? Here contact type means that the restriction $`\omega_\sigma|_{\Sigma_c}`$ has a primitive that is a contact form.

The conjecture concerns an arbitrary smooth positive magnetic form and metric on the sphere at an energy satisfying the displayed condition. It is not the contact-type conjecture for exact magnetic forms, nor a claim that every energy level of every magnetic system is contact type.

## Application

Contact type gives a Reeb-flow description of the charged-particle dynamics on that energy level and brings contact-geometric tools to the study of periodic magnetic trajectories. The original work explains that a positive answer would, in particular, establish contact type at every energy for the area-form magnetic system on any convex surface of revolution considered there.

## References

- G. Benedetti, [*The contact property for symplectic magnetic fields on $`S^2`$*](https://doi.org/10.1017/etds.2014.82), *Ergodic Theory Dynam. Systems* **36** (2016), 682–713. [Official arXiv revision](https://arxiv.org/html/1308.2128v2), Section 1, Conjecture 1.2; Section 2.2 for conventions, and Sections 3–4 for partial results.
- V. Assenza, [*Magnetic curvature and existence of a closed magnetic geodesic on low energy levels*](https://doi.org/10.1093/imrn/rnae209), *Int. Math. Res. Not.* **2024** (2024), 13586–13610. Its low-energy periodic-orbit theorem is a different conclusion.
- L. Deschamps, L. Maier and T. Stalljohann, [*On the contact type conjecture for exact magnetic systems*](https://arxiv.org/abs/2508.01113), arXiv:2508.01113v3 (2026). This concerns exact fields and a selected class of systems, so it does not resolve the symplectic $`S^2`$ conjecture.

## Status review


**Known cases:** Benedetti proves low-energy and special-geometry contact type. A noncontact example without positive magnetic curvature is not a counterexample to the implication here. Results for exact fields or merely existence of a periodic orbit have different assumptions or conclusions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Benedetti proves low-energy and special-geometry contact type. A noncontact example without positive magnetic curvature is not a counterexample to the implication here. Results for exact fields or merely existence of a periodic orbit have different assumptions or conclusions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original v1 body passage and the official v2 mathematical setup and Conjecture 1.2 were compared. Benedetti proves contact type for sufficiently low energies and in selected geometries; his noncontact example has no positive magnetic-curvature hypothesis. Current primary searches, including the author's [publication list](https://sites.google.com/view/gabrielebenedetti/research), found no exact later proof, counterexample or announced complete solution. Newer positive-curvature periodic-orbit results and work on exact magnetic forms have different hypotheses or conclusions. This is a bounded status check, not exhaustive certification. The [source receipt](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0201-remote-attested-review.json), [later-version comparison](../FURTHER_problems/_tracking/benedetti-magnetic-curvature-later-version-2026-10-22.json), [current-status audit](../FURTHER_problems/_tracking/benedetti-magnetic-curvature-status-2026-10-22.json), and [duplicate check](../FURTHER_problems/_tracking/benedetti-magnetic-curvature-duplicates-2026-10-22.json) record the limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ee2ab692d11bcb90**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
