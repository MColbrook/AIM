# 693. An analytic twist map with an irrational invariant circle that is not C1

**Area:** Conservative dynamics and small divisors
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Write $`\mathbb T=\mathbb R/\mathbb Z`$. Does there exist a real-analytic diffeomorphism $`f:\mathbb T\times\mathbb R\to\mathbb T\times\mathbb R`$, isotopic to the identity and preserving $`dx\wedge dy`$, with the following properties?

A lift $`F=(F_1,F_2):\mathbb R^2\to\mathbb R^2`$ satisfies

```math
F_1(x+1,y)=F_1(x,y)+1,\qquad F_2(x+1,y)=F_2(x,y),\qquad \partial_yF_1(x,y)>0,
```

and for every $`x`$, the map $`y\mapsto F_1(x,y)`$ is a diffeomorphism of $`\mathbb R`$ onto itself. There is a Lipschitz function $`\gamma:\mathbb T\to\mathbb R`$ whose essential graph $`\Gamma=\{(x,\gamma(x)):x\in\mathbb T\}`$ is invariant under $`f`$, is not a $`C^1`$ embedded curve, and has irrational rotation number under the restricted dynamics. More explicitly, the induced orientation-preserving circle homeomorphism

```math
g(x)=\pi_1 f(x,\gamma(x))
```

has $`\mathrm{rot}(g)=\lim_{n\to\infty}(G^n(x)-x)/n\pmod{\mathbb Z}\notin\mathbb Q/\mathbb Z`$, for a lift $`G`$.

No prescribed irrational number, minimality, closeness to an integrable map, or corner at a specified point is required. The twist inequality is pointwise; a uniform positive lower bound is not added. Failure of $`C^1`$ embedded-curve regularity is equivalent here to failure of $`C^1`$ regularity of the Lipschitz graph function.

## Application

Invariant circles constrain transport in conservative systems. This question asks whether analytic evolution can preserve an irrational invariant barrier whose geometry fails to have a continuous tangent.

## References

1. Marie-Claude Arnaud, [*A non-differentiable essential irrational invariant curve for a C1 symplectic twist map*](https://arxiv.org/abs/1104.4929v1), eligible 2011 preprint, Introduction and Section 2.1. Published in *Journal of Modern Dynamics* **5** (2011), 583–591, [DOI](https://doi.org/10.3934/jmd.2011.5.583). The Introduction explicitly asks Mather's nonperiodic, non-$`C^1`$ question separately for each regularity, including analytic, and separately poses a minimality variant.
2. Stefano Marmi and Jean-Christophe Yoccoz, [*Some Open Problems Related To Small Divisors*](https://doi.org/10.1007/978-3-540-47928-4_4), in *Dynamical Systems and Small Divisors*, Lecture Notes in Mathematics **1784** (2002). Problem 3.1.1, author version physical p. 7/printed p. 165. Its literal “rotational” wording means essential and does not explicitly exclude rational rotation. The present irrational restriction is directly supported by [1].
3. Marie-Claude Arnaud, [*Boundaries of instability zones for symplectic twist maps*](https://arxiv.org/abs/1204.5893v1), 2012 preprint. The inspected abstract constructs a $`C^2`$ map with a nondifferentiable irrational invariant curve, below the requested analytic regularity.
4. Bassam Fayad and Raphaël Krikorian, [*Some questions around quasi-periodic dynamics*](https://rkrikorian.perso.math.cnrs.fr/ICM_FayadKrikorian-cor.pdf), ICM 2018 author version, Section 4.4.1, Question 26. This variant also requires minimal dynamics.
5. Jiashen Guo, Yi Liu and Lin Wang, [*On Non-KAM Invariant Circles for Area-Preserving Twist Maps*](https://arxiv.org/abs/2510.21098v1), 2025 preprint, Theorem 4 and Remarks 1.10–1.13.
6. Qi Li, Yi Liu and Lin Wang, [arXiv:2608.05239v3](https://arxiv.org/abs/2608.05239v3), latest inspected version dated 15 October 2026, Introduction, model and Theorem 1. The intervening v2 was withdrawn; comparisons use v3.

## Status review


### Online recheck, 2026-10-30

The newly inspected October 26 paper 2610.35068, Theorem C(ii), constructs analytic rough irrational invariant graphs for dissipative maps with lambda strictly between zero and one. These maps are not area preserving, so they do not answer the present conservative global twist-map question. The October 15 invariant-graph paper and failure of C2-plus-epsilon regularity also do not supply failure of C1.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/2610.35068v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The analytic branch is taken from the explicit no-periodic-point question in [1], using its global annulus convention. The earlier wording in [2] also permits rational separatrices; the familiar pendulum corner example therefore does not answer the present irrational question. A preliminary local-annulus formulation was replaced before admission; no analytic extension of an arbitrary local map is assumed.

The constructions in [1] and [3] have $`C^1`$ or $`C^2`$ ambient maps. The smooth construction in [5] gives graphs failing $`C^{2+\varepsilon}`$, which does not imply failure of $`C^1`$. Its singular-conjugacy examples likewise need not have nonsmooth graphs. The special perturbation family in the latest version [6] preserves analytic graphs with analytic conjugacies; it supplies neither a nonsmooth example nor a universal regularity theorem.

The current searches and independent selected audit located no matching complete solution or announcement. Final published-body parity for [1] and [2], and full proof checks of the current preprints, remain unreviewed. These bounded checks do not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/analytic-twist-nonc1-circle-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-analytic-twist-nonc1-circle-review.json), [current comparisons](../FURTHER_problems/_tracking/analytic-twist-circle-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/analytic-twist-circle-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/analytic-twist-nonc1-circle-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/analytic-twist-circle-coordinator-review-2026-10-19.json) record scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6b381ca6998045ca**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
