# 518. Whitney extension with a 2^D test threshold and single-exponential loss

**Area:** Numerical analysis; approximation and complexity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For integers $`m\ge2`$, $`n\ge1`$, set $`D=\binom{m+n-1}{n}`$. Use the real scalar space $`C^{m-1,1}(\mathbb R^n)`$ with the homogeneous seminorm
```math
[F]_{m-1,1}
 =\sup_{x\ne y}
 \left(\sum_{|\alpha|=m-1}
 \frac{|\partial^\alpha F(x)-\partial^\alpha F(y)|^2}{|x-y|^2}\right)^{1/2}.
```

No supremum of the function or its lower derivatives is included.

Do absolute constants $`\gamma>0`$, $`p\ge1`$ exist such that, for every $`m,n`$, every subset $`E\subseteq\mathbb R^n`$ and every $`f:E\to\mathbb R`$, the following holds?

If each finite $`S\subseteq E`$ with $`|S|\le2^D`$ admits a global extension $`F_S\in C^{m-1,1}(\mathbb R^n)`$ satisfying $`F_S|_S=f|_S`$ and $`[F_S]_{m-1,1}\le1`$, then one global extension $`F`$ satisfies
```math
F|_E=f,\qquad [F]_{m-1,1}\le\exp(\gamma D^p).
```

The constants must be independent of $`m,n,E,f`$. No linear selection, algorithm or minimality of the test threshold is required.

## Application

Quantitative local tests for smooth interpolation could improve the guarantees available when fitting functions to scattered data.

## References

- J. Carruth, A. Frei-Pearson, A. Israel and B. Klartag, [*A coordinate-free proof of the finiteness principle for the Whitney extension problem*](https://arxiv.org/html/1808.06658v2), Introduction after Lemma 1.3 and the seminorm definition.
- J. Carruth, A. Frei-Pearson and A. Israel, [*The norm of linear extension operators for $`C^{m-1,1}(\mathbb R^n)`$*](https://arxiv.org/html/2109.03770v2), Advances in Mathematics 410 (2022), 108698, [DOI:10.1016/j.aim.2022.108698](https://doi.org/10.1016/j.aim.2022.108698), Introduction, Theorems 1.2–1.4 and the subsequent simultaneous-constants question.

## Status review


**Known cases:** The latest author version improves the extension loss at a larger test threshold; it retains the simultaneous 2^D and exp(poly(D)) question. No later matching result was located.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked 2026-10-30. The 2022 paper explicitly retains this simultaneous question. Its improved loss requires a larger test threshold; the known $`2^D`$ threshold has a larger loss. The case $`m=2`$ is already covered by stronger known bounds.

Bounded current searches found no matching complete resolution or announcement. Nearby full statements in AIM, this collection and the current OpenAI announcement index differ. Review evidence: [source and current comparison](../FURTHER_problems/_tracking/focused-Whitney-sharp-finiteness-number-and-single-exponential-constant-C341-A-20261030/OWNER-EXACT-SIMULTANEOUS-2POWERD-WHITNEY-AND-EXPPOLYD-LOSS-PRIMARY-2022-REMAINING-QUESTION-SEMANTIC-PROPOSAL.json), [independent model check](../FURTHER_problems/_tracking/focused-Whitney-sharp-finiteness-number-and-single-exponential-constant-C341-A-20261030/B-INDEPENDENT-SIMULTANEOUS-WHITNEY-2POWERD-SEMINORM-ARBITRARY-E-2022-SCOPE-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/ROOT-FINAL-Whitney-simultaneous-two-power-D-single-exponential-loss-admission-20261030.json).


### Online recheck, 2026-10-30

The latest author version improves the extension loss at a larger test threshold; it retains the simultaneous 2^D and exp(poly(D)) question. No later matching result was located.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2109.03770); [status source 2](https://arxiv.org/abs/1808.06658). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-bb2c7ec31084966f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
