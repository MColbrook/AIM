# AIM 049 — weighted p-Calderón resolution: source and scope check

- **Date:** 6 November 2026.
- **Problem:** [049 — Global conductivity uniqueness for the p-Laplacian in higher dimensions](../../problems/049-nonlinear-p-calderon.md).
- **Repository statement reviewed:** [main at 4f5b1659355cb61d194da94ef14615214e1363a8](https://github.com/MColbrook/AIM/blob/4f5b1659355cb61d194da94ef14615214e1363a8/problems/049-nonlinear-p-calderon.md).
- **Source:** Matthew J. Colbrook, *Global uniqueness for the weighted p-Calderón problem*, Zenodo preprint, 6 November 2026. [Record](https://zenodo.org/records/24017133), DOI [10.5281/zenodo.24017133](https://doi.org/10.5281/zenodo.24017133).
- **Proof:** [Deposited PDF](https://zenodo.org/api/records/24017133/files/weighted_p_calderon.pdf/content), 47 pages. The record lists file weighted_p_calderon.pdf and checksum md5:8122fa470a287f27a3037d0a8bbe0904.
- **Reviewer and extent:** Codex (AI), comparing the abstract, Theorem 1.1 and equation (1.2) on p. 2, the discussion on pp. 3–4, and the smoothness convention on p. 5. This records the extent inspected, rather than a full independent proof audit.

## Match to the original target

| Requirement in AIM 049 | Deposited theorem |
| --- | --- |
| Every dimension at least three | Theorem 1.1 assumes n at least three. |
| Every known exponent strictly between one and infinity, excluding two | Theorem 1.1 has exactly this exponent range. |
| Bounded, connected, smooth Euclidean domain | The same domain class is used. |
| Arbitrary smooth, strictly positive scalar weights, smooth up to the boundary | Theorem 1.1 states this class; p. 5 defines smoothness on the closure using extensions to a neighbourhood. |
| Equality of the full weak nonlinear boundary maps | Theorem 1.1 uses every datum in the trace space of W1,p; equation (1.2) gives the weak map. |
| Conclude equality of both weights throughout the domain | This is the conclusion of Theorem 1.1. |
| No ordering, smallness, analyticity or invariance in one direction | None of these restrictions is imposed in Theorem 1.1. |

Theorem 1.2 is a separate noncritical-solution construction; the uniqueness resolution is Theorem 1.1.

## Recorded outcome and review limits

The repository status is **Solved — affirmative proof**, following the maintainer's explicit resolution report and the matching theorem in the publicly deposited preprint. The original statement, ID and file are retained, and the proof is linked at its source.

This source-and-statement check does not certify every argument in the 47-page manuscript, its cited continuation input, peer review, or formal verification. The manuscript's AI declaration is on p. 5. No Lean verification is claimed.
