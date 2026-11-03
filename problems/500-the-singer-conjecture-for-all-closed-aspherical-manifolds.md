# 500. The Singer conjecture for all closed aspherical manifolds

**Area:** Geometric topology, spectral geometry and $`L^2`$-invariants
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a closed connected aspherical topological manifold of real dimension $`n\ge1`$. Thus $`M`$ is compact without boundary and its universal cover $`\widetilde M`$ is contractible. Put $`\Gamma=\pi_1(M)`$.

Write $`b_p^{(2)}(\widetilde M;\Gamma)`$ for the complex $`L^2`$-Betti numbers: the group von Neumann dimensions of reduced $`\ell^2`$-homology of the universal cover, computed using a finite CW model of $`M`$.

Must
```math
b_p^{(2)}(\widetilde M;\Gamma)=0
\qquad\text{for every integer }p\ge0\text{ with }2p\ne n\,?
```

For odd $`n`$, this asserts vanishing in every degree. The question includes manifolds without an orientability or curvature assumption.

## Application

The conjecture predicts concentration of square-integrable homology in a single possible degree. For $`n=2m`$, the $`L^2`$-Euler characteristic identity would then give the Hopf sign inequality $`(-1)^m\chi(M)\ge0`$.

## Known progress

Reference [1], Theorem 1.14, proves the conjecture for poly-surface fundamental groups and gives a bundle permanence result. Reference [2], Theorem 1.3, covers smooth projective varieties with semismall Albanese map and residually finite fundamental group.

OpenAI's release [3] announces the full four-dimensional case, including topological and nonorientable manifolds. This is partial progress on the all-dimensional target. The general odd-dimensional statement and unrestricted higher dimensions are not covered by that announcement.

## References

1. R. Sauer and A. Thom, *A spectral sequence to compute $`L^2`$-Betti numbers of groups and groupoids*, [arXiv:0707.0906v3](https://arxiv.org/html/0707.0906v3), Section 1.2 and Theorems 1.14--1.15. [Version record](https://arxiv.org/abs/0707.0906).
2. L. F. Di Cerbo and L. Lombardi, *Singer conjecture for varieties with semismall Albanese map and residually finite fundamental group*, Proceedings of the Royal Society of Edinburgh Section A **156** (2026), 122--128, [doi:10.1017/prm.2024.52](https://doi.org/10.1017/prm.2024.52), Conjecture 1.1 and Theorems 1.3--1.4.
3. OpenAI, *The Singer conjecture in dimension four*, September 2026; [official release overview, entry 315](https://github.com/openai/math/blob/main/overview.tex) and [linked manuscript](https://github.com/openai/math/blob/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf). Announcement scope reviewed; the full proof was not independently checked.

## Status review


**Known cases:** The official September announcement is restricted to formal dimension four. The general all-dimensional topological-manifold Singer statement remains beyond that theorem and the 2026 semismall-Albanese cases.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The coordinator read the original general statement, its latest v3 formulation and the precise scope of the 2026 projective result. Current and announced-resolution searches on 25 October 2026 located no matching all-dimensional resolution. The dimension-four announcement is retained explicitly above.

Comparison covered all 1,703 pinned AIM/OpenAI statements and all 907 preceding local findings. Motion-planning questions, Euler-parity examples and vanishing simplicial-volume conjectures have different conclusions or additional hypotheses. No equivalent general target was located. These dated checks do not certify the cited proofs or establish exhaustive literature coverage.


### Online recheck, 2026-10-30

The official September announcement is restricted to formal dimension four. The general all-dimensional topological-manifold Singer statement remains beyond that theorem and the 2026 semismall-Albanese cases.

Comparators and current-status sources: [status source 1](https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026); [status source 2](https://doi.org/10.1017/prm.2024.52). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-0261c956264167e5** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
