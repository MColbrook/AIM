# Individual pull request reviews on 21 October 2026

This batch processes the five pull requests that remained open at the start of the review. Each was inspected at its pinned submitted revision. Reviews were performed by OpenAI Codex in independent contexts, with an additional coordinating review; they are AI mathematical reviews, without human peer review or Lean verification.

| PR | AIM | Disposition | Evidence |
| --- | --- | --- | --- |
| [172](https://github.com/MColbrook/AIM/pull/172) | 541 | Partial: degree-one failure and degree-three convergence; degree two remains open | [Complete cubic and cell-level audit](172-review.md), [independent linear interval audit](172-second-review.md), [PDF checks](172-artifact-check.json) |
| [173](https://github.com/MColbrook/AIM/pull/173) | 666 | New open problem, canonical Stiefel injectivity radius | [Admission, scope and literature review](173-new-problem-review.md) |
| [175](https://github.com/MColbrook/AIM/pull/175) | 458 | Solved for the exact finite smooth-noise no-slip local theory | [Complete argument review](175-review.md), [second channel-calculus audit](175-second-review.md) |
| [176](https://github.com/MColbrook/AIM/pull/176) | 571 | Solved: all 608 independent enumeration results match, covering 618 cells | [Acceptance and full replay](176-review.md), [proof audit](176-proof-review.md), [execution summary](571-independent-replay-summary.json) |
| [177](https://github.com/MColbrook/AIM/pull/177) | 482 | Attribution repaired; existing mathematical result unchanged | [Attribution and scope checks](177-attribution-review.md) |

## Attribution and scope

Each proposed mathematical contribution was compared with the original target and current primary literature. Earlier results, distinct schemes and weaker solution classes are identified in the individual reports. No earlier matching complete proof was located for the accepted new results. A 2024 cubic-convergence announcement is explicitly credited for AIM541, while distinguishing it from an available complete proof of the exact RMD scheme.

The new Stiefel problem is numbered 666 because 652–665 are already issued archived identities. It is registered under Imaging, control, geometry and dynamics. The catalogue now allows a new problem page after archived entries while continuing to reject gaps across all issued IDs. The numbering regression preserves the existing archive and problem pages.

The earlier partial assessment of AIM458 remains available as history. The revised channel right inverses were checked independently against the actual 2013 Kunstmann–Weis correction before its status was changed. AIM541 remains an open target under the Partial label because its quadratic case is unresolved.

## Verification

Package payloads, manifests and checksums were checked against the pinned submissions; maintainer decision notes have refreshed integrity bindings. Protected problem statements, applications and reference sections are preserved. Catalogue validation and its numbering regressions use an isolated candidate containing the tracked repository, excluding unrelated local work.

All 608 distinct complete Hilbert series for AIM571 were freshly recomputed, covering all 618 cell memberships, with zero cached results reused and zero failed systems. The exported independent bundle also passed the standalone checker after download. All complete rational functions, original gradings, four action sums, Burnside identity and polynomial identity match. The disclosed Normaliz implementation remains a trusted software dependency; this is not a second counting algorithm or formal verification.

The full catalogue regression suite passed all 60 tests ([log](catalogue-regression.log)); the original geometry/export suite passed 7 tests and the new replay/receipt suite passed 11 tests. Final catalogue generation and validation passed. The [machine-readable batch record](reviewed-pull-requests.json) pins every submitted revision and integration commit. No changes from `FURTHER_problems` or other chats' untracked solution folders are included.
