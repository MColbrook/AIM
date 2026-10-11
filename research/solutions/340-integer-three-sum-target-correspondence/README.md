# AIM 340: correspondence with a recent integer 3SUM algorithm

This submission reports an application of an existing algorithm theorem to [AIM Problem 340 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/340-integer-three-sum-hardness.md).

Josh Alman and Virginia Vassilevska Williams give the deterministic integer 3SUM algorithm in [arXiv:2610.06783v1](https://arxiv.org/abs/2610.06783v1), dated October 5, 2026. Their Theorems 2 and 22, Section 3.4, supply the fixed-power speedup. All fast-algorithm credit belongs to those authors. The note gives an elementary reduction enforcing the AIM statement's pairwise-distinct elements, zero-element convention, fixed polynomial integer universe and charged preprocessing. It obtains a uniform deterministic total-time bound of `O(n^(2-1/2500))` on every valid input.

## Materials

- [Three-page paper (PDF)](paper/aim340_target_correspondence.pdf) and [editable LaTeX source](paper/aim340_target_correspondence.tex).
- [Exact target comparison](TARGET_COMPARISON.md).
- [Public file manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

Author: Kaiwen Jin. Contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).

## Evidence and review

The proof in this note is a mathematical derivation from the cited source algorithm theorem. The full external algorithm proof and its Lean project have not been independently reconstructed or rebuilt here. No implementation, benchmark, numerical experiment, computer-assisted certificate or formal verification is claimed or supplied.

OpenAI Codex assisted source retrieval, the elementary reduction, checking and drafting under the author's direction. The author-side checking used the same AI preparation context. A separate same-vendor fresh-context OpenAI Codex manuscript review found no major or required minor objection within the manuscript and cited-source-interface scope. It checked both bibliography entries, the central derivation and all three PDF pages. No detailed AI review report is included. These checks do not establish human independent review, publication acceptance or a maintainer's status decision. Independent mathematical review of the source and target correspondence is requested.

## Rebuild the paper

Use a standard LaTeX installation providing `geometry`, `amsmath`, `amssymb`, `amsthm`, `fontenc`, `lmodern` and `hyperref`. From `paper/`, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape aim340_target_correspondence.tex
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape aim340_target_correspondence.tex
```

The distributed PDF was built with pdfTeX 1.40.27 and visually inspected on all three pages. Check the distributed file bytes with `shasum -a 256 -c SHA256SUMS` from this package directory. A rebuilt PDF may have a different hash because of its creation timestamp.
