# 900. An infinite-dimensional complex reflexive space with numerical index one

**Area:** Geometry of Banach spaces / bounded linear operators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a complex Banach space $`X`$, write $`S_X=\{x\in X:\|x\|=1\}`$ and let $`X^*`$ be its continuous complex-linear dual. For a bounded complex-linear operator $`T:X\to X`$, define

```math
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\},\qquad
n(X)=\inf_{\|T\|=1}v(T).
```

Does there exist an **infinite-dimensional reflexive complex Banach space** $`X`$ such that $`n(X)=1`$? Equivalently, can such a space satisfy $`v(T)=\|T\|`$ for every bounded complex-linear operator $`T:X\to X`$?

Here reflexivity means that the canonical map $`X\to X^{**}`$ is onto. The question is existential: no particular underlying space or equivalent norm is prescribed. This is equivalent to the renorming formulation of Problem 17 in [1], because an equivalent complex norm preserves reflexivity and infinite dimension.

## Application

The numerical index measures how much operator norm can be recovered from values observed by norming functionals. The question asks whether exact recovery for every bounded operator can coexist with weak compactness of the unit ball in an infinite-dimensional space.

## References

1. V. Kadets, M. Martín and R. Payá, [*Recent progress and open questions on the numerical index of Banach spaces*](https://rac.es/ficheros/doc/01118.pdf), RACSAM **100**(1–2) (2006), 155–182, definitions pp155–156, §4, Problem 17 p167. Eligible preprint: [math/0605781](https://arxiv.org/abs/math/0605781).
2. M. S. Moslehian, G. A. Muñoz-Fernández, A. M. Peralta and J. B. Seoane-Sepúlveda, [*Similarities and differences between real and complex Banach spaces: an overview and recent developments*](https://doi.org/10.1007/s13398-022-01222-8), RACSAM **116**, 88 (2022), Theorem 6.29 and the following paragraph.
3. S. Dantas, H. del Río and T. Raunig, [*A group action approach to the Daugavet property*](https://arxiv.org/abs/2606.20429), preprint, v1 (2026), §5.3, especially its opening paragraph and Corollary 5.20. This concerns a related alternative-Daugavet formulation; general group-action examples use a different numerical index.
4. S. Pal, S. Roy and D. Sain, [*A characterization of Banach spaces with numerical index one*](https://arxiv.org/abs/2604.03690), preprint v1 (2026), Proposition 2.9, the following paragraph and Theorem 2.10.

## Status review


**Known cases:** The 2026 numerical-index characterization and group-action paper retain the complex reflexive existence question. Real-space impossibility does not settle the complex case; group-action numerical indices and approximate renorming values do not construct a complex reflexive space attaining index one.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 numerical-index characterization and group-action paper retain the complex reflexive existence question. Real-space impossibility does not settle the complex case; group-action numerical indices and approximate renorming values do not construct a complex reflexive space attaining index one.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 18 October 2026. The real reflexive analogue is impossible in infinite dimension. The complex problem is explicitly retained in [2] and in the paragraph preceding the main characterization in [4]; [3] also retains the related complex reflexive alternative-Daugavet existence question. General group-action numerical indices and numerical ranges of antilinear operators change the operator class or defining supremum. Neither supplies the requested space. Approaching numerical index one by equivalent norms does not establish that one is attained.

The published 2006 question and all its surrounding hypotheses were read directly. The final article's 28 pages, 84 references and four figures were reviewed. The later sources were read in the selected sections cited above; their complete proofs and edition parity are not certified. Catalogue and independent admission checks are recorded separately.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/numerical-index-complex-reflexive-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-numerical-index-complex-reflexive-review.json), [semantic comparison](../FURTHER_problems/_tracking/complex-reflexive-numerical-index-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/complex-reflexive-numerical-index-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/complex-reflexive-numerical-index-coordinator-review-2026-10-18.json) record the evidence and its limits. These AI checks do not assert human peer review or exhaustive verification of later proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-45613a837b829e12**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
