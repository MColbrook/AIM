# 769. A planar compact set with full projections and a nowhere dense triple sum

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a compact set $`K\subseteq[0,1]^2`$ such that every affine line $`L\subseteq\mathbb R^2`$ satisfies

```math
L\cap[0,1]^2\ne\varnothing\quad\Longrightarrow\quad L\cap K\ne\varnothing,
```


while

```math
K+K+K=\{x+y+z:x,y,z\in K\}
```


has empty interior in $`\mathbb R^2`$? This sum is compact, so empty interior is equivalent to nowhere density. The incidence condition is equivalent to every orthogonal line projection of $`K`$ being the full corresponding projection of the square.

This is Question 11.3 in the latest arXiv version of [1].

## Application

The question tests how much additive thickness is forced by complete information in every one-dimensional projection. A twofold sum can remain nowhere dense [1]; the planar triple sum is the next unresolved case in that source.

## References

1. R. Balka, M. Elekes, V. Kiss, D. Nagy and M. Poór, *Compact sets with large projections and nowhere dense sumset*, [arXiv:2006.15206v2](https://arxiv.org/abs/2006.15206v2), revised 3 August 2023, Question 11.3, p. 25; Definitions 1.2/1.4, §2, Corollary 7.2 and Theorem 8.1. [Institutional PDF](https://real.mtak.hu/191441/1/2006.15206v2.pdf). Published in *Nonlinearity* **36**(10) (2023), 5190–5215, [DOI](https://doi.org/10.1088/1361-6544/acebae).

## Status review


**Known cases:** The original compact full-projection construction gives a nowhere-dense double sum. The fixed planar triple sum and exact full-square projections are stronger; higher-dimensional lifts and merely nonempty-interior projections do not settle it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The original compact full-projection construction gives a nowhere-dense double sum. The fixed planar triple sum and exact full-square projections are stronger; higher-dimensional lifts and merely nonempty-interior projections do not settle it.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2006.15206v2); [comparison source 2](https://real.mtak.hu/191441/1/2006.15206v2.pdf); [comparison source 3](https://doi.org/10.1088/1361-6544/acebae). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. No matching proof or announced complete solution was found in bounded current searches. The known twofold construction and higher-dimensional lifting do not settle this planar triple-sum target. The source's separate question asking one set to work for every finite number of summands is stronger.

The exact reviewed source is arXiv v2. The original v1 numbers this question 11.2; full published-body parity was not established. The [coordinator review](../FURTHER_problems/_tracking/full-projection-triple-sum-coordinator-review-2026-10-23.json), [independent review](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/balka-triple-sumset-independent-bounded-check-20261023.json) and [all-status duplicate audit](../FURTHER_problems/_tracking/full-projection-triple-sum-all-status-duplicates-2026-10-23.json) record the precise checks and limits. They found no equivalent existing AIM or FURTHER target; visible proof-repository matches concern different convex-body or finite-group questions. These are bounded reviews, not exhaustive absence certificates.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0f5171005aa29e04**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
