# AIM 691: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/691-finite-time-singularities-of-the-chernricci-flow.md) · [Manuscript](../../solutions/691-finite-time-singularities-of-the-chernricci-flow/main.pdf) · [Source and provenance](../../solutions/691-finite-time-singularities-of-the-chernricci-flow/README.md).

## Verdict and exact scope

Counterexample to the analyticity conclusion: the collapsing-subvariety locus is nonanalytic for an admissible Hermitian flow.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The product metric is smooth, positive and explicitly not Gauduchon, which is permitted in the target. The maximal-time criterion gives existence for t<1/2 by a potential correction; integration over a minimum-area projective fiber gives the matching upper bound. Product symmetry rules out mixed components and reduces the flow to the displayed scalar potential equation.

The constant sub- and supersolutions bound the potential uniformly. The integration-by-parts volume identity gives the lower bound 2*pi*(50-pi), with D a=pi^2*cos(2*pi*u) and integral |D a|=2*pi. Thus the whole surface does not collapse. Fibers collapse exactly above the specified real circle; every nonfiber irreducible curve has a positive-degree projection to the elliptic base and volume at least 100. This also handles singular curves via normalization. These exhaust the positive-dimensional subvarieties of a connected complex surface.

Pulling the resulting locus back by a holomorphic section gives an infinite proper real circle in a Riemann surface, which cannot be analytic. This refutes the catalogue's conjunction. It does not separately establish or refute equality of the two loci. The maximal-time theorem and the unrestricted-Hermitian formulation were checked against the primary Chern--Ricci sources; the survey citation was completed with its journal series and DOI.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/1201.0312v3)
- [Primary source 2](https://arxiv.org/html/2107.12928v3)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 84b123ae545faca4800634e105d687435d029f952614844d4ad82e280f776053. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
