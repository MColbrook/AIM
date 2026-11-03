# AIM 1031: Dense nonperiodic limit-periodic potentials with finite interval spectra

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Solved — Affirmative proof.

Nonperiodic limit-periodic potentials with finite unions of nondegenerate spectral intervals are dense among all limit-periodic potentials.

[PDF manuscript](aim1031.pdf) · [editable TeX](aim1031.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1031-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1031.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1031.tex
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 6 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

This qualitative argument is checked in the written review; no finite spectral computation is used as a substitute for its proof.
