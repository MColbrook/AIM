# 731. Residual norm attainment and differentiability of the dual norm

**Area:** Banach space geometry and continuous optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,\|\cdot\|)`$ be an arbitrary real Banach space, let $`B_X`$ be its closed unit ball, and let $`\|\cdot\|_*`$ be the dual norm on $`X^*`$. Define
```math
\mathrm{NA}(X)=\{f\in X^*: f(x)=\|f\|_*\text{ for some }x\in B_X\}.
```

Suppose that $`\mathrm{NA}(X)`$ is residual in the norm topology of $`X^*`$: it contains a countable intersection of norm-open dense sets. Must $`\|\cdot\|_*`$ be Fréchet differentiable at every point of some norm-dense subset of $`X^*`$?

Here Fréchet differentiability at $`f`$ means that there is a bounded linear functional $`L_f\in X^{**}`$ such that
```math
\lim_{\|h\|_*\to0,\ h\ne0}
\frac{\big|\|f+h\|_*-\|f\|_*-L_f(h)\big|}{\|h\|_*}=0.
```

The question concerns the given norm; no separability or renormability hypothesis is imposed.

## Application

The dual norm is the optimal value of a linear functional over the unit ball. Its differentiability describes regularity of this support optimization problem. The question asks whether generic existence of maximizers already forces a dense set of such regular dual objectives.

## References

1. J. M. Borwein and W. B. Moors, *Non-smooth Analysis, Optimisation theory and Banach space theory*, chapter 50 in E. Pearl (ed.), *Open Problems in Topology II* (2007), Question 2.1, printed p. 548, global question 1128. [Book PDF](https://carmamaths.org/resources/jon/Preprints/Books/Open%20Probs%20in%20Top/open2.pdf#page=558).
2. A. J. Guirao, V. Montesinos and V. Zizler, *Remarks on the set of norm-attaining functionals and differentiability*, Studia Mathematica **241** (2018), 71–86. [Published article](https://doi.org/10.4064/sm8768-6-2017). The separable case is positive; Problem 3.7 asks about the LUR-renormable case.
3. W. B. Moors and N. Ö. Tan, *Dual differentiation spaces*, Bulletin of the Australian Mathematical Society **99** (2019), 467–472. [Published article](https://doi.org/10.1017/S0004972719000376); [author version](https://www.math.auckland.ac.nz/~moors/DualDifferentiationspaces.pdf). Theorem 3 proves the implication for dual differentiation spaces, including spaces admitting an equivalent locally uniformly rotund norm.
4. M. Jung, M. Martín and A. Rueda Zoca, *Residuality in the set of norm attaining operators between Banach spaces*, Journal of Functional Analysis **284** (2023), 109746. [Published article](https://doi.org/10.1016/j.jfa.2022.109746); [journal PDF hosted by an author](https://www.ugr.es/~mmartins/Curriculum/Papers/pre2022_Residuality_in_NA.pdf). Section 4 recalls the restricted scalar results; Theorem 4.1 imposes separability assumptions on the operator spaces' domain and range dual.

## Status review


**Known cases:** The residuality hypothesis is in the dual norm topology for the given arbitrary Banach norm. Ordinary Bishop-Phelps density, separable cases and operator results with additional Radon-Nikodym or differentiability assumptions do not settle the unrestricted implication.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The residuality hypothesis is in the dual norm topology for the given arbitrary Banach norm. Ordinary Bishop-Phelps density, separable cases and operator results with additional Radon-Nikodym or differentiability assumptions do not settle the unrestricted implication.

Additional comparison sources: [comparison source 1](https://carmamaths.org/resources/jon/Preprints/Books/Open%20Probs%20in%20Top/open2.pdf#page=558); [comparison source 2](https://doi.org/10.4064/sm8768-6-2017); [comparison source 3](https://doi.org/10.1017/S0004972719000376); [comparison source 4](https://www.math.auckland.ac.nz/~moors/DualDifferentiationspaces.pdf); [comparison source 5](https://doi.org/10.1016/j.jfa.2022.109746); [comparison source 6](https://www.ugr.es/~mmartins/Curriculum/Papers/pre2022_Residuality_in_NA.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Ordinary density of norm-attaining functionals follows from Bishop–Phelps; the hypothesis here is the stronger category condition. The positive results above cover substantial classes, including all separable spaces, but do not state the implication for arbitrary real Banach spaces. No matching general resolution or complete-resolution announcement was located in the bounded checks.

The [primary scope check](../FURTHER_problems/_tracking/bishop-phelps-residual-primary-review-2026-10-19.json), [current search](../FURTHER_problems/_tracking/bishop-phelps-residual-current-review-2026-10-19.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/borwein-moors-q21-independent-scope-audit-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/bishop-phelps-residual-duplicates-review-2026-10-19.json), [website comparison](../FURTHER_problems/_tracking/bishop-phelps-residual-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/bishop-phelps-residual-coordinator-review-2026-10-19.json) record checked extents and limitations. These are selected-statement and status checks, not verification of complete proofs or exhaustive certification of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8ee6d05d50adbec3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
