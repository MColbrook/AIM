# 949. Does a smooth target make energy-minimal planar deformations $`C^1`$?

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X,Y\subset\mathbb C`$ be bounded planar domains with the same finite connectivity. Following Cristina, Iwaniec, Kovalev and Onninen [1, Definitions 1.4 and 1.9], let $`\mathcal D(X,Y)`$ be their class of orientation-preserving $`W^{1,2}`$ deformations: limits of homeomorphisms $`X\to Y`$ with the stated boundary-component correspondence and nonoverlap condition. Boundary values are not prescribed pointwise, and a deformation may map some interior points of $`X`$ to $`\partial Y`$.

For a Dirichlet-energy minimizer $`h\in\mathcal D(X,Y)`$,

```math
E_X[h]=\int_X|Dh|^2=\min_{g\in\mathcal D(X,Y)}\int_X|Dg|^2,
```


must $`h`$ be $`C^1`$ **in the interior of $`X`$** whenever $`\partial Y`$ is smooth? This is [1, Question 9.2] in the published version, Question 8.3 in the original preprint. The smoothness of the *target* boundary is the essential hypothesis.

The authors prove local Lipschitz regularity in general [1, Theorem 1.14]. Their non-$`C^1`$ examples have nonsmooth target boundaries. Their explicit smooth annulus example is $`C^{1,1}`$ but not $`C^2`$, so it does not decide the stated $`C^1`$ question.

## Application

These deformations model least-energy mappings of planar elastic sheets without fixing every boundary point. Interior $`C^1`$ regularity would rule out corners in a minimizing deformation when the receiving shape has a smooth boundary, even if parts of the sheet collapse onto it.

## References

1. J. Cristina, T. Iwaniec, L. V. Kovalev and J. Onninen, [*The Hopf-Laplace equation: harmonicity and regularity*](https://journals.sns.it/index.php/annaliscienze/article/download/367/357/586), *Annali della Scuola Normale Superiore di Pisa, Classe di Scienze* (5) **13** (2014), 1145–1187, Definitions 1.4 and 1.9, Theorems 1.14–1.15 and Question 9.2 (printed p. 1185). [Original arXiv:1011.5934v1](https://arxiv.org/pdf/1011.5934v1), Question 8.3.
2. T. Iwaniec and J. Onninen, [*Mappings of least Dirichlet energy and their Hopf differentials*](https://arxiv.org/abs/1202.1017), arXiv:1202.1017 (2012). Related least-energy mappings and cracks; this is not cited as a resolution of [1, Question 9.2].

## Status review


**Known cases:** The deformation class allows cracks to the target boundary and does not prescribe pointwise boundary data. The September 2026 regularity theorem for local obstacle/constraint maps treats a different minimizer class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The deformation class allows cracks to the target boundary and does not prescribe pointwise boundary data. The September 2026 regularity theorem for local obstacle/constraint maps treats a different minimizer class.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

A [bounded status and duplicate audit](../FURTHER_problems/_tracking/w001-hopf-laplace-smooth-target-regularity-status-2026-10-22.json) through 22 October 2026 found no proof, counterexample or announcement settling this exact smooth-target question. Later regularity results for other constraint-map classes have different admissible mappings and should not be conflated with $`\mathcal D(X,Y)`$.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8ff0a972febff463**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
