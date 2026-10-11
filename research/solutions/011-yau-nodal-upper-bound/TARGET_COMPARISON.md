# Correspondence with AIM Problem 011

Target: [011. Yau's sharp upper bound for nodal volume](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/011-yau-nodal-upper-bound.md),
revision c9929805cece044705abaaebe1cebddac1ba11a6.

Manuscript: *A fixed smooth metric violating Yau's nodal upper bound:
An exposition of OpenAI's construction*, by Kaiwen Jin.
The construction is due to [OpenAI's preprint](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026),
Theorem 1.1, at revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb.
The [original PDF](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf)
contains the primary statement and proof.

The target asks for a constant $`C(M,g)`$ bounding the intrinsic nodal
$`(d-1)`$-measure by $`C(M,g)\sqrt\lambda`$, uniformly over every
nonzero real eigenfunction on every closed connected smooth
Riemannian manifold of dimension $`d\ge2`$.
The submitted alternative is a counterexample to this universal assertion.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Closed, connected, smooth Riemannian manifold, $`d\ge2`$ | Theorem 1.1; Section 6 constructs a smooth positive metric on $`S^4\times S^1`$ | One admissible example with $`d=5`$ negates the universal target |
| One metric for all eigenfunctions in the estimate | Section 6.2, summable changes in every finite derivative norm and the persistence budgets (6.3) | The final metric is fixed for the entire sequence |
| Nonzero real **exact** eigenfunctions, $`\lambda>0`$ | Lemmas 5.3–5.4; Lemma 6.1; equations (6.5)–(6.6) | Exact eigenfunctions of the limiting ordinary Laplacian; no quasimode substitution |
| Uniformity over all eigenvalues and eigenfunctions | Theorem 1.1 and the final ratio estimate in Section 6 | A sequence with $`\lambda_j\to\infty`$ makes the uniform constant impossible |
| Intrinsic Hausdorff measure for the same metric | Section 6, equations (6.7)–(6.8), using uniformly Lipschitz projections of strict sign cylinders | The lower bound is intrinsic $`\mathcal H_g^4`$; no assumed nodal regularity |
| No real analyticity hypothesis | Section 6 produces a smooth limit of positive coefficients and realizes it by a warped circle | The example lies in the stated smooth class |

The common gain exponent is established in Proposition 3.1 before arbitrary
finite residual accuracies are chosen. Proposition 2.2 gives a certificate
constant before its universal large-frequency quantifier. Section 6 then
chooses each frequency before its own persistence radius. These orders of
choice permit the power gain to survive on a single smooth metric.

The standard analytic dependencies used in the manuscript are:

| Public source | Exact locator and use | Applicability |
| --- | --- | --- |
| [Aronszajn (1957)](https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf) | pp. 235–236, unique continuation; Lemma 5.4 | Smooth elliptic coefficients satisfy the source's local regularity and boundedness assumptions; connectedness extends open-set vanishing |
| [Hunter, *Notes on Partial Differential Equations*](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), revised June 18, 2014 | Theorem 3.49, p. 76; Lemma 5.2 and Lemma 6.1 | Sobolev embedding and compactness in four-dimensional smooth charts, transferred through a finite atlas |
| Hunter, same notes | Theorems 4.27–4.28, pp. 112–114; Lemma 6.1 | Interior divergence-form regularity for smooth positive coefficients; no boundary condition is imported to the closed manifold |
| [Laugesen, arXiv:1203.2344v1](https://arxiv.org/pdf/1203.2344) | Theorem 4.1, pp. 28–32; Lemma 6.1 | Dense compact inclusion $`H^1\hookrightarrow L^2(\rho\,d\mu)`$ and a symmetric coercive shifted form |

The Laugesen identifier was submitted in 2012; the consulted PDF's title page
is dated November 27, 2024. The manuscript records both.
All construction-specific arguments are attributed to OpenAI.
This package proposes a literature update for maintainer review and leaves
catalogue classification to that review.
