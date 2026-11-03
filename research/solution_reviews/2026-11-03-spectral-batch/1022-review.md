# AIM 1022: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Counterexample.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1022-additive-intersection-index-counterexample/aim1022.pdf), [TeX](../../solutions/1022-additive-intersection-index-counterexample/aim1022.tex), and [source receipt](../../solutions/1022-additive-intersection-index-counterexample/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1022](../../../problems/1022-can-intersection-complexity-be-separated-from-eigenvalue-growth.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

Smooth embedded hypersurfaces violate every proposed dimension-only additive separation of intersection index and eigenvalue growth.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1022: independent mathematical audit

Date: 3 November 2026. Reviewer: Codex AI, lane b. Author and submitter: Matthew J. Colbrook. This review is independent AI checking, not human peer review or formal verification.

Repository target inspected at HEAD 3fa50884d129a08fec3c09cb4765e8ecad97d6ee: problems/1022-can-intersection-complexity-be-separated-from-eigenvalue-growth.md and the ID 1022 row of data/spectral.json. The supplied source snapshot is b014a51815ffd025d2b1abc4a3954205dfbf61e0.

## Verdict and target comparison

**PASS: a complete negative answer to the current problem. No fatal mathematical gap found.** I checked all sections 0 and A-H, rather than accepting the archive's completeness label. The target uses the induced metric on a smooth, compact, connected, boundaryless, embedded hypersurface, finite transverse-line intersection index, all n>=2, and a dimension-only coefficient multiplying k^(2/n). The construction supplies precisely those objects. It does not merely exclude a prescribed Weyl coefficient.

The argument supports status Solved with outcome disproved under CONTRIBUTING.md's documented-independent-audit provision, once the proof and an explicit AI audit record are integrated. The current ID should be preserved.

## Sensitive steps reconstructed

### 1. High-gap embedded input and definable approximation

The external existence input has the required codimension and embeddedness. Theorem 1.4(1) supplies embedded surfaces in R^3 with unbounded normalized first eigenvalue; part (2), with codimension one, supplies the higher-dimensional input and permits a fixed sphere topology. It is not only an immersion theorem.

The polynomial replacement is valid. Take a signed tubular coordinate rho and two fixed boundary sheets where it has opposite nonzero signs. C^2 polynomial approximation preserves the normal derivative and these signs. The intermediate value theorem and strict normal monotonicity produce a unique nearby normal graph; the nonzero signs prevent its component from escaping the tube. A compact connected component of a real polynomial zero set is semialgebraic. Uniform convergence of the induced metrics follows from C^1 convergence of the embeddings, and comparison of the Rayleigh quotients and volume densities gives spectral and volume convergence.

If the original normalized quantity is T=lambda_1 Vol^(2/n), dilation by sqrt(lambda_1) produces lambda_1=1 and volume V=T^(n/2). Thus V really can be chosen arbitrarily large before the replication number N is sent to infinity.

### 2. Length-independent handle spectral count

For p=(n-1)/2, writing w=r^p and psi=wf, expansion and integration by parts for zero endpoint traces give

```math
\int w^2|f'|^2=\int \left(|\psi'|^2+\frac{w''}{w}|\psi|^2\right).
```

The displayed potential is correct:

```math
\frac{w''}{w}=a^2\left(p\,\mathrm{sech}^2+p^2\tanh^2\right)
\ge a^2\min(p,p^2).
```

The endpoint-zero form domain has codimension two in H^1(0,L). Equivalently, any three-dimensional low-energy spectral subspace would have a nonzero element satisfying both endpoint conditions, a contradiction. This justifies the third-Neumann-level bound even though endpoint traces are not L^2-continuous functionals.

The q-metric comparison costs at most Q^2, with Q^2<=1+a^2 epsilon^2. Nonconstant angular sectors have energy at least (n-1)/epsilon^2. Consequently at most two full handle eigenvalues lie below 1/2 after fixing a and taking epsilon small, uniformly for arbitrarily long L. For example a=2 already makes the potential at least 1 in every n>=2, and sufficiently small epsilon preserves a gap above 1/2.

The volume bound follows by integrating the two decaying end profiles. It has no hidden factor L. The argument does not incorrectly assign a uniform gap to an ordinary long constant-radius cylinder.

### 3. Per-handle and total line intersections

