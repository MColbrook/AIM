# AIM 1021: mixed continuous spectrum for a limit-periodic operator

**Author and submitter:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, United Kingdom. Email: [mjc249@maths.cam.ac.uk](mailto:mjc249@maths.cam.ac.uk). Affiliation and contact checked against the [department profile](https://www.damtp.cam.ac.uk/person/mjc249) on 3 November 2026.

**AIM outcome:** Solved — Counterexample, following the documented [independent AI mathematical review](../../solution_reviews/2026-11-03-aim1021/1021-review.md).

The proof constructs a bounded real limit-periodic discrete Schrödinger operator with nonzero absolutely continuous and singular continuous spectral subspaces and no eigenvalues. Both continuous types are visible in the spectral measure of the same vector. This answers [AIM 1021](../../../problems/1021-must-limit-periodic-discrete-schrodinger-operators-have-pure-spectral-type.md), Damanik–Fillman Question 10.1, negatively. The distinct hull-element and coupling questions are not claimed to be resolved.

- [Proof PDF](limit_periodic_mixed_spectrum.pdf) and [editable TeX](limit_periodic_mixed_spectrum.tex).
- [Full mathematical review and target comparison](../../solution_reviews/2026-11-03-aim1021/1021-review.md).
- [Reproduction instructions](REPRODUCTION.md), [exact checker](verify_identities.py), and its [normal](identity_checks_normal.txt) and [optimized](identity_checks_optimized.txt) output.
- [Original submission and final-file receipt](SOURCE_RECEIPT.json), [source changes](source_changes.diff), and [package checksums](MANIFEST.sha256).

Codex (AI) read and checked the complete submitted argument, independently re-derived its central estimates, checked the primary references, and added supporting symbolic checks. This does not assert human peer review or Lean verification. The construction is an existence proof; the infinitely many periods and amplitudes are chosen recursively rather than supplied as a finite numerical potential.

The original submitted file is preserved in the submitter's Downloads folder. Its SHA256 is recorded in the receipt. The packaged source adds the requested author, a suitable title, precise repository and reference links, and an explanation of the optional reflectionless-spectrum remark. Its construction and central proof are unchanged.
