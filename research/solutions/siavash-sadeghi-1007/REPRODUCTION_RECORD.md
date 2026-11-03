# Reproduction record: AIM 1007

**Run date:** 3 November 2026.

**Submitter:** Siavash Sadeghi.

**Environment:** Windows; Python 3.12.14, SymPy 1.14.0, mpmath 1.3.0; desktop editor LaTeX compiler and existing MiKTeX/pdfTeX 1.40.28. Poppler rendered the exported PDF.

## Symbolic checks

Run from this folder after installing the pinned requirements:

```sh
python verify_identities.py
python -O verify_identities.py
```

Both runs exited successfully. Each verifies 28 exact identities and confirms that the checker rejects three deliberately nonzero scalar/matrix inputs. Checks use explicit exceptions, so optimized Python cannot disable them. Results are in [normal-mode log](identity_checks.txt) and [optimized-mode log](identity_checks_optimized.txt).

No executable verifier or numerical experiment was supplied with the original ZIP. The added checks independently recompute algebra used by the written proof. They do not prove the infinite-dimensional estimates, select a numerical phase, or certify the full theorem.

## PDF build and visual inspection

The saved source compiled successfully with the desktop editor's compiler. The distributable PDF was exported with two passes of the existing MiKTeX installation:

```sh
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error twisted-strip-counterexample.tex
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error twisted-strip-counterexample.tex
```

Both export passes succeeded. Final LaTeX diagnostics contain no unresolved references, LaTeX warnings, or box warnings. The compiler emitted its installation-level reminder about not checking for updates; no package installation or update was performed. The initial sandboxed export attempt failed on MiKTeX's cache permissions, and the authorized retry outside that sandbox succeeded.

All nine final pages were rendered and visually inspected. Author text and PDF metadata both identify Siavash Sadeghi. Equations, references and margins are legible without clipping or overlap. See the [compile summary](compile_check_log.txt).

## Repository checks

From the repository root:

```sh
python scripts/catalogue.py --write --catalogue-only
python scripts/catalogue.py --check --catalogue-only
git diff --check
```

The catalogue and final diff results are recorded in the package's check log. Catalogue checks validate consistency, required sections, math delimiters, links and generated indexes; they are not mathematical verification. Catalogue machinery was not changed, so its implementation test suite was not rerun solely for this data/documentation submission.
