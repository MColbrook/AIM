# Supplementary resolution report: AIM 457

**Claim:** Complete affirmative proof under the stated Bessel-family hypothesis; independent review pending.  
**Suggested evidence status:** Solution claimed.  
**Prepared:** 1 October 2026.  
**Contributor / submitter:** Siavash Sadeghi.  
**Target:** `MColbrook/AIM`, main branch, `problems/457-infinite-time-dynamical-frame-discretization.md`.  
**Title:** Finite-density time sampling of an infinite observation window.  
**Observed status:** Open; last checked 22 September 2026.  
**Repository commit SHA:** `aa776a01d7d48a79f93251af11fde9454b0aea95` (confirmed from a fresh read-only clone on 1 October 2026).

## Proof artifact and conclusion

See `aim_457_uniform_sampling.pdf` and its LaTeX source. For every bounded normal A and initial Bessel family satisfying the target's infinite-window continuous frame bounds m,M, every sufficiently small uniform grid T=delta*N_0 gives the required unweighted frame. The note provides explicit delta and frame constants, and D^+(T)=1/delta.

## Key steps and hypothesis audit

1. On the spectral subspace |z|<=r<1, the initial Bessel bound gives a continuous-energy upper bound B_0/(-2 log r). Choosing r=exp(-B_0/m) contradicts the continuous lower bound unless that spectral subspace is zero. This excludes both the kernel and spectral accumulation at zero.
2. Boundedness, normality and this spectral gap yield a bounded Borel logarithm L with A^t=exp(tL) for exactly the argument branch prescribed in the target. A holomorphic logarithm is not assumed.
3. For the observation trajectory F_f(t)=C exp(tL*)f, its derivative is F_{L*f}. The continuous upper frame bound therefore gives an L2 derivative bound sqrt(M)||L||||f||. No operator-norm decay or exponential stability is used.
4. Left-sample step functions on a uniform grid approximate F_f in L2 with error at most delta||F_f'||_2. Triangle inequalities supply two-sided discrete frame bounds.
5. The single constant delta from integration over grid intervals is absorbed into the frame constants. There are no time-dependent weights, repeated grid points, or altered sensor vectors. The grid is locally finite with finite upper Beurling density.

The example A e_n=exp(-1/n)e_n, g_n=sqrt(2/n)e_n has continuous frame bounds 1,1 and ||A^t||=1; it demonstrates applicability without exponential stability.

## Review and limitations

The supplied package attributes the original reasoning and checks to one AI assistant. There was no independent human or external AI review and no formal proof-assistant verification. This note does not claim to solve variants with unbounded generators, unbounded observations, or no Bessel hypothesis on the initial sensor family. It makes no certified novelty claim.

## Local revision review - 1 October 2026

Prepared for submission by **Siavash Sadeghi**. The proof content remains explicitly AI-generated; this attribution does not assert that the contributor independently proved or reviewed it. Codex (AI assistant) compared the complete note with the pinned target, read the proof argument, and reviewed the contribution rules. No critical mathematical gap was identified in that review; this is not independent human review or formal verification. Current run details and limitations are in `REVIEW_AND_CHECKS.txt`. Historical literature-search statements above describe the supplied package, not a new exhaustive search.

The repository permits **Solution claimed** reports while independent review is pending. Independent review is needed for a stronger evidence status, not as a prerequisite to reporting a claim. See the README for the existing supporting comments and this supplementary pull request.

## Primary sources checked

- Repository target: https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/457-infinite-time-dynamical-frame-discretization.md
- A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, La Matematica 5 (2026), article 37; Open Problem 1 and section 5.2(B): https://arxiv.org/html/2511.10769v3 ; https://doi.org/10.1007/s44007-026-00215-y
- R. Diaz Martin, I. Medri and U. Molter, *Continuous and discrete dynamical sampling*, JMAA 499 (2021), 125060; Theorem 3.4 assumes exponential stability: https://arxiv.org/html/2006.08046v1


## Submission context

The proof was shared in the existing repository discussion before this PR.
See the README for links, the overlap with the existing proof, and the scope
of this supplementary contribution. No priority or independent-review claim
is made, and no catalogue status change is proposed.
