# AIM 1034: A certified lower bound for the ovals problem

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Partially resolved — partial progress.

A certified universal lower bound greater than 0.96221 holds for the curvature operator on the full smooth closed-curve class.

**Remaining target:** Raise the universal lower bound to one for every smooth closed spatial curve of length $`2\pi`$, or construct a counterexample. No optimality claim is made for the new bound.

[PDF manuscript](aim1034.pdf) · [editable TeX](aim1034.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1034-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1034.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1034.tex
python -B verify_ovals_bound.py
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 6 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

The supporting Python checks use only the standard library. Run them without `-O`, because the supplied certificates use assertions. See [verification record](verification.txt). Finite arithmetic and matrix checks support the proof and do not replace its analytic arguments.
