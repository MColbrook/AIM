# Optimal obstacle regularity for stable operators

This package contains a proposed full solution to [AIM 465](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/465-nonlocal-obstacle-minimal-smoothness.md), with the minimally smooth obstacle threshold.

The manuscript's Theorem 1.1 states the interior `C^(1+s)` estimate for every noninteger `beta > 1+s`, every `n >= 2` and `0 < s < 1`, and every even positive angular Lipschitz stable density in the problem's class. Exterior values are arbitrary bounded data. Sections 2 and 3 prove a flat boundary quotient estimate and an improvement of the actual value sandwich and tail; Section 4 proves the complete norm estimate.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

The argument and manuscript were developed with AI assistance. An AI reader and an AI referee examined the initial draft in fresh contexts of the same provider; their feedback informed one author revision. The referee reported no major objection at medium confidence. The final revision was checked by the authoring assistant. This is a solution claim offered for independent mathematical review, not independent human or formal certification or acceptance by the problem repository. No separate detailed AI review report is submitted. There are no numerical experiments in this package.

Files:

- `paper/manuscript.pdf`: complete mathematical manuscript.
- `paper/manuscript.tex`: standalone editable source, with its bibliography included.
- `TARGET_COMPARISON.md`: componentwise comparison with the original target.
- `PUBLIC_MANIFEST.json`: selected public files and their content hashes.

To rebuild with a standard TeX Live installation:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

The document build checks the artifact, not the truth of its theorem. Public mathematical dependencies are linked in the bibliography; no private supplement is required to read the proof.
