# AIM 1028: The sharp upper constant for the eigenvalue-torsion product on convex domains

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [verified department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Partially resolved — partial progress.

The sharp convex upper constant pi squared over twelve is established in every dimension; the lower constant remains open.

**Remaining target:** Prove or disprove the proposed lower constant $`\inf F=\pi^2/[2(d+1)(d+2)]`$ for every $`d\ge3`$. The appended lower-route obstruction concerns test functions that are not torsion functions and is not a counterexample to this target.

[PDF manuscript](aim1028.pdf) · [editable TeX](aim1028.tex) · [complete review](../../solution_reviews/2026-11-03-spectral-batch/1028-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The mathematical review is by Codex (AI), separately identified from the author. The original archive’s assertions of internal review were not treated as verification evidence. The source has been separated into a standalone article with a title, abstract, author and precise references. The review records the exact scope and the minor clarifications applied.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1028.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim1028.tex
```

The saved source also compiled successfully with the built-in document compiler. Both final PDF export passes succeeded without unresolved references, missing characters, or LaTeX/box warnings. All 8 pages were rendered and visually inspected; author text, PDF metadata and page numbering agree.

This qualitative argument is checked in the written review; no finite spectral computation is used as a substitute for its proof.

The appendix incorporates the separately supplied lower-bound obstruction note. Its radial examples are not torsion functions; the lower conjecture remains a remaining target. Deng’s upper-bound method and the primary geometric inputs retain their attribution.
