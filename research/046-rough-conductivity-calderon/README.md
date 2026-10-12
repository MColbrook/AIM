# Measurable conductivity nonuniqueness: AIM 046 literature update

This package reports a public counterexample to the unrestricted three-dimensional scalar conductivity assertion in [AIM Problem 046](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/046-rough-conductivity-calderon.md). The construction and nonuniqueness theorem are due to OpenAI, **Nonuniqueness for Bounded Measurable Scalar Conductivities in Three Dimensions**, September 23, 2026, [Theorem 1.1, p. 1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf).

The supplied [expository note](paper/calderon_measurable_note.pdf), by Kaiwen Jin, explains the correspondence with the catalogue target and derives equality of the complete weak Dirichlet-to-Neumann maps from the cited scalar branching block. It claims exposition and target comparison. The original preprint supplies the scalarization and branching construction.

## Files

- [Manuscript PDF](paper/calderon_measurable_note.pdf) and [editable LaTeX source](paper/calderon_measurable_note.tex).
- [Target comparison](TARGET_COMPARISON.md), including the exact public dependency and its scope.
- [Public manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

## Rebuilding the note

The source is standalone and requires a normal LaTeX installation with article, Latin Modern, AMS packages, mathtools, geometry, microtype, needspace and hyperref. The exported manuscript was built with pdfTeX from TeX Live 2025 and latexmk 4.86a.

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/calderon_measurable_note.tex
```

A successful typesetting build checks the document's build integrity. The mathematical evidence is the analytic argument and its public cited dependencies. No numerical experiment or local Lean proof is part of this package.

## Attribution and review

OpenAI Codex assisted source retrieval, mathematical checking, drafting and typesetting. A same-context AI proof audit and one fresh-context AI manuscript review were conducted during preparation; these are not independent human proof certification. No detailed AI review report is submitted. Independent mathematical review is requested. Catalogue classification is left to the maintainers.
