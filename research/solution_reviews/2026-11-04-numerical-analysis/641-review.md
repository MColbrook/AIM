# AIM 641: independent audit, 4 November 2026

**Reviewer:** Codex (AI), independently reviewing the submitted argument and dependencies. The submission's own audit claims were not treated as evidence. This is not human peer review or formal verification.

**Target:** [Pinned statement](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/641-bos-simplex-interpolation-nodes.md); [snapshot](../../solutions/641-quartic-simplex-certificates/statement.md).

**Submission:** Matthew J. Colbrook. The solutions were found by AI. [PDF](../../solutions/641-quartic-simplex-certificates/main.pdf), [LaTeX](../../solutions/641-quartic-simplex-certificates/main.tex), [target comparison](../../solutions/641-quartic-simplex-certificates/TARGET_COMPARISON.md).

**Decision:** Partial progress; catalogue status **Partially resolved**. Quartic tetrahedral Fejer property and all-dimensional fourth-power bound; quartic Fekete property in dimensions at least four remains open.

## Mathematical checks

The exact 35-by-35 cardinal check covers every dimension: nodes have support at most four, and a polynomial vanishes when a distinguished coordinate vanishes. The midpoint correction to the public 2022 preprint is explained and checked at the nodes; no parity with the final journal formulas is claimed.

For the planar base, concavity in e3 at fixed e1,e2 reduces to zero or repeated coordinates; both restrictions have exact positive factorizations. In four coordinates symmetry reduces to a sorted cone. The degree-raised remainder has 1536 positive coefficients, each at least 60. The verifier reconstructs the deficit from the cardinal formulas; its output JSON equals the supplied witness. Face restriction and division by the nonzero raising factor were checked.

For the fourth-power theorem, the stable power-sum derivation, derivative mA+B and coefficient recurrence were checked. All 1255 slope coefficients are nonnegative. The 28 positive Muirhead transfers have equal partition lengths, so their orbit normalization proves inequalities in every number of coordinates. The residual identity and signs are exact. Minimum-coordinate integration reduces to a face. The separately checked coefficients a_(23)=40 and r_(23)=160 give strictness for support at least five; square-sum Fejer, partition of unity and affine reproduction identify equality on smaller supports with the interpolation nodes.

All three distributed standard-library verifiers pass. These are exact computer-assisted proofs, not sampling or Lean verification. The cubic result is prior work. Hadamard gives quartic Fekete only through dimension three, so the higher-dimensional target remains open. No blocking defect was found in assertions 2 and 4.

## Sources and reproducibility

The [reference audit](references.md) records primary sources and corrections. All citations and cross-references resolve. The saved source compiles with PDFLaTeX and the desktop compiler; the publication PDF was visually inspected. See the [build log](verification/641-latex.txt) and package checksum manifest.

The snapshot SHA-256 matches both the archive provenance and canonical Git content at the pinned revision; working-copy CRLF encoding is accounted for. Packaging adds standalone definitions, authorship and disclosure, completes references, and removes combined-report references. Supplied certificates are unchanged. Numerical experiments are not used to certify infinite-dimensional or all-dimensional theorems.