The identity r^2 being a constant multiple of 1+cosh(2a(s-L/2)) implies (r^2)''''>0. For a line with varying axial coordinate, the intersection equation is a quadratic polynomial minus r^2, whose fourth derivative never vanishes. Five distinct roots are impossible. A constant-axial-coordinate line intersects one spherical cross-section in at most two points. The bound four is valid, including possible endpoint overcounting.

The incidence dimension calculation for five vertex-disjoint segments is correct. For a fixed line in R^m, endpoint pairs admitting a segment-line intersection have dimension at most m+2: parameterize an intersection point, an interior segment parameter, and one endpoint; endpoint incidences have smaller dimension. Five independent endpoint pairs and a line parameter of dimension 2m-2 therefore give codimension at least 3m-8>0 for m>=3.

A set of nine edges of a path has a matching of size at least five. Thus a generic finite chain has no common line transversal to nine edges. No three collinear vertices gives the analogous vertex statement. These conditions can all be imposed inside the open set of increments in a small common cone and lengths in (1,2).

The robustness assertion is legitimate for each finite N: unoriented line directions form a compact projective space, and a line meeting a bounded set has bounded perpendicular offset. A limiting transversal to shrinking neighborhoods would be a forbidden core transversal. The resulting margins may depend very badly on N; this is harmless because the construction permits a fresh large dilation for each N.

### 4. Actual ports and embedding

A direction with unique support maximum and minimum and with both signs regular for the Gauss map exists by the two full-measure conditions stated in the submission. Nondegeneracy at a support extremum makes the outward second fundamental form positive definite. The local Gauss inverses can be chosen analytic and semialgebraic.

The recursion for translations joins the actual outgoing and incoming ports by exactly the intended straight segment. Its accumulated displacement from the prototype is O(N) with fixed-base constants. Taking R sufficiently large for that finite N preserves the incidence margins.

In addition to the explicit transversal conditions, the stated genericity gives positive distances between nonincident edges and vertex centers, and between nonadjacent edges. Dilation makes these clearances exceed the fixed base-ball radius. At a shared copy, incoming and outgoing rays leave through the opposite support patches and point into opposite narrow cones. With small epsilon their collars and adjacent tubes are disjoint. These observations validate the asserted global embeddedness, not just the line-count bound.

### 5. Collars and uniform definable complexity

At t=0 the collar has rho=2 epsilon and agrees with the base on a radial annulus. At t=1 it has z=epsilon, rho=r(0)=epsilon and agrees with the analytic continuation of the actual tube near s=0. Thus it has the right seams and all derivatives match.

For the unperturbed profile, at least one of eta'(t) and eta'(1-t) is positive, so the tangent never vanishes. Its radius is monotone and its axial coordinate is monotone. The base graph contributes O(epsilon^2), and the tube correction contributes O(a epsilon^2), with the same bounds after one parameter derivative. After scaling by epsilon these are small C^1 perturbations of a fixed compact embedded annular cylinder. This preserves embedding and gives the uniform scaled trace/Poincare constants used later. The retained base has projected radius at least 2 epsilon; the collar is inside that deleted disk except at the common boundary.

The flat cutoffs built from piecewise exp(-1/t) are C-infinity and definable in R_an,exp. The construction never takes an integral of a definable function. The fixed algebraic component, semialgebraic local charts and rotations, exponential tube profile, two port directions and two length parameters together form one finite-parameter definable family. Translation can be absorbed into the line parameters.

Uniform bounds on fiber connected components apply to all these parameters, even unbounded length parameters. A transverse line has only isolated intersections with the final smooth surface, so a fiber-component bound bounds its point count. Since one line meets at most two base balls and eight handle neighborhoods,

```math
i(\Sigma_N)\le 2C(B)+8\cdot4
```

is genuinely independent of N and epsilon. The complexity of B may be arbitrarily large; it is fixed before taking N to infinity.

### 6. Neumann convergence of the small modified base

The local geometry added to each punctured base has intrinsic size O(epsilon) and uniformly controlled geometry after scaling. An extension from a retained annulus into the deleted disk can preserve constants and bound the gradient seminorm uniformly. This can be seen by subtracting the annular average, applying a fixed scaled extension, and adding the average back.

The two scaled trace estimates imply exactly the submission's F2. For a bounded-energy, bounded-L^2 family, the extensions are bounded in H^1 on the fixed base. Rellich compactness yields strong L^2 convergence there; therefore the mass on shrinking annuli vanishes. F2 then forces the collar mass to vanish as well. There is no extra localized low mode on a collar.

For the energy liminf, take the fixed complement of port balls of radius delta first, and only then let delta decrease to zero. This avoids any unjustified assertion that the energy of the artificially filled disk tends to zero. Orthonormality survives because collar mass vanishes. Smooth test functions with bounded collar extensions give the matching upper eigenvalue limit. This reasoning works in n=2 as well. Only finitely many ports occur for each N, so simultaneous epsilon choices require no convergence rate uniform in N.

### 7. Bracketing, indexing, and quantifier order

Each modified base has precisely one eigenvalue below 1/2, and each of the N-1 handles has at most two. The disconnected Neumann problem therefore has at most 3N-2 eigenvalues strictly below 1/2. Its form domain is larger than that of the glued closed surface. With zero-based indexing this gives lambda_(3N-2)(Sigma_N)>=1/2, not an off-by-one upper bound.

The base pieces alone provide volume at least NV/2. Under the proposed bound, divide the resulting inequality by N^(2/n). The fixed additive term tends to zero; the limit forces

```math
\tfrac12(V/2)^{2/n}\le A_n 3^{2/n}.
```

The choice order is correct: assume A_n,F_n exist; choose a high-gap base with V violating this inequality; fix that base and its index-complexity bound; then let N grow. F_n is allowed arbitrary dependence on the large fixed index and still cannot avoid the contradiction.

The continuity-free strengthening is valid because finite intersection indices are integers in a fixed finite set. The fixed-sphere-topology strengthening for n>=3 is also valid: algebraic approximation preserves the sphere, and the chain gluing is the ordinary connected sum of spheres, with no gluing twist introducing an exotic sphere.

## Gaps and proposed refinements

No required mathematical repair was identified.

Two optional documentation refinements would make later review easier:

1. Cite an exact uniform-fiber theorem rather than leaving [3] at the level of a general consequence. The primary author manuscript of van den Dries-Miller below has Section 4.4, PDF p. 13, with exactly the required uniform bound. Its unrelated warning about a gap in a Whitney-stratification proof does not affect Section 4.4.
2. State explicitly that the large R also handles edge-versus-nonincident-base clearances and that incoming/outgoing ports lie in opposite support caps. Those facts already follow from C-D and the narrow-cone construction; they do not require a new construction.

## Verified primary sources and dated relevance check

- Colbois-Dryden-El Soufi, [primary preprint](https://arxiv.org/pdf/0909.5346), Theorem 1.4(1)-(2), PDF/printed p. 6; Section 5, pp. 14-15 checks the smooth embedded formulation. [Journal DOI](https://doi.org/10.1112/blms/bdp100). The stated hypersurface high-gap input and the n>=3 fixed-topology option match.
- van den Dries-Macintyre-Marker, [primary published text](https://www.math.ens.psl.eu/~zchatzid/papiers/o-min-21/DMM.pdf), Corollary 5.13, printed p. 204, PDF p. 23 including cover: R_an,exp is o-minimal. [DOI](https://doi.org/10.2307/2118545).
- van den Dries-Miller, [author's revised primary manuscript, Geometric categories and o-minimal structures](https://people.math.osu.edu/miller.1987/newg.pdf), Sections 4.2 and 4.4, PDF pp. 12-13. Section 4.4 bounds the number of connected components of every fiber of a fixed definable set, with no parameter-compactness assumption. This is a more precise supporting citation for E than the submission's general [3].
- Petiard, [original primary preprint](https://arxiv.org/pdf/1706.09189), p. 3, poses the additive intersection-index question. Its isoperimetric-ratio counterexample does not itself resolve this target.
- Colbois-Girouard, [primary v2](https://arxiv.org/pdf/2108.03101), Corollary 4, p. 4, and Corollary 12, p. 7, retain packing/growth or diameter/injectivity quantities; they do not furnish the target's dimension-only additive separation.

Bounded searches on 3 November 2026 included the phrases intersection index/additive/eigenvalues/Petiard, later metric upper bounds, and 2026 intersection-index spectral work. No matching published resolution of the additive target was located. This is not a proof of priority or an exhaustive literature certificate. The negative verdict above rests on the supplied proof and the verified inputs.

## Standalone reference completion

The final manuscript explicitly cites Pétiard's original additive question, with its page locator, and the precise uniform-fiber theorem used in the construction. These additions do not change the proof or verdict.
