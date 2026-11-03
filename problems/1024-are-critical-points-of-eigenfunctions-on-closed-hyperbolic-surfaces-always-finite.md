# 1024. Are critical points of eigenfunctions on closed hyperbolic surfaces always finite?

**Area:** Spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(S,g)`$ be a compact hyperbolic surface without boundary, with Gaussian curvature $`-1`$. Let $`u`$ be a nonconstant real Laplace eigenfunction,
```math
-\Delta_g u=\lambda u,\qquad \lambda>0.
```

Is its full critical set
```math
\mathrm{Crit}(u)=\{x\in S:du(x)=0\}
```

always finite?

This is the compact-surface conjecture in [1, Remark 9.6]. The qualifier $`\lambda>0`$ makes explicit the authors' implicit nonconstant-eigenfunction convention: the zero-eigenvalue constant eigenfunctions have the whole surface as their critical set. The question concerns **all** critical points, including those where $`u\ne0`$; it is stronger than finiteness of singular points of the nodal set $`u^{-1}(0)`$.

## Application

The critical set of a base-surface eigenfunction controls the zero set of a related weight-two eigenfunction on the unit tangent bundle in the constant-curvature Kaluza–Klein construction [1, Remark 9.6]. Its finiteness would rule out critical curves in that closed-surface setting and clarify the topology of lifted nodal sets.

## Known results

Jung and Zelditch explain why a local curvature argument is insufficient: rotationally invariant Dirichlet or Neumann eigenfunctions on a compact **submanifold with boundary** of a hyperbolic cylinder can have circles of critical points [1, Remark 9.6]. That example does not meet the closed, boundaryless hypothesis here. Their nearby Theorem 9.5 concerns isolated zeros for certain cusp forms on the noncompact modular surface and does not settle the conjecture. The classical nodal-set theory gives isolated critical points **on the zero level** of a nontrivial eigenfunction on a surface [2, Theorem 2.1], but leaves open whether critical curves can occur at a nonzero level on a closed hyperbolic surface.

## References

1. J. Jung and S. Zelditch, [*Boundedness of the number of nodal domains for eigenfunctions of generic Kaluza–Klein 3-folds*](https://aif.centre-mersenne.org/item/10.5802/aif.3329.pdf), *Annales de l'Institut Fourier* **70** (2020), no. 3, 971–1027, Section 9.3 and Remark 9.6, printed p. 1024. [DOI](https://doi.org/10.5802/aif.3329).
2. S. Mondal, [*On largeness and multiplicity of the first eigenvalue of hyperbolic surfaces*](https://sugatareading.github.io/reading-homepage/First%20Eigenvalue.pdf), *Mathematische Zeitschrift* **281** (2015), 333–348, Theorem 2.1 (the classical local result for critical points lying on a nodal zero set).

## Status review


**Known cases:** The full critical set at nonzero levels is required for every nonconstant eigenfunction. Finiteness of nodal singularities, generic eigenfunctions and bounded-domain theorems do not establish it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The full critical set at nonzero levels is required for every nonconstant eigenfunction. Finiteness of nodal singularities, generic eigenfunctions and bounded-domain theorems do not establish it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-body, convention, later-work and semantic-duplicate review](../FURTHER_problems/_tracking/hyperbolic-eigenfunction-critical-set-status-2026-10-21.json) checked the exact closed-surface statement and distinguished bounded-domain, zero-level and generic-eigenfunction results. No complete proof, counterexample or announcement for the universal positive-eigenvalue claim was located through 21 October 2026 in that bounded search.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a3ce1d13feb0c67d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
