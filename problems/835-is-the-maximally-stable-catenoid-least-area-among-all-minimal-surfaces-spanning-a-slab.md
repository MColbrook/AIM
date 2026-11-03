# 835. Is the maximally stable catenoid least-area among all minimal surfaces spanning a slab?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`P_-`$ and $`P_+`$ be two distinct parallel planes in $`\mathbb R^3`$, with open slab $`\Omega`$ between them. Bernstein and Breiner [1, p. 2] define $`\mathcal M(\Omega)`$ as the smooth minimal surfaces spanning these planes: a surface $`\Sigma\subset\Omega`$ is given by a conformal harmonic immersion of an open orientable surface, and its closure-boundary $`\overline\Sigma\setminus\Sigma`$ lies in $`P_-\cup P_+`$. This class allows topology and boundary behaviour beyond embedded annuli.

Let $`C_{\rm ms}\in\mathcal M(\Omega)`$ be the *maximally stable catenoidal waist* scaled to the slab, unique up to translation parallel to its boundary planes. Is

```math
\mathcal H^2(\Sigma)\geq\mathcal H^2(C_{\rm ms})
\quad\text{for every }\Sigma\in\mathcal M(\Omega),
```


with equality only when $`\Sigma`$ is a horizontal translate of $`C_{\rm ms}`$? This is [1, Conjecture 1.2]. Infinite-area surfaces satisfy the inequality trivially; the issue is the finite-area competitors outside the annular class. The source's Theorem 1.1 proves the assertion for the embedded minimal annuli $`\mathcal A(\Omega)\subset\mathcal M(\Omega)`$.

## Application

The question asks whether the catenoid's area bound is independent of a minimal surface's topology or the way its horizontal sections wind. Such bounds help distinguish geometric minimizers from other stationary soap-film configurations between planes.

## References

1. J. Bernstein and C. Breiner, [*A variational characterization of the catenoid*](https://arxiv.org/pdf/1012.3941v1), arXiv:1012.3941v1, PDF pp. 2–3, definition of $`\mathcal M(\Omega)`$, Theorem 1.1 and Conjecture 1.2; *Calculus of Variations and Partial Differential Equations* **49** (2014), 215–232, [DOI](https://doi.org/10.1007/s00526-012-0579-z).
2. J. Choe and B. Daniel, [*On the area of minimal surfaces in a slab*](https://arxiv.org/pdf/1503.02771), arXiv:1503.02771, Theorem 2.1 and closing Problems, *International Mathematics Research Notices* **2016** (2016), 7201–7211, [DOI](https://doi.org/10.1093/imrn/rnv386). Their extension requires all horizontal-section components to have the same orientation.
3. E. Matinpour, [*On the area of immersed minimal annuli in a slab*](https://arxiv.org/abs/2410.15535), *Journal of the Korean Mathematical Society* **62** (2025), 1101–1125, [DOI](https://doi.org/10.4134/JKMS.j240379). This concerns the annular class and winding numbers.

## Status review


**Known cases:** The known slab-area extensions require the same orientation for all horizontal section components or restrict to annuli. Mixed-orientation and general-topology competitors remain outside those theorems; the general Bernstein-Breiner conjecture was not matched by a complete result.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known slab-area extensions require the same orientation for all horizontal section components or restrict to annuli. Mixed-orientation and general-topology competitors remain outside those theorems; the general Bernstein-Breiner conjecture was not matched by a complete result.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The same-orientation extension [2] leaves mixed-orientation sections and other unrestricted competitors untreated, while [3] remains annular. A [bounded status and duplicate audit](../FURTHER_problems/_tracking/w001-bernstein-breiner-full-slab-catenoid-area-status-2026-10-22.json) through 22 October 2026 found no matching full-class proof, counterexample or announcement.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b9934b396e984e8a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
