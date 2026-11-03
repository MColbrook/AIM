# 397. Can one Dirichlet spectrum determine a Caputo potential?

**Area:** Inverse problems; fractional differential equations
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix a known order $`\alpha\in(1,2)`$. For a real potential $`q\in L^\infty(0,1)`$ and $`\lambda\in\mathbb C`$, define $`u_q(\cdot,\lambda)`$ as the unique continuous solution of

```math
u_q(x,\lambda)=x+\frac1{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}(q(t)-\lambda)u_q(t,\lambda)\,dt.
```

This Volterra equation specifies the normalized left Caputo problem

```math
-{}^CD_{0+}^\alpha u+qu=\lambda u,\qquad u(0)=0,\quad u'(0)=1.
```

It avoids requiring a classical second derivative of the solution for a merely bounded measurable potential. Let $`\Delta_q(\lambda)=u_q(1,\lambda)`$ and let $`\mathcal S_\alpha(q)`$ be its complete complex zero multiset, each zero repeated according to its order. These are the Dirichlet eigenvalues for $`u(0)=u(1)=0`$; no norming constants or other boundary spectra are supplied.

**Question.** For every $`\alpha\in(1,2)`$ and every pair of real bounded measurable potentials $`q_1,q_2`$, does

```math
\mathcal S_\alpha(q_1)=\mathcal S_\alpha(q_2)
\quad\Longrightarrow\quad q_1=q_2\ \text{almost everywhere on }(0,1)?
```

The complete complex spectrum is meant, including both members of each conjugate pair. No assumption of simple eigenvalues, symmetry of the potential or knowledge on half the interval is imposed. The excluded endpoint $`\alpha=2`$ has classical isospectral nonuniqueness.

## Application

Spectral measurements of anomalous diffusion or fractional wave models may be available when extra boundary excitations or norming constants are inaccessible. The question asks whether the nonselfadjoint complex spectrum of a one-sided fractional model determines its spatial potential by itself.

## References

1. Bangti Jin and William Rundell, *An inverse Sturm–Liouville problem with a fractional derivative*, Journal of Computational Physics **231** (2012), 4954–4966, [DOI](https://doi.org/10.1016/j.jcp.2012.04.005); [arXiv:1204.2475v1](https://arxiv.org/pdf/1204.2475v1), §4(c), PDF13, and AppendixA for the Volterra initial-value formulation.
2. Bangti Jin and William Rundell, *A tutorial on inverse problems for anomalous diffusion processes*, Inverse Problems **31** (2015), 035003, [DOI](https://doi.org/10.1088/0266-5611/31/3/035003); [arXiv:1501.00251v1](https://arxiv.org/pdf/1501.00251v1), §4.1, PDF18–20.

## Status review

The 2012 source explicitly conjectures single-spectrum uniqueness for every fractional order in $`(1,2)`$; its reconstruction results are numerical evidence. The 2015 tutorial says the theoretical uniqueness remains to be established. The bounded-potential class and zero-multiplicity convention above make the spectral data precise without assuming all eigenvalues are simple.

The Riemann–Liouville model and selfadjoint two-sided fractional Sturm–Liouville operators have different boundary and adjoint structure. A 2025 variable-order mixed-derivative inverse theorem uses orders below one, fractional boundary conditions and eigenvalues **plus norming constants**; it does not supply this one-spectrum theorem. Time-fractional diffusion papers with an ordinary second-order spatial Sturm–Liouville operator also concern a different inverse problem.

Checks through 17 October 2026 found no exact proof, counterexample or complete announced resolution. All-status AIM/OpenAI comparisons and the 186-page Prove2Me catalogue scan found no equivalent target. The associated review packet records the exact extents and access limits; search absence is not a proof of openness. No full mathematical certification of either source's numerical reconstruction analysis is claimed.

An apparent uniqueness claim in a thesis cites the original2012§4(c), which is explicitly a conjecture following numerical evidence. A similarly titled2024article uses an ordinary second derivative, periodic boundary conditions and a symmetric potential. Neither supplies the displayed fractional theorem. Full thesis access and full final-edition comparisons remain limited as recorded in the reviews.

The zero-multiset definition fixes the canonical integral realization and characteristic multiplicity; it does not assert equivalence with every alternative closed-operator realization. Negative literature searches are bounded evidence, not a proof of openness.

[Owner review](../FURTHER_problems/_tracking/parallel/rough-filtering/caputo-single-spectrum-review.json), [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-caputo-single-spectrum-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/caputo-spectrum-prove2-0122-review.json) and [coordinator review](../FURTHER_problems/_tracking/caputo-spectrum-coordinator-review-2026-10-17.json) preserve exact assumptions, contrary-claim comparisons and access limits.

A further trace-formula reconstruction paper studies a positive symmetric density multiplying the spectral parameter, rather than an arbitrary additive potential. A second recent paper advertises numerical reconstruction of a symmetric potential. Neither inspected primary statement claims the displayed general uniqueness theorem; final-body access limits remain explicit. [Additional dated comparisons](../FURTHER_problems/_tracking/parallel/rough-filtering/caputo-new-comparators-20261017-review.json).


### Online recheck, 2026-10-30

The exact left-Caputo Volterra characteristic function and its complete complex zero multiset are required. Variable-order mixed derivatives with norming data, self-adjoint two-sided fractional operators and classical spatial Sturm–Liouville inverse results do not prove this one-spectrum theorem.

Comparators and current-status sources: [status source 1](https://doi.org/10.1088/0266-5611/31/3/035003); [status source 2](https://arxiv.org/abs/1204.2475); [status source 3](https://arxiv.org/abs/1712.09894). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-dde636e3c888aba7** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
