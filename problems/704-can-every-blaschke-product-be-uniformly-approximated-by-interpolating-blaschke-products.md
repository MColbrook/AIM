# 704. Can every Blaschke product be uniformly approximated by interpolating Blaschke products?

**Area:** Complex analysis and Hardy spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb D`$ be the open unit disk. A Blaschke product is *interpolating* if its zeros form an interpolating sequence for $`H^\infty(\mathbb D)`$: every bounded choice of values on those zeros is attained by a bounded holomorphic function.

**Question (Garnett, Problem 5.4).** For every Blaschke product $`B`$ and every $`\varepsilon>0`$, is there a **single interpolating Blaschke product** $`I`$ such that

```math
\|B-I\|_{H^\infty(\mathbb D)}=\sup_{z\in\mathbb D}|B(z)-I(z)|<\varepsilon?
```


The norm is uniform on the entire disk. Approximation only on compact subsets, approximation of $`|B|`$, or approximation by a quotient or product of several interpolating Blaschke products does not answer the question.

## Application

The question asks whether an arbitrary Blaschke product can be represented, to any prescribed uniform accuracy, by one whose zeros have the strong interpolation property. It links approximation of bounded analytic functions to the geometry of their zero sets.

## References

1. J. B. Garnett, [*Bounded Analytic Functions*](https://doi.org/10.1007/0-387-49763-3), revised first ed., Graduate Texts in Mathematics 236, Springer (2007), Chapter X, Problem 5.4, printed p. 420; preface printed p. vii. [Read-copy source](https://ndl.ethernet.edu.et/server/api/core/bitstreams/e557b1f7-3dee-48da-9c2d-e369ab482cee/content).
2. W. K. Hayman and E. F. Lingham, [*Research Problems in Function Theory: Fiftieth Anniversary Edition*](https://link.springer.com/book/10.1007/978-3-030-25165-9), Springer (2019), Problem 9.21(a), printed p. 240. It restates the same question as open.
3. I. Chalendar, P. Gorkin and J. R. Partington, [*Inner functions and operator theory*](https://eprints.whiterose.ac.uk/id/eprint/84995/7/article2015-3.pdf), *North-Western European Journal of Mathematics* **1** (2015), 9–28, printed p. 12. The published paper explicitly distinguishes the question from approximation of moduli.
4. G. A. Hjelle and A. Nicolau, [*Approximating the modulus of an inner function*](https://msp.org/pjm/2006/228-1/pjm-v228-n1-p05-p.pdf), *Pacific Journal of Mathematics* **228** (2006), 103–118. Its approximation of absolute values is a partial result with a different target.

## Status review


**Known cases:** Algebra generation by interpolating Blaschke products and approximation by quotients or products do not imply approximation by a single interpolating Blaschke product in the full disk supremum norm.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Algebra generation by interpolating Blaschke products and approximation by quotients or products do not imply approximation by a single interpolating Blaschke product in the full disk supremum norm.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/0-387-49763-3); [comparison source 2](https://ndl.ethernet.edu.et/server/api/core/bitstreams/e557b1f7-3dee-48da-9c2d-e369ab482cee/content); [comparison source 3](https://link.springer.com/book/10.1007/978-3-030-25165-9); [comparison source 4](https://eprints.whiterose.ac.uk/id/eprint/84995/7/article2015-3.pdf); [comparison source 5](https://msp.org/pjm/2006/228-1/pjm-v228-n1-p05-p.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Garnett's revised preface reports that the neighboring Problem 5.3, concerning generation of $`H^\infty`$ as an algebra, had been solved, while Problem 5.4 remained open. The 2015 survey and the 2019 problem collection retain the latter. Focused searches for a later complete proof, counterexample, or announced resolution through 2026-10-22 found none; this is a bounded search, not a claim that no unindexed result exists. No equivalent target was found among local AIM problems or admitted FURTHER leads. The [original-body receipt](../FURTHER_problems/_tracking/blaschke-interpolating-uniform-original-2026-10-22.json) and [status audit](../FURTHER_problems/_tracking/blaschke-interpolating-uniform-status-2026-10-22.json) record the exact edition, passage and scope checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8e193915bcf7b434**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
