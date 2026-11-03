# 705. Boundary Hölder regularity of harmonic quasiconformal maps on arbitrary domains

**Area:** Complex analysis and geometric function theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq 3`$, let $`D\subset\mathbb R^n`$ be any bounded domain, and let $`0<\alpha\leq1`$. Suppose that $`f:\overline D\to\mathbb R^n`$ is continuous, its coordinate functions are harmonic in $`D`$, and $`f|_D`$ is quasiconformal. Assume that, for some finite $`M`$,
```math
|f(x)-f(y)|\leq M|x-y|^\alpha
  \qquad (x,y\in\partial D).
```

Must there be a finite constant $`M'`$ such that
```math
|f(x)-f(y)|\leq M'|x-y|^\alpha
  \qquad (x,y\in\overline D)?
```

There is no smoothness, uniform-perfectness, capacity-density or extension-domain assumption on $`D`$. The question concerns preservation of the **same** exponent; a weaker exponent follows for quasiconformal maps from a prior boundary-continuity theorem. It asks for existence of $`M'`$, not a constant independent of all domain geometry.

## Application

Harmonic quasiconformal maps combine coordinatewise potential theory with controlled geometric distortion. Boundary-to-interior regularity on rough domains matters when boundary data are prescribed but the domain has no usable smooth parametrization or uniform capacity estimate.

## References

1. M. Arsenović, V. Manojlović and M. Vuorinen, [*Hölder continuity of harmonic quasiconformal mappings*](https://link.springer.com/article/10.1186/1029-242X-2011-37), *Journal of Inequalities and Applications* **2011**, article 37, [published PDF](https://link.springer.com/content/pdf/10.1186/1029-242X-2011-37.pdf), abstract and Introduction (PDF physical pp. 1–2), Theorem 2.1 and Corollary 2.2 (physical p. 3). The [original arXiv submission](https://arxiv.org/abs/1012.3145v1) and [latest revision](https://arxiv.org/abs/1012.3145v4) retain the question.
2. A. Abaob, M. Arsenović, M. Mateljević and A. Shkheam, [*Moduli of continuity of harmonic quasiregular mappings on bounded domains*](https://www.acadsci.fi/mathematica/Vol38/vol38pp839-847.pdf), *Annales Academiæ Scientiarum Fennicæ Mathematica* **38** (2013), 839–847, Introduction and Theorems 4–5.
3. [*Lipschitz regularity of harmonic quasiconformal maps between Lyapunov domains in $`\mathbb R^n`$*](https://arxiv.org/abs/2602.05436), arXiv:2602.05436v1 (5 February 2026), abstract and Theorem 2.1.

## Status review


**Known cases:** The fresh 2602.05436 theorem requires C1-alpha Lyapunov source and target domains; the present target has arbitrary bounded source domain and preserves its boundary exponent. Uniform-perfectness results remain restricted.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fresh 2602.05436 theorem requires C1-alpha Lyapunov source and target domains; the present target has arbitrary bounded source domain and preserves its boundary exponent. Uniform-perfectness results remain restricted.

Additional comparison sources: [comparison source 1](https://link.springer.com/article/10.1186/1029-242X-2011-37); [comparison source 2](https://link.springer.com/content/pdf/10.1186/1029-242X-2011-37.pdf); [comparison source 3](https://arxiv.org/abs/1012.3145v1); [comparison source 4](https://arxiv.org/abs/1012.3145v4); [comparison source 5](https://www.acadsci.fi/mathematica/Vol38/vol38pp839-847.pdf); [comparison source 6](https://arxiv.org/abs/2602.05436). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reference 1 explicitly asks whether the boundary exponent propagates for an **arbitrary bounded** domain. Its proved theorem assumes that the nonremovable part of the boundary is uniformly perfect; its corollary assumes a uniformly perfect whole boundary. Reference 2 proves modulus propagation with $`C^2`$ boundary; its Theorem 5 still assumes a uniformly perfect boundary for the harmonic case, with an additional extension-domain hypothesis only in its alternate nonharmonic clause. Reference 3 assumes $`C^{1,\alpha}`$ source and target boundaries. None states the unrestricted-domain result above.

The historical Introduction of reference 1 does not restrict the dimension, while its published partial theorem is set in $`n\geq3`$. This page records that higher-dimensional core. The planar harmonic-quasiconformal branch remains a separately tracked status question; arbitrary-domain results for **analytic** planar maps cannot simply be applied to all harmonic quasiconformal maps. The standard radial example showing sharpness for general quasiconformal maps is not harmonic when $`0<\alpha<1`$, so it does not answer this question.

The original arXiv v1, latest v4 and published PDF were pinned and their question and theorem pages visually compared. Bounded current searches found no matching complete proof, counterexample or announcement, and a semantic check found no matching AIM or existing FURTHER problem. These searches do not certify exhaustive absence. [Source audit](../FURTHER_problems/_tracking/parallel/rough-filtering/body0164-1012.3145-holder-propagation-status-audit.json), [native-edition check](../FURTHER_problems/_tracking/parallel/rough-filtering/body0164-1012.3145-native-parity-status-addendum.json), [independent review](../FURTHER_problems/_tracking/holder-propagation-arbitrary-domain-independent-review-2026-10-21.json) and [status decision](../FURTHER_problems/_tracking/holder-propagation-n-ge-3-status-2026-10-21.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8ea604d5bc3486f4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
