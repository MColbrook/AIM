# AIM 721: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/721-real-c1-1-regularity-of-complex-hessian-obstacle-envelopes.md) · [Manuscript](../../solutions/721-real-c1-1-regularity-of-complex-hessian-obstacle/main.pdf) · [Source and provenance](../../solutions/721-real-c1-1-regularity-of-complex-hessian-obstacle/README.md).

## Verdict and exact scope

Real local C1,1 regularity for every stated complex Hessian obstacle envelope.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The dual covariance cone is compact, positive semidefinite and unitarily invariant; it contains I/n. Strictness of the given defining function supplies a common exit barrier. Uniform ellipticity is used only for each fixed smooth approximant. At a maximum of g-v the Hessian inequality has the correct sign, so the larger discount cap is inactive at the solution and the same value solves the smaller-cap equation. Every smaller-cap base control then has bounded quadratic cost q, without an optimal-feedback assumption. Translation comparison and the boundary barriers give a gradient bound independent of both parameters.

The unitary rotation was recalculated: the displayed Q is skew Hermitian, Q eta = b, and the real diffusion rotation needs P=-Real(Q). The source's asserted vanishing mixed trace is not needed: its actual absolute value is bounded by C|xi| and the resulting extra drift is absorbed by the stated Young inequality in the same first-quasiderivative barrier. The candidate retains that correction. The checked source estimates are the covariance-only finite-time lemmas, Lemma 7.4 and the terminal barrier comparison in the specified arXiv text, rather than a claim of a published obstacle theorem.

Ito's formula for psi*Z^2 gives the additional occupation bound. With the cancellation of the boundary w^2 terms, BDG gives the direct second-quasiderivative estimate without multiplying an uncontrolled random exit time by a supremum. The compensated discount c(s)=c/theta(s) stays admissible under the larger cap and fixes the killing clock exactly. Differentiating p/theta gives 8r^2-2*rhat-4rZ, with every penalty term accounted for. Terms multiplied by c are controlled by integral c*exp(-phi)<=1; the remaining terms use bounded q and the occupation estimates.

The common localized stopping time is shared by all three second differences, so its indicator is not differentiated. For each fixed approximant, the higher-moment source estimate and exit-time comparison remove localization before delta, K and nu vary. At the boundary, tangent second derivatives include the second fundamental form term and are controlled by the uniform gradient estimate; the barrier denominator kills the possibly large normal Hessian of that fixed approximant. This order of limits yields a uniform lower bound for every real Hessian direction. The nonpositive trace then gives all upper bounds as well.

The limit is m-subharmonic by distributional passage for every covariance, lies below h by the penalty estimate and takes the boundary data. The strict competitor w-epsilon+t*rho has the right viscosity sign at a hypothetical positive maximum above the approximant: there the penalty is zero, contradicting strict covariance positivity. Thus the limit is exactly the envelope. The result proves real, rather than only complex, C^(1,1) in every stated order.

The original question and its erratum were added to the standalone citations. The Zhou theorem/lemma locators are pinned to inspected arXiv revisions; published-body parity of those calculations is not asserted. Krylov's fixed-parameter existence result is explicitly cited as quoted by Zhou, rather than represented as a directly inspected book theorem. No unresolved mathematical step was identified within the stated strict defining-function class.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/1302.7062v2)
- [Primary source 2](https://arxiv.org/html/1311.6450v1)
- [Primary source 3](https://www.numdam.org/item/10.5802/jep.133.pdf)
- [Primary source 4](https://www.numdam.org/item/10.5802/jep.157.pdf)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 322569dae991b9c92b55c181d27c236b158b91a2e51041ae66e9862bfdea82ce. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
