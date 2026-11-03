# 723. Does every smooth real-algebraic CR submanifold have Nash–Artin approximation?

**Area:** Complex analysis and CR geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M\subset\mathbb C^N`$ be a smooth real-algebraic CR submanifold. Fix any point $`p\in M`$, any positive integer $`N'`$, and any real-algebraic set $`\Sigma\subset\mathbb C^N\times\mathbb C^{N'}`$. Suppose a germ of a holomorphic map $`h:(\mathbb C^N,p)\to\mathbb C^{N'}`$ has its graph over $`M`$ contained in $`\Sigma`$ near $`(p,h(p))`$.

**For every integer $`j\ge1`$, must there be a germ of an algebraic holomorphic map $`h_j:(\mathbb C^N,p)\to\mathbb C^{N'}`$ whose graph over $`M`$ still lies in $`\Sigma`$ and whose derivatives at $`p`$ agree with those of $`h`$ through order $`j`$?**

The quantifiers over $`p`$, $`N'`$ and $`\Sigma`$ are part of the question. “Algebraic holomorphic” means that the component germs are algebraic power series, not merely holomorphic approximations. The property for a given pair $`(M,\Sigma)`$ is Definition 3.6 of Mir's survey; Conjecture C asserts it for every such pair when $`M`$ is a smooth real-algebraic CR submanifold.

Known results cover generically minimal CR submanifolds, those whose CR orbits have constant dimension, and all smooth real-algebraic hypersurfaces. Every CR submanifold also has the property away from a proper real-algebraic exceptional subset. The remaining difficulty is higher codimension with variable CR-orbit dimension; the problem is not an open hypersurface case.

## Application

An affirmative answer would let one replace holomorphic maps satisfying algebraic constraints along a CR manifold by algebraic maps with any prescribed finite jet, while preserving the same constraints. In particular, it would strengthen algebraic classification of locally biholomorphic real-algebraic CR germs.

## References

- N. Mir, [*Artin's Approximation Theorems and Cauchy–Riemann Geometry*](https://archive.intlpress.com/site/pub/files/_fulltext/journals/maa/2014/0021/0004/MAA-2014-0021-0004-a005.pdf), *Methods and Applications of Analysis* **21** (2014), no. 4, 481–502, Definition 3.6 (printed p. 492), Theorems 3.7–3.10 (pp. 492–494), Conjecture C and remaining case (pp. 494–495).
- N. Mir, [*Algebraic approximation in CR geometry*](https://people.tamu.edu/~nordine.mir/jmpa2012.pdf), *Journal de Mathématiques Pures et Appliquées* **98** (2012), 72–88, Theorems 1.1 and 1.3: constant-orbit-dimension and hypersurface cases.
- G. Rond, [*Transcendental holomorphic maps between real algebraic manifolds in a complex space*](https://arxiv.org/abs/1905.06222), arXiv:1905.06222 (2019): a Nash–Artin counterexample on an elliptic Bishop surface whose origin is CR-singular, outside this conjecture's smooth CR hypothesis.
- B. Lamel, N. Mir and G. Rond, [*Unique jet determination of CR maps into Nash sets*](https://doi.org/10.1016/j.aim.2023.109271), *Advances in Mathematics* **432** (2023), 109271: strong approximation for other Nash systems and minimal-source finite-jet results, not a stated full solution of Conjecture C.

## Status review


**Known cases:** The CR condition at the exceptional point is essential. Constant-orbit-dimension and hypersurface approximation theorems, and counterexamples outside the CR class, do not settle every smooth real-algebraic CR submanifold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The CR condition at the exceptional point is essential. Constant-orbit-dimension and hypersurface approximation theorems, and counterexamples outside the CR class, do not settle every smooth real-algebraic CR submanifold.

Additional comparison sources: [comparison source 1](https://archive.intlpress.com/site/pub/files/_fulltext/journals/maa/2014/0021/0004/MAA-2014-0021-0004-a005.pdf); [comparison source 2](https://people.tamu.edu/~nordine.mir/jmpa2012.pdf); [comparison source 3](https://arxiv.org/abs/1905.06222); [comparison source 4](https://doi.org/10.1016/j.aim.2023.109271). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published original statement and Definition 3.6 were checked against the publisher PDF, with source-bound excerpts of Conjecture C and its remaining case retained in the [J0691 body review](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0691-J324-remote-pdf-body-review.json) and [definition and known-case audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal0692-Mir-Nash-Artin-native-definition-contexts.json). Mir's list of known cases prevents claiming that the hypersurface or constant-orbit-dimension regimes remain open. Rond's 2019 counterexample addresses real-algebraic manifolds without the CR condition at its critical point, so it does not refute the assertion above. The 2023 comparison has a different scope. Targeted 2026 searches for proofs, counterexamples and announcements found no exact full resolution; the search is bounded, not exhaustive. Targeted AIM and FURTHER problem-page searches found no exact duplicate. The dated [status review](../FURTHER_problems/_tracking/mir-nash-artin-cr-2026-10-22-status.json) and [duplicate check](../FURTHER_problems/_tracking/mir-nash-artin-cr-2026-10-22-duplicates.json) record these distinctions.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d5b4165e16eedb05**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
