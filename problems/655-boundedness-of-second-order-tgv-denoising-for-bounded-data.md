# 655. Boundedness of second-order TGV denoising for bounded data

**Area:** Inverse problems and imaging
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded connected Lipschitz domain, let $`a,b>0`$, and let $`f\in L^\infty(\Omega;\mathbb R)`$. Define second-order total generalized variation by
```math
\mathrm{TGV}_{a,b}^2(u)
 =\inf_{w\in BD(\Omega;\mathbb R^2)}
 \bigl(a|Du-w\,dx|(\Omega)+b|Ew|(\Omega)\bigr).
```

Here $`BV`$ consists of integrable scalar functions whose distributional gradient is a finite Radon measure; $`BD`$ consists of integrable vector fields whose symmetrized distributional gradient $`Ew=(Dw+Dw^{\mathsf T})/2`$ is a finite Radon measure. Total variations use the Euclidean and Frobenius norms, respectively.

Let $`u`$ be the unique minimizer over $`BV(\Omega)\cap L^2(\Omega)`$ of
```math
\frac12\int_\Omega |u-f|^2\,dx+\mathrm{TGV}_{a,b}^2(u).
```

No boundary traces are prescribed. Must $`u\in L^\infty(\Omega)`$ for every such choice?

Only boundedness is requested, without a bound by the data range, a bound on the auxiliary field, smoothing, or a restriction on $`b/a`$.

## Application

TGV denoising is used to retain image edges while reducing the staircasing associated with first-order total variation. This asks whether bounded input intensities always produce a bounded continuum reconstruction.

## References

- L. Calatroni and K. Papafitsoros, [*Analysis and optimisation of a variational model for mixed Gaussian and Salt & Pepper noise removal*](https://arxiv.org/abs/1809.08991), 2018, paragraph following Proposition 2.6, printed p. 12; domain convention on p. 5.
- K. Bredies, J. A. Iglesias and G. Mercier, [*Boundedness and Unboundedness in Total Variation Regularization*](https://link.springer.com/article/10.1007/s00245-023-10028-y), Applied Mathematics & Optimization 88 (2023), 51, Section 5, equations (48)–(49), Propositions 6–7 and Appendix A.
- K. Papafitsoros, L. Calatroni and A. Kofler, [*Learning spatially varying regularisation parameters of low regularity for image reconstruction*](https://arxiv.org/html/2608.25127v1), 2026, Section 2.3.

## Status review

Checked 2026-10-30. The 2018 source explicitly asks the bounded-data question. The 2023 positive planar result concerns ICTV, whose auxiliary field is a scalar potential's gradient. Its nonoptimal-field examples do not refute the TGV assertion. The 2026 review still assumes bounded solutions in its higher-dimensional jump results.

Bounded current searches found no matching complete resolution or announcement. AIM 437 concerns higher regularity of a different, first-order ROF minimizer. No equivalent target was located among nearby full statements in AIM, this collection or the current OpenAI announcement index.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-TGV-L2-bounded-data-bounded-minimizer-C347-A-20261030/OWNER-EXACT-PLANAR-UNSMOOTHED-TGV2-L2-BOUNDED-DATA-BOUNDEDNESS-PRIMARY-CURRENT-AND-SEMANTIC-PROPOSAL.json), [independent model check](../FURTHER_problems/_tracking/focused-TGV-L2-bounded-data-bounded-minimizer-C347-A-20261030/B-INDEPENDENT-TGV2-BD-FREEBOUNDARY-BOUNDEDNESS-ICTV-AND-NONOPTIMAL-EXAMPLES-MODEL-PEER.json), [coordinating review](../FURTHER_problems/_tracking/ROOT-FINAL-planar-TGV2-bounded-data-minimizer-admission-20261030.json).


### Online recheck, 2026-10-30

ICTV boundedness controls a more restricted auxiliary field, and first-order TV clipping arguments do not apply to unsmoothed second-order TGV. The 2026 spatial-parameter work still assumes bounded solutions where required; no theorem for every bounded datum and a,b>0 located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1809.08991); [status source 2](https://doi.org/10.1007/s00245-023-10028-y); [status source 3](https://arxiv.org/abs/2608.25127). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-1c9e82b2b167417c** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
