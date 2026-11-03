# 616. Weak convergence under subcritical vanishing damping

**Area:** Continuous optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`H`$ be a real Hilbert space and let $`\Phi:H\to\mathbb R`$ be convex and continuously Fréchet differentiable, with $`\nabla\Phi`$ Lipschitz on bounded sets. Assume that $`S=\mathrm{argmin}_H\Phi\ne\varnothing`$. Fix $`t_0>0`$ and $`1<\alpha<3`$. For arbitrary initial position and velocity in $`H`$, consider the global classical solution of
```math
\ddot x(t)+\frac{\alpha}{t}\dot x(t)+\nabla\Phi(x(t))=0,
 \qquad t\ge t_0.
```


**Problem.** Must there be a point $`x_\infty\in S`$ such that $`x(t)\rightharpoonup x_\infty`$ as $`t\to\infty`$?

No boundedness of the trajectory or of $`S`$, coercivity, strong convexity or additional regularization is assumed. In finite dimensions the question is ordinary norm convergence; in an arbitrary Hilbert space the target is weak convergence.

## Application
The equation models inertial methods for minimizing a convex function with damping that decreases over time. Convergence of objective values need not by itself imply convergence of the state. Attouch, Chbani and Riahi explicitly discuss the trajectory question in §3.2 and Remark 3.5. Their Theorem 2.1 gives objective-value estimates in the subcritical regime; their Theorem 3.6 proves strong convergence when the minimum has the stated quadratic growth.

The lower endpoint is deliberate. For $`\Phi\equiv0`$, a nonzero initial velocity gives a divergent trajectory when $`0<\alpha\le1`$, whereas the free trajectory converges when $`\alpha>1`$. The familiar weak-convergence results for $`\alpha>3`$ do not settle the question above.

## References

1. H. Attouch, Z. Chbani and H. Riahi, *Rate of convergence of the Nesterov accelerated gradient method in the subcritical case $`\alpha\le3`$*, ESAIM: Control, Optimisation and Calculus of Variations **25** (2019), article 2, 34 pp. [Published article](https://doi.org/10.1051/cocv/2017083), especially §2 (standing assumptions), §3.2 and Remark 3.5; see also §3.3 for the strong-minimum case.
2. U. Jang and E. K. Ryu, [arXiv:2510.23513v2](https://arxiv.org/abs/2510.23513v2), 19 January 2026, Theorem 2.2 in the PDF (Theorem 2 in the HTML). The inspected current theorem concerns critical damping $`\alpha=3`$ in its stated finite-dimensional setting. Its hypotheses and initial-condition convention should be read as printed; no extension to arbitrary Hilbert spaces or arbitrary initial conditions is inferred here.

## Status review

An earlier version of reference 2 included a subcritical convergence claim under an additional bounded-minimizer-set hypothesis. The authors explicitly correct that argument as invalid in §4.3 of the current version. This candidate does not rely on the earlier claim; the correction concerns that argument, rather than the general convergence question. The available current checks have not located a resolution of the general problem stated above; the independent selected-primary review and the dated announcement comparison are recorded below.

The186-page all-status catalogue scan yielded497 distinct windows. Every target-centred navigation excerpt and27 potentially material full windows were inspected; remaining tails and mission proofs are not claimed reviewed. The all-status AIM/OpenAI and FURTHER comparisons located no equivalent target at the recorded extents.

[Source and current-status review](../FURTHER_problems/_tracking/parallel/complex-bayesian/subcritical-avd-convergence-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-subcritical-avd-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/subcritical-prove2-0113-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/subcritical-avd-coordinator-review-2026-10-17.json) preserve exact source versions, hypotheses and search limits.


### Online recheck, 2026-10-30

The corrected January 2026 Jang–Ryu version does not retain its earlier subcritical convergence argument. Critical damping alpha=3, rates for objective values, and bounded/strong-minimum special cases do not prove arbitrary-Hilbert weak convergence for 1<alpha<3.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2510.23513); [status source 2](https://doi.org/10.1051/cocv/2017083). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-dd0bbee17368fecd** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
