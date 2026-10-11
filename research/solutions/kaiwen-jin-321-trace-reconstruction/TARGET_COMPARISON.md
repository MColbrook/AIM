# Correspondence with AIM 321

Target: [321. Polynomial sample complexity for deletion-trace reconstruction](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/321-polynomial-trace-reconstruction.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Submitted note: *A negative answer to polynomial sample complexity for deletion-trace reconstruction*.

| Original requirement | Note location and result | Coverage |
|---|---|---|
| Every fixed known deletion probability q in (0,1) | Section 1 uses deletion q; Theorem 1 quantifies over every fixed q | Full |
| All deterministic binary strings of known length n | Section 1 and Theorem 1; the cited minimum is over distinct literal length-n strings | Full |
| Complete iid traces, including empty traces and lengths, without deleted positions | Section 1 defines T_n and D_q; Lemma 1 is applied to their iid products | Same model |
| A common randomized decoder, unrestricted computation | Lemma 1 averages conditional output probabilities and imposes no runtime restriction | Full |
| q-dependent finite positive C_q,k_q, at most ceil(C_q n^{k_q}) samples | Theorem 1 and its proof cover arbitrary C,k>0 and every budget including zero; the ceiling is handled explicitly | Full |
| Exact worst-case success at least 2/3, every n>=2 | For all sufficiently large integer n, every permitted decoder fails on at least one input. Hence no bound can work for every n>=2 | Negative answer to the complete target |
| No source promise or uniformity as q approaches an endpoint | No input promises are introduced; n0 may depend on q,C,k | Same scope |
| Public mathematical dependency | Section 1 states the one-trace conclusion of OpenAI Theorem 1.2, PDF p.2, equation (1.2), at the pinned primary revision below | Attributed primary theorem |

Primary proof: [OpenAI, September 24, 2026](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf). Its Section 8 restores full trace laws and pads to every exact integer length. The new note supplies the elementary implication to the exact catalogue formulation; the multiscale construction and indistinguishability theorem are credited to that source.

This submission is a literature update with a complete analytic consequence. It requests independent mathematical review and does not assign a catalogue status.
