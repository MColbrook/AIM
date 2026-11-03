# 1009. A Hodge spectral gap from lower sectional curvature, volume, and diameter

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a dimension $`m`$, a real number $`\kappa`$, and $`v,D>0`$. Does there exist $`C=C(m,\kappa,v,D)>0`$ such that every connected oriented closed Riemannian $`m`$-manifold $`(M,g)`$ satisfying

```math
\mathrm{sec}_g\geq\kappa,\qquad \mathrm{vol}(M,g)\geq v,\qquad \mathrm{diam}(M,g)\leq D
```


has first **positive** Hodge-Laplacian eigenvalue $`\lambda^{(p)}_1(M,g)\geq C`$ in every form degree $`p=0,\ldots,m`$ [1, Remark 3.3; 2, Conjecture 6.2]?

Lott suggested the needed noncollapsing, lower-curvature class might have a finite Lipschitz-cover property [3, p. 918]. Anné and Takahashi construct small positive Hodge eigenvalues under fixed volume and a lower sectional-curvature bound, but their examples have unbounded diameter [1, 2]. A known gap bound under **two-sided** sectional-curvature control does not settle the one-sided version [2, Theorem 6.1].

## Application

A positive answer would make the spectral gap of differential forms stable across noncollapsing geometric families with only a lower sectional-curvature bound. This matters when Hodge theory is used to study geometry through eigenvalues rather than through topology alone.

## References

1. C. Anné and J. Takahashi, [*Small eigenvalues of the rough and Hodge Laplacians under fixed volume*](https://afst.centre-mersenne.org/item/10.5802/afst.1764.pdf), *Ann. Fac. Sci. Toulouse Math.* **33** (2024), no. 1, 123–151, DOI: [10.5802/afst.1764](https://doi.org/10.5802/afst.1764), Remark 3.3.
2. C. Anné and J. Takahashi, [*Small eigenvalues of the Hodge-Laplacian with sectional curvature bounded below*](https://www.math.is.tohoku.ac.jp/~junya/paper/surgery-curv-2025.pdf), *Ann. Global Anal. Geom.* **68** (2025), article 1, DOI: [10.1007/s10455-025-10005-4](https://doi.org/10.1007/s10455-025-10005-4), Theorem 6.1 and Conjecture 6.2.
3. J. Lott, [*Remark about the spectrum of the $`p`$-form Laplacian under a collapse with curvature bounded below*](https://math.berkeley.edu/~lott/S0002-9939-03-07121-1.pdf), *Proc. Amer. Math. Soc.* **132** (2004), 911–918, DOI: [10.1090/S0002-9939-03-07121-1](https://doi.org/10.1090/S0002-9939-03-07121-1), p. 918.

## Status review


**Known cases:** The one-sided sectional-curvature, volume and diameter hypotheses do not include an injectivity-radius bound. The retrieved February 2026 Ricci/injectivity-radius announcement is also officially withdrawn for a mistake in Proposition 3.1; it is not a resolution.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The one-sided sectional-curvature, volume and diameter hypotheses do not include an injectivity-radius bound. The retrieved February 2026 Ricci/injectivity-radius announcement is also officially withdrawn for a mistake in Proposition 3.1; it is not a resolution.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded audit](../FURTHER_problems/_tracking/j282-lott-hodge-eigenvalue-status-2026-10-22.json) compares the original remark, 2024 and 2025 formulations, stronger nearby theorems, and targeted result and announcement searches through 22 October 2026. It found no resolution of this exact one-sided-curvature, bounded-diameter claim.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0bbb4209e527318d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
