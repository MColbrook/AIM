# 925. Does the infinite-variable Hardy space have a Schauder basis?

**Area:** Function spaces, harmonic analysis and Dirichlet series
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\{z\in\mathbb C:|z|=1\}`$, and equip $`\mathbb T^{\mathbb N}`$ with normalized product Haar measure $`m`$. Define the complex Banach space
```math
H^1(\mathbb T^{\mathbb N})
 =\overline{\left\{\sum_{\nu\in A}a_\nu z^\nu:
 A\subset\mathbb N_0^{(\mathbb N)}\text{ finite},\ a_\nu\in\mathbb C\right\}}^{\,L^1(m)},
```

where each multi-index $`\nu`$ has finite support and $`z^\nu=\prod_jz_j^{\nu_j}`$.

Does there exist a sequence $`(e_j)_{j\ge1}`$ in this space such that every $`F\in H^1(\mathbb T^{\mathbb N})`$ has a unique scalar sequence $`(a_j)`$ satisfying
```math
\lim_{N\to\infty}\left\|F-\sum_{j=1}^{N}a_je_j\right\|_{L^1(m)}=0?
```


The basis vectors may be arbitrary elements of the space. Unconditional convergence is not required.

## Application

The question asks whether all analytic functions in this infinite-variable space can share one ordered system of unique, norm-convergent expansions. Through the Bohr correspondence it is also a question about representing Dirichlet series in their mean absolute-value norm. Such a basis would provide convergent linear truncations without requiring the canonical Dirichlet monomials to serve as basis vectors.

## References

1. E. Saksman and K. Seip, *Some open questions in analysis for Dirichlet series*, [arXiv:1601.01616v1](https://arxiv.org/abs/1601.01616v1), physical pp.2–4, Problem 2.6 (first question); published in Contemporary Mathematics **679** (2016), 179–191, [doi:10.1090/conm/679/13675](https://doi.org/10.1090/conm/679/13675).
2. A. Aleman, J.-F. Olsen and E. Saksman, *Fourier multipliers for Hardy spaces of Dirichlet series*, [arXiv:1210.4292](https://arxiv.org/abs/1210.4292), Section 3, Corollary 4 and Question 1.
3. D. Carando, S. Lassalle and L. Milne, *The fundamental functions of the canonical basis of Hardy spaces of Dirichlet series*, [arXiv:2406.03623v1](https://arxiv.org/abs/2406.03623v1), definitions, Remark 1.2 and Proposition 4.1; [published 2025 version](https://doi.org/10.1007/s00041-025-10191-6).

## Status review


**Known cases:** Any Schauder basis in infinite-variable H1 is requested. Finite-variable, p>1, Markushevich and Frechet-space basis results have different conclusions. No matching general endpoint announcement found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Any Schauder basis in infinite-variable H1 is requested. Finite-variable, p>1, Markushevich and Frechet-space basis results have different conclusions. No matching general endpoint announcement found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 18 October 2026. The 2016 survey and the earlier Question 1 explicitly ask for any Schauder basis. The Bohr correspondence is an isometry, so the formulation above preserves that question. Known results for the canonical monomials when $`1<p<\infty`$, and Markushevich bases at $`p=1`$, do not supply an arbitrary Schauder basis. A basis of a translated Fréchet space concerns a different topology; recent bases made of finite Blaschke products concern one complex variable and prescribed basis vectors.

Selected current-source, semantic, independent and catalogue checks found no matching full resolution. All 186 cached catalogue descriptions returned zero supplied-alias matches. This is a bounded literature check, not proof that no solution exists. Comparisons with the original published bodies and the 2025 subscription article remain access gaps; no certification of all proofs is claimed.

The [primary review](../FURTHER_problems/_tracking/parallel/complex-bayesian/dirichlet-h1-schauder-basis-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-dirichlet-h1-schauder-basis-review.json), [semantic comparison](../FURTHER_problems/_tracking/dirichlet-h1-basis-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/dirichlet-h1-basis-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/dirichlet-h1-basis-coordinator-review-2026-10-18.json) record the scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c213c89642744611**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
