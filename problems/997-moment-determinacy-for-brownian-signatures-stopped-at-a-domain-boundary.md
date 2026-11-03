# 997. Moment determinacy for Brownian signatures stopped at a domain boundary

**Area:** Rough paths and singular stochastic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$, let $`D\subset\mathbb R^d`$ be a nonempty bounded connected open set with $`C^\infty`$ boundary, and let $`z\in D`$. Start standard Brownian motion $`B`$ at $`z`$ and put
```math
\tau_D=\inf\{t\ge0:B_t\notin D\}.
```

Use its canonical Stratonovich rough-path lift. Its signature levels are
```math
S^0(B)=1,\qquad
S^n(B)=\int_{0<t_1<\cdots<t_n<\tau_D}
\circ dB_{t_1}\otimes\cdots\otimes\circ dB_{t_n}\quad(n\ge1).
```

Every level has finite expectation.

Suppose $`Y`$ is any random continuous geometric $`q`$-rough path in $`\mathbb R^d`$ on $`[0,1]`$, for some deterministic finite $`q\ge1`$, with all signature levels integrable and
```math
\mathbb E S^n(Y)=\mathbb E_z S^n(B)\qquad\text{for every }n\ge0.
```

Must $`S(Y)`$ and $`S(B_{[0,\tau_D]})`$ have the same distribution on
$`\prod_{n\ge0}(\mathbb R^d)^{\otimes n}`$ with its product Borel sigma algebra, for every such $`D`$ and $`z`$?

There is no extra analyticity assumption on $`Y`$. The target is the law of the signature sequence. The planar unit disc started at its centre is already an explicit test case.

## Application

Expected signatures provide moment features for stochastic paths and enter cubature methods for stochastic differential equations. This question asks whether all such features identify a signature law when observation stops at a boundary exit; it does not assert identification from a finite truncation.

## References

1. T. Lyons and H. Ni, *Expected signature of Brownian motion up to the first exit time from a bounded domain*, Annals of Probability **43**(5) (2015), 2729–2762, [DOI](https://doi.org/10.1214/14-AOP949); [electronic reprint, arXiv1101.5902v9](https://arxiv.org/pdf/1101.5902v9), open question on PDFp3 and geometric bounds in Theorem3.6.
2. C. Liu, Z. Lyu and H. Ni, *The $`L^q`$-bounds for Derivatives of Unitary Developments of Random Continuous Geometric Rough Paths*, [arXiv2609.06980v1](https://arxiv.org/html/2609.06980v1), Remark1.3, Proposition2.8 and Corollary3.24.
3. H. Boedihardjo, J. Diehl, M. Mezzarobba and H. Ni, *The expected signature of Brownian motion stopped on the boundary of a circle has finite radius of convergence*, [arXiv1905.13034v2](https://arxiv.org/pdf/1905.13034v2), Theorem10 and Remark11.
4. I. Chevyrev and T. Lyons, *Characteristic functions of measures on geometric rough paths*, [arXiv1307.3580v6](https://arxiv.org/pdf/1307.3580v6), Definition6.12 and Remark6.19.

## Status review


**Known cases:** Every integrable-signature geometric rough-path competitor is allowed without matrix-characteristic analyticity. The September 2026 theorem retains that additional condition and explicitly leaves the unrestricted competitors open.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every integrable-signature geometric rough-path competitor is allowed without matrix-characteristic analyticity. The September 2026 theorem retains that additional condition and explicitly leaves the unrestricted competitors open.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The September2026 result treats competitors whose matrix characteristic functions are real analytic along every real scale line. Its Remark1.3 explicitly leaves competitors outside that class unresolved. The question above retains those competitors. Finite radius of the expected signature, proved for the disc-centre example, does not itself imply indeterminacy.

Current proof, counterexample and announcement searches found no complete resolution of this formulation. Semantic checks against all AIM statuses, the indexed OpenAI result descriptions and the growing FURTHER list found no duplicate. The existing fixed-time Brownian signature-tail constant is a different target. Prove2Me comparison and precise version/access limits are recorded in the [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/stopped-signature-moment-determinacy.json) and [coordinator review](../FURTHER_problems/_tracking/stopped-signature-coordinator-review.json). A negative search does not certify openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-389ffa12b5d532ba**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
