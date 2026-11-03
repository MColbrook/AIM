# 193. When is a random tree built by attaching prescribed branches compact?

**Area:** Probability on real trees and random geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(a_i)_{i\ge1}`$ be an arbitrary **bounded deterministic** sequence of positive lengths. Start with a segment of length $`a_1`$. At step $`n+1`$, choose a point uniformly according to length measure on the existing finite tree and attach to it a new segment of length $`a_{n+1}`$. Let $`\mathcal T`$ be the metric completion of the union of these finite trees.

Find a necessary and sufficient condition on $`(a_i)`$ for $`\mathcal T`$ to be bounded almost surely. For this construction, Curien and Haas state this equivalently as almost-sure compactness [1, Open Question 2.12]. The question is for **general bounded sequences**, with no monotonicity or regular-variation assumption.

## Application

The branch lengths determine whether the limiting random real tree is a compact metric space, a basic prerequisite for geometric scaling-limit arguments. A criterion based on a typical sampled point does not control the longest thin branches; the question asks for a condition that controls the whole tree.

## Known results and scope

If $`\sum_i a_i<\infty`$, compactness follows without using the random attachment rule [1, Proposition 4.1]. The original paper also proves compactness under polynomial-type decay of the branch lengths [1, Proposition 3.1]. For **decreasing** lengths, Amini, Devroye, Griffiths and Olver obtain the exact criterion $`\sum_i a_i/i<\infty`$ [2, Theorem 1.11]. Curien and Haas give a nonmonotone example where this sum is finite but the limiting tree is unbounded [1, discussion after Open Question 2.12].

Donderwinkel and van Haastert establish additional compact and noncompact families in a related Poisson-intensity setting, and describe their 2026 results as partial progress on the Curien–Haas question [3]. They do not characterize all bounded deterministic branch-length sequences.

## References

1. N. Curien and B. Haas, [*Random trees constructed by aggregation*](https://www.math.univ-paris13.fr/~haas/AIF2017675.pdf), *Annales de l'Institut Fourier* **67** (2017), no. 5, 1963–2001, Open Question 2.12. [DOI](https://doi.org/10.5802/aif.3126).
2. O. Amini, L. Devroye, S. Griffiths and N. Olver, [*Explosion and linear transit times in infinite trees*](https://arxiv.org/abs/1411.4426), *Probability Theory and Related Fields* **167** (2017), nos. 1–2, 325–347, Theorem 1.11. [DOI](https://doi.org/10.1007/s00440-015-0683-z).
3. S. Donderwinkel and J. van Haastert, [*Convergence and compactness of discrete aggregation trees*](https://arxiv.org/abs/2609.13066), September 2026, Introduction and Theorems 1.2–1.5.

## Status review


**Known cases:** Known monotone/summable/regularly varying branch-length criteria and the 2026 discrete-aggregation results do not give a necessary and sufficient compactness criterion for every bounded deterministic sequence in the continuous uniform-length attachment model.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The [primary-source, later-result and duplicate review](../FURTHER_problems/_tracking/random-aggregation-tree-compactness-status-2026-10-21.json) separates the general deterministic-length question from decreasing-sequence and random-length special cases. No complete general criterion or announced settlement was found in a bounded search through 21 October 2026.


### Online recheck, 2026-10-30

Known monotone/summable/regularly varying branch-length criteria and the 2026 discrete-aggregation results do not give a necessary and sufficient compactness criterion for every bounded deterministic sequence in the continuous uniform-length attachment model.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2609.13066); [status source 2](https://arxiv.org/abs/1411.4255); [status source 3](https://www.math.univ-paris13.fr/~haas/AIF2017675.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-06da11031b621311** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
