# AIM 898: Affine Lipschitz projections on nearly Euclidean convex bodies

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Solved — Counterexample.

Canonical affine-projection norms diverge on explicit symmetric convex bodies, including examples whose Banach-Mazur distance to a Euclidean ball tends to one.

[PDF manuscript](aim898.pdf) · [editable TeX](aim898.tex) · [individual review](../../solution_reviews/2026-11-03-operators-batch/898-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The complete supplied argument was checked against the current canonical statement by Codex (AI), separately from the author. The review records the proof reasoning, precise primary-source locators, scope, bounded current-literature comparisons and access limits. The archive's earlier review claims were not used as evidence.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim898.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim898.tex
```

The saved source also compiled with the built-in document compiler. Both final export passes succeeded without LaTeX/box warnings, unresolved references or missing characters. All 6 pages were rendered and visually inspected; author information, PDF metadata and page numbering were checked.

The supplied vector figure and JSON data illustrate the exact-moment coefficient formula. The divergence proof is analytic and does not depend on plotted samples. To regenerate the illustration, install NumPy, SciPy and Matplotlib, then run `python plot_projection_growth.py`. This replaces the illustration files; PDF plotting metadata can vary.
