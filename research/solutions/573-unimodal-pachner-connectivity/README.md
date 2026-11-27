# Unimodal Pachner paths for three-manifold triangulations

This package contains Kaiwen Jin's manuscript, its LaTeX source, and the Python verifier for the finite affine calculations. The target in AIM is [problem 573 at the referenced revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/573-unimodal-pachner-connectivity.md).

Build the paper with a TeX distribution that supplies AMS-LaTeX, Latin Modern, microtype, booktabs, TikZ and hyperref.

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

Run the verifier with Python 3 and assertions enabled. The verifier uses the standard library and was tested with Python 3.13.3.

    python3 verify_ear_arch.py

It prints the relative bipyramid replacement table and five Boolean equality checks. The equalities verify the copying seed, buttress slide, two-cell insertion, shortcut and one-buttress join. The theorem is proved in the manuscript from these local identities and the argument for arbitrary input triangulations.
