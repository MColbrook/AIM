# 874. A parallel null direction in higher-order symmetric spacetimes

**Area:** Mathematical relativity / Lorentzian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`r\ge4`$ and $`n\ge3`$ be integers. Let $`(M^n,g)`$ be a connected simply connected smooth Lorentzian manifold, with Levi-Civita connection $`\nabla`$ and Riemann curvature tensor $`R`$. Suppose

```math
\nabla^rR=0,
\qquad \nabla^{r-1}R\not\equiv0.
```

Here $`\nabla^jR`$ is the full iterated covariant derivative, with no symmetrization. Must there exist a smooth vector field $`V`$ on $`M`$ such that

```math
V_p\ne0\quad(p\in M),\qquad
g(V,V)=0,\qquad \nabla V=0?
```

The hypothesis is called **proper $`r`$th-order symmetry**. It differs from the terminology for spaces whose symmetries have finite order. Completeness, compactness, homogeneity and the Einstein equation are not assumed. Simply connectedness removes the separate obstruction of transporting a local parallel vector around a topological loop.

## Application

Curvature measures relative acceleration of nearby freely falling trajectories. Higher-order symmetry restricts its variation along such trajectories to a finite polynomial hierarchy. A parallel null field would place these spacetimes in the Brinkmann class and provide a distinguished direction along which the geometry can be analyzed.

## Known results

The analogous assertion is proved for proper orders $`2`$ and $`3`$. Known examples for every higher order are plane-wave metrics with polynomial profile; they have the required null field. These examples do not classify every metric satisfying the displayed curvature condition.

The target is the existence of $`V`$. A full classification as a polynomial-profile plane wave with locally symmetric factors is a further question and is not asserted to follow from the existence statement alone.

## References

1. J. M. M. Senovilla, *Semi-Riemannian manifolds with linear differential conditions on the curvature*, *Analysis and Mathematical Physics* **14** (2024), article 63. [Published article](https://doi.org/10.1007/s13324-024-00923-0), [published PDF](https://inspirehep.net/files/1f91c296bc3c5c8f6ec16a0f104884ce). Proper higher-order symmetry is defined on p. 20; Theorems 9–10 and the precise unresolved $`r\ge4`$ discussion are on pp. 23–24; §6 revisits this direction on p. 28. This journal article is eligible through registered source J257.
2. A. S. Galaev, *Classification of third-order symmetric Lorentzian manifolds*, *Classical and Quantum Gravity* **32** (2015), 025001. [DOI](https://doi.org/10.1088/0264-9381/32/2/025001), [eligible author preprint](https://arxiv.org/pdf/1407.3594v1). Introduction, Theorem 3 and Conclusion, pp. 1–2 and 10–11 in the preprint: the order-three theorem and higher-order conjectural extension. The final 15-page edition was not compared in full.

3. S. Greenwood and T. Leistner, *Lorentzian homogeneous structures with indecomposable holonomy*, Journal of the London Mathematical Society **113** (2026), e70551, [DOI](https://doi.org/10.1112/jlms.70551), Theorem 1.4 and §2.1. The second-order condition is on a specified metric connection, which may have torsion.

## Status review


**Known cases:** Third-order symmetry and second-order torsion-connection results do not prove a parallel null direction for every proper Levi-Civita order at least four. The higher-order discussion in the current primary survey remains conjectural.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Third-order symmetry and second-order torsion-connection results do not prove a parallel null direction for every proper Levi-Civita order at least four. The higher-order discussion in the current primary survey remains conjectural.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Searches of primary publications and announcements on 17 October 2026 located no proof or counterexample for all stated orders and dimensions. Recent results for a second-order symmetric metric connection with torsion have an additional curvature hypothesis on that connection; they do not establish the displayed condition for the Levi-Civita connection at orders $`r\ge4`$.

Independent selected-primary review passed. All 186 cached catalogue pages were compared with six target aliases, with no matches. This is a bounded listing-description comparison, not review of every linked mission proof.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/higher-symmetric-null-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-higher-symmetric-null-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/higher-symmetric-null-duplicate-snapshot.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/higher-symmetric-null-prove2-0137-review.json) and [coordinator review](../FURTHER_problems/_tracking/higher-symmetric-null-coordinator-review-2026-10-17.json) preserve exact scope and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-243f17e527071c0c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
