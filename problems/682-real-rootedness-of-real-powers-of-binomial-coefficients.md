# 682. Real-rootedness of real powers of binomial coefficients

**Area:** Polynomial zeros and coefficient transformations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`n\ge1`$ and real $`\gamma\ge2`$, does

```math
B_{n,\gamma}(x)=\sum_{k=0}^n\binom nk^{\gamma}x^k
```

have only real zeros? Repeated zeros are allowed. The constant and leading coefficients are one, so any real zeros are strictly negative. Powers act on the ordinary coefficients of $`(1+x)^n`$.

The target concerns these exact finite polynomials for every degree. It does not ask for a limiting zero distribution or for preservation on every real-rooted input polynomial.

## Application

This tests how a simple nonlinear change of coefficients affects polynomial zeros. It connects total positivity and real-zero preservation with polynomial families whose limiting zeros can already be described explicitly.

## References

1. Jonas Jalowy, Zakhar Kabluchko and Alexander Marynych, [*Zeros and Exponential Profiles of Polynomials II: Examples*](https://doi.org/10.1007/s00365-026-09775-2), *Constructive Approximation*, published 11 September 2026. Section 4.5, Theorem 4.7 and Remark 4.8, physical pp. 16–17 of the inspected final 45-page publication, state the integer cases and the conjecture.
2. Yi Wang and Bin Zhang, [*Hadamard powers of polynomials with only real zeros*](https://doi.org/10.1016/j.laa.2013.08.012), *Linear Algebra and its Applications* **439** (2013), 3173–3176, Theorem 2 and Remark 1. The inspected sufficient exponent bound depends on degree.
3. Anonymous, [*The sharp exponent for ordinary Hadamard powers of quartics with positive coefficients*](https://www.evidencepress.org/releases/sharp-quartic-hadamard-powers/), Evidence Press, version 0.1.0-candidate (2026), [archived announcement](https://doi.org/10.5281/zenodo.22346503). This unrefereed announcement concerns degree exactly four; its manuscript proof has not been certified here.

## Status review


**Known cases:** The September published conjecture covers all degrees and all real powers at least two. The Evidence Press quartic candidate only addresses degree four, and asymptotic free-probability results do not supply the missing uniform finite-degree assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September published conjecture covers all degrees and all real powers at least two. The Evidence Press quartic candidate only addresses degree four, and asymptotic free-probability results do not supply the missing uniform finite-degree assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Integer exponents are known. Iterating a real-rootedness-preserving polynomial composition gives integer cases but does not supply arbitrary real exponents. The degree-dependent sufficient bounds in [2] grow with degree and do not establish the uniform threshold two.

Reference [1] extends its limiting probability density to real parameters greater than one. That limiting description does not prove real-rootedness of each finite polynomial. Its subsequent hypergeometric limit theorem explicitly assumes eventual real-rootedness.

The complete proposed claim in [3] covers a small-degree subcase; its stated scope excludes higher degrees. No matching all-degree solution or complete announcement was located in the recorded bounded current checks. These checks do not certify that no resolution exists. The source's separate numerical prediction for parameters between one and two is not an additional target here.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/binomial-real-power-roots-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-binomial-real-power-roots-review.json), [current comparisons](../FURTHER_problems/_tracking/binomial-real-power-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/binomial-real-power-duplicates-review-2026-10-19.json), [broader comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/binomial-real-power-roots-duplicates-review.json), [catalogue review](../FURTHER_problems/_tracking/binomial-real-power-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/binomial-real-power-coordinator-review-2026-10-19.json) record the evidence and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-1c31db02196c18af**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
