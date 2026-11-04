# AIM 917: Failure of split-product approximations for time-dependent form sums

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Solved — Counterexample.

Under the exact form hypotheses, exponential split products can have no strong limit; resolvent split products can fail weak and strong convergence to the specified unitary propagator.

[PDF manuscript](aim917.pdf) · [editable TeX](aim917.tex) · [individual review](../../solution_reviews/2026-11-03-operators-batch/917-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The complete supplied argument was checked against the current canonical statement by Codex (AI), separately from the author. The review records the proof reasoning, precise primary-source locators, scope, bounded current-literature comparisons and access limits. The archive's earlier review claims were not used as evidence.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim917.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim917.tex
```

The saved source also compiled with the built-in document compiler. Both final export passes succeeded without LaTeX/box warnings, unresolved references or missing characters. All 6 pages were rendered and visually inspected; author information, PDF metadata and page numbering were checked.
