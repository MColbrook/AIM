# AIM 1016: Critical inradius asymptotics and a supremum-norm bound for convex domains

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Partially resolved — partial progress.

The critical large-q asymptotic is determined uniformly over convex domains; a separate explicit supremum-norm lower bound holds for p at least N+1.

**Remaining target:** Determine the exact optimal constant at fixed finite parameters and in the other admissible regimes. The supremum-norm bound is not proved sharp and does not cover $`N<p<N+1`$.

[PDF manuscript](aim1016.pdf) · [editable TeX](aim1016.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1016-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1016.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1016.tex
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 7 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

This qualitative argument is checked in the written review; no finite spectral computation is used as a substitute for its proof.
