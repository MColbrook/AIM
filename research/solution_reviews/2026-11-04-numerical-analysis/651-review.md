# AIM 651: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/651-simple-crdt-convergence.md); [snapshot](../../solutions/651-crdt-quadrilaterals-partial/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/651-crdt-quadrilaterals-partial/main.pdf), [LaTeX](../../solutions/651-crdt-quadrilaterals-partial/main.tex), [target comparison](../../solutions/651-crdt-quadrilaterals-partial/TARGET_COMPARISON.md).

**Decision:** Partial progress; catalogue status **Partially resolved**. Global convergence for four-prevertex quadrilaterals; prescribed subdivisions with more vertices and general polygons remain open.

## Mathematical checks

The four side-length formulas were derived from the Schwarz--Christoffel integrals at 0,t,1,infinity. Positive beta parameters keep every length finite and nonzero for t in (0,1), making the scalar log absolute cross ratio well defined. Differentiating gives the stated g' formula. Cyclic relabelling changes both coordinates by the same sign; reflection exchanges the appropriate angles, preserving the derivative bounds.

For convex angles, Euler-integral logarithmic derivative bounds give 0<g'<1. With one reflex or straight angle the upper bound follows by discarding its negative term. Euler transformation cancels the adverse scalar term for the lower bound. The paired expectations are strictly ordered: both the ratio of the positive beta densities and u/(1-tu) are increasing, giving a strictly positive covariance. Straight-angle cases and positivity of all parameters were checked.

The scalar update stays between the current and true parameters and contracts geometrically on their compact interval. The primary paper's equation (7) and subdivision rules were checked; Bishop's initialization bound is not used as a convergence theorem. The rectangle, parallelogram and explicit concave examples satisfy sufficient no-subdivision conditions. An original quadrilateral with more subdivision prevertices is outside this result. No blocking defect was found in the scalar theorem; general polygons remain open.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/651-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
