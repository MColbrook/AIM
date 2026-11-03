# 634. Strong unique continuation under a small local form bound

**Area:** Partial differential equations and quantum mechanics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every dimension $`n`$, does there exist $`\varepsilon_n\in(0,1)`$ such that the following holds? Let $`V\in L^2_{\mathrm{loc}}(\mathbb R^n;\mathbb R)`$ satisfy, for every $`R>0`$ and some $`c_R\ge0`$,
```math
\int_{B_R}|V||u|^2\le\varepsilon_n\int_{\mathbb R^n}|\nabla u|^2
+c_R\int_{\mathbb R^n}|u|^2
\quad(u\in C_c^\infty(\mathbb R^n)).
```

If $`\Psi\in H^1_{\mathrm{loc}}(\mathbb R^n;\mathbb C)`$ weakly solves $`-\Delta\Psi+V\Psi=0`$ and, at some $`x_0`$,
```math
\int_{B_r(x_0)}|\Psi|^2=O(r^m)\quad\text{for every }m\ge1,
```

must $`\Psi\equiv0`$? Here $`B_R=B_R(0)`$; the same $`\varepsilon_n`$ applies for all $`R`$.

This real-potential version retains the conjecture's inherited $`L^2_{\mathrm{loc}}`$ hypothesis. It is known for $`n\le4`$; the remaining dimensional range is $`n\ge5`$.

## Application

The question concerns singular quantum potentials and whether local invisibility forces a wavefunction to vanish everywhere.

## References

1. L. Garrigue, [*Unique continuation for many-body Schrödinger operators and the Hohenberg-Kohn theorem*](https://arxiv.org/html/1804.07564v7), corrected v7 (2019), Section 1.1, conjecture following Theorem 1.1, and Proposition 2.1. Related published article: *Mathematical Physics, Analysis and Geometry* **21** (2018), 27; [DOI](https://doi.org/10.1007/s11040-018-9287-z).
2. D. Kinzebulatov and L. Shartser, [*Schrödinger operators and unique continuation. Towards an optimal result*](https://arxiv.org/html/0902.0423), Introduction and Section 2; *Journal of Functional Analysis* **258** (2010), 2662–2681. [DOI](https://doi.org/10.1016/j.jfa.2009.09.019).
3. R. Gibara and D. Kinzebulatov, [*On the vanishing of Green's function, desingularization and Carleman's method*](https://arxiv.org/html/2202.10528), v2 (2022), Section 5, Theorem 2.
4. T. Carvalho Corso, [*A maximal Hohenberg-Kohn theorem for non-interacting systems via potential theory*](https://arxiv.org/abs/2607.12852), v3 (2026), Section 2.5.

## Status review


**Known cases:** Retains real L2-local potentials with a small local form bound in every dimension. Later many-body Lebesgue-potential UCP and non-interacting Hohenberg–Kohn results do not establish this high-dimensional general form-bound conjecture.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Critical Lebesgue-potential theory covers the stated low dimensions. Higher-dimensional results in reference 2 impose a stricter potential condition; reference 3 treats dimension three. Reference 4 proves a non-interacting density theorem by a different route, without establishing this wavefunction UCP. Vanishing on a set of positive measure also reduces to infinite-order vanishing under the displayed bound, by Garrigue's Proposition 2.1.

The [coordinating review](../FURTHER_problems/_tracking/focused-small-form-bound-Schrodinger-UCP-C189-A-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, current-resolution, announcement and semantic duplicate checks, with independent model review. It uses the corrected conjecture directly because its historical Simon cross-reference is inconsistent. Bounded checks do not prove continued openness.


### Online recheck, 2026-10-30

Retains real L2-local potentials with a small local form bound in every dimension. Later many-body Lebesgue-potential UCP and non-interacting Hohenberg–Kohn results do not establish this high-dimensional general form-bound conjecture.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1804.07564); [status source 2](https://arxiv.org/abs/0902.0423); [status source 3](https://arxiv.org/abs/2607.12852). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-f49eb0b764a586f7** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
