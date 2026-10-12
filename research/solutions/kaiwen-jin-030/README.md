# AIM 030: SICs from arithmetic dilogarithms

This package contains Kaiwen Jin's expository note, *From arithmetic
dilogarithms to SICs in every dimension*, dated 12 October 2026.

The note deduces the exact all-dimension statement from cited primary
arithmetic results: for each integer `d >= 2`, there exist `d^2` unit vectors
in `C^d` with every distinct squared inner product equal to `1/(d+1)`.
No covariance assumption is added to the question. The construction uses
Weyl--Heisenberg orbits as witnesses.

The decisive primary source is Danylo Radchenko and Campbell Wheeler's
[*Stark units for real quadratic fields and
reciprocity laws*, Hexagon 2610.00186v1, 10 October 2026](https://hexagonmath.org/2610.00186v1),
Proposition 7 and Section 9.2. Its Section 9.2 already announces the SIC
consequence. This submission is a literature update and an explicit derivation,
not a claim of independent discovery. The note also uses the exact versions
of the Appleby--Flammia--Kopp and Radchenko--Wheeler preprints listed in its
bibliography.

- [Complete note](paper/sic_arithmetic.pdf)
- [Editable standalone LaTeX source](paper/sic_arithmetic.tex)
- [Comparison with the original question](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json)
- [Checksums](SHA256SUMS)

The proof uses exact arithmetic theorems and finite algebra. It has no
numerical or formal-verification premise, and no code or certificate is
required to reproduce a computation underlying the proof. The note does not
give an effective algorithm for choosing the algebraic automorphism.

To rebuild the standalone manuscript with a TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper/sic_arithmetic.tex
pdflatex -interaction=nonstopmode -halt-on-error paper/sic_arithmetic.tex
shasum -a 256 -c SHA256SUMS
```

The checksum command verifies the distributed files, rather than promising
byte-identical PDFs after rebuilding with a different engine or timestamp.
The supplied PDF has seven pages. The selected source was compiled with
pdfTeX 1.40.27 / TeX Live 2025; all pages were read and inspected for layout.
The final build had no unresolved citations, unresolved references, duplicate
labels, or overfull boxes. Typed-reference checking found no mismatch.
These artifact checks are separate from the mathematical argument.

OpenAI Codex assisted with retrieval, derivations, checking and preparation.
There has been no independent human review of this note, and no separate
detailed AI referee report is submitted. Independent mathematical review of
the note and its recent arithmetic premises is requested. The primary
reciprocity preprint discloses substantial LLM assistance. No peer-review or
catalogue-acceptance status is claimed by this package.

Contact: **Kaiwen Jin**, **yui.ui.siki@gmail.com**.
