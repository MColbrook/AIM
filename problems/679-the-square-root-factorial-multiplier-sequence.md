# 679. The square-root factorial multiplier sequence

**Area:** Polynomial zero preservation and entire functions
**Status:** ✅ SOLVED
**Last checked:** 2026-11-07

## Problem statement

For every real polynomial $`p(x)=\sum_{k=0}^m a_kx^k`$ with only real zeros, must

```math
Tp(x)=\sum_{k=0}^m\frac{\sqrt{k}}{k!}a_kx^k
```

have only real zeros or be identically zero? The constant coefficient is annihilated: $`\gamma_0=0`$, and $`\gamma_k=\sqrt{k}/k!`$ for $`k\ge1`$.

Equivalently, does the entire function

```math
\Phi(z)=\sum_{k=0}^{\infty}\frac{\sqrt{k}}{(k!)^2}z^k
```

belong to the Laguerre–Pólya class with nonnegative coefficients, meaning that it is a locally uniform limit of real polynomials whose zeros are all nonpositive? Another equivalent formulation asks whether every Jensen polynomial

```math
J_n(x)=\sum_{k=0}^n\binom nk\frac{\sqrt{k}}{k!}x^k,\qquad n\ge1,
```

has only real zeros. Zeros at the origin are allowed. These are equivalent formulations of one question.

## Application

This is a concrete test of when a diagonal operation on polynomial coefficients preserves real zeros. It connects polynomial filters with zero locations of explicit entire functions and generalized Bessel-type functions.

## References

1. George Csordas and Tamás Forgács, [*Multiplier sequences, classes of generalized Bessel functions and open problems*](https://arxiv.org/abs/1505.00355v2), Section 3.1, Lemma 21 and Problem 39(a), physical pp. 9–10 and 16 of the inspected 18-page preprint. Published in *Journal of Mathematical Analysis and Applications* **433** (2016), 1369–1389, [DOI](https://doi.org/10.1016/j.jmaa.2015.08.047). Definitions 3–7 and Theorem 6 specify the multiplier and generating-function conventions. Final 21-page body parity remains pending.
2. Summer Al-Hamdani and Alexandra Leon, [*On Classical Multiplier Sequences*](https://doi.org/10.46787/pump.v1i0.148), *The PUMP Journal of Undergraduate Research* **1** (2018), 14–29, selected indexed statements in Sections 3–4. The inspected results concern other Bessel/cosh generating formulas and representations.
3. Jonas Jalowy, Zakhar Kabluchko and Alexander Marynych, [*Zeros and Exponential Profiles of Polynomials II: Examples*](https://doi.org/10.1007/s00365-026-09775-2), published 11 September 2026, Theorems 2.4 and 5.6, Lemma 5.9 and Remark 5.10. The real-rootedness assumptions and absence of the factorial in its integer-power family distinguish those results from this question.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/679-the-square-root-factorial-multiplier-sequence/main.pdf). The square-root factorial sequence is a multiplier sequence; nonzero generating-function zeros are simple and negative.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/679-review.md) checks the complete argument against this exact target and records the primary-source comparisons. No unresolved mathematical gap was identified in the complete resolution. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



### Online recheck, 2026-10-30

The current primary record remains the 2015 v2 source. Sector-reducing and other classical Bessel multiplier results do not prove that sqrt(k)/k! preserves real zeros in every degree. A right-half-plane zero exclusion is weaker than Laguerre-Polya membership. Fresh problem-number, author, coefficient and venue searches found no matching all-degree solution.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1505.00355); [comparison source 2](https://csm.fresnostate.edu/math/faculty-staff/tforgacs/grants-publications.html); [comparison source 3](https://doi.org/10.1016/j.jmaa.2015.08.047). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves that $`\Phi`$ has no zeros in the open right half-plane. That allows nonreal zeros in the left half-plane and does not establish the requested real-zero property. Integral representations and checks of finitely many Jensen polynomials likewise do not settle all degrees.

The separate complex-zero-decreasing question in Problem 39(b) is stronger and is not an additional target here. The nearby sequence $`e^{\sqrt{k}}/k!`$ is different. Taking pointwise square roots of multiplier sequences is not a supplied closure theorem.

The September 2026 limit theorem assumes real-rooted input polynomials. Its Laguerre interpolation criterion requires an appropriate entire function; the branch expression $`\sqrt{z}/\Gamma(z+1)`$ does not supply one. No matching complete solution or announcement was located in the recorded current checks. These are bounded literature and mathematical checks, not a proof that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/sqrt-factorial-multiplier-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-sqrt-factorial-multiplier-review.json), [current comparisons](../FURTHER_problems/_tracking/sqrt-factorial-multiplier-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/sqrt-factorial-multiplier-duplicates-review-2026-10-19.json), [broader comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/sqrt-factorial-multiplier-duplicates-review.json), [catalogue review](../FURTHER_problems/_tracking/sqrt-factorial-multiplier-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/sqrt-factorial-multiplier-coordinator-review-2026-10-19.json) record the evidence and its limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-173f8d7899595d45**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
