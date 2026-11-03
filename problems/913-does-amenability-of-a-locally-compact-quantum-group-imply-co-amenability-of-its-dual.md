# 913. Does amenability of a locally compact quantum group imply co-amenability of its dual?

**Area:** Operator algebras and noncommutative harmonic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb G`$ be any locally compact quantum group in the sense of Kustermans and Vaes, with von Neumann algebra $`L^\infty(\mathbb G)`$, coproduct $`\Delta`$, and Pontryagin dual $`\widehat{\mathbb G}`$. Amenability means that there is an invariant state $`m`$ on $`L^\infty(\mathbb G)`$, so $`(m\otimes\mathrm{id})\Delta(x)=m(x)1`$ for all $`x\in L^\infty(\mathbb G)`$.

Must $`\widehat{\mathbb G}`$ be **co-amenable**? Equivalently, must $`L^1(\widehat{\mathbb G})`$ have a contractive approximate identity, or must the reduced $`C^*`$-algebra $`C_0(\widehat{\mathbb G})`$ admit a counit? The reverse implication, co-amenability of the dual implies amenability of $`\mathbb G`$, is known. The question concerns all locally compact quantum groups, with no compactness, discreteness or Kac-type assumption.

## Application

This is the quantum-group analogue of Leptin's characterization of amenable locally compact groups by approximate identities in their Fourier algebras. An affirmative answer would identify ordinary amenability with the stronger dual co-amenability condition used in quantum harmonic analysis.

## References

- J. Crann, [*Amenability and covariant injectivity of locally compact quantum groups II*](https://arxiv.org/html/1507.03296v4), *Canad. J. Math.* **69** (2017), 1064–1086, Introduction. The [original v1](https://arxiv.org/abs/1507.03296v1) also poses the general duality problem while proving the compact/discrete case.
- J. L. De Ro, [*Equivariant W*-correspondences*](https://cris.vub.be/ws/portalfiles/portal/131616327/Joeri_De_Ro_PhD_thesis.pdf), PhD thesis, Vrije Universiteit Brussel (2025), Section 1.8.1, Proposition 1.8.4 and following paragraph, printed p. 50 (PDF p. 59). This states the known implication and explicitly retains its converse as open in full generality.
- A. Viselter, [*Amenability of locally compact quantum groups via the long-time behavior of convolution semigroups*](https://arxiv.org/abs/2608.03396), preprint (2026). Its characterization distinguishes amenability and strong amenability; it does not state their general equivalence.

## Status review


**Known cases:** Compact/discrete quantum-group duality is established. Covariant injectivity and long-time convolution-semigroup characterizations do not prove general equivalence of amenability and strong amenability, hence do not give coamenability of the dual for every locally compact quantum group.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Compact/discrete quantum-group duality is established. Covariant injectivity and long-time convolution-semigroup characterizations do not prove general equivalence of amenability and strong amenability, hence do not give coamenability of the dual for every locally compact quantum group.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Crann's original and final versions prove a new injectivity characterization of amenability and a simpler proof of Tomatsu's compact/discrete duality result, while explicitly leaving the general implication open. The 2025 thesis distinguishes co-amenability, amenability and strong amenability, and expressly says the converse to the known dual implication is not known in full generality. A bounded search through 22 October 2026 found no later complete theorem or announced counterexample for arbitrary locally compact quantum groups. The 2026 convolution-semigroup work and a recent colloquium concern distinct characterizations. This check is not exhaustive certification. The [original body receipt](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0203-remote-attested-review.json), [current-status audit](../FURTHER_problems/_tracking/quantum-duality-2026-10-22-status.json) and [duplicate audit](../FURTHER_problems/_tracking/quantum-duality-2026-10-22-duplicates.json) retain the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8c3838a5a2ea868c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
