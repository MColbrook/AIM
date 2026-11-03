# 689. A sharp affine-modulus bound for harmonic homeomorphisms

**Area:** Complex analysis and geometric function theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega,\Omega^*\subset\mathbb C`$ be nondegenerate doubly connected domains: each is connected and open, and each of the two components of its complement in the Riemann sphere contains more than one point. Define
```math
\mathrm{Mod}(\Omega)=\log(R/r)
```

when $`\Omega`$ is conformally equivalent to $`\{z:r<|z|<R\}`$, where $`0<r<R<\infty`$. Define its affine modulus by
```math
\mathrm{Mod}_{\rm aff}(\Omega^*)
=\sup_{\phi}\mathrm{Mod}(\phi(\Omega^*)),
\qquad \phi(z)=az+b\overline z+c,\quad |a|^2-|b|^2\ne0.
```

The supremum ranges over all invertible real affine maps and may be infinite.

If a harmonic homeomorphism $`h:\Omega\to\Omega^*`$ exists, must
```math
\mathrm{Mod}_{\rm aff}(\Omega^*)
\ge \log\cosh\bigl(\mathrm{Mod}(\Omega)\bigr)
```

hold? Here harmonic means that both real coordinate functions of $`h`$ are harmonic.

No boundary smoothness, boundedness, finite energy, prescribed boundary correspondence, symmetry or orientation is assumed. This asks for a universal necessary condition. It is one family across all such domain pairs, including the circular-annulus case.

## Application

Harmonic homeomorphisms model planar elastic deformations that remain globally invertible. This conjecture asks for a sharp geometric obstruction to such a deformation, allowing affine changes of the target. It also connects with minimal-surface existence. It does not prescribe boundary data or assert that the inequality suffices for existence.

## References

1. T. Iwaniec, L. V. Kovalev and J. Onninen, [*Harmonic mapping problem and affine capacity*](https://arxiv.org/abs/1001.2124v1), sole arXiv v1, 13 January 2010, Definition1.1/Theorem1.2, physical p.2, Conjecture1.3, p.3, and annulus affine equality, p.5. Associated publication: *Proceedings of the Royal Society of Edinburgh Section A* **141** (2011), 1017–1030, [DOI](https://doi.org/10.1017/S0308210510000107). The locators refer to the inspected preprint; complete final-body parity remains unchecked.
2. D. Bshouty and A. Lyzzaik, [*On the Teichmüller–Nitsche Problem of T. Iwaniec, L.V. Kovalev, and J. Onninen*, published PDF](https://scholarworks.aub.edu.lb/server/api/core/bitstreams/fd59a065-f3f4-4ae0-901f-cf9fc930e716/content), *Computational Methods and Function Theory* (2023), [DOI](https://doi.org/10.1007/s40315-023-00504-5), Introduction, Conjecture1/Theorem1 and Section4, physical pp.19–20.
3. D. Kalaj, J. Liu and J.-F. Zhu, [*On an Iwaniec–Kovalev–Onninen Conjecture for harmonic quasiconformal annulus mappings*](https://arxiv.org/html/2609.29795v1), sole arXiv v1, 24 September 2026, Section1, especially Conjecture1.1 and Remark1.2. This is a different upper-bound counterexample announcement; its complete proof has not been independently certified here.

## Status review


**Known cases:** The September Kalaj-Liu-Zhu examples disprove an upper distortion bound and satisfy the present lower bound. Higher-dimensional annular results and the known circular planar case do not settle arbitrary doubly connected planar domains.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September Kalaj-Liu-Zhu examples disprove an upper distortion bound and satisfy the present lower bound. Higher-dimensional annular results and the known circular planar case do not settle arbitrary doubly connected planar domains.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The discovery source [1] states the displayed sharp necessary bound as Conjecture1.3. Its proved general bound is weaker. The circular-target case follows from the proved Nitsche theorem. Sharpness is witnessed, for every $`\tau>0`$, by
```math
h(z)=\frac12\left(z+\frac1{\overline z}\right),
\qquad 1<|z|<e^\tau,
```

whose target is $`1<|w|<\cosh\tau`$ and has affine modulus $`\log\cosh\tau`$.

The published paper [2] explicitly retains the same inequality as Conjecture1. It establishes a necessary condition for harmonic homeomorphisms between Teichmüller slit domains. Its numerical comparison of necessary bounds does not construct a map violating the conjecture or establish an attained infimum; the final paragraph explicitly leaves existence of a violating pair unresolved. Its stronger-sounding numerical discussion is therefore not treated as an announced counterexample.

The September2026 preprint [3] announces counterexamples to an **upper** bound involving quasiconformal distortion $`K`$ for circular-annulus mappings. Those examples map $`1<|z|<s`$ onto $`1<|w|<S`$ with $`1<s<S`$. They satisfy $`\log S>\log s>\log\cosh(\log s)`$, so they satisfy the lower bound asked here. The same introduction retains the proved lower Nitsche restriction.

Conformal changes of the source preserve harmonicity. Arbitrary conformal changes of the target do not, so uniformizing both domains does not reduce the whole conjecture to circular annuli. Orientation reversal is harmless because target conjugation preserves harmonicity and the affine modulus.

The complete pinned14-page discovery preprint was read for question discovery. An independent selected audit checked the formulation, circular sharpness and later comparison scopes. Final2011 body parity and the remaining referenced bodies remain tracked coverage gaps. No matching complete resolution or announcement was located in bounded current searches and semantic checks against AIM, OpenAI results and this collection; exhaustive absence and complete proof certification are not claimed.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/harmonic-affine-modulus-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-harmonic-affine-modulus-review.json), [current comparisons](../FURTHER_problems/_tracking/parallel/complex-bayesian/harmonic-affine-modulus-current-comparisons.json), [duplicate review](../FURTHER_problems/_tracking/harmonic-affine-modulus-duplicates-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/harmonic-affine-modulus-coordinator-review-2026-10-19.json) preserve the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-528a7cb2ab09cbae**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
