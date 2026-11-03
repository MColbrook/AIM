# 864. Does regular quantization force a compact Kähler metric to be homogeneous?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a compact connected complex manifold of dimension $`n\ge1`$, with Kähler form $`\omega`$ and associated metric $`g_\omega`$. Suppose a positive holomorphic line bundle $`L\to M`$ has a smooth Hermitian metric $`h`$ with curvature
```math
-\frac{i}{2\pi}\partial\bar\partial\log h(e,e)=\omega
```

in each local nonvanishing holomorphic frame $`e`$.

For each positive integer $`m`$, equip $`H^0(M,L^m)`$, the space of global holomorphic sections, with
```math
\langle s,t\rangle_m=
 \int_M h^m(s,t)\frac{\omega^n}{n!}.
```

For an orthonormal basis $`s_{m,1},\ldots,s_{m,N_m}`$, define the basis-independent Rawnsley distortion function
```math
\rho_m(x)=\sum_{j=1}^{N_m}h^m(s_{m,j}(x),s_{m,j}(x)).
```

Assume that $`\rho_m`$ is a positive constant on $`M`$ for **every sufficiently large integer $`m`$**. This is regular quantization of the fixed metric.

Must the group of global holomorphic isometries
```math
\mathrm{Aut}(M)\cap\mathrm{Isom}(M,g_\omega)
```

act transitively on $`M`$?

The same $`\omega`$, $`L`$ and $`h`$ are used throughout. No Einstein, toric, first-Chern-ray, curvature-sign or simple-connectivity assumption is made. Existence of a varying sequence of balanced metrics approximating $`g_\omega`$ is a different premise.

## Application

Regular quantization asks for spatially uniform distortion at every sufficiently fine quantization scale. The question would determine whether this exact uniformity forces a global geometric symmetry of a compact phase space.

## References

- F. Cannas Aghedu and A. Loi, *The Simanca metric admits a regular quantization*, **Annals of Global Analysis and Geometry** 56 (2019), 583–596. [Published article](https://doi.org/10.1007/s10455-019-09680-x); [arXiv:1809.04431v4](https://arxiv.org/html/1809.04431v4), Introduction, regular-quantization definition, footnote 2 and compact-case question.
- S. Huang, *Generalized Einstein Laurent polynomials, Toric Kähler–Einstein Rigidity, and Finite Exponential Families* (September 2026 working paper), [arXiv:2609.18067v1](https://arxiv.org/html/2609.18067v1), Corollary 6.8 and the end of Section 6.5.

## Status review


**Known cases:** The September 2026 toric positive-first-Chern-ray theorem explicitly retains unrestricted regular quantization. Noncompact Simanca examples do not refute compact homogeneity, and varying balanced approximations do not imply the fixed-metric regular-quantization premise.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September 2026 toric positive-first-Chern-ray theorem explicitly retains unrestricted regular quantization. Noncompact Simanca examples do not refute compact homogeneity, and varying balanced approximations do not imply the fixed-metric regular-quantization premise.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. The source explicitly leaves the compact question open. Its nonhomogeneous Simanca example is noncompact and does not answer this formulation.

The September 2026 working paper announces a positive result for compact smooth toric manifolds under an additional positive first-Chern-ray condition, and explicitly retains the unrestricted regular-quantization question. That announcement is compared for scope, without independently certifying its proof.

No matching general resolution or complete announcement was located in current searches. Semantic checks against the AIM/OpenAI all-status corpus and developing collection distinguished tangent splitting, contact/Fano classifications, Hermitian balanced forms and local homogeneity of complex-bilinear metrics. No equivalent target was found; this is a dated check rather than a guarantee against an unlocated result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f506b96e1e501d68**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
