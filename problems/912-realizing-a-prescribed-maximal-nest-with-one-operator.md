# 912. Realizing a prescribed maximal nest with one operator

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`H`$ be a complex separable infinite-dimensional Hilbert space. Let $`\mathcal N`$ be a maximal nest: a complete chain of norm-closed linear subspaces of $`H`$, containing $`\{0\}`$ and $`H`$, that is not properly contained in any other chain. Completeness means closure under arbitrary intersections and closed linear spans.

Must there exist a bounded complex-linear operator $`T\in\mathcal B(H)`$ for which

```math
\mathrm{Lat}(T):=\{M\subseteq H:M\text{ is closed and linear},\ T(M)\subseteq M\}=\mathcal N?
```


The required lattice is the given collection of concrete subspaces. Having merely an order-isomorphic lattice, or one maximal invariant chain inside a larger invariant-subspace lattice, does not satisfy the statement. No compactness, quasinilpotence or prescribed spectrum is required of $`T`$.

An operator whose entire invariant-subspace lattice is a chain is called **unicellular**. The question is Problem2 in [1, Chapter25, printed p.392].

## Application

Invariant subspaces describe closed components preserved by a linear evolution. This asks which prescribed complete hierarchies can be exactly the components preserved by a single bounded operator, linking triangular operator models with the concrete geometry of subspace lattices.

## References

1. K. R. Davidson, *Nest Algebras: Triangular Forms for Operator Algebras on Hilbert Space*, Pitman Research Notes in Mathematics **191**, Longman Scientific & Technical, 1988, Chapter25, Problem2, printed p.392. [Author’s book page and copy](https://www.math.uwaterloo.ca/~krdavids/nestbook.html).
2. W. E. Longstaff, [*Reflexive index of a family of subspaces*](https://doi.org/10.1017/S0004972713001159), *Bulletin of the Australian Mathematical Society* **90** (2014), 134–140, Definitions1.1 and Section2, observations O2–O4. This explains the one-operator formulation and the two-operator upper bound for nests.

## Status review


**Known cases:** A two-operator common invariant lattice and examples of individual unicellular operators do not realize every prescribed maximal nest by one operator. Order-isomorphic nests or one maximal invariant chain inside a larger lattice do not satisfy the exact concrete-lattice target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A two-operator common invariant lattice and examples of individual unicellular operators do not realize every prescribed maximal nest by one operator. Order-isomorphic nests or one maximal invariant chain inside a larger lattice do not satisfy the exact concrete-lattice target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary/current-source and semantic review](../FURTHER_problems/_tracking/focused-Nest-Algebras-Q1-Q2-C278-C-20261029/ROOT-FINAL-TWO-EXACT-NEST-SOURCE-CURRENT-AND-SEMANTIC-REVIEWS.json), checked29October2026, found no matching complete resolution, announced solution or duplicate in the bounded searches.

Longstaff’s observation O4 gives every separable Hilbert-space nest as the common invariant-subspace lattice of **two** operators. It also lists one-operator examples, including Donoghue and Volterra operators. These facts do not establish the requested single-operator realization for every prescribed maximal nest. Examples of lattices with larger reflexive index elsewhere in that paper are not maximal chains and do not provide counterexamples here.

The nearby catalogue questions on a common invariant subspace of an invertible operator and its inverse, real-to-complex passage, and hyperinvariant subspaces have different quantifiers and conclusions. No equivalence with them is asserted. The evidence concerns selected primary statements and bounded current searches, not complete proof verification or exhaustive absence of a later reference.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-88b2c5f4b484a93e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
