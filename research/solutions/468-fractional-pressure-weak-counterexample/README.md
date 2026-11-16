# Proposed compact-support counterexample for AIM 468

Kaiwen Jin proposes a negative answer to the universal assertion in [AIM Question 468 at the original revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/468-fractional-pressure-multidimensional-instantaneous-spread.md). The manuscript constructs a global bounded energy weak solution in three dimensions, with `m=3/2` and one `s` in `(7/8,1)`, whose support remains compact on a positive initial time interval.

**Status: Solution claimed; independent review outstanding.** The result concerns the exact initial-time energy class stated in the question. It does not classify propagation for every parameter triple or for a separately selected solution class.

- [Complete manuscript](paper.pdf)
- [Editable LaTeX source](source/main.tex) and [bibliography](source/references.bib)
- [Comparison with every clause of the target](TARGET_COMPARISON.md)
- [AI-use and review scope](REVIEW_SCOPE.md)
- [Public file manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The argument is analytic. It does not rely on numerical experiments, a numerical choice of the small fractional order, or a computational certificate.

## Build

From this package directory, with LaTeX, BibTeX and latexmk installed:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd -outdir=build source/main.tex
```

The result is `source/build/main.pdf`. The supplied paper was built with pdfTeX 1.40.27 (TeX Live 2025); its packages are declared in `source/main.tex`. All manuscript-specific inputs are in `source/`. Build dates and PDF identifiers may differ.

The manuscript cites the original public sources. Copyright in those sources remains with their authors; their PDFs are not redistributed here. Author contact: `yui.ui.siki@gmail.com`.
