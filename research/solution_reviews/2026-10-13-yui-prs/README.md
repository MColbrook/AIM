# Individual solution-PR review, 13 October 2026

**Correction, 21 October 2026:** The AIM010 manuscript has been removed and replaced by a [note pointing to Mikael Sundqvist's existing solution](../../solutions/010-mercedes-disk-partition/README.md), arXiv:2609.21964, submitted 18 September 2026. Its earlier acceptance recommendation and AI audit are superseded; the batch account below records the original processing.

Forty original open submissions from Kaiwen Jin (`yuiyuiui`) were reviewed individually at immutable heads and merged separately. Each complete argument was reconstructed against its original AIM target, with references, ancillary materials, supplied integrity records and all manuscript pages checked. The reviews are independent AI audits during maintainer processing, separate from the submission's drafting/self-review; no human peer review or Lean verification is claimed.

All forty original submissions meet the repository's documented-independent-audit criterion for **Solved**. No substantive uncorrected proof gap or omitted original target clause was found. Counterexamples resolve universal questions even when narrower related questions remain. Finite numerical checks are distinguished from proof-critical exact certificates and from analytic coverage of infinite parameter ranges. Original problem pages, IDs, statements, applications and references are retained.

The dataset preserves [individual decisions](decisions.json), [original statuses](previous-statuses.json), [actual merge receipts](merged-prs.json), [pinned package hashes](package-audit.json), [source rebuild outcomes](rebuild-results.json), [extra manifest checks](manifest-extra-qa.json), [structural report checks](review-record-structural-qa.json), and [independent reproduction results](reproduction-checks.json). The detailed per-problem reports explain exact target scope, novel proof steps and source applicability.

## Independently checked corrections

- AIM576: canonical-measure equation locators corrected from1.15-1.16 to1.23-1.24 in source and target comparison.
- AIM258: the auxiliary flatness lemma is restricted to1<sigma<2, exactly the range used by the main construction and the cited coefficient theorem.
- AIM615: the finite-block absorption paragraph distinguishes the valid2^-M two-player bound from the6^-M prescribed three-player transfer path. This is a scope clarification, not a demonstrated false bound.

All three saved source documents passed the built-in compiler, their exported PDFs were regenerated and every page inspected. Package Markdown was adapted to the repo's existing math convention, with no mathematical change. LF checkout attributes keep text hashes identical on Windows and Linux. Original pinned package integrity and subsequent maintainer updates are recorded separately.

## Original submissions

| PR | AIM | Decision | Proof | Review |
| --- | --- | --- | --- | --- |
| [#60](https://github.com/MColbrook/AIM/pull/60) | 010 | Superseded; existing solution cited | [arXiv](https://arxiv.org/abs/2609.21964) | [Correction](010-review.md) |
| [#71](https://github.com/MColbrook/AIM/pull/71) | 051 | Solved | [PDF](../../../research/solutions/051-potential-on-general-manifold/paper/main.pdf) | [Audit](051-review.md) |
| [#66](https://github.com/MColbrook/AIM/pull/66) | 063 | Solved | [PDF](../../../research/solutions/063-geodesic-scattering/paper/geodesic_scattering.pdf) | [Audit](063-review.md) |
| [#45](https://github.com/MColbrook/AIM/pull/45) | 067 | Solved | [PDF](../../../cut_problems/research/solutions/067-burgers-shock-uniform-control-time/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/067-review.md) |
| [#48](https://github.com/MColbrook/AIM/pull/48) | 138 | Solved | [PDF](../../../cut_problems/research/solutions/138-unique-minimum-time-positive-heat-control/paper/manuscript.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/138-review.md) |
| [#49](https://github.com/MColbrook/AIM/pull/49) | 139 | Solved | [PDF](../../../research/solutions/139-sharp-heat-tracking-range/paper/heat_tracking.pdf) | [Audit](139-review.md) |
| [#51](https://github.com/MColbrook/AIM/pull/51) | 258 | Solved | [PDF](../../../research/solutions/258-signed-stefan-control/stefan_signed_control.pdf) | [Audit](258-review.md) |
| [#67](https://github.com/MColbrook/AIM/pull/67) | 300 | Solved | [PDF](../../../cut_problems/research/solutions/300-carrying-simplex-interior/paper/interior_smoothness.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/300-review.md) |
| [#53](https://github.com/MColbrook/AIM/pull/53) | 385 | Solved | [PDF](../../../cut_problems/research/solutions/385-equal-speed-wentzell-wave-observability/paper/equal_speed_observability.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/385-review.md) |
| [#54](https://github.com/MColbrook/AIM/pull/54) | 386 | Solved | [PDF](../../../cut_problems/research/solutions/386-slow-surface-schrodinger-observability/paper/exterior_observability.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/386-review.md) |
| [#52](https://github.com/MColbrook/AIM/pull/52) | 387 | Solved | [PDF](../../../cut_problems/research/solutions/387-shallow-water-tank-obstruction/paper/obstruction.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/387-review.md) |
| [#56](https://github.com/MColbrook/AIM/pull/56) | 398 | Solved | [PDF](../../../cut_problems/research/solutions/398-parabolic-obstacle-counterexample/paper/obstacle_control_counterexample.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/398-review.md) |
| [#58](https://github.com/MColbrook/AIM/pull/58) | 415 | Solved | [PDF](../../../research/solutions/415-nongradient-neumann-uniform-control/paper/main.pdf) | [Audit](415-review.md) |
| [#57](https://github.com/MColbrook/AIM/pull/57) | 417 | Solved | [PDF](../../../research/solutions/417-polynomial-reachable-growth-counterexample/paper/main.pdf) | [Audit](417-review.md) |
| [#64](https://github.com/MColbrook/AIM/pull/64) | 431 | Solved | [PDF](../../../research/solutions/431-dtn-analyticity-continuous-boundary/paper/dtn_analyticity.pdf) | [Audit](431-review.md) |
| [#70](https://github.com/MColbrook/AIM/pull/70) | 434 | Solved | [PDF](../../../research/solutions/434-p-harmonic-second-sobolev-derivatives/paper/main.pdf) | [Audit](434-review.md) |
| [#69](https://github.com/MColbrook/AIM/pull/69) | 451 | Solved | [PDF](../../../research/solutions/451-mixed-sobolev-counterexample/paper/main.pdf) | [Audit](451-review.md) |
| [#85](https://github.com/MColbrook/AIM/pull/85) | 494 | Solved | [PDF](../../../research/solutions/494-degree-zero-interleaving-counterexample/paper/interleaving_counterexample.pdf) | [Audit](494-review.md) |
| [#72](https://github.com/MColbrook/AIM/pull/72) | 506 | Solved | [PDF](../../../research/solutions/yuiyuiui-506-private-density-mixed-anisotropy/paper/mixed_private_density.pdf) | [Audit](506-review.md) |
| [#74](https://github.com/MColbrook/AIM/pull/74) | 507 | Solved | [PDF](../../../research/solutions/507-sequential-private-spectral-density/paper/main.pdf) | [Audit](507-review.md) |
| [#73](https://github.com/MColbrook/AIM/pull/73) | 515 | Solved | [PDF](../../../research/solutions/515-gspo-counterexample/paper/counterexample.pdf) | [Audit](515-review.md) |
| [#75](https://github.com/MColbrook/AIM/pull/75) | 516 | Solved | [PDF](../../../cut_problems/research/solutions/kaiwen-jin-516/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/516-review.md) |
| [#39](https://github.com/MColbrook/AIM/pull/39) | 517 | Solved | [PDF](../../../research/solutions/kaiwen-jin-517/paper/main.pdf) | [Audit](517-review.md) |
| [#37](https://github.com/MColbrook/AIM/pull/37) | 518 | Solved | [PDF](../../../cut_problems/research/solutions/kaiwen-jin-518/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/518-review.md) |
| [#40](https://github.com/MColbrook/AIM/pull/40) | 519 | Solved | [PDF](../../../research/solutions/519-euclidean-mechanical-lie-algebra/paper/main.pdf) | [Audit](519-review.md) |
| [#86](https://github.com/MColbrook/AIM/pull/86) | 527 | Solved | [PDF](../../../cut_problems/research/solutions/kaiwen-jin-527-negative-jump-flow/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/527-review.md) |
| [#84](https://github.com/MColbrook/AIM/pull/84) | 554 | Solved | [PDF](../../../cut_problems/research/solutions/554-stieltjes-rational-asymptotic-constant/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/554-review.md) |
| [#46](https://github.com/MColbrook/AIM/pull/46) | 555 | Solved | [PDF](../../../research/solutions/555-nonadaptive-randomization-gain/paper/main.pdf) | [Audit](555-review.md) |
| [#83](https://github.com/MColbrook/AIM/pull/83) | 556 | Solved | [Resolution sources](../../../problems/556-smooth-integration-dimensional-curse.md) | [Audit](556-review.md) |
| [#77](https://github.com/MColbrook/AIM/pull/77) | 559 | Solved | [PDF](../../../research/solutions/559-univariate-trace-decidability/paper/trace_decidability.pdf) | [Audit](559-review.md) |
| [#76](https://github.com/MColbrook/AIM/pull/76) | 562 | Solved | [PDF](../../../research/solutions/kaiwen-jin-562-tensor-singular-values/paper/main.pdf) | [Audit](562-review.md) |
| [#88](https://github.com/MColbrook/AIM/pull/88) | 574 | Solved | [PDF](../../../research/solutions/574-trap-draws-percolation/paper/main.pdf) | [Audit](574-review.md) |
| [#78](https://github.com/MColbrook/AIM/pull/78) | 576 | Solved | [PDF](../../../research/solutions/576-ising-replica-covariance/paper/ising_replica_covariance.pdf) | [Audit](576-review.md) |
| [#87](https://github.com/MColbrook/AIM/pull/87) | 582 | Solved | [PDF](../../../research/solutions/582-accumulating-gaps/paper/main.pdf) | [Audit](582-review.md) |
| [#79](https://github.com/MColbrook/AIM/pull/79) | 583 | Solved | [PDF](../../../research/solutions/583-regular-tree-one-dependent-coloring/paper/main.pdf) | [Audit](583-review.md) |
| [#80](https://github.com/MColbrook/AIM/pull/80) | 584 | Solved | [PDF](../../../cut_problems/research/solutions/584-four-color-branched-ray/paper/main.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/584-review.md) |
| [#68](https://github.com/MColbrook/AIM/pull/68) | 597 | Solved | [PDF](../../../research/solutions/597-entropy-chain-rule-lipschitz/paper/manuscript.pdf) | [Audit](597-review.md) |
| [#81](https://github.com/MColbrook/AIM/pull/81) | 615 | Solved | [PDF](../../../cut_problems/research/solutions/615-gambler-scaling/paper/gambler_scaling.pdf) | [Audit](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/615-review.md) |
| [#38](https://github.com/MColbrook/AIM/pull/38) | 633 | Solved | [PDF](../../../research/solutions/633-kaiwen-jin-freudenthal-potentials/paper/main.pdf) | [Audit](633-review.md) |
| [#82](https://github.com/MColbrook/AIM/pull/82) | 636 | Solved | [PDF](../../../research/solutions/636-uniform-jack-normal/paper/jack_normal.pdf) | [Audit](636-review.md) |

## JohnDriscollAcademic PR35

[PR35](https://github.com/MColbrook/AIM/pull/35) was processed after the original batch and closed as already addressed by the existing AIM073 OpenAI source comparison. Its eight added lines and both links were checked against the actual published theorem. The linked public Lean comparator ends in `sorry`, so the page now expressly distinguishes a comparator statement from a verified proof. AIM073 retains its existing Solved status from the published manuscript and does not receive Lean status. [Detailed processing record](073-pr35-review.md).

## Additional PR89

The final live inventory found [PR89](https://github.com/MColbrook/AIM/pull/89), opened during processing. It was reviewed separately by two independent AI agents, rebuilt and byte-checked, then replied to and merged at its pinned head. AIM639 is **Solved** with [full review](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/639-review.md), [second check](../../../cut_problems/research/solution_reviews/2026-10-13-yui-prs/639-second-check.md) and [package evidence](pr89-package-qa.json). This brings the processed contributor batch to41 complete resolutions, with no unresolved substantive gaps. The combined decision and merge records include it.

**Attribution update incorporated 3 November 2026:** [The dated prior-art audit](../2026-10-21-yui-prior-art/README.md) supersedes the original attribution for AIM556, which cites Esra Sengelen Sevim's earlier published solution. Historical proof reviews remain dated records.
