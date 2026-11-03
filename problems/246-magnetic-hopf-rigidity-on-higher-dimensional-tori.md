# 246. Magnetic Hopf rigidity on higher-dimensional tori

**Area:** Geometric mechanics; magnetic dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, let $`g`$ be any smooth Riemannian metric on
$`\mathbb T^n=\mathbb R^n/\mathbb Z^n`$, and let $`\beta`$ be any smooth
closed real two-form on $`\mathbb T^n`$. On its cotangent bundle, write
$`\pi:T^*\mathbb T^n\to\mathbb T^n`$ for the projection and consider

```math
\omega_\beta=\omega_{\rm can}+\pi^*\beta,
\qquad H(q,p)=\tfrac12 g_q^{-1}(p,p).
```


Let $`\Phi_t`$ be the Hamiltonian flow of $`H`$ for $`\omega_\beta`$,
and let $`V_z=\ker d\pi_z\subset T_z(T^*\mathbb T^n)`$ be the full
$`n`$-dimensional vertical subspace. Suppose that

```math
d\Phi_t(z)V_z\cap V_{\Phi_t(z)}=\{0\}
\quad\text{for every }z\in H^{-1}(1/2)
\text{ and every }t\ne0.
```


Must $`\beta\equiv0`$ and $`g`$ be flat?

This is Bialy's conjugate-point convention: the derivative acts on the
full ambient cotangent tangent spaces. The vertical subspace is not
restricted to the energy hypersurface, and no quotient by the flow
direction is taken. The magnetic form need not be exact, and the metric
need not be conformally flat or close to a flat metric.

## Application

The magnetic Hamiltonian describes a charged particle with kinetic energy
moving on a periodic Riemannian configuration space. The question asks
whether the absence of all focusing in this precise variational sense
forces both a zero magnetic field and flat geometry.

## References

1. M. L. Bialy, *Rigidity for periodic magnetic fields*, Ergodic Theory and
   Dynamical Systems **20** (2000), 1619–1626.
   [DOI](https://doi.org/10.1017/S0143385700000894),
   [Preprint](https://arxiv.org/abs/math/9902013), v1, 2 February 1999:
   abstract and introduction, the definition before Theorem 1 on p. 2,
   Remark 1, and §4, p. 8.
2. V. Assenza, J. Marshall Reber and I. Terek, *Magnetic Flatness and
   E. Hopf's Theorem for Magnetic Systems*, Communications in Mathematical
   Physics **406** (2025), 24.
   [DOI](https://doi.org/10.1007/s00220-024-05166-5),
   [published paper](https://d-nb.info/1364794047/34), introduction, p. 4.
3. D. Burago and S. Ivanov, *Riemannian tori without conjugate points are
   flat*, Geometric and Functional Analysis **4** (1994), 259–269.
   [DOI](https://doi.org/10.1007/BF01896241).
4. G. B. Guglielmo and A. J. García, *A Metric Entropy Formula for Magnetic
   Flows without Conjugate Points*, [arXiv:2606.18434v2](https://arxiv.org/abs/2606.18434v2),
   Theorem B and Definition 4.2 (the additional no-focal-point condition).

## Status review


**Known cases:** The magnetic torus target uses Bialy's full ambient vertical no-conjugate-points convention in dimension >=3. The 2025 magnetic-curvature theorem retains an integral equality/curvature condition, and later entropy theorems add no-focal-point hypotheses. Conformally flat and zero-field cases do not settle arbitrary metrics.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Bialy proves the assertion when the metric is conformally flat and
explicitly conjectures that this assumption can be removed. The zero-field
case follows from Burago–Ivanov. In dimension two, uniformization reduces
the metric to the conformally flat case; the question above concerns
higher dimensions. The 2025 published paper explicitly repeats the
arbitrary-metric torus conjecture.

The newer magnetic-curvature and entropy theorems impose additional
curvature, no-focal-point, or integral-equality hypotheses. They do not
immediately supply the claimed rigidity for an arbitrary metric under the
condition above. The normal Jacobi-field convention used in some of those
papers is kept distinct from Bialy's full ambient vertical condition.

Current-status, duplicate and independent checks are recorded in the
[review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/magnetic-torus-hopf-review.json).
The final eight-page 2000 journal body has not been compared line by line
with the fully read nine-page preprint.


The [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-magnetic-torus-hopf-review.json), [current catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/magnetic-torus-prove2me0166-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/magnetic-torus-coordinator-review-2026-10-18.json) passed at their recorded extents. The latest surface-only comparison, arXiv:2608.13534v2, keeps negative Gaussian curvature and constant magnetic intensity; it does not cover arbitrary higher-dimensional tori. The catalogue check covered all186 current listing pages under six aliases, rather than all linked proof bodies.


### Online recheck, 2026-10-30

The magnetic torus target uses Bialy's full ambient vertical no-conjugate-points convention in dimension >=3. The 2025 magnetic-curvature theorem retains an integral equality/curvature condition, and later entropy theorems add no-focal-point hypotheses. Conformally flat and zero-field cases do not settle arbitrary metrics.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/math/9902013); [status source 2](https://doi.org/10.1007/s00220-024-05166-5); [status source 3](https://arxiv.org/abs/2606.18434). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-d7a7f3d186dc2267** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
