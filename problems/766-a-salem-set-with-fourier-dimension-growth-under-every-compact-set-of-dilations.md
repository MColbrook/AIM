# 766. A Salem set with Fourier-dimension growth under every compact set of dilations

**Area:** Fractal geometry and harmonic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`d\geq1`$ and every $`\alpha\in[0,d]`$, does there exist a **single** compact set $`Y\subset\mathbb R^d`$ with

```math
\dim_FY=\dim_HY=\overline{\dim}_M Y=\alpha
```


such that, for **every** nonempty compact set $`R\subset(0,\infty)`$,

```math
\dim_F(RY)\geq\min\{d,\dim_F R+\alpha\},\qquad RY=\{ry:r\in R,\ y\in Y\}?
```


Here $`\dim_F`$, $`\dim_H`$ and $`\overline{\dim}_M`$ denote Fourier, Hausdorff and upper Minkowski dimensions. The order of quantifiers is essential: $`Y`$ must work simultaneously for all $`R`$. This is Conjecture 1.5 of the published Hambrook–Taylor paper. Its original arXiv v1 Conjecture 1.11 asked the slightly weaker question without the upper Minkowski equality.

## Application

The question seeks a compact Salem set whose Fourier dimension gains the dimension of *any* family of scalar dilations, up to the ambient dimension. Such a set would give a uniform ingredient for studying dimensions and measures of scaled sums $`RY+Z`$.

## Known results and scope

Hambrook and Taylor prove the stated Fourier bound for each fixed $`R`$ in dimension one with a set $`Y`$ that **may depend on $`R`$** (Theorem 1.6). That theorem does not produce the one set required here. Their sphere example has the desired dilation bound at its specific dimension $`d-1`$. Later explicit Salem-set constructions do not, in the checked primary statements, establish this universal product property.

## References

1. K. Hambrook and K. Taylor, [*Measure and Dimension of Sums and Products*](https://doi.org/10.1090/proc/15513), *Proceedings of the American Mathematical Society* **149** (2021), 3765–3780, Conjecture 1.5, Eq. (1.1), Proposition 1.4 and Theorem 1.6. [Author-hosted published PDF](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/0/26656/files/2024/04/Hambrook-a823300942f78993.pdf).
2. K. Hambrook and K. Taylor, [arXiv:1810.11553v1](https://arxiv.org/abs/1810.11553v1), Conjecture 1.11; [v2](https://arxiv.org/abs/1810.11553v2), Conjecture 1.5.
3. J. M. Fraser and K. Hambrook, [*Explicit Salem Sets in $`\mathbb R^n`$*](https://arxiv.org/abs/1909.04581), *Advances in Mathematics* **416** (2023), 108901. An explicit-existence result, with a different target.

## Status review


**Known cases:** The same Salem set must work for every compact dilation set and have upper Minkowski dimension alpha as well. Pair-dependent constructions, explicit Salem existence and sum/product estimates with a different quantifier order do not establish the universal-set assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The same Salem set must work for every compact dilation set and have upper Minkowski dimension alpha as well. Pair-dependent constructions, explicit Salem existence and sum/product estimates with a different quantifier order do not establish the universal-set assertion.

Additional comparison sources: [comparison source 1](https://doi.org/10.1090/proc/15513); [comparison source 2](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/0/26656/files/2024/04/Hambrook-a823300942f78993.pdf); [comparison source 3](https://arxiv.org/abs/1810.11553v1); [comparison source 4](https://arxiv.org/abs/1810.11553v2); [comparison source 5](https://arxiv.org/abs/1909.04581). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published source states the universal-set assertion as a conjecture and proves a weaker quantifier order. Targeted checks of later primary work and proof, counterexample and announcement searches through 23 October 2026 found no matching full resolution. A semantic check found no matching AIM or admitted FURTHER problem. These are bounded searches, not a guarantee that no result exists. The [source and status audit](../FURTHER_problems/_tracking/hambrook-taylor-afree-admission-audit-2026-10-23.json) records exact version locators and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0e237ae6f5e14b3c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
