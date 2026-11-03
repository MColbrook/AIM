# 1006. Fourier leakage after symmetric rearrangement

**Area:** Harmonic analysis and quantitative uncertainty principles
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a measurable set $`A\subset\mathbb R^d`$ of finite positive measure, let $`A^*`$ be the centered ball with $`|A^*|=|A|`$. For $`f\in L^2(\mathbb R^d)`$, let $`|f|^*`$ be the radial nonincreasing equimeasurable rearrangement of $`|f|`$, and write $`\widehat f`$ for the Fourier transform. Fix $`d\ge2`$. Does there exist $`\kappa_d>0`$ such that, for all finite-measure sets $`S,\Sigma\subset\mathbb R^d`$ and all $`f`$ supported in $`S`$,

```math
\int_{\mathbb R^d\setminus\Sigma^*}
  \bigl|\widehat{|f|^*}(\xi)\bigr|^2\,d\xi
\le \kappa_d\exp\!\left(\kappa_d(|S|\,|\Sigma|)^{1/d}\right)
\int_{\mathbb R^d\setminus\Sigma}|\widehat f(\xi)|^2\,d\xi\;?
```

This is the corrected Conjecture 5.3 of Jaming [1]. Both the finite-support hypothesis and the exponential factor are part of the question; the paper gives a counterexample to its older version without them.

## Application

The proposed bound would control how much Fourier energy escapes a frequency set after spatial symmetrization. It would imply the pure volume-product form of the multidimensional Nazarov uncertainty inequality [1, Conjecture 5.4]:

```math
\|f\|_2^2\le C_d\exp\!\left(C_d(|S|\,|\Sigma|)^{1/d}\right)
\left(\int_{\mathbb R^d\setminus S}|f|^2
+\int_{\mathbb R^d\setminus\Sigma}|\widehat f|^2\right).
```

## Known results and scope

Jaming proves the inequality in the opposite direction for Fourier energy **inside** a set of finite measure [1, Theorem 5.1]. His paper proves that the rearrangement leakage conjecture would imply the displayed uncertainty estimate. The one-dimensional uncertainty estimate is due to Nazarov, and special higher-dimensional cases with a convex set are known [1, discussion after Conjecture 5.4]. These do not establish the corrected rearrangement estimate for arbitrary measurable $`S`$ and $`\Sigma`$.

## References

1. P. Jaming, [*On the Fourier transform of the symmetric decreasing rearrangements*](https://aif.centre-mersenne.org/item/10.5802/aif.2597.pdf), *Annales de l'Institut Fourier* **61** (2011), 53–77, Theorem 5.1 and Conjectures 5.3–5.4, with the counterexample immediately after.

## Status review


**Known cases:** The finite-support assumption and exponential loss belong to the corrected conjecture. The older uncorrected rearrangement inequality is false. The January 2026 Oxford rearrangement talk concerns ordering finite additive sets and is unrelated.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The finite-support assumption and exponential loss belong to the corrected conjecture. The older uncorrected rearrangement inequality is false. The January 2026 Oxford rearrangement talk concerns ordering finite additive sets and is unrelated.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [primary-body, later-result and duplicate audit](../FURTHER_problems/_tracking/fourier-rearrangement-leakage-status-2026-10-21.json) identifies the corrected conjecture and distinguishes it from the false older variant. Bounded searches found no complete proof or counterexample through 21 October 2026; this does not rule out unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-02cf98bff0f8e0b0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
