# 768. Must every blow-down of a perimeter minimizer be a cone in an RCD space?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,d,\mathcal H^N)`$ be a noncollapsed $`\mathrm{RCD}(0,N)`$ metric-measure space with positive Euclidean volume growth,
```math
\lim_{r\to\infty}\frac{\mathcal H^N(B_r(x))}{r^N}>0.
```

Let $`E\subset X`$ be a global perimeter-minimizing set and fix $`x\in\partial E`$. Take any sequence of scales $`r_j\to\infty`$ along which the rescaled pointed space and set converge to an asymptotic metric-measure cone $`(C(Z),o)`$ and a limiting perimeter minimizer $`F\subset C(Z)`$. Must **every** such $`F`$ itself be a cone, invariant under radial dilation about $`o`$?

The authors prove that every ambient asymptotic cone contains *some* globally perimeter-minimizing conical set. Their proof first obtains a blow-down $`F`$ of the given $`E`$ and may then blow down $`F`$ again to produce a cone. The open question asks whether that extra step is unnecessary for **all** blow-downs of $`E`$.

## Application

A positive answer would give a sharper description of the large-scale shape of individual perimeter minimizers under synthetic nonnegative Ricci curvature, not just existence of a conical minimizer in the limiting space.

## References

1. Francesco Fiorani, Andrea Mondino and Daniele Semola, [*Monotonicity formula and stratification of the singular set of perimeter minimizers in RCD spaces*](https://doi.org/10.4171/CMH/598), *Commentarii Mathematici Helvetici* **101** (2026), 193–238, Theorem 1.7 and following open question on pp. 197–198, with proof on p. 230. The [published PDF](https://ems.press/content/serial-article-files/52484?nt=1) supplies the exact hypotheses.
2. Alessandro Cucinotta and Mattia Magnabosco, [*On perimeter minimizing sets in manifolds with quadratic volume growth*](https://doi.org/10.1515/crelle-2026-0017), *Journal für die reine und angewandte Mathematik* **834** (2026), 1–26. Its product-and-slice theorem has stronger smooth curvature and quadratic growth hypotheses.

## Status review


**Known cases:** The inspected 2026 theorem still permits a second blow-down to obtain a conical minimizer. Existence of some cone in each ambient cone, and restricted quadratic-volume-growth smooth products, do not prove every original blow-down conical.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The inspected 2026 theorem still permits a second blow-down to obtain a conical minimizer. Existence of some cone in each ambient cone, and restricted quadratic-volume-growth smooth products, do not prove every original blow-down conical.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/CMH/598); [comparison source 2](https://ems.press/content/serial-article-files/52484?nt=1); [comparison source 3](https://doi.org/10.1515/crelle-2026-0017). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Theorem 1.7 concerns existence of at least one conical minimizer in each ambient asymptotic cone; it does not show that the particular limit of $`E`$ along every scale sequence is conical. The later product-and-slice result covers a restricted smooth setting with quadratic volume growth, outside the general Euclidean $`N`$-volume-growth hypothesis. Bounded searches and an independent source-and-scope audit on 21 October 2026 found no complete resolution of the general RCD question or a duplicate in AIM/FURTHER. This is a live-status assessment, not a proof of unsolvedness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0f2cd2a71ea0597d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
