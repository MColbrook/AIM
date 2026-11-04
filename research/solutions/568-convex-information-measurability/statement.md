# 568. A linear information bound for arbitrary convex model classes

**Area:** Information-based complexity and optimal recovery
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-03

## Problem statement

Let $`X,Y`$ be real Banach spaces, let $`S:X\to Y`$ be bounded and linear, and let $`F\subset X`$ be nonempty, bounded and convex. Symmetry of $`F`$ is not assumed. For $`m\ge0`$, set

```math
e_m^{\mathrm{det,non}}(S,F)
=\inf_{L_1,\ldots,L_m\in X',\;\Phi:\mathbb R^m\to Y}
\sup_{f\in F}\|Sf-\Phi(L_1f,\ldots,L_mf)\|_Y.
```

Here $`X'`$ is the continuous dual, and the deterministic reconstruction is unrestricted.

A randomized algorithm may choose its next functional in $`X'`$ using its random seed and the preceding measured values. Every realization uses at most $`n`$ measurements on every input. Its error is

```math
\sup_{f\in F}\mathbb E_\omega\|Sf-A_\omega(f)\|_Y,
```

and $`e_n^{\mathrm{ran}}(S,F)`$ is the infimum of these errors over all such algorithms and seed probability spaces. The error criterion is expected norm. To specify the source's measurability convention, give $`F`$ the metric $`d_F(f,g)=p_F(f-g)`$, where

```math
p_F(v)=\inf\{t>0:v\in t(F-F)\},\qquad v\in\mathrm{span}(F-F).
```

Require the real error map $`(f,\omega)\mapsto\|Sf-A_\omega(f)\|_Y`$ to be jointly measurable for the Borel sigma algebra of this metric and the seed sigma algebra. Boundedness and convexity make $`p_F`$ a norm on that span, unless the span is zero; in that trivial case take the one-point topology. [1, §2]

Does there exist an absolute constant $`C<\infty`$, independent of $`X,Y,S,F`$ and $`n`$, such that

```math
e_{2n}^{\mathrm{det,non}}(S,F)
\le Cn\,e_n^{\mathrm{ran}}(S,F)
\qquad(n\ge1)
```

for every such convex class? This is the nonsymmetric extension of the individual-budget question in [1, §6.1, Open problem 1]. It asks for this estimate at each budget, without a regular-decay assumption on the error sequence.

## Application

Convex prior classes arise when unknown functions are constrained to be nonnegative, monotone or convex. The question asks how much a fixed batch of linear measurements can lose compared with measurements chosen using randomization and feedback. It concerns information requirements for recovering a function or a linear quantity, without imposing a running-time guarantee. [1, §§1–2]

## References

1. David Krieg, Erich Novak and Mario Ullrich, *On the power of adaption and randomization*, Forum of Mathematics, Sigma **13** (2025), e152, 1–23. [Published article](https://doi.org/10.1017/fms.2025.10101), §2, pp. 4–5; Proposition 4.4, p.12; §6.1 Open problem 1, p.16.
2. Mario Ullrich, *On bounds between all s-numbers and widths of convex sets*, [arXiv:2608.05024v1](https://arxiv.org/abs/2608.05024v1), 5 August 2026. Theorem 7 and its definitions, pp.13–15; Remark 9, p.16. Current-status reference, not an arXiv-cutoff discovery source.

## Status review


**Known cases:** Ullrich's 2026 all-s-number result treats symmetric operator balls. Its nonsymmetric convex-set extension yields a linear factor for Hilbert targets and a larger factor in general; it does not supply the requested general Banach-target randomized-error estimate.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Literature check: 18 October 2026.** The published source explicitly asks the extension from symmetric to arbitrary convex classes. Its geometric-mean and polynomial-rate comparisons do not give the displayed individual-budget bound. [1, Theorems 1.1/5.1; §6.1]

The current preprint [2] announces a stronger pointwise width comparison that supplies the desired estimate for symmetric classes. It also supplies the desired linear bound for arbitrary convex classes when $`Y`$ is a Hilbert space. For general Banach target spaces, its Theorem 7 supplies an $`O(n^{3/2})`$ bound by combining it with [1, Proposition 4.4]. Remark 9 explains that the sharp $`n^{3/2}`$ comparison with Hilbert widths does not decide the corresponding comparison with the larger Bernstein widths. Thus that width example does not itself refute the displayed randomized-error inequality. The proofs of the entire current preprint have not been independently certified.

The solved AIM555 problem determines a maximal asymptotic gain from nonadaptive randomization on symmetric Banach unit balls. Its existence construction does not establish this universal bound for nonsymmetric classes. Continuous nonlinear measurements and continuous-decoder questions are also different algorithm classes.

Current announcement searches and all-status AIM/OpenAI/FURTHER comparisons found no matching complete solution. An independent selected-primary audit passed. All 186 cached catalogue pages were compared using six aliases; the sole returned context was an unrelated cone-optimization reference. Coordinator review passed at the recorded extents.

The [owner packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/nonsymmetric-individual-budget-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-nonsymmetric-individual-budget-review.json), [semantic comparison](../FURTHER_problems/_tracking/nonsymmetric-budget-duplicates-coordinator-2026-10-18.json), [catalogue receipt](../FURTHER_problems/_tracking/nonsymmetric-budget-catalogue-coordinator-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/nonsymmetric-budget-coordinator-review-2026-10-18.json) retain the source versions, scope and access limits.


### Online recheck, 2026-10-30

Ullrich's 2026 all-s-number result treats symmetric operator balls. Its nonsymmetric convex-set extension yields a linear factor for Hilbert targets and a larger factor in general; it does not supply the requested general Banach-target randomized-error estimate.

Comparators and current-status sources: [status source 1](https://arxiv.org/html/2608.05024); [status source 2](https://doi.org/10.1017/fms.2025.10101). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

### Announcement check, 3 November 2026

Krieg, Novak and Ullrich, [*On the power of adaption and randomization 2: Non-symmetric convex sets*](https://arxiv.org/pdf/2610.33733v1) (24 October 2026), Theorem 1.1, announce a $`27n`$ comparison at budget $`2n-1`$ for arbitrary convex classes and Banach targets. Section 1 additionally requires the adaptive decision rules and reconstruction to be jointly measurable on finite-dimensional affine slices. The local problem requires only joint measurability of the scalar error map. A bridge between those admissibility classes was not established, so the broader displayed problem remains partial. The new theorem is a matching bound for its stated model; its proof is unverified here. [Comparison](../research/solution-status-audit-2026-11-03/lane-b/568.json).

## Collection provenance

Promoted from retained further problem **FURTHER-6069eb14c3ea51cf** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
