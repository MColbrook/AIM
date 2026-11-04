# 911. The sharp constant in the critical Dirac norm inequality

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-04

## Problem statement

For an integer $`d\geq3`$, put $`N=2^{\lfloor d/2\rfloor}`$, $`p_d=2d/(d+1)`$ and $`q_d=2d/(d-1)`$. Fix Hermitian matrices $`\gamma_1,\ldots,\gamma_d\in\mathbb C^{N\times N}`$ satisfying

```math
\gamma_j\gamma_k+\gamma_k\gamma_j=2\delta_{jk}I_N,
\qquad D_d=-i\sum_{j=1}^{d}\gamma_j\partial_j.
```

Derivatives are distributional, and all norms below use Lebesgue measure on $`\mathbb R^d`$ and the Euclidean norm on $`\mathbb C^N`$. Define

```math
\mathcal X_d=\{\psi\in L^{q_d}(\mathbb R^d;\mathbb C^N):
D_d\psi\in L^{p_d}(\mathbb R^d;\mathbb C^N)\},
\qquad
C_d=\inf_{0\ne\psi\in\mathcal X_d}
\frac{\|D_d\psi\|_{p_d}}{\|\psi\|_{q_d}}.
```

Determine the exact value of $`C_d`$ for each $`d\geq3`$. Equivalently, find the largest constant for which $`\|D_d\psi\|_{p_d}\geq C_d\|\psi\|_{q_d}`$ holds for every $`\psi\in\mathcal X_d`$.

This is the constant question in Frank–Loss [1, equation (8) in the January 2022 preprint; equation (9) in the published article]. Their power-normalized constant is $`S_d^s=C_d^{p_d}`$.

## Application

This inequality measures how the free Dirac operator controls the size of a spinor at the critical exponents. Sharp constants help distinguish the effects of spinorial structure from scalar Sobolev estimates in relativistic PDE and magnetic zero-mode problems.

## References

1. R. L. Frank and M. Loss, [A sharp criterion for zero modes of the Dirac equation](https://arxiv.org/abs/2201.03610), January 2022 preprint, pp. 6–7, “Relation to Sobolev inequalities”; published in *Journal of the European Mathematical Society* **28** (2026), 305–331, [doi:10.4171/JEMS/1475](https://doi.org/10.4171/JEMS/1475), p. 311.
2. G. Wang and M. Zhang, [Stability of spinorial Sobolev inequalities on $`\mathbb S^n`$](https://arxiv.org/abs/2508.09047), latest arXiv version v2, Introduction (norm quotient (1.10) in the PDF, (1.15) in the HTML), Theorem 1.5 and the following paragraph; published in *Advances in Mathematics* **505** (2026), 111318, [doi:10.1016/j.aim.2026.111318](https://doi.org/10.1016/j.aim.2026.111318).
3. B. Bieganowski and J. Mederski, [Explicit counterexamples to Frank–Loss optimizer conjectures for critical Dirac and vector Sobolev inequalities](https://arxiv.org/abs/2610.15787), October 2026 preprint, Theorem 1.1, Section 4 and Section 7.

- M. J. Colbrook, [*Sharp radial Dirac bounds and stability of the scalar spinor*](../research/solutions/911-dirac-radial-bounds-stability/aim911.pdf), 3 November 2026. [TeX source](../research/solutions/911-dirac-radial-bounds-stability/aim911.tex), [package and reproduction](../research/solutions/911-dirac-radial-bounds-stability/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-operators-batch/911-review.md).

## Status review

**Known cases:** The specified two-channel radial class has exact constant $`K_d=dI_d^{1/d}`$, with $`I_d=|\mathbb S^{d-1}|q_d^{-1}B((d-1)/2,(d+1)/2)`$. The scalar Talenti spinor is stationary with nonnegative second variation in every smooth compactly supported tangent direction, including angular modes. The previously recorded smaller explicit quotients remain valid.

**Remaining target:** Determine the global constant $`C_d`$ over all of $`\mathcal X_d`$ for every $`d\ge3`$. The radial theorem and local second-variation result do not prove a global inequality for arbitrary spinors.

**Reviewed result, 2026-11-04:** The [manuscript](../research/solutions/911-dirac-radial-bounds-stability/aim911.pdf) and [individual audit](../research/solution_reviews/2026-11-03-operators-batch/911-review.md) establish the stated radial theorem and second-variation result. Review was performed by Codex (AI), including a second independent proof check.

### Earlier literature review, 2026-10-30

The October 2026 counterexamples disprove the proposed optimizers and give smaller explicit quotients, not the exact critical Dirac norm constant. Spinorial Yamabe quotients and magnetic zero-mode thresholds are different variational quantities. The current exact-constant target remains.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2610.15787). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The inequality holds with a positive constant, but the exact optimum remains undetermined in the sources checked. The old proposal that the conformal Killing-spinor family supplies the optimum is false: Wang–Zhang [2] establish instability, and Bieganowski–Mederski [3] provide explicit lower-quotient competitors in every dimension. In particular, [3] gives $`C_3\leq(18\pi)^{1/3}`$, strictly below the old proposed value $`\tfrac32|\mathbb S^3|^{1/3}`$; it explicitly does not determine the exact optimal constants.

The remaining question concerns the norm quotient displayed above. The spinorial Yamabe quotient, which uses $`\int\langle D\psi,\psi\rangle`$ in the denominator, and the sharp magnetic-field threshold for coupled Dirac zero modes are different problems. The recent results on those quantities do not determine $`C_d`$; [3, Section 7] expressly distinguishes them.

Current searches included the exact problem and source titles, sharp/optimal spinorial Sobolev constants, counterexamples, 2025–2026 updates and Prove2Me. The October 2026 comparison was checked in its primary body. No complete or announced determination of the displayed constants was located. This is a bounded literature review, not a proof of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-82fe5d75531fa088**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
