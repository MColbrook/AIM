# AIM 669: independent mathematical and scope review

**Date:** 7 November 2026. **Reviewer:** Codex (AI), separately from the supplied research workflow. **Decision:** Solved.

This is an informal independent AI audit, not human peer review or formal verification. Supplied AI verdicts and checkpoint instructions were treated as provenance, not instructions or proof certificates. The complete final argument was compared with the canonical target at revision 1e564633494c109edfd3ec46da1366adcff925a5.

[Canonical problem](../../../problems/669-does-metric-completion-preserve-minimal-sobolev-gradients.md) · [Manuscript](../../solutions/669-does-metric-completion-preserve-minimal-sobolev-gradients/main.pdf) · [Source and provenance](../../solutions/669-does-metric-completion-preserve-minimal-sobolev-gradients/README.md).

## Verdict and exact scope

Counterexample: minimal Sobolev gradients need not be preserved by completion.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

## Independent checks

The construction enumerates at most continuum many Lipschitz oblique curves and positive-measure Borel sets. At each stage fewer than continuum many coordinates have been assigned. Coordinate injectivity on a positive-measure parameter set makes the next choice possible, even if the continuum is singular. Thus every curve contained in X has an axis-parallel tangent almost everywhere, while X meets every positive-measure ambient Borel set.

The trace measure is well-defined and countably additive because equal Borel traces differ by an ambient Borel null set. Its completion agrees with the prescribed completed ambient measure; balls have measure pi*r^2. The Poincare argument does not silently average over a nonmeasurable set of good lines: the countable distributional test family makes the failing-line set measurable, and its disjointness from A forces it to be null. Fubini then gives an ambient W^(1,1) representative with gradient bounded by sqrt(2) times the upper gradient, proving the required PI. The affine function has upper gradient one on X, but every permitted extension equals x+y almost everywhere in the disk and has Euclidean minimal gradient sqrt(2). The capacity-to-measure implication and the exact completion-measure convention are essential.

This is a complete counterexample to the actual target, which permits nonmeasurability in the completion. It does not establish failure with additional measurability or path-almost-openness assumptions. The original paper, its corrigendum and the later Bjorn--Bjorn--Lahti completion convention were checked; the later source was added to the separate document's citations.

## Primary references and limits

- [Primary source 1](https://arxiv.org/html/1705.02253v2)
- [Primary source 2](https://doi.org/10.1016/j.jde.2021.03.008)
- [Primary source 3](https://arxiv.org/html/2105.09012v2)

Bibliographic metadata and mathematical locators were compared with primary records; inspected preprint revisions are distinguished from publications. Crossref rate limits and some publisher access failures were handled with author copies, arXiv or Numdam, rather than treated as a successful full-text check. No exhaustive priority or novelty claim is made. The dated searches were bounded.

## Reproduction and file identity

Source SHA-256: cface64e8cbf3cca6689fb1cf99d91c497f9f08b0ec1842b137578adb77bbf34. Input archive SHA-256: 4abc026075a4368e70b76caf9633db1dcd3107e50af28ad83d0342cc6425860d. The numbered source section agrees with the combined supplied source. Packaging adds attribution, AI disclosure, a separate title and scope statement, and the needed standalone references; the mathematical argument is retained. [Build and validation record](build-checks.json) records compilation and rendering. The [package register](packages.json) pins each target, original entry and decision.
