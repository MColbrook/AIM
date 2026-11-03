# 857. Uniqueness of the critical Möbius band at Morse index five

**Area:** Minimal surfaces and geometric variational problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Sigma\subset\overline{B^4}`$ be a smooth compact connected properly embedded nonorientable surface with nonempty boundary. Assume that $`\Sigma`$ is minimal, its interior lies in $`B^4`$, and it meets $`S^3`$ orthogonally along its boundary. Suppose its **area Morse index** is five: the maximal dimension of a space of normal variations on which the area second variation is negative definite, with the varied boundary constrained to $`S^3`$, is five.

Must $`\Sigma`$ be an $`O(4)`$ image of the critical Möbius band?

For a concrete normalization, this band is the image of
```math
F(t,\theta)=\frac1{\sqrt6}\bigl(2\sinh t\cos\theta,\;2\sinh t\sin\theta,
\cosh(2t)\cos(2\theta),\;\cosh(2t)\sin(2\theta)\bigr),
```

where $`|t|\le T=\mathrm{arctanh}(1/\sqrt3)`$, $`\theta\in\mathbb R/(2\pi\mathbb Z)`$, and $`(t,\theta)\sim(-t,\theta+\pi)`$.

This is the compact connected smooth formulation of Medvedev's Conjecture1.3. It imposes neither rotational symmetry nor a first-Steklov-eigenfunction condition. The index is for all normal area variations, rather than the energy, spectral or symmetry-restricted index.

## Application

The question classifies stationary area configurations with exactly five unstable directions under a spherical free-boundary constraint. It is a benchmark connecting geometric variational problems and boundary spectral methods.

## References

1. Vladimir Medvedev, *On the Index of the Critical Möbius Band in B4*, Journal of Geometric Analysis **33** (2023),93, [published article](https://doi.org/10.1007/s12220-022-01069-w); [arXiv:2112.04883v2](https://arxiv.org/abs/2112.04883v2), Conjecture1.3 and §2, native pp.3,5–6.
2. Ailana Fraser and Richard Schoen, *Sharp eigenvalue bounds and minimal surfaces in the ball*, Inventiones Mathematicae **203** (2016),823–890, [published article](https://doi.org/10.1007/s00222-015-0604-x); [author version](https://arxiv.org/abs/1209.3789), Proposition7.1 and Theorem7.4.
3. Otis Chodosh and Matilde Gianocca, *Free boundary minimal surfaces of genus zero*, [arXiv:2609.13054v1](https://arxiv.org/abs/2609.13054v1), Theorem1.1 and Corollary1.2. These concern the three-dimensional ball.

## Status review


**Known cases:** The index-five computation does not identify every index-five surface. First-Steklov-coordinate, rotational-symmetry and local-uniqueness results add hypotheses. The genus-zero critical-catenoid announcement concerns B3, not nonorientable codimension-two surfaces in B4.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The index-five computation does not identify every index-five surface. First-Steklov-coordinate, rotational-symmetry and local-uniqueness results add hypotheses. The genus-zero critical-catenoid announcement concerns B3, not nonorientable codimension-two surfaces in B4.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Medvedev computes the critical example's index and separately conjectures uniqueness. Fraser–Schoen's Möbius-band rigidity requires a specified topology and first Steklov coordinate eigenfunctions; index five alone has not supplied those hypotheses in the inspected results. Recent spherical-cap results also impose different assumptions. The September2026 catenoid uniqueness announcement concerns surfaces in $`B^3`$, rather than nonorientable surfaces of codimension two in $`B^4`$.

The displayed factor $`1/\sqrt6`$ ensures a unit-ball normalization. The inspected native Medvedev formula omits this radius factor; Fraser–Schoen explicitly rescale their construction. The independent audit checks that the normalized boundary has radius one and outward conormal $`F`$. Compactness and connectedness are explicit here; those adjectives are not explicit in the source's conjecture sentence.

Bounded current searches located no matching complete solution or announcement. AIM108/109, the closest FURTHER entries and all seven returned cached website passages concern different targets. The [coordinator review](../FURTHER_problems/_tracking/critical-mobius-index5-coordinator-review-2026-10-19.json), [current checks](../FURTHER_problems/_tracking/critical-mobius-index5-current-review-2026-10-19.json), [duplicate comparison](../FURTHER_problems/_tracking/critical-mobius-index5-duplicates-review-2026-10-19.json) and [independent native-source audit](../FURTHER_problems/_tracking/parallel/rough-filtering/critical-mobius-index5-independent-audit.json) record precise reading and verification limits. These checks do not establish an exhaustive absence of resolutions.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e5a73329dded1fbf**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
