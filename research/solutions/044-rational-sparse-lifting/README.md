# AIM 044: a rational-input specialization of Kelner's sparse solver

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

This package submits a complete argument for the
[pinned problem 044](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/044-sparse-linear-solve-bit-complexity.md),
revision `c9929805cece044705abaaebe1cebddac1ba11a6`, as a literature update
and explicit rational-input specialization. The central algorithm is due to
Jonathan A. Kelner,
[arXiv:2609.38101v1](https://arxiv.org/abs/2609.38101v1), posted
29 September 2026, after the problem page's 8 September literature check.
No algorithmic priority or independent mathematical certification is claimed.

Theorem 1 gives a deterministic algorithm for every fixed positive integer
`c` and every promised nonsingular rational sparse matrix and nonzero rational
right-hand side. It attains relative Euclidean solution error at most
`n^-c/10` in `~O_c(nm)` bit operations. Sections 2-3 provide the lifting,
height, short-operand and direct forward-error argument, importing Kelner's
fast bounded reconstruction theorem. This covers the full pinned target;
classification in the AIM catalogue remains subject to maintainer review.

## Materials

- [Complete manuscript](paper/aim044.pdf) and [editable LaTeX](paper/aim044.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [Code, tests and reproduction at fixed commit d1541aa](https://github.com/yuiyuiui/aim-044-sparse-lift/tree/d1541aa86177584bcf75dc8545d8859a4d549258).
- [Pinned code reproduction instructions](https://github.com/yuiyuiui/aim-044-sparse-lift/blob/d1541aa86177584bcf75dc8545d8859a4d549258/numerical_case/README.md)
  and [compact finite-case results](https://github.com/yuiyuiui/aim-044-sparse-lift/blob/d1541aa86177584bcf75dc8545d8859a4d549258/numerical_case/published/SUMMARY.md).

`PUBLIC_MANIFEST.json` and `SHA256SUMS` bind the selected files. The manuscript
is standalone and uses only public cited sources; no private supplement is
needed for its argument. With a standard LaTeX installation, build it twice
from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/aim044.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/aim044.tex
```

## Validation and review scope

The final six-page manuscript was built, read on every page and visually
checked; its references have no unresolved or mismatched types. The isolated
code projection passed all 14 tests and 16 admissible fixed cases, including
exact Gaussian reference solves, exact squared error acceptance and a
32768-bit reconstruction modulus. These finite software checks do not prove
the all-input theorem or the asymptotic bit-operation bound.

OpenAI Codex assisted with source retrieval, derivation, proof checking,
implementation and finite-case checks, as disclosed in the manuscript.
The preparation includes AI checking by the same assistant that developed
the argument; no independent human or formal verification is asserted.
No separate detailed AI report is submitted. Independent mathematical review
is requested. This package-only contribution leaves catalogue status changes
to the maintainers.
