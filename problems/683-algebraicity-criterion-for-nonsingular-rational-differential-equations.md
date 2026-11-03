# 683. Algebraicity criterion for nonsingular rational differential equations

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For integers $`n,N\ge1`$, let $`G\in\mathbb Q(z,y_0,\ldots,y_{n-1})`$ and $`f\in\mathbb Z[1/N][[z]]`$ satisfy
```math
f^{(n)}=G(z,f,f',\ldots,f^{(n-1)}).
```

Assume a quotient representation $`G=P/Q`$ with polynomial numerator and denominator satisfies
```math
Q(0,f(0),f'(0),\ldots,f^{(n-1)}(0))\ne0.
```

Must there exist a nonzero $`H\in\mathbb Q[z,w]`$ with $`H(z,f(z))=0`$?

Membership in $`\mathbb Z[1/N]`$ permits growing powers of finitely many denominator primes. A uniform numerical denominator bound is not assumed. Nonsingularity at the initial jet is essential.

## Application

This asks for an arithmetic criterion for algebraicity of analytic ODE solutions. Its significance here is mathematical; no specific physical application is asserted.

## References

1. Yeuk Hay Joshua Lam and Daniel Litt, [*Algebraicity and integrality of solutions to differential equations*](https://arxiv.org/html/2501.13175v1), arXiv:2501.13175v1 (2025), §1.1, Conjecture 1.1.1 and Remarks 1.1.3–5; Theorems 1.2.4 and 1.3.3–4.
2. Daniel Litt, [*Problem 1*](https://www.problemsilike.com/1), last edited 29 May 2026; [discussion](https://www.problemsilike.com/forum/thread/1).
3. Yeuk Hay Joshua Lam and Daniel Litt, [*p-Curvature and Non-Abelian Cohomology*](https://arxiv.org/html/2601.07933v1), arXiv:2601.07933v1 (2026), Theorems A/B.

## Status review


**Known cases:** Lam and Litt retain bounded integrality on the current Problems I Like page. Special Picard-Fuchs and isomonodromy cases do not settle arbitrary nonsingular rational ODEs with finitely many denominator primes.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Lam and Litt retain bounded integrality on the current Problems I Like page. Special Picard-Fuchs and isomonodromy cases do not settle arbitrary nonsingular rational ODEs with finitely many denominator primes.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 25 October 2026. This is the bounded-integrality branch, separate from the full conjecture involving superlinear prime-wise integrality. No implication to the Grothendieck–Katz conjecture is asserted for this branch alone.

The owner and coordinator read the primary formulation and compared restricted later results. The bounded literature/announcement search found no matching full resolution; the author’s discussion concerns statement formalization. Nearby AIM/OpenAI/FURTHER statements checked were distinct. These checks do not certify every proof or exhaust the literature.

**Admission review:** 25 October 2026. The recorded primary-statement, current-status and semantic duplicate checks were completed before admission. Public AIM-head and complete OpenAI-CONTENTS comparisons were refreshed without a change. The dated, bounded search and access limits above remain part of this assessment.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-24cc8f3b9313a7f2**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
