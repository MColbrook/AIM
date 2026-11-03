# 1027. Does the Steklov spectrum determine the boundary Laplace spectrum?

**Area:** Spectral geometry and inverse boundary problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, and let $`(\Omega_1,g_1)`$ and $`(\Omega_2,g_2)`$ be smooth compact $`n`$-dimensional Riemannian manifolds with smooth nonempty boundary. Require each connected component to meet the boundary. The manifolds and their boundaries may have several connected components; no orientability assumption is imposed.

For each manifold, let $`\sigma_j(\Omega_i,g_i)`$ be the ordinary, unweighted Steklov eigenvalues, repeated with multiplicity, of

```math
\Delta_{g_i}u=0\quad\text{in }\Omega_i,
\qquad \partial_{\nu_i}u=\sigma u\quad\text{on }\partial\Omega_i,
```

where $`\nu_i`$ is the outward unit normal. These are the eigenvalues of the Dirichlet-to-Neumann map on the full boundary. Set $`h_i=g_i|_{T\partial\Omega_i}`$, and let $`\lambda_j(\partial\Omega_i,h_i)`$ be the eigenvalues of the nonnegative Laplace–Beltrami operator $`-\Delta_{h_i}`$ on the closed boundary. Both lists include zero eigenvalues with their full multiplicities.

Does

```math
\sigma_j(\Omega_1,g_1)=\sigma_j(\Omega_2,g_2)
\quad\text{for every }j\ge0
```

imply

```math
\lambda_j(\partial\Omega_1,h_1)=\lambda_j(\partial\Omega_2,h_2)
\quad\text{for every }j\ge0?
```

Prove this implication for every $`n\ge3`$, or construct a pair that violates it in some such dimension. The data consist only of the Steklov eigenvalues at frequency zero. Equality of the full Dirichlet-to-Neumann maps, of spectra at other frequencies, or of all Robin spectra is not assumed. The requested conclusion is equality of boundary spectra, not isometry of the boundaries.

## Application

The Dirichlet-to-Neumann operator maps prescribed boundary values to the normal flux of their harmonic extension through the interior. This question asks whether its eigenvalues determine the intrinsic Laplace spectrum of the boundary itself. It concerns exact identifiability from an infinite spectrum, rather than reconstruction from finitely many noisy measurements.

## References

1. A. Girouard and I. Polterovich, *Spectral geometry of the Steklov problem*, Journal of Spectral Theory **7** (2017), 321–359, §5.1, Open Problem 7 on p.344. [DOI](https://doi.org/10.4171/JST/164); [published PDF](https://ems.press/content/serial-article-files/33609).
2. A. Girouard, L. Parnovski, I. Polterovich and D. A. Sher, *The Steklov spectrum of surfaces: asymptotics and invariants*, Mathematical Proceedings of the Cambridge Philosophical Society **157** (2014), 379–389. [DOI](https://doi.org/10.1017/S030500411400036X); [arXiv manuscript](https://arxiv.org/abs/1311.5533), Question 1.11 on p.3 and Corollary 1.12 on p.4 of version 1.
3. B. Colbois, A. Girouard, C. Gordon and D. Sher, *Some recent developments on the Steklov eigenvalue problem*, Revista Matemática Complutense **37** (2024), 1–161, §9, Open Question 9.1. [Published article](https://doi.org/10.1007/s13163-023-00480-3).

## Status review


**Known cases:** The implication is between spectra alone at frequency zero for arbitrary higher-dimensional manifolds. Equality of full maps, strong isospectrality, conformal-class rigidity and surface boundary-length recovery are stronger hypotheses or narrower settings.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The implication is between spectra alone at frequency zero for arbitrary higher-dimensional manifolds. Equality of full maps, strong isospectrality, conformal-class rigidity and surface boundary-length recovery are stronger hypotheses or narrower settings.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

For surfaces, the implication is known: the Steklov spectrum determines the multiset of lengths of boundary components, which determines the Laplace spectrum of their disjoint union of circles. The question therefore starts in dimension three. The usual cylinder, Sunada and torus-action examples of Steklov isospectrality preserve boundary Laplace spectra and do not answer it negatively.

The August 2026 [Hu–Shi–Tang construction](https://arxiv.org/html/2608.10557v2), Theorem 1.1.2, claims noncongruent strictly convex planar domains with identical Steklov spectra. Their boundaries are circles of the same intrinsic length, so their boundary Laplace spectra also agree. Taking products does not automatically extend that construction to a counterexample here: the separation argument uses additional, nonzero-frequency spectra absent from the hypothesis.

The September 2026 version of [Florentin's conformal rigidity theorem](https://arxiv.org/html/2501.15535v4), Theorem I.2, assumes a fixed conformal class, Anosov boundary dynamics with simple length spectrum, and equality of the conformal factor to one on the boundary. It does not settle the unrestricted implication above.

Current searches located no full resolution or announced counterexample for this exact question. AIM295 concerns interior Dirichlet spectra and planar shape, while AIM051 uses the full boundary operator on known geometry. Neither is the present spectral implication. An independent selected-primary audit confirmed the statement, component conventions and current comparisons. The fresh186-page catalogue scan returned12 spectral/name contexts; all were read and concern unrelated journal citations, transforms, nodal lengths, symplectic packing or conformal rigidity. These listing checks do not certify mission proofs. The complete published2017survey and original2013manuscript were read for discovery; only recorded sections of the2024survey and recent follow-ups were inspected. The final2014publication remains a separate edition comparison gap, while the exact question is verified directly in the published2017and2024sources.

[Detailed source and status review](../FURTHER_problems/_tracking/parallel/rough-filtering/steklov-boundary-spectrum-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-steklov-boundary-spectrum-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/steklov-prove2-0100-review.json) and [coordinator review](../FURTHER_problems/_tracking/steklov-coordinator-review-2026-10-17.json) record the dated evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c90002eaa1e080c2**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
