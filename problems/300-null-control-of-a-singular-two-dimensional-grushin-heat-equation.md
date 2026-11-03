# 300. Null control of a singular two-dimensional Grushin heat equation

**Area:** Inverse problems, control and parabolic PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On $`\Omega=(-1,1)\times(0,1)`$, consider the controlled equation
```math
\partial_t f-\partial_x^2f-|x|^{2\gamma}\partial_y^2f
 +\frac{\nu^2-\tfrac14}{x^2}f=\mathbf1_\omega u,
 \qquad \gamma>0,\quad 0<\nu<1,
```

with zero Dirichlet data on the outer boundary. At $`x=0`$, use the **transmitting self-adjoint realization** constructed by Morancey [1, Section 2], and understand solutions through its semigroup [1, Proposition 2.10]. This choice matters: imposing separate Dirichlet conditions on the two sides would prevent a control on one side from acting on the other.

For which parameters $`\gamma,\nu`$, control regions $`\omega\subset\Omega`$, and times $`T>0`$ can every $`f_0\in L^2(\Omega)`$ be driven to $`f(T)=0`$ by an $`L^2`$ control supported in $`(0,T)\times\omega`$? A concrete case is a one-sided vertical strip $`\omega=(a,b)\times(0,1)`$, $`0<a<b<1`$, with $`\nu\ne\tfrac12`$ (a nonzero inverse-square potential). Determine whether null control holds in sufficiently large time and, if it does, its time threshold.

Morancey explicitly posed null controllability for $`0<\nu<1`$ in the conclusion of [1]. The exact coefficient is $`c_\nu=\nu^2-1/4`$ [1, (2.2)].

## Application

The model combines diffusion that degenerates along $`x=0`$ with a singular potential there. Deciding whether a control away from that line can extinguish heat on both sides tests how the transmission condition and the geometry of the control region affect observability.

## Known results and scope

Morancey proves **approximate** controllability for every nonempty open $`\omega`$, $`\gamma>0`$ and $`0<\nu<1`$ for the specified realization [1, Theorem 1.2]. Approximate reachability does not imply exact null control. The no-potential Grushin problem and a model with the singularity at the boundary have different established regimes [1, Introduction].

Lissy and Lourme prove null control for the **one-dimensional** heat equation with an interior inverse-square potential [2]. Their concluding discussion separately identifies the two-dimensional singular Grushin equation, including a one-sided vertical strip, as a remaining question. Even when $`\nu=\tfrac12`$ makes the potential coefficient zero, the transmitting realization specified in [1] must be checked against the domain used in no-potential results before transferring a theorem. Vanlaere's later observability work [3] treats a boundary singularity in two dimensions or an interior singularity in higher dimensions; it does not settle this two-dimensional interior case.

## References

1. M. Morancey, [*Approximate controllability for a 2D Grushin equation with potential having an internal singularity*](https://aif.centre-mersenne.org/item/10.5802/aif.2966.pdf), *Annales de l'Institut Fourier* **65** (2015), no. 4, 1525–1556; equations (1.1), (2.2), Theorem 1.2, Proposition 2.10, and open question on p. 1555. [DOI](https://doi.org/10.5802/aif.2966).
2. P. Lissy and T. Lourme, [*Null controllability of the 1D heat equation with interior inverse square potential*](https://arxiv.org/pdf/2505.07302), *Journal of Differential Equations* (2026), [DOI](https://doi.org/10.1016/j.jde.2026.114221); concluding discussion under “Grushin equation with a singularity.”
3. R. Vanlaere, [*Observability properties of the singular Grushin equation*](https://arxiv.org/pdf/2602.08044), 2026 preprint; two-dimensional boundary and higher-dimensional interior singularities.

## Status review


**Known cases:** The current Lissy–Lourme result is one-dimensional. Vanlaere's singular-Grushin work concerns boundary singularities in 2D or interior singularities in higher dimension; no full answer for Morancey's transmitting 2D interior model found.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The [primary-source, later-result and duplicate audit](../FURTHER_problems/_tracking/singular-grushin-null-control-status-2026-10-21.json) separates the full transmitting two-dimensional problem from its one-dimensional analogue and other singularity geometries. No complete resolution or announcement for this precise problem was located in the bounded search through 21 October 2026.


### Online recheck, 2026-10-30

The current Lissy–Lourme result is one-dimensional. Vanlaere's singular-Grushin work concerns boundary singularities in 2D or interior singularities in higher dimension; no full answer for Morancey's transmitting 2D interior model found.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2505.07302); [status source 2](https://arxiv.org/abs/2602.08044); [status source 3](https://aif.centre-mersenne.org/item/AIF_2015__65_4_1525_0/). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-be3c0fd43ac6e182** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
