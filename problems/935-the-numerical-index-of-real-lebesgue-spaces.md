# 935. The numerical index of real Lebesgue spaces

**Area:** Functional analysis / bounded linear operators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`1<p<\infty`$, $`p\ne2`$, and let $`X=L_p([0,1];\mathbb R)`$ have its usual Lebesgue norm. Write $`S_X`$ and $`S_{X^*}`$ for the unit spheres of $`X`$ and its continuous real dual. For a bounded real-linear operator $`T:X\to X`$, define
```math
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\},
\qquad n(X)=\inf_{\|T\|=1}v(T).
```

Is it true that, for every such $`p`$,
```math
n\!\left(L_p([0,1];\mathbb R)\right)=M_p,
\qquad
M_p=\max_{0\le t\le1}\frac{|t^{p-1}-t|}{1+t^p}\,?
```

This is the ordinary numerical index of all bounded real-linear operators. The unresolved lower-bound direction asks whether $`v(T)\ge M_p\|T\|`$ always holds.

## Application

The numerical index measures the best uniform recovery of operator norm from evaluations by norming functionals. Its exact value quantifies this loss for bounded operators on a standard Lebesgue function space.

## References

1. M. Martín, J. Merí and M. Popov, *On the numerical radius of operators in Lebesgue spaces*, **Journal of Functional Analysis 261** (2011), 149–168, §5, Problem 5.1. [DOI](https://doi.org/10.1016/j.jfa.2011.03.007); [eligible arXiv record](https://arxiv.org/abs/1011.4785); [author preprint](https://www.ugr.es/~mmartins/Curriculum/Papers/pre-MarMerPop(2).pdf).
2. R. Chiclana, *The Numerical Index of Two-Dimensional Real $`\ell_p`$ Spaces*, [arXiv:2606.01675v1](https://arxiv.org/pdf/2606.01675v1), submitted 1 June 2026, introduction pp1–2 and Theorem 1.1. This gives the corresponding formula for real two-dimensional $`\ell_p^2`$ and explicitly distinguishes the still-open general real $`L_p`$ problem.

## Status review


**Known cases:** The June 2026 Chiclana result is exactly two-dimensional real ell-p; its introduction retains the general real Lebesgue-space numerical index problem. Rank-one, absolute and complex indices do not supply the missing lower bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The June 2026 Chiclana result is exactly two-dimensional real ell-p; its introduction retains the general real Lebesgue-space numerical index problem. Rank-one, absolute and complex indices do not supply the missing lower bound.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The June 2026 primary source explicitly retains the general real $`L_p`$ problem. Bounded searches through 25 October 2026 found no complete solution, counterexample or announced solution for the target above. The two-dimensional result does not settle the infinite-dimensional statement. Complex, rank-one and absolute numerical indices are separate questions and are not asserted open here.

## Duplicate check

The target was compared with the current and all-status AIM/OpenAI statements, all recorded finding decisions, and admitted problem pages. The existing question about a complex reflexive space with numerical index one is a different existential problem.

## Review provenance

Discovered in the full recovered-body scan of arXiv:1011.4785v1. Exact retained positive passages were jointly read with the coordinator; definitions were checked against the author primary, and the coordinator independently read the selected June 2026 primary passages and version record. This records a bounded source/current-status review, not verification of every cited proof or an exhaustive guarantee of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fc28301b7c478124**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
