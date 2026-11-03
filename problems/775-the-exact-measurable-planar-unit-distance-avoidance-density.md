# 775. The exact measurable planar unit-distance-avoidance density

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a Lebesgue-measurable set $`A\subset\mathbb R^2`$ having no two points at Euclidean distance exactly $`1`$, set
```math
\overline\delta(A)=\limsup_{R\to\infty}\frac{|A\cap B(0,R)|}{\pi R^2},
\qquad m_1(\mathbb R^2)=\sup_A\overline\delta(A).
```

**Determine $`m_1(\mathbb R^2)`$ exactly.** In particular, is it equal to Croft's optimized periodic tortoise density
```math
\delta_C=\max_{\sqrt3/2\le h\le1}
\frac{\pi-6\arccos h+6h\sqrt{1-h^2}}{2\sqrt3(1+h)^2}
\approx0.2293647316?
```

A tortoise is an open radius-$`1/2`$ disc intersected with an aligned open regular hexagon of height $`h`$, repeated on a triangular lattice of spacing $`1+h`$. The formula is its area divided by lattice-cell area.

## Application

This continuous extremal problem asks how much of the plane a measurable region can occupy while excluding one prescribed separation. It connects measurable geometry, harmonic analysis and convex optimization.

## References

- E. DeCorte, F. M. de Oliveira Filho and F. Vallentin, *Complete positivity and distance-avoiding sets*, [original 2018 primary](https://arxiv.org/pdf/1804.09099v1), Problem (P2) and planar discussion; [latest v4](https://arxiv.org/html/1804.09099v4).
- G. Ambrus, A. Csiszárik, M. Matolcsi, D. Varga and P. Zsámboki, *The density of planar sets avoiding unit distances*, Math. Program. **207** (2024), 303-327, [DOI](https://doi.org/10.1007/s10107-023-02012-9), [primary v3](https://arxiv.org/html/2207.14179v3), definition (1), Croft construction and Theorem 1.
- Á. Dúcz and D. Varga, *A unit-distance graph in the plane with independence ratio below 1/4* (2026), [primary](https://arxiv.org/html/2606.28157v1), Section 2.1, Conjecture 1.
- S. Li and Y. Su, *Every n points in the plane contain (m1+o(1))n points with no unit distance* (2026), [primary](https://arxiv.org/html/2610.15424v1), Theorem 1.1 and the paragraph after Corollary 1.2.

## Status review


**Known cases:** The exact measurable avoidance density is distinct from finite unit-distance edge counts and chromatic numbers. The October independence-ratio transfer leaves its numeric value open, and the strict-quarter result and double-cap announcement do not identify the Croft optimum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact measurable avoidance density is distinct from finite unit-distance edge counts and chromatic numbers. The October independence-ratio transfer leaves its numeric value open, and the strict-quarter result and double-cap announcement do not identify the Croft optimum.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1804.09099v1); [comparison source 2](https://arxiv.org/html/1804.09099v4); [comparison source 3](https://doi.org/10.1007/s10107-023-02012-9); [comparison source 4](https://arxiv.org/html/2207.14179v3); [comparison source 5](https://arxiv.org/html/2606.28157v1); [comparison source 6](https://arxiv.org/html/2610.15424v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Partial progress; checked 28 October 2026.** The bounds are $`\delta_C\le m_1(\mathbb R^2)\le0.2470`$. The strict-quarter question is already solved. The October 2026 transfer theorem equates this density with a limiting finite independence ratio and explicitly leaves its numerical value open. No matching later resolution or AIM/private duplicate was found.

The exact-density question predates the cutoff; later Croft-equality statements supply a sharper candidate. Finite incidence bounds and coloring results do not evaluate this density. The separate double-cap conjecture has a matching announced solution and is excluded.

Review evidence: [owner](../FURTHER_problems/_tracking/B-C227-180409099-doublecap-density-scientific-gates-20261028/SCIENTIFIC-REVIEW.json), [full public comparison](../FURTHER_problems/_tracking/B-C227-180409099-doublecap-density-scientific-gates-20261028/ROOT-FULL1704-PUBLIC-AND-NEW-PRIVATE-SEMANTIC-SUPPLEMENT.json), [coordinating review](../FURTHER_problems/_tracking/B-C227-180409099-doublecap-density-scientific-gates-20261028/ROOT-EXACT-CONTINUOUS-DENSITY-PRIMARY-CROFT-GEOMETRY-AND-SCOPED-EXCLUSIONS-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2c3c2e1ff07f2a96**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
