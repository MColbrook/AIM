# AIM 412: an attributed literature resolution

The assertion that the downstream transport-control cost tends to zero for
every T>L/M has a negative answer. For every fixed L,M>0, the admissible
time T=3L/(2M) instead has control cost tending to infinity.

This package explains the implication of Kai Koike and Vincent Laheurte's
[arXiv:2609.35355v1](https://arxiv.org/abs/2609.35355v1),
Theorem 4.1 (PDF pp. 16--18), for the exact
[AIM 412 statement at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/412-positive-transport-sharp-uniform-control-time.md).
The threshold theorem belongs to Koike and Laheurte. This contribution is a
literature update and an explanation of scaling and transposition duality.

## Materials

- [Complete note](manuscript.pdf) and [editable LaTeX source](manuscript.tex).
- [Target comparison](TARGET_COMPARISON.md), including the equation,
  parameter range, data/control classes and full negative answer.
- [Public file manifest](PUBLIC_MANIFEST.json) and [SHA256 sums](SHA256SUMS).

The three-page note proves divergence for each fixed 0<T<2L/M. The source
leaves the critical time T=2L/M open; that endpoint is not needed to refute
the universal assertion in this problem. No numerical or formal proof claim
is made.

## Rebuilding

The source is a standalone article using standard LaTeX packages
(geometry, fontenc, lmodern, amsmath, amssymb, amsthm and hyperref).
With TeX Live and latexmk installed, run:

    latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

The supplied PDF was built with TeX Live 2025 and checked on all three pages.
The editable source builds using only this package and the standard TeX
distribution. No auxiliary research repository or proof supplement is needed.

The manifest hashes the four content files: this README, the note PDF,
the note source and the target comparison. SHA256SUMS additionally hashes
the manifest; neither file attempts to hash itself.

## AI use and review

OpenAI Codex retrieved sources, checked the theorem's connection to the
stated control problem, and drafted the explanatory note and comparison.
The same AI checked the full mathematical argument and the source's
applicability. No independent human or formal verification is asserted.
No separate detailed AI review is supplied; independent mathematical review
is requested. Catalogue classification remains for maintainer review.

Manuscript author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
