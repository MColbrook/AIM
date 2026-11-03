# 909. Can every non-RNP Banach space be renormed so all unit-ball slices have diameter two?

**Area:** Geometry of Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a real Banach space without the Radon–Nikodým property. Does $`X`$ have an equivalent norm $`\|\cdot\|'`$ such that **every slice of its closed unit ball has diameter two** in that norm? For $`x^*\in X^*\setminus\{0\}`$ and $`\varepsilon>0`$, a slice is

```math
S(B',x^*,\varepsilon)=\{x\in B':x^*(x)>\sup_{y\in B'}x^*(y)-\varepsilon\},\qquad B'=\{x:\|x\|'\leq1\}.
```


The assertion is about the existence of *one* equivalent norm for which all slices have diameter exactly $`2`$. It is stronger than known renormings that make slice radii close to $`1`$, and distinct from asking whether slice diameter two implies the diameter-two property for weakly open subsets.

## Application

The Radon–Nikodým property is characterized by dentability, whereas a slice-diameter-two norm places every unit-ball slice at the opposite diameter extreme. A positive answer would characterize failure of the Radon–Nikodým property through an equivalent norm with this uniform slice geometry.

## References

1. M. D. Acosta, J. Becerra-Guerrero and G. López-Pérez, [*Stability Results of Diameter Two Properties*](https://journalofconvexanalysis.com/articles/jca22001/), *J. Convex Anal.* **22** (2015), no. 1, 1–17, explicit question on p. 3. [Primary PDF](https://journalofconvexanalysis.com/articles/jca22001/jca22001.pdf?v=2).
2. G. López-Pérez, E. Martínez Vañó and A. Rueda Zoca, [*Big Weak Open Radius Versus Big Slice Diameter*](https://arxiv.org/html/2510.15461), *Mediterranean Journal of Mathematics* (2026), [DOI 10.1007/s00009-026-03143-x](https://doi.org/10.1007/s00009-026-03143-x), Introduction, which still identifies this exact renorming statement as a conjecture.

## Status review


**Known cases:** The 2026 big-radius paper retains the non-RNP renorming question. Slice radius near one does not give one equivalent norm with every slice of diameter exactly two. The known failure of slice-diameter-two to imply a weak-open-set property addresses another direction.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 big-radius paper retains the non-RNP renorming question. Slice radius near one does not give one equivalent norm with every slice of diameter exactly two. The known failure of slice-diameter-two to imply a weak-open-set property addresses another direction.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded searches through 20 October 2026 found no exact proof, counterexample or public resolution announcement and no matching AIM or admitted FURTHER problem. The separate implication from slice diameter two to diameter two has a known counterexample. See the [primary reading](../FURTHER_problems/_tracking/rnp-slice-diameter-renorming-primary-2026-10-20.json), [later-status check](../FURTHER_problems/_tracking/rnp-slice-diameter-renorming-current-2026-10-20.json), [duplicate review](../FURTHER_problems/_tracking/rnp-slice-diameter-renorming-duplicates-2026-10-20.json) and [decision](../FURTHER_problems/_tracking/rnp-slice-diameter-renorming-coordinator-2026-10-20.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7438221c37fe12f7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
