# AIM 689: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/689-a-sharp-affine-modulus-bound-for-harmonic-homeomorphisms.md) · [Manuscript](../../solutions/689-a-sharp-affine-modulus-bound-for-harmonic-homeomorphisms/main.pdf) · [Source and provenance](../../solutions/689-a-sharp-affine-modulus-bound-for-harmonic-homeomorphisms/README.md).

## Verdict and exact scope

Counterexample to the sharp bound after the complete real-affine optimization.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

Direct differentiation gives the stated Jacobian. Its first-order perturbation is controlled uniformly down to t=0, and the intermediate Jordan curves and positive degree prove a global homeomorphism, rather than only local invertibility.

The logarithmic boundary expansions give A=2, B=-1 for the harmonic perturbation and the coefficient -(1-R^(-2)). The affine mode has angular frequency two and yields -2(R^2-1)/(R^2+1). Rotation invariance excludes mixed quadratic terms. The fixed-annulus energy formulation supplies joint analytic dependence and a uniform cubic remainder; the local negative quadratic estimate therefore holds simultaneously for all small affine parameters.

The Carleman area calculation has the correct sign for negative Laurent indices and its equality case forces a round annulus. It gives a strict deficit on compact affine-parameter sets away from zero. The vertical-segment condenser estimate forces modulus to zero as the affine determinant degenerates, uniformly for small harmonic perturbations. These local, compact, and degenerating regimes cover the full supremum. Thus the result is a complete counterexample to the affine bound, not merely a decrease of ordinary modulus. The numerical record is supplementary and is not used to justify the global supremum or an explicit perturbation threshold.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/1001.2124)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 4a41ee2d41aa3a3287a90d00a131a74c2d5e43af600c04cdcd22d9fe3a3f4d04. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
