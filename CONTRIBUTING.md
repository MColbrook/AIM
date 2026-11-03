# Contributing

Suggestions, corrections and resolution reports are welcome through [issues](https://github.com/MColbrook/AIM/issues) or pull requests.

## Adding or revising a problem

Give a precise statement, primary references, and a dated search for later proofs or counterexamples. Explain its applications or mathematical significance; say when no direct application is known. Further additions exclude numerical linear algebra.

## Reporting a resolution

Include the problem ID and repository commit, a proof or counterexample link, and an explanation of how it matches the full target. Identify what was reviewed and by whom, including whether the review was human or AI.

For Lean work, follow the [setup and verification guide](docs/lean/README.md).
The shared [statement workspace](lean-statements/README.md) pins the same Lean,
Mathlib and LeanCert versions as OpenProblemsInNLA. Complete proof projects
live in `research/lean/<ID>/` and use the isolated Linux verification workflow.

## Status and evidence

Use the [status labels](README.md#problem-status), keeping the page badge and metadata consistent.

- **Partially resolved** entries need nonempty `**Known cases:**` and `**Remaining target:**` notes in **Status review**.
- A complete claim awaiting independent review is **Solution claimed**.
- **Solved** requires a published resolution or a documented independent audit of the complete argument.
- **Lean verified** requires a local `verification_record` linked from the page: pinned proof revision, Lean and dependency versions, theorem-to-target comparison, reproduction commands, a dated successful log, and transitive axiom output. Only `propext`, `Classical.choice` and `Quot.sound` are acceptable; no `sorryAx` or unproved custom axioms.

Only `Open` and `Partially resolved` count as open targets. Use `Solved`, `Lean verified` or `Solution claimed` in the existing page and `data/*.json` row, keeping the ID and linking to the proof and review; Lean-verified rows also need `verification_record`. The generator lists claims separately from solved problems. Other retained statuses use `research/` and `catalogue.json`. Update `last_checked` only after an actual literature or evidence review.

Retained entries need a subject `group`; solved entries also need an `outcome` and direct `proof` and `review` links for the generated lists.

## Updating the catalogue

Problem pages need **Area**, **Status**, **Last checked**, and the sections **Problem statement**, **Application**, **References**, and **Status review**. Put the status badge before the first section. Use `math` fences for display equations and dollar-backtick delimiters for inline equations, with core TeX operators such as `\mathop{\mathrm{Per}}`.

Update the page and its `data/*.json` row. Add new IDs to a publication batch in `catalogue.json`; preserve IDs across active pages, retained resolutions and the cut registry. An editorial cut preserves the complete problem and dedicated solution packages in cut_problems. The [30 October backfill](research/catalogue-backfill-2026-10-30/README.md) explicitly reuses 111 cut IDs: each historical cut record registers its replacement file, stable further-problem key and matching subject group. Keep the archived identity distinct from the current entry. Further reuse requires an explicit editorial decision and a corresponding registry update. Repair links when moving files. Edit the generator for README or index wording.

```sh
python3 scripts/catalogue.py --write --catalogue-only
python3 scripts/catalogue.py --check --catalogue-only
```

The catalogue-only checks cover registered current, retained and cut AIM pages plus generated indexes. Omit --catalogue-only for a full-tree audit, which also scans staged drafts and historical logs. The checks validate structure and links, not mathematical correctness. Run `python3 scripts/test_catalogue.py` when changing catalogue machinery.

Optional rendering QA: install `scripts/requirements-math.txt` and `mathjax-full@3.2.2`, set `NODE_PATH` to its `node_modules` directory, and run `python3 scripts/check_math.py`.

## Local working folders

`FURTHER_problems/`, `PROBLEM_SCORING/` and `cut_problems/` stay local and must not be committed. Downloaded audit sources under `_sources/` also stay local; publish the original source URL and scope review. A public checkout validates the historical selection registry without requiring those unpublished files. A local checkout with the archive present continues to validate its records.
