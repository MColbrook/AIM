# Local no-slip Navier--Stokes equations under stochastic parabolicity

Kaiwen Jin, revision of 19 October 2026.

**Revised complete solution claim, awaiting independent review.** The [15 October review of PR171](../solution_reviews/2026-10-15-active-prs/458-review.md) correctly found a missing compatible fractional right-inverse hypothesis in the original channel-calculus argument. The repository recorded that version as partial progress. New Lemmas 3.1--3.2 supply the extra channel regularity and both compatible right-inverse estimates required by the 2013 erratum. The historical review is preserved. See the [point-by-point response](REVISION_RESPONSE.md) for the precise repair and its review limits.

The target remains [AIM Problem 458](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/458-stochastic-navier-stokes-no-slip-local.md), fixed revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. The abstract and Theorem 1.1 are unchanged. The claimed result covers every bounded smooth three-dimensional domain, positive viscosity and finite smooth solenoidal wall-tangent noise satisfying only stochastic parabolicity. It asserts adapted local existence, the exact requested Besov/Sobolev path class, uniqueness among all solutions in that class and continuous dependence in probability after pairwise common stopping. No added amplitude smallness or interior-rank restriction is imposed.

- [Revised manuscript, PDF](paper/paper.pdf) and [editable LaTeX](paper/paper.tex).
- [Response to the blocking finding](REVISION_RESPONSE.md).
- [Original-target comparison and external inputs](TARGET_COMPARISON.md).
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The linear argument combines explicit channel and full-torus models with Stokes energy-form localization, negative-order pressure estimates and a quantitative square-root comparison. An adapted cutoff and stopped energy argument give the nonlinear conclusions. This is an analytic claim: no numerical certificate or formal proof is asserted. Broader rough/infinite-noise regimes and global three-dimensional regularity are outside its scope.

## Rebuild and artifact checks

From `paper/`, with a standard LaTeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The source uses standard LaTeX packages and no external assets. The supplied PDF was built with pdfTeX/TeX Live 2025 and has 22 pages. Its final log has no unresolved citation/reference or layout warning. Every page was read and visually inspected, and the typed-reference preflight found no mismatched or unresolved target. These checks verify the artifacts, not the mathematical theorem.

## AI use and evidence limits

OpenAI Codex was used extensively for the argument, source checks, writing and author audits. Two additional Codex contexts reviewed an earlier draft as reader and referee without the author checks or each other's report. The present repair and full natural-language recheck were performed in the same context; no new independent review of the new lemmas is claimed. These same-provider checks are not human peer review, Lean verification or upstream acceptance. Independent review of the revised complete argument is requested.
