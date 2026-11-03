# 567. Perfect Lee codes beyond dimension two

**Area:** Coding theory and discrete geometry

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

For integers $`n\geq3`$ and $`r\geq2`$, define the discrete Lee ball

```math
B_1(n,r)=\left\{z\in\mathbb Z^n:\sum_{j=1}^n|z_j|\leq r\right\}.
```

Prove or disprove that there is no set $`C\subseteq\mathbb Z^n`$ for which

```math
\mathbb Z^n=\bigsqcup_{c\in C}\bigl(c+B_1(n,r)\bigr).
```

Equivalently, no code in the integer lattice should correct every Lee-metric error of radius $`r`$ perfectly: every lattice point would have to lie within distance $`r`$ of exactly one codeword. This is the strong Golomb–Welch conjecture, stated as Conjecture 3 in [1, Section II]. The centers are arbitrary; no linearity, lattice, or periodicity assumption is imposed.

## Application

Lee distance measures the total magnitude of coordinate errors. Perfect Lee codes would meet the corresponding packing bound exactly, making their existence relevant to the limits of error correction for integer-valued signals and related finite-alphabet storage models.

## References

1. P. Horak and D. Kim, [50 Years of the Golomb–Welch Conjecture](https://doi.org/10.1109/TIT.2017.2786675), *IEEE Transactions on Information Theory* **64**(4) (2018), 3048–3061. Section II, Conjecture 3, and Sections III–IV; [author manuscript](https://arxiv.org/html/1706.03589v3).
2. K. H. Leung and Y. Zhou, [No lattice tiling of $`\mathbb Z^n`$ by Lee sphere of radius 2](https://doi.org/10.1016/j.jcta.2019.105157), *Journal of Combinatorial Theory, Series A* **171** (2020), 105157. [Preprint](https://arxiv.org/abs/1808.08520).

3. B. Chen, J. Huang and G. Luo, [*The Golomb–Welch conjecture for arbitrary centre sets*](https://arxiv.org/pdf/2610.34291v1), arXiv:2610.34291v1 (25 October 2026), equation (1) and Theorem 1.1; proof completion in §5.6.

## Status review

**Affirmative proof.** Chen, Huang and Luo, Theorem 1.1 of [arXiv:2610.34291v1](https://arxiv.org/pdf/2610.34291v1), prove nonexistence of the displayed translational tiling for every integer $`n\ge3`$ and $`r\ge2`$. Their centre set is arbitrary: no lattice, linearity, periodicity or density assumption is imposed. This matches the full strong conjecture stated here. The companion lattice-only result is not the basis for this status.

The current version and theorem scope were checked on 3 November 2026. [Scope check](../research/solution-status-audit-2026-11-03/lane-b/567.json). Earlier low-dimensional, large-radius and lattice cases remain historical partial progress.
