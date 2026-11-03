# 806. Must every elliptic Weingarten sphere in a homogeneous three-manifold be rotational?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M=\mathbb{E}^3(\kappa,\tau)`$ be a simply connected homogeneous Riemannian three-manifold with four-dimensional isometry group, so $`\kappa-4\tau^2\ne0`$. These spaces have a canonical vertical direction from their Riemannian fibration over a constant-curvature surface.

Let a closed connected oriented surface of genus zero be smoothly immersed in $`M`$. Write $`k_1,k_2`$ for its principal curvatures,
```math
H=\frac{k_1+k_2}{2},\qquad K_e=k_1k_2.
```

Suppose it satisfies
```math
H=\phi(H^2-K_e),\qquad
\phi\in C^\infty([0,\infty)),\qquad
4t\phi'(t)^2<1\quad(t\ge0).
```


Must its image be invariant under the one-parameter rotational isometries fixing some vertical geodesic?

The immersion need not be embedded or convex. The question imposes no sign condition on $`H`$ and no global uniform ellipticity bound. It asks for symmetry of an existing immersed sphere, rather than existence for every equation.

## Application

This extends the Hopf uniqueness problem from constant mean curvature to nonlinear elliptic curvature equations. It asks whether the symmetries of these ambient spaces force symmetry of every spherical solution. No direct practical application is identified here.

## References

1. José A. Gálvez and Pablo Mira, *Rotational symmetry of Weingarten spheres in homogeneous three-manifolds*, Journal für die reine und angewandte Mathematik **773** (2021), 21–66. [DOI](https://doi.org/10.1515/crelle-2020-0031); [primary preprint](https://arxiv.org/abs/1807.09654). Introduction, Eq. (1.1), Problem (P), Theorems 1.2–1.6 and Example 8.6.
2. Isabel Fernández, *Rotational elliptic Weingarten surfaces in $`\mathbb{S}^2\times\mathbb{R}`$ and the Hopf problem*, Journal of Mathematical Analysis and Applications **526** (2023), 127268. [DOI](https://doi.org/10.1016/j.jmaa.2023.127268); [primary preprint, v2](https://arxiv.org/abs/2211.11373v2). Definition 2.1 and Theorem 4.2 give the uniformly elliptic product-space result.

## Status review


**Known cases:** Uniform ellipticity or a bounded-curvature canonical rotational model are additional hypotheses in the available classification results. Compactness of the given immersed sphere does not automatically bound that separate model. The nonproduct homogeneous three-manifold case remains beyond the known product reductions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Uniform ellipticity or a bounded-curvature canonical rotational model are additional hypotheses in the available classification results. Compactness of the given immersed sphere does not automatically bound that separate model. The nonproduct homogeneous three-manifold case remains beyond the known product reductions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 30 October 2026. There is substantial partial progress. The hyperbolic product case is affirmative, as are several special curvature relations. The general uniqueness theorem assumes bounded second fundamental form of a distinguished **canonical rotational model**; bounded curvature of the given compact immersion does not supply that hypothesis.

Fernández's theorem also implies rotational symmetry for a fixed compact sphere in $`\mathbb{S}^2\times\mathbb{R}`$ satisfying the equation above. Indeed, let $`T=\max(H^2-K_e)`$ on that sphere and extend $`\phi`$ beyond $`[0,T]`$ by cutting off its derivative. The resulting bounded smooth function agrees on the sphere and satisfies $`2\sqrt t|\widetilde\phi'(t)|\le c<1`$ globally. For the associated symmetric curvature equation, both principal-curvature partial derivatives lie in $`[(1-c)/2,(1+c)/2]`$, so the uniform theorem applies. This is a checked reduction, rather than a stronger theorem quoted from that paper; it does not settle the nonproduct spaces.

Bounded current searches and semantic comparison with AIM, current saved OpenAI announcements and private findings found no matching resolution of the full question. A singular canonical model is not a counterexample consisting of a smooth nonrotational sphere. Exact preprint statements were read; full published-body parity is not asserted. These checks do not prove openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-79d43c862e5f0386**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
