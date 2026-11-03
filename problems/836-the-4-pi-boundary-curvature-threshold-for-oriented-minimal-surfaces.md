# 836. The $`4\pi`$ boundary-curvature threshold for oriented minimal surfaces

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Gamma\subset\mathbb R^3`$ be a smooth, simple closed curve with total *boundary-curve* curvature
```math
\mathrm{tc}(\Gamma)=\int_\Gamma |\kappa|\,ds\leq4\pi.
```

Must every smooth, compact, oriented minimal surface spanning $`\Gamma`$ be a disk? Equivalently, if such a curve bounds an oriented minimal surface that is not a disk, must $`\mathrm{tc}(\Gamma)>4\pi`$? The orientability condition matters: curves of total curvature below $`4\pi`$ can bound minimal Möbius strips.

Brian White proves the disk conclusion for $`\mathrm{tc}(\Gamma)\leq 2\pi\sqrt{2\pi/e}`$, approximately $`1.014\cdot3\pi`$, and conjectures the sharp $`4\pi`$ threshold for oriented surfaces. Curves of curvature less than $`4\pi+\varepsilon`$ can bound oriented embedded minimal surfaces of arbitrarily high genus, so the proposed constant cannot be raised.

## Application

The conjecture asks how much bending of a single boundary curve is needed before an oriented spanning minimal surface can acquire positive genus. A sharp answer would connect curve geometry with topology in the Plateau problem.

## References

1. Brian White, [*Boundary singularities in mean curvature flow and total curvature of minimal surface boundaries*](https://doi.org/10.4171/CMH/542), *Commentarii Mathematici Helvetici* **97** (2022), 669–689, Theorem 19 and following conjecture on p. 683; [published PDF](https://ems.press/content/serial-article-files/43576).
2. Otis Chodosh, [*Introduction to minimal surfaces*](https://web.stanford.edu/~ochodosh/Math286-min-surf.pdf), Stanford Math 286 lecture notes (updated 15 September 2025), §11, Theorem 11.5 and Open Question 2 on p. 34. This later source explicitly keeps the oriented $`4\pi`$ question open.

## Status review


**Known cases:** White improves the disk threshold beyond three pi, but not to four pi. Embeddedness at total boundary curvature at most four pi is not a disk-topology theorem. Nonorientable Mobius-strip examples do not refute the oriented target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

White improves the disk threshold beyond three pi, but not to four pi. Embeddedness at total boundary curvature at most four pi is not a disk-topology theorem. Nonorientable Mobius-strip examples do not refute the oriented target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

White's result is a strict improvement over $`3\pi`$, but it does not reach $`4\pi`$. The Ekholm–White–Wienholtz embeddedness theorem for a spanning minimal immersion at curvature at most $`4\pi`$ does not force its topology to be a disk. The Möbius-strip examples are nonorientable and therefore do not refute the stated question. Targeted AIM/FURTHER duplicate and current-resolution searches on 21 October 2026 found no matching complete announcement. This is a bounded live-status assessment, not a proof of unsolvedness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-bc3f9bee6a33f2bf**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
