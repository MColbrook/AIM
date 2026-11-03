# AIM 1019: A flat torus with logarithmic Sobolev constant below half its spectral gap

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Partially resolved — partial progress.

An explicit flat torus has spectral gap one and logarithmic Sobolev constant at most 1296/2669, strictly less than one half.

**Remaining target:** Determine the sharp logarithmic Sobolev constant for general lattices, including its exact value for the displayed triangular-dual torus. Disproving universal equality alone does not answer that part of the entry.

[PDF manuscript](aim1019.pdf) · [editable TeX](aim1019.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1019-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1019.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1019.tex
python -B verify_torus_certificate.py
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 5 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

The supporting Python checks use only the standard library. Run them without `-O`, because the supplied certificates use assertions. See [verification record](verification.txt). Finite arithmetic and matrix checks support the proof and do not replace its analytic arguments.
