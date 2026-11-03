# 1066. Can a smooth boundary wavemaker extinguish every compactly supported KdV wave on the half-line?

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`y_0\in C_c^\infty(0,\infty)`$. For $`T>0`$ and a boundary control $`h\in C_c^\infty(0,T)`$, let $`y`$ be the smooth solution of

```math
\begin{cases}
y_t+y_{xxx}+y_x+y\,y_x=0, & 0<t<T,\quad x>0,\\
y(t,0)=h(t), & 0<t<T,\\
y(0,x)=y_0(x), & x>0.
\end{cases}
```


Does there exist $`T_0=T_0(y_0)`$ such that, for every $`T\ge T_0`$, some such control satisfies $`y(T,x)=0`$ for all $`x>0`$? Equivalently, is zero reachable for at least one sufficiently large $`T`$? Once a wave is extinguished, the zero solution and zero control extend it to all later times. This is Rosier's exact reachable-set question [1, Problem 7.4], with both the initial wave and the control **smooth and compactly supported**.

## Application

The boundary value represents a wavemaker at one end of a long canal. An affirmative answer would show that waves generated at that boundary can exactly cancel any initially localized wave, despite the canal's unbounded extent. A negative answer would identify an obstruction to exact control in this model.

## References

1. L. Rosier, *Control of the KdV equation*, Problem 7.4 in V. D. Blondel and A. Megretski (eds.), *Unsolved Problems in Mathematical Systems and Control Theory*, Princeton University Press, 2004, pp. 260–264, [academic-hosted full text](https://dcn.nat.fau.eu/wp-content/uploads/UnsolvedProblems_-BlondelMegretski_2004.pdf), PDF pp. 276–277 for the model and explicit question; [chapter DOI](https://doi.org/10.1515/9781400826155.260).
2. L. Rosier, [*Exact boundary controllability for the linear Korteweg–de Vries equation on the half-line*](https://doi.org/10.1137/S0363012999353229), *SIAM Journal on Control and Optimization* **39** (2000), 331–351. The result changes the equation and permits a weaker solution framework.
3. L. Rosier, [*Control of the surface of a fluid by a wavemaker*](https://www.numdam.org/article/COCV_2004__10_3_346_0.pdf), *ESAIM: Control, Optimisation and Calculus of Variations* **10** (2004), 346–380. Its null-control and noncontrol results concern a bounded interval with extra endpoint conditions.
4. R. de A. Capistrano-Filho and F. Gallego, [*Another look at the control properties of the Korteweg-de Vries equation*](https://arxiv.org/pdf/2409.15571v2), May 2026 revision, Theorem 1.1 and Remark 5; [journal DOI](https://doi.org/10.1016/j.bulsci.2026.103909). Its right-half-line nonlinear result is local for small data and an admissible final-state class, with $`H^{1/3}`$ boundary controls.

## Status review


**Known cases:** All compactly supported smooth data must be extinguished with compactly supported smooth control. The May 2026 right-half-line result assumes small data and weaker Sobolev boundary controls; finite-interval and linear results do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

All compactly supported smooth data must be extinguished with compactly supported smooth control. The May 2026 right-half-line result assumes small data and weaker Sobolev boundary controls; finite-interval and linear results do not cover it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The later results checked do not establish this exact all-data, smooth-control, right-half-line claim. A [bounded status and duplicate audit](../FURTHER_problems/_tracking/d007-rosier-halfline-kdv-smooth-null-control-status-2026-10-22.json) through 22 October 2026 found no matching complete result or announced solution. The audit also distinguishes this target from other KdV control questions already in AIM.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f8514d4e5b4613bc**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
