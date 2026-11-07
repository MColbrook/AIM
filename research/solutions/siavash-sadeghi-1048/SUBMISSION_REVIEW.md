# Submission review and search record

**Date:** 5 November 2026. **Reviewer:** Codex (AI), in this submission chat.
**Target revision:** `4f5b1659355cb61d194da94ef14615214e1363a8`. **No human has reviewed the work.**

## Scope and mathematical findings

I read the complete six-section proof and the review guide, then compared the supplied AI reports. This is an additional AI review with access to those reports, not a blind independent review. The original reports' claims about separate reviewer contexts are supplied provenance; I did not recreate or verify their original sessions.

The single-factor derivative is c(1-t²)(1-τ²)/(1+iτt)². Summable normalized tails give a nonzero product away from the simple zero lattice, and the translation quotient is b+/b−, so division subtracts χ=(1−y/d)/2. The phase choice therefore sends the source character to the desired target character. Fixed interior y suffices; no uniform edge limit is used.

For complex Bloch Fourier coefficients, conjugation and index exchange replace exp(d(n−m)) by cosh(d(n−m)) in the real part of the cross integral. This yields the middle-line mass with p and cancels the Bloch phase. The real-part operation and positivity of p are essential. Equal edge moduli and |B|≤1 then give the mass comparison. From Δ|F|²=4|F′|² and Q=½∫|F′|², Green's formula gives exactly the ¼ boundary-loss factor. Unit characters cancel the lateral boundary terms separately.

The one complex evaluation condition has codimension at most one in an n+2 dimensional complex spectral approximation. Division and reconstruction are injective, since the reconstruction multiplier cosh(dk) is positive. This produces the correct n+1 dimensional target space and comparison direction, including repeated eigenvalues and the zero frequency.

For analytic physical graphs, annular uniformization preserves the period after lifting. Nonvanishing boundary derivatives and degree one force the bottom horizontal derivative p>0; positivity of an arbitrary surface weight alone would not suffice. The transformed mass is physical dx. For C¹ convergence, the fixed-domain coefficient matrix has determinant one and stays uniformly positive; relative energy comparison passes through harmonic minimization and min-max. The added top-mass term controls phase continuity and attained extrema. No restriction absent from the repository statement was identified.

No substantive defect was found. This is an informal mathematical review, not formal verification or a proof established by numerical experiments. The mathematical proof body is unchanged in this submission.

## Reproduced checks and correction

The source script used Python assertions, which disappear under `-O`. Validation now raises explicit exceptions, rejects non-finite data, checks the already recorded modulus/normal-derivative/quotient inequalities, and has negative-control regression tests. The underlying numerical construction and recorded 21-case outputs are unchanged. [Build and reproduction record](BUILD_VERIFICATION.txt) gives the results and limitations; [metadata](metadata.json) pins the final proof source and input archive.

## Public submission search

The fresh GitHub API check covered every page of all-state PRs, issues (including PRs), issue discussion comments and inline review comments. It searched titles/bodies for AIM1048, the current title, water-wave band overlap, the Blaschke nonoverlap construction, arXiv 1706.07417, DOI 17M113561X, EMSS/93 and stable key FURTHER-787bd7da5d0b8ea8. Every accessible public PR head was fetched; added text and paths were searched against the merge base with current main. [The summary](submission-search.json) records 180 PRs, 184 issue/PR records, 111 comments, zero inline review comments and 182 PR heads, with no matches. Current solution folders contained no matching package. Historical routing/audit records about this open problem are not prior solutions.

The search does not cover private repositories, inaccessible/deleted history, external unindexed work, or every standalone review-summary body. Publication priority cannot be guaranteed.

## Primary-source and literature check

The [2018 primary paper, introduction after Definition 1.1](https://arxiv.org/html/1706.07417v2) distinguishes general nonoverlap from the separate edge-location question. The [2025 primary paper, Section 4, printed p. 270](https://ems.press/content/serial-article-files/50748) develops perturbative gaps and does not supply this general theorem. Targeted searches for water-wave Bloch band nonoverlap, periodic-bottom proofs and the Blaschke construction found no later matching general resolution; results about other wave models, flexible structures and shallow approximations do not match the target. The standard annular uniformization and analytic reflection background is Ahlfors, *Complex Analysis*, third edition, Chapter VI; its connectivity-two mapping has no remaining circular slits. These checks do not amount to an exhaustive literature review.
