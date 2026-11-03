# 688. Interior regularity of a single-pole pluricomplex Green function

**Area:** Complex analysis and potential theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Does there exist a bounded domain $`\Omega\subset\mathbb C^n`$, $`n\ge2`$, with $`C^\infty`$ smooth strictly pseudoconvex boundary and a pole $`w\in\Omega`$, such that the single-pole Green function

```math
g_\Omega(z,w)=\sup\{u(z):u\in\mathrm{PSH}(\Omega),\ u\le0,\ \limsup_{s\to w}(u(s)-\log\|s-w\|)<\infty\}
```

fails to belong to $`C^2(\Omega\setminus\{w\})`$? The failure must occur at an interior point away from the pole.

## Application

The Green function is a fundamental singular potential for the complex Monge–Ampère operator. This question determines whether interior loss of second-order regularity can occur with one source and smooth strictly pseudoconvex boundary.

## References

1. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations 61(7) (2016), 902–930, Question 28, preprint p14. [Primary preprint](https://arxiv.org/abs/1511.00705).
2. Z. Błocki, *The $`C^{1,1}`$ regularity of the pluricomplex Green function*, Michigan Mathematical Journal 47 (2000), 211–215, Theorem 1 and following paragraph. [Author PDF](https://gamma.im.uj.edu.pl/~blocki/publ/grreg.pdf).

## Status review


### Online recheck, 2026-10-30

The target requires an interior failure of C2 regularity away from a single pole on a smooth strictly pseudoconvex domain. Two-pole bidisc examples, failures at the boundary and examples requiring only C2 rather than smooth boundary do not match. The indexed Pome page could not be fetched; its description alone is not treated as a counterexample.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 16 October 2026. The Green function is known to have $`C^{1,1}`$ regularity away from its pole, including near the boundary. Failure of $`C^2`$ regularity up to the boundary and interior counterexamples with two poles do not settle the single-pole interior question. Smooth strongly convex domains have smooth Green functions. Searches located no matching complete resolution; the dated packet records the completed scope and catalogue comparisons.

The original Bedford–Demailly example rules out smoothness near a closed disk meeting the boundary. That statement and later shorthand citations to it do not establish the interior failure requested here.

Review evidence: [dated scope and current-status packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/green-single-pole-c2-review.json). Negative searches are bounded evidence, not a proof that no resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-505bb8de912ac514**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
