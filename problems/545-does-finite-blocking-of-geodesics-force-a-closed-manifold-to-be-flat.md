# 545. Does finite blocking of geodesics force a closed manifold to be flat?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^n,g)`$ be a smooth, connected, compact Riemannian manifold without boundary, with $`n\ge2`$. For $`p,q\in M`$, including $`p=q`$, let $`\mathcal L_g(p,q)`$ consist of the unit-speed geodesic segments $`\gamma:[0,L]\to M`$, with $`L>0`$, such that
```math
\gamma(0)=p,\qquad \gamma(L)=q,\qquad
\gamma((0,L))\cap\{p,q\}=\varnothing.
```

Suppose that for every pair $`(p,q)`$ there is a finite set $`B_{p,q}\subset M\setminus\{p,q\}`$ such that every $`\gamma\in\mathcal L_g(p,q)`$ satisfies
```math
\gamma((0,L))\cap B_{p,q}\ne\varnothing.
```

Must every sectional curvature of $`g`$ vanish?

The finite blocking set may depend on both endpoints. Its cardinality need not have a uniform bound, and no continuous or separated choice of blockers is assumed. The geodesic segments need not minimize distance.

## Application

The condition describes whether finitely many point obstacles can intercept all light rays connecting each pair of points. The problem links geometrical optics to curvature, geodesic dynamics and inverse questions about the geometry of a space.

## References

1. J.-F. Lafont and B. Schmidt, [*Blocking light in compact Riemannian manifolds*](https://msp.org/gt/2007/11-2/gt-v11-n2-p06-p.pdf), *Geometry & Topology* **11** (2007), 867–887, definitions on pp. 867–868, the unnumbered conjecture on p. 868, and Theorems 2–4; [doi:10.2140/gt.2007.11.867](https://doi.org/10.2140/gt.2007.11.867). Also [arXiv:math/0607789](https://arxiv.org/abs/math/0607789).
2. K. Burns and E. Gutkin, [*Growth of the number of geodesics between points and insecurity for Riemannian manifolds*, author-posted final manuscript](https://sites.math.northwestern.edu/~burns/papers/bg/final.pdf), Definitions 2.1–2.2, Theorem 4.3 and Conjecture 5.6 (physical p. 10 in this 11-page file). Earlier versions have different conjecture numbering; [arXiv:math/0701579](https://arxiv.org/abs/math/0701579).
3. S. Lelièvre, T. Monteil and B. Weiss, [*Everything is illuminated*](https://arxiv.org/abs/1407.2975), introduction and main classification theorem for translation surfaces.
4. W. K. Ho, [*On Blocking Numbers of Surfaces*](https://arxiv.org/abs/0807.2934v3), arXiv:0807.2934v3 (2008), Section 2 and the surface results. Its uniform-blocking formulation is a related special case.

## Status review


**Known cases:** Known finite-blocking flatness results impose nonpositive curvature, no conjugate points or regularity/separation of blockers. Translation-surface classifications permit conical singularities and do not classify arbitrary smooth Riemannian metrics.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 26 October 2026. Compact flat manifolds have finite blocking. The open direction above is the general converse stated by Lafont–Schmidt.

Known theorems establish the converse under nonpositive sectional curvature, or under the additional regularity and separation conditions on blocking sets used by Lafont–Schmidt. Burns–Gutkin prove that uniform finite blocking implies zero geodesic-flow entropy and a virtually nilpotent fundamental group; their flatness conclusion additionally assumes no conjugate points. These hypotheses are not part of the question above.

The classification of finite blocking for translation surfaces concerns metrics given by flat translation charts with possible conical singularities. It does not classify arbitrary smooth Riemannian metrics. Likewise, results for particular surface topologies do not settle the all-dimensional statement.

The published primary definitions and relevant partial-result hypotheses were read. Bounded current searches and all-status AIM/FURTHER/OpenAI statement comparisons found no matching complete resolution or equivalent listed target. This review does not certify every proof cited above.


### Online recheck, 2026-10-30

Known finite-blocking flatness results impose nonpositive curvature, no conjugate points or regularity/separation of blockers. Translation-surface classifications permit conical singularities and do not classify arbitrary smooth Riemannian metrics.

Comparators and current-status sources: [status source 1](https://people.math.osu.edu/lafont.1/gt-blocking.pdf); [status source 2](https://arxiv.org/abs/math/0701579); [status source 3](https://arxiv.org/abs/1407.2975). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-2aa10e21a6f6259e** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
