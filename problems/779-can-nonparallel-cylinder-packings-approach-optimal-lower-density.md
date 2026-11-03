# 779. Can nonparallel cylinder packings approach optimal lower density?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathfrak C`$ be the class of countably infinite families $`\mathcal C=\{C_i\}`$ of solid infinite circular cylinders of radius 1 in $`\mathbb R^3`$. Their interiors must be pairwise disjoint, and no two axes may be parallel. Define the lower density by
```math
\delta^-(\mathcal C)=\liminf_{R\to\infty}
 \frac{\mathrm{Vol}(B_R(0)\cap\bigcup_i C_i)}
      {\mathrm{Vol}(B_R(0))}.
```

Is
```math
\sup_{\mathcal C\in\mathfrak C}\delta^-(\mathcal C)
 =\frac{\pi}{\sqrt{12}}?
```

Equivalently, can the lower density exceed $`\pi/\sqrt{12}-\varepsilon`$ for every $`\varepsilon>0`$? Attainment by one packing is not required.

## Application

This measures how efficiently nonparallel straight tubes can fill three-dimensional space at every sufficiently large scale about a fixed center.

## References

- D. Ismailescu and P. Laskawiec, *Dense packings with nonparallel cylinders*, **Elemente der Mathematik** 74(3) (2019), 89–103. [Published article](https://doi.org/10.4171/EM/387); [author preprint](https://arxiv.org/html/1809.10721v1), §4, preprint pp. 12–13.
- O. Eliyahu, *On non-parallel cylinder packings*, [arXiv:2310.06943v1](https://arxiv.org/html/2310.06943v1), introduction, Theorem 2.2, Corollary 3.9 and §4.

## Status review


**Known cases:** The current Eliyahu theorem obtains optimal upper density but only lower density close to pi/6. A limsup construction does not give a liminf near pi/sqrt(12), and the bounded-holes target is separate.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current Eliyahu theorem obtains optimal upper density but only lower density close to pi/6. A limsup construction does not give a liminf near pi/sqrt(12), and the bounded-holes target is separate.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/EM/387); [comparison source 2](https://arxiv.org/html/1809.10721v1); [comparison source 3](https://arxiv.org/html/2310.06943v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. Eliyahu establishes a packing attaining **upper** density $`\pi/\sqrt{12}`$, and packings with lower density at least $`\pi/6-\varepsilon`$. The lower-density optimum remains an explicit question in §4. The universal upper-density bound also bounds the lower density.

Current searches found no matching complete resolution or announcement. Semantic comparisons distinguished finite cylinder coverings, finite-field cylinder structure and cylinder-contact problems. No equivalent AIM or developing-list entry was located. This is a dated, bounded check.

The separate [bounded-holes question](../cut_problems/FURTHER_problems/geometry-topology/lead-64461deeeb0a7c4c.md) concerns uniform coverage over all centers.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-3138cdf543b2c1a5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
