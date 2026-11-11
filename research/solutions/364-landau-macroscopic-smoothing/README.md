# Macroscopic bounds for the Landau–Coulomb equation

Kaiwen Jin · [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This manuscript presents a complete solution claim for [Problem 364, Landau–Coulomb smoothing controlled only by macroscopic quantities](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/364-landau-macroscopic-smoothing.md). Independent mathematical review is requested.

For every real entropy cap H and every 0 < τ < T, Theorem 1.1 asserts a finite bound C(H,τ,T) for the global velocity supremum of each nonnegative smooth rapidly decaying solution on [0,T], normalized to mass one, zero momentum and energy three. The constant is independent of every initial higher moment, Fisher information, supremum and derivative norm. No sharp waiting-time exponent or rough-data existence theorem is claimed.

The proof combines a weighted Fisher estimate, a local small-entropy estimate retaining two transverse diffusion directions and the nonlinear collision energy, an exact velocity dilation at large velocities, and a bounded-region parabolic iteration.

- [Complete manuscript](paper/main.pdf).
- [Editable LaTeX source](paper/main.tex) and [bibliography](paper/references.bib).
- [Comparison with the original target](TARGET_COMPARISON.md).

The result is analytic. It does not rely on numerical experiments, computational certificates or formal proof code.

## Build

The sources require a standard TeX Live installation with `latexmk`, BibTeX, Latin Modern, `amsmath`, `amsthm`, `mathtools`, `aliascnt`, `microtype`, `hyperref` and `cleveref`. From this directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build -cd paper/main.tex
```

The output is `paper/build/main.pdf`. Compilation checks document construction; it does not certify the mathematics.

## AI use

OpenAI Codex assisted with proof development, source checking and manuscript preparation. The author is responsible for the mathematical claims and references. An AI reader and an AI referee reviewed the draft in separate contexts, followed by one author revision. No human or formal verification is claimed, and no separate detailed AI review report is submitted.
