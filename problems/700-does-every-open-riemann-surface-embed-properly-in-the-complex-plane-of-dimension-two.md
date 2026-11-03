# 700. Does every open Riemann surface embed properly in the complex plane of dimension two?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be any connected, noncompact Riemann surface. Does there always exist a **proper holomorphic embedding**
```math
f:X\hookrightarrow\mathbb C^2?
```

Here embedding means an injective holomorphic immersion identifying $`X`$ with its image, and proper means that $`f^{-1}(K)`$ is compact for every compact $`K\subset\mathbb C^2`$. The question concerns the given complex structure on $`X`$, with no finite-topology, planar, bordered, or prior-embedding assumption.

## Application

A positive answer would represent every open complex curve as a closed complex submanifold of the smallest target dimension permitted by general embedding heuristics. Proper embeddings into $`\mathbb C^3`$ and proper immersions into $`\mathbb C^2`$ are available generally; the question asks whether both properness and injectivity can be achieved simultaneously in $`\mathbb C^2`$.

## References

1. F. Forstnerič and E. Fornæss Wold, [*Bordered Riemann surfaces in $`\mathbb C^2`$*](https://doi.org/10.1016/j.matpur.2008.09.010), *Journal de Mathématiques Pures et Appliquées* **91** (2009), 100–114, [author preprint](https://arxiv.org/pdf/0708.2887), Introduction and Theorem 1.1. Their theorem gives a proper embedding for compact bordered complex curves already embedded in $`\mathbb C^2`$, and the introduction states the unrestricted problem separately.
2. F. Forstnerič, [*Proper holomorphic embeddings with small limit sets*](https://doi.org/10.1090/bproc/212), *Proceedings of the American Mathematical Society, Series B* **11** (2024), 77–83, [author PDF](https://users.fmf.uni-lj.si/forstneric/papers/2024PAMS.pdf), printed p. 78, after Corollary 1.2. The author calls this the Forster or Bell–Narasimhan conjecture and obtains general proper embeddings into $`\mathbb C^3`$, leaving the $`\mathbb C^2`$ question open.

## Status review


**Known cases:** The current author statement still distinguishes general proper C3 embeddings and C2 immersions from proper C2 embeddings. Results for already embedded bordered surfaces or particular topology do not cover every fixed open Riemann surface.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current author statement still distinguishes general proper C3 embeddings and C2 immersions from proper C2 embeddings. Results for already embedded bordered surfaces or particular topology do not cover every fixed open Riemann surface.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2009 result removes the boundary from a curve already embedded in $`\mathbb C^2`$; it does not construct such a starting embedding for every open Riemann surface. The 2024 paper still identifies the unrestricted question as open. A bounded current literature and announcement check on 21 October 2026 found no complete matching resolution. Results on particular topologies, harmonic embeddings into $`\mathbb C\times\mathbb R^2`$, null embeddings into other complex manifolds, and proper holomorphic embeddings into $`\mathbb C^3`$ have different hypotheses or targets.

The [historical arXiv body packet](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0143-review.json) and [coordinator status and duplicate review](../FURTHER_problems/_tracking/forster-c2-embedding-coordinator-check-2026-10-21.json) record the specific passages and limits of this check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7db8c41b76923298**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
