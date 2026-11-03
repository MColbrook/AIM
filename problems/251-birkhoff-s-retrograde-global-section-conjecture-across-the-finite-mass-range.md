# 251. Birkhoff's retrograde global-section conjecture across the finite-mass range

**Area:** Celestial mechanics, Hamiltonian dynamics and contact geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

In the planar circular restricted three-body problem, let the two primaries have mass ratio $`0<\mu<1`$. Let $`E<L_1(\mu)`$ be below the first Lagrange critical energy. At this energy there are two bounded physical components, one around each primary; after collision regularization each is a flow on a three-manifold diffeomorphic to $`\mathbb RP^3`$. A **retrograde orbit** is a periodic orbit that winds around a primary in the direction opposite to the rotating frame.

**Question (Birkhoff).** For every such finite $`\mu`$ and every subcritical $`E`$, does the double cover of a retrograde orbit bound a disk-like global surface of section on each regularized bounded component? Equivalently, in the $`\mathbb RP^3`$ description, does the retrograde orbit bind a rational disk-like page whose interior is transverse to the flow and which every other trajectory meets in both forward and backward time?

Existence of retrograde periodic orbits alone is known and is not the question. The unresolved target is the global return property with the correct disk-like boundary. The all-parameter statement does not follow from results near equal masses or in the Hill lunar limit.

## Application

Such a section reduces the dynamics away from its binding orbit to a two-dimensional first-return map. It would give a uniform tool for studying periodic and recurrent trajectories throughout the finite-mass, subcritical parameter range.

## References

1. G. D. Birkhoff, [*The restricted problem of three bodies*](https://doi.org/10.1007/BF03015982), *Rendiconti del Circolo Matematico di Palermo* **39** (1915), 265–334.
2. C. Joung and O. van Koert, [*Computational symplectic topology and symmetric orbits in the restricted three-body problem*](https://arxiv.org/abs/2407.19159v3), *Nonlinearity* **38** (2025), 025015. The introduction describes Birkhoff's conjecture and partial computational results.
3. L. Liu and P. A. S. Salomão, [*Finite energy foliations and global dynamics in the restricted three-body problem*](https://arxiv.org/html/2506.17867v2), arXiv:2506.17867v2 (25 May 2026), §1.4 and Theorem 1.16. They prove the conjecture for $`\mu`$ sufficiently close to $`1/2`$ and all subcritical energies.
4. L. Liu and P. A. S. Salomão, [*Birkhoff conjecture and finite energy foliations in Hill's lunar problem*](https://arxiv.org/abs/2606.12912), arXiv:2606.12912v1 (11 June 2026). This proves the analogous Hill limiting-model statement.
5. [Prove2Me mission: Birkhoff's retrograde global-section conjecture](https://prove2.me/missions/Birkhoff%27s_Retrograde_Global-Section_Conjecture_in_the_Planar_Circular_Restricted_Three-Body_Problem), consulted 21 October 2026. Its formal theorem rows use `sorry` placeholders and are not claimed solutions.

## Status review


**Known cases:** The current near-equal-mass theorem covers all subcritical energies only for mu near 1/2; the Hill theorem is a limiting model. They do not give disk-like global sections for every finite mass ratio.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Liu and Salomão's current arXiv version explicitly formulates Birkhoff's question in §1.4 and proves its near-equal-mass case in Theorem 1.16. Their later Hill paper proves a limiting problem; it does not cover every finite $`\mu`$. Joung and van Koert give methods and restricted numerical results. Targeted exact-question, later-proof, counterexample and announcement searches through 2026-10-21 found no matching all-finite-mass result. This is a bounded search, not a guarantee about unpublished or inaccessible work.

An AIM/FURTHER semantic search found no duplicate; AIM's Birkhoff billiards entry concerns a different conjecture. The [status and duplicate receipt](../FURTHER_problems/_tracking/prove2-birkhoff-retrograde-status-2026-10-21.json) records the checks and points to the cached full mission description.


### Online recheck, 2026-10-30

The current near-equal-mass theorem covers all subcritical energies only for mu near 1/2; the Hill theorem is a limiting model. They do not give disk-like global sections for every finite mass ratio.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2506.17867); [status source 2](https://arxiv.org/abs/2606.12912); [status source 3](https://arxiv.org/abs/2407.19159). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c1eabf628ed77452** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
