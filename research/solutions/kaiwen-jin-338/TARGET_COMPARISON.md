# Target comparison for AIM 338

Target: [338 — Decidability of local asymptotic stability for polynomial ODEs](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/338-polynomial-local-stability-decidability.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted note: *Local asymptotic stability of rational polynomial ODEs is undecidable*, Kaiwen Jin, October 12, 2026. [PDF](paper/aim338.pdf); [source](paper/aim338.tex).

| Original requirement | Result and location in the note | Coverage |
| --- | --- | --- |
| Positive dimension; finite monomial lists with exactly encoded rational coefficients and nonnegative integer exponents; `f(0)=0` | Section 1 defines this input; Section 3 gives exact source-code validation and monomial conversion | Same input convention; no approximation |
| Arbitrary dimension and degree; no homogeneity or linearization promise | Corollary 3 rules out a decider for the unrestricted class by restricting it to the homogeneous subclass of Theorem 1 | Full nonexistence claim for the unrestricted class |
| Real autonomous continuous-time polynomial ODE, unique maximal classical solutions, Euclidean norm | Section 1 states these conventions; Lemma 2 uses the same solutions and norm | Same model |
| For every positive epsilon, some positive delta guarantees all-time existence and a strict epsilon bound for every initial state of norm less than delta | Section 1, condition (i); Lemma 2 retains this stability clause | Exact stability and existence quantifiers |
| Some positive radius gives all-time existence and convergence to zero for every initial state within the radius | Section 1, condition (ii); Lemma 2 proves the corresponding global condition for homogeneous fields | Exact local attraction clause |
| Global existence for distant initial states is not assumed | Lemma 2 constructs a global solution from a nearby solution by positive amplitude and time scaling, then identifies it with the maximal solution | No added global-completeness premise |
| Stable but nonattracting equilibria must receive a negative answer | Section 1 states this distinction; the decision predicate is the conjunction (i) and (ii) | Preserved |
| Algorithm must halt on every valid finite input, with no running-time bound | Corollary 3 and its proof construct a total homogeneous GAS decider from any alleged total LAS decider; invalid source codes are negative | Exact total-decision target |
| Public imported theorem matches the input class and solution convention | Theorem 1 cites Shevchenko–Liu–Liu, arXiv:2610.12434v1, Theorem 1.5, PDF p. 4; source definitions in Section 1.1, pp. 2–3; proof in Section 15, pp. 44–45 | Exact rational homogeneous continuous-time theorem, retained as a cited preprint dependency |
| Permitted answer: total decidability or undecidability | Corollary 3 proves nonexistence of the requested total algorithm via many-one completeness and the halting contradiction | Negative answer to the full stated question |

The construction establishing the external undecidability theorem belongs to the cited authors. This submission is an attributed literature update with the complete internal scaling and encoding reduction. It supplies no new independent proof or formal verification of that preprint's construction. Independent mathematical and repository review is requested.
