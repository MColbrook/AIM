# Reproduction: AIM 1021

Checked on 3 November 2026 by Codex (AI).

## Exact supporting checks

Use Python 3.12, SymPy 1.14.0 and mpmath 1.3.0:

```sh
python -m pip install -r requirements.txt
python -B verify_identities.py
python -B -O verify_identities.py
```

Both runs passed all 35 exact identities and inequalities and rejected the two deliberately incorrect scalar/matrix inputs. Output is retained in [normal mode](identity_checks_normal.txt) and [optimized mode](identity_checks_optimized.txt). The checks use explicit exceptions, not removable assertions.

They cover the monodromy derivative and indexing, initial discriminant and rational bounds, period-independent local-density normalization, elliptic conjugacy and phase identities, adiabatic first-order cancellation, boundary current, the Combes–Thomas exponent budget, and Gordon transfer identities. They support the algebra; the written [review](../../solution_reviews/2026-11-03-aim1021/1021-review.md) checks the analytic estimates, induction and spectral conclusions. No spectral discretization or finite numerical experiment replaces those arguments.

## PDF

The saved TeX compiled successfully with the built-in document compiler. The distributed PDF was exported using the existing MiKTeX pdfTeX 1.40.25 installation:

```sh
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error limit_periodic_mixed_spectrum.tex
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error limit_periodic_mixed_spectrum.tex
```

Two final export passes on the finished source exited successfully. The final log has no LaTeX warnings, undefined references or citations, or overfull/underfull boxes. The nine pages were rendered with Poppler and visually inspected. The displayed author and PDF metadata identify Matthew J. Colbrook. No package installation or LaTeX update was performed; an initial sandboxed export could not access MiKTeX's cache, and the authorized retry succeeded.

## Repository

From the repository root:

```sh
python -B scripts/catalogue.py --write --catalogue-only
python -B scripts/catalogue.py --check
python -B cut_problems/verify_cut.py --skip-protected
git diff --check
```

The cut verifier is a local preservation check when the working archive is present. Neither it nor this submission changes selection decisions or problem IDs. The local working folders are not part of this package. Catalogue machinery is unchanged; consistency checks do not certify mathematics.
