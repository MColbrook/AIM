# Comparison with AIM 030

Target: [SIC measurements in every finite dimension](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/030-sic-povms.md),
at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted note: *From arithmetic dilogarithms to SICs in every dimension*,
Kaiwen Jin, 12 October 2026. Locators refer to its seven-page PDF.

| Original requirement | Result and manuscript location | Scope |
| --- | --- | --- |
| Complex dimension `d`, every integer `d >= 2` | Theorem 1, p1; arithmetic branch `d >= 4`, Sections 3--4; explicit `d=2,3`, pp6--7 | Full integer range |
| Exactly `d^2` vectors in `C^d` | Section 4, p6: one displacement for each class in `(Z/dZ)^2`; pp6--7: four and nine explicit exceptional witnesses | Exact count |
| Unit norm | Section 4, p6: a unit vector spanning the Hermitian projector's range and unitary displacement orbit; explicit low-dimensional norms | Exact |
| Every distinct squared inner product `1/(d+1)` | Equations (25)--(26), p6; Weyl multiplication gives all distinct vector pairs; pp6--7 verify the exceptional pairs | All pairs, exact |
| No covariance hypothesis | Theorem 1 and Section 1, pp1--2, retain the unrestricted conclusion. Section 4 exhibits a covariant family as sufficient witnesses | No added assumption |
| Complete proof rather than numerical agreement | Sections 2--4 give the arithmetic values, coordinate conversion, convolution calculation, algebraic conjugation, Hermitian projection and vector construction | No numerical premise |
| Imported algebraicity and nonzero values | RW26 v2, Theorems 1--2; Section 2, pp2--3, states the normalized arithmetic values and their domain | Applied to the explicit hyperbolic matrix and lattice |
| Imported twisted convolution | AFK26 v1, Theorem 1.2 and its proof pp7--8; Section 3, p5, uses the proved rank-one shift `lambda=0` | No conjecture about the whole shift set is invoked |
| Imported normalization and representatives | AFK25 v2, Lemma 1.42, Lemma 2.13, Theorem 5.8 and Equation (5.65); Section 3, pp4--5 | Includes even dimensions and both zero terms |
| Imported common algebraic conjugation | REC26 v1, Proposition 7; Proposition 2, p3, states one automorphism simultaneously for all nonzero values | Explicit hypotheses verified in Section 3 |

There is no remaining dimension or vector-pair class in the claimed result.
The conclusion depends on the cited primary arithmetic theorems, whose proofs
remain open to independent scrutiny. This note does not prove those source
theorems anew. The October reciprocity preprint already gives the universal
SIC consequence in Section 9.2; this submission supplies its detailed
coordinate and matrix deduction and reports the literature change.

The claim does not include classification of all SICs, higher-rank SICs, or
an effective automorphism-selection algorithm. Compilation, AI checking and
filing a pull request are not independent mathematical certification or
upstream acceptance.
