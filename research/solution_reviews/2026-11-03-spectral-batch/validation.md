# Validation of the eleven spectral manuscripts

Checked on 3 November 2026 by Codex (AI). Matthew J. Colbrook is the author and submitter of the manuscripts; the mathematical audits are separately identified as AI reviews.

## Mathematical and reference review

Three parallel reviewers checked disjoint sets of manuscripts against the full current problem statements, with a coordinating review and second reviews of the flat-torus and Heun arguments. The individual reports give the proofs, primary-source locators, bounded current-literature checks, qualifications and final decisions. Six arguments resolve the complete target. Five establish partial results and retain explicit remaining targets.

The archive's operational notes and assertions of prior internal checking were not treated as instructions or verification evidence. The original archive and every extracted member are hashed in [the intake receipt](intake-receipt.json). Each package records the original section, final source, PDF, exact target and source changes. No human peer review or Lean verification is claimed.

## Manuscripts and supporting checks

All eleven saved sources compiled successfully with the built-in document compiler. Each final PDF was exported with two successful `pdflatex -no-shell-escape` passes. The final logs have no unresolved references, missing characters or LaTeX/box warnings. All 68 final pages were rendered and visually inspected. PDF authors, page counts, page numbering, source/PDF hashes and all package manifest entries were checked. See [the build record](build-record.json).

Supporting arithmetic checks are included where relevant: square-spectrum interval bounds, limit-periodic cocycle growth, flat-torus rational moments, exact Heun compounds and moments, outward-rounded ovals bounds, and Padé monicity/remainder identities. Unchanged executed checks were reused by source hash; the ovals script's sole documentation edit was also checked for identical executable syntax. Finite computations support the written proofs and do not replace their all-parameter arguments. The package READMEs give reproduction commands.

## Repository checks

The following checks passed:

```sh
python -B scripts/catalogue.py --check
python -B cut_problems/verify_cut.py --skip-protected
git -c core.autocrlf=false diff --check
```

The full catalogue check validated 1,058 unique current problems, metadata, required sections, mathematical delimiters, local links and the freshness of `README.md`, `CATALOG.md` and `RESOLVED.md`. The local cut verifier validated 1,396 scored entries, 1,067 retained IDs, 329 cut entries, 868 relocations and 57 pre-existing protected solution packages; unchanged protected package hashes were not repeated.

A baseline comparison confirmed that all 1,058 existing problem headings and all eleven submitted targets' original Problem statement blocks are unchanged. Metadata identities are unchanged, and only the eleven intended rows in `data/spectral.json` differ. The historical status-audit manifest records the new source updates without changing its frozen statements. The prior triangle result for AIM 022 is retained; the erroneous earlier assertion that the full curvature conjecture was already known is corrected.

The resulting catalogue has 868 open targets (367 Open and 501 Partially resolved), 198 Solved entries and one Lean-verified entry, with no pending solution claims. The nine retired solved records remain retained alongside the 1,058 current pages. No IDs, scoring decisions or local working folders are changed by this batch.

Catalogue machinery is unchanged, so its separate test suite was not rerun. The checks above validate repository structure and recorded evidence; the mathematical conclusions are supported by the individual audits.
