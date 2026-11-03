# Sharp logarithmic complexity of adaptive continuous measurements

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**Target:** [AIM 553 at revision `59a8f0c2957d`](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/553-continuous-adaptive-measurement-complexity.md), with a [local statement snapshot](statement.md).

**Submission status:** Solution claim; awaiting pull-request review. This package does not change the catalogue status.

Read the [manuscript (PDF)](aim553_adaptive_measurements.pdf) or [standalone LaTeX source](aim553_adaptive_measurements.tex). The [pre-submission check](RESOLUTION_REPORT.md) compares the proof with the target, and the [reference audit](REFERENCES.md) records checked sources. These checks were performed by OpenAI Codex (AI); independent human review and formal verification are not claimed.

This establishes the sharp asymptotic growth expressly allowed as a target in AIM 553. It does not determine every exact value; in particular N(3) remains open.

[SUBMISSION.json](SUBMISSION.json) records the author information, input hashes and pinned target. The [complete original combined source](submission-original/five_targets.tex) is preserved byte for byte for provenance; only the indicated argument is submitted in this package. The original source describes itself as prepared with ChatGPT.

[source-checks.json](source-checks.json) records source validation. Separate document-production and package-checksum receipts are not included in this saved copy.

To reproduce the standalone PDF with an existing LaTeX distribution, run twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim553_adaptive_measurements.tex
```

No external figures or bibliography files are required.
