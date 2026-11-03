# 681. Positive capacity of transcendental quasiregular backward-orbit closures

**Area:** Geometric function theory and nonlinear potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge3`$. Let $`f:\mathbb R^d\to\mathbb R^d`$ be nonconstant and continuous, with $`f\in W^{1,d}_{\mathrm{loc}}`$ and

```math
\|Df(x)\|^d\le K\det Df(x)\quad\text{a.e.}
```

for some finite $`K\ge1`$, where $`\|Df\|`$ is the operator norm. Assume that $`f`$ is of transcendental type: $`\lim_{|x|\to\infty}|f(x)|`$ does not exist. The map is defined on all of Euclidean space. Set

```math
O_f^-(x)=\bigcup_{m\ge0}\{y:f^m(y)=x\},\qquad
E(f)=\{x:O_f^-(x)\text{ is finite}\}.
```

For compact $`C`$ inside a bounded open $`A\subset\mathbb R^d`$, define

```math
\mathrm{cap}(A,C)=\inf\left\{\int_A|\nabla u|^d\,dx:
 u\in C_c^\infty(A),\ u\ge0,\ u|_C\ge1\right\}.
```

A compact set has zero conformal $`d`$-capacity if this infimum is zero; this property is independent of the enclosing bounded open set. A closed unbounded set has zero capacity if every compact subset does.

**Does every $`x\notin E(f)`$ satisfy**

```math
\mathrm{cap}\!\left(\overline{O_f^-(x)}\right)>0?
```

The closure is taken in $`\mathbb R^d`$. Equivalently, zero capacity of that closure should characterize exceptional points, since finite sets have zero capacity. This is the entire, no-pole component of the conjectural relation discussed in [1].

## Application

The question tests whether inverse iterates of every nonexceptional point accumulate on a set large enough for nonlinear potential theory. Such capacity bounds support the Julia-set framework for higher-dimensional quasiregular dynamics.

## References

1. L. Warren, *On the iteration of quasimeromorphic mappings*, Math. Proc. Cambridge Philos. Soc. **168** (2020), 1–11, [DOI](https://doi.org/10.1017/S030500411800052X); [author manuscript](https://arxiv.org/pdf/1805.00454v2), introduction before Theorem 1.5 and §§2.1–2.2.
2. W. Bergweiler and D. A. Nicks, *Foundations for an iteration theory of entire quasiregular maps*, Israel J. Math. **201** (2014), 147–184, [DOI](https://doi.org/10.1007/s11856-014-1081-4); [author manuscript](https://arxiv.org/pdf/1210.3972v1), Theorems 1.6–1.11 and §2.

## Status review


**Known cases:** The closed backward-orbit capacity question remains for arbitrary entire transcendental quasiregular maps in dimensions >=3. At-least-one-pole theorems, polynomial-type and commuting-map theorems have different assumptions; no-pits-effect and local-index cases do not cover the target. Fresh author, subject and proof-venue searches found no complete result.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The closed backward-orbit capacity question remains for arbitrary entire transcendental quasiregular maps in dimensions >=3. At-least-one-pole theorems, polynomial-type and commuting-map theorems have different assumptions; no-pits-effect and local-index cases do not cover the target. Fresh author, subject and proof-venue searches found no complete result.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1805.00454); [comparison source 2](https://arxiv.org/abs/1210.3972); [comparison source 3](https://arxiv.org/abs/1912.04152). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 2026-10-29. Source [2] proves the conclusion in dimension two and, in higher dimensions, under conditions including absence of the pits effect or bounded local index. Source [1] proves the corresponding at-least-one-pole case. These results leave the unrestricted class stated here.

Bounded exact-question, author, proof/counterexample and 2025–2026 searches found no complete or announced resolution. Current conditional growth/dimension results, uniformly quasiregular polynomial-type constructions and proper-domain iteration theorems were checked for their actual scope. All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. [Owner review](../FURTHER_problems/_tracking/focused-transcendental-quasiregular-backward-capacity-C241-A-20261029/OWNER-V2-EXACT-TRANSCENDENTAL-QUASIREGULAR-CLOSED-BACKWARD-CAPACITY-PRIMARY-CURRENT-AND-DUPLICATE-PROPOSAL.json) and [coordinating review](../FURTHER_problems/_tracking/focused-transcendental-quasiregular-backward-capacity-C241-A-20261029/ROOT-CLOSED-BACKWARD-ORBIT-CAPACITY-PRIMARY-VISUAL-CURRENT-AND-FINAL-REVIEW.json) retain the exact capacity, closure, version and independent model checks, including visual verification of the source overbar.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-1bbd1c61a62bf3e7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
