# AIM 568: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/568-a-linear-information-bound-for-arbitrary-convex-model-classes.md); [snapshot](../../solutions/568-convex-information-measurability/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/568-convex-information-measurability/main.pdf), [LaTeX](../../solutions/568-convex-information-measurability/main.tex), [target comparison](../../solutions/568-convex-information-measurability/TARGET_COMPARISON.md).

**Decision:** Full resolution; catalogue status **Solved**. The 27n comparison holds with scalar-error measurability, already at deterministic budget 2n-1.

## Mathematical checks

The measurable-majorant lemma was checked in full. Lusin is applied to the original finite-history laws; coordinatewise Tietze extensions preserve their selected compact parts. A union bound controls altered histories. Uniform polynomial approximation on compact neighborhoods of reachable histories gives a countable family of rational policies dense in mean loss. Euclidean projection bounds the loss without increasing distance to the target.

The corresponding value is Borel as a function of the input probability law. Disintegrating the fixed first query and inducting on frozen fibers bounds the integral of the Borel majorant. The least almost-optimal member of the countable policy family is a Borel choice. The argument integrates the simulator and majorant, never the original unmeasurable decisions or output. A frozen continuation extends off its fiber arbitrarily, since the conditional law is supported on the fiber.

The 2026 primary preprint's determinant convention, rank convention, Lemma 2.2, fixed uniform-simplex average bound (1.4), and Theorem 1.1 match the quantities and constants used here. The simplex and contraction are chosen independently of the algorithm and seed. The finite-dimensional restriction of p_F is equivalent to a Euclidean norm, so the stipulated joint scalar-error measurability supports Tonelli. The zero-determinant affine-span case and budget 2n-1 were checked. No blocking defect was found in the full target argument.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/568-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
