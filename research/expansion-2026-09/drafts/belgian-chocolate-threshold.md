# The sharp Belgian chocolate stabilization threshold

**Area:** Feedback control and polynomial stability

**Status:** Accepted; published as entry 311

**Last checked:** 2026-09-17

## Problem statement

Let $`\mathcal H`$ be the set of nonzero real polynomials whose roots all have strictly negative real part; nonzero constant polynomials belong to $`\mathcal H`$. Define

```math
\mathcal D=\left\{\delta\in(0,1):\quad
\begin{array}{l}
\text{there exist }x,y\in\mathcal H\text{ with }\deg y\le\deg x,\\[2pt]
(s^2-2\delta s+1)x(s)+(s^2-1)y(s)\in\mathcal H
\end{array}\right\}.
```

Determine the exact value of

```math
\delta_* = \sup\mathcal D.
```

The polynomial degrees are arbitrary finite integers, and coefficients are arbitrary real numbers. Stability is strict. The question asks for the sharp threshold over all degrees, with matching feasibility and impossibility arguments, rather than an optimum within a prescribed controller family. It is a supremum: the endpoint need not be attained by a pair of strictly stable polynomials.

## Applied significance

For the plant $`G_\delta(s)=(s^2-1)/(s^2-2\delta s+1)`$, the quotient $`y/x`$ represents a proper, stable, minimum-phase linear time-invariant controller. The displayed combination is its closed-loop characteristic polynomial under negative feedback. The problem tests stabilization limits when an unstable pole approaches an unstable zero, a difficulty that also arises in engineering control design.

## References

1. Zachary Charles and Nigel Boston, *Exploiting Algebraic Structure in Global Optimization and the Belgian Chocolate Problem*, [arXiv:1708.08114v1](https://arxiv.org/pdf/1708.08114v1), August 27, 2017 author manuscript; journal version J. Global Optimization 72 (2018), 241–254. See §1 Eq. (1.1), §3.2 Theorems 3.4–3.6, §5 Theorem 5.1 and §8.
2. Walter Bergweiler and Alexandre Eremenko, *Goldberg’s constants*, J. d’Analyse Mathématique 119 (2013), 365–402, [author manuscript](https://www.math.purdue.edu/~eremenko/dvi/goldbergconst.pdf), §11, especially Theorem 11.1.
3. Alexandre Eremenko, *Goldberg’s constant and its relatives*, [author’s problem note](https://www.math.purdue.edu/~eremenko/dvi/goldconst.pdf), April 4, 2015, Problem 3.
4. Patrizio Colaneri and Didier Henrion, *Switching and periodic control of the Belgian chocolate system*, IFAC ROCOND 2006, [author manuscript](https://homepages.laas.fr/henrion/papers/chocoswitch.pdf), §§3–5.

## Status review

Charles–Boston report feasibility for every $`0<\delta\le0.9808348`$. Their finite-degree constructions and perturbations of polynomials with imaginary-axis roots do not identify the unrestricted threshold. Bergweiler–Eremenko prove $`\delta_*<0.999579`$, leaving a gap. Eremenko’s separate problem note asks for the corresponding extremal constant in the unit disk.

The solved $`\delta=0.9`$ prize instance is weaker than determining $`\delta_*`$. The switching and periodic-controller paper changes the time-invariance assumption and explicitly leaves the original problem unresolved. Likewise, exact results for other Goldberg constants impose different zero and one-point conditions.

September 17, 2026 searches covering recent and unrestricted resolution claims found no matching sharp-threshold result. The [evidence ledger](../candidates/belgian-chocolate-threshold.json) records the source scopes, duplicate comparison and access limits. The polynomial, rational-control and equivalent holomorphic formulations are one problem family.

A clearly separated adversarial self-pass passed on September 17. Integrated as [entry 309](../../../cut_problems/problems/308-belgian-chocolate-threshold.md) after the September 17, 2026 batch refresh.
