# 872. Is the algebraic Hilbert number exactly the Harnack-type expression?

**Area:** Inverse problems, control and dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`d\ge 2`$, let $`H_a(d)`$ be the supremum, over real planar polynomial vector fields
```math
\dot x=P(x,y),\qquad \dot y=Q(x,y),\qquad \max(\deg P,\deg Q)\le d,
```

of the number of *algebraic limit cycles*: isolated periodic orbits contained in the zero set of a nonzero real polynomial. Is
```math
H_a(d)=1+\frac{(d-1)(d-2)}2\qquad\text{for every }d\ge2?
```

The equality asserts both a coefficient-independent upper bound and its attainment. The invariant algebraic curves are **not** assumed smooth, nodal, generic, or of bounded degree.

## Application

The count measures how complicated the algebraically visible oscillations of a polynomial dynamical system can be at a fixed vector-field degree. It is a sharp, restricted version of the limit-cycle counting question in Hilbert's sixteenth problem. A resolution would in particular settle the still-open quadratic algebraic case $`H_a(2)=1`$, while leaving the broader count of nonalgebraic limit cycles as a different question.

## References

1. J. Llibre, R. Ramírez and N. Sadovskaia, [*On the 16th Hilbert problem for algebraic limit cycles*](https://doi.org/10.1016/j.jde.2009.11.023), *Journal of Differential Equations* **248** (2010), 1401–1409. The generic invariant-curve theorem and source of the full conjecture.
2. J. Llibre, R. Ramírez and N. Sadovskaia, [*On the 16th Hilbert problem for limit cycles on nonsingular algebraic curves*](https://doi.org/10.1016/j.jde.2010.06.009), *Journal of Differential Equations* **250** (2011), 983–999, [author preprint](https://ddd.uab.cat/pub/artpub/2011/gsduab_2789/joudifequ_a2011v250p983preprint.pdf), printed p. 2, Conjecture 2 and Theorem 1. The same authors state the unrestricted conjecture and distinguish it from their results under hypotheses on invariant curves.
3. J. Llibre and X. Zhang, [*A survey on algebraic and explicit non-algebraic limit cycles in planar differential systems*](https://doi.org/10.1016/j.exmath.2020.03.001), *Expositiones Mathematicae* **39** (2021), 48–61, [author preprint](https://ddd.uab.cat/pub/artpub/2021/239786/LliZha2019c.pdf), §2.3, Open problems 1–3. The full formula remains an explicit open problem; the survey records the nodal-case theorem and the quadratic and cubic subquestions.

## Status review


**Known cases:** The generic or nodal invariant-curve theorems do not establish the unrestricted algebraic Hilbert number. The Prove2Me listing presents the exact formula as a goal, not an independently checked solution. The older Winkel counterexample concerns a different conjecture.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The generic or nodal invariant-curve theorems do not establish the unrestricted algebraic Hilbert number. The Prove2Me listing presents the exact formula as a goal, not an independently checked solution. The older Winkel counterexample concerns a different conjecture.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2010 generic result gives the displayed bound for even $`d`$, and one less for odd $`d`$, when *all* irreducible invariant algebraic curves meet the genericity assumptions. Zhang's nodal-curve theorem also concerns a restricted class. These theorems do not cover arbitrary invariant curves. The 2021 author survey continues to list the unrestricted formula as Open problem 3. A bounded literature and announcement check on 21 October 2026 found no complete matching resolution. The older paper titled “Counterexample to a conjecture on the algebraic limit cycles of polynomial vector fields” disproves Winkel's different 2000 conjecture about the minimum vector-field degree for given ovals, not this 2010 formula.

The discovery cue was a [Prove2Me listing](https://prove2.me/?status=all&page=96). Its listed formalization targets were not treated as verified Lean proofs. The [body and status audit](../FURTHER_problems/_tracking/prove2-llibre-algebraic-hilbert-body-and-status-2026-10-21.json) and [semantic comparison](../FURTHER_problems/_tracking/prove2-llibre-algebraic-hilbert-duplicate-2026-10-21.json) record the checks and their limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-67bda3e4afc372e4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
