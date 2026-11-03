# 802. Minimal sections over noncompact bases in Killing submersions

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\pi:(E^3,g_E)\to(M^2,g_M)`$ be a smooth Riemannian submersion between connected orientable manifolds, with $`M`$ noncompact. Suppose its fibres are the integral curves of a complete nowhere-zero Killing vector field $`\xi`$ on $`E`$. Here Riemannian submersion means that $`d\pi`$ is an isometry on the horizontal subspaces $`(\ker d\pi)^\perp`$.

Must there exist a smooth section
```math
s:M\longrightarrow E,\qquad \pi\circ s=\mathrm{id}_M,
```

whose image has zero mean curvature in $`E`$?

This is Lerma--Manzano's explicit noncompact-base conjecture. The Killing field need not have constant length; its completeness means that its flow exists for every real time. No completeness assumption on the base metric, simple-connectivity, curvature bound, prescribed boundary values, or growth bound is added. The requested object is a section over the whole base. General minimal immersions or sections over proper subdomains do not settle the question.

## Application

A section turns the minimal-surface problem into a nonlinear elliptic graph equation. The conjecture asks whether the topology allowing a section always permits a stationary surface for the geometric area functional.

## References

1. A. M. Lerma and J. M. Manzano, *Compact stable surfaces with constant mean curvature in Killing submersions*, Annali di Matematica Pura ed Applicata 196 (2017), 1345--1364, DOI [10.1007/s10231-016-0619-y](https://doi.org/10.1007/s10231-016-0619-y). [Preprint](https://arxiv.org/abs/1604.00542), Introduction, final paragraph before acknowledgements; Definition 2.1; Proposition 3.3; Theorem 3.6. The compact-base existence result requires that a global section be topologically possible.
2. A. Del Prete, H. Lee and J. M. Manzano, *A duality for prescribed mean curvature graphs in Riemannian and Lorentzian Killing submersions*, Mathematische Nachrichten 297 (2024), 1581--1600, DOI [10.1002/mana.202300282](https://doi.org/10.1002/mana.202300282), Theorem 4.3 and Remark 4.5. The constructions have additional geometry or boundedness hypotheses.
3. A. Del Prete, *Minimal graphs over non-compact domains in 3-manifolds with a Killing vector field*, Results in Mathematics 80 (2025), article 192, DOI [10.1007/s00025-025-02500-8](https://doi.org/10.1007/s00025-025-02500-8), Theorem 3.4 and Remark 3.6: existence on specified convex wedge/strip domains.

4. A. Del Prete, J. M. Manzano and B. Nelli, *The Jenkins--Serrin problem in 3-manifolds with a Killing vector field*, [arXiv:2306.12195](https://arxiv.org/abs/2306.12195), Section 2.1 and Lemma 2.1. The global question is distinguished from existence over relatively compact subdomains.

## Status review


**Known cases:** Jenkins-Serrin and specified wedge or strip constructions impose domain or ambient hypotheses absent from an arbitrary noncompact orientable base and variable-length Killing submersion. No full global-minimal-section result for this class was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Jenkins-Serrin and specified wedge or strip constructions impose domain or ambient hypotheses absent from an arbitrary noncompact orientable base and variable-length Killing submersion. No full global-minimal-section result for this class was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Primary targets, latest versions and subsequent theorem hypotheses were read. No matching target was found in the all-status AIM/OpenAI comparison or the existing further-problem list. Exact-target and announced-solution searches found no complete proof or counterexample through the check date. This records a literature review, not a proof of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-77d47da0c10b1061**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
