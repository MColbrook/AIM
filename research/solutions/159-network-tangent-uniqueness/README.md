# Unique tangent varifolds for planar network flow

Kaiwen Jin's article proposes an affirmative resolution of [AIM Problem 159](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/159-network-tangent-uniqueness.md). At an interior finite-time singularity, the arclength varifolds of the rescaled networks converge locally weakly. The limit includes the integer multiplicity of each regular strand and is specified in the original coordinates.

- [Manuscript PDF](paper/article.pdf)
- [Comparison with the original statement](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json)

From the paper directory, compile the manuscript with a TeX Live installation containing AMS-LaTeX, Latin Modern, microtype, mathtools, geometry, hyperref, and cleveref.

    cd paper
    SOURCE_DATE_EPOCH=1795806690 FORCE_SOURCE_DATE=1 latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -jobname=article -outdir=build main.tex

The article is analytic and states the mathematical and source dependencies in full. It records AI assistance and the scope of the AI review.
