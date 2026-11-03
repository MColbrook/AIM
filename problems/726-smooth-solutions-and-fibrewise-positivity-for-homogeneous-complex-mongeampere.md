# 726. Smooth solutions and fibrewise positivity for homogeneous complex Monge–Ampère

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb D\subset\mathbb C`$ be the unit disc, and let $`\omega_{\mathrm{FS}}`$ be the Fubini–Study form on $`\mathbb P^1`$, normalized to have area one. Write $`\pi:\mathbb P^1\times\overline{\mathbb D}\to\mathbb P^1`$ for projection.

Does there exist a real function $`\varphi\in C^\infty(\mathbb P^1\times\partial\mathbb D)`$ such that

```math
\omega_{\mathrm{FS}}+dd^c_z\varphi(\cdot,\tau)>0
\qquad(\tau\in\partial\mathbb D),
```

but the unique weak Dirichlet solution

```math
\Omega:=\pi^*\omega_{\mathrm{FS}}+dd^c\Phi\ge0,
\qquad \Omega^2=0,
\qquad \Phi|_{\mathbb P^1\times\partial\mathbb D}=\varphi
```

is smooth on $`\mathbb P^1\times\overline{\mathbb D}`$ and its fibre form

```math
\omega_{\mathrm{FS}}+dd^c_z\Phi(\cdot,\tau_0)
```

vanishes at some point $`z_0\in\mathbb P^1`$, for some $`\tau_0\in\mathbb D`$?

Here $`d^c=\frac{i}{4\pi}(\bar\partial-\partial)`$. The weak solution is the plurisubharmonic Perron envelope; the equation uses the Bedford–Taylor product. The boundary family is arbitrary and need not have rotational symmetry.

This uses the source's definition of maximal rank as strict positivity in the fibre directions. It does not require the total form $`\Omega`$ to vanish at the point of degeneration.

## Application

The equation describes families of Kähler metrics and is related to their geodesic equation. This question separates smoothness of a potential from positivity of the metric it defines on each fibre.

## References

1. J. Ross and D. Witt Nyström, *On the maximal rank problem for the complex homogeneous Monge–Ampère equation*, Analysis & PDE **12** (2019), 493–503. [Published PDF](https://msp.org/apde/2019/12-2/apde-v12-n2-p07-s.pdf), definition on p. 493, standing setup in §2B on p. 495, and Question 3.2 in §3B on p. 501. [Preprint](https://arxiv.org/abs/1610.02280).
2. J. Hu, *A metric lower bound estimate for geodesics in the space of Kähler potentials*, Journal of Geometric Analysis **34** (2024), [DOI](https://doi.org/10.1007/s12220-024-01654-1). [Preprint](https://arxiv.org/pdf/2208.13651v1), Theorems 1.1–1.2 on p.4 require small boundary data; selected preprint comparison only.

## Status review


**Known cases:** Existing degeneration examples lack the requested global smoothness. Small-boundary-data lower bounds and flat-affine or annulus results do not decide a smooth fibre-degenerate solution on P1 times the closed disc for arbitrary positive boundary data.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Existing degeneration examples lack the requested global smoothness. Small-boundary-data lower bounds and flat-affine or annulus results do not decide a smooth fibre-degenerate solution on P1 times the closed disc for arbitrary positive boundary data.

Additional comparison sources: [comparison source 1](https://msp.org/apde/2019/12-2/apde-v12-n2-p07-s.pdf); [comparison source 2](https://arxiv.org/abs/1610.02280); [comparison source 3](https://doi.org/10.1007/s12220-024-01654-1); [comparison source 4](https://arxiv.org/pdf/2208.13651v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The first source constructs weak solutions that degenerate on an open set, and retains the additional smoothness question. The metric lower bound theorem inspected here assumes small boundary data. Highly regular nonsmooth examples on a flat torus with annulus parameter have a different setup.

Checked 17 October 2026. Independent selected-primary review confirmed the fibrewise definition, the fixed projective-line/disc setting and the global smoothness requirement. The later regularity theorem inspected in Hu’s 2019 manuscript already assumes strict fibre positivity. Hu’s 2025 flat-affine result excludes the projective line, and Yao’s 2025 compact-manifold statement requires small boundary data. None of those inspected statements answers the arbitrary-boundary-data question above.

All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. The fresh Prove2Me snapshot reconciles 4,629 distinct listings on 186 pages. Its eleven rank-related matching contexts concern tensor degenerations, secretary rankings or finite-field rank-metric codes. No matching announcement was found in the dated searches. This is a comparison of public listing descriptions, not all mission proofs.

The published 2019 source was read in full. Later status papers were inspected only to the extents recorded in the [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/smooth-hmae-rank-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-smooth-hmae-rank-review.json); several published-version parity checks and the original Donaldson article body remain access gaps. The [fresh catalogue comparison](../FURTHER_problems/_tracking/fresh-catalogue-riccati-skt-rank-review.json) records the website check. These are bounded status checks, not a proof that every possible announcement has been found.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-eee53365fdf11c4f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
