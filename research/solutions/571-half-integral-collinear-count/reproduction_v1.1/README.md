# Reproducing all 608 Normaliz series

This supplement to [PR122](https://github.com/MColbrook/AIM/pull/122)
adds a bounded-process, checkpointed replay and a standalone receipt checker.
The original manuscript, mathematical source modules, 608-input export and
version 1.0.0 files remain unchanged.

The [AIM review](https://github.com/MColbrook/AIM/blob/24edaadc6bb272737d8da0745c662c992db07b22/research/solution_reviews/2026-10-15-active-prs/571-review.md)
independently reconstructed the reduction and exact algebra,
but stopped after 12 of 608 unique software computations. This contribution
addresses reproducibility of the computational step. The recorded rerun is
author-side work; it does not replace the maintainer's independent acceptance
decision or assert a new mathematical audit, human certification or Lean proof.

## Recorded complete replay

The fresh run on 19 October 2026 completed with `FULL_REPLAY_MATCHED` and
exit code zero. All 608 complete rational functions and original gradings
matched. Reaggregation of the computed outputs also passed all four action
sums, Burnside's identity and the degree-seven polynomial identity.

| Measurement | Recorded value |
| --- | ---: |
| Unique systems freshly computed | 608 / 608 |
| Original cell members covered | 618 / 618 |
| Cached results reused / failed systems | 0 / 0 |
| Normaliz processes / threads per process | 3 / 1 |
| Controller wall time | 3487.01 s (58 min 7 s) |
| Largest individual native computation | 299.03 s |
| Largest single-worker peak resident memory | 34.75 MiB |

The execution host was an Apple M4 Pro with 14 logical CPUs and 48 GiB RAM,
running macOS 26.5.1. This is one observed run, not a portable timing guarantee.
Identity, horizontal, vertical and combined-reflection actions cover 420,
72, 84 and 42 original cells, respectively.

The [complete execution-record bundle](recorded/replay_bundle.json) is
checked with `python3 -S -B reproduction_v1.1/check.py reproduction_v1.1/recorded/replay_bundle.json`.
See the [verification report](recorded/verification.json),
[benchmark and environment record](recorded/benchmark.json),
[608-row timing/memory table](recorded/per_system.csv), and
[single-input diagnostic comparison](recorded/pilot_comparison.json).
The benchmark includes a hardware observation from the same host during the
run. The slowest 20 systems accounted for 33.77% of native computation time;
the median was 0.042 s and the empirical 95th percentile was 118.86 s.
The records retain the software trust boundary described below.

## Install and run

Run the following from the parent package directory, which contains `src/`,
`numerical_case/` and this `reproduction_v1.1/` directory. The controller uses
POSIX process groups, CPU limits and file locks; Linux, macOS or WSL is required.

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B reproduction_v1.1/replay.py \
  --workers 3 --timeout 900 --output numerical_case/raw/fresh-replay
```

On Python 3.13/macOS arm64, reproduce the original wheel bytes with
`.venv/bin/python -m pip install --require-hashes -r reproduction_v1.1/requirements-macos-arm64-cp313.txt`
instead of the general requirements command. This platform-specific hash lock
was resolved against the original wheel; the recorded fresh installation's
wrapper and all eight native-library hashes match `ENVIRONMENT.json`.

Choose a fresh output directory. `--workers` caps simultaneous processes;
each invokes Normaliz with one thread. The timeout is per system, not a claim
that an unfinished system passed. Increase concurrency only within available
CPU and memory capacity. The full replay remains substantially longer than
the stored-data algebra check.

The default options are exactly `HilbertSeries`, `BigInt`, `NoGradingDenom`.
No truncation, floating-point approximation, `NoLLL` or altered input matrices
are introduced. Each worker receives only its exact constraints, grading and
options; the expected rational answer stays in the controller. Each completed
output is compared as an entire rational function and with the original
grading, then saved atomically under its input SHA256.

The original expected input/data SHA256 is
`bd22e0775a0475fe485349483dec748c0045fa3b4e2b0f066a716a3b031bdc21`.

## Interrupt, resume and audit

An interrupt stops only this controller's worker process groups. Completed
records remain. Resume with the same input, driver, mathematical sources,
software and options:

```bash
.venv/bin/python -B reproduction_v1.1/replay.py \
  --workers 3 --timeout 900 --resume --output numerical_case/raw/fresh-replay
```

The controller rechecks every cached record's context, input hash, exact
output and grading before reusing it. A different strategy or software
environment needs a separate output directory. Workers and timeout may be
changed on resumption; each actual invocation records their values. Failed
attempts are retained separately and never counted as completed systems.
`run.json` describes the latest controller invocation, while completed
per-system records and failed attempt files persist. Copy the manifest before
resuming if the complete history of scheduling settings is needed.

Validate all 608 unique outputs, all 618 cell assignments and the full
generating-function/polynomial identities without importing Normaliz:

```bash
python3 -S -B reproduction_v1.1/check.py numerical_case/raw/fresh-replay
python3 -S -B reproduction_v1.1/summarize.py numerical_case/raw/fresh-replay
```

The checker rejects incomplete coverage, missing or modified result files,
wrong gradings, floating-point substitutes for exact integers, changed data,
and inconsistent context or options. Normaliz's empty-numerator zero series
and an explicit zero numerator are compared as the same rational function.
`--only INPUT_SHA256` selects a diagnostic subset; a subset can report only
`SUBSET_REPLAY_MATCHED`, and the full checker rejects it.

The summary exports 608 per-system time/memory rows in `per_system.csv`, the
computed-output algebra in `verification.json`, and timing/environment details
in `benchmark.json`. Keep `run.json` and the complete `results/` directory
together; the manifest binds every result file by SHA256.

For distribution, package the same checked records into one inspectable JSON
file, avoiding hundreds of tracked result files:

```bash
python3 -S -B reproduction_v1.1/bundle.py \
  numerical_case/raw/fresh-replay numerical_case/raw/replay_bundle.json
python3 -S -B reproduction_v1.1/check.py numerical_case/raw/replay_bundle.json
```

The bundle preserves the individual result hashes and the complete
verification report. It is an execution-record bundle, not a mathematical
decomposition certificate.

## What is measured and trusted

An initial matched-environment diagnostic used the slow identity413 input.
The original default driver completed in 296.20 seconds; a separate DualMode
trial completed in 293.55 seconds. Both complete rational functions and gradings
matched. These are single observations, with different Python front ends, not
a statistically established speedup. The full replay therefore retains the
original computation options and uses independent single-thread processes.

`benchmark.json` records the actual full-run wall time, per-system timings,
worker memory peaks, software hashes and zero/nonzero cache reuse. A native
sampling diagnostic located the work inside the Normaliz computation rather
than the Python aggregation. Detailed timings distinguish construction,
native computation, readback and whole-worker invocation. No unmeasured
serial-versus-parallel speedup is claimed.

The recorded macOS replay uses a fresh virtual environment installed from the
same PyNormaliz 2.24 wheel identified in the original `ENVIRONMENT.json`.
Every worker checks its actual wrapper/native hashes against the controller's
environment fingerprint. This binding does not expose the exact compiled
Normaliz minor version; the binary hashes identify what actually ran. A
different platform may install different native bytes and should record a new
run, rather than resume a run from another implementation/environment.

The arithmetic still relies on Normaliz and its native dependencies. `BigInt`
does not remove its bounded degree types or ordinary LLL operations. A
successful fresh replay strengthens reproducibility; it is not a second
counting implementation or a separately checked simplicial-decomposition
certificate. The standalone checker verifies recorded results and exact
algebra; it does not independently derive the Hilbert series.

## Tests

```bash
python3 -B -m unittest discover -s test -v
python3 -B -m unittest discover -s reproduction_v1.1 -p 'test_*.py' -v
```

The new receipt tests use explicitly marked synthetic fixtures. They test
failure handling and evidence accounting; their fixtures are not replay
evidence. Actual Normaliz controls and the full-run results are recorded
separately.

OpenAI Codex implemented and tested this supplement at Kaiwen Jin's request.
No new independent manuscript review or mathematical certification is claimed.
