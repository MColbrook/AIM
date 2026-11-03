# 831. Sheaf-theoretic SL(2,C) Floer cohomology detects the three-sphere

**Area:** Geometric topology / complex character varieties
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`Y`$ be a closed, connected, oriented smooth three-manifold with
```math
H_*(Y;\mathbb Z)\cong H_*(S^3;\mathbb Z).
```

Write
```math
X_{\mathrm{irr}}(Y)=
\mathrm{Hom}^{\mathrm{irr}}(\pi_1(Y),\mathrm{SL}(2,\mathbb C))
\big/\mathrm{PSL}(2,\mathbb C)
```

for its irreducible character scheme, with its natural scheme structure. Here an irreducible representation preserves no complex line in $`\mathbb C^2`$.

Use the **unframed** Abouzaid–Manolescu invariant. More precisely, choose a Heegaard splitting $`Y=U_0\cup_\Sigma U_1`$ of genus at least three. The handlebody character varieties
```math
L_i=X_{\mathrm{irr}}(U_i)\subset X_{\mathrm{irr}}(\Sigma)
```

are complex Lagrangians, and $`L_0\cap L_1=X_{\mathrm{irr}}(Y)`$. Their canonical spin structures give the perverse sheaf of vanishing cycles $`\mathcal P(Y)`$ constructed in [1]. It is canonically independent of the splitting. Set
```math
HP^k(Y;\mathbb Z)
=\mathbb H^k(X_{\mathrm{irr}}(Y),\mathcal P(Y)),
\qquad k\in\mathbb Z,
```

using ordinary hypercohomology, without compact supports.

Does
```math
HP^k(Y;\mathbb Z)=0\quad\text{for every }k\in\mathbb Z
\qquad\Longrightarrow\qquad
Y\cong S^3
```

hold for every such $`Y`$? The reverse implication follows from
$`X_{\mathrm{irr}}(S^3)=\varnothing`$.

## Application

This would connect recognition of the three-sphere with the algebraic geometry of complex flat connections. The question concerns a mathematical characterization; no practical computational complexity bound is asserted.

## References

1. M. Abouzaid and C. Manolescu, *A sheaf-theoretic model for SL(2,C) Floer homology*, Journal of the European Mathematical Society **22** (2020), 3641–3695, [DOI](https://doi.org/10.4171/jems/994). [arXiv:1708.00289v2](https://arxiv.org/abs/1708.00289v2), Theorem 1.1, §4.2 and Question 9.1, native pp. 2, 19 and 41. [Current author copy](https://web.stanford.edu/~cm5/SL2.pdf).
2. R. Zentner, *Integer homology 3-spheres admit irreducible representations in SL(2,C)*, Duke Mathematical Journal **167** (2018), 1643–1712, [DOI](https://doi.org/10.1215/00127094-2018-0004), Theorem 9.4. [arXiv:1605.08530](https://arxiv.org/abs/1605.08530).
3. I. Neithalath, *SL(2,C) Floer cohomology for surgeries on some knots*, Michigan Mathematical Journal **73** (2023), 925–950, [DOI](https://doi.org/10.1307/mmj/20216036). [arXiv:2002.04103v3](https://arxiv.org/abs/2002.04103v3), Theorems 1–4, native pp. 1–2.
4. Z.-C. Ong and M.-C. Tan, *Vafa-Witten Theory: Invariants, Floer Homologies, Higgs Bundles, a Geometric Langlands Correspondence, and Categorification*, Advances in Theoretical and Mathematical Physics **27** (2023), 1759–1812, [DOI](https://doi.org/10.4310/ATMP.2023.v27.n6.a3). [arXiv:2203.17115v5](https://arxiv.org/abs/2203.17115v5), §5.3, native pp. 31–32.

5. A. Pedroza, *A Quick View of Lagrangian Floer Homology*, [arXiv:1701.02293v1](https://arxiv.org/abs/1701.02293v1) (2017), Theorems 10–11, native pp. 19–20.

## Status review


**Known cases:** Nonempty irreducible SL2 character schemes do not imply nonzero hypercohomology of the vanishing-cycle sheaf. Special surgery calculations and proposed comparisons with a different instanton theory do not prove general detection by the unframed Abouzaid-Manolescu invariant.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Nonempty irreducible SL2 character schemes do not imply nonzero hypercohomology of the vanishing-cycle sheaf. Special surgery calculations and proposed comparisons with a different instanton theory do not prove general detection by the unframed Abouzaid-Manolescu invariant.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Question 9.1 of [1] explicitly asks this detection question. Its hypotheses matter: the same paper computes $`HP^*=0`$ for lens spaces, so one cannot extend the statement to all rational homology spheres. It also computes nonzero invariants for the indicated Brieskorn spheres.

Zentner's theorem [2] shows that $`X_{\mathrm{irr}}(Y)`$ is nonempty whenever an integral homology sphere $`Y`$ differs from $`S^3`$. Existence of irreducible representations alone does not establish nonvanishing of the sheaf's hypercohomology. Neithalath's calculations [3] treat specified knot surgeries, with the small-knot result excluding boundary slopes; they do not cover all integral homology spheres.

The comparison with complex instanton Floer homology discussed in [4] concerns a different Abouzaid–Manolescu conjecture. The ordinary-cohomology theorem used in its intermediate comparison is a self-Floer result, with Hamiltonian-perturbation, compactness and area hypotheses [5, Theorems 10–11]. Those hypotheses require separate justification for two Heegaard Lagrangians in a noncompact character variety. This comparison does not establish general sphere detection.

The latest arXiv versions, current author copy, relevant later literature and online announcements were checked on 24 October 2026. No solution of this exact implication was located. This is a literature and statement comparison, not an independent proof audit of the cited papers.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b38f83452c83b3c3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
