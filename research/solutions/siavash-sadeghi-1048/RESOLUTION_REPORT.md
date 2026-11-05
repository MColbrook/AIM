# Resolution report: AIM 1048

**Submitter:** Siavash Sadeghi. **Date:** 5 November 2026.
**Requested status:** Solution claimed, pending further independent mathematical review.
**Human review:** None. **Formal verification:** None.

The claim addresses [Can neighboring water-wave Bloch bands overlap?](https://github.com/MColbrook/AIM/blob/4f5b1659355cb61d194da94ef14615214e1363a8/problems/1048-can-neighboring-water-wave-bloch-bands-overlap.md) at repository revision `4f5b1659355cb61d194da94ef14615214e1363a8`.

The [proposed proof](research_nonoverlap_proof.pdf) claims an affirmative answer: for all n ≥ 0 and all phases θa, θb, Λn(θa) ≤ Λn+1(θb). Phase continuity makes this equivalent to the requested maximum/minimum inequality. See the [review guide](review_note.pdf) for a detailed comparison and the [submission review](SUBMISSION_REVIEW.md) for review scope and limitations.

| Repository requirement | Coverage in the proposed proof |
| --- | --- |
| Every h > 0 and real 2π-periodic C¹ graph with positive lower depth | Theorem and Section 6; analytic approximants converge in C¹ and retain positive depth. |
| Exact flat-top harmonic-extension operator and homogeneous Neumann bottom | Sections 1 and 5 preserve the Dirichlet energy and the natural bottom condition. |
| Physical surface L²(dx) mass | Section 5 supplies dx = ρ(s) ds; Section 1 gives the exact complex mass identity. |
| Arbitrary phases and separately ordered eigenvalues with multiplicity | Section 4 uses one complex evaluation constraint and injective division; coincident characters use ordinary ordering. |
| Every index n ≥ 0 | The n+2 dimensional source subspace yields a target subspace of dimension at least n+1. |
| No amplitude, parity, mean-zero or fundamental-period restriction | None is introduced. The positivity needed for the mass inequality follows from graph geometry. |
| Touching allowed | The result is non-strict; no strict gap assertion is made. |

The proof uses an automorphic strip Blaschke factor to change any nontrivial Bloch character while decreasing energy and increasing mass on one evaluation kernel. Conformal geometry supplies the required middle-line positive weight; a physical-domain form comparison covers all C¹ bottoms. Periodic/antiperiodic edge localization and monotonicity are separate questions and are not claimed.

The original package contains three detailed AI reports and a coordinating synthesis. They are preserved as supplied and are not human review or cryptographic attestations of every final byte. Codex (AI) additionally read the complete final argument, re-derived the central identities and reproduced the diagnostics for this submission. No substantive mathematical defect was identified; that assessment is fallible and the claim remains open to independent review.

The public-record check found no matching earlier submission in 180 all-state PR records, 184 issue/PR records, 111 discussion comments, zero inline review comments, and 182 public PR branch diffs. [Dated search counts](submission-search.json) and limitations are documented in the submission review. This bounded search is not a guarantee of priority.
