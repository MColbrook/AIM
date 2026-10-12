# Correspondence with AIM Problem 046

Reviewed target: [046 — Calderón uniqueness for bounded measurable conductivities](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/046-rough-conductivity-calderon.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`, checked October 12, 2026.

The target asks whether, on every bounded connected smooth domain in three dimensions, two real scalar uniformly positive bounded measurable conductivities with equal complete weak Dirichlet-to-Neumann maps must coincide almost everywhere. It expressly permits a counterexample.

The [note](paper/calderon_measurable_note.pdf), Theorem 1, states the counterexample on the smooth ball Ω = B(0,3). The theorem and construction are attributed to the public OpenAI preprint, September 23, 2026, Theorem 1.1, p. 1. One admissible pair on one admissible domain refutes the universal assertion; a construction on every domain is not required for this alternative.

| Original requirement | Manuscript location and result | Scope |
| --- | --- | --- |
| Bounded connected domain with smooth boundary in R³ | Theorem 1 uses the ball B(0,3); Section 2 places all blocks strictly inside it. | Admissible domain for a counterexample. |
| Real scalar γ ∈ L∞, uniformly positive with finite upper bound | Section 2, equation (3), constructs one measurable scalar with depth-independent bounds c₀,C₀. Section 4 sets γ₀ = γ and γ₁ = (1 + δw)²γ, with common bounds c₀/4 and 9C₀/4. | Same coefficient class. No tensor is the final conductivity. |
| No continuity, derivative or known-partition condition | The countable measurable pasting in Section 2 imposes no such restriction. Imported scalarization preserves fixed positive finite bounds. | No added restriction on the target assertion. |
| Complete weak boundary data on H¹ᐟ²(∂Ω), with dual H⁻¹ᐟ²(∂Ω) | Equation (1) uses the same energy pairing. Section 4 proves equality for every smooth boundary voltage against every H¹ᐟ² test trace, then extends by density and boundedness to the entire input space. | Exact full operator equality, without restricting the measurements to constant voltages or finite data. |
| Failure of almost everywhere equality | Section 3 constructs w with ∫γ∇w·∇η = 1, hence w is nonzero on a set of positive volume. Section 4 chooses nonzero δ with positive 1 + δw, so γ₀ and γ₁ differ on a set of positive volume. | Exact analytic failure of the proposed conclusion. |
| Constants and all depths | The same scalar block is scaled at every depth. Current normalization is shown before equation (5), and the geometric series after equation (7) converge because 2s = 1.14 > 1. | Fixed finite ellipticity and a justified infinite construction. |
| Public imported theorem | Proposition 2 restates [OpenAI Proposition 4.1, p. 16, proof pp. 16–25](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf). Its collar geometry and probability-measure normalization are checked in Section 2. The construction uses its whole conormal functional for separately constant block voltages. | An explicitly imported scalar branching result; its proof is in the cited public manuscript, not reproduced in this note. |
| Relation to known Lipschitz results | Section 1 cites Caro–García-Ferrero–Rogers, arXiv:2401.06120v1, Introduction, for the Lipschitz case. | The rough example does not contradict uniqueness under that regularity assumption. |

Both coefficients additionally equal one near the outer boundary. This is a property of the example and is not an assumption narrowing the universal statement.

This is a literature update with a source-attributed expository note. No new-construction priority, independent human certification, local Lean verification or maintainer acceptance is claimed. The claim depends on the exact public scalar branching proposition above. Independent assessment of the complete original proof is welcome.
