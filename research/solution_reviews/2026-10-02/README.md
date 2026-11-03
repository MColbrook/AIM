# Independent solution review, 2026-10-02

Twelve pull requests open at the start of the review supplied thirteen complete solution arguments. Only these open requests were processed. Their commits and full proof packages are preserved. Each target received a separate statement comparison and mathematical audit by Codex (AI) in this maintenance session, distinct from the originating preparation runs.

All thirteen recorded targets are marked **Solved**, using the documented-independent-audit convention. This is AI review; it does not assert human peer review, proof-assistant verification, journal acceptance or novelty priority. Solved includes counterexamples to universal statements.

Original IDs refer to revision aa776a01d7d48a79f93251af11fde9454b0aea95. At this checkpoint the active collection had 652 consecutive entries, and the retired records have IDs 653–665. [The complete mapping](id-mapping.json) preserves all 665 identities. Submitted files retain their original IDs, pinned links and pending-review wording.

| Original ID | Archive ID | PR | Conclusion | Mathematical audit |
| --- | --- | --- | --- | --- |
| 024 | 653 | [#11](https://github.com/MColbrook/AIM/pull/11) | Counterexample | [Exponential interior decay for smooth Steklov domains](024-review.md) |
| 218 | 654 | [#14](https://github.com/MColbrook/AIM/pull/14) | Affirmative proof | [Bounded harmonic lifting for complex media](218-review.md) |
| 405 | 655 | [#1](https://github.com/MColbrook/AIM/pull/1) | Counterexample | [Logarithmic convexity for subdiffusion with non-gradient drift](../../../cut_problems/research/solution_reviews/2026-10-02/405-review.md) |
| 435 | 656 | [#15](https://github.com/MColbrook/AIM/pull/15) | Counterexample | [Poisson kernel bounds for elliptic boundary diffusion on Lipschitz domains](435-review.md) |
| 457 | 657 | [#10](https://github.com/MColbrook/AIM/pull/10) | Affirmative proof | [Finite-density time sampling of an infinite observation window](457-review.md) |
| 471 | 658 | [#5](https://github.com/MColbrook/AIM/pull/5) | Counterexample | [Does directional ellipticity force a fractional energy bound?](471-review.md) |
| 488 | 659 | [#6](https://github.com/MColbrook/AIM/pull/6) | Affirmative proof | [Full-space minimizers for subcritical fourth-order aggregation energy](../../../cut_problems/research/solution_reviews/2026-10-02/488-review.md) |
| 506 | 660 | [#13](https://github.com/MColbrook/AIM/pull/13) | Counterexample | [Small-ball ratios for general symmetric product priors](506-review.md) |
| 514 | 661 | [#2](https://github.com/MColbrook/AIM/pull/2) | Counterexample | [Path connectivity of the infinity Z-Gromov–Wasserstein space](../../../cut_problems/research/solution_reviews/2026-10-02/514-review.md) |
| 558 | 662 | [#10](https://github.com/MColbrook/AIM/pull/10) | Counterexample | [Variance ordering for Gaussian alpha-divergence approximations](558-review.md) |
| 560 | 663 | [#12](https://github.com/MColbrook/AIM/pull/12) | Affirmative proof | [Monotone variance in the Gaussian approximation to DrMMD flow](../../../cut_problems/research/solution_reviews/2026-10-02/560-review.md) |
| 593 | 664 | [#8](https://github.com/MColbrook/AIM/pull/8) | Affirmative proof | [Logarithmic controlled bandwidth for locally analytic functions](../../../cut_problems/research/solution_reviews/2026-10-02/593-review.md) |
| 618 | 665 | [#4](https://github.com/MColbrook/AIM/pull/4) | Affirmative proof | [Smooth-gradient approximation of finite-Fisher-information scores](618-review.md) |

## Reproduced supporting checks

All 67 submitted file hashes matched their committed original bytes. All nine supporting runs exited successfully. The [reproduction record](reproduction.json) gives Python/library versions, commands and individual logs.

- Original 558: exact rational certificate, symbolic identities and 90-digit stationarity check.
- Original 506: 31 exact checks, 80 numerical checks including 25 independent convolutions, and 21 numerical-guard cases.
- Original 560: 2,237 exact checks and seven rigorous series enclosures; 12 direct-kernel comparisons, six high-precision endpoint comparisons and 363,810 finite-prefix signs; the numerical-guard test suite.
- Original 024: order-256, 8,192-sample Galerkin calculation as a finite-dimensional supplement only.

Run [reproduce.py](reproduce.py) with its documented dependencies to recreate the logs without rewriting the source packages. The computations do not certify the universal analytic statements. The mathematical audit is in each review above.

## Catalogue preservation

The [catalogue preservation check](catalogue-preservation.json) compared all 665 identities against the pinned baseline, including statements, applications, references, publication batches and programme histories. Archive pages retain their statements, applications, references and previous status reviews. Current IDs, status, dated review and navigation were updated. Surviving active entries retain their statements, statuses and review dates. Publication-batch membership follows each identity through renumbering.

Historical research checkpoints retain historical IDs; use the mapping to interpret them. The research queue was synchronized administratively with programme statuses and discovery dates preserved. Solved entries are ineligible. Campaign 001 and its attempt/review counters were not advanced.

## Subsequent Robin gap submission

[PR #16](https://github.com/MColbrook/AIM/pull/16) supplied a separate counterexample for original 021 at revision 37a2536. The [complete AI audit](021-review.md) and [subsequent identity mapping](021-id-mapping.json) record its classification as Solved, now archive 652. The current collection has 651 active and 14 retained solved entries. The earlier mapping and checks above remain historical records of the thirteen-request batch.
