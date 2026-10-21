# PR 177 attribution correction for AIM 482

Date: 21 October 2026. Reviewed head: `9a0afd1f0e61b7880026edc282df2576b62183bd` in [PR 177](https://github.com/MColbrook/AIM/pull/177). Review by OpenAI Codex, independently of the authoring context; this is AI review, without human peer review or formal verification.

## Decision

Accept the attribution correction. It restores Kaiwen Jin and the supplied contact address in the manuscript, PDF metadata, README and manifest. AIM 482 retains its existing Solved classification and its [complete earlier argument audit](../2026-10-15-active-prs/482-review.md).

## Source and PDF comparison

The old and new TeX sources are byte-identical after normalizing exactly the `pdfauthor` and author/contact fields. No mathematical statement, proof, reference, target comparison or AI disclosure changes. The PDF has six pages and author metadata `Kaiwen Jin`; author and contact are visible on page 1. Extracted mathematical text across all six pages is identical after removing the inserted attribution and the known page footers, whose positions shift after typesetting the author. All six rendered pages were inspected for clipping or omitted content. All manifest byte lengths, SHA-256 payload hashes and checksum entries match the actual pinned files.

## Mathematical scope

The counterexample remains a reversible two-species cubic reaction with equal positive diffusion on a smooth three-dimensional ball. Initial data `(C/|x|, 0)` have finite entropy and belong to L2, while allowing an absent species. The reaction is locally Lipschitz and quasi-positive and dissipates the stated entropy. The singular datum is admissible in the original problem, which does not assume bounded data or a positive lower bound.

I reread the unchanged construction. Heat comparison supplies the common total concentration and uniform small-ball mass control. For the compact seed, direct calculation gives the displayed polynomial residual `-23/2 + 17s + 5s^2/2`; its two parameter ranges imply the required subsolution inequality. Its value and first derivatives vanish at the moving support boundary, so extension by zero produces no omitted surface measure. Comparison bounds every seeded solution by half the heat total. Positive-time compactness and a diagonal limit preserve a nonzero seed lower bound.

The initial trace follows from the localized exterior-mass estimate followed by the small-ball limit; it is not inferred from small initial seed mass alone. The common entropy dominator gives the actual initial entropy trace, and regularized entropy dissipation yields square-root gradient bounds. Compact concentration cutoffs make all renormalized reaction and gradient terms integrable, allowing passage to the initial time. Both the zero-catalyst solution and the nonzero limit therefore lie in the exact comparison class.

## Earlier literature

A dated search for entropy-dissipating reaction–diffusion nonuniqueness and renormalized uniqueness found no earlier matching full counterexample beyond the existing repository submission. [Fischer (2017)](https://arxiv.org/abs/1703.00730) proves weak–strong uniqueness conditional on a sufficiently regular comparison solution. [Fellner–Fischer–Kniely–Tang (2023)](https://doi.org/10.1007/s00332-023-09926-w), Remark 1.4, distinguishes the general uniqueness question. [Agresti–Kniely–Tang (2026)](https://arxiv.org/abs/2608.13332) concerns regularization by transport noise and does not supply this deterministic counterexample. Later weak–strong/interface results have different hypotheses. The current OpenAI mathematics preprint index was also checked for an overlapping result.

This bounded source search does not prove absence of unindexed work. PR 177 is an attribution repair to an already retained proof, rather than a new resolution claim; the correction does not enlarge the accepted theorem.
