# Comparison with AIM Question 468

The target is [Instantaneous spreading for fractional-pressure flow in several dimensions](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/468-fractional-pressure-multidimensional-instantaneous-spread.md), fixed at commit `b2ec0fac559f532fc0ed04fce81deea0ce07c68b`. The problem statement is preserved in the catalogue page; only its status and evidence are updated.

The proposed answer is a counterexample to the universal assertion, rather than a classification of all fixed parameter triples. Theorem 1.2 gives one `N=3`, `m=3/2`, and `s=1-alpha/2` with `0<alpha<1/4`.

| Target requirement | Manuscript evidence |
| --- | --- |
| Whole-space equation and inverse pressure with multiplier `|xi|^(-2s)` | Definition 1.1, equations (1.1)-(1.3), and the normalized Riesz kernel calculation (2.2)-(2.6). Here `K_alpha=(-Delta)^(-1+alpha/2)=(-Delta)^(-s)`. |
| Nonzero nonnegative compact datum in `L1` and `L-infinity` | The explicit radial datum (2.1), with supremum 100, an inner jump from 1 to 100, and an outer jump from `1/16` to vacuum. Section 2.1 proves its fractional regularity. |
| Global nonnegative distributional solution with the prescribed initial trace | Section 2.5 passes the viscous construction to a whole-space weak solution; Proposition 5.1 and the proof of Theorem 1.2 extend and concatenate it globally. |
| Continuity into weak `L1`, against every bounded spatial test | Equation (2.38) on the compact-support interval. Section 5 proves global tightness using (5.1)-(5.2), then continuity of every bounded-test pairing, including the junction and initial time. |
| Conserved mass and initial supremum bound at every time | Equations (2.21), (2.38), Lemma 2.1, and the representative argument and concatenation in Section 5. |
| Locally integrable nonlinear flux | Uniform field convergence (2.39), strong density convergence, and the whole-space flux bound (5.1) for the continuation. |
| Pressure energy inequality from time zero | Equation (2.42); Section 5 adds the two segment inequalities, cancelling the common endpoint energy. |
| Every real `q>1` power inequality with the target coefficient and differentiating order | Equations (4.11)-(4.12), the dense-exponent and every-terminal-time passages, and Section 5. Since `m=1+a`, the coefficient is exactly `4q(q-1)/(m+q-1)^2`; the differentiating exponent `(1-s)/2` equals `alpha/4`. One state-resolved measure and one initial interval serve all powers. |
| Failure of positive exterior mass for every finite radius and positive time | On `0<t<T_*`, Theorem 1.2 gives `u(t)=0` outside the finite `C1` radius `R(t)`. At `t=T_*/2`, choose that finite radius: the exterior integral is zero. This negates the universal assertion. |

The solution is radial on the initial compact-support interval. No radiality or compact-support assertion is made for its global continuation. The energies are required from the original initial time; the target does not add local entropy admissibility, inequalities on arbitrary time subintervals, or a prescribed whole-space approximation selection. The proof works within that stated class and does not assert the same behavior for a stricter class.

Theorem 1.2 is the proposed complete result. Independent mathematical review remains outstanding; the public status is **Solution claimed**.
