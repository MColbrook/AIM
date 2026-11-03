# 1035. Do matrix local-mass bounds imply Stahl–Totik regularity?

**Area:** Spectral theory and matrix orthogonal polynomials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`E`$ be a finite union of disjoint closed intervals in $`\mathbb R`$, and let $`\mu`$ be an $`\ell\times\ell`$ positive matrix-valued measure with associated block Jacobi matrix having essential spectrum $`E`$. For $`\eta>0`$ and positive integers $`m`$, put

```math
S_{m,\eta}=\left\{x:\mu\!\left([x-m^{-1},x+m^{-1}]\right)\succeq e^{-\eta m}I_\ell\right\}.
```


Suppose $`|E\setminus S_{m,\eta}|\to0`$ as $`m\to\infty`$ for every $`\eta>0`$, where $`|\cdot|`$ is Lebesgue measure and $`\succeq`$ is the positive-semidefinite order. **Must $`\mu`$ be regular?** In the source's notation, this means the determinant of the off-diagonal block Jacobi coefficients obeys

```math
\lim_{n\to\infty}\bigl|\det(A_1\cdots A_n)\bigr|^{1/n}=\mathrm{Cap}(E)^\ell.
```


This is Conjecture 5.9 of Damanik, Pushnitski and Simon. Their scalar direct-sum case follows from an existing Stahl–Totik theorem; the conjecture asks about general matrix measures.

## Application

The proposed criterion would let local spectral-mass information establish the large-degree asymptotics of matrix orthogonal polynomials and their block Jacobi parameters.

## References

- D. Damanik, A. Pushnitski and B. Simon, [*The Analytic Theory of Matrix Orthogonal Polynomials*](https://surveys-in-approximation-theory.com/papers/11/11.pdf), *Surveys in Approximation Theory* **4** (2008), 1–85. See printed pp. 68–72, especially (5.1), Theorem 5.4 and Conjecture 5.9; [publisher record](https://surveys-in-approximation-theory.com/papers/11/index.html).

## Status review


**Known cases:** The local matrix-mass condition must imply determinant regularity for general matrix measures. Scalar direct sums, other matrix regularity criteria and GMP Cesaro-Nevai results do not establish it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The local matrix-mass condition must imply determinant regularity for general matrix measures. Scalar direct sums, other matrix regularity criteria and GMP Cesaro-Nevai results do not establish it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper proves matrix regularity criteria and notes the direct-sum special case, but leaves the general local-mass implication as Conjecture 5.9. The later [GMP-matrix regularity paper](https://arxiv.org/abs/2008.11884) proves a different Cesàro–Nevai conjecture, and the [2025 habilitation account](https://benjamineichinger.eu/pdf/habilitation.pdf) does not announce this exact implication. Bounded searches through 22 October 2026 found no matching complete proof, counterexample or announcement; this negative result is not exhaustive. The [publisher-PDF body receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0679-J321-remote-pdf-body-review.json), [scope/status audit](../FURTHER_problems/_tracking/matrix-stahl-totik-2026-10-22-status.json) and [duplicate audit](../FURTHER_problems/_tracking/matrix-stahl-totik-2026-10-22-duplicates.json) record the checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fbfaae302efa3887**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
