# 523. Can adaptive Monte Carlo approximate a noncompact operator?

**Area:** Information-based complexity / operator approximation
**Status:** ✅ SOLVED
**Last checked:** 2026-11-04

## Problem statement

Let $`I:\ell_1(\mathbb N;\mathbb R)\to\ell_\infty(\mathbb N;\mathbb R)`$ be the identity inclusion and $`B=\{x:\|x\|_1<1\}`$. An algorithm may sequentially query continuous linear functionals on $`\ell_1`$, choose later queries and its stopping rule from the answers and a random seed $`\omega`$, and return $`A_\omega(x)\in\ell_\infty`$. Write $`N(x,\omega)`$ for its finite number of queries. Require the cardinality and output maps to be jointly measurable for the norm Borel structures, and impose the expected cost bound $`\sup_{x\in B}\mathbb E N(x,\omega)\le n`$.

Define
```math
e_n(I)=\inf_A\sup_{x\in B}\bigl(\mathbb E\|x-A_\omega(x)\|_\infty^2\bigr)^{1/2}.
```

Is there a constant $`c>0`$ such that $`e_n(I)\ge c`$ for every $`n\ge1`$? Equivalently, is $`\lim_{n\to\infty}e_n(I)>0`$?

## Application

This asks whether randomization and adaptive measurements can give uniformly accurate recovery even when the operator is not compact. The source reduces the general compactness-necessity question for bounded linear operators between Banach spaces to this one inclusion.

## Status review

**Resolution:** The [manuscript](../research/solutions/523-adaptive-monte-carlo-error-floor/main.pdf) proves the exact identity $`e_n(I)=1/2`$ for every $`n\ge1`$ in the stated adaptive expected-budget RMS model. Its lower bound allows arbitrary history-to-query rules and the required joint output/count measurability. The one-query upper bound returns the constant sequence with value $`\tfrac12\sum_jx_j`$. This resolves the full displayed question affirmatively.

**Audit, 4 November 2026:** The solutions were found by AI and are written up by Matthew J. Colbrook. A [fresh independent AI audit](../research/solution_reviews/2026-11-04-numerical-analysis/523-review.md) checked the submitted argument, target match and dependencies. No independent human review or formal verification is claimed.

### Earlier status history

Nonadaptive Monte Carlo methods have a positive error floor, and cannot approximate noncompact operators arbitrarily well in the model of Kunsch, Novak and Wnuk (2024). Their Remark 2.10 still discusses the adaptive case as a conjectural extension. Their strict-budget, expected-norm model has additional measurement-selection measurability assumptions; the question above retains the expected-budget, root-mean-square model of the 2011 source. Dimension-dependent adaptive algorithms on finite sequence spaces do not automatically answer the infinite-dimensional question. The particular value $`1/2`$ is not part of the target.

Reviewed through 18 October 2026; independent selected review passed; catalogue comparison and coordinator review pending. The final 2013 and 2024 publication bodies have not been compared with the available primary manuscripts.



### Online recheck, 2026-10-30

The September 2026 high-dimensional-vector article retains dimension dependence, albeit log log m, in adaptive bounds. It does not make the infinite-dimensional noncompact inclusion approximable, nor prove an adaptive error floor in the expected-budget RMS model.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2308.01705); [status source 2](https://arxiv.org/abs/2410.23067); [status source 3](https://doi.org/10.1016/j.jat.2026.106318). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References

1. A. Hinrichs, E. Novak and H. Woźniakowski, *Discontinuous information in the worst case and randomized settings*, [arXiv:1106.2945v1](https://arxiv.org/abs/1106.2945v1), §3, Remark 5, p. 13. Published in *Mathematische Nachrichten* **286** (2013), 679–690, [DOI](https://doi.org/10.1002/mana.201100128). The [16 September 2011 author version](https://users.fmi.uni-jena.de/~novak/triebel_arxive.pdf) retains this question.
2. R. J. Kunsch, E. Novak and M. Wnuk, *Randomized approximation of summable sequences—adaptive and non-adaptive*, *Journal of Approximation Theory* **304** (2024), 106056, [DOI](https://doi.org/10.1016/j.jat.2024.106056); reviewed [arXiv:2308.01705v3](https://arxiv.org/abs/2308.01705v3), Corollary 2.9, Remark 2.10 and Theorem 2.11.

The [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/randomized-compactness-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-randomized-compactness-review.json), [semantic comparison](../FURTHER_problems/_tracking/randomized-compactness-duplicates-coordinator-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/randomized-compactness-catalogue-coordinator-2026-10-18.json) and [coordinator decision](../FURTHER_problems/_tracking/randomized-compactness-coordinator-review-2026-10-18.json) record the exact checks and access limits. All five catalogue contexts were unrelated. Current retrieved manuscript dates differ internally; no historical byte parity or exhaustive absence of later results is certified.

## Collection provenance

Promoted from retained further problem **FURTHER-0883cceb05b0dcdd** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
