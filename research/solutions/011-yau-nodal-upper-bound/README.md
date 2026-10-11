# A fixed smooth metric violating Yau's nodal upper bound

An attributed exposition by **Kaiwen Jin**
([yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)).

This package concerns [AIM Problem 011](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/011-yau-nodal-upper-bound.md).
Its mathematical construction is due to OpenAI's September 23, 2026 preprint
[Power-law violations of Yau's nodal upper bound](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026),
Theorem 1.1. This is a literature update and exposition; it claims no new counterexample.
The [original preprint PDF](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf)
is available directly at that same pinned revision.

The manuscript gives one fixed smooth positive metric on $`S^4\times S^1`$
and a sequence of nonzero real exact eigenfunctions with
$`\mathcal H_g^4(\{u_j=0\})/\lambda_j^{1/2+\epsilon_0}\to\infty`$
for a fixed $`\epsilon_0>0`$. One admissible dimension-five example
negates the original assertion quantified over all smooth closed manifolds.

- [Complete manuscript](paper/main.pdf)
- [Editable source](paper/main.tex)
- [Target comparison and analytic dependencies](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA256 checksums](SHA256SUMS)
- [Attribution notice](paper/NOTICE) and [original source license](paper/LICENSE.OpenAI)

The proof is analytic. It uses no numerical experiment or formal proof build.
With TeX Live, latexmk, and standard LaTeX packages installed, run
**make paper** from this directory. The compiled PDF is written to
paper/build/main.pdf. The included PDF is the submitted artifact.

Codex assisted with source retrieval, reconstruction, mathematical checking,
drafting and typesetting. The paper identifies this assistance and attributes
the construction to OpenAI. AI checks are not human certification.
No separate detailed AI review report is submitted; independent mathematical
review is requested. Catalogue classification is left to the maintainers.
