# 579. Can a Heisenberg surface be more than one-half Hölder?

**Area:** Geometry and topology
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Let $`U\subset\mathbb R^2`$ be a nonempty open set and let $`\mathbb H^1`$ be the first Heisenberg group with its Carnot–Carathéodory distance $`d_{cc}`$. Does there exist an injective map $`f:U\to\mathbb H^1`$ which is locally $`\alpha`$-Hölder for some $`\alpha>1/2`$; that is, on every compact $`K\subset U`$ there is a constant $`C_K`$ with
```math
d_{cc}(f(x),f(y))\le C_K|x-y|^\alpha\qquad(x,y\in K)?
```


The conjectured answer is **no**. Since $`d_{cc}`$ induces the usual topology on $`\mathbb H^1\cong\mathbb R^3`$, an injective continuous map on a planar open set is an embedding locally. The nontrivial range is $`1/2<\alpha\le 2/3`$: smooth Euclidean surface embeddings give $`1/2`$-Hölder examples, while Gromov's theorem rules out $`\alpha>2/3`$.

## Application

The Heisenberg group is a local model of a contact manifold. This question asks how regular a two-dimensional surface can be when distance is measured along the allowed horizontal directions. It separates geometric regularity of embedded surfaces from the existence of Hölder maps that may fold or identify points.

## References

1. E. Le Donne and R. Züst, [*Some properties of Hölder surfaces in the Heisenberg group*](https://arxiv.org/abs/1205.0228), *Illinois J. Math.* **57** (2013), 229–249, Introduction and Theorems 1.1–1.3. States the folk conjecture and proves restrictions under additional conditions.
2. P. Hajłasz and A. Schikorra, [*On the Gromov non-embedding theorem*](https://arxiv.org/html/2303.12960v2) (2023), Introduction and Theorem 1.2. Restates the one-half conjecture and proves a non-embedding theorem requiring additional Euclidean regularity.
3. P. Hajłasz, J. Mirra and A. Schikorra, [*Hölder continuous mappings, differential forms and the Heisenberg groups*](https://arxiv.org/html/2503.11506v3) (2025), §8, Theorem 8.2 and Corollaries 8.4, 8.6. Gives refined bounds with an additional Euclidean regularity hypothesis.
4. S. Wenger and R. Young, [*Constructing Hölder maps to Carnot groups*](https://arxiv.org/abs/1810.02700) (2018), Introduction and main theorems. Constructs maps below exponent $`2/3`$ without giving embeddings.

5. P. Hajłasz and A. Schikorra, [*Hölder embeddings of a disk into the Heisenberg group*](https://sites.pitt.edu/~hajlasz/Gromov/Gromov_conjecture.pdf), preliminary version of 6 September 2026, Theorem 1.1, p. 2; Propositions 8.2 and 9.2 and proof completion, p. 40. The authors explicitly state that the proposed calculations have not yet been verified by them.

## Status review

**Complete construction proposed; preliminary and unverified.** Hajłasz and Schikorra's [author-hosted draft](https://sites.pitt.edu/~hajlasz/Gromov/Gromov_conjecture.pdf), Theorem 1.1, proposes an embedding of the closed planar unit disk into $`\mathbb H^1`$ with its Carnot–Carathéodory metric and exponent $`\alpha=1/2+1/1800`$. Restricting to the disk's interior gives the injective locally Hölder map requested here, contradicting the conjectured negative answer. Its proposed proof treats injectivity and the metric estimate for the same limit map.

**The authors explicitly say that the calculations have not yet been verified by the human authors and the manuscript is not ready for arXiv.** This status records the full-scope announcement under the catalogue's announcement policy, not an accepted or independently checked proof. The draft and its qualification were checked on 3 November 2026; [scope review](../research/solution-status-audit-2026-11-03/lane-b/579.json). The separate 2016 withdrawn claim is not used.

## Collection provenance

Promoted from retained further problem **FURTHER-9ebaedcfc1da3807** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
