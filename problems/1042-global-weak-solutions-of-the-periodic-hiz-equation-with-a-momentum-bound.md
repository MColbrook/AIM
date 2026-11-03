# 1042. Global weak solutions of the periodic HIZ equation with a momentum bound

**Area:** Nonlinear surface waves
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$ and define the Hilbert transform by $`\widehat{Hf}(k)=-i\mathrm{sgn}(k)\widehat f(k)`$, with $`\mathrm{sgn}(0)=0`$. For smooth real functions the HIZ equation is

```math
\partial_t\phi+H[(H\phi)(H\phi)_x]_x+(H\phi)\phi_{xx}=0.
```

For every real $`\phi_0\in C^\infty(\mathbb T)`$ of mean zero, does there exist
```math
\phi\in C_{\mathrm w}([0,\infty);H^{1/2}_0(\mathbb T;\mathbb R)),\qquad \phi(0)=\phi_0,
```
with momentum bounded by its initial value
```math
P(\phi(t))\le P(\phi_0)\quad(t\ge0),\qquad
P(f)=\sum_{k\ne0}|k|\,|\widehat f(k)|^2,
```
that solves the following weak form? Here $`H^{1/2}_0`$ denotes the mean-zero Sobolev space and $`C_{\mathrm w}`$ means continuity in its weak topology.

Use $`\widehat f(k)=(2\pi)^{-1}\int_0^{2\pi}f(x)e^{-ikx}\,dx`$, and set
```math
T(k,m,n)=\frac{2|kmn|}{|k|+|m|+|n|},\qquad T(0,0,0)=0.
```
For every $`k\in\mathbb Z`$ and $`t\ge0`$, require
```math
\widehat\phi(k,t)=\widehat\phi_0(k)
+i\mathrm{sgn}(k)\int_0^t\sum_{n\in\mathbb Z}
T(-k,k-n,n)\widehat\phi(k-n,\tau)\widehat\phi(n,\tau)\,d\tau.
```
The sum is absolutely convergent for $`H^{1/2}`$ functions: $`T(-k,m,n)\le |k|\sqrt{|mn|}`$ when $`m+n=k`$. This specifies the quadratic distribution at the stated regularity, without treating undefined pointwise products as a definition.

This is a precise necessary part of the source's conjecture on global admissible weak solutions. It asks for the initial momentum bound. It does not require all-times momentum monotonicity, convergence of a prescribed viscous approximation, or identification of a physically selected continuation.


## Application

The equation models the weakly nonlinear profile of nondispersive surface waves, including waves on a tangential discontinuity in magnetohydrodynamics. Such profiles may develop cusps. Global weak existence would provide a mathematical continuation after smooth evolution breaks down.


## References

1. John K. Hunter, [*Nonlinear Hyperbolic Surface Waves*](https://www.math.ucdavis.edu/~hunter/papers/surf_corrected.pdf), in *Nonlinear Conservation Laws and Applications*, IMA Volumes **153** (2011), 303–314, [chapter DOI](https://doi.org/10.1007/978-1-4419-9554-4_16). Inspected: the corrected author version, equations (1.1), (5.1)–(5.6), Theorem 5.1 and the global weak-existence question on physical p. 11.
2. Giuseppe Alì and John K. Hunter, [*Nonlinear surface waves on a tangential discontinuity in magnetohydrodynamics*](https://doi.org/10.1090/qam/1999831), Quarterly of Applied Mathematics **61** (2003), 451–474; [author version](https://www.math.ucdavis.edu/~hunter/papers/mhd.pdf), selected numerical and admissibility discussion.
3. Paolo Secchi, [*Data dependence for the amplitude equation of surface waves*](https://doi.org/10.1007/s00033-016-0628-0), Zeitschrift für angewandte Mathematik und Physik **67** (2016), article **33**, equations (1)–(4) and Theorems 1–2.
4. Olivier Pierre and Jean-François Coulombel, [*Weakly nonlinear surface waves in magnetohydrodynamics*](https://arxiv.org/abs/1807.00536v1) (2018), Theorems 1.2 and 4.1, equations (4.30)–(4.34) and the following global-existence discussion, physical pp. 16 and 56–58 of the inspected 153-page version. The later published parts are separate edition/parity obligations.

## Status review


**Known cases:** The exact periodic HIZ Fourier weak formulation and initial momentum bound are required. Hunter-Saxton continuation results and different surface-wave amplitude estimates do not address this quadratic nonlocal equation.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact periodic HIZ Fourier weak formulation and initial momentum bound are required. Hunter-Saxton continuation results and different surface-wave amplitude estimates do not address this quadratic nonlocal equation.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source conjectures global admissible weak existence. This entry isolates a precise weaker requirement: distributional existence with the initial momentum bound. It does not identify a viscous or physically selected continuation.

The chapter's printed Fourier equation (5.2) has the opposite sign from its spatial equation (1.1) under the stated Hilbert-transform convention. The weak form above follows the spatial equation and agrees with Secchi's signed kernel. A check is $`\phi_0=\cos x`$, which gives $`\partial_t\phi|_{t=0}=-(1/2)\sin 2x`$.

Secchi's theorem gives local smooth well-posedness. Pierre–Coulombel construct finite-time smooth amplitude profiles and explicitly retain global weak or strong existence as open after Theorem 4.1. Their construction of arbitrarily accurate approximate magnetohydrodynamic solutions does not give the requested global weak continuation.

A uniform momentum bound alone does not justify passing to the quadratic term in a Galerkin limit: that term is not weakly continuous on bounded subsets of $`H^{1/2}`$. No matching complete resolution or announced solution was located in the recorded bounded checks.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/hiz-global-weak-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-hiz-global-weak-review.json), [current comparisons](../FURTHER_problems/_tracking/hiz-weak-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/hiz-weak-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/hiz-weak-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/hiz-weak-coordinator-review-2026-10-19.json) record the checks and their limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-071132570685178a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
