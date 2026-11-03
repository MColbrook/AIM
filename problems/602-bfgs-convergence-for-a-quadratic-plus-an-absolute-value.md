# 602. BFGS convergence for a quadratic plus an absolute value

**Area:** Continuous optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`f:\mathbb R^2\to\mathbb R`$ be
```math
f(u,v)=u^2+|v|.
```

Fix $`0<c_1<c_2<1`$ and a symmetric positive definite matrix $`H_0\in\mathbb R^{2\times2}`$. Consider any infinite sequence $`x_k=(u_k,v_k)`$, with $`v_k\ne0`$ for every $`k`$, generated as follows. At each step put
```math
g_k=\nabla f(x_k)=(2u_k,\mathrm{sgn}v_k)^T,
 \qquad p_k=-H_kg_k,
 \qquad x_{k+1}=x_k+a_kp_k,
```

where $`a_k>0`$ satisfies the Armijo and weak Wolfe conditions
```math
f(x_{k+1})\le f(x_k)+c_1a_kg_k^Tp_k,
 \qquad g_{k+1}^Tp_k\ge c_2g_k^Tp_k.
```

With $`s_k=x_{k+1}-x_k`$, $`y_k=g_{k+1}-g_k`$ and $`\rho_k=(y_k^Ts_k)^{-1}`$, use the full inverse BFGS update
```math
H_{k+1}=(I-\rho_ks_ky_k^T)H_k(I-\rho_ky_ks_k^T)
                  +\rho_ks_ks_k^T.
```

The conditions imply $`y_k^Ts_k>0`$, so this update is well defined.

**Conjecture.** Every such sequence converges to the unique minimizer $`(0,0)`$.

The quantifier covers all positive definite initial matrices and all accepted steps satisfying the two inequalities. It does not prescribe a particular line-search implementation or a convergence rate. The restriction $`v_k\ne0`$ is part of the source's definition: the conjecture concerns infinite BFGS sequences at differentiable points, without assigning a gradient or an update at a kink. Equivalently, the question is whether $`f(x_k)\to0`$.

## Application
BFGS is frequently used on nonsmooth objectives despite having been designed for smooth optimization. This small convex example tests whether its changing metric can prevent convergence to a nonoptimal point on the nonsmooth line. The source proves that every such sequence has a subsequence approaching that line; this does not establish convergence to the minimizer. It also gives particular convergent sequences and proves convergence for the Euclidean norm, which is a different objective.

## References

1. J. Guo and A. S. Lewis, *Nonsmooth variants of Powell's BFGS convergence theorem*, SIAM Journal on Optimization **28** (2018), 1301–1311, [DOI](https://doi.org/10.1137/17M1121883). [Revised author manuscript](https://people.orie.cornell.edu/aslewis/publications/18-nonsmooth.pdf), Definition 2.1 on p. 3 and the explicit conjecture following Corollary 4.4 on p. 9. The eligible earlier version is [arXiv:1703.06690v1](https://arxiv.org/abs/1703.06690v1), where the conjecture follows Corollary 4.5 on p. 10.
2. B. Gebken, *Technical results on the convergence of quasi-Newton methods for nonsmooth optimization*, Journal of Optimization Theory and Applications **209** (2026), article 57, [DOI](https://doi.org/10.1007/s10957-026-03008-z). The introduction explicitly retains this example as unresolved; the convergence results impose additional conditions on the quasi-Newton matrices.

## Status review

The 2026 results inspected for smooth convex BFGS require a globally Lipschitz gradient, which this objective does not have. The September 2026 announcement [arXiv:2609.09872v1](https://arxiv.org/abs/2609.09872v1) concerns initialization dependence of trial-normalized rates for a one-dimensional tilted absolute value. Its two constructed executions converge, and its rate counterexample does not disprove this two-dimensional convergence conjecture. Limited-memory, smoothed-objective and modified-update methods also differ from the full BFGS iteration above.

The eligible 2017 preprint and the revised 2018 author manuscript were read in full. The publisher's final PDF has not been compared with the revised author manuscript. Current searches have not located a complete proof or counterexample for the stated target; the independent selected-primary audit and catalogue comparison have been completed at the recorded extents.

The all-status AIM/OpenAI and FURTHER comparisons located no equivalent target. Every186-page cached catalogue job was checked under five aliases; all87 target-centred navigation excerpts and four potentially material full windows were read. Remaining window tails and complete mission proofs were not audited.

[Primary and current-status packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/bfgs-quadratic-absolute-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-bfgs-quadratic-absolute-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/bfgs-prove2-0117-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/bfgs-coordinator-review-2026-10-17.json) retain precise source versions, hypotheses and bounded search limits.


### Online recheck, 2026-10-30

The 2026 nonsmooth quasi-Newton paper retains assumptions on matrix eigenvalues that are not established for all executions. Smooth-convex, isolated-nonsmooth-minimum, one-dimensional rate and modified/L-BFGS results do not prove the u^2+|v| all-Armijo–Wolfe-sequence conjecture.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/s10957-026-03008-z); [status source 2](https://arxiv.org/abs/2511.03296); [status source 3](https://people.orie.cornell.edu/aslewis/publications/18-nonsmooth.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-072328cf729a616d** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
