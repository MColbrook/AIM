# 764. Growth of the Euclidean Lipschitz extension modulus

**Area:** Metric geometry and nonlinear functional analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a metric space $`M`$, let $`e(M)`$ be the least $`L`$ such that every $`1`$-Lipschitz map from **any** subset $`C\subseteq M`$ into **any** Banach space $`Z`$ extends to a map $`M\to Z`$ with Lipschitz constant at most $`L`$.

**Question.** What is the asymptotic growth, up to universal constant factors, of $`e(\ell_2^n)`$ as $`n\to\infty`$?

The target space is allowed to be an arbitrary Banach space. Restricting it to a Hilbert space changes the question: Kirszbraun's theorem then gives an extension without loss.

## Application

This modulus measures the worst unavoidable distortion when data defined on part of Euclidean space are extended to the whole space with Banach-valued outputs. Its growth is linked to the geometry of random metric partitions and quantitative extension procedures.

## References

1. Assaf Naor, [*Extension, Separation and Isomorphic Reverse Isoperimetry*](https://ems.press/books/mems/283), EMS Memoirs **11** (2024), DOI 10.4171/MEMS/11, Chapter 1, printed pp. 1–2, 13. The book defines $`e(M)`$ and explicitly identifies the Euclidean asymptotic as a longstanding open problem.
2. Mustafa Alper Gunes and Assaf Naor, [*The separation modulus of unitarily invariant matrix norms*](https://arxiv.org/abs/2508.03853), arXiv:2508.03853, Introduction, Problem 4 and Theorem 3. The authors report that no unitarily invariant matrix norm has a known constant-factor order for $`e`$; the Hilbert–Schmidt case is Euclidean in dimension $`n^2`$.

## Status review


**Known cases:** The target is constant-factor growth for Euclidean domains with arbitrary Banach targets. OpenAI family 332 concerns only target ell-one; Kirszbraun Hilbert targets, bilipschitz nets and different domain geometries do not determine this modulus.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is constant-factor growth for Euclidean domains with arbitrary Banach targets. OpenAI family 332 concerns only target ell-one; Kirszbraun Hilbert targets, bilipschitz nets and different domain geometries do not determine this modulus.

Additional comparison sources: [comparison source 1](https://ems.press/books/mems/283); [comparison source 2](https://arxiv.org/abs/2508.03853). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2025 primary paper improves extension upper bounds while expressly leaving constant-factor growth unknown even for Hilbert–Schmidt matrix spaces. Bounded 2026 and announcement searches found no resolution of the Euclidean question. The exact-asymptotic result for $`\ell_\infty^n`$ in Naor's book concerns a different domain geometry.

A local semantic check found no equivalent AIM or FURTHER page. [Primary-source](../FURTHER_problems/_tracking/euclidean-lipschitz-extension-primary-2026-10-20.json), [current-status](../FURTHER_problems/_tracking/euclidean-lipschitz-extension-current-2026-10-20.json), [duplicate](../FURTHER_problems/_tracking/euclidean-lipschitz-extension-duplicates-2026-10-20.json), and [coordinator](../FURTHER_problems/_tracking/euclidean-lipschitz-extension-coordinator-2026-10-20.json) receipts record the bounded review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-05291453c5ef11de**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
