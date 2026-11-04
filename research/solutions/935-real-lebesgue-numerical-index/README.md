# AIM 935: A strict numerical-index bound for real Lebesgue spaces

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk); [department profile](https://www.damtp.cam.ac.uk/person/mjc249).

**Status:** Solved — Counterexample.

The proposed real Lebesgue numerical-index identity fails at every permitted non-Hilbert exponent, using three-dimensional perturbations and additional exact certificates at exponent four.

[PDF manuscript](aim935.pdf) · [editable TeX](aim935.tex) · [individual review](../../solution_reviews/2026-11-03-operators-batch/935-review.md) · [source receipt](SOURCE_RECEIPT.json) · [source changes](source_changes.diff) · [checksums](MANIFEST.sha256).

The complete supplied argument was checked against the current canonical statement by Codex (AI), separately from the author. The review records the proof reasoning, precise primary-source locators, scope, bounded current-literature comparisons and access limits. The archive's earlier review claims were not used as evidence.

## Reproduce

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim935.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error aim935.tex
```

The saved source also compiled with the built-in document compiler. Both final export passes succeeded without LaTeX/box warnings, unresolved references or missing characters. All 9 pages were rendered and visually inspected; author information, PDF metadata and page numbering were checked.

The standard-library exact checks use assertions; run without Python `-O`. They write the two JSON certificates beside the scripts. Public I/O uses UTF-8 and LF deterministically; the numerical comparisons use integers and fractions.

```sh
python -B verify935_exact.py
python -B verify935_independent.py
python -B verify935_interval.py
```

All three final programs passed, and both resulting certificate objects equal the submitted originals. See [verification output](verification.txt). The finite certificates supplement the all-exponent analytic perturbation proof.
