# 649. Must positive finite density for an arbitrary norm have integer dimension in dimension three and higher?

**Area:** Geometric measure theory and normed geometry
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq3`$, let $`\lVert\cdot\rVert`$ be any norm on $`\mathbb R^n`$, and let $`\mu`$ be a nonzero Radon measure. Suppose that for some $`\alpha>0`$,

```math
0<\lim_{r\downarrow0}\frac{\mu(B_{\lVert\cdot\rVert}(x,r))}{r^\alpha}<\infty\qquad\text{for }\mu\text{-almost every }x.
```


**Must $`\alpha`$ be an integer?** The norm, measure and exponent are arbitrary subject to these assumptions. This is the unresolved higher-dimensional scope of De Lellis's Conjecture 10.9. The Euclidean result is classical; Del Nin and Merlo proved the arbitrary-norm assertion in the plane in 2025. Their discussion explicitly leaves extension to higher-dimensional normed spaces open.

## Application

Positive finite small-ball density is a basic signal of dimension and geometric structure of a measure. Knowing that its exponent must be integral for every norm would support rectifiability theory beyond Euclidean metrics and identify which metric features are essential to density theorems.

## References

1. C. De Lellis, [*Rectifiable Sets, Densities, and Tangent Measures*](https://www.math.ias.edu/delellis/sites/math.ias.edu.delellis/files/Delellis_note136_corrected.pdf), Zürich Lectures in Advanced Mathematics, EMS (2008), DOI 10.4171/044, Chapter 10, p.112, Conjecture 10.9. This is the author-hosted corrected PDF linked to the [publisher's book record](https://ems.press/books/zlam/43); publisher chapter bytes were unavailable for parity comparison.
2. G. Del Nin and A. Merlo, [*Marstrand's density theorem for arbitrary norms in the plane*](https://arxiv.org/html/2508.15400), arXiv:2508.15400v1 (2025), Introduction, Theorem 1.1 and §1.3. Proves the planar case and discusses the remaining higher-dimensional difficulty.
3. B. Wilson, [*Density properties of sets in finite-dimensional, strictly convex Banach spaces*](https://doi.org/10.1016/j.jmaa.2025.129342), *Journal of Mathematical Analysis and Applications* **548** (2025), article 129342. Its integer-dimensional rectifiability setting is distinct from the noninteger-exponent question above.

## Status review

The 2025 planar theorem does not settle arbitrary norms on $`\mathbb R^n`$ for $`n\geq3`$. The [bounded source, announcement and semantic-duplicate review](../FURTHER_problems/_tracking/marstrand-arbitrary-norm-higher-dimension-status-2026-10-21.json) found no matching complete result or existing AIM/FURTHER item; it cannot exclude an unindexed announcement.


### Online recheck, 2026-10-30

The arbitrary-norm theorem is planar. Higher-dimensional Euclidean density integrality and fixed-integer-dimensional rectifiability in strictly convex Banach spaces do not prove integrality for all norms in dimension >=3.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2508.15400); [status source 2](https://doi.org/10.1016/j.jmaa.2025.129342). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-96180d4336b97a08** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
