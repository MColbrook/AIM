# AIM 708: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Partially resolved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/708-the-critical-opening-for-asymptotic-borel-surjectivity.md) · [Manuscript](../../solutions/708-the-critical-opening-for-asymptotic-borel-surjectivity/main.pdf) · [Source and provenance](../../solutions/708-the-critical-opening-for-asymptotic-borel-surjectivity/README.md).

## Verdict and exact scope

Both uniform critical endpoints are excluded for every strongly regular sequence.

The nonuniform critical endpoint inclusion remains unresolved here.

## Independent checks

The assumed uniform endpoint surjectivity supplies a bounded function formally equal to z. Dividing by z makes a bounded coefficient-preserving cutoff with inverse-power decay. Moderate growth controls the shifted remainder sequence. Multiplication by this cutoff preserves all coefficients while ensuring integrable ray tails.

The inverse-Borel contour changes opening by exactly s on the logarithm surface. The reciprocal-gamma Hankel formula has the displayed normalization. The order-N radius gives the divided sequence M_N/Gamma(1+sN), uniformly up to angular edges. The separate constant-term integration-by-parts bound supplies the global order-zero estimate without a reciprocal angular cosine. Gamma-quotient comparison and the increasing lower envelope produce an exponentially equivalent log-convex sequence with moderate growth, strong nonquasianalyticity and index gamma(M)-s.

Taking the remaining opening rational contradicts the primary rational-opening criterion. Theorem 4.17 and Corollaries 4.18--4.19 were checked in arXiv:1805.01153v1. Thus both uniform endpoints are excluded; nonuniform endpoint surjectivity is not established, so the combined catalogue target remains partial.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/1805.01153v1)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 68d7559f28bd7d7b53948d10c3100d5986228da66e21b92029ac8ff9891651b9. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
