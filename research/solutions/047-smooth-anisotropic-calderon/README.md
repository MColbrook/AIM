# Smooth anisotropic Calderón uniqueness: an attributed exposition

This package supplies a complete natural-language exposition of the argument
in OpenAI's September 24, 2026 preprint, together with the deduction for
[AIM 047](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/047-smooth-anisotropic-calderon.md).
The underlying uniqueness argument and its priority are attributed to OpenAI.
The package is offered as a literature update for mathematical review.

Theorem 2.1 of the [manuscript](paper/manuscript.pdf) states the full target:
for every compact connected smooth manifold of dimension at least three with
nonempty smooth boundary, and every pair of smooth positive Riemannian metrics
with the same tangential boundary metric, equality of their single ordinary
zero-frequency Dirichlet-to-Neumann maps implies a smooth diffeomorphism fixing
the whole boundary and pulling one metric to the other. Nonorientable
manifolds and disconnected boundaries are included. The proof occupies
Sections 3–10; [the target comparison](TARGET_COMPARISON.md) gives locations.

The source preprint is
[Smooth anisotropic uniqueness in the Calderón problem from one boundary patch](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026),
pinned at revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, especially
Theorem 1.1 and Corollary 1.2. The submitted exposition includes the patch
argument, angular spectral estimates, and the passage to ordinary full
boundary measurements. It does not claim a new discovery.

## Contents and reproduction

- [Complete manuscript](paper/manuscript.pdf), by Kaiwen Jin,
  contact `yui.ui.siki@gmail.com`.
- [Editable LaTeX source](paper/manuscript.tex), its bibliography and vector
  figure sources.
- [Target comparison](TARGET_COMPARISON.md) and [AI-use disclosure](AI_USE.md).
- [License](LICENSE) and [attribution and modification notice](NOTICE).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

With a TeX distribution containing `latexmk`, `natbib`, `hyperref`, `cleveref`,
and TikZ, build from this package directory:

```sh
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/manuscript.tex
```

The argument is analytic. It uses no numerical experiment, computer-assisted
certificate or formal proof project. No additional unpublished supplement is
needed to read the argument.

## Review status

AI assistance and mathematical checks are disclosed in the manuscript and
`AI_USE.md`. No formal verification or independent human refereeing is claimed.
Successful typesetting and file verification establish artifact reproducibility;
they do not certify the theorem. Independent mathematical review is requested,
and catalogue classification is left to the maintainers.
