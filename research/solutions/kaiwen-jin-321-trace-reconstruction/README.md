# AIM 321: negative resolution from a primary lower-bound theorem

This is an attributed literature update for [AIM problem 321](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/321-polynomial-trace-reconstruction.md).
The underlying lower bound and construction are due to OpenAI, *Quantitative lower bounds for trace reconstruction*, September 24, 2026, [Theorem 1.2, page 2, equation (1.2)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf).

For every fixed deletion probability q in (0,1), its one-trace indistinguishability bound defeats every polynomial sample budget, even for randomized common decoders with unrestricted computation. The note proves the testing, iid-product and ceiling steps and states the complete negative quantifiers.

- [Manuscript](paper/trace_reconstruction_negative.pdf), by Kaiwen Jin, contact yui.ui.siki@gmail.com.
- [Editable standalone source](paper/trace_reconstruction_negative.tex).
- [Target correspondence](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The result is analytic and uses the cited public theorem. Its mathematical proof has no numerical or certificate input. To rebuild with a standard TeX Live installation:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/trace_reconstruction_negative.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/trace_reconstruction_negative.tex
shasum -a 256 -c SHA256SUMS
```

AI use and review: OpenAI Codex assisted in source retrieval, drafting, source-to-target checking and the elementary proof checks. The final three-page manuscript compiled without unresolved references. No separate detailed AI review report is submitted; independent mathematical review is requested. Catalogue classification is left to the maintainers.
