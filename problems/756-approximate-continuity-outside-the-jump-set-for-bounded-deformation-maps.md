# 756. Approximate continuity outside the jump set for bounded-deformation maps

**Area:** Calculus of variations / fracture and plasticity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$ and let $`u\in L^1_{\mathrm{loc}}(\mathbb R^d;\mathbb R^d)`$ have distributional symmetric gradient

```math
Eu=\tfrac12(Du+Du^T)\in\mathcal M_{\mathrm{loc}}(\mathbb R^d;\mathbb R^{d\times d}_{\mathrm{sym}}).
```

Thus $`u\in\mathrm{BD}_{\mathrm{loc}}(\mathbb R^d)`$. Define $`C_u`$ to consist of points $`x`$ for which some $`z\in\mathbb R^d`$ satisfies

```math
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r(x)}|u(y)-z|\,dy=0,
\qquad S_u=\mathbb R^d\setminus C_u.
```

Define $`J_u`$ to consist of points $`x`$ for which there are $`a\ne b`$ in $`\mathbb R^d`$ and $`\nu\in\mathbb S^{d-1}`$ such that, writing $`B_r^\pm(x,\nu)=\{y\in B_r(x):\pm(y-x)\cdot\nu>0\}`$,

```math
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r^+(x,\nu)}|u(y)-a|\,dy=0,
\qquad
\lim_{r\downarrow0}\frac1{|B_r(x)|}\int_{B_r^-(x,\nu)}|u(y)-b|\,dy=0.
```

Is it true for every such $`d,u`$ that

```math
\mathcal H^{d-1}(S_u\setminus J_u)=0?
```

Approximate continuity here means the displayed mean-$`L^1`$ limit. No additional boundedness, higher strain integrability, absence of Cantor strain, or finite jump-set measure is assumed.

## Application

Bounded-deformation maps describe displacements with finite total strain in models of plasticity, damage and fracture. The conjecture asks whether almost every displacement discontinuity at the dimension of a crack is an ordinary jump across a surface, including for maps with diffuse singular strain.

## References

1. G. De Philippis and F. Rindler, *Fine properties of functions of bounded deformation — an approach via linear PDEs*, Mathematics in Engineering **2**(3) (2020), 386–422. Conjecture 1.3, p.390; approximate-continuity definition p.388. [Published article](https://doi.org/10.3934/mine.2020018), [published PDF](https://www.aimspress.com/aimspress-data/mine/2020/3/PDF/mine-02-03-018.pdf), [eligible preprint v2](https://arxiv.org/abs/1911.01356v2).
2. A. Arroyo-Rabasa and A. Skorobogatova, *A look into some of the fine properties of functions with bounded $`\mathscr A`$-variation*, ESAIM: Control, Optimisation and Calculus of Variations **31** (2025), article50, 30pp. Introduction and §2.4 discuss the remaining discontinuity-set question and capacitary/scale-dependent continuity results. [DOI](https://doi.org/10.1051/cocv/2025003), [institutional published copy](https://www.research-collection.ethz.ch/bitstreams/340e9307-a903-44e8-b0a8-956825697e37/download).

## Status review


**Known cases:** The desired Hausdorff-(d-1)-null exceptional set is stronger than the known strain-measure-null statement. Approximate quasi-continuity, fixed-polar tangent results and rectifiable-surface restrictions do not establish it for arbitrary BD maps.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The desired Hausdorff-(d-1)-null exceptional set is stronger than the known strain-measure-null statement. Approximate quasi-continuity, fixed-polar tangent results and rectifiable-surface restrictions do not establish it for arbitrary BD maps.

Additional comparison sources: [comparison source 1](https://doi.org/10.3934/mine.2020018); [comparison source 2](https://www.aimspress.com/aimspress-data/mine/2020/3/PDF/mine-02-03-018.pdf); [comparison source 3](https://arxiv.org/abs/1911.01356v2); [comparison source 4](https://doi.org/10.1051/cocv/2025003); [comparison source 5](https://www.research-collection.ethz.ch/bitstreams/340e9307-a903-44e8-b0a8-956825697e37/download); [comparison source 6](https://arxiv.org/abs/2606.12061v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Literature check: 17 October 2026.** The exact conjecture is stated in both the eligible 2020 preprint and the published survey. It is stronger than the known statement $`|Ev|(S_u\setminus J_u)=0`$ for every bounded-deformation map $`v`$. The 2025 paper retains the Hausdorff-size question: capacitary estimates and approximate continuity on each countably rectifiable hypersurface do not establish the required Hausdorff-null conclusion on the whole exceptional set. In particular, a scale-dependent choice of best constant need not converge to a single vector.

The June2026 plane-wave results in [arXiv:2606.12061v1](https://arxiv.org/abs/2606.12061v1) concern measures with fixed polar and tangent decompositions; their stated conclusions do not give the displayed Hausdorff estimate for arbitrary BD maps. The 2026 deviatoric-strain results distinguish quasi-continuity from approximate continuity and ask a different, strain-measure-almost-everywhere question. No matching resolution was found in the checked primary announcements. The independent selected-primary audit and scoped catalogue comparison passed. Capacity-notation inconsistencies in the 2025 source are recorded without certifying its formulas.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/bd-approx-continuity-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-bd-approx-continuity-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/bd-approx-continuity-duplicate-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/batch-0151-deployment-validation.json) and [coordinator review](../FURTHER_problems/_tracking/bd-approx-continuity-coordinator-review-2026-10-17.json) preserve exact definitions, versions and reading limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-66a100fb14595af8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
