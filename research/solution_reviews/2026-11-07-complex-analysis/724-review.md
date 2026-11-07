# AIM 724: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/724-is-polynomial-local-mass-almost-necessary-for-regular-orthogonal-polynomials.md) · [Manuscript](../../solutions/724-is-polynomial-local-mass-almost-necessary-for-regular/main.pdf) · [Source and provenance](../../solutions/724-is-polynomial-local-mass-almost-necessary-for-regular/README.md).

## Verdict and exact scope

The required capacity limit holds for every fixed exponent greater than two, with ambient ball centers.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

Orthonormalizing the Vandermonde determinant gives exactly Z_n=n!*product(kappa_j^(-2)). Regularity and transfinite diameter give the same n^2 logarithmic scale. Ambient two-dimensional packing bounds the measure of low-mass support centers by C*r^(L-2).

Taking n asymptotic to log(1/r)/epsilon makes configurations with a positive fraction of bad centers exponentially negligible relative to Z_n, for fixed positive delta and epsilon. A separate suboptimal-energy cutoff then supplies a high-energy configuration with few bad points. After diameter normalization all pair logarithmic energies are nonnegative, so deleting bad points has the required direction. The circle mean identity bounds every cross energy by the center energy, including overlapping circles; self-energies contribute log(2/r)/N. These circles are contained in the good ambient-center set at radius 2r.

The resulting probability measure supplies the capacity lower bound. Taking the liminf before sending eta, delta and epsilon to zero gives the correct order of limits, and compact support-neighborhood capacity gives the upper bound. Scaling back uses an intermediate exponent between two and the requested exponent to absorb mass and length constants. This proves the stronger fixed-exponent statement only for ambient centers, exactly as in the target; support-restricted centers are not asserted. The Bloom primary Vandermonde asymptotics and Stahl--Totik normalization were checked.

## Primary references and limits

- [Primary source 1](https://emis.de/ft/41335)
- [Primary source 2](https://doi.org/10.1017/CBO9780511759420)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: c00771f1cb9f3ce4310bed9e69d6c3ee48423b082126b9cd0590090e681930bb. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
