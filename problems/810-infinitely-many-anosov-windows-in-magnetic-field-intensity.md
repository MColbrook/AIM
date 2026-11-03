# 810. Infinitely many Anosov windows in magnetic-field intensity

**Area:** Magnetic dynamics / bifurcation theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a closed connected oriented smooth surface $`M`$ of genus at
least two and a smooth Riemannian metric $`g`$ for which the following set has
infinitely many connected components?

For each constant $`\lambda\ge0`$, let $`\varphi_t^\lambda`$ be the flow on the
unit tangent bundle $`SM`$ determined by

```math
\nabla_{\dot\gamma}\dot\gamma=\lambda J\dot\gamma,
\qquad |\dot\gamma|_g=1,
```

where $`J`$ rotates tangent vectors by $`\pi/2`$ according to the orientation.
This is the magnetic flow whose field is $`\lambda`$ times the area form of
the **same fixed metric** $`g`$. Define

```math
\mathcal A_g=\{\lambda\in[0,\infty):\varphi^\lambda
\text{ is an Anosov flow on }SM\}.
```

Here Anosov means that there are continuous invariant line bundles
$`E^s_\lambda,E^u_\lambda`$ and constants $`C_\lambda,c_\lambda>0`$ with

```math
T(SM)=\mathbb R F_\lambda\oplus E^s_\lambda\oplus E^u_\lambda,
\qquad
\|d\varphi_t^\lambda|_{E^s_\lambda}\|\le C_\lambda e^{-c_\lambda t},
\qquad
\|d\varphi_{-t}^\lambda|_{E^u_\lambda}\|\le C_\lambda e^{-c_\lambda t}
\quad(t\ge0),
```

where $`F_\lambda`$ generates the flow. The constants may depend on
$`\lambda`$. The question concerns infinitely many windows for **one**
metric; choosing a different metric for each prescribed finite number
of windows does not answer it.

## Application

This is a question about repeated loss and recovery of uniform chaotic
motion as the strength of a homogeneous magnetic field is increased.
It tests how complicated a phase diagram can be even though the parameter
enters the charged-particle equation linearly.

## References

1. K. Burns and G. P. Paternain, *Anosov magnetic flows, critical values and
   topological entropy*, **Nonlinearity 15** (2002), 281–314,
   [DOI](https://doi.org/10.1088/0951-7715/15/2/305),
   [author manuscript](https://sites.math.northwestern.edu/~burns/papers/magflow/final311.pdf).
   Section 1.2 defines Anosov intervals; the end of Section 7, manuscript
   pp.30–31, distinguishes arbitrarily many finite alternations from the
   unknown infinite case.

## Status review


**Known cases:** Arbitrarily many Anosov/non-Anosov alternations across a sequence of different metrics do not supply infinitely many windows for a single fixed metric. Results under nonpositive magnetic curvature address only restricted intensity ranges.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Arbitrarily many Anosov/non-Anosov alternations across a sequence of different metrics do not supply infinitely many windows for a single fixed metric. Results under nonpositive magnetic curvature address only restricted intensity ranges.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Burns–Paternain construct arbitrarily many finite alternations, including
examples with negative Gaussian curvature and magnetic field proportional
to area. They explicitly leave arranging infinitely many alternations
unresolved. Structural stability makes $`\mathcal A_g`$ open, and their
critical-value bound makes it bounded; neither property implies finitely
many connected components.

The later constant-intensity surface results reviewed here impose
nonpositive magnetic curvature, a condition covering only part of the
intensity range. Results about infinitely many invariant hypersurfaces
of a single flow concern a different question.

The [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/infinite-anosov-intervals-review.json)
records current searches and review limits. The complete 40-page author
edition has been read; the 34-page final journal body has not been compared.


The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-infinite-anosov-intervals-review.json), [catalogue comparison](../FURTHER_problems/_tracking/infinite-anosov-catalogue-coordinator-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/infinite-anosov-coordinator-review-2026-10-18.json) passed at their recorded extents. All186current listing pages returned no contexts under the six candidate aliases; complete mission proof bodies remain unreviewed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8068458e5d850a2e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
