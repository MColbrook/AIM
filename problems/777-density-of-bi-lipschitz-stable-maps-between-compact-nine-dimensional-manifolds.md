# 777. Density of bi-Lipschitz stable maps between compact nine-dimensional manifolds

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`N`$ and $`P`$ be compact connected smooth manifolds without boundary, both of dimension $`9`$, equipped with smooth Riemannian metrics. Give $`C^\infty(N,P)`$ its Whitney $`C^\infty`$ topology.

Call a smooth map $`g:N\to P`$ **bi-Lipschitz stable** if there is a neighborhood $`U_g`$ of $`g`$ in $`C^\infty(N,P)`$ such that, for every $`h\in U_g`$, there are bi-Lipschitz homeomorphisms $`\phi:N\to N`$ and $`\psi:P\to P`$ with

```math
h=\psi\circ g\circ\phi^{-1}.
```

Neither continuous dependence of these homeomorphisms on $`h`$ nor a uniform bound on their bi-Lipschitz constants is required. On these compact manifolds the definition is independent of the chosen smooth Riemannian metrics.

**Question.** For every such pair $`N,P`$, are the bi-Lipschitz stable maps dense in $`C^\infty(N,P)`$? Equivalently, does every smooth map have a bi-Lipschitz stable smooth map in each of its Whitney neighborhoods?

This is the compact-source-and-target $`(n,p)=(9,9)`$ branch of Conjecture 9.1 in [1]. It asks for stability of whole maps under changes of coordinates in source and target.

## Application

Stability describes which singularities persist under small smooth perturbations of a model. Such classifications organize geometric singularities and bifurcations; controlling distance distortion gives a finer notion of robustness than topological equivalence. Mather's theory gives density under topological equivalence in all dimensions, whereas smooth stability fails to be dense at this first equal-dimension boundary case. Bi-Lipschitz changes of coordinates provide an intermediate geometric notion that controls distortion of distances.

The eligible survey [1, §8.2] explicitly lists $`(9,9)`$ in the boundary of the nice dimensions. Ruas and Trivedi [2] establish bi-Lipschitz **contact** invariance of the relevant Thom–Mather strata. This is useful progress, but contact equivalence permits transformations beyond independent coordinate changes in source and target. The survey [1, §9] still identifies bi-Lipschitz right-left triviality of the modal families as the missing step in its proposed density argument.

The same survey already discusses the smooth Whitney fibering result and its consequences for strong **topological** stability [1, §7.4]; these consequences do not establish bi-Lipschitz stability. More recent work classifies isolated complex scalar function germs of corank two [3], or distinguishes ordinary from strong bi-Lipschitz triviality of a smooth scalar deformation [4]. These are different statements from density for maps between nine-dimensional manifolds.

## Status review


**Known cases:** The target concerns stability of whole maps under source-and-target bi-Lipschitz homeomorphisms in the compact nine-by-nine branch. Contact-orbit classification of germs and a bi-Lipschitz invariant stratification are not this density assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target concerns stability of whole maps under source-and-target bi-Lipschitz homeomorphisms in the compact nine-by-nine branch. Contact-orbit classification of germs and a bi-Lipschitz invariant stratification are not this density assertion.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2201.03888v1); [comparison source 2](https://doi.org/10.1007/978-3-030-95760-5_1); [comparison source 3](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0006/AJM-2019-0023-0006-a004.pdf); [comparison source 4](https://arxiv.org/abs/2510.06792v1); [comparison source 5](https://arxiv.org/abs/2609.17034v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source is arXiv:2201.03888v1, submitted 11 January 2022, Definitions 2.2–2.3, §8.2 and Conjecture 9.1. A bounded current-literature and announced-solution search on 24 October 2026 found no matching resolution of this precise branch. This is a research-status check, not a proof that no unpublished solution exists. The published chapter's metadata and abstract were checked; its full subscription body was not accessed, so no full edition-parity claim is made.

## References

1. M. A. S. Ruas, *Old and New Results on Density of Stable Mappings*, Handbook of Geometry and Topology of Singularities III (2022), 1–80. [Eligible arXiv version](https://arxiv.org/abs/2201.03888v1), [published chapter](https://doi.org/10.1007/978-3-030-95760-5_1).
2. M. A. S. Ruas and S. Trivedi, *Bi-Lipschitz geometry of contact orbits in the boundary of the nice dimensions*, Asian J. Math. 23 (2019), 953–968. [Publisher PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0006/AJM-2019-0023-0006-a004.pdf).
3. N. Nguyen, M. Ruas and S. Trivedi, *Classification of Lipschitz unimodal function germs*, [arXiv:2510.06792v1](https://arxiv.org/abs/2510.06792v1) (2025).
4. D. Chakraborty and S. Trivedi, *On Strong Bi-Lipschitz Triviality of Deformations*, [arXiv:2609.17034v1](https://arxiv.org/abs/2609.17034v1) (2026).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2e78c0973003528e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
