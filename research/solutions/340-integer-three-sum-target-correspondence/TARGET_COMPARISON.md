# Exact target comparison: AIM Problem 340

Statement: [The modern integer 3SUM conjecture](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/340-integer-three-sum-hardness.md), Problem 340, revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The submitted [paper](paper/aim340_target_correspondence.pdf) is a literature-based target correspondence. Its fixed-power algorithmic input is the theorem of Josh Alman and Virginia Vassilevska Williams in [arXiv:2610.06783v1, Theorems 2 and 22, Section 3.4](https://arxiv.org/html/2610.06783v1#S3.SS4). It is not a claim to have discovered that algorithm.

| Requirement in the pinned target | Correspondence in the paper |
| --- | --- |
| Every integer `n >= 3` | Theorem 3; the construction has `m >= 2`, including the smallest size. |
| Every explicitly listed `n`-element integer set in `[-n^3,n^3]` | Sections 1–2 and Theorem 3 impose no distribution, clustering, sign or spread promise. |
| Three **pairwise distinct** original elements with `a+b=c` | Proposition 2: rank bits separate the summands; deleting zero prevents equality with the output. |
| Witnesses with output `c=0` | The initial sorted opposite-pair stage detects the distinct triple `(x,-x,0)`. |
| Source zero-sum formulation | The tags `1,2,-3` and `Q=4n^3+1` force exactly one value from each role; Proposition 2 proves both directions. |
| Fixed polynomial integer magnitude for each source call | Lemma 1: `N=2m` lies in `[n,2n]` and every entry has magnitude at most `N^6`; the fixed source parameter is `nu=6`. |
| Classical word-RAM with `Theta(log n)` words | Section 3: all new integers use `O(log n)` bits, and `log N=Theta(log n)`; the fixed logarithmic-word constant suffices. |
| A uniform finite program and no free advice | Section 3 fixes the source algorithm for `nu=6` and uses fixed sorting, binary rank and bit-loop procedures. |
| All input-dependent preprocessing counted | Section 3 charges sorting, opposite-pair tests, instance construction and the entire source-call time, including preprocessing. |
| Per-input success probability at least `2/3` | Proposition 2 and deterministic source calls give success probability `1` for every input. |
| Maximum over valid inputs of expected **total** steps | The deterministic uniform all-input bound also bounds the maximum of the expectations in the target definition. |
| One fixed positive power saving for all large sizes | Theorem 3: finite binary algebra absorbs `O(log n)` calls and yields `O(n^(2-1/2500))`; `epsilon=1/2500` is fixed. |

The transfer is analytic and uses no finite numerical test as proof. The external source algorithm remains a cited theorem: its statement, model and application conditions are checked, but its complete proof and Lean development are not independently certified by this note. The conclusion applies to every quantifier of the pinned target if the cited source theorem is used as stated. Any correction to that theorem requires revisiting this correspondence. Maintainer review and catalogue status are separate from this submission.
