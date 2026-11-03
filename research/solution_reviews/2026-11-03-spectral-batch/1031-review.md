# AIM 1031: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Affirmative proof.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1031-limit-periodic-finite-interval-spectra/aim1031.pdf), [TeX](../../solutions/1031-limit-periodic-finite-interval-spectra/aim1031.tex), and [source receipt](../../solutions/1031-limit-periodic-finite-interval-spectra/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1031](../../../problems/1031-are-non-cantor-spectra-dense-among-nonperiodic-limit-periodic-potentials.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

Nonperiodic limit-periodic potentials with finite unions of nondegenerate spectral intervals are dense among all limit-periodic potentials.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

## Detailed mathematical audit

### Exact target mapping

The target quantifies over every nonperiodic limit-periodic potential and every positive approximation tolerance, requiring another nonperiodic limit-periodic potential whose spectrum has nonempty interior. The manuscript proves this even when the starting potential is periodic and makes the whole approximating spectrum a finite union of nondegenerate intervals. The required nearby potential is explicitly proved nonperiodic; periodic approximation alone is not being substituted for the target.

### Independent proof checks

1. A spectral point of a bounded self-adjoint operator has finitely supported approximate unit eigenvectors: first use the approximate-eigenvector criterion, then approximate in norm by finitely supported vectors and renormalize. Translating by a period preserves the background and the residual. A sufficiently long block, with length a multiple of the period, can contain the translated finite support. Potential differences outside the support do not alter the residual, because they are a multiplication operator. This is the correct reason no extra boundary condition or zero boundary residual is required.
2. The two marker boundaries have identical background phase. For each proposed period `p < L`, the two shift differences are `v_p-2a` and `v_p+2a`; at least one has magnitude at least `2a`. The same three marker blocks thus detect all the finitely many proposed periods required at that stage.
3. For the envelopes, the previous mesh is `delta_{k-1}=a_k/8` for `k>=2`. Every point of an old hull is within this mesh of the old spectrum, and each extension of the hull is within `a_k` of an actual spectral endpoint. Conversely, an `a_k` neighborhood of the old spectrum cannot leave the expanded hulls. These observations prove the exact neighborhood identity (13). It is not an assertion of spectral monotonicity under arbitrary perturbations.
4. A finite `delta_k/4` net, with residuals below `delta_k/4`, gives the required mesh, in fact below `delta_k/2`. Norm continuity of the spectrum gives confinement of *all* new spectral points to the same expanded envelopes. This handles possible spectral points associated with block interfaces; such points are not omitted.
5. Original inter-cluster gaps remain at least `G-2 sum a_k = G-2t/3`, greater than `G/2` under the stated choice. The spectral points close to endpoints of any expanded cluster must therefore be in that cluster. This gives (17)--(18) and nesting of the hulls because `delta_k<a_k`. All hulls remain nondegenerate since the original bands are nondegenerate.
6. The limiting interval union is within `a_k/3` in Hausdorff distance of the stage-k hulls; those hulls are within `delta_k` of the stage-k spectra; the stage-k spectra are within `a_k/3` of the limit operator's spectrum. The triangle inequality therefore bounds the desired distance by `2a_k/3+delta_k`, which tends to zero. Thus there are no residual small gaps or extra spectral components in the limit.
7. The geometric tail is exactly `sum_{s>k} a_s = a_k/3`. A marker of size `2a_k` consequently retains at least `4a_k/3` in the limit. Every fixed positive integer is detected at a stage `k>=p`; hence the limit has no period. The total approximation error is strictly below `epsilon/2+t/3<epsilon`. No quantitative bound on the rapidly growing block lengths is needed.

No proof repair is required. For standalone readability, the norm-continuity fact could be followed by one sentence: if `dist(E,sigma(A)) > ||A-B||`, the resolvent identity and Neumann series imply `E` is in the resolvent set of `B`; interchange `A` and `B`. This is optional because the manuscript already states the standard bounded-self-adjoint result correctly.

### References and limits

The Damanik--Fillman bibliography entry above also applies here. The exact target is Question 10.4, arXiv v1 printed p.36. Periodic nondegenerate bands are established there in Theorem 2.1 and the ensuing description on printed pp.3--4.

D. Damanik, Z. Gan and H. Krüger, *Limit-periodic Schrödinger operators with a discontinuous Lyapunov exponent*, *Journal of Functional Analysis* **279** (2020), no.4, article 108565, DOI <https://doi.org/10.1016/j.jfa.2020.108565>. The primary publisher manuscript text was available through <https://www.sciencedirect.com/science/article/am/pii/S0022123620301087> in search extraction, though a direct subsequent fetch returned 403. Its Theorem 1.3 concerns density of potentials with a Lyapunov-exponent discontinuity at the spectrum's bottom. It is accurately distinguished in the submission and is not being used as a spectral-interior theorem.

No supplied script is associated with 1031. The proof is qualitative and was checked by the exact argument above; no finite numerical computation is needed to justify the density or interval-union conclusion.
