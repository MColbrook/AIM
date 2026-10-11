# Manuscript

The three-page note is in [main.pdf](main.pdf); its editable source is
[main.tex](main.tex). The main uniform estimate and its original proof are
attributed to the public OpenAI preprint cited in the note. Corollary 2 gives
the complete elementary passage to the catalogue target.

With TeX Live and latexmk installed, run from the package directory:

```sh
latexmk -pdf -no-shell-escape -halt-on-error -interaction=nonstopmode \
  -outdir=build paper/main.tex
```

The generated PDF is `build/main.pdf`. The source uses standard LaTeX
packages and embeds its bibliography. It has no external figures, local
input files, private dependencies or scripts. Build output is ignored.
PDF timestamps and document identifiers may vary across builds; comparison
of extracted text and visible pages checks manuscript content.
