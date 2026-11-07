# AIM 673: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/673-cluster-values-on-the-complex-ell-p-ball.md) · [Manuscript](../../solutions/673-cluster-values-on-the-complex-ell-p-ball/main.pdf) · [Source and provenance](../../solutions/673-cluster-values-on-the-complex-ell-p-ball/README.md).

## Verdict and exact scope

Cluster-value equality at every interior point of the complex ell-p ball, for all 1<p<infinity.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The origin lemma uses the finite-coordinate polynomial ideal and inversion of an element bounded away from zero. The inverse is holomorphic and uniformly continuous, since the reciprocal is Lipschitz on that range. The ell-p dual tail tends to zero uniformly on a bounded tail ball, giving the requested weak neighborhood.

The exponential weight has its maximum at the exact head norm u, yielding r^k for a homogeneous tail polynomial. Applying this bound to the homogeneous pieces of Q^m and taking m-th roots gives the correct radius bound for arbitrary continuous polynomials, without assuming they depend on finitely many coordinates. Translating the tail character puts it in the zero fiber of the slightly enlarged tail ball. The preliminary norm bound tends to one; radial rescaling puts the final points inside the original ball, with polynomial errors uniform on the bounded sets used. One polynomial approximation is fixed before choosing the head size. Spectrum compactness supplies the reverse inclusion.

No withdrawn general Banach-space theorem is invoked. The proof covers every stated nonzero interior point and all 1<p<infinity. The original Question 8 source was added; the 2018 corrigendum and the established origin theorem remain separately cited.

## Primary references and limits

- [Primary source 1](https://riunet.upv.es/server/api/core/bitstreams/91e84467-fcf4-4ea8-b14c-24f0fc4daa0b/content)
- [Primary source 2](https://mate.dm.uba.ar/~slassall/clustervalues.pdf)
- [Primary source 3](https://doi.org/10.1016/j.aim.2018.03.019)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: 3dd4eb843e98c7047486f8d277354b3ec0d2dc5d4fe47e6c6abb0a56145bc1d8. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
