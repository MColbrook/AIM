# 770. Does the circle minimize the planar Euclidean photon-number integral?

**Area:** Geometric curve functionals and mathematical physics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`C`$ be any smooth, regular, simple closed curve in the Euclidean plane, parameterized by $`x:S^1\to\mathbb R^2`$. For $`t\ne s`$, put $`\Delta=x(t)-x(s)`$ and
```math
v_t^\perp=x'(t)-\frac{x'(t)\cdot\Delta}{|\Delta|^2}\Delta,
 \qquad
 v_s^\perp=x'(s)-\frac{x'(s)\cdot\Delta}{|\Delta|^2}\Delta.
```

The Euclidean photon-number integral of [1, equation (2)] is
```math
n_C=-2\int_{S^1}\!\int_{S^1}
      \frac{v_t^\perp\cdot v_s^\perp}{|x(t)-x(s)|^2}\,dt\,ds.
```

Is $`n_C\geq2\pi^2`$ for every such planar curve $`C`$? The circle has value $`2\pi^2`$ [1].

## Application

This is a shape-minimization question for a conformally invariant nonlocal curve functional. Its answer would identify whether the circle is the universal planar minimizer and clarify the geometric content of an integral originally motivated by radiation calculations. The quantity here is Euclidean; it is not a literal photon count for arbitrary planar motion.

## Known results and scope

For an ellipse with semiaxis ratio $`\xi>0`$, Ruijsenaars and Stodolsky compute $`n_C=(\xi+\xi^{-1})\pi^2`$, which is minimized within ellipses at the circle [1, equation (29)]. Their analysis shows the same functional has **no lower bound** for general curves in ambient dimension greater than two [1, Section 4]. The planar hypothesis in this problem is therefore essential. The source notes that related Möbius curve energies use different regularizations and do not supply this inequality [1, Introduction].

## References

1. S. Ruijsenaars and L. Stodolsky, [*On the Euclidean Version of the Photon Number Integral*](https://arxiv.org/pdf/0710.4276v1), arXiv:0710.4276v1 (2007), equations (2), (29) and the conjecture after (29); published in *Journal of Mathematical Physics* **49** (2008), 023502. [DOI](https://doi.org/10.1063/1.2836411).

## Status review


**Known cases:** The photon-number curve integral is distinct from quantum entropy photon-number inequalities and Mobius knot-energy minima. The original source confirms circles and ellipses but leaves arbitrary smooth planar Jordan curves as the conjecture.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The photon-number curve integral is distinct from quantum entropy photon-number inequalities and Mobius knot-energy minima. The original source confirms circles and ellipses but leaves arbitrary smooth planar Jordan curves as the conjecture.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/0710.4276v1); [comparison source 2](https://doi.org/10.1063/1.2836411). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-source, later-result and duplicate audit](../FURTHER_problems/_tracking/planar-photon-number-circle-minimizer-status-2026-10-21.json) checks the planar scope and distinguishes this integral from nearby knot energies. No complete proof, counterexample or announced settlement was found in bounded searches through 21 October 2026.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0f6a97bb396b7258**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
