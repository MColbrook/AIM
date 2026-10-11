# Exact comparison with AIM 450

The comparison uses the finished note and the
[original problem at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/450-stein-lipschitz-direction-hilbert-bound.md).
The note's imported estimate is
[OpenAI, Theorem 1.1, PDF page 3, fixed revision
adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf).

| Original requirement | Location in the finished note | Coverage |
| --- | --- | --- |
| Globally defined unit field from the plane to the unit circle | Definition before Theorem 1; Theorem 1 and Corollary 2 | Same domain and unit normalization |
| `|v(x)-v(y)| <= |x-y|` for every pair of planar points | Theorem 1 and Corollary 2 | Same global 1-Lipschitz hypothesis; constant fields included |
| Fields may depend on both spatial coordinates | Paragraph after Theorem 1 and final scope paragraph | No one-coordinate restriction |
| Every Schwartz function | Operator definition and both result statements | Every complex Schwartz input; no frequency restriction |
| Straight-line samples `f(x-t v(x))` | Equation (1), Corollary 2, equation (3) | Direction is fixed at the output point; not a flow equation |
| Symmetric principal value with outer cutoff `1/K` | Corollary 2, equations (3) and (5), first proof paragraph | Existence at every output point by symmetric cancellation and dominated convergence |
| Absolute `K >= 1` and finite `C`, chosen before all data | Corollary 2 and final sentence of its proof | `K = 1/a_* > 2`, `C = C_*^2`; independent of the field, input and level |
| Every positive level `lambda` and the stated weak bound | Corollary 2, equation (4), final proof display | Exactly the requested level-set inequality |
| Public theorem used for the uniform estimate | Theorem 1, attributed to OpenAI's Theorem 1.1 | All hypotheses, operator normalization and truncation ranges match |

The imported theorem provides absolute `0 < a_* < 1/2` and finite `C_*`
with a uniform bound on the norm of each inner truncation. Its supremum is
outside the norm. The note first proves pointwise principal-value convergence
using smoothness of the input. Continuity of each truncation makes the limit
measurable. Fatou's lemma along `epsilon_n = a_*/(n+2)` gives the same strong
bound for the limit, and Chebyshev's inequality gives equation (4).

The source itself already records the principal-value and weak-type
consequences. The note is an attributed explanation and correspondence, not
a new proof of the uniform estimate. The full target follows from that
public theorem; no additional field regularity, geometric restriction or
frequency assumption is introduced. Neither a maximal-truncation estimate
nor a bound for arbitrary outer lengths is asserted. Independent review of
the complete original proof remains requested.
