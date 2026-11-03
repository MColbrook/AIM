# 994. Interlaced maximal-correlation mixing for a uniformly mixing Markov chain

**Area:** Stationary stochastic processes and Markov chains
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X_k)_{k\in\mathbb Z}`$ be a strictly stationary real-valued time-homogeneous Markov chain on a probability space. No finiteness of its state space, reversibility, density, moment or minorization assumption is imposed.

For two sigma-fields $`\mathcal A,\mathcal B`$, put
```math
\phi(\mathcal A,\mathcal B)
=\sup_{A\in\mathcal A,\ P(A)>0,\ B\in\mathcal B}
|P(B\mid A)-P(B)|,
```
and let $`\rho(\mathcal A,\mathcal B)`$ be the supremum of $`|\mathrm{Corr}(f,g)|`$ over real square-integrable $`\mathcal A`$-measurable $`f`$ and $`\mathcal B`$-measurable $`g`$ with positive variances. A supremum over no such pair is zero. Define
```math
\phi_X(n)=\phi\bigl(\sigma(X_k:k\le0),\sigma(X_k:k\ge n)\bigr),
```
```math
\rho_X^*(n)=\sup\rho\bigl(\sigma(X_k:k\in S),\sigma(X_k:k\in T)\bigr),
```
where the second supremum ranges over all nonempty disjoint sets $`S,T\subset\mathbb Z`$ with $`\inf_{s\in S,t\in T}|s-t|\ge n`$. The sets may interlace and need not be finite.

**Question.** Does $`\phi_X(n)\to0`$ imply $`\rho_X^*(n)\to0`$ for every such chain?

## Application

This asks whether uniform loss of dependence between a chain's past and future also controls correlations between arbitrary separated collections of observation times. Such control supports limit theorems and statistical inference for dependent data.

## References

1. Richard C. Bradley, [*Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*](https://arxiv.org/abs/math/0511078v1), *Probability Surveys* **2** (2005), 107–144, [DOI](https://doi.org/10.1214/154957805100000104). Question 5, physical p. 13 / printed p. 119; coefficient definitions on physical pp. 2 and 7; Theorem 3.3 and the Doeblin discussion on pp. 12–16.
2. Richard C. Bradley, [*On Mixing Properties of Reversible Markov Chains*](https://arxiv.org/abs/1403.4895), Theorem 1.1. Its ordinary rho-mixing counterexample does not assert phi-mixing.
3. Yeor Hafouta and Brenden Williams, [*Limit theorems for inhomogeneous phi-mixing Markov chains*](https://arxiv.org/abs/2510.15323v2), v2, 2 August 2026. Selected statements concern additive-function limit theorems rather than arbitrary interlaced sigma-fields.

## Status review


**Known cases:** The premise is phi-mixing, not ordinary rho-mixing. Reversible spectral-gap counterexamples and inhomogeneous additive limit theorems do not settle interlaced rho-star mixing under this premise.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The premise is phi-mixing, not ordinary rho-mixing. Reversible spectral-gap counterexamples and inhomogeneous additive limit theorems do not settle interlaced rho-star mixing under this premise.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This explicitly selects the strictly stationary case of Bradley's Question 5; its literal wording does not repeat stationarity. It differs from Question 2 for general stationary processes. The stronger lower-psi condition in Theorem 3.3(7) already implies the conclusion. Finite-state irreducible aperiodic chains are also known cases. Exponential decay of ordinary phi-mixing for Markov chains does not by itself reduce the interlaced supremum to two endpoints.

A [September 2026 producer announcement](https://github.com/tadamcz/phi-mixing-clt) gives a causal stationary phi-mixing process violating a central limit conjecture. Its public construction does not assert that the observed process is Markov. Encoding its whole past as a state preserves past information and fails to preserve phi-mixing; therefore that announcement does not directly settle this Markov formulation. No independent certification or Lean replay of that construction is claimed here.

No matching complete solution or announcement was found in the recorded bounded current checks. This does not certify that no solution exists. The inspected source is a 38-page institutional journal-typeset PDF bearing an arXiv v1 stamp; separate final-edition byte parity remains unverified.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/markov-phi-interlaced-rho-review.json), [selected independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-markov-phi-interlaced-rho-review.json), [current comparisons](../FURTHER_problems/_tracking/markov-phi-interlaced-rho-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/markov-phi-interlaced-rho-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/markov-phi-specific-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/markov-phi-interlaced-rho-coordinator-review-2026-10-19.json) record the checked scope and remaining coverage limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-205d9eaf81dea50c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
