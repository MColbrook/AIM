# 642. Hunt's hypothesis for driftless subordinators

**Area:** Probability and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\nu`$ be a Borel measure on $`(0,\infty)`$ with
```math
\int_0^\infty (1\wedge r)\,\nu(dr)<\infty,
\qquad \nu((0,\infty))=\infty.
```

Let $`S=(S_t)_{t\ge0}`$ be the conservative subordinator with $`S_0=0`$ and Laplace transform
```math
\mathbb E e^{-\lambda S_t}
=\exp\!\left[-t\int_0^\infty(1-e^{-\lambda r})\,\nu(dr)\right]
\quad(\lambda,t\ge0).
```

Thus its deterministic drift and killing rate are zero. For $`x\in\mathbb R`$, let $`\mathbb P^x`$ be the law of $`x+S`$, and for a Borel set $`A\subset\mathbb R`$ put
```math
T_A=\inf\{t>0:x+S_t\in A\},\qquad\inf\varnothing=\infty.
```

Is the following implication true for every such $`\nu`$ and every Borel set $`A`$?
```math
\boxed{\quad
\bigl[\mathbb P^x(T_A=0)=0\ \text{for every }x\in\mathbb R\bigr]
\ \Longrightarrow\
\bigl[\mathbb P^x(T_A<\infty)=0\ \text{for every }x\in\mathbb R\bigr].
\quad}
```

The hypothesis says that $`A`$ is thin and the conclusion that it is polar. Requiring this for Borel thin sets is equivalent to Hunt's hypothesis (H), usually expressed using all semipolar sets; the reduction is the cited Lemma 2.1. No density, regular variation or symmetry assumption is imposed on $`\nu`$.

## Application

Subordinators provide random clocks for Markov processes. A known subordination theorem says that if an independent clock satisfies (H), then the time-changed standard Markov process satisfies (H). A positive answer would therefore extend this potential-theoretic regularity result to every conservative driftless infinite-activity subordinator.

## References

1. Z.-C. Hu and W. Sun, *Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond*, [arXiv:1908.06825v1](https://arxiv.org/pdf/1908.06825v1), definitions pp. 1–2, subordinator discussion pp. 10–11, Theorem 2.31 p. 13, Question 5 p. 25. Published in *Acta Mathematica Sinica, English Series* **37** (2021), 491–508, [doi:10.1007/s10114-021-9343-7](https://doi.org/10.1007/s10114-021-9343-7).
2. Z.-C. Hu, W. Sun and L.-F. Wang, *Two Theorems on Hunt's Hypothesis (H) for Markov Processes*, [arXiv:1903.00050v1](https://arxiv.org/html/1903.00050v1), introduction, Theorems 1.2–1.3 and Lemma 2.1 with its proof. The lemma gives the Borel thin-set formulation above.

## Status review


**Known cases:** Known special driftless subordinators and decompositions into two clocks satisfying (H) do not imply (H) for every driftless infinite-activity subordinator; closure under arbitrary sums is not supplied.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 18 October 2026. This is the first clause of Question 5 in the survey. Finite Lévy measure gives a compound Poisson process and is already known. The hypothesis is also known for driftless special subordinators and locally quasi-stable subordinators. Positive deterministic drift is an obstruction, so it is excluded explicitly.

The known decomposition of some subordinators into two independent processes satisfying (H) does not resolve the question: preservation under arbitrary sums is another question in the source. Theorems about positive-drift time changes likewise do not prove that the driftless clock itself satisfies (H).

The pinned 27-page preprint has been read completely. The final 18-page publisher body has not been compared: one ordinary PDF request returned an HTML article page. Bounded current searches found no matching complete resolution. Independent formulation, semantic and coordinator comparisons passed; all 186 cached catalogue descriptions were scanned, and the single surname hit concerns a reference in an unrelated optimal-stopping mission. No proof of the assertion is claimed.

The [primary review](../FURTHER_problems/_tracking/parallel/rough-filtering/hunt-subordinator-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-hunt-subordinator-review.json), [semantic comparison](../FURTHER_problems/_tracking/hunt-subordinator-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/hunt-subordinator-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/hunt-subordinator-coordinator-review-2026-10-18.json) record the scope and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

Known special driftless subordinators and decompositions into two clocks satisfying (H) do not imply (H) for every driftless infinite-activity subordinator; closure under arbitrary sums is not supplied.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1908.06825); [status source 2](https://arxiv.org/abs/1406.2013); [status source 3](https://arxiv.org/abs/1210.2016). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-57e9893a2f4942a6** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
