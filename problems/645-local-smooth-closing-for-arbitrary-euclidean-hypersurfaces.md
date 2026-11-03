# 645. Local smooth closing for arbitrary Euclidean hypersurfaces

**Area:** Symplectic geometry and Hamiltonian dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`n\ge2`$ and every smooth compact regular co-oriented hypersurface $`i:M\hookrightarrow\mathbb R^{2n}`$, set
```math
\omega=i^*\omega_{\rm std},\qquad
\omega_{\rm std}=\sum_{j=1}^n dq_j\wedge dp_j.
```

Does there exist a symplectic form $`\Omega`$ on $`\mathbb R\times M`$ with $`i_0^*\Omega=\omega`$, where $`i_0(m)=(0,m)`$, and a residual subset $`\Sigma`$ of the Fréchet space $`C^\infty(M,\mathbb R)`$ such that the following holds?

For every $`f\in\Sigma`$, set $`M_f=\{(f(m),m):m\in M\}`$. The union of the closed leaves of
```math
L_f=\ker\bigl(\Omega|_{TM_f}\bigr)
```
must be dense in $`M_f`$.

Residual means containing a countable intersection of open dense sets in the usual $`C^\infty`$ topology. One $`\Omega`$ is chosen for each $`M`$ and fixed for all $`f`$.

**Genericity convention.** Definition 1.7 says “Baire subset” without defining the phrase. This entry adopts its intended generic, residual interpretation, supported by the following discussion and independent review.

## Application

Closed characteristics are periodic Hamiltonian trajectories on an energy hypersurface. The question concerns generic spatial density under smooth changes, beyond the contact-type setting. It connects perturbation questions in Hamiltonian mechanics to symplectic geometry and pseudoholomorphic-curve methods.

## References

1. J. W. Fish and H. Hofer, [*Almost existence from the feral perspective and some questions*](https://doi.org/10.1017/etds.2021.20), Ergodic Theory and Dynamical Systems **42** (2022), 792–834. Canonical statement: [arXiv:2006.16351v1](https://arxiv.org/pdf/2006.16351v1), 29 June 2020, Definitions 1.1–1.2, 1.7–1.8 and Conjecture 1, manuscript pp. 3–4 and 8–9. Published-body parity was inaccessible.
2. K. Irie, [*Strong Closing Lemmas in Hamiltonian Dynamics*](https://doi.org/10.1137/25M1805400), Proceedings of the International Congress of Mathematicians 2026, Volume 4, pp. 179–198, published 13 July 2026; Sections 2, 3 and 7. The bounded native comparison used the author PDF [arXiv:2512.05523](https://arxiv.org/abs/2512.05523); published section context was also checked.

## Status review


**Known cases:** Current closing results cover contact-type, ellipsoid, near-periodic and other restricted Hamiltonian settings. They do not supply the specified compatible symplectic form and residual graph statement for every compact Euclidean hypersurface.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Checked 2026-10-23.** The original arXiv history still has only v1. Its following discussion distinguishes the known contact-type case in $`\mathbb R^4`$ from arbitrary hypersurfaces. The current survey [2] treats special classes including ellipsoids, near-periodic contact forms and selected Hamiltonian maps. Its general near-periodic theorem has additional Gromov–Witten/SFT assumptions. These results do not establish the stated arbitrary-hypersurface property.

The global smooth Hamiltonian closing statement on tori discussed in [2, Section 2] is a different formulation. This entry retains compact hypersurfaces in standard Euclidean symplectic space and the specified compatible-form and graph quantifiers.

Independent review confirmed the explicitly adopted residual reading. All-status AIM and FURTHER checks distinguish fixed-surface orbit counts, fixed-flow existence and the $`C^1`$ stable-capture question. Bounded current proof and announcement searches found no matching complete resolution. Prove2Me's current page was inaccessible; indexed queries found no exact match, with the access gap retained.

[Coordinator review](../FURTHER_problems/_tracking/fish-hofer-closing-coordinator-review-2026-10-23.json) · [Duplicate review](../FURTHER_problems/_tracking/fish-hofer-closing-duplicate-review-2026-10-23.json) · [Independent review](../FURTHER_problems/_tracking/journal1135-Fish-Hofer-independent-peer-audit-2026-10-23.json).


### Online recheck, 2026-10-30

Current closing results cover contact-type, ellipsoid, near-periodic and other restricted Hamiltonian settings. They do not supply the specified compatible symplectic form and residual graph statement for every compact Euclidean hypersurface.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2512.05523); [status source 2](https://arxiv.org/abs/2006.16351). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-6a8010fe5c2c360f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
