# AIM 690: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/690-a-smirnov-function-without-a-hilbert-domain-holomorphic-extension.md) · [Manuscript](../../solutions/690-a-smirnov-function-without-a-hilbert-domain-holomorphic/main.pdf) · [Source and provenance](../../solutions/690-a-smirnov-function-without-a-hilbert-domain-holomorphic/README.md).

## Verdict and exact scope

Every stated Smirnov function extends holomorphically to the Hilbert polydisc; no proposed nonextendible example exists.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The coordinate automorphism has the stated Poisson pushforward density. The correlated weight exp(-2|S_z|) is invariant under common circle rotation, so averaging analytic discs still gives a Jensen measure. Its pushforward density is bounded using the elementary logarithm inequality, orthogonality, and Jensen's lower bound on Z_z. The constant depends on the ell-2 norm and the uniform coordinate margin, not on dimension.

The logarithmic polynomial Cauchy estimate gives uniform convergence on every fixed Hilbert norm-and-margin set. These contain neighborhoods of every Hilbert-polydisc point, so the limit is Frechet holomorphic and agrees with the canonical representative. For the full radial class, weighted dilation maps ell-2 boundedly into ell-1 and its image closed polydisc is compact. Local bounds, Cauchy line estimates, and density of finite-support points give the limit without applying a finite-dimensional Montel theorem to an infinite-dimensional ball. The non-ell-2 linear examples prove sharp failure of continuous evaluation.

This is a negative answer to the existence of a nonextendible Smirnov function, with the stated stronger radial-class result. Lemma 2.24, Theorem 2.27 and the radial definition were checked in Guo--Ni--Zhou arXiv v2. That inspected version is now pinned explicitly in the bibliography, avoiding ambiguous locators between versions.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/2201.01993v2)
- [Primary source 2](https://doi.org/10.5802/aif.3696)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: ff56ca14cb786e1a38dec47b9fb9e3c27da5f93ed5d89d8b302d746b5003eb2b. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
