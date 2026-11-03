# 901. Finite-dimensional detection of almost-periodic Banach cocycles

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`G`$ be any locally compact Hausdorff group and $`V`$ a real Banach space. Let $`\pi:G\to\mathrm{GL}(V)`$ be a strongly continuous representation by bounded linear isomorphisms, such that every orbit $`\{\pi(g)v:g\in G\}`$ has compact closure in norm.

Suppose a continuous map $`b:G\to V`$ satisfies
```math
b(gh)=b(g)+\pi(g)b(h)
```

and does not belong to the closure of
```math
B^1(G,V)=\{g\mapsto v-\pi(g)v:v\in V\}
```

in the topology of uniform convergence on compact subsets of $`G`$.

Must there exist a closed $`\pi(G)`$-invariant subspace $`W\subset V`$, with $`0<\dim(V/W)<\infty`$, such that
```math
\sup_{g\in G}\|b(g)+W\|_{V/W}=\infty?
```

There is no compact-generation, countability, reflexivity or uniform dimension assumption. Closure need not be sequential.

## Application

The question asks whether an obstruction to approximate fixed points of an affine Banach-space action can always be witnessed in a finite-dimensional quotient.

## References

- Y. Cornulier and R. Tessera, *On the vanishing of reduced 1-cohomology for Banach representations*, Ann. Inst. Fourier **70** (2020), 1951-2003, [DOI](https://doi.org/10.5802/aif.3363), [2017 primary](https://arxiv.org/html/1711.05566v1), **Definition 4.1 and Question 4.7**; [published text](https://www.numdam.org/item/10.5802/aif.3363.pdf), pp. 1971-1973.
- A. Thom, *Sublinear growth of 1-cocycles and uniform convexity* (2026), [primary](https://arxiv.org/html/2603.22049v1). Its mixing and Banach-space hypotheses differ from this target.

## Status review


**Known cases:** The source proves the finite-quotient detection property for special structured groups and the unitary Hilbert version. Mixing-cocycle or uniform-convexity results impose different representation assumptions. Compact-open closure of coboundaries cannot be replaced by failure to be a single coboundary.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The source proves the finite-quotient detection property for special structured groups and the unitary Hilbert version. Mixing-cocycle or uniform-convexity results impose different representation assumptions. Compact-open closure of coboundaries cannot be replaced by failure to be a single coboundary.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Partial progress; checked 29 October 2026.** The unitary Hilbert version is positive. The source also proves the relevant detection property for compactly generated groups of polynomial growth and other structured classes. These do not exhaust the stated Banach and group hypotheses. No matching complete theorem, counterexample, announcement or AIM/private duplicate was found.

This is the source's property $`\mathcal{AP}_{\mathrm{fd}}`$. Failure to be a single exact coboundary is insufficient; the compact-open closure is essential.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-APfd-finite-factor-detection-C234-C-20261028/OWNER-EXACT-ALMOST-PERIODIC-BANACH-COCYCLE-FINITE-QUOTIENT-DETECTION-APFD-PRIMARY-PUBLISHED-CURRENT-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-APfd-finite-factor-detection-C234-C-20261028/A-INDEPENDENT-APFD-STRONG-CONTINUITY-COMPACT-OPEN-CLOSURE-AND-FINITE-QUOTIENT-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-APfd-finite-factor-detection-C234-C-20261028/ROOT-EXACT-APFD-COMPACT-OPEN-REDUCED-COCYCLE-CURRENT-AND-SEMANTIC-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4880a1c2c2498869**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
