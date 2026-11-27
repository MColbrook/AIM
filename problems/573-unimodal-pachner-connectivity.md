# 573. Unimodal connectivity by 2–3 and 3–2 Pachner moves

**Area:** Computational topology and triangulated 3-manifolds

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Let $`M`$ be a compact connected 3-manifold with no 2-sphere boundary components. Use generalized triangulations formed by affine pairings of all faces of finitely many tetrahedra; vertices and edges within one tetrahedron may be identified, but an edge may not be identified with itself in reverse. A vertex whose link is a 2-sphere is internal. Other vertices are ideal, and truncating them produces boundary components of $`M`$.

Let $`T`$ and $`U`$ be triangulations of the closed manifold $`M`$, or ideal triangulations representing $`M`$ when its boundary is nonempty. Suppose each has at least two tetrahedra and they have the same number of internal vertices, possibly zero.

A legal $`2`$–$`3`$ move replaces two distinct tetrahedra joined along a face by three tetrahedra around a new edge; its inverse is a $`3`$–$`2`$ move. Is it always possible to pass from $`T`$ to $`U`$ by a finite sequence consisting first entirely of $`2`$–$`3`$ moves and then entirely of $`3`$–$`2`$ moves, with every move preserving the represented manifold?

Equivalently, must $`T`$ and $`U`$ have a common triangulation reachable from each using only $`2`$–$`3`$ moves? Either portion of the sequence may be empty.

## Application

Triangulation moves support manifold recognition and simplification algorithms. A common triangulation reachable by increasing moves would impose useful structure on the search space and justify algorithms that organize searches around a single maximum of the tetrahedron count.

## References

1. B. A. Burton and A. He, [Connecting 3-Manifold Triangulations with Unimodal Sequences of Elementary Moves](https://doi.org/10.1007/s00454-025-00735-4), *Discrete & Computational Geometry* **75** (2026), 1306–1330, Section 2.1, Notation 2.6 and Conjecture 3.1. [arXiv:2012.02398](https://arxiv.org/abs/2012.02398), version 3 (2025).
2. B. A. Burton, [Code accompanying computational topology papers](https://people.smp.uq.edu.au/BenjaminBurton/code/), including the experiments with A. He.

## Status review

Arbitrary sequences of $`2`$–$`3`$ and $`3`$–$`2`$ moves are known to connect the triangulations under these hypotheses. Burton and He [1] give a unimodal sequence with a $`2`$–$`0`$ descent. Their Conjecture 3.1 (Conjecture 8 in arXiv v3) asks for the descent by $`3`$–$`2`$ moves.

**Proposed solution (2026-11-27):** Kaiwen Jin's [manuscript](../research/solutions/573-unimodal-pachner-connectivity/main.pdf) gives an affirmative proof claim. Theorem 1 produces two positive paths to a common triangulation, with the generalized affine pairings, ideal vertices, and fixed internal vertex count of the stated problem. The [target comparison](../research/solutions/573-unimodal-pachner-connectivity/TARGET_COMPARISON.md) maps the hypotheses and conclusion. The [verifier](../research/solutions/573-unimodal-pachner-connectivity/verify_ear_arch.py) replays the finite affine calculations in the proof.

**Review scope:** OpenAI Codex assisted with the proof and manuscript. A same-context AI natural-language audit was followed by one AI reader pass and one AI referee pass in fresh proof contexts that inherited campaign instructions and shared a filesystem. Their feedback informed one manuscript revision. Independent human review and AIM acceptance remain outstanding.
