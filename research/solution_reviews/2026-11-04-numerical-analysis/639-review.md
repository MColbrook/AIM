# AIM 639: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/639-sharp-complexity-of-noisy-continuous-sensing-of-a-sobolev-ellipsoid.md); [snapshot](../../solutions/639-noisy-continuous-sensing-partial/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/639-noisy-continuous-sensing-partial/main.pdf), [LaTeX](../../solutions/639-noisy-continuous-sensing-partial/main.tex), [target comparison](../../solutions/639-noisy-continuous-sensing-partial/TARGET_COMPARISON.md).

**Decision:** Partial progress; catalogue status **Partially resolved**. Uniform joint upper bound; two sharp regimes, with an unresolved intermediate transition.

## Mathematical checks

The colored-cover decoder was checked for adversarial history-dependent answers. At each branch the two forbidden compact sets are disjoint, so a continuous separator into [-1,1] exists. The sign decision cannot discard the true input. Within one color, compact pieces are separated; ceil(1/delta) levels have gap strictly greater than 2delta. Tietze extensions preserve continuous bounded queries. The target does not require continuity in the history.

The skeletal grid cover has m+1 colors, cell diameter at most 2/m, and same-color separation from successive skeleton thresholds. Counting grid vertices and incident faces inside the dilated ellipsoid gives N<=2^(10m). Integer query budgets, coordinate projection and the ellipsoid tail give error at most 4/m. Inversion with Z=L log2(1+2^n/L), its small-Z zero-output case and floor/ceiling margins give constant 256 uniformly.

The two matching regimes and the growing possible ratio around L~2^n/n were checked. Exact-measurement coloring, published noisy-information results and the retained AIM 553 antipodal transcript proof have distinct cited roles. An explicit citation to that last proof was added. No blocking defect was found in the upper bound; the full joint order remains unresolved.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/639-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
