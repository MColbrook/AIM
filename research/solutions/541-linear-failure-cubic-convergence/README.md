# Linear failure and cubic convergence for relaxed minimal deformation

**Maintainer decision, 21 October 2026:** Accepted as partial progress for AIM541: linear failure and cubic convergence, with the quadratic case unresolved. The [complete cubic and cell-level audit](../../solution_reviews/2026-10-21-active-prs/172-review.md) and [independent linear analytic-interval audit](../../solution_reviews/2026-10-21-active-prs/172-second-review.md) record the separate reviewers' scope. These are AI mathematical reviews, without human peer review or Lean verification. The submitted description below records its status before this reassessment.

**Partially solved (proposed): AIM Problem 541. The quadratic case remains unresolved.**

Kaiwen Jin — yui.ui.siki@gmail.com

The [manuscript](paper/manuscript.pdf) studies the original semidiscrete
relaxed minimal-deformation equations, with exact integrals on the fixed
initial surface and the discontinuous geometric unit normals of the current
elements.

| Degree | Result in this submission |
| --- | --- |
| 1 | One fixed smooth torus, fixed tangential rotation, and admissible alternating mesh family give a positive lower bound for the uniform-in-time lifted L2 map error. The original discrete solutions exist uniquely and remain nondegenerate on a common positive interval. |
| 2 | Unresolved: neither general convergence nor an admissible original-scheme counterexample is established. |
| 3 | For every original admissible cubic family and every smooth exact solution with smooth inverse on a fixed interval, the original discrete solution exists uniquely throughout the interval and its lifted map error is at most C_T h^3 sqrt(1+abs(log h)). |

The precise results are Theorems 2.2 and 6.1. The first result does not assert
failure for every linear mesh family. The second adds no mesh prescription,
stabilization, normal averaging, or modified measure to the original scheme.
This submission does not claim a complete classification of degrees 1, 2, 3.

- [Complete paper, including both proofs](paper/manuscript.pdf)
- [Editable LaTeX source](paper/manuscript.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)
- [AI use and review scope](AI_USE_AND_REVIEW.md)
- [Payload manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The paper is an analytic result. No numerical experiment, unpublished
computation, or separate proof supplement is required to follow its arguments.
The original higher-degree result is credited to Gao, Li and Tang; its
author manuscript and the Fourier-analysis reference are linked in the paper.

To rebuild with a standard LaTeX installation, run from this directory:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/manuscript.tex
```

The submitted PDF has 27 pages. Compilation and reference checks do not
constitute independent mathematical verification. Independent review is
requested; catalogue classification is left to the maintainers.
