# 728. Do continuous polynomial roots have weak endpoint derivative regularity?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq3`$, let $`I=(a,b)`$ be a bounded interval, and let

```math
P_t(z)=z^n+a_1(t)z^{n-1}+\cdots+a_n(t)
```


be a monic complex polynomial whose coefficients belong to $`C^{n-1,1}([a,b];\mathbb C)`$. For **every** continuous choice of a root $`\lambda:I\to\mathbb C`$, is

```math
\lambda'\in L^{n/(n-1),\infty}(I),\qquad
\sup_{s>0}s\,|\{t\in I:|\lambda'(t)|>s\}|^{(n-1)/n}<\infty?
```


The derivative exists almost everywhere by the known absolute-continuity theorem [2, Theorem 1]. This is the weak-Lebesgue endpoint question stated by Ghisi and Gobbino [1, §4] and again by Parusiński and Rainer [2, Open Problem 2]. The latter also ask for an explicit bound in terms of the coefficients and interval.

The distinction between **weak** and ordinary $`L^{n/(n-1)}`$ is essential: $`P_t(z)=z^n-t`$ has a root with derivative proportional to $`|t|^{1/n-1}`$, which misses ordinary endpoint integrability but has the critical weak-space scaling. The known theorem gives $`\lambda'\in L^q(I)`$ for every $`q<n/(n-1)`$ [2]; those separate bounds do not imply the weak endpoint.

## Application

Polynomial-root regularity controls how branches change as coefficients vary. The authors use the below-endpoint theorem in local solvability of certain pseudodifferential systems and in lifting maps into finite-group orbit spaces [2, §10]. An endpoint bound would sharpen the limiting regularity available in such applications.

## References

1. M. Ghisi and M. Gobbino, [*Higher order Glaeser inequalities and optimal regularity of roots of real functions*](https://www.numdam.org/item/ASNSP_2013_5_12_4_1001_0.pdf), *Annali della Scuola Normale Superiore di Pisa, Classe di Scienze* (5) **12** (2013), 1001–1021, §4, explicit Open problem on printed pp. 1020–1021.
2. A. Parusiński and A. Rainer, [*Optimal Sobolev regularity of roots of polynomials*](https://math.univ-cotedazur.fr/~parus/publis/ens.pdf), *Annales scientifiques de l'École Normale Supérieure* (4) **51** (2018), 1343–1387, Theorem 1 and §1.2 Open Problem 2; [DOI](https://doi.org/10.24033/asens.2376).
3. A. Parusiński and A. Rainer, [*Selections of bounded variation for roots of smooth polynomials*](https://arxiv.org/pdf/1705.10492v3), *Selecta Mathematica* **26** (2020), article 13. Its weak endpoint theorem concerns radicals; its general-polynomial regularity remains below the endpoint.
4. A. Parusiński and A. Rainer, [*Natural reparameterization and continuity of the solution map for polynomials*](https://arxiv.org/pdf/2609.39389), arXiv:2609.39389 (30 September 2026). Its Lipschitz result changes the parameter and does not settle this question in the original parameter.

## Status review


**Known cases:** The September reparameterization theorem assumes Cd coefficients and changes the time parameter. It retains subcritical Sobolev bounds and does not imply weak endpoint derivative regularity in the original parameter under C(n-1,1) coefficients.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September reparameterization theorem assumes Cd coefficients and changes the time parameter. It retains subcritical Sobolev bounds and does not imply weak endpoint derivative regularity in the original parameter under C(n-1,1) coefficients.

Additional comparison sources: [comparison source 1](https://www.numdam.org/item/ASNSP_2013_5_12_4_1001_0.pdf); [comparison source 2](https://math.univ-cotedazur.fr/~parus/publis/ens.pdf); [comparison source 3](https://doi.org/10.24033/asens.2376); [comparison source 4](https://arxiv.org/pdf/1705.10492v3); [comparison source 5](https://arxiv.org/pdf/2609.39389). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

A [bounded status and duplicate audit](../FURTHER_problems/_tracking/j303-polynomial-root-weak-endpoint-status-2026-10-22.json) through 22 October 2026 found no matching proof, counterexample or announcement. The restriction to degrees $`n\geq3`$ focuses the general question beyond the elementary quadratic reduction to a radical.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fce0a07486626e42**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
