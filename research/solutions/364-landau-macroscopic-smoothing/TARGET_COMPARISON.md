# Comparison with Problem 364

Original target: [Landau–Coulomb smoothing controlled only by macroscopic quantities](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/364-landau-macroscopic-smoothing.md), repository revision `b2ec0fac559f532fc0ed04fce81deea0ce07c68b`.

Submitted paper: Kaiwen Jin, *Macroscopic L∞ bounds for the Landau–Coulomb equation*, [manuscript](paper/main.pdf). This is a complete solution claim awaiting independent mathematical assessment.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| Spatially homogeneous three-dimensional Coulomb equation, with A=(8π)⁻¹(Π/|·|)∗f and a=(4π|·|)⁻¹∗f | Equations (1.1)–(1.2) use exactly these coefficients. The kernel identities at the end of Section 1 give the equivalent nondivergence equation. | Same equation and normalization. |
| Every nonnegative smooth rapidly decaying solution on [0,T]×R³ | Theorem 1.1. Section 2.4 treats vacuum initial profiles by normalized positive approximations, identifies their limit with the given nonlinear solution, and transfers the weighted estimate. | Full stated solution class; no added Gaussian-tail hypothesis. |
| Mass one, mean zero and energy three | Equation (1.3), conservation in Section 1, and the entropy core in Section 2.3. | Exact normalization. |
| Every H∈R and every 0<τ<T, assuming initial entropy≤H | Theorem 1.1; Proposition 2.1; Sections 4.1–4.3. Thresholds and constants depend only on the permitted data. | Same parameter ranges and quantifiers. |
| Bound independent of every initial higher moment, Fisher information, pointwise bound and derivative norm | Theorem 1.1. The positive-time estimate in Proposition 2.1 has only entropy dependence. Section 2.4 uses individual-datum auxiliary bounds solely to identify the approximation limit, then discards them. Sections 3–4 retain only macroscopic constants and waiting times. | Full required uniformity. |
| Global velocity L∞ bound on the entire closed waiting interval [τ,T] | Section 4.2, equation (4.10), controls every sufficiently large velocity after τ/2. Section 4.3 bounds the remaining ball and includes endpoints by continuity. | Entire velocity space and closed time interval. |
| A finite bound without a prescribed sharp time exponent | Equation (1.4) and the last proof. The Introduction explicitly leaves the separate conjectural 1/t rate unclaimed. | Exact requested conclusion. |

## Public analytic inputs

The manuscript contains the weighted metric calculations, tangential kernel/Nash proof, arbitrary-length cutoff entropy estimate, spatial and level iterations, full-matrix core geometry, velocity scaling, and bounded-region iteration. Its specialized imported results have the following roles.

| Public source | Manuscript use and applicability |
| --- | --- |
| Guillen–Silvestre, [arXiv:2311.09420v2](https://arxiv.org/abs/2311.09420v2), Lemma 9.1 | The even spherical inequality is stated as (2.7), with even product slices and the exact doubled-variable factor. |
| Guillen–Silvestre, Theorems 1.1, 1.2, 2.3, 2.4 and Appendix B | Section 2.4 uses nonlinear Gaussian-data existence, ordinary Fisher monotonicity, moment and Gaussian/derivative bounds only for individual-datum approximation identification and justified integrations. The source time is κ₀t. |
| Silvestre, [arXiv:1511.03248v3](https://arxiv.org/abs/1511.03248v3), Theorem 2.1 | Section 2.4 applies the general parabolic estimate with d=3, p=2, α=1, β=0 and κ=9, after checking determinant, matrix and weighted L² bounds. No soft-potential corollary is applied at the Coulomb endpoint. |
| Fournier, [arXiv:0909.0647](https://arxiv.org/abs/0909.0647), Theorem 2(ii) | Section 2.4 checks the probability/second-moment class, initial W₂ convergence and uniform time-integrable auxiliary suprema. It displays the source generator and the time change 2κ₀t before (2.16). |
| Golse–Imbert–Ji–Vasseur, [arXiv:2206.05155v3](https://arxiv.org/abs/2206.05155v3), equations (3.29)–(3.34) | Credited for the pre-coercivity entropy calculation. Lemma 3.3 reproduces the smooth calculation at the cutoff lengths used here. The published small-radius weak-solution lemma is not extended by citation. |

Golding–Gualdani–Loher’s [2025 paper](https://doi.org/10.1007/s00205-025-02107-x), Section 1, first open problem, supplies the background macroscopic question. Ji’s and Desvillettes–Golding–Gualdani–Loher’s Fisher production estimates are discussed as prior results with stronger moment dependence, not as proofs of the target. The separate sharp-rate question and rough-data global existence are outside this submission’s claim.
