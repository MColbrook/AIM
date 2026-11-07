# AIM 707: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/707-smooth-chernricci-collapse-on-non-kahler-elliptic-bundles.md) · [Manuscript](../../solutions/707-smooth-chernricci-collapse-on-non-kahler-elliptic-bundles/main.pdf) · [Source and provenance](../../solutions/707-smooth-chernricci-collapse-on-non-kahler-elliptic-bundles/README.md).

## Verdict and exact scope

Counterexample to bounded normalized full Chern curvature, despite smooth normalized convergence.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The canonical-line-bundle quotient is a compact holomorphic bundle with a fixed elliptic fiber. The real Gysin sequence gives odd first Betti number 2g+1, proving the required non-Kahler property. The phase q descends because rho changes by 2*pi. The structure equations make the mixed metric terms separately partial or bar-partial closed; the remaining term has partial-bar-partial proportional to the square of the base form, hence zero. Thus the displayed positive metric is Gauduchon.

In holomorphic coordinates its determinant is exactly (t+1)g. Its Chern--Ricci form is minus the base metric, so the displayed family solves the full flow globally and gives smooth normalized convergence directly. Multiplying the curvature matrices gives R(Z,bar Z,W,bar Z)=-B_(z bar z)=bar q*a; the inverse-metric terms cancel in W=partial_w-B partial_z. Constant rescaling and four unit vectors give t|a|/sqrt((t+1)g), which diverges wherever the chosen holomorphic one-form is nonzero.

This is a complete counterexample to the bounded-full-Chern-curvature conclusion, and hence to the conjunction. It is consistent with smooth convergence and lies outside the known special partial-bar-partial class. Conjecture 4.2 and its curvature convention were checked in the primary survey; the journal series and DOI were completed.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/2107.12928v3)
- [Primary source 2](https://doi.org/10.4171/RLM/965)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 4cb233843a9f02c58a2f823932e696d1b8d0ed9cadb86a44f8e7e48273851420. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
