# 571. Sharp few-distance bound for arbitrary normed spaces

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d,k\ge1`$ be integers and let $`(X,\|\cdot\|)`$ be an arbitrary real normed vector space of dimension $`d`$. For a finite set $`S\subset X`$, put

```math
D(S)=\{\|x-y\|:x,y\in S,\ x\ne y\}.
```

If $`|D(S)|\le k`$, must

```math
|S|\le(k+1)^d?
```

Moreover, if $`|S|=(k+1)^d`$, must the closed unit ball $`B_X=\{x:\|x\|\le1\}`$ be a **parallelotope**, meaning a linear image of $`[-1,1]^d`$ under an invertible linear map?

Both claims quantify over every real norm and every finite $`S`$. No Euclidean, smoothness, strict-convexity or lattice assumption is imposed. Only nonzero pairwise distances are counted. The original exactly-$`k`$ formulation gives the displayed at-most-$`k`$ version by applying it to the actual number of distances; equality in the displayed bound forces that number to be $`k`$.

The converse extremal construction is known: if $`B_X=T[-1,1]^d`$, then $`T\{0,1,\ldots,k\}^d`$ has $`(k+1)^d`$ points and exactly $`k`$ nonzero distances. This asserts the existence of an extremal set in that norm; it does not assert equality for every finite set.

## Application

This links the number of distances in a finite configuration to the convex geometry of its norm ball. The equality question asks whether the largest possible configurations identify precisely the norms linearly isometric to the maximum norm.

## References

1. K. J. Swanepoel, [Cardinalities of $`k`$-distance sets in Minkowski spaces](https://arxiv.org/html/0712.0953v1), *Discrete Mathematics* **197–198** (1999), 759–767; arXiv:0712.0953v1, Conjecture 1 and Theorems 1 and 3.
2. K. J. Swanepoel, [Combinatorial distance geometry in normed spaces](https://arxiv.org/html/1702.00066v2), in *New Trends in Intuitive Geometry*, Bolyai Society Mathematical Studies **27** (2018), 407–458, §8, Conjecture 15 and Theorem 29.
3. A. Polyanskii, [Pairwise intersecting homothets of a convex body](https://arxiv.org/html/1610.04400v2), *Discrete Mathematics* **340**(8) (2017), 1950–1956, Theorem 2.
4. R. Chen, F. Gui, J. Tang and N. Xiong, [Few distance sets in $`\ell_p`$ spaces and $`\ell_p`$ product spaces](https://arxiv.org/html/2009.12512v3), *European Journal of Combinatorics* **102** (2022), 103459, §1.1 and Theorem 3; [doi:10.1016/j.ejc.2021.103459](https://doi.org/10.1016/j.ejc.2021.103459).
5. Z. Füredi, *Few-distance sets in $`d`$-dimensional normed spaces*, in [Discrete Geometry, Oberwolfach Report 17/2005](https://ems.press/content/serial-article-files/45990?nt=1), 947–950.

## Status review


**Known cases:** The planar, parallelotope and equilateral cases are known. Euclidean or specified lp-norm theorems do not prove the bound and rigidity for all finite-dimensional norms; no matching general announcement located.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 26 October 2026. The original paper proves the conjecture for normed planes and parallelotope unit balls; the equilateral case $`k=1`$ is also known. References 2 and 3 give weaker general estimates, while reference 4 treats specified $`\ell_p`$ and product norms. Located Euclidean distinct-distance announcements do not settle the arbitrary-norm statement.

Reference 5 reports a three-dimensional subcase, but a proof or precise supporting reference for that report was not located. This entry therefore states the full quantified conjecture and makes no claim about a smallest unresolved dimension. Current literature, complete-announcement and all-status duplicate checks found no matching complete resolution of the full bound and equality question. Edition and subcase limits are retained in the review records.


### Online recheck, 2026-10-30

The planar, parallelotope and equilateral cases are known. Euclidean or specified lp-norm theorems do not prove the bound and rigidity for all finite-dimensional norms; no matching general announcement located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/0712.0953); [status source 2](https://arxiv.org/abs/1702.00066); [status source 3](https://arxiv.org/abs/2009.12512). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-42fbb72b316da0aa** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
