# 869. Are saddle-connection lengths uniformly distributed modulo one on every flat surface?

**Area:** Translation surfaces and dynamical systems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a closed compact Riemann surface of genus at least two, and let $`\omega`$ be a nonzero holomorphic one-form on $`X`$. A saddle connection is a straight geodesic segment for the translation metric induced by $`\omega`$, joining zeros of $`\omega`$ with no zero in its interior. Enumerate **all saddle connections**, counted as geometric connections rather than distinct length values, as $`v_1,v_2,\ldots`$ in nondecreasing length. Write

```math
\ell_n=\left\|\left(\int_{v_n}\mathrm{Re}\omega,\int_{v_n}\mathrm{Im}\omega\right)\right\|_2.
```

Is $`(\ell_n)`$ uniformly distributed modulo one for **every** such pair $`(X,\omega)`$? Equivalently, for every $`0\leq a<b\leq1`$, must

```math
\lim_{N\to\infty}\frac{1}{N}\#\{1\leq n\leq N:\{\ell_n\}\in[a,b)\}=b-a?
```

The source's “every flat surface” formulation imposes no unit-area normalization. Ties in length do not affect the sequence of lengths.

## Application

A universal answer would describe length statistics even on exceptional translation surfaces excluded by almost-everywhere theorems. It would also clarify how far orbitwise equidistribution methods can be strengthened in flat-surface dynamics.

## Context

Chaika and Robertson prove uniform distribution for almost every flat surface under each relevant invariant ergodic measure and explicitly pose the universal version as Question 6. Robertson and Dozier later prove that **almost every** surface in the $`\mathrm{SL}(2,\mathbb R)`$ orbit of **each** starting surface has the property. The quantifier over individual surfaces remains the issue. An appendix to the original paper settles a separate torus case.

## References

1. J. Chaika and D. Robertson, with an appendix by D. El-Baz and B. Huang, [*Uniform distribution of saddle connection lengths*](https://par.nsf.gov/servlets/purl/10315760), *Journal of Modern Dynamics* **15** (2019), 329–343, [doi:10.3934/jmd.2019023](https://doi.org/10.3934/jmd.2019023). See the author manuscript, Introduction, Question 6, and appendix.
2. D. Robertson and B. Dozier, [*Uniform distribution of saddle connection lengths in all $`\mathrm{SL}(2,\mathbb R)`$ orbits*](https://link.springer.com/article/10.1007/s10711-023-00800-3), *Geometriae Dedicata* **217** (2023), article 65, [doi:10.1007/s10711-023-00800-3](https://doi.org/10.1007/s10711-023-00800-3). See Theorem 1.1.

## Status review


**Known cases:** The all-SL2-orbits theorem is almost everywhere within each orbit, not every individual flat surface. Its newer indexed record repeats that almost-everywhere quantifier. No matching every-surface proof or counterexample was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The all-SL2-orbits theorem is almost everywhere within each orbit, not every individual flat surface. Its newer indexed record repeats that almost-everywhere quantifier. No matching every-surface proof or counterexample was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The final accessible author manuscript still calls Question 6 open. The 2023 theorem has an almost-everywhere conclusion within each orbit, so it does not settle the every-surface target. Targeted proof, counterexample and announcement searches through 23 October 2026 found no complete resolution; existing AIM and admitted FURTHER pages were checked for this target. The publisher's 2019 full text was subscription-gated, so exact published-page parity was not claimed. The [audit](../FURTHER_problems/_tracking/saddle-connection-lengths-every-surface-audit-2026-10-23.json) records these limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fae3bc1353cb66f0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
