# 993. Uniqueness of a reflected rough equation with one scalar input

**Area:** Rough paths and constrained dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$, $`2<p<3`$, and let $`D\subset\mathbb R^d`$ be a bounded connected domain with smooth boundary. Let $`n`$ be its inward unit normal, $`f\in C_b^\infty(\mathbb R^d;\mathbb R^d)`$, and $`y_0\in\overline D`$. Given a continuous scalar path $`x:[0,1]\to\mathbb R`$ with $`x_0=0`$ and finite $`p`$-variation, use its canonical scalar enhancement

```math
\mathbf X_{s,t}=\left(x_t-x_s,\frac12(x_t-x_s)^2\right).
```

Does the normally reflected equation

```math
Y_t=y_0+\int_0^t f(Y_s)\,d\mathbf X_s+K_t,
\qquad Y_t\in\overline D,
\qquad K_0=0,
\qquad dK_t=n(Y_t)\,d|K|_t
```

have at most one solution pair $`(Y,K)`$? Here $`K`$ is continuous and has bounded variation; its variation measure is supported on $`\{t:Y_t\in\partial D\}`$. The continuous path $`Y`$ has finite $`p`$-variation and is controlled by $`x`$ with derivative $`f(Y)`$: the remainder $`Y_t-Y_s-f(Y_s)(x_t-x_s)`$ has finite $`p/2`$-variation. The integral is the usual controlled rough integral, obtained from compensated sums

```math
\sum_{[s,t]\in\mathcal P}
\left(f(Y_s)(x_t-x_s)+\frac12 Df(Y_s)f(Y_s)(x_t-x_s)^2\right).
```

There is one scalar input and no independent drift or time channel. Zeros and boundary tangencies of $`f`$ are allowed. This is the smooth bounded-domain, step-two part of the broader scalar-driver question in the source.

Uniqueness for a one-dimensional **state** is known even with several driving signals. The present question instead has a multidimensional state and a scalar driver. The known multidimensional counterexample uses both a rough scalar signal and an independent bounded-variation input, including in its fixed-time-drift version.

## Application

A state constrained by a hard wall can be driven by one irregular control or one external noise realization. Uniqueness would ensure that the prescribed input and initial state determine a single trajectory under normal reflection.

## References

1. P. Gassiat, *Non-uniqueness for reflected rough differential equations*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques **57**(3) (2021), 1369–1387. [DOI](https://doi.org/10.1214/20-AIHP1121), [primary preprint v2](https://arxiv.org/pdf/2001.11914v2). Remark 2.7(3), PDF p. 6 and its referee footnote, explicitly leave the scalar-driver case open; Assertion $`(A)_{d,m,p}`$ is on PDF p. 2.
2. S. Aida, *Rough Differential Equations Containing Path-Dependent Bounded Variation Terms*, Journal of Theoretical Probability **37** (2024), 2130–2183. [Published text](https://doi.org/10.1007/s10959-024-01319-3). Remark 2.8(6) distinguishes state dimension from driver dimension; Definition 5.5 and Theorem 5.6 give the nearby existence theory.

## Status review


**Known cases:** There is one scalar rough input with its canonical enhancement and no independent drift channel. The known multidimensional nonuniqueness uses a second bounded-variation signal; one-dimensional-state uniqueness is also different.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

There is one scalar rough input with its canonical enhancement and no independent drift channel. The known multidimensional nonuniqueness uses a second bounded-variation signal; one-dimensional-state uniqueness is also different.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Searches and selected current primary comparisons on 17 October 2026 located no matching resolution. All 22 pages and both figures of the pinned Gassiat v2 were read; parity with the 19-page published version has not been checked. Selected passages of Aida’s 2024 paper were read. The AIM and OpenAI announcement snapshots and existing FURTHER category pages had no equivalent target under the recorded comparisons.

A separate primary scope audit checked the solution class, controlled integral, normal-reflection measure and scalar-input distinction. The complete Prove2Me listing-description comparison returned 74 Skorokhod contexts; every returned context was reviewed, with exact overlaps merged without dropping text. They concern topology, stopping-time embeddings, prescribed-input queueing reflection or other stochastic models, rather than the displayed equation. No matching announcement was located.

The displayed enhancement is weakly geometric; no assumption that every finite-variation-norm approximation can be taken smooth in the exact $`p`$-variation topology is needed. Current searches and selected later theorem comparisons are bounded and do not certify every external proof. See the [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/scalar-reflected-rde-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-reflected-rde-review.json) and [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/scalar-reflected-rde-prove2-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0265708709c26efe**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
