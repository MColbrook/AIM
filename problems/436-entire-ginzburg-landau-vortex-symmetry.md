# 436. Radial classification of higher-degree entire planar Ginzburg–Landau vortices

**Area:** Elliptic PDEs and superfluid vortices

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03
## Problem statement

Let $`u\in C^\infty(\mathbb R^2;\mathbb C)`$ satisfy

```math
-\Delta u=u(1-|u|^2),\qquad \lim_{|x|\to\infty}|u(x)|=1,
```

and let its degree on sufficiently large circles be an integer $`q\ge2`$. Must there exist $`x_0\in\mathbb R^2`$ and $`\alpha\in\mathbb C`$, $`|\alpha|=1`$, such that

```math
u(x_0+re^{i\theta})=\alpha e^{iq\theta}g_q(r)?
```

Here $`g_q`$ is the positive radial vortex profile solving $`g_q''+r^{-1}g_q'-q^2r^{-2}g_q+g_q(1-g_q^2)=0`$, $`g_q(0)=0`$, $`g_q(r)\to1`$. A single nonradial entire solution in this class would disprove the assertion.

## Application

The degree is the quantized circulation of a vortex. Classifying stationary states tests whether an isolated multiple-quantum vortex can support a noncircular equilibrium structure.

## References

1. H. Brezis, [Some of my favorite open problems](https://doi.org/10.4171/RLM/1008), *Rendiconti Lincei—Matematica e Applicazioni* (2023), equations (2.5)–(2.6), Open Problem 2.4.
2. P. Esposito, [Some remarks concerning symmetry-breaking for the Ginzburg–Landau equation](https://doi.org/10.1016/j.jfa.2013.07.029), *Journal of Functional Analysis* **265** (2013), 2189–2203, introduction and correlation-coefficient theorem.

3. H.-G. Chen, Y. Liu, J. Wei and W. Yang, [*On Brezis’ open problem 2.4*](https://arxiv.org/abs/2610.34979), arXiv:2610.34979v1 (26 October 2026), equation (1.1), Theorem 1.1 and Lemma 2.1. [Primary manuscript](https://arxiv.org/pdf/2610.34979v1).

## Status review

**Resolution update (3 November 2026):** Counterexample. Chen–Liu–Wei–Yang’s Theorem 1.1 asserts the existence of a smooth entire solution of the displayed isotropic equation, with modulus tending to one, outside every translate and constant-phase rotation of the radial vortex. Its degree is at least one of 8 and 9; the argument does not identify which. One such degree suffices to refute the universal classification asked here. Lemma 2.1 explicitly supplies a smooth Euclidean-plane solution, including at the origin, from the auxiliary cone construction.

[Proof](https://arxiv.org/pdf/2610.34979v1) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-b/436.json). The theorem hypotheses and current announcement were checked.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

The source explicitly discusses why an earlier proposed symmetry-breaking construction does not settle this question. Searches through the review date for entire isotropic Ginzburg–Landau vortices, degree-two symmetry and Brezis Problem 2.4 found no later resolution. The September 2026 preprint [arXiv:2609.19020](https://arxiv.org/abs/2609.19020) claims finite potential energy from the asymptotic modulus condition (Problem 2.5), not the radial classification in Problem 2.4. Disk minimizer results, anisotropic systems, and magnetic vortices also have different hypotheses.
