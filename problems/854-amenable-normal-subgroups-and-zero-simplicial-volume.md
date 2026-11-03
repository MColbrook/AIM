# 854. Amenable normal subgroups and zero simplicial volume

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq1`$ and let $`M`$ be a connected, oriented, closed topological $`n`$-manifold whose universal cover is contractible. Suppose its fundamental group $`\Gamma=\pi_1(M)`$ contains an infinite amenable normal subgroup $`A\trianglelefteq\Gamma`$.

Amenability means that there is a positive linear functional $`m:\ell^\infty(A)\to\mathbb R`$ with $`m(1)=1`$ that is invariant under left translations of $`A`$.

Must the **real simplicial volume** vanish?

```math
\|M\|=\inf\left\{\sum_{j=1}^{k}|a_j|:\ \sum_{j=1}^{k}a_j\sigma_j
\text{ represents }[M]_{\mathbb R}\right\}=0.
```

The chains are finite real singular cycles. No affine structure, completeness, finite generation of $`A`$, residual finiteness of $`\Gamma`$ or cohomological-dimension restriction on $`\Gamma/A`$ is assumed. The whole group $`\Gamma`$ need not be amenable, and $`A`$ need not lie in its centre.

## Application

This asks whether an amenable direction in the topology of a closed aspherical manifold forces its fundamental class to have zero real homological norm. It would extend known vanishing theorems beyond fibrations with amenable fibres and geometric decompositions. 

## References

1. M. Bucher, C. Connell and J.-F. Lafont, *Vanishing simplicial volume for certain affine manifolds*, Proceedings of the American Mathematical Society **146** (2018), 1287–1294, question at the beginning of§2, p.1289; Lemma2.1 and Theorem2.2. [Published article](https://people.math.osu.edu/lafont.1/Bucher-Connell-Lafont-PAMS.pdf), [DOI](https://doi.org/10.1090/proc/13799).
2. A. Casali and M. Moraschini, *Topological volumes of certain complete affine manifolds*, [arXiv:2502.06303v1](https://arxiv.org/abs/2502.06303v1), Question1.5, Corollary1.4 and§6. The original question is attributed there and in[1] to Lück, Question14.39 of his2002book.
3. F. Sarti, *Simplicial volume via foliated simplices and duality*, [arXiv:2506.02962v2](https://arxiv.org/abs/2506.02962v2), Corollaries4–5 and Question6.

## Status review


**Known cases:** The complete-affine vanishing theorem imposes an affine structure. General measurable-action and quotient-cohomology criteria are sufficient conditions, without constructing them for every infinite amenable normal subgroup. No unrestricted aspherical-manifold resolution was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The complete-affine vanishing theorem imposes an affine structure. General measurable-action and quotient-cohomology criteria are sufficient conditions, without constructing them for every infinite amenable normal subgroup. No unrestricted aspherical-manifold resolution was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The complete published source[1] was read, including its diagrams. Its vanishing criterion requires an additional condition on the top-dimensional cohomology map of the quotient, or the specific hypotheses of Theorem2.2. The current result[2] assumes a complete affine structure. Its§6 explicitly retains the general question.

The measurable bounded-cohomology criteria[3] require a suitable action with vanishing cohomology; their existence for every manifold in this target is still posed as Question6. A sufficient criterion is not a construction of that action for every amenable normal subgroup.

The affine-manifold vanishing question has a different hypothesis: general affine manifolds need not satisfy this target's asphericity and amenable-normal-subgroup assumptions, while the present question does not assume any affine atlas. The AIM centre-rank motion-planning formula is also a different target. The independent selected-primary audit and the scoped catalogue comparison passed.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/lueck-amenable-normal-volume-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-lueck-amenable-normal-volume-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/lmr-all-target-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/gromov-lueck-prove2-0147-review.json) and [coordinator review](../FURTHER_problems/_tracking/lueck-amenable-normal-volume-coordinator-review-2026-10-17.json) record exact hypotheses and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e0695418dea8008b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
