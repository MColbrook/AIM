# 979. Boundary independence of the half-line KPZ lower-tail rate

**Area:** Probability, statistics and learning
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each fixed finite $`A>-1/2`$, let $`Z_A`$ solve the stochastic heat equation on $`x\geq0`$, in the Itô mild sense,
```math
\partial_t Z_A=\partial_x^2Z_A+\sqrt2\,Z_A\xi,
\qquad \partial_xZ_A(t,0)=A Z_A(t,0),
\qquad Z_A(0,\cdot)=\delta_0,
```

where $`\xi`$ is standard space-time white noise. Use the Robin heat kernel with unit boundary delta mass to fix the initial normalization, and put
```math
H_A(t)=\log Z_A(t,0)+t/12.
```

For every fixed $`s<0`$, do the finite limits
```math
I_A(s)=-\lim_{t\to\infty}t^{-2}\log\mathbb P\{H_A(t)<st\}
```

exist and have the same value for all such $`A`$? The parameter stays fixed as time grows.

## Application

This asks whether interaction with a boundary changes the exponential cost of a large downward fluctuation of a randomly growing interface, or its associated directed polymer.

## References

- A. Krajenbrink and P. Le Doussal, *Large fluctuations of the KPZ equation in a half-space*, SciPost Phys. **5**, 032 (2018), [DOI](https://doi.org/10.21468/SciPostPhys.5.4.032), [primary v2](https://arxiv.org/html/1804.08800v2), **Section 9.3**.
- The same authors, *Replica Bethe Ansatz solution to the Kardar-Parisi-Zhang equation on the half-line*, SciPost Phys. **8**, 035 (2020), [DOI](https://doi.org/10.21468/SciPostPhys.8.3.035), [primary v4](https://arxiv.org/html/1905.05718), Sections 2.1-2.2.
- L.-C. Tsai, *Exact lower-tail large deviations of the KPZ equation*, Duke Math. J. **171** (2022), 1879-1922, [DOI](https://doi.org/10.1215/00127094-2022-0008), Corollary 1.4 ([archived Corollary 1.3](https://arxiv.org/html/1809.03410v1)).

## Status review


**Known cases:** The parameter A is fixed in the entire open interval above -1/2 and the fixed-depth rate must exist. The critical-boundary formula, typical fluctuations and half-space universality do not prove this boundary-independence assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The parameter A is fixed in the entire open interval above -1/2 and the fixed-depth rate must exist. The critical-boundary formula, typical fluctuations and half-space universality do not prove this boundary-independence assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Partial progress; checked 28 October 2026.** The critical case $`A=-1/2`$ is known. It lies outside the question. Typical $`t^{1/3}`$ fluctuations and deep-tail exponents do not establish the full fixed-$`s`$ rate. No matching complete result, announcement or AIM/private duplicate was found. Independence on this open interval alone does not identify the rate with its critical-boundary value.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-halfspace-KPZ-left-rate-boundary-independence-C229-A-20261028/OWNER-EXACT-FIXED-ROBIN-HALFLINE-KPZ-LONGTIME-LEFT-RATE-INDEPENDENCE-PRIMARY-PARTIALS-CURRENT-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-halfspace-KPZ-left-rate-boundary-independence-C229-A-20261028/C-INDEPENDENT-ROBIN-SHE-NOISE-TIME2-CONVERSION-AND-FIXED-A-LONGTIME-LOWER-RATE-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-halfspace-KPZ-left-rate-boundary-independence-C229-A-20261028/ROOT-EXACT-LONGTIME-SHE-BOUNDARY-RATE-CRITICAL-PARTIAL-AND-CURRENT-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-72dae1cc0ab2901f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
