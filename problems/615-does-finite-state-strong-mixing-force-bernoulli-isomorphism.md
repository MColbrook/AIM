# 615. Does finite-state strong mixing force Bernoulli isomorphism?

**Area:** Stationary stochastic processes and ergodic theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`A`$ be a finite nonempty alphabet, and let $`\mu`$ be a shift-invariant Borel probability measure on $`A^{\mathbb Z}`$. Write $`(Sx)_k=x_{k+1}`$. Define

```math
\alpha_\mu(n)=\sup\{|\mu(E\cap F)-\mu(E)\mu(F)|:
 E\in\sigma(x_k:k\le0),\ F\in\sigma(x_k:k\ge n)\}.
```

If $`\alpha_\mu(n)\to0`$, must $`(A^{\mathbb Z},\mu,S)`$ be isomorphic modulo null sets to a Bernoulli shift?

Here a Bernoulli shift means $`(B^{\mathbb Z},\nu^{\mathbb Z},S)`$ for some standard probability space $`(B,\nu)`$. An isomorphism is a measure-preserving measurable bijection between invariant conull subsets, with measurable inverse, that intertwines the shifts. No finite coding radius, output alphabet, coordinatewise form or prescribed entropy is imposed. Degenerate point-mass systems are allowed and are already Bernoulli.

## Application

A positive answer would identify a broad class of dependent observations with iid dynamics after a measurable change of coordinates. It asks how uniform loss of past–future dependence relates to the structure of a stochastic system.

## References

1. Richard C. Bradley, [*Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*](https://arxiv.org/abs/math/0511078v1), *Probability Surveys* **2** (2005), 107–144, [DOI](https://doi.org/10.1214/154957805100000104). Question 4, physical p. 11 / printed p. 117; definitions on physical pp. 2 and 5.
2. Marlies Gerber and Philipp Kunde, [*Anticlassification Results in Ergodic Theory*](https://epubs.siam.org/doi/full/10.1137/25M1806004), *Proceedings of the International Congress of Mathematicians 2026*, vol. 3, 57–75, Section 5.1, [DOI](https://doi.org/10.1137/25M1806004).

## Status review

This is Bradley's Question 4, attributed there to Donald Ornstein. The coefficient is uniform over the entire past and future sigma-fields, a stronger condition than ordinary pointwise mixing in ergodic theory. The conclusion concerns the system's isomorphism class; the displayed coordinates need not themselves be independent.

Absolute regularity (beta-mixing, or the weak Bernoulli condition) already implies the conclusion, as do sufficiently fast alpha-mixing rates in the cited source. No rate is assumed here. The K property, non-Bernoulli examples with ordinary mixing, and bilateral determinism of a particular coordinate presentation do not alone settle this exact question.

Section 5.1 of [2] explicitly retains the alpha-mixing-to-Bernoulli question and cites Bradley's Question 4. A separate announced phi-mixing counterexample to a central limit theorem does not assert a non-Bernoulli system: failure of a CLT for an observable does not rule out Bernoulli isomorphism. No matching complete solution or announcement was found in the recorded bounded checks; this does not certify that no resolution exists.

The inspected 38-page source carries journal typesetting and an arXiv v1 stamp. Independently certified final-edition byte parity is not claimed.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/alpha-mixing-bernoulli-review.json), [selected independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-alpha-mixing-bernoulli-review.json), [current comparisons](../FURTHER_problems/_tracking/alpha-bernoulli-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/alpha-bernoulli-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/alpha-bernoulli-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/alpha-bernoulli-coordinator-review-2026-10-19.json) record the evidence and its limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

Question is alpha-mixing of a finite-state stationary process implying Bernoulli isomorphism, with no rate. Beta-mixing, ordinary mixing and observable CLTs are different conditions/conclusions; the 2026 ICM discussion retains the question.

Comparators and current-status sources: [status source 1](https://epubs.siam.org/doi/10.1137/25M1806004); [status source 2](https://arxiv.org/abs/math/0511078). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c2175c321caa0269** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
