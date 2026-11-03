# 992. Shy reflected Brownian couplings in contractible domains

**Area:** Probability, statistics and learning
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\geq3`$ and let $`D\subset\mathbb R^d`$ be a bounded contractible domain with $`C^2`$ boundary. Suppose $`(X_t,Y_t)_{t\geq0}`$ is a **co-adapted** coupling of two normally reflected Brownian motions in $`\overline D`$. Must it be true, for every starting pair and every $`\varepsilon>0`$, that

```math
\mathbb P\!\left(\inf_{t\geq0}|X_t-Y_t|>\varepsilon\right)=0\,?
```


Equivalently, can any such domain support a shy co-adapted coupling [1, Section 5.2, Conjecture 1]? The $`C^2`$ restriction specifies a standard regular setting for reflection; the source conjectures the broader bounded contractible case. In dimension two, the regular simply connected case follows from the source's $`\mathrm{CAT}(0)`$ theorem [1, Theorem 2].

## Application

Co-adapted means each Brownian motion retains its transition law with respect to the common filtration; the coupling may correlate their driving noise but cannot anticipate future motion. The conjecture asks whether the topology of a bounded domain alone forces the two paths arbitrarily close with probability one, a question about how geometry constrains probabilistic coupling. Later work rules out shy couplings in regular star-shaped and more generally uniformly well-contractible-loop domains [2, Theorem 5.5]. Its contractible three-dimensional example is not in that geometric class [2, Example 7.1], so that result does not cover the question here.

## References

1. M. Bramson, K. Burdzy and W. S. Kendall, [*Shy couplings, CAT(0) spaces, and the lion and man*](https://arxiv.org/abs/1007.3199), *Ann. Probab.* **41** (2013), no. 2, 744–784, DOI: [10.1214/11-AOP723](https://doi.org/10.1214/11-AOP723), Section 5.2, Conjecture 1.
2. M. Bramson, K. Burdzy and W. S. Kendall, [*Rubber bands, pursuit games and shy couplings*](https://arxiv.org/abs/1207.0597), *Proc. Lond. Math. Soc.* **109** (2014), no. 1, 121–160, DOI: [10.1112/plms/pdt067](https://doi.org/10.1112/plms/pdt067), Theorem 5.5 and Example 7.1.

## Status review


**Known cases:** The smooth contractible case in dimension at least three is needed. CAT(0), rubber-band and planar simply-connected theorems impose stronger geometry; no matching general conclusion found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The smooth contractible case in dimension at least three is needed. CAT(0), rubber-band and planar simply-connected theorems impose stronger geometry; no matching general conclusion found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded audit](../FURTHER_problems/_tracking/shy-coupling-contractible-status-2026-10-22.json) checks the original statement, later geometric partial results, targeted proof/counterexample announcements, and AIM/FURTHER duplicates through 22 October 2026. No resolution of the smooth contractible $`d\geq3`$ case was located.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f3d8745ef4645ca8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
