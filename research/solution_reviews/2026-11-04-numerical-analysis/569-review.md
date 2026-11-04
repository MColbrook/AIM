# AIM 569: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/569-does-discontinuous-information-help-randomized-approximation.md); [snapshot](../../solutions/569-discontinuous-randomized-information/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/569-discontinuous-randomized-information/main.pdf), [LaTeX](../../solutions/569-discontinuous-randomized-information/main.tex), [target comparison](../../solutions/569-discontinuous-randomized-information/TARGET_COMPARISON.md).

**Decision:** Full resolution; catalogue status **Solved**. Counterexample on the incomplete normed space (ell1, norm2): one algebraic query beats every finite continuous-information budget.

## Mathematical checks

The counterexample was checked against the normed-space target. The ell1 set is a Borel dense linear subspace of ell2. The fair-sign sum converges absolutely for every input and seed; finite partial sums are jointly Borel, as is their limit. The algebraic functional need not be continuous in the ell2 norm because its domain is incomplete.

For s=||x||_2^2 the squared-query average has variance at most 2s^2/n. With kappa=sqrt(2/(n+2)), a=kappa/(1+kappa) and b=1-kappa, the affine estimator has a convex quadratic risk in s on [0,1] with balanced endpoint values a^2. The one-query bound sqrt(6)-2 is strictly below 1/2.

Every continuous functional on this dense subspace extends to ell2. The weak-shift lemma's Gaussian regression preserves the required ell1 covariance ranges and regression vectors; its conditional measures give the input subspace full mass and residual shifts remain weakly null. L1 translation continuity handles varying first answers without measurability of selection rules. After clipping to [0,1], symmetric conditioned Gaussian noise and shifts r e_j give an expected target gap r^2 while the algorithm's expected difference vanishes. The boundary/noise limits give the RMS floor 1/2. Truncation covers expected budgets, and the constant output 1/2 supplies the upper bound. No blocking defect was found. A Banach-only variant is not resolved.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/569-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
