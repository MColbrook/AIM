# 703. Talenti comparison for complex Monge–Ampère equations in a ball

**Area:** Complex analysis and potential theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`B=B(0,R)\subset\mathbb C^n`$, $`n\ge2`$, and let $`f\ge0`$ be continuous on $`\overline B`$. Write $`f^*`$ for its radially nonincreasing rearrangement with respect to Lebesgue measure. Let $`u,v\in\mathrm{PSH}(B)\cap C(\overline B)`$ be the weak Dirichlet solutions

```math
(dd^cu)^n=f\,dV,\qquad (dd^cv)^n=f^*\,dV,\qquad u=v=0\quad\text{on }\partial B.
```

Here $`d^c=i(\bar\partial-\partial)`$, and the equations are interpreted in the Bedford–Taylor sense. For the nonpositive solution $`u`$, define $`u^*=-(-u)^*`$, its radially nondecreasing equimeasurable rearrangement, using the usual generalized-inverse convention.

Must $`v\le u^*`$ almost everywhere on $`B`$?

## Application

Such a comparison would reduce nonlinear potential bounds to a radial equation. The source identifies consequences for Kołodziej estimates and optimal constants on a ball.

## References

1. Z. Błocki, *Rearrangements and the Monge–Ampère equations*, Mathematische Zeitschrift 308 (2024), article 17, p3, final paragraph, referring to equation (2) on p2. [Publisher](https://doi.org/10.1007/s00209-024-03557-x), [author PDF](https://gamma.im.uj.edu.pl/~blocki/publ/tal.pdf).

## Status review


### Online recheck, 2026-10-30

The original Talenti paper disproves a general-domain analogue but retains its ball conjecture. Real Monge-Ampere rearrangements and extra rotational invariance do not settle arbitrary continuous ball densities.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00209-024-03557-x); [comparison source 2](https://gamma.im.uj.edu.pl/~blocki/publ/tal.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 16 October 2026. The same article disproves the analogous comparison on arbitrary pseudoconvex domains and explicitly retains the ball case as a conjecture. The planar case follows from the classical Talenti theorem. Real Monge–Ampère comparison with a different rearrangement and results for rotationally invariant plurisubharmonic energies do not give this assertion for arbitrary densities. No later complete resolution was located; the dated packet records the completed catalogue comparison.

Review evidence: [dated scope and current-status packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/ball-talenti-cma-review.json). Negative searches are bounded evidence, not a proof that no resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-85320448052ad60a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
