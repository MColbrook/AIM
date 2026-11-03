# 713. Higher-dimensional asymptotic attraction rates of holomorphic germs

**Area:** Local holomorphic dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`n\ge3`$, let $`f:(\mathbb C^n,0)\to(\mathbb C^n,0)`$ be a holomorphic germ fixing $`0`$, with $`\det Df`$ not identically zero and $`\det Df(0)=0`$. Thus $`f`$ is dominant and is not locally biholomorphic. For any nonzero vector-valued germ $`g`$ fixing $`0`$, let $`c(g)`$ be the least total degree of a monomial with nonzero coefficient in any component of its Taylor series. Write $`f^{\circ k}`$ for composition iterates and
```math
\lambda(f)=\lim_{k\to\infty}c(f^{\circ k})^{1/k}.
```

The supermultiplicative order sequence defines this limit initially in $`[1,+\infty]`$. Must $`\lambda(f)`$ be finite and an algebraic integer of degree at most $`n`$, and must there exist a constant $`\delta_f\in(0,1]`$ such that
```math
\delta_f\lambda(f)^k\le c(f^{\circ k})\le\lambda(f)^k\qquad(k=1,2,\ldots)?
```
Here an algebraic integer of degree at most $`n`$ means a root of some monic polynomial in $`\mathbb Z[t]`$ of degree at most $`n`$. The constants may depend on the entire germ. There is no assumption that $`f`$ is a polynomial, finite as a map germ, rigid, monomial, or a skew product. The question concerns the order at the fixed point, not global polynomial degree or topological multiplicity.

## Application

The order of an iterate measures how rapidly a holomorphic map flattens near a fixed point. The question asks whether this growth always has an algebraic rate and a uniform multiplicative estimate, extending a precise two-dimensional theorem to higher dimensions.

## References

1. Marco Abate, [*Open problems in local discrete holomorphic dynamics*](https://doi.org/10.1007/s13324-011-0017-y), *Analysis and Mathematical Physics* **1** (2011), 261–287. Definition 11 and Theorem 9 on p. 270; OP5 on p. 271. [Author preprint](https://arxiv.org/abs/1107.4876v1). The published e-offprint was read separately from the preprint.
2. Charles Favre and Mattias Jonsson, [*Eigenvaluations*](https://www.numdam.org/article/ASENS_2007_4_40_2_309_0.pdf), *Annales scientifiques de l'École Normale Supérieure* **40** (2007), 309–349, [DOI](https://doi.org/10.1016/j.ansens.2007.01.002). Local Theorem A concerns dimension two; the affine Theorem A-prime is distinct.
3. William Gignac and Matteo Ruggiero, [*Growth of attraction rates for iterates of a superattracting germ in dimension two*](https://webusers.imj-prg.fr/~matteo.ruggiero/pub/pdf/gignac-attractionrates.pdf), inspected author version dated 9 May 2013. Theorems A–B and the formal local-ring formulation retain dimension two.
4. Matteo Ruggiero, [*Contracting rigid germs in higher dimensions*](https://arxiv.org/abs/1109.6803v2), inspected v2, 9 January 2013; [published DOI](https://doi.org/10.5802/aif.2818). The classification assumes rigidity and additional internal-action hypotheses.
5. Kohei Ueno, [*Attraction rates for iterates of a superattracting skew product*](https://doi.org/10.1016/j.jmaa.2024.128519), *Journal of Mathematical Analysis and Applications* **539** (2024), article 128519. The inspected official indexed abstract/model concerns two variables; its full body was not available in this check.

## Status review


**Known cases:** The current attraction-rate results found concern dimension two or restricted higher-dimensional normal forms. They do not give a degree-at-most-n algebraic integer and uniform exponential comparability for every dominant singular germ.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current attraction-rate results found concern dimension two or restricted higher-dimensional normal forms. They do not give a degree-at-most-n algebraic integer and uniform exponential comparability for every dominant singular germ.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s13324-011-0017-y); [comparison source 2](https://arxiv.org/abs/1107.4876v1); [comparison source 3](https://www.numdam.org/article/ASENS_2007_4_40_2_309_0.pdf); [comparison source 4](https://doi.org/10.1016/j.ansens.2007.01.002); [comparison source 5](https://webusers.imj-prg.fr/~matteo.ruggiero/pub/pdf/gignac-attractionrates.pdf); [comparison source 6](https://arxiv.org/abs/1109.6803v2); [comparison source 7](https://doi.org/10.5802/aif.2818); [comparison source 8](https://doi.org/10.1016/j.jmaa.2024.128519). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Dimension one is elementary and dimension two is established in [2]. Subsequent two-dimensional recurrence results [3], restricted higher-dimensional rigid classifications [4] and two-variable skew-product results [5] do not establish the general statement above. If the differential has a nonzero eigenvalue, every iterate has order one, so that case already holds. Nilpotent differentials remain included.

The upper inequality follows from supermultiplicativity of the orders; the positive lower multiplicative bound is substantive. Passing to an iterate alone does not establish the requested algebraic degree bound for its positive root. The printed polynomial example in OP5 has inconsistent indices; its explicit prose asks for degree at most $`n`$, as stated here. The separate eventual-recurrence OP6 is not an additional entry here.

No matching complete solution or announcement was located in the recorded bounded checks. This does not certify that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/abate-attraction-rate-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-abate-attraction-rate-review.json), [current comparisons](../FURTHER_problems/_tracking/abate-attraction-rate-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/abate-attraction-rate-duplicates-review-2026-10-19.json), [catalogue check](../FURTHER_problems/_tracking/abate-attraction-rate-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/abate-attraction-rate-coordinator-review-2026-10-19.json) record the checked scope and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b3197eb0c751e1d9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
