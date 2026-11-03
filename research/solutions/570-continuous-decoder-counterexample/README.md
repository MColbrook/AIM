# An unbounded cost of continuous decoding on Banach unit balls

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**Target:** [AIM 570 at revision `59a8f0c2957d`](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/570-continuous-decoder-banach-balls.md), with a [local statement snapshot](statement.md).

**Submission status:** Solution claim; awaiting pull-request review. This package does not change the catalogue status.

Read the [manuscript (PDF)](aim570_continuous_decoder.pdf) or [standalone LaTeX source](aim570_continuous_decoder.tex). The [pre-submission check](RESOLUTION_REPORT.md) compares the proof with the target, and the [reference audit](REFERENCES.md) records checked sources. These checks were performed by OpenAI Codex (AI); independent human review and formal verification are not claimed.

The counterexample uses nonseparable Banach spaces, as permitted by AIM 570. The corresponding question restricted to separable spaces is not settled here.

[SUBMISSION.json](SUBMISSION.json) records the author information, input hashes and pinned target. The [complete original combined source](submission-original/five_targets.tex) is preserved byte for byte for provenance; only the indicated argument is submitted in this package. The original source describes itself as prepared with ChatGPT.

[source-checks.json](source-checks.json) records source validation. Separate document-production and package-checksum receipts are not included in this saved copy.

To reproduce the standalone PDF with an existing LaTeX distribution, run twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim570_continuous_decoder.tex
```

No external figures or bibliography files are required.
