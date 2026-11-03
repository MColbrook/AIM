# 793. Bounded scalar curvature and extension of the closed $`G_2`$ Laplacian flow

**Area:** Geometric analysis and nonlinear parabolic PDE
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a compact connected smooth seven-dimensional manifold without boundary. Let $`\varphi(t)`$ be a smooth family of closed positive three-forms, hence closed $`G_2`$-structures, solving
```math
\partial_t\varphi(t)=\Delta_{\varphi(t)}\varphi(t),\qquad
 d\varphi(t)=0,\qquad 0\le t<T<\infty.
```

Here $`g(t)=g_{\varphi(t)}`$ is the induced metric and
```math
\Delta_{\varphi}=d d^*_{\varphi}+d^*_{\varphi}d
```

is its Hodge Laplacian. Suppose that for some finite $`K`$,
```math
R_{g(t)}(x)\ge-K\qquad\text{for every }(x,t)\in M\times[0,T).
```

Must there exist $`\varepsilon>0`$ and a smooth solution on $`[0,T+\varepsilon)`$ agreeing with the original solution for every $`t<T`$?

For a closed $`G_2`$-structure, scalar curvature is nonpositive and is a negative fixed multiple of squared torsion norm. Thus the hypothesis is equivalent to a uniform torsion bound. No Ricci, full-curvature, Weyl, injectivity-radius or symmetry assumption is imposed.

## Application

The question asks whether control of a first-derivative geometric quantity can prevent finite-time singularities in a flow used to construct torsion-free $`G_2`$ metrics.

## References

1. Y. Li, [*Local curvature estimates for the Laplacian flow*](https://arxiv.org/html/1805.06231), v3 (2018), Introduction following Theorem 1.3 and preceding Proposition 1.5.
2. J. D. Lotay and Y. Wei, *Laplacian flow for closed $`G_2`$ structures: Shi-type estimates, uniqueness and compactness*, *Geometric and Functional Analysis* **27** (2017), 165–233, Open Problem (3), p.230. [DOI](https://doi.org/10.1007/s00039-017-0395-x).
3. C. Li and Y. Li, [*Long-time existence of some geometric flows with bounded scalar curvature*](https://arxiv.org/html/2606.10354), Question 4.10 and Corollary 4.14 (2026).
4. C. Li, Y. Li and K. Zheng, [*Long-time existence of the Laplacian flow with Weyl tensor*](https://arxiv.org/html/2610.23412), Theorems 1.1–1.2 (16 October 2026).

## Status review


**Known cases:** The scalar-only criterion for compact closed G2 Laplacian flow is required. Hypersymplectic products and current estimates adding spatial or spacetime control of W77 remain restricted; Ricci-flow scalar-extension announcements concern a different evolution.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The scalar-only criterion for compact closed G2 Laplacian flow is required. Hypersymplectic products and current estimates adding spatial or spacetime control of W77 remain restricted; Ricci-flow scalar-extension announcements concern a different evolution.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/1805.06231); [comparison source 2](https://doi.org/10.1007/s00039-017-0395-x); [comparison source 3](https://arxiv.org/html/2606.10354); [comparison source 4](https://arxiv.org/html/2610.23412). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Extension is known under stronger curvature or flow-velocity bounds and in hypersymplectic product geometries. The October 2026 theorems require a scalar bound **together with** a spatial or spacetime integrability bound on the Weyl component $`W_{77}`$. They do not establish the scalar-only criterion posed here. The original scalar evolution identity also does not settle it.

The [primary and current-status review](../FURTHER_problems/_tracking/focused-G2-Laplacian-bounded-scalar-extension-C213-Root-20261028/OWNER-EXACT-COMPACT-CLOSED-G2-SCALAR-ONLY-EXTENSION-PRIMARY-OCT2026-PARTIAL-AND-DUPLICATE-PROPOSAL.json) and [independent model review](../FURTHER_problems/_tracking/focused-G2-Laplacian-bounded-scalar-extension-C213-Root-20261028/A-INDEPENDENT-CLOSED-G2-POSITIVITY-FLOW-SIGN-SCALAR-NORM-AND-OCT2026-EXTRA-WEYL-SCOPE-PEER.json) record the precise flow, compactness restriction, latest versions, current announcement searches and semantic duplicate checks. No matching complete resolution was located. Closedness of the three-form and absence of a boundary on $`M`$ are separate hypotheses.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-60c3f3ff41ac635a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
