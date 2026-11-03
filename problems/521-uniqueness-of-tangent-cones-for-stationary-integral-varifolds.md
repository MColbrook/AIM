# 521. Uniqueness of tangent cones for stationary integral varifolds

**Area:** Geometric measure theory / minimal interfaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`2\le m<n`$ be integers and let $`U\subset\mathbb R^n`$ be open. Let $`V`$ be an integral $`m`$-varifold in $`U`$: it is represented by a countably $`m`$-rectifiable set $`M`$ with positive integer multiplicity $`\theta`$, with locally finite measure
```math
\|V\|=\theta\,\mathcal H^m\!\restriction M.
```

Assume that $`V`$ is stationary in the Euclidean metric, meaning
```math
\delta V(X)=\int_M \mathrm{div}_{T_yM}X(y)\,\theta(y)\,d\mathcal H^m(y)=0
\quad\text{for every }X\in C_c^1(U;\mathbb R^n).
```


For $`x\in U\cap\mathrm{spt}\|V\|`$, set $`\eta_{x,r}(y)=(y-x)/r`$. A tangent cone at $`x`$ is any weak varifold limit of $`(\eta_{x,r_j})_\#V`$ along a sequence $`r_j\downarrow0`$. Here $`\#`$ is varifold push-forward, which includes the $`m`$-dimensional Jacobian; weak convergence tests continuous compactly supported functions of both the position and the unoriented tangent plane.

Must $`V`$ have exactly one tangent cone at every $`x\in U\cap\mathrm{spt}\|V\|`$? Equality of cones includes their integer multiplicities, with no rotation applied when comparing limits.

The question concerns all stationary integral varifolds, without stability, area minimization, a prescribed tangent model or an almost-everywhere restriction. The ambient metric is Euclidean.

## Application

Stationary varifolds describe generalized equilibrium interfaces. A unique tangent cone would make their infinitesimal interface geometry independent of the sequence of magnification scales. This is a basic step toward understanding singularities and the local structure of minimal surfaces.

## References

1. N. Wickramasekera, [*Regularity of stable minimal hypersurfaces: recent advances in the theory and applications*](https://intlpress.com/site/pub/files/_fulltext/journals/sdg/2014/0019/0001/SDG-2014-0019-0001-a009.pdf), *Surveys in Differential Geometry* **19** (2014), 231–301. [DOI](https://doi.org/10.4310/sdg.2014.v19.n1.a9). §1.7, printed pp. 247–248, explicitly states the stationary integral-varifold question.
2. A. Naber and D. Valtorta, [*The singular structure and regularity of stationary varifolds*](https://doi.org/10.4171/JEMS/987), *Journal of the European Mathematical Society* **22** (2020), 3305–3382. [Eligible author version](https://arxiv.org/pdf/1505.03428v4), p. 3, asks the broader bounded-mean-curvature question; §2.1 defines integrality and stationarity.
3. G. Székelyhidi, [*Uniqueness of certain cylindrical tangent cones*](https://doi.org/10.1007/s00222-026-01445-1), *Inventiones mathematicae* (2026), Theorems 1.1–1.2 and §1.1.
4. B. Firester, R. Tsiamis and Y. Wang, [*Uniqueness of Cylindrical Tangent Cones $`C_{p,q}\times\mathbb R`$*](https://doi.org/10.1007/s00526-025-03238-5), *Calculus of Variations and Partial Differential Equations* **65** (2026), 165. [Author version](https://arxiv.org/pdf/2507.22373v1), Theorem 1.
5. C. De Lellis, J. Hirsch, Z. Lihn and L. Spolaor, [*Stationary varifolds with singularities II*](https://arxiv.org/abs/2609.20647), preprint (2026), Theorem 1.1 and introduction.

6. N. Edelen and P. Minter, [*Uniqueness of Regular Tangent Cones for Immersed Stable Hypersurfaces*](https://doi.org/10.1007/s00205-024-02071-y), *Archive for Rational Mechanics and Analysis* **248** (2024), 121, Theorems 1.1–1.3.
7. S. Becker-Kahn, P. Minter and N. Wickramasekera, [*On the Nature of Stationary Integral Varifolds near Multiplicity 2 Planes*](https://arxiv.org/abs/2507.13148v1), preprint (2025), Definition 2.1, Theorem 2.5 and Corollary 2.6.
8. OpenAI, [*A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold*](https://github.com/openai/math/blob/main/preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf), Theorem 1.1, and [*Almost-everywhere regularity of stationary integral varifolds*](https://github.com/openai/math/blob/main/preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf), Theorem 1.1, preprints (2026).

## Status review


**Known cases:** Current cylindrical-cone uniqueness and near-multiplicity-two-plane theorems retain tangent-model or structural assumptions. Almost-everywhere regularity/singular-dimension announcements do not establish uniqueness at every singular point for Euclidean stationary integral varifolds.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The pre-2022 sources [1–2] explicitly leave the relevant uniqueness question open. Integer multiplicity is essential to this formulation: the nonunique stationary rectifiable examples discussed in [1, §1.7] are non-integral.

Uniqueness at $`\|V\|`$-almost every point follows from rectifiability; it does not settle every singular point. Naber–Valtorta's uniqueness of the Euclidean factor in tangent cones at almost every point of a singular stratum likewise leaves the transverse cone factor undetermined.

The recent results [3–4] establish uniqueness for specified multiplicity-one cylindrical cones. They retain assumptions on the tangent model, and [4] also assumes area minimization. The examples in [5] have a multiplicity-two tangent plane and use a changed smooth Riemannian metric; they do not produce two distinct Euclidean tangent cones.

Edelen–Minter [6] allow higher multiplicity under stability and regular-cone assumptions. The near-double-plane theorem [7] proves uniqueness under an additional topological separation condition in coarse gaps; its general corollary retains the alternative that this condition fails. Neither removes the hypotheses absent from the question above.

The current OpenAI catalogue's stationary-varifold announcements concern the dimension or measure of the singular set. Their reviewed theorem statements do not assert uniqueness at every singular point. Current targeted searches located no matching theorem, counterexample or announced resolution. Selected primary definitions and statements were read; external proofs were not fully audited.


### Online recheck, 2026-10-30

Current cylindrical-cone uniqueness and near-multiplicity-two-plane theorems retain tangent-model or structural assumptions. Almost-everywhere regularity/singular-dimension announcements do not establish uniqueness at every singular point for Euclidean stationary integral varifolds.

Comparators and current-status sources: [status source 1](https://doi.org/10.1007/s00222-026-01445-1); [status source 2](https://arxiv.org/abs/2507.13148); [status source 3](https://arxiv.org/abs/2609.20647). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c3f89b7723f99eb8** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
