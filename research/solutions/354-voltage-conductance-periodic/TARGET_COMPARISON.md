# Correspondence with AIM problem 354

The comparison is against
[the original problem at commit b2ec0fac559f532fc0ed04fce81deea0ce07c68b](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/354-voltage-conductance-periodic.md).
The manuscript claims a complete affirmative answer to its existential
question. The table identifies its supporting locations; it is not an
independent proof certificate.

| Original requirement | Manuscript location and result | Scope |
|---|---|---|
| Some positive physical parameters with $v_E>v_F>0$ | Theorem 1.1 fixes $v_E=2$, $v_F=1$, $y_L=1$. Equation (5.9) reconstructs positive $y_*,a_*,c$. | A subfamily inside the original existential quantifiers. |
| Full voltage and conductance density | Equations (1.1)–(1.3), response (5.5), and final proof in Section 5.3. | The full half-strip equation with positive conductance diffusion. |
| Drift and diffusion feedback | Equation (4.20) retains both linear feedback terms; (5.5) retains the nonlinear terms. Substitution after (5.9) gives the original coefficients. | Neither feedback term is dropped. |
| Nonnegative mass-one periodic density | Section 5.3 identifies the response with a positive prescribed period-map fixed point. | Mass and nonnegativity hold for the continuous time representative. |
| Positive period and nonconstant actual firing rate | Lemma 5.2 selects $T$; Proposition 5.4 gives a nonzero first rate coefficient. Equation (5.6) equates the rate with the outgoing flux. | No externally prescribed drive. |
| Low-conductance zero traces and high-conductance flux reset | Equations (1.3), (2.2), and the completed weak construction, collected at the end of Section 5.3. | Kinetic traces; no value assigned at the single grazing conductance. |
| Zero conductance flux at zero and infinity | Equation (2.10) retains the natural floor input; Appendix A.2 constructs reflection. The final paragraph of Section 5.3 verifies the nonlinear floor and tail traces. | Distributional conormal traces for the requested distributional solution. |
| Time continuity into $L^1$ | Theorem 1.1 and final proof give time $H^1$ with an exponential weighted spatial $L^2$ norm. | Implies the requested continuity. |
| Entropy and uniform second conductance moment | Equation (1.4) and final proof in Section 5.3. | Uniform over one period. |
| All time harmonics controlled | Lemmas 5.2–5.3 exclude the other harmonics and control high frequencies. | Countable analytic selection; no uniform-in-harmonic noise expansion. |

The prescribed evolution and frozen stationary decay come from Fonte Sanchez
and Mischler, arXiv:2408.02471v1, Theorems 2.2 and 1.2. Process identification
uses Trevisan, arXiv:1507.01357v2, Theorem 2.5, together with Appendix A.
Hörmander's regularity theorem is used in the interior; the reflecting
boundary and bounded-clock estimates are constructed in the manuscript.
Their hypotheses are checked in the corresponding proofs.

The result concerns existence for selected parameters. Stability, explicit
numerical parameters, and a claim for every small diffusion are outside it.
