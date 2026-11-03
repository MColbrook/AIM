# 481. A sharp entropy–dissipation inequality for planar fractional-pressure diffusion

**Area:** Nonlocal diffusion and functional inequalities
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\rho\in C_c^\infty(\mathbb R^2)`$ be nonnegative, with $`\int_{\mathbb R^2}\rho=1`$. Define its half-order Riesz potential by
```math
p_\rho(x)=(-\Delta)^{-1/2}\rho(x)=\frac1{2\pi}\int_{\mathbb R^2}\frac{\rho(y)}{|x-y|}\,dy.
```

The gradient is the distributional gradient, equivalently the usual principal-value singular integral; it is smooth for these data. Put
```math
\mathcal E(\rho)=\frac12\int\rho p_\rho+\frac12\int |x|^2\rho,
\qquad
\mathcal I(\rho)=\int\rho\,|\nabla p_\rho+x|^2.
```

All integrals are over $`\mathbb R^2`$. Set
```math
R=(3/8)^{1/3},\qquad
\rho_*(x)=\frac4\pi(R^2-|x|^2)_+^{1/2}.
```

Thus $`\int\rho_*=1`$ and $`\mathcal E(\rho_*)=3R^2/5`$. Is
```math
\boxed{\quad\mathcal E(\rho)-\frac35R^2\leq\frac12\mathcal I(\rho)\quad}
```

true for every such $`\rho`$?

This asks for a concrete planar instance of the higher-dimensional inequality posed by Carrillo, Huang, Santos and Vázquez. It imposes no radial symmetry, connected-support or positivity-on-the-whole-plane assumption. The reference profile is not required to lie in the smooth test class, and no equality classification is requested.

## Application

The quantities are the free energy and its dissipation for the confined fractional-pressure porous-medium flow
```math
\partial_t\rho=\nabla\cdot\bigl(\rho(\nabla(-\Delta)^{-1/2}\rho+x)\bigr).
```

Together with a justified energy-dissipation identity, the inequality would give exponential decay of relative energy at rate $`2`$ in this normalization. It is a functional inequality; weak-solution uniqueness is a separate question.

## References

1. J. A. Carrillo, Y. Huang, M. C. Santos and J. L. Vázquez, *Exponential convergence towards stationary states for the 1D porous medium equation with fractional pressure*, J. Differential Equations **258** (2015), 736–763, [doi:10.1016/j.jde.2014.10.003](https://doi.org/10.1016/j.jde.2014.10.003). [Pinned arXiv v1](https://arxiv.org/pdf/1407.4392v1), §1 and §2.1, physical pp. 2–8: energy (1.8), dissipation, inequality (2.7), and sharp product formulation (2.9); the paragraph following (2.9) explicitly asks to prove or disprove it in higher dimensions. The served [HTML](https://arxiv.org/html/1407.4392) numbers the corresponding inequalities (2.12) and (2.14).
2. J. L. Vázquez, *The mathematical theories of diffusion. Nonlinear and fractional diffusion*, [arXiv:1706.08241v1](https://arxiv.org/pdf/1706.08241v1), §6, especially pp. 40–41, describes the higher-dimensional convergence-rate problem and its connection with unknown functional inequalities.

## Status review

Reviewed 18 October 2026; an independent selected-primary audit confirmed the formulation and constants. Coordinator current, semantic and catalogue checks are complete at the selected scope recorded below. The original theorem proves the corresponding inequality in one dimension. The planar question above specializes the source's higher-dimensional problem to $`d=2`$, $`s=1/2`$, mass $`1`$ and confinement coefficient $`1`$.

The mobility-$`\sqrt u`$ fast-diffusion model of Dolbeault–Zhang has different energy and dissipation. Its statement that some fractional interpolation optimizers differ from self-similar profiles does not by itself decide this inequality. General fractional Sobolev inequalities and failure of Wasserstein displacement convexity do not automatically imply either answer here. AIM 466 concerns weak uniqueness of a related evolution equation and has a different target.

The full 2015 publisher body has not been compared with the pinned preprint. The inspected 2025 Lévy-pressure theorem constructs unconfined weak solutions; the 2026 finite-element theorem adds ordinary diffusion on a bounded spectral-Neumann domain. The current finite-difference paper states discrete conservation and dissipation results. None of those inspected statements supplies this sharp whole-plane inequality. The OpenAI subgaussian log-concave theorem concerns relative entropy for test functions against a fixed measure, rather than this nonlinear density-dependent Riesz energy. All 186 cached all-status catalogue descriptions returned zero supplied-alias matches; this is a description comparison, not a review of mission proofs. Publication-version and full-body access gaps remain explicit. No matching full resolution was located in the bounded checks; this does not establish exhaustive absence of a solution. No proof of the proposed inequality is claimed.

The [primary review](../FURTHER_problems/_tracking/parallel/continuum/fractional-pressure-lsi-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-fractional-pressure-lsi-review.json), [semantic comparison](../FURTHER_problems/_tracking/fractional-pressure-lsi-duplicates-review-2026-10-18.json), [catalogue comparison](../FURTHER_problems/_tracking/fractional-pressure-lsi-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/fractional-pressure-lsi-coordinator-review-2026-10-18.json) record the scope and limits. These are AI checks, not human peer review or certification of every cited proof.


### Online recheck, 2026-10-30

The one-dimensional entropy-dissipation result uses displacement convexity absent in the plane. Higher-dimensional existence/discrete dissipation or different fractional fast-diffusion functionals do not establish this sharp whole-plane Riesz-energy inequality.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1407.4392); [status source 2](https://arxiv.org/abs/1706.08241). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-67078dd7e6e16552** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
