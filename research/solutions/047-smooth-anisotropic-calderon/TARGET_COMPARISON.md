# Correspondence with AIM 047

The comparison is with
[047 — Smooth anisotropic Calderón uniqueness](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/047-smooth-anisotropic-calderon.md)
at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
The submitted [manuscript](paper/manuscript.pdf) is an attributed exposition of
OpenAI's September 24, 2026 argument, rather than a claim of new priority.

| Original requirement | Manuscript location and asserted conclusion | Coverage |
| --- | --- | --- |
| Every compact connected smooth manifold with nonempty smooth boundary | Section 2 and Theorem 2.1, p. 3 | Full stated domain; no orientability assumption and no connected-boundary assumption |
| Every dimension `n >= 3` | Theorem 2.1, p. 3; final deduction, Section 10, p. 42 | All stated dimensions, without an upper bound |
| Arbitrary smooth positive Riemannian metrics inducing the same tangential boundary metric | Section 2 and Theorem 2.1, p. 3 | Smoothness and positive definiteness hold up to the boundary; no analyticity, smallness or geometric subclass is imposed |
| Exactly one full ordinary zero-frequency Dirichlet-to-Neumann map for each metric | Section 2, p. 3; Green identity and density comparison in Section 10, p. 42 | The common boundary metric gives the common boundary density; equality of ordinary maps yields equality of the energy forms without extra measurements |
| A smooth boundary-fixing diffeomorphism `F:M -> M` with `g1 = F* g2` | Theorem 2.1; Propositions 9.1–9.2, pp. 40–42; Section 10, p. 42 | Global diffeomorphism, smooth through the boundary, fixing every boundary point; the inverse corrects the pullback direction |
| Complete argument rather than a restricted case | Theorem 2.2 and Sections 3–9; Section 10 | The patch theorem is proved in the exposition; the full-data deduction uses the dense proper patch obtained by removing one boundary point |

The source result is OpenAI's
[Theorem 1.1 and Corollary 1.2](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf).
The manuscript reconstructs that argument; it does not take the uniqueness
theorem as an unexplained external premise. Sections 3–4 identify the classical
analytic inputs, and the bibliography links their primary sources.

This package presents an affirmative full-target argument for review. It
contains no counterexample. The original problem's classification remains a
maintainer decision; AI checks and artifact validation do not constitute
independent human acceptance.
