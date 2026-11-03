# 398. An electric far-field factorization criterion for a perfect conductor

**Area:** Inverse electromagnetic scattering and operator ranges
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`D\subset\mathbb R^3`$ be a bounded connected open set with connected $`C^2`$ boundary and connected exterior. Fix $`k>0`$ which is not an interior perfectly conducting Maxwell eigenfrequency: there is no nonzero $`V\in H_0(\mathrm{curl};D)`$ with $`\mathrm{div}V=0`$ and $`\mathrm{curl}\mathrm{curl}V=k^2V`$ in $`D`$.

Let $`L_t^2(\mathbb S^2)=\{g\in L^2(\mathbb S^2;\mathbb C^3):g(d)\cdot d=0\text{ a.e.}\}`$. For every transverse polarization $`p`$, let $`E_D^\infty(\hat x;d,p)`$ be the electric far-field pattern for the incident plane wave $`E^i=p e^{ikd\cdot x}`$, $`H^i=(d\times p)e^{ikd\cdot x}`$. The total field satisfies

```math
\nabla\times E=ikH,\qquad\nabla\times H=-ikE
\quad\hbox{in }\mathbb R^3\setminus\overline D,\qquad
\nu\times E=0\quad\hbox{on }\partial D,
```

and the scattered fields satisfy $`r(H^s\times\hat x-E^s)\to0`$ uniformly at infinity. Normalize $`E^s(r\hat x)=e^{ikr}E_D^\infty(\hat x;d,p)/r+O(r^{-2})`$.

Define the compact electric far-field operator $`F:L_t^2(\mathbb S^2)\to L_t^2(\mathbb S^2)`$ by

```math
(Fg)(\hat x)=\int_{\mathbb S^2} E_D^\infty(\hat x;d,g(d))\,ds(d).
```

For $`z\in\mathbb R^3\setminus\partial D`$ and $`0\ne q\in\mathbb R^3`$, put

```math
\phi_z^q(\hat x)=\bigl(I-\hat x\otimes\hat x\bigr)q\,e^{-ik\hat x\cdot z}.
```

This is the electric dipole far-field test function, up to a nonzero scalar constant. Prove or disprove that for every such $`D,k,q,z`$,

```math
z\in D\quad\Longleftrightarrow\quad
\phi_z^q\in\mathrm{Ran}\bigl((F^*F)^{1/4}\bigr).
```

Here $`F^*`$ is the Hilbert-space adjoint and the fourth root is the positive spectral fourth root. The range is the actual operator range, not its closure. The operator $`F`$ is unmodified; the data include every incident direction and polarization.

## Application

An affirmative answer gives an exact inside/outside test for a conducting object using spectral data of its measured far-field operator. This is a different task from recovering an object with only one illumination.

## References

- D. Colton and R. Kress, *Looking Back on Inverse Scattering Theory*, SIAM Review **60** (2018), 779–807, Section3.3, Theorem3.1 and following discussion: [author copy, p19](https://num.math.uni-goettingen.de/kress/looking-back.pdf), [DOI](https://doi.org/10.1137/17M1144763). The displayed formulation makes precise the standard electric-operator analogue posed there.
- F. Cakoni and D. Colton, *Open problems in the qualitative approach to inverse electromagnetic scattering theory*, European Journal of Applied Mathematics **16** (2005), 411–425, Sections2 and4: [author copy](https://sites.math.rutgers.edu/~fc292/survey.pdf), [DOI](https://doi.org/10.1017/S0956792505005978).
- A. Lechleiter, *Factorization method in inverse scattering*, in B. Engquist (ed.), *Encyclopedia of Applied and Computational Mathematics* (2015), pp. 479–485; author manuscript pp. 3–5: [author copy](https://www.math.uni-bremen.de/zetem/cms/media.php/278/factorization.pdf), [DOI](https://doi.org/10.1007/978-3-540-70529-1_17). It identifies the failure of the usual middle-operator coercivity hypothesis for a perfect conductor.

## Status review

The 2018 source explicitly retains the perfectly conducting Maxwell analogue as open. Factorization results for penetrable media, static electromagnetic models, periodic structures or modified measurement operators require separate comparison. Selected independent formulation, current-status, semantic, coordinator and catalogue checks passed. The186 cached catalogue descriptions produced one supplied-alias context, concerning semidefinite lifts of polytopes; its target is different. These bounded checks do not prove that no solution exists. The displayed target is an explicit source-inspired specialization rather than a verbatim fully quantified source statement.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/pec-factorization-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-pec-factorization-review.json), [semantic comparison](../FURTHER_problems/_tracking/pec-factorization-duplicates-review-2026-10-19.json), [catalogue comparison](../FURTHER_problems/_tracking/pec-factorization-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/pec-factorization-coordinator-review-2026-10-19.json) record evidence and limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

The target is the actual range of the unmodified electric far-field operator's quarter power for a PEC obstacle. Modified-operator, penetrable, static and waveguide factorization results avoid the middle-operator obstruction and do not establish this exact criterion.

Comparators and current-status sources: [status source 1](https://num.math.uni-goettingen.de/kress/looking-back.pdf); [status source 2](https://sites.math.rutgers.edu/~fc292/Cakoni-Colton-Monk-CBMS80.pdf); [status source 3](https://doi.org/10.1017/S0956792505005978). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-96efe2be67155a2d** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
