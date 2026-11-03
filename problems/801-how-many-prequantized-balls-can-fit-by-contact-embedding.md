# 801. How many prequantized balls can fit by contact embedding?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge1`$ and let $`X=\mathbb R^{2n}\times S^1`$ carry the standard contact structure
```math
\ker\!\left(dz+\frac12\sum_{j=1}^{n}(x_j\,dy_j-y_j\,dx_j)\right).
```

For the Euclidean ball $`B^{2n}(a)\subset\mathbb R^{2n}`$, write $`\widehat B^{2n}(a)=B^{2n}(a)\times S^1`$. Fix radii with $`\pi R^2>\pi r^2>1`$. Is there a finite maximum $`k`$ for which the disjoint union of $`k`$ copies of $`\widehat B^{2n}(r)`$ admits a contact embedding into $`\widehat B^{2n}(R)`$? If so, what is that maximum as a function of $`n,r,R`$?

Here “contact embedding” follows the source's convention: a contact isotopy beginning with inclusion moves the union into the target. The source poses this as Problem 258*. Its symplectic analogue has packing and volume constraints, but those results do not determine the contact answer.

## Application

This asks whether contact geometry imposes a finite packing capacity on large prequantized balls. The answer would clarify which symplectic packing obstructions persist after passing to the contact product with a circle.

## References

1. Y. Eliashberg, “Embeddings of contact domains,” in M. T. Rassias, [*Solved and unsolved problems*](https://euromathsoc.org/magazine/articles/78), *European Mathematical Society Magazine* **123** (2022), 57–66, §II, Problem 258*; [DOI 10.4171/MAG/78](https://doi.org/10.4171/MAG/78). Gives the definitions and poses the exact question.
2. Y. Eliashberg, S. S. Kim and L. Polterovich, [*Geometry of contact transformations and domains: orderability versus squeezing*](https://arxiv.org/abs/math/0511658), *Geometry & Topology* **10** (2006), 1635–1747. Background single-domain contact squeezing obstructions cited by the source.
3. S.-F. Chiu, [*Nonsqueezing property of contact balls*](https://arxiv.org/abs/1405.1178), *Duke Mathematical Journal* **166** (2017), 605–655. Single-ball non-squeezing, distinct from the packing of several balls.

## Status review


**Known cases:** Contact nonsqueezing of a single prequantized ball and ordinary symplectic volume packing do not establish a finite bound for arbitrarily many contact-embedded balls in the stated greater-than-one regime. The exact EMS problem remains unmatched.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Contact nonsqueezing of a single prequantized ball and ordinary symplectic volume packing do not establish a finite bound for arbitrarily many contact-embedded balls in the stated greater-than-one regime. The exact EMS problem remains unmatched.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Eliashberg described this contact packing question as open in 2022. Bounded searches through 22 October 2026 found no later primary result or announced solution answering the finite-maximum question. The cited single-ball contact non-squeezing results and later symplectic packing work address different statements. A text search of the local AIM problem list and this category found no matching problem. This is a literature search result, not a proof of openness; the [dated audit](../FURTHER_problems/_tracking/j308-contact-packing-258-status-2026-10-22.json) records its limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-77384f76b1d6cfbb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
