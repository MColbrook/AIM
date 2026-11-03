# The cubic Fejer property on simplices in every dimension

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**Target:** [AIM 641 at revision `59a8f0c2957d`](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/641-bos-simplex-interpolation-nodes.md), with a [local statement snapshot](statement.md).

**Submission status:** Partial solution claim (cubic conjecture only); awaiting pull-request review. This package does not change the catalogue status.

Read the [manuscript (PDF)](aim641_cubic_fejer.pdf) or [standalone LaTeX source](aim641_cubic_fejer.tex). The saved package includes the exact certificate and verification scripts linked below. Separate pre-submission and reference-audit reports are not included in this copy; independent human review and formal verification are not claimed.

Only the cubic Fejer conjecture in AIM 641 is addressed. The three quartic conjectures grouped into that entry are not claimed.

[SUBMISSION.json](SUBMISSION.json) records the author information, input hashes and pinned target. The [complete original combined source](submission-original/five_targets.tex) is preserved byte for byte for provenance; only the indicated argument is submitted in this package. The original source describes itself as prepared with ChatGPT.

Separate source-validation and document-production receipts and a package checksum manifest are not included in this saved copy.

To reproduce the standalone PDF with an existing LaTeX distribution, run twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim641_cubic_fejer.tex
```

No external figures or bibliography files are required.

The exact certificate is included as [JSON](cubic_certificate.json), with [symbolic verification](verify_cubic.py) and a [direct polynomial cross-check](crosscheck_cubic.py). Run `python verify_cubic.py` and `python crosscheck_cubic.py` with SymPy installed, without Python optimization (`-O`). The saved [review log](review-verification.log) records additional checks.
