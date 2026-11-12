# Periodic probability densities for the full voltage–conductance equation

Author: Kaiwen Jin  
Contact: yui.ui.siki@gmail.com

This package presents a proposed affirmative answer to
[AIM problem 354](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/354-voltage-conductance-periodic.md).
Theorem 1.1 constructs, for suitable positive physical parameters, a nonnegative
periodic probability density for the full voltage–conductance equation with a
nonconstant actual firing rate. It retains the reset boundary, reflection at
zero conductance, and feedback in both conductance drift and diffusion.

The claim is existential. The construction selects parameters analytically;
it supplies neither an explicit numerical parameter certificate nor a stability
classification of the periodic solutions. Independent mathematical assessment
is requested.

- [Complete manuscript](paper/main.pdf)
- [Editable TeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)

The argument is analytic. No numerical experiment, code-based certificate, or
formal proof is used.

To rebuild with a standard TeX installation providing AMS-LaTeX, mathtools,
microtype, geometry, and hyperref, run this command inside paper/:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

The selected source files suffice; no external figures, bibliography database,
or private supplement is needed.

AI assistance was extensive and included mathematical exploration, proof
development, literature retrieval, internal checks, and writing. The manuscript
contains the AI use statement. A detailed AI review report is not included.

The initial 26-page draft received AI reader feedback with a disclosed reading-order limitation and partial layout coverage, and a separate full-manuscript AI referee reading with source checks. This 27-page version incorporates one combined revision and author artifact checks. No further reviewer pass on the revised bytes, independent human review, or formal verification is claimed.

The selected sources were compiled in isolation. Compilation and document checks establish reproducibility of this artifact, not mathematical certification.
