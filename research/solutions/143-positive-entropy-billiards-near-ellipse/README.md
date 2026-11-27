# Proposed resolution of AIM 143

[Read the proof (PDF)](paper.pdf) · [LaTeX source](paper.tex) ·
[File checksums](SHA256SUMS)

Kaiwen Jin, *Positive metric entropy for billiards near a fixed ellipse*.

## Comparison with the target

Theorem 1 addresses the existence question in the pinned AIM problem. It
fixes the noncircular ellipse with semiaxes 2 and the square root of 3.
The proof uses smooth centrally symmetric normal graphs over the fixed
ellipse. Their boundaries are strictly positively curved and their
parametrizations converge with all derivatives. Sections 2–6 construct and
control actual specular reflections at those walls. Section 7 restores the
four bounding heteroclinic circles by changing the wall profiles.

Section 8 transfers the positive entropy of the invariant island to the
whole collision probability. It uses actual boundary arclength and the
outgoing angle from the positive tangent, with density
sin(phi) divided by twice the boundary length. Positivity holds for every
member of the resulting sequence after discarding finitely many initial
rows. [Pinned AIM statement](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/143-positive-entropy-billiards-near-ellipse.md).

## Review scope

AI assistance contributed to the argument and manuscript. The full
natural-language proof received an AI audit with separate reviewer roles.
One AI reader and one AI referee reviewed the same frozen draft in fresh
role contexts, each with a separate manuscript package on a shared host.
Filesystem isolation was unverified. A single revision followed, with
checks against the audited argument, its sources, and the rendered pages.
Human peer review is pending.

Compile the standalone source with a TeX Live installation using
`latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex`.
