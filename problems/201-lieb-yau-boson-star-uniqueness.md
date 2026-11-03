# 201. Uniqueness of a boson star at every subcritical mass

**Area:** Relativistic quantum matter; self-gravitating waves

**Status:** 🟡 PARTIAL

**Last checked:** 2026-11-03

## Problem statement

For $`u\in H^{1/2}(\mathbb R^3)`$ define

```math
D(u)=\iint\frac{|u(x)|^2|u(y)|^2}{|x-y|}\,dx\,dy,\qquad K(u)=\langle u,\sqrt{-\Delta}\,u\rangle,
```



```math
N_* =\inf_{u\ne0}\frac{2K(u)\|u\|_2^2}{D(u)},\qquad \mathcal E(u)=\langle u,(\sqrt{-\Delta+1}-1)u\rangle-\tfrac12D(u).
```

The square roots are Fourier multipliers. For every $`0<N<N_*`$, the infimum of $`\mathcal E`$ over $`\|u\|_2^2=N`$ is attained.

Is this minimizer unique modulo translation and constant phase for every such $`N`$? Precisely, must any two minimizers satisfy $`v(x)=e^{i\theta}u(x-x_0)`$ for some $`\theta\in\mathbb R`$, $`x_0\in\mathbb R^3`$?

## Application

The model balances relativistic kinetic energy and Newtonian attraction. Uniqueness would determine whether a fixed subcritical stellar mass selects a single equilibrium density profile.

## References

1. Yujin Guo and Xiaoyu Zeng, [The Lieb–Yau Conjecture for Ground States of Pseudo-Relativistic Boson Stars](https://arxiv.org/abs/1904.06957), *J. Funct. Anal.* 278 (2020), 108510. Section 1 states the full conjecture and proves its small-mass case.
2. Pan Chen and Xiaoyu Zeng, [A new proof of uniqueness of ground state for pseudo-relativistic Hartree equation](https://arxiv.org/abs/2608.08493), preprint, 9 August 2026. Section 1, equations (1.1)–(1.3) and the paragraph before (1.4), explicitly retain the full conjecture; Theorem 1.1 concerns the nonrelativistic regime.

## Status review

**Known cases:** Uniqueness modulo translation and phase is established for sufficiently small positive mass. The September 2026 preprint cited below also announces uniqueness sufficiently close to the critical mass from below.

**Remaining target:** Uniqueness for every mass in the full subcritical interval.

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 paper gives another proof in the sufficiently-small-mass regime. A later preprint by Pan Chen, Qi Guo, Juncheng Wei and Yuanyang Yu, [*Uniqueness and Nondegeneracy of Ground State for the L²-Critical Boson Star Equation*](https://arxiv.org/html/2609.23771v1) (20 September 2026), announces uniqueness for N sufficiently close to N_* from below in Corollary 1.3. The text immediately following that corollary explicitly leaves the intermediate-mass regime open. This additional partial announcement has not been independently proof-verified here. Fixing the rest mass at one is a choice of units.

**Search audit:** Queries: “Lieb Yau boson star uniqueness 2025 2026”, “pseudo relativistic Hartree uniqueness full mass conjecture”; checked the August 2026 theorem against the full interval. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
