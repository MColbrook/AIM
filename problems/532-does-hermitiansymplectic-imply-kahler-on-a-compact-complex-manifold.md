# 532. Does Hermitian–symplectic imply Kähler on a compact complex manifold?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,J)`$ be a compact complex manifold of complex dimension $`n\ge3`$. Suppose there is a real closed two-form $`\Omega`$ such that

```math
\Omega(v,Jv)>0\qquad\text{for every nonzero real tangent vector }v.
```

Must $`X`$ admit a Kähler metric? Equivalently, can a compact non-Kähler complex manifold carry such a **Hermitian–symplectic** form? The Kähler metric sought need not be the $`(1,1)`$ part of the given $`\Omega`$.

## Application

The question asks whether a symplectic form that tames an integrable complex structure forces Kähler geometry on a compact manifold. A positive answer would rule out this intermediate structure on all non-Kähler compact complex manifolds; a counterexample would separate two central notions in complex and symplectic geometry.

## References

1. J. Streets and G. Tian, *A parabolic flow of pluriclosed metrics*, International Mathematics Research Notices **2010**(16), 3101–3133, Definition 1.5 and Question 1.7 in [arXiv:0903.4418v2, physical pp. 4–5](https://arxiv.org/pdf/0903.4418v2); [publisher](https://doi.org/10.1093/imrn/rnp237).
2. N. Enrietti, A. Fino and L. Vezzoni, *Hermitian-symplectic structures and SKT metrics*, [arXiv:1002.3099v1](https://arxiv.org/pdf/1002.3099v1), abstract and §1, physical pp. 1–2; explicit compact formulation and nilmanifold obstruction.
3. K. Cao and F. Zheng, *Streets–Tian conjecture on Lie algebras with codimension 2 abelian ideals*, [arXiv:2410.04791](https://arxiv.org/abs/2410.04791); a restricted Lie-group case.
4. S. Chen and F. Zheng, *Streets–Tian conjecture holds for 2-step solvmanifolds*, Journal of Geometry and Physics **209** (2025), article 105390; [publisher](https://www.sciencedirect.com/science/article/abs/pii/S0393044024002912), [author preprint](https://arxiv.org/abs/2410.10540), stating the general dimension-three-and-higher question remains open while proving this subclass.
5. K. Cao and S. Chen, *The Streets–Tian conjecture on compact homogeneous quotients*, [arXiv:2610.25229v1](https://arxiv.org/html/2610.25229v1) (18 October 2026), Theorem 1 and Corollary 2; a recent preprint claiming a wider homogeneous-quotient case, still short of arbitrary compact complex manifolds.

## Status review


**Known cases:** The October 2026 Streets–Tian announcement assumes compact homogeneous quotient structure. Nilmanifold, solvmanifold and surface cases leave arbitrary compact complex manifolds of dimension >=3 outside their scope.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Reviewed 21 October 2026. Complex dimension two is settled. The known nilmanifold, solvmanifold and other geometric-class results impose extra structure. The paper posted on 18 October 2026 claims another substantial special case under homogeneity and quotient hypotheses; its proof has not been independently certified here, and its stated result does not answer the unrestricted question. Merely assuming a pluriclosed metric is weaker than the hypothesis above.

No equivalent question was found in AIM or the admitted FURTHER list. The [dated current-status and duplicate audit](../FURTHER_problems/_tracking/streets-tian-hermitian-symplectic-status-2026-10-21.json) records the exact scope of the cited claims and the bounded search, which cannot rule out unindexed work.


### Online recheck, 2026-10-30

The October 2026 Streets–Tian announcement assumes compact homogeneous quotient structure. Nilmanifold, solvmanifold and surface cases leave arbitrary compact complex manifolds of dimension >=3 outside their scope.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.25229); [status source 2](https://arxiv.org/abs/2410.10540); [status source 3](https://arxiv.org/abs/0903.4418). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-439ec2676e6cc7be** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
