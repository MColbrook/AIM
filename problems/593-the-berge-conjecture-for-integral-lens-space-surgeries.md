# 593. The Berge conjecture for integral lens-space surgeries

**Area:** Geometric topology and Dehn surgery
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`K\subset S^3`$ be a smooth knot and $`n\in\mathbb Z`$. Write $`S^3_n(K)`$ for the Dehn filling that identifies the meridian of the attached solid torus with $`n\mu+\lambda`$, where $`\mu`$ is the meridian and $`\lambda`$ the preferred longitude of the knot exterior.

If $`S^3_n(K)`$ is a lens space, must $`K`$ be **doubly primitive**?

Explicitly, the conclusion asks for an isotopy of $`K`$ onto the standard genus-two Heegaard surface
```math
S^3=H_1\cup_\Sigma H_2
```

and properly embedded essential meridian disks $`D_i\subset H_i`$ such that
```math
|K\cap\partial D_i|=1,\qquad i=1,2,
```

with transverse intersections. A lens space means $`L(p,q)`$, $`p\ge1`$, $`\gcd(p,q)=1`$, obtained by gluing two solid tori; $`p=1`$ includes $`S^3`$.

The quantifiers cover every knot and every qualifying integer slope, without a genus or tunnel-number restriction. The target is the knot-classification conclusion, without an additional prescribed identification of the filling.

## Application

Dehn surgery is a basic construction of closed three-manifolds. This question asks whether lens-space fillings force an explicit geometric description of the original knot through a genus-two splitting.

## Known progress

The current primary source [1] retains the general conjecture and establishes the genus-at-most-five case. It also records the tunnel-number-one theorem of Li, Moriah and Pinsky. Realizing the same lens space by a Berge knot is a weaker conclusion than identifying the original surgery knot.

## References

1. M. Schmalian and S. Sivek, *Lens space surgeries on knots of small genus*, [arXiv:2609.39260v1](https://arxiv.org/html/2609.39260v1), 30 September 2026, Conjecture 1.1 and its following paragraph, Theorem 1.2.
2. R. İ. Baykur, R. C. Kirby and D. Ruberman (eds.), *K3: A New Problem List in Low-Dimensional Topology*, Mathematical Surveys and Monographs **295**, AMS, 2026, Problem 1.9, [author copy](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf), physical pp. 18–19.
3. T. Li, Y. Moriah and T. Pinsky, *Tunnel number one knots satisfy the Berge conjecture*, *Geometry & Topology* **29**(6) (2025), 3271–3343, [publisher](https://msp.org/gt/2025/29-6/p06.xhtml); restricted-case context as recorded in [1].

## Status review


**Known cases:** September 2026 result verifies Berge for genus <=5; the tunnel-number-one theorem is another restricted case. Lens-space realization and purely cosmetic surgery assertions do not classify all knots admitting an integer lens-space surgery.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked on 25 October 2026 against the primary statement and current version, bounded resolution and announcement searches, all-status AIM/OpenAI statements, and all local findings and admitted pages. No matching complete resolution was located. The purely cosmetic surgery announcement concerns equality of two fillings; it does not classify knots possessing one lens-space filling. The local Stein-fillability question asks about contact structures, while the Reeb-orbit question asks about dynamics.

The source's stronger formulation also describes the pair consisting of knot and surgery slope. This page isolates its knot-classification conclusion and states the integer-slope scope explicitly. The review checks selected primary statements and precise scope; it does not certify the cited proofs or exhaustive literature coverage.


### Online recheck, 2026-10-30

September 2026 result verifies Berge for genus <=5; the tunnel-number-one theorem is another restricted case. Lens-space realization and purely cosmetic surgery assertions do not classify all knots admitting an integer lens-space surgery.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2609.39260); [status source 2](https://doi.org/10.2140/gt.2025.29.3271); [status source 3](https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p03-p.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-1e8f28681c735c13** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
