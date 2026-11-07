# 1048. Can neighboring water-wave Bloch bands overlap?

**Area:** Water waves and spectral theory
**Status:** ✅ SOLVED
**Last checked:** 2026-11-07

## Problem statement

Fix $`h>0`$ and a real $`2\pi`$-periodic $`b\in C^1(\mathbb R)`$ with $`h-b(x)\ge c_0>0`$. Set
```math
\Omega_b=\{(x,y)\in\mathbb R^2:-h+b(x)<y<0\}.
```

For each $`\theta\in[-\tfrac12,\tfrac12]`$, use traces $`f\in H^1_{\mathrm{loc}}(\mathbb R)`$ satisfying $`f(x+2\pi)=e^{2\pi i\theta}f(x)`$. Their harmonic extensions satisfy
```math
\Delta\Phi=0\ \text{in }\Omega_b,\qquad
\Phi(x,0)=f(x),\qquad
\partial_\nu\Phi=0\ \text{on }y=-h+b(x),
```

with the same quasiperiodicity and finite energy on a period cell. The free-surface Dirichlet–Neumann map is $`f\mapsto\partial_y\Phi(x,0)`$.

Write its fiber eigenvalues on one period cell in increasing order, including multiplicities:
```math
\Lambda_0(\theta)\le\Lambda_1(\theta)\le\cdots.
```

Define
```math
\Lambda_n^-=\min_\theta\Lambda_n(\theta),\qquad
\Lambda_n^+=\max_\theta\Lambda_n(\theta).
```

**Must $`\Lambda_n^+\le\Lambda_{n+1}^-`$ hold for every $`n\ge0`$ and every such bottom profile?**

Touching bands are allowed. There is no small-amplitude assumption, and the labels are ordered fiber eigenvalues rather than analytic branches continued through crossings.

## Application

These bands govern propagation of linearized free-surface waves above periodic seabeds. Their ordering would clarify which frequency ranges can be separated by forbidden propagation intervals.

## References

1. W. Craig, M. Gazeau, C. Lacave and C. Sulem, *Bloch theory and spectral gaps for linearized water waves*, **SIAM Journal on Mathematical Analysis** 50(5) (2018), 5477–5501, [DOI:10.1137/17M113561X](https://doi.org/10.1137/17M113561X). The question is explicit in the introduction after Definition 1.1. See [arXiv:1706.07417v2](https://arxiv.org/html/1706.07417v2), with first version dated 22 June 2017.
2. C. Lacave, M. Ménard and C. Sulem, *Bloch–Floquet band gaps for water waves over a periodic bottom*, **EMS Surveys in Mathematical Sciences** 12(1) (2025), 243–288, [DOI:10.4171/EMSS/93](https://doi.org/10.4171/EMSS/93), Section 4, p. 270. Its results construct gaps perturbatively; the general ordering is not established there. Section 3.4 distinguishes ordered eigenvalues from analytic relabelings.

The source also asks about periodic/antiperiodic band edges. That additional question and stronger monotonicity statements are separate from the inequality above.

## Status review

### Reviewed resolution, 2026-11-07

The AI-assisted [proof submitted by Siavash Sadeghi](../research/solutions/siavash-sadeghi-1048/research_nonoverlap_proof.pdf) establishes the full nonoverlap inequality for every admissible C¹ graph bottom, every ordered index, and all phase pairs. The [resolution report](../research/solutions/siavash-sadeghi-1048/RESOLUTION_REPORT.md) compares the submission with the exact target; the [review guide](../research/solutions/siavash-sadeghi-1048/review_note.pdf) explains the argument and its scope.

**Review:** On 7 November 2026, Codex (AI), separately from the submission workflow, checked the complete six-section proof against the canonical target, rederived its central identities, checked the cited primary sources and reproduced the supplementary diagnostics. The [independent audit](../research/solution_reviews/2026-11-07-pr186/1048-review.md) documents the argument and the limits of the review. No mathematical gap or restriction excluding part of the target was found, so the status is **Solved** under the repository's documented-audit criterion. This is an independent AI review, not human peer review or Lean verification. The supplied audits and [submission review](../research/solutions/siavash-sadeghi-1048/SUBMISSION_REVIEW.md) remain historical evidence.

The proof uses conformal geometry, an exact complex mass identity and a strip Blaschke division argument followed by ordered min-max and C¹ form convergence. It adds no amplitude, symmetry, mean-zero or simplicity assumption. Touching is allowed; band-edge localization and monotonicity are not claimed. [Reproduction details](../research/solutions/siavash-sadeghi-1048/BUILD_VERIFICATION.txt) distinguish computational checks from the analytic proof.

### Earlier status review, 2026-10-30 (historical)

Before this submission, the recorded remaining target was the full nonoverlap inequality. The following dated search describes that earlier state, rather than a remaining gap in the reviewed proof.

No small bottom-amplitude condition is allowed and band labels are ordered fiber eigenvalues. Perturbative gap constructions and analytic branch relabeling do not prove the no-overlap inequality.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2025 paper establishes perturbative gaps, with smallness depending on the spectral range; it does not establish the general inequality above. No matching complete proof, counterexample or announced resolution was located in the dated bounded search.

The [source and current review](../FURTHER_problems/_tracking/focused-water-wave-Bloch-band-order-C162-A-20261028/WATER-WAVE-BAND-ORDER-EXACT-PRIMARY-CURRENT-981MODELS614P-1704ROWS-PEER-PASS-NO-ADMISSION.json), [independent review](../FURTHER_problems/_tracking/focused-water-wave-Bloch-band-order-C162-A-20261028/ROOT-EXACT-PRIMARY-FIBER-MODEL-CURRENT-STATUS-REVIEW-PASS.json) and [all-status comparison](../FURTHER_problems/_tracking/focused-water-wave-Bloch-band-order-C162-A-20261028/ROOT-FRESH-981MODELS614P-1704ROWS-CONTENT-DUPLICATE-GATE.json) preserve the model and search limits. These are AI checks, not human peer review or a proof certificate.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-787bd7da5d0b8ea8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
