# 686. Boundary-pole decay of the pluricomplex Green function

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb C^n`$, $`n\ge2`$, be a bounded hyperconvex domain: there exists a negative plurisubharmonic exhaustion $`\rho`$, with $`\{\rho<c\}\Subset\Omega`$ for every $`c<0`$. Define

```math
g_\Omega(z,w)=\sup\{u(z):u\in\mathrm{PSH}(\Omega),\ u\le0,\ \limsup_{s\to w}(u(s)-\log\|s-w\|)<\infty\}.
```

For every nonempty compact $`K\Subset\Omega`$ and every sequence $`w_j\in\Omega`$ with $`\mathrm{dist}(w_j,\partial\Omega)\to0`$, must

```math
\sup_{z\in K}|g_\Omega(z,w_j)|\longrightarrow0?
```

## Application

This asks how a singular complex Monge–Ampère potential changes as its source approaches the boundary. Such estimates also control boundary behavior of the Bergman metric. The Green function need not be symmetric in its two arguments.

## References

1. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations 61(7) (2016), 902–930, Question27, preprint p14. [Primary preprint](https://arxiv.org/abs/1511.00705).
2. Z. Błocki, *Cauchy–Riemann meet Monge–Ampère*, Bulletin of Mathematical Sciences 4 (2014), 433–480, §5 and Proposition5.1. [Publisher](https://doi.org/10.1007/s13373-014-0058-2).

## Status review


**Known cases:** The target is compact-uniform decay as the pole approaches an arbitrary hyperconvex boundary. Lipschitz-boundary results, Lp decay and continuity in the other Green-function argument do not give this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is compact-uniform decay as the pole approaches an arbitrary hyperconvex boundary. Lipschitz-boundary results, Lp decay and continuity in the other Green-function argument do not give this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 16 October 2026. The assertion holds for pseudoconvex domains with Lipschitz boundary. On arbitrary bounded hyperconvex domains, convergence in every finite $`L^p`$ norm is known; this does not establish the displayed locally uniform convergence. Searches located no complete resolution of the rough-boundary target. The [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/green-boundary-pole-review.json) records current primary comparisons and bounded catalogue checks. No equivalent question was found in the all-status AIM and FURTHER collections or the indexed OpenAI announcements. The six matching Prove2Me listing contexts concern other Green functions or meromorphic poles; their proof contents were not certified.

Only compact subsets of the interior are involved. Uniformity up to distinct boundary points is a stronger assertion and is not part of this question.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-39bf7ccf72798af9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
