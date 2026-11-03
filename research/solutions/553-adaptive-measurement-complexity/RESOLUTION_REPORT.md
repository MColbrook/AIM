# Pre-submission mathematical check: AIM 553

Checked on 2026-10-03 by OpenAI Codex (AI), against the repository statement pinned in [SUBMISSION.json](SUBMISSION.json). This is an AI-assisted pre-submission check, not a documented independent human audit, acceptance decision, or proof-assistant verification. No substantive proof gap was found in this check.

The proof establishes the alternative target of sharp asymptotic growth: floor(log2(m))+1 <= N(m) <= ceil(log2(m))+1. It also determines N(m) at powers of two. It leaves the exact values at other dimensions, including N(3), open.

The audit checked the Borsuk-Ulam normalization of antipodal genus, coordinatewise Tietze extension on compact metric spaces, and the odd-zero-set inequality. For the even-fibre lemma, explicit alternating grid intervals have length below a Lebesgue number, and same-colour intervals are disjoint. Distance-to-complement weights give a continuous odd nonvanishing map into twice the fibre dimension. This justifies the halving bound without assuming regular level sets or finite-dimensional cell complexes.

At each adaptive stage, the preceding transcript is fixed on a compact invariant set, so only the required branchwise continuity is used. After n-1 stages, m >= 2^n leaves genus at least two. The final odd difference has a zero, producing an indistinguishable antipodal pair on every sphere. The Euclidean error is at least the arbitrary radius. Early stopping can be padded with constant measurements. No continuity of the whole encoder, of history dependence, or of the decoder is assumed.

A second Codex agent separately challenged the even-fibre lemma and adaptive quantifiers and found no gap. The root check replaced the implicit interval refinement and partition of unity by explicit choices and added the missing background references. No numerical test can certify this topological argument; none is represented as doing so.

The checked claim is submitted for pull-request review. The catalogue page and status are unchanged. The source snapshot, original notes and reference audit are included so reviewers can assess the argument and its scope.
