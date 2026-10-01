# Resolution report: AIM 558

**Claim:** Complete disproof, pending independent review.  
**Suggested evidence status:** Solution claimed.  
**Prepared:** 1 October 2026.  
**Contributor / submitter:** Siavash Sadeghi.  
**Repository:** MColbrook/AIM, main branch.  
**Target path:** `problems/558-gaussian-variational-variance-ordering.md`.  
**Target title:** Variance ordering for Gaussian alpha-divergence approximations.  
**Observed target status:** Open; last checked 24 September 2026.  
**Repository commit SHA:** `aa776a01d7d48a79f93251af11fde9454b0aea95` (confirmed from a fresh read-only clone on 1 October 2026).

## Result

For the fixed rational target precision

```
K = [[37/5,       -4,       -4],
     [  -4,   243/70,     17/7],
     [  -4,     17/7,   243/70]],
```

let the target be N(0, K^{-1}) and let Psi(a) be its unique optimal diagonal Gaussian covariance for the divergence in the target statement. The proof establishes:

- Psi(10) = I_3.
- Psi_11(a) > 1 and Psi_22(a) = Psi_33(a) < 1 for every a > 10.

In particular, the finite pair a_1=10, a_2=11 violates the requested coordinatewise inequality in two coordinates. The proof is an exact global convex-optimization comparison; it does not depend on rounding, a numerical optimizer, or a limiting alpha value.

## Theorem-to-target comparison

| Target requirement | Where it is met |
|---|---|
| Real dimension at least two | Dimension three; also proved to be minimal for a counterexample |
| Fixed non-diagonal positive-definite covariance | The displayed K equals (R^{-1}+9I)/10 for an explicitly positive-definite R; its exact inverse is displayed |
| Gaussian target and all positive diagonal Gaussian approximations | Section 2 derives the original Gaussian-integral objective, including optimization over the mean |
| Same divergence direction and exponent convention | Equation (1) is integral p^a q^(1-a), with denominator a(a-1), exactly as in the target |
| Two parameters strictly above one | The exact finite pair is 10 and 11 |
| Finite-divergence domain | H=aK-(a-1)T is positive definite at every comparison point; the optimizer is proved to exist in the interior |
| Global rather than local optima | Strict convexity, a barrier/existence argument, and uniqueness are proved in Proposition 2 |
| Violation of coordinatewise covariance ordering | Both leaf precisions at a=11 exceed one, hence both leaf variances are strictly below their value one at a=10 |
| No change of target as a changes | K is fixed throughout; only the rational comparison precision depends on a |
| Not the paper's different score-divergence comparison | Only two members of the alpha-divergence family are compared |

The note also proves a general logarithmic sensitivity identity and strict determinant/entropy monotonicity for all non-diagonal Gaussian targets when a>1. These results are additional, not prerequisites for the disproof.

## Evidence and reviewers

**Proof artifact:** `aim_558_counterexample.pdf`, with editable source `aim_558_counterexample.tex`.

**Exact arithmetic audit:** `verify_558.py`, Python standard library only. It checks twelve exact conditions, including positive definiteness, the inverse covariance, stationarity at 10, the feasible comparison point and signed gradient at 11, the exact sensitivity vector, and supplemental cubic signs. The recorded successful output is `exact_audit_log.txt`.

**Symbolic and numerical cross-check:** `symbolic_audit_558.py`, audited using SymPy 1.14.0 and mpmath 1.3.0. It checks the full rational-function identity for the comparison curve and independently solves the original precision stationarity equations at 90-digit working precision. The recorded output is `symbolic_audit_log.txt`.

**Review performed:** The original package's AI assistant generated the argument, re-derived the convex comparison and sensitivity calculation, checked the source statement and original paper, and ran the arithmetic audits during the original research session.

**Review not performed:** No independent human review, external AI reviewer, peer review, published acceptance, or proof-assistant/kernel verification. Algebra checks do not formally verify the real-analysis portions of the argument. No claim of exhaustive literature novelty is made.

## Local revision review - 1 October 2026

Prepared for submission by **Siavash Sadeghi**. The proof content remains explicitly AI-generated; this attribution does not assert that the contributor independently proved or reviewed it. Codex (AI assistant) compared the complete note with the pinned target, read the proof argument, and reviewed the contribution rules. No critical mathematical gap was identified in that review; this is not independent human review or formal verification. Current run details and limitations are in `REVIEW_AND_CHECKS.txt`. Historical literature-search statements above describe the supplied package, not a new exhaustive search.

The repository permits **Solution claimed** reports while independent review is pending. Independent review is needed for a stronger evidence status, not as a prerequisite to reporting a claim. See the README for the existing supporting comments and this supplementary pull request.

## Primary sources checked

1. Repository target: https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/558-gaussian-variational-variance-ordering.md
2. C. C. Margossian, L. Pillaud-Vivien and L. K. Saul, *Variational Inference for Uncertainty Quantification: an Analysis of Trade-offs*, JMLR 26(202) (2025), 1–41. Definition 2, p.5, and Remark 12, p.26: https://www.jmlr.org/papers/v26/24-0878.html
3. Latest manuscript version checked, arXiv:2403.13748v5, 19 October 2025: https://arxiv.org/html/2403.13748v5
4. Repository contribution/status rules: https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/CONTRIBUTING.md

The JMLR PDF pages containing the ordering definition and conjecture were visually inspected. Web searches on 1 October 2026 did not locate a matching later resolution, but this does not certify publication priority.


## Submission context

The proof was shared in the existing repository discussion before this PR.
See the README for links, the overlap with the existing proof, and the scope
of this supplementary contribution. No priority or independent-review claim
is made, and no catalogue status change is proposed.
