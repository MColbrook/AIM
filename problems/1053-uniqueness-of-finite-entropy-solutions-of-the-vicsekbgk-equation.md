# 1053. Uniqueness of finite-entropy solutions of the Vicsek–BGK equation

**Area:** Kinetic equations and collective motion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X=(\mathbb R/\mathbb Z)^2`$, let $`\Theta=\mathbb R/(2\pi\mathbb Z)`$ with probability measure $`dm(\theta)=d\theta/(2\pi)`$, and write $`e(\theta)=(\cos\theta,\sin\theta)`$. For a nonnegative density $`f(t,x,\theta)`$, define

```math
\rho_f(t,x)=\int_\Theta f(t,x,\theta)\,dm(\theta),\qquad
J_f(t,x)=\int_\Theta e(\theta)f(t,x,\theta)\,dm(\theta),
```

and, for every $`J\in\mathbb R^2`$, set

```math
Z(J)=\int_\Theta \exp(e(\eta)\cdot J)\,dm(\eta),\qquad
M_J(\theta)=\frac{\exp(e(\theta)\cdot J)}{Z(J)}.
```

Consider the local Vicsek–BGK equation with transport speed and relaxation rate equal to one:

```math
\partial_t f+e(\theta)\cdot\nabla_x f=\rho_f M_{J_f}-f.
```

For every nonnegative $`f_0\in L^1(X\times\Theta)`$ satisfying

```math
\int_{X\times\Theta}f_0|\log f_0|\,dx\,dm<\infty,
```

and every finite $`T>0`$, are any two solutions in the following class with initial datum $`f_0`$ equal?

Require $`f\ge0`$, $`f\in C([0,T];L^1(X\times\Theta))`$, preservation of the initial mass, and

```math
\mathrm*{ess\,sup}_{0<t<T}
\int_{X\times\Theta}f(t)|\log f(t)|\,dx\,dm<\infty,
```

where $`0|\log0|=0`$. The equation is required in the precise mild sense

```math
f(t,x,\theta)=e^{-t}f_0(x-te(\theta),\theta)
+\int_0^t e^{-(t-s)}
\rho_f(s,x-(t-s)e(\theta))
M_{J_f(s,x-(t-s)e(\theta))}(\theta)\,ds,
```

as an identity in $`L^1(X\times\Theta)`$ for every $`t\in[0,T]`$. Spatial translations are taken modulo $`\mathbb Z^2`$. The integral is an $`L^1`$ integral. The translated collision gain has norm equal to the conserved mass $`m_0`$, and the displayed integrand has norm $`e^{-(t-s)}m_0`$, because $`\int M_J\,dm=1`$.

No bound on $`\rho_f`$ in $`L^\infty_x`$, smallness condition, lower density bound, nonzero-moment assumption, or closeness to equilibrium is imposed. The finite-entropy requirement is a boundedness condition on finite time intervals; no monotonicity of the entropy is assumed. The alignment distribution uses the full local moment $`J_f`$, not $`J_f/|J_f|`$, and is defined also at $`J_f=0`$.

## Application

This kinetic model describes agents moving at fixed speed and changing direction at random times, with the new direction sampled from a von Mises distribution determined by the local population flux. Uniqueness would make this evolution unambiguous for the finite-entropy populations for which global solutions are known, including spatially unbounded densities.

## References

1. S. Merino-Aceituno, C. Schmeiser and R. Winter, *Stability of equilibria of the spatially inhomogeneous Vicsek-BGK equation across a bifurcation*, SIAM Journal on Mathematical Analysis **57**(6) (2025), 6017–6038. [DOI](https://doi.org/10.1137/24M1715908); [published PDF](https://orca.cardiff.ac.uk/id/eprint/182475/1/24m1715908.pdf); [author manuscript](https://arxiv.org/abs/2404.00347v3). Model (1.1)–(1.2), Theorem 2.6, Remark 2.7 on p.6023, and the mild identity at the end of §5 on p.6035.

The statement fixes dimension two and transport parameter one within the source question. Replacing its circle area measure by $`dm`$ is the exact change of density $`f=2\pi F`$; the moments, mass and equation are preserved when the von Mises density is changed consistently.

## Status review


**Known cases:** The class includes arbitrary finite-entropy mild solutions without a bounded spatial density. The published remark retains uniqueness as open; equilibrium stability and conditional bounded-density arguments do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The class includes arbitrary finite-entropy mild solutions without a bounded spatial density. The published remark retains uniqueness as open; equilibrium stability and conditional bounded-density arguments do not cover it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published Remark 2.7 explicitly leaves uniqueness for the finite-entropy solutions of Theorem 2.6 unresolved. Theorem 2.6 supplies global existence in this class, while the strong stability results require regularity and proximity to an equilibrium. A spatial density bound would permit a stronger uniqueness argument and is deliberately absent here.

Searches through 17 October 2026 located no complete solution or announced counterexample for this exact class. The 2026 Evans–Morris–Yoldaş theorem for a different BGK model uses a fixed Maxwellian and two-sided Maxwellian bounds; it does not establish uniqueness for this local flux-dependent sampling law with merely finite entropy. Results for the angularly diffusive Vicsek–Fokker–Planck equation, spatial convolution, or BGK laws normalized by $`J/|J|`$ concern different operators.

AIM227 concerns entropy-admissible renormalized hard-sphere Boltzmann solutions with Euclidean velocities and a binary collision integral. Its announced resolution does not settle this compact-velocity nonlinear relaxation equation. The admitted local Vicsek continuation problem concerns angular diffusion and smooth data, while the active Brownian uniqueness problem includes degenerate spatial cross-diffusion. Neither is the present target.

An independent selected-primary audit confirmed the exact published question, circle-measure conversion, entropy class, initial trace and damped mild formula. The fresh 186-page catalogue scan returned three matching name contexts: one reinforcement-learning reference and two textbook Boltzmann–BGK Maxwellian contexts. None concerns this local angular von Mises uniqueness question. These are listing-description comparisons, rather than certifications of mission proofs.

The [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-vicsek-bgk-entropy-review.json) and [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/vicsek-bgk-prove2me0096-comparison.json) record their exact extents, current searches and limits. The coordinator also read the actual final 2025 model, complete Theorem 2.6/Remark 2.7 and the published mild-solution conclusion. Thus the retained question is checked in the published edition, without assuming preprint parity. The complete 21-page author text was read for discovery; only the recorded selected portions of the final 22-page article were inspected. The audit preserves a caveat about a displayed moment estimate in the existence proof; these checks do not independently certify that entire proof. No matching complete uniqueness result or announcement was found in the dated bounded checks. [Detailed review packet](../FURTHER_problems/_tracking/parallel/continuum/vicsek-bgk-entropy-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a34c40fa63efd9ef**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
