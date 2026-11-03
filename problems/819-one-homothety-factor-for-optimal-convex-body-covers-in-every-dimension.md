# 819. One homothety factor for optimal convex-body covers in every dimension

**Area:** Geometry and topology / convex geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

A convex body in $`\mathbb R^d`$ is a compact convex set with nonempty interior. For two such sets define
```math
N(K,L)=\min\left\{m\in\mathbb N:
K\subseteq\bigcup_{j=1}^{m}(t_j+L)
\text{ for some }t_1,\ldots,t_m\in\mathbb R^d\right\}.
```

Let
```math
H_d=\min\left\{m\in\mathbb N:
\text{for every convex body }K\subset\mathbb R^d
\text{ there exists }\lambda_K\in(0,1)
\text{ with }N(K,\lambda_KK)\le m\right\}.
```

Thus $`H_d`$ is the optimal **worst-case** number of smaller copies over all convex bodies in dimension $`d`$.

Does there exist a single $`\lambda\in(0,1)`$, independent of the dimension, such that
```math
\text{for every }d\ge1\text{ and every convex body }K\subset\mathbb R^d,
\qquad N(K,\lambda K)\le H_d?
```

Equivalently, if $`\overline H_d(\lambda)=\sup_KN(K,\lambda K)`$, is
$`\overline H_d(\lambda)=H_d`$ for one universal $`\lambda`$ and every $`d`$?

The copies use translations and one positive scale; individual rotations and reflections are not allowed. No symmetry or boundary regularity is assumed. The number permitted is $`H_d`$, rather than the possibly smaller optimal number for the particular body $`K`$.

## Application

This asks whether an optimal bound on the number of convex-body copies can also provide a fixed quantitative amount of shrinkage in every dimension. It is a quantitative question about geometric covering constructions.

## References

1. M. Naszódi, *On the constant of homothety for covering a convex set with its smaller copies*, **Pro Mathematica** 24 (47–48) (2010), 113–119, Definition 3.2 and Question 3.3 on p. 117. [Published article](https://revistas.pucp.edu.pe/index.php/promathematica/article/view/10276); [PDF](https://revistas.pucp.edu.pe/index.php/promathematica/article/viewFile/10276/10721). The same question occurs in [arXiv:0901.2652v1](https://arxiv.org/abs/0901.2652), §3.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, [arXiv:2609.23913v1](https://arxiv.org/abs/2609.23913), 20 September 2026, Theorems 1–2 and Proposition 3. Used for the current scope comparison below.

## Status review


**Known cases:** Naszodi proves a scale for each fixed dimension. Fractional illumination and asymptotic covering estimates permit more than the exact optimal worst-case number and use dimension-dependent shrinkage. They do not supply a single scale at the exact H_d count for all dimensions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Naszodi proves a scale for each fixed dimension. Fractional illumination and asymptotic covering estimates permit more than the exact optimal worst-case number and use dimension-dependent shrinkage. They do not supply a single scale at the exact H_d count for all dimensions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Naszódi's Theorem 1.2 proves that, for each fixed $`d`$, one can choose a scale $`\lambda_d<1`$ uniformly over all bodies. Question 3.3 asks for a single scale across all dimensions, and is not the question already answered by that theorem.

The nearby AIM illumination problem bounds $`H_d`$ by $`2^d`$ and characterizes equality. Its statement does not specify a dimension-independent scale at the exact worst-case count. The announced OpenAI covering-density and metric-entropy results concern different objectives; their complete catalogue summaries and constituent abstracts were compared.

The 2026 preprint in reference 2 claims a sharp fractional illumination bound and an asymptotic integral covering bound. The latter allows more copies than the unknown exact optimum, and its asymptotic proof chooses $`1-\lambda=1/(d\log d)`$. Those statements do not answer this question. Their full proofs were not independently certified in this review.

No matching complete solution or announcement was located in the bounded checks. The original arXiv source predates the January 2022 intake cutoff; newer work is cited only to check status. The [owner review](../FURTHER_problems/_tracking/C118-0901.2652-universal-homothety-Q3.3-focused-owner-ready-A-END-20261026.json) and [independent review](../FURTHER_problems/_tracking/C118-universal-homothety-root-independent-formulation-current-allstatus-PASS-END-20261026.json) retain the exact source bindings, searches and all-status duplicate comparisons.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-97a6e82304bc4820**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
