# AIM 1007: an embedded eigenvalue in a purely twisted strip

**Author and submitter:** Siavash Sadeghi

**Current AIM status:** Solved — Counterexample, following the [independent maintainer audit](../../solution_reviews/2026-11-03-pr181/1007-review.md) on 3 November 2026.

**Reviewed:** 3 November 2026.

This package gives a counterexample to universal absence of eigenvalues above the first threshold in an asymptotically flat, all-Dirichlet twisted strip. The complete transverse space is retained. The scale is sufficiently large and the phase is selected by an existence argument; no particular numerical scale or phase is certified.

The submitted proof PDF and TeX are unchanged. The reports below record the submission-stage review and proposed status; the linked maintainer audit records the subsequent acceptance. Both reviews were performed by AI, and no human peer review or Lean verification is claimed.

- [Proof PDF](twisted-strip-counterexample.pdf) and [editable source](twisted-strip-counterexample.tex).
- [Resolution report and complete target comparison](RESOLUTION_REPORT.md).
- [Fresh mathematical audit, reviewer identity, and provenance](MATHEMATICAL_AUDIT.md).
- [Submission and literature search](TARGET_AUDIT.md), with [search counts and pinned revision](submission-search.json).
- [Reproduction instructions and results](REPRODUCTION_RECORD.md).

The original package contained a TeX proof, its PDF and a research-state note, without a README, contribution guide or executable tests. Repository submission requirements are supplied by the upstream [CONTRIBUTING.md](https://github.com/MColbrook/AIM/blob/ee5c5c52f527db2f310cb0734bbebc9f7b95aac8/CONTRIBUTING.md). AI-assisted review and exact symbolic identities are supporting evidence, not formal proof verification or human peer review.

## Reproduce the supporting checks

```sh
python -m pip install -r requirements.txt
python verify_identities.py
python -O verify_identities.py
pdflatex -interaction=nonstopmode -halt-on-error twisted-strip-counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error twisted-strip-counterexample.tex
```

From the repository root, run `python scripts/catalogue.py --check --catalogue-only`.

The identity checker covers transverse integrals, scalar normalization, the resonant coefficient, the matrix reduction, weighted-kernel integrals and the ribbon metric. It does not check the functional-analytic estimates or prove existence of an eigenfunction. Those obligations are treated in the proof and the mathematical audit.
