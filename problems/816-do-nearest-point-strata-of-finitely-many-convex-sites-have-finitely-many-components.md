# 816. Do nearest-point strata of finitely many convex sites have finitely many components?

**Area:** Convex geometry and Voronoi topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`k,n\geq2`$, and let $`A_1,\ldots,A_n`$ be pairwise disjoint nonempty closed convex subsets of Euclidean $`\mathbb R^k`$. They need not be bounded. Put $`A=\bigcup_{j=1}^n A_j`$, and for $`x\in\mathbb R^k`$ define

```math
P_A(x)=\{a\in A:\|x-a\|=\mathrm{dist}(x,A)\},\qquad
X_p=\{x\in\mathbb R^k:|P_A(x)|=p\},\quad 1\leq p\leq n.
```


Projection onto each individual $`A_j`$ is unique, so $`|P_A(x)|\leq n`$. **Must every $`X_p`$ have only finitely many connected components?**

The source proves that $`X_1`$ has exactly $`n`$ components and that $`X_1\cup X_2`$ is connected. Neither assertion answers the question for every individual $`X_p`$.

## Application

This asks whether a Voronoi decomposition built from arbitrary convex sites has finite topological complexity at each exact tie multiplicity. The absence of boundedness or algebraic boundary assumptions makes it stronger than finiteness for polygonal or semialgebraic sites.

## References

1. T. K. Subrahmonian Moothathu, [*Midsets and Voronoi Type Decomposition with Respect to Closed Convex Sets*](https://journalofconvexanalysis.com/articles/jca25082/), *J. Convex Anal.* **25** (2018), no. 4, 1345–1354. The hypotheses and notation are on p. 1349; the question is posed on p. 1353. [Primary PDF](https://journalofconvexanalysis.com/articles/jca25082/jca25082.pdf?v=2).

## Status review


**Known cases:** The source proves finiteness for X1 and connectedness of X1 union X2, not finiteness of every exact multiplicity stratum. Semialgebraic-site finiteness and non-Euclidean bisector examples impose or change hypotheses. Author/title and current-resolution searches found no matching unrestricted Euclidean theorem or counterexample.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source proves finiteness for X1 and connectedness of X1 union X2, not finiteness of every exact multiplicity stratum. Semialgebraic-site finiteness and non-Euclidean bisector examples impose or change hypotheses. Author/title and current-resolution searches found no matching unrestricted Euclidean theorem or counterexample.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded searches through 20 October 2026 found no exact proof, counterexample or public resolution announcement, and no matching AIM or admitted FURTHER problem. A non-Euclidean norm result about infinitely many bisector intersections does not settle this Euclidean convex-site question. See the [primary reading](../FURTHER_problems/_tracking/voronoi-stratum-components-primary-2026-10-20.json), [later-status search](../FURTHER_problems/_tracking/voronoi-stratum-components-current-2026-10-20.json), [duplicate review](../FURTHER_problems/_tracking/voronoi-stratum-components-duplicates-2026-10-20.json) and [decision](../FURTHER_problems/_tracking/voronoi-stratum-components-coordinator-2026-10-20.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-961e9c36db75680a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
