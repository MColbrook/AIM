# AIM 571 independent computational acceptance review

Date: 21 October 2026. Supplement: [PR 176](https://github.com/MColbrook/AIM/pull/176), pinned head `3cc0f979cb475aeacc120e0523897a9786da1850`. The original proof was submitted in [PR 122](https://github.com/MColbrook/AIM/pull/122). Review by independent OpenAI Codex contexts and the coordinating maintainer session; no human peer review or Lean verification is claimed.

## Decision and exact target

**Decision:** Solved. The independent fresh replay completes the outstanding computational acceptance gate for the exact all-parameter AIM571 target.

The target counts all two-dimensional half-integral polygons, including integral ones, with each prescribed number of collinear interior lattice points at least three. Equivalence uses unimodular integer linear maps and integer translations. The exact degree-seven formula and all-parameter quantifier are unchanged.

The [earlier complete argument review](../2026-10-15-active-prs/571-review.md) reconstructed the geometry, normalization, finite cell decomposition, fixed-class equations and exact algebra, but independently replayed only 12 of 608 systems. The [new proof and supplement audit](176-proof-review.md) rechecks the unchanged original material and the new driver. All 17 original package files match the accepted bytes exactly. The new supplement introduces no altered theorem or mathematical input.

## Independent execution

All **608/608 distinct systems**, covering **618/618 original cell members**, were freshly computed with **zero reused cached results and zero failures**. The run used PyNormaliz 2.24 on Linux x86-64 with Python 3.10, sixteen separate single-threaded workers, the unchanged `HilbertSeries`, `BigInt`, `NoGradingDenom` options, and a 3600-second per-system limit. The controller completed in 926.38 seconds. Both the output directory and exported bundle pass the standalone checker. All complete rational functions, original gradings, four action sums, Burnside identity and the degree-seven polynomial identity match.

The worker receives only the exact input constraints, grading, timeout and computation options. It independently constructs a Normaliz cone and requests the complete Hilbert series and grading; expected answers stay in the controller. Every result is compared as an entire rational function with its original grading, rather than through a finite initial coefficient sample. Full reaggregation then checks all four action sums, Burnside's identity and the polynomial coefficient identity.

The [independent execution bundle](571-independent-replay-bundle.json) preserves every completed result and its hash/context binding. The [execution summary](571-independent-replay-summary.json) records the actual environment and coverage. The unchanged input export has SHA-256 `bd22e0775a0475fe485349483dec748c0045fa3b4e2b0f066a716a3b031bdc21`. The standalone checker validates all required results, inputs, gradings, full rational outputs and computed-output algebra.

## Additional checks

The submitted author-side execution bundle passes its standalone consistency checker. The seven original geometry/export tests and eleven supplement receipt/cache/failure tests pass. Their synthetic fixtures test the checker and process accounting; they are not counted as independently executed Normaliz systems. The acceptance decision relies on the separate maintainer-side fresh execution described above.

The normal form, strict lattice inequalities, residual four-element symmetry group, cell multiplicities, original unit grading, full rational identities and polynomial coefficient extraction were compared with the exact problem. The published [Bohnert–Springer paper](https://doi.org/10.1007/s00454-026-00822-0), Proposition 3.5 and Conjecture 3.7, supplies the geometric strip reduction and still poses the all-parameter formula. Its finite verified range and later finite classifications are distinguished from a full proof. A dated primary-source search found no earlier matching all-parameter resolution; the proof audit records the search limits.

## Trust boundary

This is a computer-assisted analytic and exact-enumeration result. The independent run completes the previously outstanding reproduction gate while continuing to trust Normaliz and its native arithmetic dependencies, together with ordinary hardware/runtime correctness. It does not supply a second enumeration algorithm, independently checked simplicial decomposition certificates, a formally verified counting kernel, or human peer review. The prior review remains available as the historical verification boundary.
