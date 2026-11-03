# 1049. Scalar integrable PDEs with the same quasilinear part

**Area:** Integrable nonlinear evolution equations; formal conservation-law hierarchies
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

In the formal perturbative setting of Arsie, Lorenzoni and Moro, consider scalar integrable evolutionary equations

```math
u_t=\sum_{k\geq 0}\varepsilon^k F_{k+1}(u,u_x,u_{xx},\ldots),
```


where $`F_{k+1}`$ is a homogeneous differential polynomial of derivative degree $`k+1`$. Write the **quasilinear part** (terms linear in derivatives of $`u`$) as

```math
\sum_{k\geq 0}\varepsilon^k X_{k+1}(u)u_{(k+1)},
\qquad u_{(j)}=\partial_x^j u.
```


If two such integrable equations have identical coefficient functions $`X_j(u)`$ for every $`j\geq1`$, must they be related by a formal Miura transformation

```math
v=M_0(u)+\sum_{k\geq1}\varepsilon^k M_k(u,u_x,u_{xx},\ldots),
```


with locally invertible $`M_0`$ and each $`M_k`$ homogeneous of derivative degree $`k`$? This is Conjecture 1.1 of the cited paper. “Integrable” here refers to the source's formal commuting-flow framework; the question does not assert analytic well-posedness for arbitrary data.

## Application

The coefficients of the highest derivative at each perturbative order are known to be necessary Miura invariants. A positive answer would make those coefficients complete invariants for classifying scalar integrable hierarchies, including dispersive and viscous conservation laws. The original paper checks cases through finite orders and gives familiar Miura-related examples, but these do not establish the all-orders statement.

## References

1. A. Arsie, P. Lorenzoni and A. Moro, [*On integrable conservation laws*](https://arxiv.org/html/1401.1166), arXiv:1401.1166v1 (2014); *Proceedings of the Royal Society A* **471** (2015), 20140124, [doi:10.1098/rspa.2014.0124](https://doi.org/10.1098/rspa.2014.0124). Introduction, equations (1.3) and (1.7), Conjecture 1.1; Section 2, Theorem 2.1 and Corollary 2.2; Section 3, finite-order calculations.
2. A. Arsie and P. Lorenzoni, [*Flat F-manifolds, Miura invariants, and integrable systems of conservation laws*](https://academic.oup.com/integrablesystems/article/3/1/xyy004/4964995), *Journal of Integrable Systems* **3** (2018), xyy004, Introduction and Section 2. This proves related necessary invariance and still describes the scalar converse as conjectural.
3. A. Buryak and P. Rossi, [*Deformations of the Riemann hierarchy and the geometry of $`\overline{\mathcal M}_{g,n}`$*](https://arxiv.org/html/2504.02079), arXiv:2504.02079v2 (2025), Introduction and Section 4.1. It explicitly treats the Miura-classification assertion from Conjecture 1.1 as conjectural and develops conditional and narrower conservation-law results.

## Status review


**Known cases:** Identical quasilinear coefficients must imply a full formal Miura equivalence. Necessary invariance, finite-order computations and the 2025 conditional classification remain narrower; the 2026 Haantjes conjecture concerns another integrability assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Identical quasilinear coefficients must imply a full formal Miura equivalence. Necessary invariance, finite-order computations and the 2025 conditional classification remain narrower; the 2026 Haantjes conjecture concerns another integrability assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2018 invariance result establishes the **necessary** direction. The 2025 paper invokes the original classification conjecture conditionally and presents a more restricted normal-form conjecture; neither is a proof of the universal converse stated above. A bounded search through 2026-10-21 found no exact-scope proof, counterexample or complete announcement. The [source-bound arXiv packet](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0183-review.json), [independent primary and status review](../FURTHER_problems/_tracking/arsie-lorenzoni-moro-miura-status-2026-10-21.json), and [semantic duplicate snapshot](../FURTHER_problems/_tracking/arsie-lorenzoni-moro-miura-duplicates-2026-10-21.json) record the checked scope and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7e0d31e19e5ddab4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
