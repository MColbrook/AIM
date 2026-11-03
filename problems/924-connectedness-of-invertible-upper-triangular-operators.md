# 924. Connectedness of invertible upper-triangular operators

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`H=\ell^2(\mathbb N_0;\mathbb C)`$ with standard basis $`(e_j)`$, set $`E_n=\mathrm{span}\{e_0,\ldots,e_n\}`$, and define

```math
\mathcal A=\{T\in\mathcal B(H):T(E_n)\subseteq E_n\text{ for every }n\ge0\}.
```


This is the unital Banach algebra of bounded upper-triangular operators. Is its group

```math
GL(\mathcal A)=\{T\in\mathcal A:\exists S\in\mathcal A,\ ST=TS=I\}
```


connected in the operator-norm topology? Equivalently, for every $`T\in GL(\mathcal A)`$, does there exist a norm-continuous path $`G:[0,1]\to GL(\mathcal A)`$ with $`G(0)=I`$ and $`G(1)=T`$? The equivalence follows because the invertible group of a Banach algebra is open and locally path connected. No uniform path length or common inverse bound is required.

This is Problem1 in [1, Chapter25]. Remark2.3 of [2] reduces the corresponding question for arbitrary nest algebras to this standard atomic case.

## Application

The problem tests whether every invertible operator preserving a fixed hierarchy of finite-dimensional coordinate spaces can be continuously deformed to the identity while preserving that hierarchy and invertibility. It concerns the topology of structured infinite-dimensional linear transformations.

## References

1. K. R. Davidson, *Nest Algebras: Triangular Forms for Operator Algebras on Hilbert Space*, Pitman Research Notes in Mathematics **191**, Longman Scientific & Technical, 1988, Chapter25, Problem1, printed pp.391–392. [Author’s book page and copy](https://www.math.uwaterloo.ca/~krdavids/nestbook.html).
2. K. R. Davidson, J. L. Orr and D. R. Pitts, [*Connectedness of the Invertibles in Certain Nest Algebras*](https://doi.org/10.4153/CMB-1995-060-6), *Canadian Mathematical Bulletin* **38**(4) (1995), 412–420, Theorem2.1, Corollary2.2 and Remark2.3.
3. Y. Ji and Y. Zhang, [*On the connectedness of the invertibles in nest algebras and related problems*](https://doi.org/10.1360/SSM-2020-0167), *Scientia Sinica Mathematica* **50** (2020), 1773–1782. The primary abstract and reference list were inspected; its full text was inaccessible in this check.

## Status review


**Known cases:** The atomic standard nest has infinitely many rank-one atoms. Width restrictions and no-isolated-finite-rank-atom connectedness results do not cover it; the 2020 survey still treats the problem. Kadison-Singer is not by itself an established implication here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The atomic standard nest has infinitely many rank-one atoms. Width restrictions and no-isolated-finite-rank-atom connectedness results do not cover it; the 2020 survey still treats the problem. Kadison-Singer is not by itself an established implication here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

A [source, current-result and semantic review](../FURTHER_problems/_tracking/focused-Nest-Algebras-Q1-Q2-C278-C-20261029/ROOT-FINAL-TWO-EXACT-NEST-SOURCE-CURRENT-AND-SEMANTIC-REVIEWS.json), checked29October2026, found no matching complete resolution, announcement or duplicate. The actual theorems in [2] cover nests without isolated finite-dimensional atoms and certain bounded runs of finite-rank atoms; they do not cover the infinite sequence of rank-one atoms here. Later conditional Toeplitz-path results also leave this full statement untreated in the sources checked.

Disconnected invertibles in a smaller function algebra do not decide the larger group above. Paths in all of $`\mathcal B(H)`$ must also be shown to preserve $`\mathcal A`$. The review records the access limits and bounded search scope; no full-proof or exhaustive-literature certification is asserted.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ab417eaa6db5ba04**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
