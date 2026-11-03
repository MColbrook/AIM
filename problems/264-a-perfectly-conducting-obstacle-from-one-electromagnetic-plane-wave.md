# 264. A perfectly conducting obstacle from one electromagnetic plane wave

**Area:** Inverse electromagnetic scattering
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`k>0`$, $`d\in\mathbb S^2`$, and $`0\ne p\in\mathbb R^3`$ with $`p\cdot d=0`$. Let $`D_1,D_2\subset\mathbb R^3`$ be bounded connected open sets with connected $`C^2`$ boundaries and connected exteriors. For $`j=1,2`$, let $`(E_j,H_j)`$ be the outgoing electromagnetic field outside $`\overline D_j`$ with incident field

```math
E^i(x)=p e^{ikd\cdot x},\qquad H^i(x)=(d\times p)e^{ikd\cdot x}.
```

The total fields satisfy

```math
\nabla\times E_j=ikH_j,\qquad \nabla\times H_j=-ikE_j,\qquad
\nu_j\times E_j=0\quad\hbox{on }\partial D_j.
```

Writing $`E_j=E^i+E_j^s`$ and $`H_j=H^i+H_j^s`$, impose the Silver–Müller condition

```math
\lim_{r\to\infty}r\bigl(H_j^s(r\hat x)\times\hat x-E_j^s(r\hat x)\bigr)=0
```

uniformly in $`\hat x\in\mathbb S^2`$. Define the complex electric far-field pattern by

```math
E_j^s(r\hat x)=\frac{e^{ikr}}r E_j^\infty(\hat x;k,d,p)+O(r^{-2}).
```

Does

```math
E_1^\infty(\hat x;k,d,p)=E_2^\infty(\hat x;k,d,p)
\quad\hbox{for every }\hat x\in\mathbb S^2
```

imply $`D_1=D_2`$? The wavenumber, incident direction and polarization are each fixed; the data include the complex phase. The question is for every such fixed triple and every pair of domains in this class. No size or convexity assumption is imposed.

## Application

This asks whether a single fixed radar illumination, observed in every far-field direction, uniquely identifies a smooth perfectly conducting three-dimensional object.

## References

- F. Cakoni and D. Colton, *Open problems in the qualitative approach to inverse electromagnetic scattering theory*, European Journal of Applied Mathematics **16** (2005), 411–425, Section3, first open problem: [author-linked copy](https://sites.math.rutgers.edu/~fc292/survey.pdf), [DOI](https://doi.org/10.1017/S0956792505005978).
- R. Kress, *Uniqueness in inverse obstacle scattering for electromagnetic waves*, URSI General Assembly (2002), pp1–3: [author copy](https://num.math.uni-goettingen.de/~rkress/ursi.pdf). The model fixes one incident direction and polarization, and the discussion after Theorem1 explicitly poses the general uniqueness question.
- H. Liu, *A global uniqueness for formally determined inverse electromagnetic obstacle scattering*, Inverse Problems **24** (2008), 035018: [author version](https://arxiv.org/abs/0801.2623). This proves a polyhedral case.

## Status review


**Known cases:** Polyhedral, ball and waveguide results do not determine a general smooth PEC obstacle from one fixed-frequency/direction/polarization plane wave. The broad 2016 claim remains withdrawn; acoustic and elastic boundary conditions are different.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Balls and polyhedral obstacle classes have positive results. General smooth bounded obstacles require a separate argument; the scalar sound-soft obstacle question uses a different boundary condition. A general uniqueness claim by Genqian Liu, [arXiv1606.06529](https://arxiv.org/abs/1606.06529), was explicitly withdrawn in April2021 because of a gap in its main proof. Selected independent formulation, current-status, semantic, coordinator and catalogue checks passed. The supplied aliases matched none of the186 cached catalogue descriptions. These bounded checks do not prove that no solution exists.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/maxwell-single-wave-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-maxwell-single-wave-review.json), [semantic comparison](../FURTHER_problems/_tracking/maxwell-single-wave-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/maxwell-single-wave-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/maxwell-single-wave-coordinator-review-2026-10-19.json) record evidence and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

Polyhedral, ball and waveguide results do not determine a general smooth PEC obstacle from one fixed-frequency/direction/polarization plane wave. The broad 2016 claim remains withdrawn; acoustic and elastic boundary conditions are different.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1606.06529); [status source 2](https://arxiv.org/abs/0801.2623); [status source 3](https://doi.org/10.1017/S0956792505005978). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-f67c2612b1ddd8ed** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
