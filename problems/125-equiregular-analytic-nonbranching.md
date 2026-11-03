# 125 — Nonbranching of analytic equiregular sub-Riemannian geodesics

**Area:** Nonholonomic geometry / optimal transport

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

Let $`(M,\Delta,g)`$ be real analytic, with $`g`$ a positive inner product on the bracket-generating distribution $`\Delta`$. Define $`\Delta^1=\Delta`$ and let $`\Delta^{j+1}`$ be spanned by $`\Delta^j`$ and brackets of local sections of $`\Delta`$ with sections of $`\Delta^j`$. Assume equiregularity: the rank of each $`\Delta^j`$ is constant on $`M`$.

Are length-minimizing geodesics nonbranching? Precisely, if $`\gamma_1,\gamma_2:[0,L]\to M`$ are unit-speed horizontal length minimizers and agree on $`[0,\varepsilon]`$ for some $`\varepsilon>0`$, must they agree on all of $`[0,L]`$?

## Application

Branching allows optimal motions to share an initial trajectory and then split. Excluding it would clarify uniqueness structures used in nonholonomic transport and motion planning.

## References

1. T. Rossi, A. J. A. Schiavoni Piazza and A. Socionovo, *Interior singularity and branching of geodesics in real-analytic sub-Riemannian manifolds* (2026), [arXiv:2603.23068](https://arxiv.org/abs/2603.23068), §1.4, second Open problem. Exact source of the equiregular question.
2. E. Le Donne, N. Paddeu and A. Socionovo, *Metabelian distributions and sub-Riemannian geodesics* (2026), [Advances in Calculus of Variations](https://doi.org/10.1515/acv-2025-0104), Theorem 1.1 and structural definitions. Supplies a regularity result in a restricted analytic setting, rather than a general nonbranching theorem.

## Status review

**Resolution update (3 November 2026):** Counterexample. Theorem1.3 proves branching minimizing geodesics in Carnot groups. Those structures are analytic and equiregular, and the lift preserves length minimality and branching of curves sharing a nontrivial initial segment. Common arclength parametrization gives the local unit-speed convention. The nonequiregular3D example alone would not suffice; the Carnot lift is essential.

[Proof](https://arxiv.org/pdf/2603.23068v3) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-a/125.json). Source locator: Theorem1.3 and Carnot-group lifting in§10.

### Earlier status record


Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Result: negative: branching analytic equiregular minimizers

[Proof or source](https://arxiv.org/pdf/2603.23068v3) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-125). The linked review records the target comparison.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-125). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Literature check:** Open in cited literature; no later resolution located.

Rossi–Schiavoni Piazza–Socionovo construct analytic branching minimizers in a non-equiregular Martinet region and explicitly pose the remaining equiregular question. Smoothness or $`C^1`$ regularity alone does not settle branching. Searches included “equiregular real analytic sub-Riemannian nonbranching 2026” and “2603.23068 branching equiregular solution”. No subsequent answer to the stated question was located.
