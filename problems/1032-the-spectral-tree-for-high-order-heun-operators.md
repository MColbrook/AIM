# 1032. The spectral tree for high-order Heun operators

**Area:** Spectral asymptotics of differential operators and planar potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`k\geq3`$ and

```math
\mathfrak d=\sum_{i=1}^{k}Q_i(z)\frac{d^i}{dz^i},
\qquad \deg Q_i\leq i+1,\quad\deg Q_k=k+1.
```

Assume the $`k+1`$ roots of $`Q_k`$ are simple and not all collinear. For each sufficiently large $`n`$, take all linear **Van Vleck polynomials** $`V_{n,j}(z)`$ for which $`(\mathfrak d+V_{n,j})S=0`$ has a polynomial solution $`S`$ of degree $`n`$, counting the $`n+1`$ possibilities with multiplicity. Write $`z_{n,j}`$ for the root of $`V_{n,j}`$ and

```math
\mu_n=\frac{1}{n+1}\sum_{j=1}^{n+1}\delta_{z_{n,j}}.
```

Do the measures $`\mu_n`$ converge weakly to a positive probability measure determined only by $`Q_k`$, supported on a **finite planar tree** inside the convex hull of the roots of $`Q_k`$, whose leaves are exactly those roots? The conjecture also asks that this limiting measure reproduce the exterior logarithmic potential calculated from the operator's finite-band recurrence [2, Conjecture 1].

## Application

The answer would identify where the spectral parameters of polynomial solutions accumulate for high-order Heun equations. It would turn an exterior moment calculation into the actual planar root distribution.

## Known results and scope

Shapiro and Tater [1, Conjecture 3] proposed the generalized Heun spectral tree in 2008. The second-order classical Heun support problem was settled separately in [3]. In July 2026, Shapiro [2] proved that every fixed limiting holomorphic moment, and the Cauchy transform and logarithmic potential **outside** the convex hull, depend only on $`Q_k`$. Full weak convergence is proved there when the roots of $`Q_k`$ are collinear. For genuinely non-collinear roots, the paper still states the tree and positive mother-body claim as a conjecture. Exterior moments alone need not locate a measure uniquely inside a two-dimensional hull.

## References

1. B. Shapiro and M. Tater, [*On spectral polynomials of the Heun equation. I*](https://arxiv.org/pdf/0812.2321), arXiv:0812.2321 (2008), Section 4, Conjecture 3.
2. B. Shapiro, [*Van Vleck spectra of high-order Heun operators: finite-band universality and exterior asymptotics*](https://arxiv.org/pdf/2607.02700), arXiv:2607.02700 (2026), Theorems 2–5 and Conjecture 1.
3. B. Shapiro, K. Takemura and M. Tater, [*On spectral polynomials of the Heun equation. II*](https://arxiv.org/pdf/0904.0650), arXiv:0904.0650 (2009), Theorem 2 for the classical second-order case.

## Status review


**Known cases:** General noncollinear simple leading roots and every high order k>=3 require a full positive spectral-tree limit. The July 2026 finite-band and exterior-moment results retain the tree conjecture; the classical second-order result is narrower.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

General noncollinear simple leading roots and every high order k>=3 require a full positive spectral-tree limit. The July 2026 finite-band and exterior-moment results retain the tree conjecture; the classical second-order result is narrower.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-body, later-result and duplicate audit](../FURTHER_problems/_tracking/high-order-heun-spectral-tree-status-2026-10-21.json) separates the current conjecture from the proved moment and collinear results. Bounded searches found no complete proof or counterexample through 21 October 2026; this does not rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f2efae695b2822f4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
