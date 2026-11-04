# AIM 496: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/496-semilinear-galerkin-global-uniqueness.md); [snapshot](../../solutions/496-galerkin-uniqueness-partial/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/496-galerkin-uniqueness-partial/main.pdf), [LaTeX](../../solutions/496-galerkin-uniqueness-partial/main.tex), [target comparison](../../solutions/496-galerkin-uniqueness-partial/TARGET_COMPARISON.md).

**Decision:** Partial progress; catalogue status **Partially resolved**. Full planar global uniqueness; three-dimensional bounded-branch exclusion and positive separable reactions. General three-dimensional uniqueness remains open.

## Mathematical checks

The entire manuscript was reviewed, including both three-dimensional restrictions. Superlevel comparison uses absolute continuity of the drift Lp norm on shrinking level sets, including p=3 in dimension three. The fixed-operator Garding estimate gives a nonzero L2 limit for normalized approximate kernels.

In two dimensions, bounded energy gives finitely many triangles with nodal oscillation above fixed eta. Logarithmic capacity cutoffs remove them with vanishing H1 cost. On the remaining triangles the interpolated truncated test has the sign needed to discard arbitrary nonnegative potentials without an acute-mesh assumption. The product-interpolation defect, scalar energy-measure limit, non-atomic truncation levels and compact drift limit were checked. Continuous comparison contradicts the normalized kernel. Secant potentials of any two fixed-mesh roots are nonnegative L2 functions, giving all-root uniqueness.

Fixed-potential convex recovery and compact lower-order/skew terms justify strong convergence of bounded root sequences. The nodal small-perturbation cutoff excludes energy-bounded extra roots in both dimensions. The separable-reaction result uses a scalar convex-potential epi-limit and Mosco recovery respecting its finite domain; strict positivity of c almost everywhere is retained. Casas--Mateos--Rosch's primary Theorem 3.7 was checked as the source of the bounded branch. No blocking defect was found in the restricted results. The missing three-dimensional capacity/uniform-bound argument for arbitrary reactions is not supplied.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/496-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
