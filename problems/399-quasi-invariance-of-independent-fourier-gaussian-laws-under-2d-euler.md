# 399. Quasi-invariance of independent-Fourier Gaussian laws under 2D Euler

**Area:** Two-dimensional Euler dynamics and Gaussian measures
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On the flat torus $`\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2`$, consider the two-dimensional Euler equation in vorticity form
```math
\partial_t\omega+u\cdot\nabla\omega=0,\qquad
u=\nabla^\perp(-\Delta)^{-1}\omega,
```

with flow $`\Phi_t`$. Fix $`\sigma>0`$. Let $`a=(a_n)_{n\in\mathbb Z^2}`$ be real, $`a_0=0`$, $`a_{-n}=a_n`$, and
$`\sum_n\langle n\rangle^{2\sigma}|a_n|^2<\infty`$. For one representative of each pair $`n,-n`$, take $`g_n=r_n+is_n`$ with independent real standard Gaussians $`r_n,s_n`$, imposing $`g_{-n}=\overline{g_n}`$, and let $`\mu_a`$ be the law of
$`\omega_0(x)=\sum_n a_ng_ne^{in\cdot x}`$. Define its active support $`S(a)=\{n\ne0:a_n\ne0\}`$. For $`0<\alpha<\min(\sigma,1)`$, the random data almost surely belong to the little Hölder space $`c_0^\alpha`$, for which the cited later work uses a global Borel Euler flow.

Is $`(\Phi_t)_*\mu_a`$ equivalent to $`\mu_a`$ for every $`t\in\mathbb R`$ **if and only if** $`S(a)`$ is contained in one line through the origin or one circle centered at the origin?

This is the $`\sigma>0`$ part of Bedrossian–Latocca Conjecture 1.10. Their parenthetical possibility of $`\sigma>-1`$, conditional on a suitable well-posedness theory, is outside the question retained here. The Gaussian law is restricted to mutually independent Fourier modes as above; arbitrary Gaussian measures are outside the target.

## Application

Quasi-invariance asks whether Euler evolution preserves the null sets of this family of random-vorticity laws. It can transfer almost-sure properties between initial and evolved data, so it is stronger information than a test showing that a law changes under the flow.

## References

1. Jacob Bedrossian and Mickaël Latocca, *Non-invariance of Gaussian measures under the 2D Euler flow*, *Ann. Inst. H. Poincaré C Anal. Non Linéaire* **43** (2026), 1419–1453, [published article](https://doi.org/10.4171/AIHPC/175), Conjecture 1.10 on printed p. 1425; equations (E), (1.1), (1.2) and Assumptions 1.1–1.2.
2. Ziyu Liu, *On the classification of invariant Gaussian measures for the 2D Euler equation*, [arXiv:2608.01019v1](https://arxiv.org/html/2608.01019v1), Theorems A and B. Theorem A treats **invariance** for all $`\sigma>0`$; Theorem B treats **quasi-invariance** when active modes lie in a finite union of lines.
3. Anne-Sophie de Suzzoni and Mickaël Latocca, *Obstruction to quasi-invariance of Gaussian measures under transport flows on Riemannian Manifolds*, [arXiv:2609.01105v2](https://arxiv.org/abs/2609.01105v2). It concerns a prescribed divergence-free transport flow, a different model from Euler's self-consistent velocity.

## Status review


**Known cases:** The August 2026 classification proves invariance generally and the quasi-invariance equivalence only for finitely many active directions. A prescribed transport-flow obstruction is not Euler's self-consistent Gaussian flow. The infinitely-many-directions quasi-invariance target remains beyond these theorems.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The later Liu paper states a complete invariant-measure classification and proves quasi-invariance equivalent to invariance when the active modes occupy a finite union of lines. Consequently the unresolved part concerns sequences with infinitely many active directions. Neither theorem states the full quasi-invariance equivalence for arbitrary $`S(a)`$. The de Suzzoni–Latocca transport result does not cover Euler's nonlinear random-data flow. Bounded searches on 21 October 2026 found no later matching complete announcement; that absence is not an exhaustive proof. The [independent source audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal0258-aihpc175-conjecture110-independent-owner-audit.json) and [coordinator scope and duplicate check](../FURTHER_problems/_tracking/aihpc175-gaussian-quasi-invariance-coordinator-check-2026-10-21.json) record the inspected evidence.


### Online recheck, 2026-10-30

The August 2026 classification proves invariance generally and the quasi-invariance equivalence only for finitely many active directions. A prescribed transport-flow obstruction is not Euler's self-consistent Gaussian flow. The infinitely-many-directions quasi-invariance target remains beyond these theorems.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2608.01019); [status source 2](https://arxiv.org/abs/2609.01105); [status source 3](https://doi.org/10.4171/AIHPC/175). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-3f1ac500a16ac818** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
