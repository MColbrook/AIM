# 1050. Uniqueness for a planar plasma coupled to an attractive moving point charge

**Area:** Kinetic equations and singular particle–field coupling
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Set $`K(z)=z/|z|^2`$ for $`z\in\mathbb R^2\setminus\{0\}`$. Fix $`\xi_0,\eta_0\in\mathbb R^2`$ and a nonnegative bounded probability density $`f_0(x,v)`$ on $`\mathbb R^2\times\mathbb R^2`$. Suppose that, for some finite $`C_0`$, its support is contained, up to null sets, in

```math
\left\{(x,v):x\ne\xi_0,\quad
\left|\frac12|v-\eta_0|^2+\log|x-\xi_0|\right|\le C_0\right\}.
```

Consider the coupled system

```math
\partial_t f+v\cdot\nabla_x f+
\big(E(t,x)-K(x-\xi(t))\big)\cdot\nabla_v f=0,
\qquad
E(t,x)=\int_{\mathbb R^2}K(x-y)\rho(t,y)\,dy,
\quad
\rho(t,x)=\int_{\mathbb R^2}f(t,x,v)\,dv,
```

```math
\dot\xi(t)=\eta(t),\qquad
\dot\eta(t)=-E(t,\xi(t)),\qquad
(f,\xi,\eta)|_{t=0}=(f_0,\xi_0,\eta_0).
```

The plasma repels itself and is attracted to the moving point charge. No initial positive distance between the plasma and the charge is assumed.

Is the coupled solution unique in the characteristic existence class of Caprino–Marchioro–Miot–Pulvirenti, Theorem 1? More explicitly, on every finite interval $`[0,T]`$, use the solutions supplied there: $`f\in L^\infty(0,T;L^1\cap L^\infty)`$, bounded $`E`$, and $`C^1`$ charge position and velocity. The plasma is transported along characteristics satisfying

```math
\dot X=V,\qquad \dot V=E(t,X)-K(X-\xi(t)).
```

For $`f_0(x,v)\,dx\,dv`$-almost every initial label, these characteristics are $`C^1`$ and avoid the charge throughout $`[0,T]`$. Require the same finite microscopic-energy control and density estimate as in that theorem:

```math
\mathop{\mathrm{ess\,sup}}_{(x,v)\sim f_0\,dx\,dv}
\sup_{0\le s\le T}
\left|\frac12|V(s;x,v)-\eta(s)|^2+
\log|X(s;x,v)-\xi(s)|\right|<\infty,
```

```math
\rho(t,x)\le C_T\big(1+\log_-|x-\xi(t)|\big),
\qquad \log_-r=\max\{0,-\log r\}.
```

Uniqueness means that two such solutions with the same initial data have the same charge trajectory and the same transported plasma density almost everywhere. The question concerns the fully coupled evolution. Uniqueness of characteristics after prescribing $`f`$, already established in the source, does not answer it. This is the single-charge core of one plasma-charge uniqueness family.

## Application

A hybrid plasma model treats a diffuse cloud kinetically and a distinguished charge as a moving particle. Uniqueness would ensure that the same initial cloud and charge motion determine one subsequent evolution, even when particles can approach the singular attractive field closely.

## References

1. S. Caprino, C. Marchioro, E. Miot and M. Pulvirenti, *On the attractive plasma-charge system in 2-d*, Communications in Partial Differential Equations **37** (2012), 1237–1272, [DOI](https://doi.org/10.1080/03605302.2011.653032). [Author version, arXiv:1106.5527v1](https://arxiv.org/html/1106.5527v1), Introduction and Section 2, equations (2.1)–(2.6), Theorem 1 and Remark 1. These selected statements, rather than the full existence proof, were inspected.
2. J. Wu and M. Zhu, *Initial-boundary value problem of plasma-charge model in the half space*, Electronic Journal of Differential Equations **2025**, no. 106, 1–18, [official article](https://ejde.math.txstate.edu/Volumes/2025/106/wu.pdf). The Introduction on physical p. 4 retains the two-dimensional attractive uniqueness gap.
3. J. Wu, *The Plasma-Charge Model: Boundary Effects and Global Well-posedness*, [arXiv:2604.11371v1](https://arxiv.org/html/2604.11371v1), 13 April 2026, Section 1.1. Its discussion still separates planar attractive existence from uniqueness; its new theorems concern a different bounded-domain setting.

## Status review


**Known cases:** The attractive fully coupled model permits unbounded velocities near the charge. The April 2026 primary still retains uniqueness as open; prescribed-field characteristic uniqueness and initially separated or repulsive models do not decide it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The attractive fully coupled model permits unbounded velocities near the charge. The April 2026 primary still retains uniqueness as open; prescribed-field characteristic uniqueness and initially separated or repulsive models do not decide it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The initial assumption is an absolute microscopic-energy band, allowing unbounded particle velocities near the charge. It is not an assumption of compact velocity support or uniform separation.

The source proves existence in the displayed class and explicitly leaves the coupled uniqueness question unanswered. The 2025 and 2026 sources retain that distinction. Repulsive three-dimensional Lagrangian existence results have different signs and hypotheses. Nonuniqueness of stationary three-dimensional plasmas with fixed background charges does not provide two evolutions from the same initial data here.

Current searches and comparisons on 19 October 2026 found no matching complete resolution or announcement. The AIM, OpenAI and developing FURTHER lists were compared; the nearby relativistic regularity, Coulomb mean-field limit and Landau damping problems have different targets. A bounded skim of the cached Prove2Me matches found different equations and formalization tasks.

The [source packet](../FURTHER_problems/_tracking/plasma-charge-planar-uniqueness-selected-candidate-2026-10-19.json), [source supplement](../FURTHER_problems/_tracking/plasma-charge-planar-uniqueness-source-supplement-2026-10-19.json), [independent formulation audit](../FURTHER_problems/_tracking/parallel/continuum/cross-plasma-charge-planar-uniqueness-review.json), [current comparisons](../FURTHER_problems/_tracking/plasma-charge-planar-uniqueness-current-review-2026-10-19.json), [duplicate review](../FURTHER_problems/_tracking/plasma-charge-planar-uniqueness-duplicates-review-2026-10-19.json) and [catalogue skim](../FURTHER_problems/_tracking/plasma-charge-planar-uniqueness-catalogue-review-2026-10-19.json) record the exact extents and access limits. These are AI research checks, not human peer review or certification that no solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-80bfd332a03103b9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
