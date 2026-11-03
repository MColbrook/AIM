# 395. Can one bending experiment locate a cavity in an elastic plate?

**Area:** Inverse problems and imaging
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a smooth simply connected plate midplane, and let $`D\Subset\Omega`$ be a smooth simply connected cavity. In the static isotropic Kirchhoff–Love bending model, the transverse displacement $`w_D`$ satisfies

```math
\mathrm{div}\mathrm{div}(\mathbb P\nabla^2w_D)=0
\quad\text{in }\Omega\setminus\overline D,
```


with a prescribed nonzero compatible couple field $`\widehat M`$ on the accessible outer boundary and the **free-edge** (zero bending moment and effective shear) conditions on $`\partial D`$. The direct problem and both boundary conditions are specified in [1, equations (1)–(6)]. Since $`w_D`$ is determined only up to an affine function, normalize it consistently.

Suppose two such cavities $`D_1,D_2`$ under the *same single* $`\widehat M`$ produce identical transverse displacements and normal slopes on $`\partial\Omega`$:

```math
w_{D_1}|_{\partial\Omega}=w_{D_2}|_{\partial\Omega},
\qquad
\partial_\nu w_{D_1}|_{\partial\Omega}=\partial_\nu w_{D_2}|_{\partial\Omega}.
```


Must $`D_1=D_2`$? One may ask this within the regularity and ellipticity class of the two-measurement cavity theorem [2, Theorem 4.4]. Morassi and Rosset explicitly pose the one-measurement cavity case in [1, p. 451]. Their one-measurement theorem concerns an **unknown part of the exterior boundary**, where competing plates share an accessible boundary arc. Their separate result for an interior *rigid inclusion* imposes different conditions on its boundary.

## Application

A single controlled bending test is a natural non-destructive way to inspect a thin plate. A uniqueness theorem would say whether the measured outer deflection and slope determine the shape of an unseen free cavity, before any reconstruction method is attempted.

## References

1. A. Morassi and E. Rosset, [*Unique determination of unknown boundaries in an elastic plate by one measurement*](https://comptes-rendus.academie-sciences.fr/mecanique/item/10.1016/j.crme.2010.07.011.pdf), *Comptes Rendus Mécanique* **338** (2010), 450–460, p. 451, explicit final open question; §3 for the solved outer-boundary and rigid-inclusion cases; [DOI](https://doi.org/10.1016/j.crme.2010.07.011).
2. A. Morassi, E. Rosset and S. Vessella, [*Unique determination of a cavity in an elastic plate by two boundary measurements*](https://www.aimsciences.org/article/doi/10.3934/ipi.2007.1.481), *Inverse Problems and Imaging* **1** (2007), 481–506; [DOI](https://doi.org/10.3934/ipi.2007.1.481). Their later [survey](https://arxiv.org/pdf/1209.6066), §4.3, Theorems 4.4–4.5, compares the two-measurement cavity theorem with the one-measurement outer-boundary theorem.
3. A. Morassi, E. Rosset and S. Vessella, [*Optimal identification of cavities in the Generalized Plane Stress problem in linear elasticity*](https://arxiv.org/abs/2001.04805), *Journal of the European Mathematical Society* (2022), [DOI](https://doi.org/10.4171/JEMS/1190). Its one-experiment result uses in-plane loads and displacement in a different plate model.

## Status review

The [bounded status and duplicate audit](../FURTHER_problems/_tracking/j302-morassi-rosset-one-measurement-cavity-status-2026-10-22.json) through 22 October 2026 found no matching one-measurement theorem or announcement for this transverse-bending, free-cavity setting. It checks the later in-plane result separately.


### Online recheck, 2026-10-30

The 2026 exterior biharmonic-cavity paper uses an unbounded plate and two measurement sets. In-plane elasticity, time-harmonic scattering and one-measurement outer-boundary/rigid-inclusion results do not settle one static bending experiment for a free interior cavity in a bounded plate.

Comparators and current-status sources: [status source 1](https://doi.org/10.1016/j.crme.2010.07.011); [status source 2](https://www.sciencedirect.com/science/article/abs/pii/S0022039626003062); [status source 3](https://doi.org/10.3934/ipi.2007.1.481). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-8db01cfffaa2ac1c** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
