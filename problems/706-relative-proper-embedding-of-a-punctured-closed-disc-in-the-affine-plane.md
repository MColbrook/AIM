# 706. Relative proper embedding of a punctured closed disc in the affine plane

**Area:** Complex analysis and holomorphic embeddings
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Write $`\mathbb D=\{z\in\mathbb C:|z|<1\}`$ and let $`b\mathbb D`$ be its boundary circle. Suppose that $`f:\overline{\mathbb D}\to\mathbb C^2`$ is a holomorphic embedding, $`K\subset\mathbb C^2\setminus f(b\mathbb D)`$ is compact and polynomially convex, and $`C\subset\mathbb D`$ is compact with $`f^{-1}(K)\subset C^\circ`$. Choose any $`a\in\mathbb D\setminus C`$.

**Question (Forstnerič–Wold, Question 1.2).** For every $`\varepsilon>0`$, is there a proper holomorphic embedding
```math
g:\overline{\mathbb D}\setminus\{a\}\hookrightarrow\mathbb C^2
```

such that $`\sup_{z\in C}|g(z)-f(z)|<\varepsilon`$ and
```math
g^{-1}\!\bigl(g(\overline{\mathbb D}\setminus\{a\})\cap K\bigr)\subset C^\circ\,?
```


The closed-disc domains and the condition on $`K`$ are part of the original question. Existence of some proper embedding of a punctured disc does not imply this relative approximation statement for an arbitrary initial embedding and protected compact set.

## Application

An affirmative answer would supply a controlled way to turn an interior point into a proper end while preserving an existing embedded curve near a selected compact set. The authors identify this as a possible step toward embedding more planar domains with punctures into $`\mathbb C^2`$.

## References

1. F. Forstnerič and E. Fornæss Wold, [*Embeddings of infinitely connected planar domains into $`\mathbb C^2`$*](https://doi.org/10.2140/apde.2013.6.499), *Analysis & PDE* **6** (2013), no. 2, 499–514, Question 1.2, printed p. 500. The [official arXiv HTML, v4](https://arxiv.org/html/1110.5354v4) preserves the overbars on both source domains that PDF text extraction can lose.
2. G. D. Di Salvo and E. Fornæss Wold, [*Proper holomorphic embeddings of complements of large Cantor sets in $`\mathbb C^2`$*](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2022/0060/0002/ARKIV-2022-0060-0002-a005.pdf), *Arkiv för Matematik* **60** (2022), 323–333, introduction. The paper distinguishes known punctured-disc existence from further embedding questions.
3. A. Alarcón and F. Forstnerič, [*Embedded complex curves in the affine plane*](https://doi.org/10.1007/s10231-023-01418-8), *Annali di Matematica Pura ed Applicata* **203** (2024), 1673–1701, Lemma 1.1 and Theorem 1.2.

## Status review


**Known cases:** Proper embeddings of punctured open discs do not give the relative closed-disc-minus-point approximation and compact-set avoidance required here. Bordered-surface theorems have a different source domain.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Proper embeddings of punctured open discs do not give the relative closed-disc-minus-point approximation and compact-set avoidance required here. Bordered-surface theorems have a different source domain.

Additional comparison sources: [comparison source 1](https://doi.org/10.2140/apde.2013.6.499); [comparison source 2](https://arxiv.org/html/1110.5354v4); [comparison source 3](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2022/0060/0002/ARKIV-2022-0060-0002-a005.pdf); [comparison source 4](https://doi.org/10.1007/s10231-023-01418-8). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2013 paper proves proper embeddings for a class of infinitely connected planar domains but poses this relative puncture construction separately. The 2022 paper notes that a punctured disc can be properly embedded; that existence result has no prescribed approximation or $`K`$-avoidance. The 2024 paper proves powerful approximation and interpolation results on bordered surfaces, including proper embeddings of their interiors. Its stated hypotheses and source domain do not give the closed-disc-minus-$`a`$ conclusion above for every compact $`C`$ and polynomially convex $`K`$. Focused proof, counterexample and announcement searches through 2026-10-22 found no exact full resolution. This bounded search is not a guarantee about inaccessible work.

The checked AIM and `FURTHER_problems` pages contain no semantic duplicate. The [original-question receipt](../FURTHER_problems/_tracking/punctured-disc-relative-embedding-original-2026-10-22.json) and [later-status audit](../FURTHER_problems/_tracking/punctured-disc-relative-embedding-status-2026-10-22.json) record the formulation, scope comparisons and search limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-98061ab7564df353**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
