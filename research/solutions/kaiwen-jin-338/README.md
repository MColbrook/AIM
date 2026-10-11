# AIM 338: local asymptotic stability is undecidable

This package records a literature resolution of [AIM Problem 338](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/338-polynomial-local-stability-decidability.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

[The note](paper/aim338.pdf), by Kaiwen Jin, proves that no total Turing algorithm decides the specified local asymptotic stability predicate for arbitrary exactly encoded rational polynomial autonomous ODEs of unrestricted dimension and degree. [Editable LaTeX source](paper/aim338.tex) and a [target comparison](TARGET_COMPARISON.md) are included.

The undecidability construction is due to Ivan O. Shevchenko, Jun Liu and Xinzhi Liu, [arXiv:2610.12434v1, Theorem 1.5](https://arxiv.org/abs/2610.12434v1). The source is an October 8, 2026 preprint; its proof appears in Section 15, PDF pages 44–45. This note gives the homogeneous local/global scaling argument and the exact effective encoding reduction. It uses the cited theorem and does not reproduce the source's entire construction.

The three-page note includes the stability and attraction quantifiers, forward existence near the equilibrium, continuation of the maximal solutions under scaling, invalid-code handling, and the undecidability contradiction. The argument is analytic and uses no numerical certificate or formal proof artifact.

To rebuild the PDF with a standard TeX installation containing `latexmk` and the packages named in the source, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/aim338.tex
```

The supplied PDF was built with pdfTeX (TeX Live 2025), and all three rendered pages were inspected. `PUBLIC_MANIFEST.json` identifies the four payload files and their SHA-256 hashes; `SHA256SUMS` also covers that manifest. The hashes identify the supplied files, not a promise of byte-identical PDF output across TeX installations.

AI assistance: OpenAI Codex (gpt-6.1-sol) assisted with source retrieval, writing and checking the note. Fresh-context Codex checks examined the note's mathematics and citations, source-order readability and qualitative prose. They shared the host filesystem. No separate detailed AI report is submitted. Independent mathematical review of the note and the cited preprint theorem is requested; catalogue classification is left to the maintainers.

Contact: Kaiwen Jin, <yui.ui.siki@gmail.com>.
