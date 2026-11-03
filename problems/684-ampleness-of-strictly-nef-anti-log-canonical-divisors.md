# 684. Ampleness of strictly nef anti-log canonical divisors

**Area:** Complex algebraic geometry and positivity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a normal projective variety over $`\mathbb C`$, and let $`\Delta\ge0`$ be an effective divisor with rational coefficients such that $`K_X+\Delta`$ is $`\mathbb Q`$-Cartier. Assume that the pair $`(X,\Delta)`$ has Kawamata log terminal (**klt**) singularities: all its discrepancies are greater than $`-1`$.

Suppose the anti-log canonical divisor
```math
D=-(K_X+\Delta)
```

is **strictly nef**, meaning that
```math
D\cdot C>0
\quad\text{for every irreducible complete curve }C\subset X.
```


Must $`D`$ be ample, in every dimension?

For a rational divisor, ampleness means that a positive Cartier multiple is ample, or equivalently that some positive multiple gives a projective embedding. No bigness or existence of sections is assumed. The case $`\Delta=0`$ is included.

## Application

The conclusion makes $`(X,\Delta)`$ a log Fano pair. It would characterize this strong positivity of the anti-log canonical divisor by its positive degrees on individual curves, under mild singularity assumptions. Strict nefness does not imply ampleness for arbitrary divisors, so the canonical form of $`D`$ is essential.

## Known progress

The source proves that $`X`$ is rationally connected under these assumptions in every dimension (Theorem A), and proves the ampleness assertion for threefolds (Theorem D).

Liu's subsequent work proves the boundary-free assertion for log canonical threefolds and gives further restrictions on a possible smooth fourfold counterexample. These results leave the arbitrary-dimensional klt-pair question unresolved in the checked sources.

This is the Campana–Peternell question about a strictly nef anticanonical divisor. The conjecture bearing the same names about Fano manifolds with nef tangent bundle and homogeneous structures is a different statement.

## References

1. J. Liu, W. Ou, J. Wang, X. Yang and G. Zhong, *Algebraic fibre spaces with strictly nef relative anti-log canonical divisor*, [arXiv:2111.05234v1](https://arxiv.org/abs/2111.05234v1), Conjecture 1.1 and Theorems A and D, native pp. 1–3; pair and divisor conventions in Section 2, native p. 3. *Journal of the London Mathematical Society* **109**(6) (2024), e12942, [doi:10.1112/jlms.12942](https://doi.org/10.1112/jlms.12942).
2. H. Liu, *On the log version of Serrano's conjecture*, [arXiv:2302.06209v2](https://arxiv.org/abs/2302.06209v2), Conjecture 1.5, Theorems 1.6–1.7 and Remark 1.8, native pp. 2–3, revised 25 May 2023.

## Status review


**Known cases:** The current OpenAI numerical-semiampleness theorem explicitly requires K_X+B to be pseudo-effective. For this strictly nef anti-log-canonical target K_X+Delta is the negative of a nonzero strictly nef divisor, so that hypothesis is unavailable. Generalized minimal models, threefold ampleness and rational connectedness do not prove all-dimensional ampleness. No matching full resolution or announcement located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current OpenAI numerical-semiampleness theorem explicitly requires K_X+B to be pseudo-effective. For this strictly nef anti-log-canonical target K_X+Delta is the negative of a nonzero strictly nef divisor, so that hypothesis is unavailable. Generalized minimal models, threefold ampleness and rational connectedness do not prove all-dimensional ampleness. No matching full resolution or announcement located.

Additional comparison sources: [comparison source 1](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md); [comparison source 2](https://arxiv.org/abs/2111.05234); [comparison source 3](https://arxiv.org/abs/2302.06209). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the eligible conjecture and definitions, later primary partial results, recent author publication lists, and all-status AIM/FURTHER records, the OpenAI announcement catalogue, and bounded Prove2Me material. No matching proof, counterexample or announced resolution was located in the bounded searches. Selected native windows and scope comparisons are retained; no exhaustive literature or whole-paper proof audit is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-28680fa9260e837e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
