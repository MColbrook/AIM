# 878. Zero vacuum Bartnik mass without a no-horizon condition

**Area:** Geometric analysis and mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(\Omega,g_\Omega)`$ be a smooth compact connected orientable Riemannian three-ball with nonnegative scalar curvature and strictly positive outward boundary mean curvature $`H`$. Write $`\gamma=g_\Omega|_{\partial\Omega}`$. Mean curvature means the trace of the second fundamental form.

Let $`\mathcal C(\gamma,H)`$ consist of smooth connected orientable Riemannian three-manifolds $`(M,g)`$ complete up to their boundary, with $`\partial M`$ identified with $`\partial\Omega`$, exactly one asymptotically flat end, and

```math
R_g\equiv0,\qquad g|_{\partial M}=\gamma,\qquad H_{\partial M}=H.
```

Here the boundary normal points into the exterior manifold, toward its asymptotically flat end. Outside a compact set, require coordinates in which, for some $`\tau>1/2`$,

```math
\partial^\alpha(g_{ij}-\delta_{ij})=O(r^{-\tau-|\alpha|}),\qquad |\alpha|\le2.
```

There is **no restriction on compact minimal surfaces**, and the extension topology is unrestricted. Define

```math
m_B^0(\gamma,H)=\inf_{(M,g)\in\mathcal C(\gamma,H)}m_{\rm ADM}(M,g),
\qquad \inf\varnothing=+\infty,
```

using the standard three-dimensional ADM normalization $`1/(16\pi)`$. Does

```math
m_B^0(\gamma,H)=0\quad\Longrightarrow\quad
\mathrm{Riem}(g_\Omega)\equiv0
```

always hold? The infimum need not be attained. This is the smooth strictly mean-convex three-ball case of Anderson's Conjecture 2.2; only the displayed implication is requested.

## Application

Scalar-flat initial data model vacuum in time-symmetric general relativity. This question tests whether minimizing the mass of vacuum exteriors detects nonflat interior geometry even when horizons are allowed. It bears on the definition of quasi-local gravitational mass.

## References

1. M. T. Anderson, *Recent progress and problems on the Bartnik quasi-local mass*, Pure and Applied Mathematics Quarterly **15** (2019), 851–873. Definition 2.1, Conjecture 2.2 and Remark 2.3; the conjecture and remark are printed on p. 857. [Published article](https://doi.org/10.4310/PAMQ.2019.v15.n3.a4), [eligible preprint v1](https://arxiv.org/abs/1903.03822v1), pp. 4–5.
2. C. Dong and A. Song, *Stability of Euclidean 3-space for the positive mass theorem*, Inventiones Mathematicae **239** (2025), 287–319; [published article](https://doi.org/10.1007/s00222-024-01302-z), [preprint v3](https://arxiv.org/abs/2302.07414v3), §5 and Theorem 5.1. Its admissible extensions exclude closed minimal surfaces in their interiors.
3. Z. An and L.-H. Huang, *Strict Stability of the ADM Mass and Static Vacuum Extensions*, [preprint v1](https://arxiv.org/abs/2609.28101v1) (2026), Theorems 1–3. Local stability near an existing static background.

## Status review


**Known cases:** Attained zero ADM mass is covered by positive-mass rigidity, but the problem includes nonattained infima over scalar-flat exteriors allowing horizons. Dong-Song restrict admissible exteriors by excluding minimal surfaces. The newly published spacetime black-hole paper treats compact apparent-horizon boundary or noncompact domains with horizons in each admissible extension, not strictly mean-convex compact three-balls with this exact vacuum exterior infimum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Attained zero ADM mass is covered by positive-mass rigidity, but the problem includes nonattained infima over scalar-flat exteriors allowing horizons. Dong-Song restrict admissible exteriors by excluding minimal surfaces. The newly published spacetime black-hole paper treats compact apparent-horizon boundary or noncompact domains with horizons in each admissible extension, not strictly mean-convex compact three-balls with this exact vacuum exterior infimum.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/2606.07781v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The positive mass theorem with corners gives nonnegativity and settles the implication when a zero-mass extension attains the infimum. The question includes nonattained minimizing sequences. Dong–Song's strict positivity theorem concerns a different admissible class, with a no-interior-minimal-surface condition. A lower bound for that restricted infimum does not bound this larger class from below.

Anderson's Remark 2.3 describes a possible obstruction: a small-mass exterior with nonnegative scalar curvature can be conformally corrected to scalar curvature zero while preserving $`\gamma`$, but the resulting mean curvature is only bounded above by $`H`$. The construction does not preserve the exact pair $`(\gamma,H)`$, and uncontrolled derivatives obstruct an immediate limiting argument. Local static stability likewise gives no global bound over all members of $`\mathcal C(\gamma,H)`$.

Current results involving black-hole boundaries, outer-minimizing boundaries, noncompact fill-ins or positive attained spacetime mass have different hypotheses. Bounded proof, counterexample and announcement searches through 18 October 2026 found no complete matching claim. The [coordinator review](../FURTHER_problems/_tracking/vacuum-rigidity-coordinator-review-2026-10-18.json) records the selected theorem comparisons and limits. This is a literature assessment, not a proof of openness or certification of all cited proofs.

The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-vacuum-bartnik-rigidity-review.json), [semantic comparison](../FURTHER_problems/_tracking/vacuum-rigidity-duplicates-review-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/vacuum-rigidity-catalogue-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/vacuum-rigidity-coordinator-review-2026-10-18.json) record the exact extents and limitations. These are AI literature and formulation checks, not human peer review or certification of every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7245f417ffab844d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
