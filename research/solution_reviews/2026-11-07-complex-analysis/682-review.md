# AIM 682: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Partially resolved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/682-real-rootedness-of-real-powers-of-binomial-coefficients.md) · [Manuscript](../../solutions/682-real-rootedness-of-real-powers-of-binomial-coefficients/main.pdf) · [Source and provenance](../../solutions/682-real-rootedness-of-real-powers-of-binomial-coefficients/README.md).

## Verdict and exact scope

The Le Roy equivalence and all degrees at most five are proved.

Arbitrary noninteger exponents at least two in degrees six and above remain unresolved here.

## Independent checks

The scaled binomial polynomials converge locally uniformly to the Le Roy function by the coefficient domination (k!)^(-gamma). Its order is 1/gamma<1, so a negative-real-zero assertion implies a genus-zero product. Conversely, Polya--Schur supplies the multiplier (k!)^(1-gamma). Multiplication, reversal, and multiplication again give exactly (n!)^(1-gamma) times B_(n,gamma); no factorial has been omitted.

The reciprocal substitutions in degrees four and five give the displayed discriminants. The stated ratio bounds imply both real y-roots are at most -2, so their corresponding x-roots are negative. Degrees one through three check directly. These finite-degree statements and the equivalence do not settle the entire-function question at arbitrary noninteger gamma. The primary 2026 Remark 4.8 was checked and added to the standalone references, together with the multiplier characterization used in the reduction.

## Primary references and limits

- [Primary source 1](https://link.springer.com/article/10.1007/s00365-026-09775-2)
- [Primary source 2](https://arxiv.org/html/1505.00355v2)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 908c5d626e5c268e255c8e4208f81ecdc78c330f36812ff1f8d7aab224793650. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
