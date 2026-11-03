# 535. The thermal near-critical Ising spin-interface limit

**Area:** Continuum limits in probability and statistical mechanics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D\subset\mathbb C`$ be a bounded simply connected Jordan domain with piecewise smooth boundary and distinct marked boundary points $`a,b`$. Take square-lattice approximations $`(D_\delta,a_\delta,b_\delta)`$ satisfying the marked Carathéodory and close-boundary-approximation conditions of [2, Section 2.1], with uniformly bounded diameters. These conditions include convergence of normalized conformal maps and their marked prime ends, and prevent a marked lattice point from approaching the wrong side of a narrow boundary passage. More precisely, for each sufficiently small circle about $`a`$, the approximation $`a_\delta`$ must be connected inside that circle in the polygonal lattice domain to the midpoint of the last circular crosscut separating $`a`$ from a fixed interior basepoint; impose the analogous condition at $`b`$.

For any fixed $`m\in\mathbb R\setminus\{0\}`$, put

```math
\beta_\delta=\beta_c+m\delta,\qquad \beta_c=\tfrac12\log(1+\sqrt2).
```

On the nearest-neighbour graph use the zero-field Ising law

```math
\Pr_\delta(\sigma)\ \propto\
\exp\!\left(\beta_\delta\sum_{x\sim y}\sigma_x\sigma_y\right),\qquad\sigma_x\in\{-1,+1\},
```

with Dobrushin boundary conditions: plus spins on the clockwise boundary arc from $`a_\delta`$ to $`b_\delta`$, and minus on the other arc. The sum includes nearest-neighbour edges meeting the interior, with boundary spins fixed. Choose the leftmost spin interface from $`a_\delta`$ to $`b_\delta`$, using the auxiliary square-octagon convention of [2, Section 2.2.1] to resolve lattice ambiguities. It separates plus spins on its left from minus spins on its right.

Does its law converge along the full mesh sequence to a single probability law depending only on $`(D,a,b,m)`$, independently of the admissible approximation sequence? Use continuous oriented curves modulo increasing reparametrization, with the uniform curve metric

```math
d_{\rm curv}(\gamma,\eta)=\inf_\rho\ \sup_{0\le t\le1}|\gamma(t)-\eta(\rho(t))|,
```

where $`\rho`$ ranges over increasing homeomorphisms of $`[0,1]`$ and curves at zero distance are identified. Curves in the approximating domains may be transported to $`D`$ by the normalized conformal maps as in [2, Section 2.3.2].

This is a restricted descendant of [1, Problems A–B and Section 2.5]. It asks for full curve-law convergence and uniqueness, without requiring an explicit driving equation, absolute continuity with respect to SLE$`_3`$, full loop-ensemble convergence, or universality across different lattices. A square with opposite marked boundary points already supplies a concrete domain prototype.

## Application

The question asks whether a continuum law describes phase boundaries when temperature approaches its critical value at the mesh scale. Such a law would quantify how a macroscopic thermal perturbation changes critical interface geometry.

## References

1. N. Makarov and S. Smirnov, [*Off-critical lattice models and massive SLEs*](https://arxiv.org/abs/0909.5377v1), eligible 2009 preprint, Problems A–B and Section 2.5. The served sole-version PDF has an internal October 2018 header; proceedings-body parity was not certified.
2. Léonie Papon, [*Interface scaling limit for the critical planar Ising model perturbed by a magnetic field*](https://arxiv.org/abs/2411.16452v1), 2024 preprint, Introduction and Sections 2.1–2.3. It fixes the domain/interface/topology conventions and distinguishes the thermal perturbation from its magnetic-field theorem.
3. Christophe Garban and Antti Kupiainen, [*Energy field of critical Ising model and examples of singular fields in QFT*](https://arxiv.org/abs/2502.02554v3), latest inspected v3 (2026), Sections 2.2 and 2.4. It discusses subsequential thermal scaling limits and the spin-interface question.
4. OpenAI, [*Thermal FK–Ising interfaces and massive SLE*](https://github.com/openai/math/blob/main/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/paper.pdf), 5 October 2026, model and Theorem 2.1. This is an active complete announcement for the distinguished thermal FK exploration.
5. Stéphane Benoist and Clément Hongler, [*The scaling limit of critical Ising interfaces is CLE3*](https://arxiv.org/abs/1604.06975v3), inspected latest preprint v3, Section 3.1, Remark 8, and Section 4. The critical reconstruction argument uses separate convergence of free Ising arcs and additional loop information.
6. S. C. Park, [*Convergence of Fermionic Observables in the Massive Planar FK-Ising Model*](https://arxiv.org/abs/2103.04649v3), latest inspected v3, 5 January 2022. Observable and crossing results are relevant progress; the inspected statements do not give this spin-interface law.

## Status review


**Known cases:** New 23 October 2026 paper by Yu Feng proves mutual absolute continuity with SLE3 for every subsequential thermal spin-interface limit, using uniformly controlled densities. It does not identify a unique full-sequence limit in all admissible Jordan domains. Thermal FK-interface and weak-interaction critical-universality announcements have different targets.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Magnetic-field perturbations at critical inverse temperature, including a later random-field theorem, change a different parameter. Massive observable and spin-correlation limits also do not, by themselves, identify the full thermal spin-interface law.

The complete announcement [4] is retained in this comparison. Its interface separates primal-wired and dual-wired FK clusters and has parameter $`16/3`$; the present target is the plus/minus spin interface. The distinction requires more than comparing those parameters. Edwards–Sokal coupling colours every FK cluster, while one distinguished FK curve does not encode the whole coloured configuration. Deriving the spin limit would require a suitable branching or full-loop convergence result with induced boundary conditions and control of the colouring/gluing operation. The inspected critical argument in [5] separately requires free-Ising-arc convergence; Remark 8 describes the colouring route as a proof scheme needing further discrete FK-loop study.

No matching complete spin-interface theorem or immediate consequence of the inspected current results was located. This does not rule out a further reconstruction argument. Current comparisons are selected checks; the whole proof of [4], other cited proofs, and proceedings-version parity remain unreviewed. These bounded searches do not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/thermal-ising-interface-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-thermal-ising-interface-review.json), [current comparisons](../FURTHER_problems/_tracking/thermal-ising-spin-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/thermal-ising-spin-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/thermal-ising-interface-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/thermal-ising-spin-coordinator-review-2026-10-19.json) record scope and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

New 23 October 2026 paper by Yu Feng proves mutual absolute continuity with SLE3 for every subsequential thermal spin-interface limit, using uniformly controlled densities. It does not identify a unique full-sequence limit in all admissible Jordan domains. Thermal FK-interface and weak-interaction critical-universality announcements have different targets.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.32860); [status source 2](https://arxiv.org/abs/2411.16452); [status source 3](https://github.com/openai/math/blob/main/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/paper.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-312b0ccb8e800320** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
