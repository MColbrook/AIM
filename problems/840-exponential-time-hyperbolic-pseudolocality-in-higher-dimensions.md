# 840. Exponential-time hyperbolic pseudolocality in higher dimensions

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each integer $`n\ge3`$, do constants $`A(n),c(n),\overline R(n)>0`$ exist with the following property?

Let $`g(t)`$, $`0\le t\le T`$, be a smooth complete Ricci flow of bounded curvature on a smooth $`n`$-manifold $`M`$, with $`T>0`$ and
```math
\partial_tg=-2\mathrm{Ric}(g).
```

Suppose that for some $`x\in M`$ and $`R\ge\overline R(n)`$ the initial pointed ball
```math
(B_{g(0)}(x,R),g(0),x)
```

is isometric to the radius-$`R`$ ball centred at a point in hyperbolic $`n`$-space of sectional curvature $`-1`$.

Must the Riemann curvature tensor satisfy
```math
|\mathrm{Rm}(g(t))|_{g(t)}(x)\le A(n)
\qquad\text{for }0\le t\le\min\{T,e^{c(n)R}\}?
```

The constants must be independent of the flow's global curvature bound and of its initial geometry outside the ball. This concerns the given unnormalized flow and a bound at its fixed centre. It does not assert existence of the flow up to $`e^{c(n)R}`$, a decay rate, or a bound on the entire ball.

## Application

This asks how long a large negatively curved region is protected from the influence of arbitrary surrounding geometry under Ricci flow. A time exponential in its initial radius would give substantially stronger local stability than a fixed short-time curvature estimate.

## References

1. A. D. McLeod, *Improved pseudolocality on large hyperbolic balls*, Communications in Analysis and Geometry **30**(10), 2285–2314 (published 2023). [DOI](https://doi.org/10.4310/CAG.2022.v30.n10.a4); [primary preprint, v2](https://arxiv.org/abs/1807.09005v2). Conjecture 1, native p. 4. The surface results in the same paper are proved; this question concerns $`n\ge3`$.
2. [Pseudolocality theorems of Ricci flows on incomplete manifolds](https://arxiv.org/abs/2210.15397), v5, Theorems 1.1–1.4. The local existence and entropy hypotheses differ from the statement here.
3. [On the stability of Ricci flow on hyperbolic 3-manifolds of finite volume](https://arxiv.org/abs/2509.00188), v1, Theorem 1.1. Its global closeness assumption is absent here.
4. O. C. Schnürer, F. Schulze and M. Simon, *Stability of hyperbolic space under Ricci flow*, [primary preprint](https://arxiv.org/abs/1003.2107), Theorems 1.2–1.4. These impose global smallness and integrability assumptions.

## Status review


**Known cases:** The higher-dimensional hyperbolic-pseudolocality statement remains distinct from the established surface theorem. General local-existence estimates and global-small-perturbation hyperbolic stability do not yield an exponential time bound for every given complete flow from a ball hypothesis alone.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The higher-dimensional hyperbolic-pseudolocality statement remains distinct from the established surface theorem. General local-existence estimates and global-small-perturbation hyperbolic stability do not yield an exponential time bound for every given complete flow from a ball hypothesis alone.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 30 October 2026. The latest source conjecture and the relevant later primary theorem statements were read. Local constructions of a flow and global hyperbolic stability results do not establish the estimate for every given complete flow under only the stated ball hypothesis. Time normalization does not remove their extra spatial assumptions.

Bounded searches for later resolutions and complete announcements found no matching result. Semantic checks against AIM, the saved current OpenAI announcement corpus and private findings found no equivalent target. These checks are not a proof of openness. Selected primary statements and hypotheses were compared; no complete proof audit or published-body parity is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c9394a2f34ce3739**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
