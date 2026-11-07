# 690. A Smirnov function without a Hilbert-domain holomorphic extension

**Area:** Infinite-variable complex analysis and function spaces
**Status:** ✅ SOLVED
**Last checked:** 2026-11-07

## Problem statement

Let $`\mathbb T^\infty`$ have normalized product Haar measure $`m`$, and let $`\mathcal P`$ be the analytic polynomials depending on finitely many coordinates. Define $`N_*(\mathbb T^\infty)`$ as the closure of $`\mathcal P`$ for the metric
```math
d_0(f,g)=\int_{\mathbb T^\infty}\log(1+|f-g|)\,dm.
```

For $`q=1,2`$, put $`D_q^\infty=\ell^q(\mathbb C)\cap\mathbb D^\infty`$, with its $`\ell^q`$ topology. Every $`f\in N_*(\mathbb T^\infty)`$ has a canonical holomorphic representative $`F`$ on $`D_1^\infty`$.

Does there exist such an $`f`$ for which there is **no** Fréchet-holomorphic function $`G:D_2^\infty\to\mathbb C`$ satisfying $`G|_{D_1^\infty}=F`$?

## Application

The question determines the natural domain of holomorphy of the logarithmic closure of infinite-variable Hardy spaces. Every function in $`H^p(\mathbb T^\infty)`$, for each $`p>0`$, extends to $`D_2^\infty`$; the issue is whether logarithmic integrability allows a genuinely smaller extension domain.

## References

Kunyu Guo, Jiaqi Ni and Qi Zhou, *Nevanlinna class, Dirichlet series and Szegő’s problem*, Annales de l’Institut Fourier **75** (2025), 1603–1647, [Question 2.28 and Theorem 2.27](https://aif.centre-mersenne.org/articles/10.5802/aif.3696/), printed pp.1627–1628. Final published source pinned and fully read; first arXiv submission 6 January 2022, latest preprint revision 1 June 2022.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/690-a-smirnov-function-without-a-hilbert-domain-holomorphic/main.pdf). Every stated Smirnov function extends holomorphically to the Hilbert polydisc; no proposed nonextendible example exists.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/690-review.md) checks the complete argument against this exact target and records the primary-source comparisons. No unresolved mathematical gap was identified in the complete resolution. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



### Online recheck, 2026-10-30

The target is extension from the infinite-dimensional Smirnov class to the Hilbert polydisc. Hardy-class extension and unrelated one-variable or vector-measure results do not answer the published Question 2.28. No matching later complete announcement was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The final 2025 source explicitly asks this question. Its Hardy-space extension theorem and Corollary 2.29 do not imply that every Smirnov function belongs to some Hardy space. Polynomial density in the logarithmic metric establishes the canonical extension on $`D_1^\infty`$, without establishing extension on $`D_2^\infty`$.

Bounded current searches through 18 October 2026 found no matching complete announcement. Selected 2026 work on composition operators and the Nevanlinna class of Dirichlet series concerns different classes and does not state this extension conclusion in the inspected passages. Selected independent formulation, semantic and coordinator checks passed. All 186 cached catalogue descriptions returned zero supplied-alias matches. These bounded checks do not prove that no solution exists.

The [primary review](../FURTHER_problems/_tracking/parallel/complex-bayesian/smirnov-hilbert-extension-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-smirnov-hilbert-extension-review.json), [semantic comparison](../FURTHER_problems/_tracking/smirnov-hilbert-extension-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/smirnov-hilbert-extension-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/smirnov-hilbert-extension-coordinator-review-2026-10-18.json) record the scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-57dc9c6d27bf78a5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
