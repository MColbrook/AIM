# Reproduction and validation

Checked on October 12, 2026 (Asia/Shanghai). The manuscript is an analytic
consequence note. Its proof dependency is the publicly cited OpenAI theorem;
compilation and package checks do not independently prove that theorem.

## Selected-source build

The exported `paper/main.tex` was compiled from the public checkout with
latexmk, shell escape disabled and a separate generated-output directory.
Only that public source and standard TeX packages were manuscript inputs.
The bibliography is embedded in the source. No figure, external local input,
numerical data or unpublished supplement is required.

Observed environment:

- TeX Live 2025, pdfTeX 1.40.27.
- latexmk 4.86a.
- Python 3.12.14 and pypdf 6.10.0 for PDF text and metadata inspection.

From the package directory, the reproduction command is:

```sh
latexmk -pdf -no-shell-escape -halt-on-error -interaction=nonstopmode \
  -outdir=build paper/main.tex
```

The fresh build succeeded and produced three pages, with no warnings,
unresolved references or overfull/underfull boxes. Extracted text on all
three rebuilt pages exactly matched the submitted PDF. The submitted pages
were also read and visually inspected; the equations, citations and links
are legible and complete. Internal PDF links resolve to the intended theorem,
corollary, equation or bibliography destinations. Metadata contain the
public author/title and ordinary TeX production fields.

Submitted source SHA-256:
`57b9d73d69495e0d2ebe50a0a3ce0f927c097e0a252986baa0fbbb72a78eef6b`.

Submitted PDF SHA-256:
`477a84571544eca364c656f3d0f95e5ce35e41f6029bc7a96d02f9d834b8d532`.

The fresh PDF's byte hash differs because creation metadata/document IDs
can vary. Reproduction here means identical extracted manuscript content
and checked page layout, not guaranteed byte-identical TeX output.

## Source and target identification

The public AIM 450 file at target revision
`c9929805cece044705abaaebe1cebddac1ba11a6` has SHA-256
`fc5c2577276f951e5d3789af2eb113b6d1abeef0b76330c041f8948bb60a28b0`.
The [target comparison](TARGET_COMPARISON.md) covers every stated hypothesis,
quantifier and conclusion.

The [OpenAI preprint](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf)
is pinned at revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
Its PDF SHA-256 is
`38d5c48b4d83500390195f5c177d2b3d2b7eb80aa9a732ad30a49db51f46e8a4`;
Theorem 1.1 is on PDF page 3. The complete 87-page proof remains at that
public source. The note does not replace it with a new uniform-estimate proof.

The background formulation is explicitly cited to the verified final
[Lacey--Li arXiv 0704.0808v3](https://arxiv.org/abs/0704.0808v3),
January 11, 2008, Conjecture 1.5 and equation (1.6). The associated journal
metadata and DOI are also given in the manuscript.

## Package checks

`PUBLIC_MANIFEST.json` lists the seven content files and their purposes,
sizes and SHA-256 hashes. It excludes itself and `SHA256SUMS` to avoid a
self-reference. `SHA256SUMS` covers those seven files and the manifest;
only the checksum file itself is excluded. Verify from the package root:

```sh
shasum -a 256 -c SHA256SUMS
```

The nine-file package was checked against that exact allowlist, with no
symlinks or extra files. Its content and PDF contain no unpublished-file
dependencies. Local Markdown links were checked in the public receiving
checkout. The repository's `scripts/catalogue.py --check` validates catalogue
structure, mathematical delimiters, local links and generated-file freshness.
It does not assess the correctness of the imported analytic proof.

No numerical experiments, proof certificates or Lean project are submitted.
Independent mathematical review of the complete cited argument is requested.
