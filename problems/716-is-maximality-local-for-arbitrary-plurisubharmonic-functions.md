# 716. Is maximality local for arbitrary plurisubharmonic functions?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb C^n`$, $`n\ge2`$, be a domain and let $`u\in\mathrm{PSH}(\Omega)`$ satisfy $`u\not\equiv-\infty`$. Call $`u`$ **maximal** if, for every $`v\in\mathrm{PSH}(\Omega)`$ satisfying $`v\le u`$ outside a compact subset of $`\Omega`$, one has $`v\le u`$ throughout $`\Omega`$.

Suppose every point has an open neighborhood on which the restriction of $`u`$ is maximal. Must $`u`$ be maximal on $`\Omega`$? No boundedness, analytic-singularity or Monge–Ampère domain-of-definition assumption is imposed.

## Application

Maximal functions extend solutions of the homogeneous complex Monge–Ampère equation to singular plurisubharmonic functions for which that equation may not be defined. Locality would permit local comparisons to establish global extremality in this setting.

## References

1. Z. Błocki, *A note on maximal plurisubharmonic functions*, Uzbek Mathematical Journal (2009), no.1, 28–32; question on p29. [Author PDF](https://gamma.im.uj.edu.pl/~blocki/publ/max.pdf).
2. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations 61(7) (2016), 902–930, Question3, preprint p4. [Primary preprint](https://arxiv.org/abs/1511.00705).
3. T. D. Do and P. H. Hiep, *Local-to-global maximality for plurisubharmonic functions with locally analytic singularities*, arXiv:2610.05937v2 (15 October2026), Theorem1.1. [Preprint](https://arxiv.org/abs/2610.05937).
4. T. D. Do and P. H. Hiep, *Comparison principles for local plurisubharmonic potentials on complex manifolds and applications*, arXiv:2610.05948v2 (6 October2026), assumption(8) and Theorem1.5. [Preprint](https://arxiv.org/abs/2610.05948).

## Status review


**Known cases:** The October local-to-global papers restrict to analytic singularities with bounded remainder or a specified Cegrell class in dimension two. The revised Hilbert-space theorem assumes C2 regularity and additional spectral or boundedness conditions; arbitrary singular psh functions remain outside those hypotheses.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The October local-to-global papers restrict to analytic singularities with bounded remainder or a specified Cegrell class in dimension two. The revised Hilbert-space theorem assumes C2 regularity and additional spectral or boundedness conditions; arbitrary singular psh functions remain outside those hypotheses.

Additional comparison sources: [comparison source 1](https://gamma.im.uj.edu.pl/~blocki/publ/max.pdf); [comparison source 2](https://arxiv.org/abs/1511.00705); [comparison source 3](https://arxiv.org/abs/2610.05937); [comparison source 4](https://arxiv.org/abs/2610.05948). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed 16 October 2026. Locality is known for locally bounded functions and appropriate Monge–Ampère domains of definition. Recent preprints cover locally analytic singularities with a bounded remainder, and a restricted analytic/Cegrell class in dimension two. These assumptions do not give arbitrary singularities. Błocki’s 2009 counterexample concerns a different truncation-convergence statement.

No equivalent question was found in all-status AIM, retained entries, the developing FURTHER list or the indexed OpenAI announcement families. Prove2Me’s matching plurisubharmonic contexts concern classical pseudoconvexity and smoothing, rather than this maximality question. The [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/psh-local-maximality-review.json) records exact partial-result assumptions, current searches and the limits of the catalogue comparison.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-badf86ac363144a0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
