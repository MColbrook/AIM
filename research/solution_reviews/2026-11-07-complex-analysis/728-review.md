# AIM 728: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/728-do-continuous-polynomial-roots-have-weak-endpoint-derivative-regularity.md) · [Manuscript](../../solutions/728-do-continuous-polynomial-roots-have-weak-endpoint-derivative/main.pdf) · [Source and provenance](../../solutions/728-do-continuous-polynomial-roots-have-weak-endpoint-derivative/README.md).

## Verdict and exact scope

The weak endpoint derivative estimate holds for every continuous polynomial root, with an explicit coefficient bound.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The established complex-radical estimate is used at its weak exponent, and the full degree-n theorem only for absolute continuity. All strong exponents above the degree-n endpoint are applied after splitting, to strictly lower-degree factors. Tschirnhausen weighted homogeneity, bounded endpoint extension and the interpolation lemma give normalized coefficient bounds even when the original coefficient scale is below one.

The stopping interval equation has a unique solution before reaching the extension boundary, because h>=2A_0. Radical variation bounds keep the fixed-amplitude coefficient path within one uniform factorization chart. The compact normalized coefficient set avoids z^n, so coprime factors exist locally; a finite nested cover supplies a common chart margin and derivative bounds. A continuous root cannot switch between coprime factors. The rescaled truncated interval has length at least one half, so the known lower-degree strong estimate has uniform constants.

For the global endpoint, the 5r lemma gives disjoint cores whose fivefold enlargements cover the nonzero set. The average of h over each enlargement is bounded by the uncentered maximal function at every point of its core. Chebyshev therefore bounds the whole distribution function by an integral of min(1,C*(Mh/u)^q). Layer cake converges because q>p; weak-(p,p) boundedness of the maximal operator for p>1 closes the estimate. No local weak quasinorms are summed and no overlap bound for enlarged intervals is assumed. Absolute continuity handles the common-zero set.

Rescaling produces |I|^(-1/n), with the stated weighted coefficient norm. The test z^n-t still excludes the strong endpoint, consistently. The primary Parusinski--Rainer Proposition 1, Corollary 2, Theorem 1 and Open Problem 2 were checked, together with the Ghisi--Gobbino background reference. The complete endpoint argument was not inferred from separate subcritical estimates.

## Primary references and limits

- [Primary source 1](https://math.univ-cotedazur.fr/~parus/publis/ens.pdf)
- [Primary source 2](https://www.numdam.org/item/ASNSP_2013_5_12_4_1001_0.pdf)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 80ea54aa9df097618cfe351c1296295fc1c95f0cc022d92b3b50c22489680ee1. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
