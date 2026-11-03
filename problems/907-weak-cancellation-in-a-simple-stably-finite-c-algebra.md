# 907. Weak cancellation in a simple stably finite C*-algebra

**Area:** Operator algebras
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a simple, unital, stably finite complex $`C^*`$-algebra $`A`$ and $`x,y,z\in\mathrm{Cu}(A)`$ such that

```math
x+z\ll y+z,\qquad x\not\ll y?
```


Here simplicity excludes nontrivial closed two-sided ideals. Stable finiteness means that every isometry in every matrix algebra $`M_n(A)`$ is unitary. Let $`\mathcal K`$ be the compact operators on a separable infinite-dimensional complex Hilbert space. The ordinary Cuntz semigroup uses positive elements of the spatial stabilization $`A\otimes\mathcal K`$: $`a\precsim b`$ when $`r_nbr_n^*\to a`$ in norm for a sequence $`r_n\in A\otimes\mathcal K`$. Quotient by mutual subequivalence, order by $`\precsim`$, and add by block sum. The relation $`x\ll y`$ means that every increasing sequence whose supremum dominates $`y`$ has a term dominating $`x`$.

No separability, nuclearity, exactness or comparison hypothesis is imposed.

## Application

The question tests cancellation of positive-operator comparison under finiteness and simplicity.

## Known progress

Stable rank one guarantees weak cancellation [1, Theorem 10.3], so an example must lie beyond that case. Familiar failures from infinite algebras or nonsimple cones do not meet the stated hypotheses.

Recent rank approximation [2, Theorem A] concerns traces. The nuclear regularity equivalence [3, Corollary 7.4] uses additional hypotheses and does not force regularity for every algebra above. Corrections concerning the unitary invariant $`\mathrm{Cu}_1`$ concern a different invariant [4].

## References

1. E. Gardella and F. Perera, *The modern theory of Cuntz semigroups of C*-algebras*, EMS Surveys in Mathematical Sciences 13 (2026), 133–214, [DOI](https://doi.org/10.4171/EMSS/84), [published text](https://ems.press/content/serial-article-files/52386), Question 16.5, p.206; definitions in Sections 2–4 and 10. The published question includes **unital**.
2. H. Thiel, *Ranks of operators and pureness of C*-algebras*, [arXiv:2610.06761v1](https://arxiv.org/html/2610.06761v1), Theorem A and Corollary B.
3. S. Evington, S. Hua, C. Schafhauser, A. Seth, A. Tikuisis and S. White, *Regular simple nuclear C*-algebras*, [arXiv:2610.09390v1](https://arxiv.org/html/2610.09390v1), Corollary 7.4.
4. L. Cantier, *The unitary Cuntz semigroup on the classification of non-simple C*-algebras*, J. Math. Anal. Appl. 522 (2023), 127003, [DOI](https://doi.org/10.1016/j.jmaa.2023.127003), erratum section.

## Status review


**Known cases:** Stable rank one supplies weak cancellation, and simple nuclear regularity theorems impose extra assumptions. Abstract Cu-semigroups, infinite or nonsimple cone examples, and the unitary Cuntz semigroup do not realize the requested ordinary Cu failure for a simple unital stably finite algebra.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Stable rank one supplies weak cancellation, and simple nuclear regularity theorems impose extra assumptions. Abstract Cu-semigroups, infinite or nonsimple cone examples, and the unitary Cuntz semigroup do not realize the requested ordinary Cu failure for a simple unital stably finite algebra.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Independent primary-statement review and current searches found no matching resolution or complete announcement. The comparison included all 1,703 pinned AIM/OpenAI statement records and all 910 preceding local findings, across all statuses. The closest regularity and proper-infiniteness announcements impose different hypotheses. This is a bounded status check, not a certification of every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-70841d96258727ed**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
