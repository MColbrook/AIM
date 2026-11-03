# 601. Polynomial-query convex optimization with almost linear memory

**Area:** Continuous optimization and first-order oracle complexity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Write $`B_2^d=\{x\in\mathbb R^d:\|x\|_2\le1\}`$ and, for integers $`d\ge3`$, put
```math
\varepsilon_d=\exp\!\bigl(- (\log d)^2\bigr),
```

where $`\log`$ is the natural logarithm. Let $`\mathcal F_d`$ consist of all convex, globally $`1`$-Lipschitz functions $`F:\mathbb R^d\to\mathbb R`$ having a global minimizer in $`B_2^d`$.

Do constants $`C,k>0`$ and $`d_0\ge3`$ exist such that, for every integer $`d\ge d_0`$, there is a deterministic first-order oracle algorithm with the following guarantee?

It uses at most $`M_d=\lceil C d(\log d)^2\rceil`$ persistent bits and at most $`T_d=\lceil d^k\rceil`$ oracle calls, and for every $`F\in\mathcal F_d`$ returns $`\widehat x\in\mathbb R^d`$ satisfying
```math
F(\widehat x)-\min_{x\in\mathbb R^d}F(x)\le\varepsilon_d.
```

Each query at $`x_t\in\mathbb R^d`$ returns the exact pair $`(F(x_t),g_t)`$, with $`g_t\in\partial F(x_t)`$. The guarantee must hold for every choice of valid returned subgradients, as in the source's minimax convention. [1, §2]

Precisely, the persistent state is $`\mu_t\in\{0,1\}^{M_d}`$, initially zero. For maps fixed before observing $`F`$,
```math
x_t=\phi_{d,t}(\mu_t),\qquad
\mu_{t+1}=\psi_{d,t}(\mu_t,F(x_t),g_t),\qquad
\widehat x=\zeta_d(\mu_{T_d+1}).
```

The maps may depend on $`d,t`$ and use unrestricted real computation and temporary memory between calls; only the retained state is limited to $`M_d`$ bits. Neither query locations nor the final output have additional storage outside this state. The time index is available to the maps. No bound on arithmetic work or a uniform finite-program implementation is requested. Fewer calls can be padded. These conventions reproduce the deterministic bottleneck model in [1], with the final-state index written consistently.

This is a fixed-accuracy specialization of Question 2 in [1], rather than a claim that its entire memory-query tradeoff is unresolved. All dimensions form one problem family.

## Application

The question separates the cost of acquiring first-order information from the memory needed to retain it. It asks whether an optimizer can attain high accuracy using nearly the amount of information needed merely to encode its answer, while making only polynomially many oracle calls. Since between-call computation is unrestricted, a positive answer alone would not give an efficient implementation. [1, §§1–4]

## References

1. B. Woodworth and N. Srebro, *Open Problem: The Oracle Complexity of Convex Optimization with Limited Memory*, COLT 2019, Proceedings of Machine Learning Research **99**, 3202–3210. [Published full text](https://proceedings.mlr.press/v99/woodworth19a/woodworth19a.pdf), §§2–4, Question 2; Appendix A. Eligible preprint: [arXiv:1907.00762](https://arxiv.org/abs/1907.00762).
2. M. Blanchard, J. Zhang and P. Jaillet, *Memory-Constrained Algorithms for Convex Optimization*, NeurIPS 2023. [Published full text](https://proceedings.nips.cc/paper_files/paper/2023/file/1395b425d06a50e42fafe91cf04f3a98-Paper-Conference.pdf), Theorems 3.2–3.3 and §5. The arXiv title adds “via Recursive Cutting-Planes.”
3. M. Blanchard, *Gradient Descent is Pareto-Optimal in the Oracle Complexity and Memory Tradeoff for Feasibility Problems*, FOCS 2024. [Published full text](https://ieee-focs.org/FOCS-2024-Papers/pdfs/FOCS2024-1oojWxXs5YAKfs3z3lBRMF/167400c413/167400c413.pdf), introduction, Theorems 1–2 and explicit distinction on p. 3 between feasibility and convex-optimization lower bounds.
4. M. Blanchard, J. Zhang and P. Jaillet, *Quadratic Memory Is Necessary for Optimal Query Complexity in Convex Optimization: Center of Mass Is Pareto Optimal*, Mathematics of Operations Research **50** (2025), 2941–2971. [Published author-hosted copy](https://web.mit.edu/jaillet/www/general/bzj-mor25.pdf), Theorem 1 and §2; [DOI](https://doi.org/10.1287/moor.2023.0208).
5. M. Menart, A. Nikolov and O. Shamir, *Stronger Memory-Query Tradeoffs for Convex Optimization: The Limitations of Subquadratic Memory*, [arXiv:2607.24827v1](https://arxiv.org/html/2607.24827v1), July 21, 2026, §§1–2 and Theorems 1–2. Preprint, used only for current status.

## Status review


**Known cases:** July 2026 memory/query lower bounds force larger polynomial exponents, not superpolynomial queries for every exponent. Feasibility-oracle lower bounds do not automatically transfer to the narrower global-minimizer first-order model; no matching complete answer found.

**Known progress:** Discretized gradient descent uses $`O(d\log(1/\varepsilon_d))=O(d(\log d)^2)`$ persistent bits, with an available $`O(\varepsilon_d^{-2})=\exp(O((\log d)^2))`$ query bound [1, Appendix A]. This is superpolynomial in $`d`$. Cutting-plane methods achieve polynomial query bounds using more memory. The recursive cutting-plane upper bounds in [2, Theorem 3.2] do not supply a polynomial-query method with the displayed almost linear memory allowance.

**Remaining target:** Establish or refute the existence of the constants and algorithm family in the problem statement. A polynomial lower bound on the required number of calls does not refute this target, because its polynomial exponent $`k`$ is not prescribed.

The deterministic lower bound in [4] and the sharper bounds in [5] rule out nearly optimal query counts with too little memory in their ball-constrained optimization models. They do not assert that every fixed polynomial query budget is insufficient for the stated accuracy. Moreover, the source class here requires a global minimizer in the unit ball, while these comparator models minimize over the ball; no lower-bound transfer to this narrower class is assumed. The accuracy-dependent lower bounds in [3] concern the broader separation-oracle feasibility problem; the paper expressly warns that these do not imply corresponding lower bounds for first-order convex optimization. The recursive algorithm in [2] also relies on oracle consistency for recomputation; no transfer of that assumption to the broader subgradient convention here is asserted.

**Literature check:** Source and current comparisons checked October 18, 2026. No matching complete solution located in the inspected primary statements. This is a bounded literature review, not a certification that no proof exists. Catalogue and independent audit receipts accompany the research packet.

The [primary packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/memory-convex-polynomial-query-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-memory-convex-polynomial-query-review.json), [semantic comparison](../FURTHER_problems/_tracking/limited-memory-convex-duplicates-review-2026-10-18.json), [catalogue review](../FURTHER_problems/_tracking/limited-memory-convex-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/limited-memory-convex-coordinator-review-2026-10-18.json) record exact evidence and review limits.


### Online recheck, 2026-10-30

July 2026 memory/query lower bounds force larger polynomial exponents, not superpolynomial queries for every exponent. Feasibility-oracle lower bounds do not automatically transfer to the narrower global-minimizer first-order model; no matching complete answer found.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2607.24827); [status source 2](https://proceedings.mlr.press/v99/woodworth19a/woodworth19a.pdf); [status source 3](https://arxiv.org/abs/2306.12534). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-a16c71c960582bfb** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
