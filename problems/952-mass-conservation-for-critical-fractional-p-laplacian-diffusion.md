# 952. Mass conservation for critical fractional p-Laplacian diffusion

**Area:** Nonlinear nonlocal diffusion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`N\ge2`$, let

```math
\frac{N}{2N-1}\le s<1,\qquad p=p_c=\frac{2N}{N+s}.
```


For every nonnegative $`u_0\in L^1(\mathbb R^N)`$, let $`u(t)=S_tu_0`$ be the standard $`L^1`$ contraction-semigroup solution of

```math
\partial_tu+\mathcal L_{s,p}u=0,\qquad
 \mathcal L_{s,p}f(x)=\mathrm{PV}\int_{\mathbb R^N}
 \frac{\Phi_p(f(x)-f(y))}{|x-y|^{N+sp}}\,dy,
```


where $`\Phi_p(r)=|r|^{p-2}r`$ for $`r\ne0`$ and $`\Phi_p(0)=0`$.
Must

```math
\int_{\mathbb R^N}u(x,t)\,dx
 =\int_{\mathbb R^N}u_0(x)\,dx
 \qquad\text{for every }t>0?
```


The parameter range is exactly the remaining critical regime $`sp\ge1`$, including equality. There is no such remaining range in dimension one.

For precision, $`S_t`$ is the $`L^1`$ extension by contraction of the $`L^2`$ gradient flow of the lower semicontinuous convex energy

```math
E(f)=\frac1{2p}\iint_{\mathbb R^N\times\mathbb R^N}
       \frac{|f(x)-f(y)|^p}{|x-y|^{N+sp}}\,dx\,dy,
```


with $`E=+\infty`$ outside its finite-energy domain. Thus $`S_tu_0`$ is the $`L^1`$ limit of the flows for nonnegative $`L^1\cap L^2`$ approximations to $`u_0`$ [3, Section 2.1]. Pointwise principal values need not exist for every datum. No compact support, boundedness, radial symmetry or moment condition is assumed.

## Application

This determines whether critical nonlinear diffusion can transport a positive amount of finite initial mass to spatial infinity in finite time.

## Known progress

Mass conservation holds for $`p>p_c`$ [3, Theorem 5.1] and for $`p=p_c`$ with $`sp<1`$ [2, Theorem 9.1]. The latter theorem's proof and following open problem explicitly retain the complementary range. The expanded survey does likewise [1, Open Problem 4]. Contractivity provides an upper bound on mass, so equality remains the issue.

Results for the local $`p`$-Laplacian, spectral fractional porous-medium equations, time-fractional equations or Dirac initial measures do not settle this function-data semigroup question.

## References

1. J. L. Vázquez, *A survey on mass conservation, self-similarity and related topics in nonlinear diffusion*, [arXiv:2311.18357v2](https://arxiv.org/html/2311.18357v2), Section 12.2, Theorem 12.4 and Open Problem 4; revised 23 December 2025. [Journal DOI](https://doi.org/10.4171/EMSS/121), online first 14 October 2026. The checked author version governs the statement here.
2. J. L. Vázquez, *Growing solutions of the fractional p-Laplacian equation in the Fast Diffusion range*, Nonlinear Analysis 214 (2022), 112575, [DOI](https://doi.org/10.1016/j.na.2021.112575), [published text](https://repositorio.uam.es/bitstream/handle/10486/700583/growing_vazquez_NA_2021.pdf?sequence=1), Theorem 9.1 and following open problem, pp.30–32.
3. J. L. Vázquez, *The fractional p-Laplacian evolution equation in R^N in the sublinear case*, Calculus of Variations and Partial Differential Equations 60 (2021), Paper 140; [arXiv:2011.01521v2](https://arxiv.org/html/2011.01521v2), Sections 2.1 and 5.

## Status review


**Known cases:** The remaining critical regime has sp>=1. The October 2026 survey still identifies the critical gap; supercritical mass conservation and the critical sp<1 theorem are outside this residual.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The remaining critical regime has sp>=1. The October 2026 survey still identifies the critical gap; supercritical mass conservation and the critical sp<1 theorem are outside this residual.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Independent primary-statement review and current searches on 25 October 2026 found no matching resolution or complete announcement. The review included all 1,703 pinned AIM/OpenAI statement records and all 911 preceding local findings. In particular, AIM473 concerns a different spectral fractional porous-medium operator. These bounded checks do not certify every proof or parity between the published 2026 survey and its expanded author version.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b762cb1cf883ff40**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
