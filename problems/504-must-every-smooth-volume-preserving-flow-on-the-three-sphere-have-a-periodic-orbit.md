# 504. Must every smooth volume-preserving flow on the three-sphere have a periodic orbit?

**Area:** Geometry and topology
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega`$ be a smooth volume form on $`S^3`$ and let $`X`$ be a nowhere-vanishing $`C^\infty`$ vector field whose flow preserves $`\Omega`$, equivalently $`\mathcal L_X\Omega=0`$. Must the flow of $`X`$ contain a periodic orbit? Equivalently, can one construct a **smooth, volume-preserving aperiodic flow** on $`S^3`$?

The regularity and conservation assumptions are both essential. Smooth aperiodic vector fields on $`S^3`$ are known without volume preservation. Volume-preserving aperiodic flows are known in the $`C^1`$ class, while the smooth volume-preserving construction in [2] still has a discrete collection of periodic trajectories. The theorem guaranteeing a periodic orbit for a Reeb field on $`S^3`$ concerns a narrower class of volume-preserving flows.

## Application

This question tests whether smooth incompressibility alone forces a closed trajectory in three-dimensional flow. A positive answer would establish a qualitative constraint for every smooth nonsingular divergence-free field on $`S^3`$; a negative answer would require a smooth volume-preserving plug or another aperiodic construction.

## References

1. A. Cannas da Silva, [*Lectures on Symplectic Geometry*](https://people.math.ethz.ch/~acannas/Papers/lsg.pdf), Springer Lecture Notes in Mathematics **1764**, revised author PDF (January 2006), §11.3, printed p. 65. The text explicitly distinguishes the smooth unrestricted and $`C^1`$ volume-preserving counterexamples from this unknown $`C^\infty`$ case.
2. G. Kuperberg, [*A volume-preserving counterexample to the Seifert conjecture*](https://arxiv.org/abs/math/9504230), *Commentarii Mathematici Helvetici* **71** (1996), 70–97. The abstract states the $`C^1`$ aperiodic result and the smooth construction with discrete closed trajectories.
3. J. Fontana-McNally, E. Miranda, C. Oms and D. Peralta-Salas, [*A counterexample to the singular Weinstein conjecture*](https://doi.org/10.1016/j.aim.2024.109998), *Advances in Mathematics* **458** (2024), 109998, discussion following Conjecture 6.2. They explicitly describe the smooth volume-preserving Seifert question as unsolved; their singular-contact counterexample is a different setting.

## Status review

The 2024 primary paper still calls this exact $`C^\infty`$ volume-preserving question open. Bounded searches for later proofs, counterexamples, and announcements through 22 October 2026 found no matching resolution. This status is provisional, with search terms and version limits recorded in the [audit](../FURTHER_problems/_tracking/d015-smooth-volume-preserving-seifert-status-2026-10-22.json). Searches of the AIM list and admitted FURTHER pages found no matching entry; the existing Reeb-flow question has a narrower hypothesis and asks for infinitely many orbits.


### Online recheck, 2026-10-30

Kuperberg's volume-preserving aperiodic construction is C1; unrestricted smooth counterexamples do not preserve volume. The smooth conservative S3 question remains separate from Reeb/contact and singular-contact variants.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/math/9504230); [status source 2](https://doi.org/10.1016/j.aim.2024.109998). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-d3398ebc51f66665** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
