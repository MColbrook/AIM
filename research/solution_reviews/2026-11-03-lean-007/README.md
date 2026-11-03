# AIM 007: Lean verification record

Reviewed on 3 November 2026. **Verdict: Lean verified; affirmative proof.**

Quanyu Tang and Haiqi Zhang's formal theorem covers [AIM 007](../../../problems/007-buckling-load-ball.md). This record combines an AIM review of the statement, concrete definitions and assumptions with **Palomar's external mechanical verification**, as requested by the editor. It does not claim a new AIM kernel replay or human peer review.

## Pinned proof and successful checks

- [Palomar registration](https://palomar-registry.org/entry?id=PALOMAR-2026-10-18-000008&version=1): `PALOMAR-2026-10-18-000008`, version 1, verified at `2026-10-18T07:02:04Z`.
- [Registered source revision](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/tree/5311f47821b5da92e81e75b7da5091d176c8deb9): `5311f47821b5da92e81e75b7da5091d176c8deb9`.
- Lean: `leanprover/lean4:v4.35.0-rc3`; Mathlib: `c55e6e786f49471c72fbddbec5415808896aec1e`. The 81 vendored EllipticPDE modules are pinned to upstream `ec784093f30308ef770ff855ce624725adf6f870`; the complete dependency revisions are retained in [registration.json](registration.json).
- [Palomar's successful verification run](https://github.com/PalomarRegistry/PalomarSubmission/actions/runs/39105403007), using verifier revision `d4e41c1d5b0d114c4859e6e5831dc6d3ad1d0d44`. We read the live run metadata and downloaded its `mechanical-report-f9dxp5fzpa27` artifact. The report's SHA-256 matches the immutable registration.
- [Preserved mechanical report](mechanical-report.json): `status: pass`, `stage: complete`, no errors or warnings. Its Comparator transcript records acceptance by **con-ron, NanoDa and the Lean default kernel**. The separate [source build and axiom-audit run](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/actions/runs/39103658555) also completed successfully for the registered commit.

| Verified input | SHA-256 |
| --- | --- |
| `PlanarBucklingChallenge.lean` | `92f8c376d384bdeb53cb09c9de868d743bfbd7fdc2ea04b3c25fae13f534d45b` |
| `PlanarBucklingSolution.lean` | `76863569c0628a3c096bdbfb9a6a4989cf16a57c623f0a6371af763d462f4f0a` |
| Palomar mechanical report | `a08f3cd0a35732ed71c1e2837904c0226c135693c7254a00309c0e443fb1023e` |

All 185 Lean source files in the registered snapshot were scanned after removing nested comments and strings. The only `sorry` tokens are the five deliberate specification placeholders in the isolated Challenge. No other Lean file in the submitted repository imports that Challenge, and none contains an `axiom`, `sorry`, `admit`, `native_decide`, `unsafe`, `implemented_by` or `extern` token. This source check supplements the transitive axiom gate; it does not substitute for kernel checking. The later manuscript revision `3b3417486b092363b411ed25ee2edb5e6f87f0ed` has byte-identical Lean sources, but the verification designation is pinned to the registered revision.

## Match to the original target

The independently inspected [scope review and source hashes](scope-review.json) preserve the canonical statement hash and identify the declarations read.

| AIM target | Formal definition or declaration | Comparison |
| --- | --- | --- |
| Bounded smooth nonempty planar domain | `Plane := EuclideanSpace ℝ (Fin 2)`; `polya_szego_buckling` | The theorem permits every open planar set of finite positive area, including the original domain class. |
| Clamped Sobolev space | `IsTestFn`, `h2Data`, `H02` | Closure of actual smooth compactly supported functions and their first and second derivatives in the product of genuine real L2 spaces. Its topology is the usual second-order Sobolev closure topology; smooth domains have both clamped traces. |
| Buckling Rayleigh quotient | `gradEnergy`, `laplEnergy`, `bucklingEig` | Laplacian squared norm divided by gradient squared norm, over nonzero gradient energy. The admissible class is nonempty, and no sign condition is imposed. |
| Disk with the same area | `BucklingChallenge.polya_szego_buckling` | Positive radius, equal area, and the actual disk buckling eigenvalue on the left. The theorem additionally proves exact disk rigidity. |

The challenge and solution repeat the same mathematical definitions. The solution proves `H02_eq` and `bucklingEig_eq`, linking those definitions to the proof objects. Compactly supported smooth functions and their derivatives are proved square integrable, so `toL2`'s zero fallback does not alter the Sobolev graph. The bump-function construction and density argument in `RequestProject/Core2.lean` establish nonempty admissible functions and the correct infimum. `H02_weak_gradient` identifies the derivative components.

No eigenfunction positivity, connectedness or additional topology assumption appears in the final theorem. An older intermediate theorem accepts `PaperExternals`; the reviewed final proof constructs that package using `faberKrahn_holds_without_E12` and `paperExternals_holds_without_E12`. It is not an unproved input to the public theorem. The result concerns the buckling quotient, rather than the different clamped-plate vibration quotient.

## Axioms and proof boundary

The five public targets are `area_inequality`, `area_equality_iff`, `polya_szego_buckling`, `bucklingEig_ball` and `buckling_ge_dirichlet`, all in namespace `BucklingChallenge`. The registered protected Comparator configuration selects all five and permits only:

```text
propext
Classical.choice
Quot.sound
```

The [successful report](mechanical-report.json) retains that protected configuration and the actual three-kernel acceptance transcript. The [submission audit](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/5311f47821b5da92e81e75b7da5091d176c8deb9/SubmissionSolutionAudit.lean) prints the full types and guards the exact three-axiom output for each public theorem. The [internal audit](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/5311f47821b5da92e81e75b7da5091d176c8deb9/UnconditionalAreaFinalAudit.lean) checks 14 proof roots in the same way. Their guards consume the expected axiom messages; the guard source alone is not treated as evidence of execution. The dated successful build and Palomar report provide that evidence and rule out `sorryAx` or custom unproved axioms in the selected proofs.

## Reproduction

On Linux with the registered Lean toolchain, its bundled Comparator/kernels and the sandbox prerequisites described in the upstream workflows, use a separate checkout of the pinned proof repository:

```sh
git clone https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar.git
cd polya-szego-planar-unconditional-palomar
git checkout 5311f47821b5da92e81e75b7da5091d176c8deb9
lake exe cache get
bash scripts/build-serial.sh
lake env lean UnconditionalAreaFinalAudit.lean
lake env lean SubmissionSolutionAudit.lean
bash scripts/verify-comparator.sh
```

The [pinned official workflow](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/5311f47821b5da92e81e75b7da5091d176c8deb9/.github/workflows/palomar-official.yml) invokes Palomar's full verifier and outer sandbox; its registered run is the mechanical evidence used here. We inspected these commands and records without executing the external build scripts in the AIM checkout. This is an external proof review, not a new AIM `research/lean/` project.

The informal [working manuscript v5](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/3b3417486b092363b411ed25ee2edb5e6f87f0ed/manuscript/PS_dim2_v5.pdf) remains a separate explanatory source. Formal verification establishes the pinned formal statements; it does not certify every line of that manuscript. Authors disclose ChatGPT assistance to the informal proof and Aristotle/Codex assistance to the formalization; the source license is Apache-2.0. AIM's additional statement review is by an AI assistant. The original problem ID, statement and editorial selection are unchanged.
