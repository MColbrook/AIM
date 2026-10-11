# AIM 450: an attributed consequence of OpenAI's uniform estimate

Author of this note: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package reports a public preprint whose Theorem 1.1 covers the complete
target of [AIM 450, Stein's Hilbert-transform bound along Lipschitz
directions](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/450-stein-lipschitz-direction-hilbert-bound.md).
The target is frozen at revision
`c9929805cece044705abaaebe1cebddac1ba11a6`.

The main uniform estimate and its full proof are due to **OpenAI**,
[*A uniform Hilbert transform estimate for Lipschitz directions*, September
25, 2026, Theorem 1.1, PDF page 3](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf).
The source also states the principal-value and weak-type consequences. The
present note restates the exact interface, spells out those elementary
consequences and compares them with the catalogue target. It makes no claim
of an original uniform estimate by the note's author.

The result allows every globally 1-Lipschitz planar unit direction field,
including dependence on both coordinates, and every complex Schwartz input.
The direction is fixed at the output point while the integration parameter
varies. Absolute constants can be taken as `K = 1/a_* > 2` and
`C = C_*^2`, using the source theorem's constants. The complete local passage
is Corollary 2 and its proof in the note.

## Materials

- [Manuscript PDF](paper/main.pdf) and [editable LaTeX source](paper/main.tex).
- [Exact target comparison](TARGET_COMPARISON.md).
- [Build and package reproduction](REPRODUCTION_REPORT.md).
- [Manuscript build instructions](paper/README.md).
- [Public file manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The complete proof of the imported theorem is the directly linked public
preprint. No unpublished supplement is needed to read the note and its cited
proof. This analytic result uses no numerical experiment, computer-assisted
certificate or formal proof project.

## AI use and review

OpenAI's preprint supplies the original mathematical proof. OpenAI's
ChatGPT/Codex assisted the present note's source comparison, drafting and
proof checking, including the stated theorem interface and elementary target
implication. These are AI checks associated with preparation. No separate
detailed AI review is submitted; independent mathematical review of the
complete cited argument is requested.

This is a package-only literature-update submission. Catalogue classification
is left to the maintainers. Successful compilation and package validation
check the submitted artifacts; they do not establish community acceptance
or independent certification of the original theorem.
