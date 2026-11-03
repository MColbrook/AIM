# AIM 1032: A leading Heun root at a branch point of its limiting spectral tree

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Solved — Counterexample.

The operator with leading coefficient z^4-z has a limiting three-spoke spectral star, with the leading root zero a branch point rather than a leaf.

[PDF manuscript](aim1032.pdf) · [editable TeX](aim1032.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1032-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1032.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1032.tex
python -B heun_exact_check.py
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 6 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

The supporting Python checks use only the standard library. Run them without `-O`, because the supplied certificates use assertions. See [verification record](verification.txt). Finite arithmetic and matrix checks support the proof and do not replace its analytic arguments.

The support diagram is copied unchanged from the submitted archive. Exact rational checks cover all residue classes and finite compounds; the analytic proof establishes every degree and the full limiting law. A separate exact beta-product moment check covers orders zero through twelve.
