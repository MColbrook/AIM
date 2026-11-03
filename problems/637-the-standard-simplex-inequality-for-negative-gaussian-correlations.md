# 637. The standard simplex inequality for negative Gaussian correlations

**Area:** Gaussian probability, geometric analysis, and noise stability
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`q\geq3`$ and $`n\geq q-1`$ be integers, let $`-1<\rho<0`$, and let $`X,Z`$ be independent standard Gaussian vectors in $`\mathbb R^n`$. Set
```math
Y=\rho X+\sqrt{1-\rho^2}\,Z.
```
Thus $`X`$ and $`Y`$ both have law $`\gamma_n=N(0,I_n)`$ and $`\mathrm{Cov}(X,Y)=\rho I_n`$. For a measurable partition $`\mathcal A=(A_1,\ldots,A_q)`$ of $`\mathbb R^n`$, define its noise stability by
```math
S_\rho(\mathcal A)
=\sum_{i=1}^q\mathbb P(X\in A_i,\ Y\in A_i).
```
No balance or prescribed-volume condition is imposed on the competing cells $`A_i`$.

Choose unit vectors $`a_1,\ldots,a_q\in\mathbb R^n`$ satisfying
```math
\langle a_i,a_j\rangle=-\frac1{q-1}\quad(i\neq j),
```
and let $`\mathcal C=(C_1,\ldots,C_q)`$ be the centered regular-simplex partition
```math
C_i=\{x:\langle x,a_i\rangle=\max_{1\leq j\leq q}\langle x,a_j\rangle\},
```
with ties assigned to one cell; the ties have Gaussian measure zero. Each $`C_i`$ has Gaussian measure $`1/q`$.

Is it true that every such partition satisfies
```math
S_\rho(\mathcal A)\geq S_\rho(\mathcal C)?
```
This is the negative-correlation part of Isaksson–Mossel's standard simplex conjecture, Conjecture 1.4(ii) in the cited arXiv version. It asks for the centered, balanced simplex as a global minimum over partitions with arbitrary cell masses. The full Gaussian range $`-1<\rho<0`$ is intended; the narrower bound $`\rho\geq-1/(q-1)`$ arises in the discrete applications and is not imposed here.

## Application

The quantity $`S_\rho`$ measures how often a common classifier assigns the same label to two anticorrelated Gaussian observations. The conjecture would identify the smallest possible agreement probability and its geometric benchmark. Its range $`-1/(q-1)\leq\rho<0`$ also enters Gaussian rounding and conditional sharp approximation bounds for MAX-$`q`$-CUT.

## References

- M. Isaksson and E. Mossel, *Maximally stable Gaussian partitions with discrete applications*, Israel Journal of Mathematics **189** (2012), 347–396, [DOI: 10.1007/s11856-011-0181-7](https://doi.org/10.1007/s11856-011-0181-7). The exact formulation used here is Definition 1.3 and Conjecture 1.4(ii), p. 2 of [arXiv:0903.3362v3](https://arxiv.org/pdf/0903.3362v3).
- S. Heilman, E. Mossel, and J. Neeman, *Standard simplices and pluralities are not the most noise stable*, Israel Journal of Mathematics **213** (2016), 33–53, [DOI: 10.1007/s11856-016-1320-y](https://doi.org/10.1007/s11856-016-1320-y). Theorem 2.6 of [arXiv:1403.0885v3](https://arxiv.org/pdf/1403.0885v3) concerns shifted flat partitions with prescribed unequal masses.
- S. Heilman, *Hyperstable Sets with Voting and Algorithmic Hardness Applications*, [arXiv:2209.11216v1](https://arxiv.org/pdf/2209.11216v1) (2022), Problem 7.1 and Theorems 7.9 and 8.5.
- S. Heilman, *Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT*, [arXiv:2608.00333v1](https://arxiv.org/pdf/2608.00333v1) (2026), Theorem 7.1, p. 21, and the future-work discussion on p. 8.

## Status review


**Known cases:** The three-cell 2026 negative-correlation result covers only a subrange of correlations. It does not settle all q>=3 and -1<rho<0. Unequal-mass comparisons and conditional hyperstability classifications do not refute or prove the centered-simplex benchmark here.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The 2026 preprint claims the displayed inequality for $`q=3`$, every $`n\geq2`$, and $`-1/2\leq\rho<0`$, without a balance condition or a Unique Games assumption on this Gaussian theorem. This is partial progress on the full question. Its computational certificates have not been reproduced in this review. The paper identifies the extension to four or more cells and to the full correlation range as further work.

The 2022 paper studies a stronger bilinear minimization problem with two partitions whose corresponding masses match, while those masses are otherwise free. Its dimension reduction does not itself identify regular-simplex optimizers. The regular-cone conclusion for up to four cells in Theorem 8.5 requires the additional hyperstability assumption.

The unequal-volume counterexamples in Theorem 2.6 of Heilman–Mossel–Neeman include negative correlations. They compare an unequal-mass shifted partition with better competitors having those same prescribed masses; they do not compare against the centered, equal-mass benchmark in the question above.

This differs from [AIM 294](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/294-gaussian-simplex.md), which asks about positive-correlation maximization under equal cell masses. The OpenAI Gaussian propeller announcement concerns a Gaussian first-moment bound, rather than the full fixed-correlation functional here. No matching complete resolution or counterexample was located in the checked primary literature, current announcements, or the current AIM, FURTHER, and OpenAI records.

The endpoints omitted from the question are immediate: $`S_{-1}(\mathcal C)=0`$, while $`S_0(\mathcal A)=\sum_i\gamma_n(A_i)^2\geq1/q`$.



### Online recheck, 2026-10-30

The three-cell 2026 negative-correlation result covers only a subrange of correlations. It does not settle all q>=3 and -1<rho<0. Unequal-mass comparisons and conditional hyperstability classifications do not refute or prove the centered-simplex benchmark here.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2608.00333); [status source 2](https://arxiv.org/abs/2209.11216); [status source 3](https://arxiv.org/abs/0903.3362). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-e672ccf566fc3b55** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
