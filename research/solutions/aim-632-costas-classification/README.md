# AIM 632: classification of Costas polynomials over extension fields

Author: Kaiwen Jin ([yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)).

This package presents a complete solution claim for
[AIM 632 at the original source revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/632-costas-polynomial.md).
The claim is submitted for independent mathematical review.

- [Complete paper](paper/costas-classification.pdf)
- [LaTeX source](paper/costas-classification.tex)

Theorem 1.1 states that, for every prime $`p`$, every $`r\ge2`$, and
$`K=\mathbb F_{p^r}`$, a function $`f:K\to K`$ fixing zero has all
differences $`f(dx)-f(x)`$, $`d\ne1`$, bijective if and only if
$`f(x)=L(x^s)`$, where $`s>0`$, $`\gcd(s,p^r-1)=1`$, and $`L`$ is an
invertible $`\mathbb F_p`$-linear map. The multiplier $`d=0`$ is included.
No shifting condition is assumed. Every function has a polynomial
representative, so the theorem covers the entire function class.

## Comparison with the original target

| Original requirement | Paper location | Coverage |
|---|---|---|
| Every prime and every extension degree $`r\ge2`$ | Theorem 1.1; final proof in Section 4 | Full |
| Arbitrary $`f:K\to K`$, with $`f(0)=0`$ | Introduction and equation (2.1) | Identical function class and normalization |
| Bijective differences for every $`d\ne1`$, including zero | Equation (2.1); scalar balance; final converse | Full multiplier set |
| No stronger shifting assumption | Theorem 1.1 and Introduction | None added |
| Positive unit exponent and invertible prime-field-linear output map | Theorem 1.1; Proposition 3.4; closing proof | Exact conclusion |
| Characteristic two and all odd-characteristic cases | Proposition 3.7, Corollary 4.2, Proposition 4.5 | Exhaustive case split, including $`r=2`$ |

## Argument and sources

Scalar trace components give difference sets and Frobenius multipliers.
Their parameter count yields two rank inequalities for the coefficients on
Frobenius orbits. These force a full-rank orbit and a normalization.
Ball's direction theorem removes the remaining binomial case; a three-root
character estimate forces rigidity on the remaining multiplicative cosets.
The argument is mathematical and uses no finite search or numerical
certificate as a premise.

The established external results are credited precisely in the paper:

| Imported result | Source location | Use |
|---|---|---|
| Prime-field homogeneity and relative difference sets | Pott--Wang, arXiv:1309.7842v1, Theorem 5.4 and Corollary 5.5, with Remark 3.2 normalization | Section 2.1 |
| Sufficient cyclic multiplier theorem | Hall's theorem as stated in Turyn (1964), p. 386 | Section 2.2 |
| Relative multiplier lifting | Pott--Reuschling--Schmidt (1997), Result 2 | Section 2.2, with the specialized parameters displayed |
| Directions and graph linearity | Ball, author version of 15 September 2003, Theorem 1.1 | Lemma 4.1 |
| Weil character bound | Akbary--Ghioca--Wang, Theorem 2.1 in the linked author version | Lemma 4.4 |

The 2015 paper of Muratović-Ribić, Pott, Thomson, and Qiang Wang gives
the construction and extension-field conjecture. Torres--Rubio proves the
stronger shifting case. The June 2026 preprint of Muratović-Ribić and
Balašev-Samarski discusses the orthomorphism formulation and retains the
general conjecture. Full primary references and links are in the manuscript.

## Review status

OpenAI Codex assisted in proof development and manuscript drafting. The
complete argument and its cited theorem applications underwent automated
natural-language logical and source checking. Separate fresh-context Codex
passes then read the same frozen draft as a reader and as a skeptical referee.
The manuscript was revised once to clarify local notation and correct
bibliographic metadata and source-version labels. Its final references,
target coverage, build, links and PDF were checked after that revision.

These are AI reviews. No separate detailed AI report is submitted;
independent mathematical review is requested. Human referee review, Lean
verification and upstream acceptance are not claimed.

## Building the paper

With a standard TeX Live installation providing `latexmk`, run from this
package directory:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/costas-classification.tex
~~~

The rebuilt file is `build/costas-classification.pdf`. The checked delivery
PDF is also included under `paper/`. There are no external assets, numerical
dependencies, or proof-critical computations to reproduce.
