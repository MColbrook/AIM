# 833. A compact subset that cannot escape to infinity by homotopy

**Area:** Riemannian geometry and topology of noncompact manifolds
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a smooth connected noncompact boundaryless complete Riemannian $`n`$-manifold, $`n\ge2`$, of finite volume. Assume that $`M`$ is **tame**: it is homeomorphic to the interior of a compact manifold with boundary. Retain both sectional-curvature bounds
```math
-b^2\le\mathrm{Sec}_g\le0
```

for some finite $`b>0`$.

Must there exist compact subsets $`C,K\subset M`$ such that every continuous map
```math
H:C\times[0,1]\longrightarrow M,\qquad H(c,0)=c,
```

satisfies
```math
H(C,1)\cap K\ne\varnothing?
```

Thus the inclusion of some compact $`C`$ cannot be homotoped outside every compact set. The endpoint need not be an embedding, and the homotopy is not required to be an ambient isotopy. No particular dimension or loop structure is required of $`C`$.

## Application

The conjecture asks whether finite volume and bounded nonpositive curvature force some topological content to remain anchored in a compact region, even when individual loops can be moved arbitrarily far into the ends.

## References

1. G. Avramidi and T. T. Nguyễn-Phan, [*Examples of noncompact nonpositively curved manifolds*](https://doi.org/10.1112/blms.12484), *Bulletin of the London Mathematical Society* **53** (2021), 1061–1071, §4.4, Conjecture 9 and its footnotes. [Original preprint](https://arxiv.org/html/1711.03629), §5.5.
2. A. Pettet and J. Souto, [*Periodic maximal flats are not peripheral*](https://arxiv.org/html/0909.2899), Theorem 1.2; *Journal of Topology* **7** (2014), 363–384. [DOI](https://doi.org/10.1112/jtopol/jtt034).

## Status review


**Known cases:** Periodic maximal flats establish a nonperipheral compact subset in the locally symmetric case. Counterexamples to loop-only nonperipherality and examples without a uniform lower sectional bound do not refute this tame bounded-curvature compact-subset assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Periodic maximal flats establish a nonperipheral compact subset in the locally symmetric case. Counterexamples to loop-only nonperipherality and examples without a uniform lower sectional bound do not refute this tame bounded-curvature compact-subset assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Pettet and Souto establish the locally symmetric case using periodic maximal flats. The first source disproves an older loop-only conjecture but explicitly proposes this distinct compact-subset replacement. Its examples do not refute the replacement. The uniform lower curvature bound is essential; the source explains that removing it allows counterexamples.

The [primary and current-status review](../FURTHER_problems/_tracking/focused-nonperipheral-compact-core-Conj9-C208-Root-20261028/OWNER-EXACT-TAME-BOUNDED-CURVATURE-NONPERIPHERAL-COMPACT-SUBSET-PRIMARY-CURRENT-DUPLICATE-PROPOSAL.json) and [independent quantifier review](../FURTHER_problems/_tracking/focused-nonperipheral-compact-core-Conj9-C208-Root-20261028/C-INDEPENDENT-NONPERIPHERAL-EXISTS-C-K-ALL-H-TAMENESS-AND-LOWER-CURVATURE-MODEL-PEER-PASS.json) preserve tameness, curvature bounds and the precise homotopy quantifiers. Current-resolution and announcement searches and all-status semantic duplicate checks found no equivalent target or matching general resolution. This is a bounded status check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b883bd05c16749bb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
