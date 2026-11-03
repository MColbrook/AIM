# 847. Does the ∂∂̄-lemma imply the existence of a balanced metric?

**Area:** Complex geometry and Hermitian metrics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a smooth compact connected complex manifold of complex dimension $`n\ge3`$. Suppose $`X`$ satisfies the $`\partial\bar\partial`$-lemma: every smooth complex differential form $`\alpha`$ of pure bidegree that is $`d`$-closed and $`d`$-exact can be written as $`\alpha=\partial\bar\partial\beta`$ for a smooth form $`\beta`$.

**Must $`X`$ admit a balanced Hermitian metric?** Equivalently, must there exist a smooth positive definite real $`(1,1)`$-form $`\omega`$ satisfying

```math
d\bigl(\omega^{n-1}\bigr)=0?
```

The question is stated after Theorem 1.2 of [1] and at the start of §6 of [2]. No Kähler, Fujiki-class, SKT/pluriclosed or canonical-bundle assumption is imposed. The unknown is any balanced metric, without prescribing a conformal class. The lower-dimensional cases are known; the converse implication is false.

## Application

This tests whether a cohomological condition resembling Kähler Hodge theory forces a global positive metric structure. It separates the algebra of differential forms from existence of a particular Hermitian metric.

## References

1. S. Yang and X. Yang, *Bott-Chern blow-up formula and bimeromorphic invariance of the $`\partial\bar\partial`$-Lemma for threefolds*, Trans. Amer. Math. Soc. 373 (2020), 8885–8909. [DOI](https://doi.org/10.1090/tran/8213); [primary v3, introduction and Proposition 2.1](https://arxiv.org/html/1712.08901v3).
2. D. Popovici, *Volume and Self-Intersection of Differences of Two Nef Classes*, [arXiv:1505.03457v2, §6](https://arxiv.org/html/1505.03457v2). The cone conjecture there is stronger than the metric-existence question.
3. D. Popovici, [author monograph, §4.5.5, Conjecture 4.5.56, printed pp. 311–312](https://www.math.univ-toulouse.fr/~popovici/hodge-def.pdf). The revision date of the served copy was not independently established.
4. *Balanced manifolds and SKT metrics*, [author manuscript](https://math.vanderbilt.edu/rasdear/bgskt-revision.pdf), Ann. Mat. Pura Appl. 201 (2022), 2505–2517; introduction Theorems 1.3–1.4 and Conjecture 1.5.

## Status review


**Known cases:** The source asks existence of some balanced metric, not equality of positive cones. Deformation or bimeromorphic-invariance counterexamples to the ddbar lemma and failures of a stronger cone identity do not imply a nonbalanced ddbar manifold. Restricted solvmanifold and hypercomplex theorems do not settle the full implication.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source asks existence of some balanced metric, not equality of positive cones. Deformation or bimeromorphic-invariance counterexamples to the ddbar lemma and failures of a stronger cone identity do not imply a nonbalanced ddbar manifold. Restricted solvmanifold and hypercomplex theorems do not settle the full implication.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Existence alone is weaker than the balanced/Gauduchon cone equality. Counterexamples to a stronger cone assertion on already balanced manifolds do not answer this question. A September 2026 announced counterexample to bimeromorphic invariance of the $`\partial\bar\partial`$-lemma concerns a separate target; no nonbalanced example is inferred from it.

Bounded current-resolution and complete-announcement searches found no matching solution. Semantic comparisons used 1,155 private findings and 1,704 retained public all-status statements, with later Spin(7) and particle-scattering holds checked separately. Hermitian-symplectic-to-Kähler, generalized Gauduchon signs and Kähler semiampleness have different hypotheses or conclusions. Published identity is verified; complete published/preprint body parity is not asserted. See the [owner and current review](../FURTHER_problems/_tracking/focused-ddbar-balanced-metric-C258-C-20261029/OWNER-EXACT-COMPACT-DDBAR-IMPLIES-BALANCED-METRIC-PRIMARY-CURRENT-AND-SEMANTIC-PROPOSAL.json) and [independent primary model peer](../FURTHER_problems/_tracking/focused-ddbar-balanced-metric-C258-C-20261029/A-INDEPENDENT-COMPACT-DDBAR-PREMISE-BALANCED-POSITIVE-METRIC-AND-STRONGER-CONE-SCOPE-PEER.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d1cf67e74776d392**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
