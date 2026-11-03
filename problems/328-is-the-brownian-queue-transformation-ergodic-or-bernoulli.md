# 328. Is the Brownian queue transformation ergodic or Bernoulli?

**Area:** Probability and ergodic theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`X=(X(t))_{t\in\mathbb R}`$ be a two-sided standard Brownian motion with constant drift $`\nu>0`$, pinned by $`X(0)=0`$. On its path space with the Brownian-with-drift law, define
```math
M_X(t)=\sup_{-\infty<s\leq t}X(s),\qquad
(TX)(t)=2M_X(t)-X(t)-2M_X(0),\quad t\in\mathbb R.
```

The past supremum is finite almost surely, and the continuous Brownian analogue of Burke's theorem gives $`TX\stackrel d=X`$ [1, §3].

**Question.** Is this measure-preserving transformation $`T`$ ergodic? Is it metrically isomorphic to a two-sided Bernoulli shift?

These are the two levels of the question explicitly posed in [1, §3]. The answer may depend on $`\nu`$; the paper poses it for positive drift. The question concerns the transformation of the **entire two-sided continuous path**, not only its known Bernoulli factor or the discrete queue map.

## Application

Burke-type output theorems say that a stationary queue's output has the same law as its input. Ergodicity or Bernoulli behavior of the full path transformation would describe how much randomness remains dynamically coupled across repeated queue transformations, beyond equality in distribution of a single output.

## Known results

Keane and O'Connell prove that the analogous discrete random-walk queue transformation is Bernoulli [1, Theorem 2.2]. For the continuous Brownian transformation, they obtain a two-sided i.i.d. exponential factor: the variables $`M_{T^kX}(0)`$, $`k\in\mathbb Z`$, have exponential law with parameter $`2\nu`$ and shift under $`T`$ [1, §3]. They explain that recovery of $`X`$ from this sequence is unknown. A Bernoulli factor alone does not settle ergodicity of the whole transformation.

A later continuous box-ball/Pitman-transform study proves invariance of the same positive-drift Brownian law and describes the i.i.d. current sequence [2, Theorem 5.9 and Remark 5.15]. Its discrete configuration ergodicity results and its continuous-law invariance theorem do not establish ergodicity or Bernoulli behavior of this full Brownian-path map. Its Section 6 still raises the general continuous-dynamics ergodicity question. A 2026 review likewise distinguishes Brownian invariance from discrete box-ball ergodicity [3, §3.4]. Lévy's Brownian transformation, mentioned by [1] as an analogy, is a different map.

## References

1. M. Keane and N. O'Connell, [*The M/M/1 queue is Bernoulli*](https://arxiv.org/pdf/0804.3935v1), *Colloquium Mathematicum* **110** (2008), no. 1, 205–210, [DOI](https://doi.org/10.4064/cm110-1-9), Section 3 (Brownian version), especially the formula and final open-question sentence on physical p. 4; Section 2, Theorem 2.2 for the discrete result. [Published PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/87112).
2. D. A. Croydon, T. Kato, M. Sasada and S. Tsujimoto, [*Dynamics of the box-ball system with random initial conditions via Pitman's transformation*](https://arxiv.org/pdf/1806.02147), *Memoirs of the American Mathematical Society* **283** (2023), no. 1398, Section 5.4, Theorem 5.9 and Remark 5.15, and Section 6, question (6). [Publisher record](https://doi.org/10.1090/memo/1398).
3. M. Sasada, [*Box-ball System and Related Discrete Integrable Systems with Random Initial Conditions*](https://epubs.siam.org/doi/full/10.1137/25M1806715), *Proceedings of the International Congress of Mathematicians 2026*, Section 3.4 (invariance and discrete ergodicity).

## Status review

The [primary-body and later-work review](../FURTHER_problems/_tracking/brownian-queue-pitman-ergodicity-status-2026-10-21.json) records the exact question, later scope checks, current searches and semantic duplicate check. No complete proof or announcement for this exact Brownian transformation was located through 21 October 2026 in that bounded search; this does not certify exhaustive absence.


### Online recheck, 2026-10-30

The discrete M/M/1 transformation is Bernoulli and the Brownian map has a Bernoulli factor. Neither proves ergodicity or Bernoulli isomorphism of the entire two-sided continuous Brownian-with-positive-drift transformation.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/0804.3935); [status source 2](https://arxiv.org/abs/1806.02147); [status source 3](https://doi.org/10.1137/25M1806715). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ba52145912456216** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
