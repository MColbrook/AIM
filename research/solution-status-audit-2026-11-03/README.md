# Individual solution-status audit

Started 3 November 2026. All 912 current local non-solved entries are in scope, including existing complete solution claims for scope/current-status checking. Cut entries are excluded. Local IDs and problem statements are preserved; FURTHER_problems and PROBLEM_SCORING receive no writes. No commit, push, pull or fetch.

The user explicitly requests Solved for a complete matching announced solution; such entries say that the proof is an unverified announcement. This does not claim independent proof or Lean verification. Partial results do not settle the full remaining problem.

## Coverage — individual bounded searches finished

At 2026-11-03T14:17:13.175436+00:00, all 912 targets have individual bounded search records, with no unreviewed targets. This completes the individual search pass, not exhaustive source coverage or independent certification of the claimed proofs. See [progress.json](progress.json) and [manifest.json](manifest.json).

Two source-comparison limits remain explicit: AIM 368's older Schneider theorem body was unavailable (its advertised scope is a restricted subclass), and AIM 962's original Coron book could not be freshly recovered. Their pages remain unresolved. Abstract-level exclusions and publication/preprint parity limitations are identified in the individual records.

## Newly located complete announcements

- [AIM 007 — Pólya–Szegő conjecture for the first buckling load](../../problems/007-buckling-load-ball.md) — [scope check](lane-a/007.json).
- [AIM 083 — The bulk ground-state energy of the planar Lennard–Jones system](../../problems/083-lennard-jones-planar-crystallization.md) — [scope check](lane-a/083.json).
- [AIM 097 — Simon’s multidimensional weighted square-integrability conjecture](../../problems/097-simon-weighted-l2.md) — [scope check](lane-a/097.json).
- [AIM 410 — Quadratic-growth rigidity for the complex Monge–Ampère equation](../../problems/410-complex-monge-ampere-quadratic-growth.md) — [scope check](lane-b/410.json).
- [AIM 436 — Radial classification of higher-degree entire planar Ginzburg–Landau vortices](../../problems/436-entire-ginzburg-landau-vortex-symmetry.md) — [scope check](lane-b/436.json).
- [AIM 439 — Interior bounds for stable elliptic states with sign-changing reaction laws](../../problems/439-stable-semilinear-sign-changing-interior-bound.md) — [scope check](lane-b/439.json).
- [AIM 567 — Perfect Lee codes beyond dimension two](../../problems/567-golomb-welch.md) — [scope check](lane-b/567.json).
- [AIM 579 — Can a Heisenberg surface be more than one-half Hölder?](../../problems/579-can-a-heisenberg-surface-be-more-than-one-half-holder.md) — [scope check](lane-b/579.json).
- [AIM 1026 — Steklov zeros in a fixed boundary collar](../../problems/1026-steklov-zeros-in-a-fixed-boundary-collar.md) — [scope check](lane-d/1026.json).

## Existing complete claims checked

The following 27 entries already recorded complete solution claims. They are now labelled Solved under the user's announcement policy, with the unverified qualification retained on each page. They are not newly discovered solutions.

[030](../../problems/030-sic-povms.md), [044](../../problems/044-sparse-linear-solve-bit-complexity.md), [092](../../problems/092-kls-poincare.md), [098](../../problems/098-maximal-molecular-ionization.md), [108](../../problems/108-critical-catenoid-uniqueness.md), [110](../../problems/110-steklov-bulk-nodal-volume.md), [111](../../problems/111-steklov-fixed-boundary-multiplicity.md), [123](../../problems/123-sard-conjecture-endpoint-map.md), [125](../../problems/125-equiregular-analytic-nonbranching.md), [126](../../problems/126-pansu-heisenberg-isoperimetry.md), [175](../../problems/175-percolation-preserves-transience.md), [195](../../problems/195-laughlin-gap.md), [214](../../problems/214-bilu-linial-signing.md), [250](../../problems/250-periodic-triangular-billiard.md), [298](../../problems/298-li-li-multiple-unicast.md), [330](../../problems/330-sharp-matroid-secretary.md), [338](../../problems/338-polynomial-local-stability-decidability.md), [340](../../problems/340-integer-three-sum-hardness.md), [342](../../problems/342-entanglement-of-purification-additivity.md), [348](../../problems/348-brownian-fleming-viot-nonexplosion.md), [361](../../problems/361-one-dimensional-convex-entropy-nonuniqueness.md), [392](../../problems/392-polyhedral-transport-singular-interface.md), [393](../../problems/393-polyhedral-partial-transport-free-boundary.md), [394](../../problems/394-villani-mtw-convex-injectivity-domains.md), [412](../../problems/412-positive-transport-sharp-uniform-control-time.md), [446](../../problems/446-beurling-ahlfors-sharp-norm.md), [462](../../problems/462-nonlocal-pucci-finite-integrability-abp.md).

## Requested author searches

The current arXiv math author listing for Colbrook M J returned 62 unique entries over two pages. Zenodo's requested Matthew Colbrook creator query returned 18 records. AIM 083's complete matching announcement was found here; the other entries were routed by mathematical statement, not by historical IDs. The listings and body-level AIM 083 scope check are retained locally. These author listings do not constitute a proof audit of every listed work.

## Other source findings

AIM 091's older Hueter claim has an unjustified transfer between weak and strict self-avoidance in Corollaries 1–2, pp. 27–28. A separate review supplied an explicit countermodel to the quoted limit inference. The page cites the claim and explains the gap; it remains open.

AIM 901's source question locator is 4.7. AIM 902's common perturbations occur inside the square root; the decay restriction and independent-sequence distinction are now stated accurately. Both remain partial and both problem statements are unchanged.

AIM 807's source locator, AIM 957's strict contrast bound, the AIM 189 erratum, AIM 213's current title and AIM 201's near-critical partial result were corrected or added without changing their problem statements. AIM 568 now cites the October bound and explains the unresolved measurability mismatch; it remains partial. AIM 782's existing explicit obstruction to the claimed proof remains in place.

AIM 579 is especially preliminary: its authors explicitly say the proposed calculations have not been verified by the human authors and the manuscript is not ready for arXiv. Its Solved label records the editor-requested announcement convention only.

## Validation

The catalogue-only check and cut/score verifier pass: 1067 kept identities and 329 cut identities, including all local IDs, are preserved. All 912 original titles and problem-statement hashes are checked. Thirty-three targeted presentation, number-allocation, mathematical-formatting and evidence-chain regression tests pass. Generated indexes have been rebuilt.

The broader legacy integration-test fixture omits the cut/archive tree from its disposable copy, so its baseline fails on missing cut/archive records; it is not reported as passing. The actual repository's catalogue-only and frozen-selection checks pass. The archive verifier now applies the existing dated-content hash chain consistently to reused-ID promotions, preserving the original title and statement checks.

FURTHER_problems protected-file hashing is not repeated because the main research thread may write there. This audit does not write to FURTHER_problems or PROBLEM_SCORING and makes no commit, push, pull or fetch.
