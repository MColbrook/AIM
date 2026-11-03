# 950. Global regularity for strictly positive periodic scalar stretching

**Area:** Nonlocal evolution equations; viscoelasticity models
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T^2=(\mathbb R/(2\pi\mathbb Z))^2`$. Define the periodic Riesz transform $`R_1`$ by

```math
\widehat{R_1h}(k)=-i\frac{k_1}{|k|}\widehat h(k)\quad(k\in\mathbb Z^2\setminus\{0\}),
\qquad \widehat{R_1h}(0)=0.
```

Thus $`R_1^2`$ has multiplier $`-k_1^2/|k|^2`$ at nonzero modes and zero at the origin. For every real $`\omega_0\in C^\infty(\mathbb T^2)`$ with $`\min\omega_0>0`$, consider

```math
\partial_t\omega=\omega R_1^2\omega,\qquad \omega(0,x)=\omega_0(x).
```

**Does its unique local smooth solution extend smoothly to every finite time?** Equivalently, can a finite maximal time of smooth existence occur for any such strictly positive initial datum? Smooth extension means $`\omega\in C^1([0,T];H^s(\mathbb T^2))`$ for every finite $`T`$ and every $`s>1`$, with the displayed equation and initial trace. Positivity is preserved as long as the smooth solution exists. There is no smallness or Fourier-cone condition on the datum.

## Application

This scalar equation isolates a quadratic nonlocal stretching mechanism from a model of polymeric fluids. It tests whether dissipation and strict positivity can prevent singularities in that simplified mechanism; it does not assert regularity for the tensorial Oldroyd–B fluid system.

## References

1. R. Bianchini and T. M. Elgindi, *Finite-time singularity formation for scalar stretching equations*, Nonlinearity **38** (2025), 075003, [DOI](https://doi.org/10.1088/1361-6544/addcae). The explicit question is §3.4, published pp. 9–10; [author manuscript](https://arxiv.org/abs/2407.16450v1), p. 9. The actual publisher-provided [published full text](https://www.researchgate.net/publication/392372714_Finite-time_singularity_formation_for_scalar_stretching_equations) retains it.
2. P. Constantin and W. Sun, *Remarks on Oldroyd-B and related complex fluid models*, Communications in Mathematical Sciences **10** (2012), 33–73, §6, [published PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cms/2012/0010/0001/CMS-2012-0010-0001-a003.pdf), [DOI](https://doi.org/10.4310/CMS.2012.v10.n1.a3). Their Fourier-cone condition gives a restricted global class.
3. D. Du, J. Li and X. Shi, *On self-similar singular solutions to a vorticity stretching equation*, [arXiv:2512.15017v1](https://arxiv.org/abs/2512.15017v1), equations (0.1)–(0.2) and Theorems 1.1–1.2, for comparison of the opposite sign and whole-space model.

## Status review


**Known cases:** Strictly positive periodic data with this sign of the Riesz-square stretching are required. Whole-space nonnegative cone-supported blowup and the opposite-sign model do not supply a counterexample.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Strictly positive periodic data with this sign of the Riesz-square stretching are required. Whole-space nonnegative cone-supported blowup and the opposite-sign model do not supply a counterexample.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2025 source explicitly distinguishes its nonnegative, cone-supported whole-space blow-up construction from this strictly positive torus question. With $`f=\log\omega`$, one has $`f_t=R_1^2(e^f)`$, conserved mean $`f`$, and

```math
\frac12\frac{d}{dt}\int_{\mathbb T^2}|\nabla f|^2
=-\int_{\mathbb T^2}e^f|\partial_1f|^2\le0.
```

These bounds control every fixed finite $`L^p`$ norm of $`\omega`$ through the two-dimensional Moser–Trudinger inequality. They do not directly supply a uniform $`L^\infty`$ or smooth continuation estimate.

The December 2025 announcement uses $`Z_{11}=\partial_{11}\Delta^{-1}=-R_1^2`$ and the equation $`w_t=wZ_{11}w`$ on $`\mathbb R^2`$. Under the sign change $`w=-\omega`$, its positive-integral blow-up data have the opposite sign to the present positive $`\omega`$. Its compactly supported or $`L^2`$ whole-space profiles do not give smooth strictly positive periodic counterexamples. A later survey's unrestricted statement that scalar stretching equations admit some singular data also has no positivity restriction.

Current searches on 17 October 2026 found no matching resolution or announced solution. The independent selected-primary audit and the scoped catalogue comparison passed; the review records retain the exact current-status comparisons and access limits. No absence proof is claimed.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/scalar-positive-stretching-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-scalar-positive-stretching-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/scalar-stretching-duplicate-query-receipt.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/scalar-positive-stretching-prove2me0145-review.json) and [coordinator review](../FURTHER_problems/_tracking/scalar-positive-stretching-coordinator-review-2026-10-17.json) record the checked conventions and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a9a98b190b25ceba**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
