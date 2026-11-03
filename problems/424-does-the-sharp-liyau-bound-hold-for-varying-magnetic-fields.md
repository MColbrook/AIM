# 424. Does the sharp Li–Yau bound hold for varying magnetic fields?

**Area:** Spectral theory and mathematical physics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded domain, and let $`A`$ be a smooth real vector potential on a neighbourhood of $`\overline\Omega`$. Denote by $`\lambda_1(\Omega,A)\le\lambda_2(\Omega,A)\le\cdots`$ the Dirichlet eigenvalues, counted with multiplicity, of the magnetic Laplacian $`(-i\nabla+A)^2`$. Is it true, for **every** such $`A`$ and every positive integer $`N`$, that

```math
\sum_{j=1}^{N}\lambda_j(\Omega,A)\ \ge\ \frac{2\pi N^2}{|\Omega|}\,?
```

The issue is a field $`B=\mathrm{curl}A`$ that varies with position. The same sharp bound is known for constant $`B`$; the question is whether its constant survives arbitrary smooth variation. Equivalently, by Legendre duality, one asks for the sharp Berezin bound at Riesz order $`\gamma=1`$ for such fields.

## Application

This would give a universal sharp semiclassical lower bound on the total energy of the first $`N`$ magnetic Dirichlet states, independent of the field's shape and strength. The constant is forced by the large-$`N`$ Weyl asymptotic.

## Known results and scope

Erdős, Loss and Vougalter prove the bound for constant magnetic fields and explicitly ask about arbitrary fields. Their counterexamples disprove **stronger** magnetic comparisons, not the displayed lower bound. For spatially varying fields, the sharp Berezin inequality is known at Riesz order $`\gamma\ge3/2`$; that result does not descend to $`\gamma=1`$. A 2025 primary paper still attributes the $`\gamma=1`$ result to the constant-field setting.

## References

1. L. Erdős, M. Loss and V. Vougalter, [*Diamagnetic behavior of sums Dirichlet eigenvalues*](https://aif.centre-mersenne.org/item/10.5802/aif.1777.pdf), *Annales de l'Institut Fourier* **50** (2000), 891–907, doi:10.5802/aif.1777. Theorem 1, equation (1.10), on printed p. 893; question on pp. 894 and 906.
2. H. Kovařík and T. Weidl, [*Improved Berezin-Li-Yau inequalities with magnetic field*](https://cvgmt.sns.it/media/doc/paper/2321/mag-berezin-final.pdf), introduction, PDF physical pp. 1–3. Its sharp arbitrary-field result begins at Riesz order $`3/2`$, while its order-one and remainder results concern constant fields.
3. M. Baur and T. Weidl, [*Eigenvalues of the magnetic Dirichlet Laplacian with constant magnetic field on disks in the strong field limit*](https://link.springer.com/article/10.1007/s13324-024-01008-8), *Analysis and Mathematical Physics* **15** (2025), article 9, introduction and §2.3, especially equation (10).

## Status review

Reviewed 21 October 2026. Bounded searches for later papers, counterexamples and announcements found no complete variable-field $`\gamma=1`$ result. The [dated status and duplicate audit](../FURTHER_problems/_tracking/magnetic-li-yau-variable-field-status-2026-10-21.json) records the precise comparisons and their limits; absence from a bounded search cannot rule out unindexed work. No equivalent AIM or admitted FURTHER target was found.


### Online recheck, 2026-10-30

The sharp constant-field sum inequality is known. Variable-field bounds at Riesz order >=3/2, or different constants, do not prove the stated sharp order-one Li–Yau inequality for arbitrary smooth magnetic fields.

Comparators and current-status sources: [status source 1](https://www.numdam.org/articles/10.5802/aif.1777/); [status source 2](https://cvgmt.sns.it/media/doc/paper/2321/mag-berezin-final.pdf). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-aba1561af4e8b2e3** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
