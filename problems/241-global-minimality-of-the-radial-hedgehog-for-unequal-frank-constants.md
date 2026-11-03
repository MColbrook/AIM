# 241. Global minimality of the radial hedgehog for unequal Frank constants

**Area:** Liquid crystals and the calculus of variations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`B=B_1(0)\subset\mathbb R^3`$, and set
```math
\mathcal A=\{n\in H^1(B;\mathbb S^2):\mathrm{Tr}n(x)=x\text{ on }\partial B\}.
```

For $`a,b>0`$, define
```math
E_{a,b}(n)=\frac12\int_B\left[(\mathrm{div}n)^2
+a(n\cdot\mathrm{curl}n)^2+b|n\times\mathrm{curl}n|^2\right]dx.
```

Determine exactly the set
```math
\mathcal M=\left\{(a,b)\in(0,\infty)^2:
E_{a,b}(n)\ge E_{a,b}(n_*)=8\pi\quad\text{for every }n\in\mathcal A\right\},
\qquad n_*(x)=x/|x|.
```

The value assigned to $`n_*`$ at the origin is immaterial. Competitors have no symmetry or prescribed defect structure. This is the Oseen–Frank problem with $`K_1=1,K_2=a,K_3=b`$; multiplying all three constants by the same positive number does not change minimality. The omitted saddle-splay term is a null Lagrangian with constant integral on this fixed trace class.

It is known that every $`a\ge1,b>0`$ belongs to $`\mathcal M`$, whereas $`8(a-1)+b<0`$ excludes membership. A September 2026 preprint further proves that there is a universal, unspecified $`\delta\in(0,1/8]`$ such that $`1\le a+\delta\min(a,b)`$ implies membership. This is partial progress toward the exact region. The question does not assert that the second-variation inequality $`8(a-1)+b\ge0`$ suffices for global minimality, and it asks for no uniqueness conclusion.

## Application

The radial hedgehog is a basic point-defect configuration in nematic liquid crystals. Its global minimality determines whether a prescribed radial boundary alignment selects this configuration or permits an energetically preferable texture when splay, twist and bend have different costs.

## References

1. J. M. Ball, [Mathematics and liquid crystals](https://arxiv.org/abs/1612.03792), §6.1.1, physical p.23 of v3; published in *Molecular Crystals and Liquid Crystals* 647 (2017), 1–27, [DOI](https://doi.org/10.1080/15421406.2017.1289425).
2. L. Nguyen, [Zero-homogeneous and O(2)-equivariant critical points of the Oseen-Frank energy with multiple Frank constants](https://arxiv.org/abs/2503.22599), Introduction, especially the global/local distinctions and Theorem 1.1.
3. S. Li, [The hedgehog uniquely minimises every p-energy](https://arxiv.org/abs/2609.13979), model and Theorem 1: an isotropic power energy, distinct from the three-constant problem above.
4. Z. Dai, H. Fu, H. Wang and W. Wang, [Boundary regularity for Oseen-Frank minimizers with arbitrary positive splay, twist, and bend constants](https://arxiv.org/abs/2608.22287), §1 and Theorem 1.1: boundary smoothness of an already given global minimizer.
5. P. Bousquet and X. Lamy, [On the minimality of the radial singularity in nematic liquid crystals](https://arxiv.org/abs/2609.36972), Introduction and Theorems 1.1–1.2: the enlarged global regime and a stronger result restricted to competitors continuous away from the origin.

## Status review


**Known cases:** The September Bousquet–Lamy result enlarges a sufficient global regime but retains a gap; its stronger explicit condition restricts competitors. Isotropic p-energies, second-variation stability and boundary regularity do not determine the full two-parameter global-minimality region.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Ball explicitly asks for necessary and sufficient conditions for global minimality with the hedgehog's own boundary values. The 2025 equivariant construction distinguishes global minimization from second-variation stability and minimization within a restricted symmetry class. The September 2026 Bousquet–Lamy preprint explicitly retains a gap after its improved global result; its explicit $`1/8`$ result assumes continuity away from the origin. The inspected power-energy and boundary-regularity theorems do not determine this parameter region.

The cited second-variation results concern local perturbations. The literature review distinguishes them from global minimization over the full Sobolev class.

The pinned Ball preprint has been read completely; full parity with the final 27-page publication remains unverified. Selected independent formulation, semantic and coordinator checks passed. All 186 cached catalogue descriptions returned zero supplied-alias matches. These bounded checks do not prove that no solution exists.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/hedgehog-global-frank-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-hedgehog-global-frank-review.json), [semantic comparison](../FURTHER_problems/_tracking/hedgehog-global-frank-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/hedgehog-global-frank-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/hedgehog-global-frank-coordinator-review-2026-10-19.json) record the scope and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

The September Bousquet–Lamy result enlarges a sufficient global regime but retains a gap; its stronger explicit condition restricts competitors. Isotropic p-energies, second-variation stability and boundary regularity do not determine the full two-parameter global-minimality region.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2609.36972); [status source 2](https://arxiv.org/abs/2503.22599); [status source 3](https://arxiv.org/abs/1612.03792). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-1f3802a7508b4463** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
