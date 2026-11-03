# 904. Does every separable non-reflexive Banach space admit a Read norm?

**Area:** Banach-space geometry and continuous functional analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,\|\cdot\|)`$ be a real separable non-reflexive Banach space. Does there exist an equivalent norm $`p`$ on $`X`$ for which the set
```math
\mathrm{NA}(X,p)=
\{f\in X^*: |f(x)|=p^*(f)\text{ for some }x\in X,\ p(x)=1\}
```

contains no two-dimensional real linear subspace? Here $`p^*`$ is the dual norm, and equivalence means that $`a\|x\|\le p(x)\le b\|x\|`$ for some $`0<a\le b<\infty`$.

The norm may depend on $`X`$. The question imposes no smoothness or quantitative bound on its equivalence constants. It concerns linear subspaces contained in the set of attaining functionals, rather than the dimension of that set's linear span.

## Application

Norm attainment asks whether a continuous linear objective achieves its maximum on a unit ball. This question tests how changing an equivalent norm can limit the linear structure of objectives with maximizers, while preserving the underlying Banach-space topology.

## References

1. V. Kadets, G. López, M. Martín and D. Werner, [*Equivalent norms with an extremely nonlineable set of norm attaining functionals*](https://doi.org/10.1017/S1474748018000087), *Journal of the Institute of Mathematics of Jussieu* **19** (2020), 259–279. Problem 5.1; [current author preprint](https://arxiv.org/pdf/1709.01756v3), printed p. 15; real-field convention and definition on p. 2.
2. M. Martín, [*A Banach space whose set of norm-attaining functionals is algebraically trivial*](https://doi.org/10.1016/j.jfa.2024.110815), *Journal of Functional Analysis* **288** (2025), 110815. [Current author preprint](https://arxiv.org/html/2406.07273v3), Theorem 1 and Proposition 4.

## Status review


**Known cases:** The Read-norm constructions and the 2025 algebraically-trivial norm-attainment result cover separable spaces containing c0. They do not cover every separable nonreflexive real space; correcting the older strict-convexity proof does not settle the general renorming question.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The Read-norm constructions and the 2025 algebraically-trivial norm-attainment result cover separable spaces containing c0. They do not cover every separable nonreflexive real space; correcting the older strict-convexity proof does not settle the general renorming question.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The first paper constructs such norms for separable spaces containing an isomorphic copy of $`c_0`$. The 2025 paper gives a stronger conclusion on this class, excluding non-trivial cones of attaining functionals, but does not cover every separable non-reflexive space. Its correction concerning an older strict-convexity argument does not resolve Problem 5.1. No matching proof, counterexample, or complete-resolution announcement was located in the bounded checks through the date above.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-59d2ca6a5f45c305**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
