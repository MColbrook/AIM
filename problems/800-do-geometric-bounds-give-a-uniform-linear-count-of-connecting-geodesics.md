# 800. Do geometric bounds give a uniform linear count of connecting geodesics?

**Area:** Riemannian geometry and quantitative topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`n\ge3`$, $`k\in\mathbb R`$ and $`v,D>0`$. Let $`M`$ range over simply connected, closed $`n`$-dimensional Riemannian manifolds with sectional curvature at least $`k`$, volume at least $`v`$ and diameter at most $`D`$. **Is there a constant $`C=C(k,v,D,n)`$ such that, for every $`M`$ in this class, every $`p,q\in M`$ and every integer $`m\ge1`$, at least $`m`$ geodesics from $`p`$ to $`q`$ have length at most $`Cm`$?**

This is the unresolved higher-dimensional part of Conjecture 3 in the 22frg800 workshop report contained in the BIRS 2022 proceedings [1, printed p. 229]. The [standalone workshop report](https://www.birs.ca/workshops/2022/22frg800/report22frg800.pdf) labels the same statement Conjecture 2.1. The report asks about geodesics joining $`p`$ and $`q`$; its separate periodic-geodesic proposal adds a geometrically-distinct qualifier that is not part of this question.

## Application

A positive answer would give a linear length bound for a prescribed number of connecting geodesics using only curvature, volume, diameter and dimension data, uniformly across the manifold class.

## Known results and scope

The report [1] cites a general bound of $`4nD\,m^2`$ from Nabutovsky and Rotman [2]. Beach, Contreras-Peruyero, Rotman and Searle [3] obtain a linear bound under an additional quantitative assumption: loops of length at most twice the diameter must contract through curves whose length is controlled by $`c`$ times the diameter. Their coefficient depends on $`c`$ as well as $`k,v,D,n`$, so it does not give the uniform $`C(k,v,D,n)`$ requested here. Their introduction also records a curvature-free linear bound for surfaces; higher dimensions remain the main unresolved range.

## References

1. Banff International Research Station, [*2022 Proceedings*](https://www.birs.ca/files/publications/proceedings/birs_2022_proceedings.pdf), workshop 22frg800, *Cohomogeneity Two Manifolds of Positive Sectional Curvature*, Project 2, Conjecture 3, printed p. 229 (PDF p. 233); [standalone report, Conjecture 2.1](https://www.birs.ca/workshops/2022/22frg800/report22frg800.pdf).
2. A. Nabutovsky and R. Rotman, *Length of geodesics and quantitative Morse theory on loop spaces*, *Geometric and Functional Analysis* **23** (2013), 367–414, as cited in [1]. [DOI](https://doi.org/10.1007/s00039-012-0207-2).
3. I. Beach, H. Contreras-Peruyero, R. Rotman and C. Searle, [*Linear bounds for the lengths of geodesics on manifolds with curvature bounded below*](https://link.springer.com/article/10.1007/s12220-025-02003-6), *Journal of Geometric Analysis* **35** (2025), article 217, abstract and Introduction pp. 1–2; [author/institutional PDF](https://soar.wichita.edu/server/api/core/bitstreams/65c59689-8320-4178-b2d9-ea406983224c/content).

## Status review


**Known cases:** The 2025 uniform linear geodesic-count theorem requires an additional loop-contraction parameter. It does not derive that parameter solely from sectional lower bound, volume lower bound and diameter upper bound. The general dimension-uniform geometric target remains.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2025 uniform linear geodesic-count theorem requires an additional loop-contraction parameter. It does not derive that parameter solely from sectional lower bound, volume lower bound and diameter upper bound. The general dimension-uniform geometric target remains.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [independent source audit](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/birs22frg800-linear-geodesic-length-bounded-audit-20261023.json) and [coordinator review](../FURTHER_problems/_tracking/birs-uniform-geodesic-count-coordinator-audit-2026-10-23.json) check the proceedings passage and the 2025 published comparison for their exact assumptions and constants. The later result retains the extra loop-contraction parameter $`c`$. Bounded current-result, announcement and AIM/FURTHER duplicate searches found no exact unconditional linear bound. These searches do not establish exhaustive absence of a solution, and the proceedings receipt covers only selected passages, not the whole volume.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-773386dd76f6f489**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
