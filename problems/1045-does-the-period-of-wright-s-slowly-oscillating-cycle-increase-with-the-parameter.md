# 1045. Does the period of Wright's slowly oscillating cycle increase with the parameter?

**Area:** Delay differential equations and population dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`\alpha>\pi/2`$, consider Wright's equation with delay one,
```math
y'(t)=-\alpha y(t-1)\bigl(1+y(t)\bigr).
```

Let $`y_\alpha:\mathbb R\to(-1,\infty)`$ be its nonconstant slowly oscillating periodic solution, unique up to time translation [1, Theorem 1.1]. Write $`L(\alpha)`$ for its least positive period. After a phase shift, slow oscillation means that some $`q>1`$ satisfies $`L(\alpha)-q>1`$, with
```math
y_\alpha(0)=y_\alpha(q)=0,\qquad
y_\alpha(t)>0\ (0<t<q),\qquad
y_\alpha(t)<0\ (q<t<L(\alpha)).
```

**Prove or disprove that**
```math
\pi/2<\alpha_1<\alpha_2
\quad\Longrightarrow\quad
L(\alpha_1)<L(\alpha_2).
```


This is Conjecture 7.1 of [1]. Its subsequent discussion explicitly uses the strict comparison above. The question concerns period values; it does not assert that $`L'(\alpha)>0`$ everywhere.

## Application

The equation models population growth with delayed density feedback. The question asks how the duration of sustained oscillations changes with feedback strength when the delay is fixed.

## Status review


**Known cases:** Strict monotonicity of the least period over every alpha>pi/2 is required. Uniqueness of the slowly oscillating orbit, near-Hopf monotonicity and asymptotic period estimates do not establish it globally.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Strict monotonicity of the least period over every alpha>pi/2 is required. Uniqueness of the slowly oscillating orbit, near-Hopf monotonicity and asymptotic period estimates do not establish it globally.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Monotonicity is proved for $`\pi/2<\alpha\le\pi/2+0.006830`$. Balázs and Röst restate the global question as Conjecture 13; their Theorem 14 also treats small intervals on higher Hopf branches [2, §4.1]. Those higher branches concern rapidly oscillating solutions and do not extend the parameter range for the cycle defined here.

The uniqueness theorem for this cycle [1] leaves its period dependence undetermined. Numerical evidence and large-parameter estimates are also distinguished from a monotonicity proof in [1, §7].

Current searches covered the equation, period monotonicity and period-function terminology, the conjecture numbers, author publications, proof/counterexample claims and announcements. No matching complete result was found. This is a dated literature review, not a guarantee that no proof exists.

All 953 recorded findings and 587 saved pages were checked alongside the current all-status AIM/OpenAI comparison snapshot. AIM 322 asks about attraction to equilibrium in a locally stable parameter range for a class of feedback functions. AIM 285 concerns Nicholson's different equation. Neither asks the supercritical cycle-period question above. The evidence and access qualifications are retained in the [review record](../FURTHER_problems/_tracking/Wright-period-monotonicity-Root-20261027/ROOT-FORMULATION-CURRENT-AND-SEMANTIC-DUPLICATE-PASS.json).

## References

1. Jonathan Jaquette, *A proof of Jones' conjecture*, **Journal of Differential Equations 266** (2019), 3818–3859, [DOI 10.1016/j.jde.2018.09.017](https://doi.org/10.1016/j.jde.2018.09.017). Checked source: [arXiv:1801.09806v1](https://arxiv.org/html/1801.09806), Eq. (2), Theorem 1.1 and §7, Conjecture 7.1; [author PDF](https://sites.math.rutgers.edu/~jaquette/JonesPreprint.pdf), pp. 2 and 37–38. The arXiv record lists only v1. The published HTML retains the same conjecture; full PDF parity was not certified.
2. István Balázs and Gergely Röst, *Hopf bifurcation for Wright-type delay differential equations: The simplest formula, period estimates, and the absence of folds*, **Communications in Nonlinear Science and Numerical Simulation 84** (2020), 105188, [DOI 10.1016/j.cnsns.2020.105188](https://doi.org/10.1016/j.cnsns.2020.105188); [accepted manuscript](https://publicatio.bibl.u-szeged.hu/18524/3/31123767.pdf), §4.1, Conjecture 13 and Theorem 14.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2321ce8a88ccd56a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
