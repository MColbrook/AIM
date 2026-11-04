# AIM 523: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/523-can-adaptive-monte-carlo-approximate-a-noncompact-operator.md); [snapshot](../../solutions/523-adaptive-monte-carlo-error-floor/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/523-adaptive-monte-carlo-error-floor/main.pdf), [LaTeX](../../solutions/523-adaptive-monte-carlo-error-floor/main.tex), [target comparison](../../solutions/523-adaptive-monte-carlo-error-floor/TARGET_COMPARISON.md).

**Decision:** Full resolution; catalogue status **Solved**. Exact error 1/2 at every finite positive expected budget for the noncompact inclusion.

## Mathematical checks

The finite-information tightness lemma was checked by induction, including degenerate first queries. Gaussian regression gives a full-support conditional measure on the query kernel. Finite bins for the bounded first answers and L1 translation continuity control the shifted conditional weights. The countable supremum is measurable because the actual integer-valued output is Borel; measurable query-selection rules are not assumed.

Conditioned full-support Gaussian noise in ell1 and shifts r e_j stay uniformly inside the open unit ball. Small sup-norm error forces the first sufficiently large output coordinate to identify an arbitrarily large index, contradicting uniform tightness. Averaging over seeds is legitimate for the countable shifted experiments. Separability of the input image supplies measurability of the error despite the nonseparable output space. Boundary and small-noise limits give the strict-budget lower bound 1/2. Truncation at k adds at most n/k to squared error and covers expected budgets. The sum-query constant-sequence upper bound was checked coordinatewise.

The additional c0 floor, compactness criterion and separable-target radius bound were also reviewed. The compact upper approximation uses finite covers and Hahn--Banach functionals and does not assume the approximation property. The primary sources distinguish the earlier nonadaptive result from this adaptive target. No blocking mathematical defect was found.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/523-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
