# Colbrook's Palomar registrations and the current AIM catalogue

Reviewed on 3 November 2026 against AIM commit `18c719282b7425409f415df5273c1636d5c1511d`.

**Result: six registrations checked; no additional current AIM problem qualifies for Lean verified.** The current problem pages, IDs, statements and statuses remain unchanged. AIM 007 remains the collection's one Lean-verified entry.

The complete [current author query](https://data.palomar-registry.org/api/v1/results?q=Colbrook), registry revision 738, returned six entries with no next page. Each names Matthew J. Colbrook as an author. All six immutable registrations report successful mechanical verification. We downloaded their independent Challenge specifications, solution entry points and mechanical reports, and matched their SHA-256 hashes to the registration records. The [audit receipt](audit.json) retains the pins, selected theorem names, dependency versions, verification URLs, report hashes and individual comparisons.

## Results

| Registration and result | Comparison with the current collection |
| --- | --- |
| [Affine reverse Faber–Krahn](https://palomar-registry.org/entry?id=PALOMAR-2026-11-01-000009&version=1) | Related to the historical reverse Faber–Krahn identity formerly numbered 106. Today's [AIM 106](../../../problems/106-payne-dirichlet-buckling-comparison.md) is Payne's all-index Dirichlet–buckling comparison, which the registered first-Dirichlet-eigenvalue estimates do not state. |
| [Spectral isometries of C*-algebras](https://palomar-registry.org/entry?id=PALOMAR-2026-10-28-000031&version=1) | The subject matches the unnumbered historical candidate **FURTHER-09af6d42534bd94c**, rather than a current numbered AIM entry. |
| [Kroó's conjecture](https://palomar-registry.org/entry?id=PALOMAR-2026-10-27-000004&version=1) | The subject matches the unnumbered historical candidate **FURTHER-4777013998884f03**. All thirteen principal approximation/quadrature statements and their conjunction were considered; none states a current AIM target in full. |
| [Crown graph representation numbers](https://palomar-registry.org/entry?id=PALOMAR-2026-10-22-000009&version=1) | No current AIM target for this uniform-word graph invariant or crown extremality was located. |
| [Unrestricted Eden conjecture](https://palomar-registry.org/entry?id=PALOMAR-2026-09-22-000001&version=1) | The explicit five-dimensional polynomial-flow counterexample does not settle [AIM 147](../../../problems/147-navier-stokes-inertial-manifold.md), which asks for inertial manifolds for every forced two-dimensional Navier–Stokes system. |
| [Kung–Traub conjecture](https://palomar-registry.org/entry?id=PALOMAR-2026-09-20-000006&version=1) | No current scalar analytic root-finding-order target was located. The twelve registered statements use a different oracle and conclusion from [AIM 527](../../../problems/527-arbitrarily-slow-strong-approximation-of-a-smooth-scalar-stochastic-equation.md)'s scalar stochastic-equation sampling problem. |

The [editorial identity register](../../../catalogue.json) already distinguishes the former reverse Faber–Krahn entry from its replacement and records the two unnumbered historical candidates. This review does not reinstate any of them or allocate an ID.

## Nearby statements checked

The affine theorem's information-dependent result M03 **assumes** a Poincaré bound and concludes a Dirichlet eigenvalue estimate. It does not prove the dimension-free Poincaré inequality of [AIM 092](../../../problems/092-kls-poincare.md). Its Fisher-information definitions and Euclidean Sobolev framework also do not state the smooth compact-manifold score-gradient approximation requested in [retained AIM 665](../../resolved/665-fisher-score-gradient-closure.md). The magnetic Neumann problem [103](../../../problems/103-magnetic-neumann-disk.md), sharp superhomogeneous inradius lower bound [1016](../../../problems/1016-the-sharp-inradius-bound-for-superhomogeneous-dirichlet-frequencies.md), and sharp eigenvalue–torsion constants [1028](../../../problems/1028-sharp-convex-polya-functional-bounds-in-dimensions-three-and-higher.md) have different operators, normalizations or conclusions.

Kroó's finite-dimensional convex-boundary approximation theorem does not establish the infinite-dimensional Banach-space isomorphism in [AIM 931](../../../problems/931-do-isomorphic-duals-determine-homogeneous-polynomial-spaces.md), the Schatten-class conclusion in [036](../../../problems/036-arveson-douglas.md), or the spherical-mean classification in [058](../../../problems/058-spherical-mean-noninjectivity-sets.md). Its supporting density, Fourier cutoff and quadrature results do not give the sharp unrestricted approximation lower bounds in [522](../../../problems/522-sharp-uniform-approximation-of-lipschitz-functions-by-shallow-relu-networks.md) or [664](../../../problems/664-sharp-uniform-approximation-widths-for-small-mixed-holder-smoothness.md). Neither those statements nor the Kung–Traub root-finding bounds establish the specific high-dimensional integration-complexity result in [556](../../../problems/556-smooth-integration-dimensional-curse.md).

## Scope and reproducibility

We indexed the titles and canonical statements of all **1,058 current problem pages and nine retained numbered records**, then compared the six complete registered specifications and individually read the nearby AIM targets identified above. The receipt records the source revision, catalogue identity/statement digest, hashes of those target pages, and the exact declarations reviewed. It distinguishes direct statement comparisons from keyword routing.

The `Challenge` files contain deliberate specification placeholders. Their existence is not evidence of a proof: the separate registered solution and the hash-matching passing mechanical report are the relevant external evidence. Only `propext`, `Classical.choice` and `Quot.sound` are permitted by these registrations. We relied on Palomar's mechanical verification, as requested by the editor, and performed no new local Lean replay. The review is AI-assisted and claims no independent human peer review.

This is a bounded comparison of the **registered benchmark statements**, including all configured public targets. It does not exclude an additional implication requiring a new mathematical argument or an unregistered auxiliary result elsewhere in those repositories. Downloaded source copies stay in the ignored local cache; the receipt links their immutable originals. No files in `FURTHER_problems/`, `PROBLEM_SCORING/` or `cut_problems/` were edited.
