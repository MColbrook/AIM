# Global convergence of the simple CRDT iteration for quadrilaterals

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**AI disclosure:** The solutions were found by AI.

**Scope:** Partial progress. Global convergence for four-prevertex quadrilaterals; prescribed subdivisions with more vertices and general polygons remain open.

Read the [manuscript](main.pdf) and [standalone source](main.tex). The [target comparison](TARGET_COMPARISON.md) states the quantifiers covered and the remaining scope. The [independent AI audit](../../solution_reviews/2026-11-04-numerical-analysis/651-review.md) records the checks. Independent human review and formal verification are not claimed.

The [statement snapshot](statement.md) matches [AIM 651 at revision `c4036871b0bf`](https://github.com/MColbrook/AIM/blob/c4036871b0bf15cbc83e79c780b7191bcbb2cfed/problems/651-simple-crdt-convergence.md). [SUBMISSION.json](SUBMISSION.json) records authorship, disclosure and input hashes; [MANIFEST.sha256](MANIFEST.sha256) pins the public files. See the [reference review](../../solution_reviews/2026-11-04-numerical-analysis/references.md) for source checks and access limits.

Reproduce the PDF by running twice in this directory:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```
